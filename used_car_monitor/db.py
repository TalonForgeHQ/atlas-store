"""SQLite store for the used-car deal monitor.

Schema design:
- briefs: one row per acquisition target ("Tacoma TRD 2016-2020 <$25k all-in, Austin 100mi")
- listings: dedupe key = (source, listing_id). Fingerprint keeps re-imports stable
            when IDs change (some Marketplaces rotate IDs).
- valuations: many rows per listing, one per source, with timestamp
- risk_flags: many rows per listing, with severity
- alerts: one row per alert we ever sent (idempotency: never send same alert twice)
- approvals: human approve/decline a candidate before any outbound contact
- audit_log: every state change for a listing (status, source, price, valuation,
              risk, alert, approval)
"""

from __future__ import annotations

import json
import os
import sqlite3
import time
import hashlib
from contextlib import contextmanager
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable, Optional


SCHEMA = """
CREATE TABLE IF NOT EXISTS briefs (
    id            INTEGER PRIMARY KEY AUTOINCREMENT,
    name          TEXT NOT NULL UNIQUE,
    geography     TEXT NOT NULL,           -- "Austin, TX, 100mi"
    target_json   TEXT NOT NULL,           -- {"make":"Toyota","model":"Tacoma","year_min":2016,"year_max":2020,"trim":"TRD"}
    max_all_in    REAL NOT NULL,           -- hard all-in budget cap
    min_discount  REAL NOT NULL DEFAULT 0.15,
    min_confidence TEXT NOT NULL DEFAULT 'low',
    sources_json  TEXT NOT NULL,           -- ["file","community_mcp"]
    created_at    TEXT NOT NULL DEFAULT (datetime('now')),
    active        INTEGER NOT NULL DEFAULT 1
);

CREATE TABLE IF NOT EXISTS listings (
    id              INTEGER PRIMARY KEY AUTOINCREMENT,
    source          TEXT NOT NULL,
    listing_id      TEXT NOT NULL,
    url             TEXT,
    first_seen_at   TEXT NOT NULL,
    last_seen_at    TEXT NOT NULL,
    status          TEXT NOT NULL DEFAULT 'new',
    -- vehicle identity
    year            INTEGER,
    make            TEXT,
    model           TEXT,
    trim            TEXT,
    vin             TEXT,
    mileage         INTEGER,
    drivetrain      TEXT,
    transmission    TEXT,
    -- listing facts
    ask_price       REAL,
    location        TEXT,
    seller_name     TEXT,
    seller_type     TEXT,                 -- private|dealer|unknown
    seller_profile  TEXT,
    title_claim     TEXT,                 -- clean|salvage|rebuilt|unknown
    description     TEXT,
    photos_json     TEXT,                 -- JSON array of URLs
    -- derived
    fingerprint     TEXT NOT NULL,        -- sha256 of normalized identity + price + location
    brief_id        INTEGER,
    FOREIGN KEY (brief_id) REFERENCES briefs(id),
    UNIQUE(source, listing_id)
);
CREATE INDEX IF NOT EXISTS idx_listings_status ON listings(status);
CREATE INDEX IF NOT EXISTS idx_listings_brief ON listings(brief_id);
CREATE INDEX IF NOT EXISTS idx_listings_fingerprint ON listings(fingerprint);

CREATE TABLE IF NOT EXISTS valuations (
    id              INTEGER PRIMARY KEY AUTOINCREMENT,
    listing_id      INTEGER NOT NULL,
    source          TEXT NOT NULL,        -- "kbb","edmunds","jd_power","comps_local","heuristic"
    lookup_at       TEXT NOT NULL,
    low             REAL,
    midpoint        REAL,
    high            REAL,
    confidence      TEXT NOT NULL,        -- low|medium|high
    raw_json        TEXT,
    notes           TEXT,
    FOREIGN KEY (listing_id) REFERENCES listings(id) ON DELETE CASCADE,
    UNIQUE(listing_id, source, lookup_at)
);
CREATE INDEX IF NOT EXISTS idx_valuations_listing ON valuations(listing_id);

CREATE TABLE IF NOT EXISTS risk_flags (
    id              INTEGER PRIMARY KEY AUTOINCREMENT,
    listing_id      INTEGER NOT NULL,
    severity        TEXT NOT NULL,        -- info|warn|hard_stop
    code            TEXT NOT NULL,        -- "vin_mismatch","recall_open","price_too_good","..."
    message         TEXT NOT NULL,
    evidence_json   TEXT,
    created_at      TEXT NOT NULL DEFAULT (datetime('now')),
    FOREIGN KEY (listing_id) REFERENCES listings(id) ON DELETE CASCADE
);
CREATE INDEX IF NOT EXISTS idx_risk_listing ON risk_flags(listing_id);

CREATE TABLE IF NOT EXISTS alerts (
    id              INTEGER PRIMARY KEY AUTOINCREMENT,
    listing_id      INTEGER NOT NULL,
    brief_id        INTEGER NOT NULL,
    kind            TEXT NOT NULL,        -- "new_flag","price_drop","status_change"
    sent_at         TEXT NOT NULL DEFAULT (datetime('now')),
    dedupe_key      TEXT NOT NULL,        -- stable per (listing, brief, kind)
    payload_json    TEXT NOT NULL,
    delivered       INTEGER NOT NULL DEFAULT 1,
    FOREIGN KEY (listing_id) REFERENCES listings(id) ON DELETE CASCADE,
    FOREIGN KEY (brief_id) REFERENCES briefs(id) ON DELETE CASCADE,
    UNIQUE(dedupe_key)
);
CREATE INDEX IF NOT EXISTS idx_alerts_listing ON alerts(listing_id);

CREATE TABLE IF NOT EXISTS approvals (
    id              INTEGER PRIMARY KEY AUTOINCREMENT,
    listing_id      INTEGER NOT NULL,
    decision        TEXT NOT NULL,        -- "approve_first_message"|"decline"|"ask_for_vin"|"approve_offer_max:NNNN"
    decided_by      TEXT NOT NULL,
    decided_at      TEXT NOT NULL DEFAULT (datetime('now')),
    note            TEXT,
    FOREIGN KEY (listing_id) REFERENCES listings(id) ON DELETE CASCADE,
    UNIQUE(listing_id, decision, decided_by)
);

CREATE TABLE IF NOT EXISTS audit_log (
    id              INTEGER PRIMARY KEY AUTOINCREMENT,
    at              TEXT NOT NULL DEFAULT (datetime('now')),
    listing_id      INTEGER,
    event           TEXT NOT NULL,
    details_json    TEXT
);
CREATE INDEX IF NOT EXISTS idx_audit_listing ON audit_log(listing_id);
"""


