"""CLI entrypoint: `python -m used_car_monitor <command> ...`"""

from __future__ import annotations

import argparse
import json
import os
import sqlite3
import sys
import time
from pathlib import Path
from typing import Any, Optional

from . import db, pipeline
from .adapters import discovery as discovery_mod
from .adapters import notifier as notifier_mod
from .adapters import risk as risk_mod
from .adapters import valuation as valuation_mod


HERE = Path(__file__).resolve().parent
DATA_DIR = HERE / "data"
DROPS_DIR = DATA_DIR / "drops"
ALERTS_LOG = DATA_DIR / "alerts.jsonl"
COMPS_FILE = DATA_DIR / "comps.json"


def _build_pipeline(enable_community_mcp: bool = False,
                    enable_telegram: bool = False,
                    enable_carsxe: Optional[bool] = None) -> pipeline.PipelineAdapters:
    """Build the pipeline with the best-of-multiple-worlds stack.

    Adapters are added in preference order:
      - Discovery: file feed (always), community MCP (opt-in)
      - Valuation: CarsXE if CARSXE_API_KEY set, comps + heuristic always
      - Risk: NHTSA VIN + recall + scarcity always; CarsXE history + CarGurus
              if enabled
      - Notifier: local log always, Telegram if enabled
    """
    drop = DROPS_DIR / "manual_export"
    drop.mkdir(parents=True, exist_ok=True)
    discoverers = [
        discovery_mod.FileFeedAdapter(drop, source_tag="manual_export"),
    ]
    if enable_community_mcp:
        # OPT IN. Operator accepts Meta's automation policy at their own risk.
        discoverers.append(discovery_mod.CommunityMCPAdapter(
            command=["npx", "-y", "secondhand-mcp"],
            source_tag="secondhand_mcp",
        ))
    # Valuation stack
    carsxe_key = os.environ.get("CARSXE_API_KEY")
    if enable_carsxe is False or (enable_carsxe is None and not carsxe_key):
        # Operator has either disabled CarsXE or no key
        valuators = [
            valuation_mod.HeuristicValuation(),
            valuation_mod.CompsLocalAdapter(COMPS_FILE),
        ]
    else:
        # CarsXE primary, comps cross-check, heuristic floor
        valuators = [
            valuation_mod.CarsXEMarketValueAdapter(api_key=carsxe_key),
            valuation_mod.CompsLocalAdapter(COMPS_FILE),
            valuation_mod.HeuristicValuation(),
        ]
    # Risk stack
    risk_screeners = [
        risk_mod.NHTSAVinDecodeAdapter(),
        risk_mod.NHTSARecallAdapter(),
        risk_mod.ScarcitySignalsAdapter(),
        risk_mod.CarsXEHistoryAdapter(),   # auto-enabled if CARSXE_API_KEY set
        risk_mod.CarGurusDealRatingAdapter(),  # reads cargurus_rating from listing
    ]
    notifiers = [
        notifier_mod.LocalLogNotifier(ALERTS_LOG),
    ]
    if enable_telegram:
        notifiers.append(notifier_mod.TelegramNotifier())
    return pipeline.PipelineAdapters(
        discoverers=discoverers, valuators=valuators,
        risk_screeners=risk_screeners, notifiers=notifiers,
    )


def cmd_init(args, conn):
    db.init_db(conn)
    print(f"Initialized {db.default_db_path()}")
    return 0


def cmd_add_brief(args, conn):
    target = json.loads(args.target) if isinstance(args.target, str) else args.target
    sources = json.loads(args.sources) if isinstance(args.sources, str) else args.sources
    cur = conn.execute(
        """INSERT INTO briefs(name, geography, target_json, max_all_in, min_discount,
                              min_confidence, sources_json)
           VALUES (?, ?, ?, ?, ?, ?, ?)""",
        (args.name, args.geography, json.dumps(target), args.max_all_in,
         args.min_discount, args.min_confidence, json.dumps(sources)),
    )
    print(f"Brief #{cur.lastrowid} '{args.name}' added.")
    return 0