def default_db_path() -> Path:
    """Default DB location: <project>/used_car_monitor/data/monitor.db"""
    here = Path(__file__).resolve().parent
    return here / "data" / "monitor.db"


def connect(db_path: Optional[Path] = None) -> sqlite3.Connection:
    """Open a connection with foreign keys on and WAL mode for safer concurrent writes."""
    path = Path(db_path) if db_path else default_db_path()
    path.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(str(path), timeout=30.0, isolation_level=None)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON;")
    conn.execute("PRAGMA journal_mode = WAL;")
    conn.execute("PRAGMA synchronous = NORMAL;")
    return conn


def init_db(conn: sqlite3.Connection) -> None:
    """Create schema if missing."""
    conn.executescript(SCHEMA)


@contextmanager
def tx(conn: sqlite3.Connection):
    """Manual transaction context. Use for any multi-statement write."""
    conn.execute("BEGIN")
    try:
        yield
        conn.execute("COMMIT")
    except Exception:
        conn.execute("ROLLBACK")
        raise


def fingerprint(payload: dict[str, Any]) -> str:
    """Stable dedupe fingerprint when listing IDs change.

    Inputs: year, make, model, trim, ask_price (rounded to $50), location (lowercased).
    Two listings with the same fingerprint are almost certainly the same car.
    """
    def _n(v: Any) -> str:
        if v is None:
            return ""
        return str(v).strip().lower()

    price = float(payload.get("ask_price") or 0)
    # round price to nearest $50 so small re-prices don't split the record
    bucket = int(round(price / 50.0) * 50)
    parts = [
        _n(payload.get("year")),
        _n(payload.get("make")),
        _n(payload.get("model")),
        _n(payload.get("trim")),
        str(bucket),
        _n(payload.get("location")),
    ]
    raw = "|".join(parts)
    return hashlib.sha256(raw.encode("utf-8")).hexdigest()[:32]