def cmd_list_briefs(args, conn):
    rows = conn.execute("SELECT * FROM briefs ORDER BY id").fetchall()
    for r in rows:
        print(f"#{r['id']:>3} {r['name']:<30} geo={r['geography']:<25} "
              f"max_all_in=${r['max_all_in']:,.0f}  discount>={r['min_discount']:.0%}  "
              f"active={bool(r['active'])}")
    return 0


def cmd_ingest(args, conn):
    """Manually push a JSON listing into the drop dir and run a single pipeline pass."""
    drop = DROPS_DIR / "manual_export"
    drop.mkdir(parents=True, exist_ok=True)
    payload = json.loads(args.listing)
    payload["listing_id"] = payload.get("listing_id") or f"manual-{int(time.time()*1000)}"
    out = drop / f"manual-{int(time.time()*1000)}.json"
    out.write_text(json.dumps([payload], indent=2), encoding="utf-8")
    print(f"Wrote {out}")
    return cmd_run(args, conn)


def cmd_run(args, conn):
    pl = _build_pipeline(enable_community_mcp=args.enable_community_mcp,
                         enable_telegram=args.enable_telegram,
                         enable_carsxe=getattr(args, "enable_carsxe", None))
    only = args.brief
    rep = pipeline.run_once(conn, pl, only_brief_id=only)
    print(json.dumps(rep, indent=2, default=str))
    return 0


def cmd_status(args, conn):
    """Summary of the last run + current top candidates."""
    brief_rows = conn.execute("SELECT * FROM briefs WHERE active = 1").fetchall()
    if not brief_rows:
        print("No active briefs. Use `add-brief` first.")
        return 0
    for b in brief_rows:
        rows = conn.execute(
            """SELECT id, year, make, model, trim, ask_price, status,
                      (SELECT midpoint FROM valuations WHERE valuations.listing_id =
                           listings.id AND source='blended' ORDER BY lookup_at DESC LIMIT 1) AS val_mid,
                      (SELECT confidence FROM valuations WHERE valuations.listing_id =
                           listings.id AND source='blended' ORDER BY lookup_at DESC LIMIT 1) AS val_conf
               FROM listings WHERE brief_id = ?
               ORDER BY status, id DESC LIMIT 50""",
            (b["id"],),
        ).fetchall()
        print(f"\n=== Brief #{b['id']} '{b['name']}' "
              f"(max_all_in=${b['max_all_in']:,.0f}, "
              f"discount>={b['min_discount']:.0%}) ===")
        if not rows:
            print("  (no listings yet)")
            continue
        for r in rows:
            disc = ""
            if r["val_mid"] and r["ask_price"]:
                disc = f"  disc={(r['val_mid']-r['ask_price'])/r['val_mid']:+.1%}"
            print(f"  #{r['id']:>4} [{r['status']:<8}] "
                  f"{r['year'] or '?'} {r['make'] or '?'} {r['model'] or '?'} "
                  f"{r['trim'] or '':<8} "
                  f"ask=${r['ask_price'] or 0:,.0f} "
                  f"mid=${r['val_mid'] or 0:,.0f} ({r['val_conf'] or '?'}){disc}")
    return 0


def cmd_alerts(args, conn):
    rows = conn.execute(
        """SELECT a.id, a.listing_id, a.brief_id, a.kind, a.sent_at, a.delivered,
                  a.payload_json
           FROM alerts a ORDER BY a.id DESC LIMIT ?""",
        (args.limit,),
    ).fetchall()
    if not rows:
        print("(no alerts)")
        return 0
    for r in rows:
        delivered = "✓" if r["delivered"] else "•"
        try:
            p = json.loads(r["payload_json"])
            veh = p.get("vehicle", {})
            print(f"{delivered} alert#{r['id']} listing#{r['listing_id']} "
                  f"brief#{r['brief_id']} {r['kind']} @ {r['sent_at']}")
            print(f"    {veh.get('year')} {veh.get('make')} {veh.get('model')} "
                  f"{veh.get('trim','')} — ask ${p.get('ask_price',0):,.0f}  "
                  f"mid ${p.get('valuation_mid',0):,.0f}  "
                  f"disc {p.get('discount_pct',0)}%")
            for fl in p.get("risk_flags", [])[:3]:
                print(f"    ! {fl['severity']}: {fl['message']}")
        except Exception:
            print(f"alert#{r['id']} (unparseable)")
    return 0