def audit(conn: sqlite3.Connection, event: str, listing_id: Optional[int] = None,
          details: Optional[dict[str, Any]] = None) -> None:
    conn.execute(
        "INSERT INTO audit_log(listing_id, event, details_json) VALUES (?, ?, ?)",
        (listing_id, event, json.dumps(details or {}, default=str)),
    )


def upsert_listing(conn: sqlite3.Connection, raw: dict[str, Any]) -> tuple[int, bool]:
    """Insert or update a listing. Returns (id, was_inserted)."""
    src = raw["source"]
    lid = raw["listing_id"]
    now = raw.get("now") or time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    fp = fingerprint(raw)

    row = conn.execute(
        "SELECT id, last_seen_at FROM listings WHERE source = ? AND listing_id = ?",
        (src, lid),
    ).fetchone()

    if row is None:
        cur = conn.execute(
            """
            INSERT INTO listings(
                source, listing_id, url, first_seen_at, last_seen_at, status,
                year, make, model, trim, vin, mileage, drivetrain, transmission,
                ask_price, location, seller_name, seller_type, seller_profile,
                title_claim, description, photos_json, fingerprint
            ) VALUES (?, ?, ?, ?, ?, 'new',
                      ?, ?, ?, ?, ?, ?, ?, ?,
                      ?, ?, ?, ?, ?,
                      ?, ?, ?, ?)
            """,
            (
                src, lid, raw.get("url"), now, now,
                raw.get("year"), raw.get("make"), raw.get("model"), raw.get("trim"),
                raw.get("vin"), raw.get("mileage"), raw.get("drivetrain"),
                raw.get("transmission"),
                raw.get("ask_price"), raw.get("location"),
                raw.get("seller_name"), raw.get("seller_type"),
                raw.get("seller_profile"),
                raw.get("title_claim", "unknown"), raw.get("description", ""),
                json.dumps(raw.get("photos") or []), fp,
            ),
        )
        new_id = cur.lastrowid
        audit(conn, "listing.inserted", new_id, {"source": src, "listing_id": lid})
        return new_id, True

    # existing - update fields, advance last_seen_at
    existing_id = row["id"]
    conn.execute(
        """
        UPDATE listings SET
            url = COALESCE(?, url),
            last_seen_at = ?,
            year = COALESCE(?, year),
            make = COALESCE(?, make),
            model = COALESCE(?, model),
            trim = COALESCE(?, trim),
            vin = COALESCE(?, vin),
            mileage = COALESCE(?, mileage),
            drivetrain = COALESCE(?, drivetrain),
            transmission = COALESCE(?, transmission),
            ask_price = COALESCE(?, ask_price),
            location = COALESCE(?, location),
            seller_name = COALESCE(?, seller_name),
            seller_type = COALESCE(?, seller_type),
            seller_profile = COALESCE(?, seller_profile),
            title_claim = COALESCE(?, title_claim),
            description = COALESCE(?, description),
            photos_json = COALESCE(?, photos_json)
        WHERE id = ?
        """,
        (
            raw.get("url"), now,
            raw.get("year"), raw.get("make"), raw.get("model"), raw.get("trim"),
            raw.get("vin"), raw.get("mileage"), raw.get("drivetrain"),
            raw.get("transmission"),
            raw.get("ask_price"), raw.get("location"),
            raw.get("seller_name"), raw.get("seller_type"),
            raw.get("seller_profile"), raw.get("title_claim"),
            raw.get("description"),
            json.dumps(raw.get("photos")) if raw.get("photos") is not None else None,
            existing_id,
        ),
    )
    audit(conn, "listing.updated", existing_id, {"source": src, "listing_id": lid})
    return existing_id, False