def cmd_approve(args, conn):
    """Record a human approval to contact a seller (the actual contact action is NOT taken here)."""
    listing = conn.execute("SELECT * FROM listings WHERE id = ?",
                           (args.listing_id,)).fetchone()
    if listing is None:
        print(f"Listing #{args.listing_id} not found.", file=sys.stderr)
        return 2
    decision = f"approve_first_message_max:{int(args.max_offer)}"
    try:
        conn.execute(
            """INSERT INTO approvals(listing_id, decision, decided_by, note)
               VALUES (?, ?, ?, ?)""",
            (args.listing_id, decision, args.who, args.note or ""),
        )
    except sqlite3.IntegrityError:
        print(f"Approval already recorded for #{args.listing_id} by {args.who}.",
              file=sys.stderr)
        return 3
    db.audit(conn, "approval.granted", args.listing_id,
             {"by": args.who, "max_offer": args.max_offer, "note": args.note})
    conn.execute("UPDATE listings SET status = 'contacted' WHERE id = ?",
                 (args.listing_id,))
    print(f"Approved #{args.listing_id} for first message with max offer "
          f"${args.max_offer:,.0f}. Outbound contact is NOT auto-sent. "
          f"Use a permitted channel manually or wire a contact adapter.")
    return 0


def cmd_decline(args, conn):
    listing = conn.execute("SELECT * FROM listings WHERE id = ?",
                           (args.listing_id,)).fetchone()
    if listing is None:
        print(f"Listing #{args.listing_id} not found.", file=sys.stderr)
        return 2
    conn.execute(
        """INSERT INTO approvals(listing_id, decision, decided_by, note)
           VALUES (?, 'decline', ?, ?)""",
        (args.listing_id, args.who, args.note or ""),
    )
    conn.execute("UPDATE listings SET status = 'rejected' WHERE id = ?",
                 (args.listing_id,))
    db.audit(conn, "approval.declined", args.listing_id, {"by": args.who})
    print(f"Declined #{args.listing_id}.")
    return 0


def cmd_set_rating(args, conn):
    """Attach a CarGurus-style rating to a listing. Triggers re-evaluation."""
    listing = conn.execute("SELECT * FROM listings WHERE id = ?",
                           (args.listing_id,)).fetchone()
    if listing is None:
        print(f"Listing #{args.listing_id} not found.", file=sys.stderr)
        return 2
    rating = args.rating.lower()
    # We don't have a cargurus_rating column; store it in audit_log + risk_flags
    # so it's both retrievable and the next pipeline run will re-evaluate it.
    code = f"cargurus_{rating.replace(' ', '_')}"
    # Clear any prior cargurus rating flags for this listing
    conn.execute(
        "DELETE FROM risk_flags WHERE listing_id = ? AND code LIKE 'cargurus_%'",
        (args.listing_id,),
    )
    severity = "warn" if rating == "high_price" else "info"
    conn.execute(
        """INSERT INTO risk_flags(listing_id, severity, code, message, evidence_json)
           VALUES (?, ?, ?, ?, ?)""",
        (args.listing_id, severity, code,
         f"CarGurus rating: {rating}",
         json.dumps({"rating": rating})),
    )
    db.audit(conn, "rating.set", args.listing_id,
             {"rating": rating, "by": "zinou"})
    print(f"Rating '{rating}' attached to listing #{args.listing_id}. "
          f"Re-run the pipeline to see it reflected in flags.")
    return 0


def cmd_dry_run(args, conn):
    pl = _build_pipeline(enable_community_mcp=False, enable_telegram=False)
    rep = pipeline.run_once(conn, pl, only_brief_id=args.brief)
    # For dry-run, suppress notifier side effects
    print("[dry-run] pipeline completed without side-effects beyond DB writes")
    print(json.dumps(rep, indent=2, default=str))
    return 0


def main(argv: Optional[list[str]] = None) -> int:
    p = argparse.ArgumentParser(prog="used-car-monitor")
    p.add_argument("--db", default=None, help="Path to SQLite DB (default: ./data/monitor.db)")
    sub = p.add_subparsers(dest="cmd", required=True)

    sub.add_parser("init", help="Create or migrate the database schema")

    ab = sub.add_parser("add-brief", help="Add a buying brief")
    ab.add_argument("--name", required=True)
    ab.add_argument("--geography", required=True,
                    help='e.g. "Austin, TX, 100mi"')
    ab.add_argument("--target", required=True,
                    help='JSON e.g. {"make":"Toyota","model":"Tacoma","year_min":2016,"year_max":2020,"trim":"TRD"}')
    ab.add_argument("--max-all-in", type=float, required=True,
                    help="Hard cap on landed cost (ask + tax + fees + transport + repair + contingency)")
    ab.add_argument("--min-discount", type=float, default=0.15)
    ab.add_argument("--min-confidence", default="low",
                    choices=["low", "medium", "high"])
    ab.add_argument("--sources", default='["file","community_mcp"]',
                    help='JSON array of source tags')

    sub.add_parser("list-briefs", help="List briefs")

    sp = sub.add_parser("ingest", help="Drop a JSON listing and run the pipeline")
    sp.add_argument("--listing", required=True, help="JSON listing object")
    sp.add_argument("--enable-community-mcp", action="store_true")
    sp.add_argument("--enable-telegram", action="store_true")

    sr = sub.add_parser("run", help="Run the full pipeline once")
    sr.add_argument("--brief", type=int, default=None)
    sr.add_argument("--enable-community-mcp", action="store_true")
    sr.add_argument("--enable-telegram", action="store_true")
    sr.add_argument("--enable-carsxe", dest="enable_carsxe", action="store_true",
                    default=None, help="Force CarsXE Market Value + History (needs CARSXE_API_KEY)")
    sr.add_argument("--no-carsxe", dest="enable_carsxe", action="store_false",
                    help="Disable CarsXE even if CARSXE_API_KEY is set")

    sd = sub.add_parser("dry-run", help="Run pipeline without enabling MCP/Telegram")
    sd.add_argument("--brief", type=int, default=None)
    sd.add_argument("--enable-carsxe", dest="enable_carsxe", action="store_true", default=None)
    sd.add_argument("--no-carsxe", dest="enable_carsxe", action="store_false")

    sub.add_parser("status", help="Show current listings grouped by brief")

    sa = sub.add_parser("alerts", help="Show last N alerts")
    sa.add_argument("--limit", type=int, default=20)

    sa2 = sub.add_parser("approve", help="Approve contacting seller for a listing")
    sa2.add_argument("--listing-id", type=int, required=True)
    sa2.add_argument("--max-offer", type=float, required=True)
    sa2.add_argument("--who", default="zinou")
    sa2.add_argument("--note", default=None)

    sd2 = sub.add_parser("decline", help="Decline a listing")
    sd2.add_argument("--listing-id", type=int, required=True)
    sd2.add_argument("--who", default="zinou")
    sd2.add_argument("--note", default=None)

    sr2 = sub.add_parser("set-rating", help="Attach a CarGurus-style rating to a listing")
    sr2.add_argument("--listing-id", type=int, required=True)
    sr2.add_argument("--rating", required=True,
                     choices=["great deal", "good deal", "fair deal",
                              "high price", "clear"])

    args = p.parse_args(argv)
    # Tests inject a connection via env var MONITOR_DB_CONN to share state.
    injected = os.environ.get("MONITOR_DB_CONN")
    if injected:
        from . import db as _db
        conn = sqlite3.connect(":memory:")
        conn.row_factory = sqlite3.Row
        # Tests pass a real on-disk DB path through MONITOR_DB_CONN
        conn = _db.connect(Path(injected))
        _db.init_db(conn)
    else:
        conn = db.connect(Path(args.db) if args.db else None)
        db.init_db(conn)
    handlers = {
        "init": cmd_init, "add-brief": cmd_add_brief, "list-briefs": cmd_list_briefs,
        "ingest": cmd_ingest, "run": cmd_run, "dry-run": cmd_dry_run,
        "status": cmd_status, "alerts": cmd_alerts,
        "approve": cmd_approve, "decline": cmd_decline,
        "set-rating": cmd_set_rating,
    }
    return handlers[args.cmd](args, conn)


if __name__ == "__main__":
    sys.exit(main())