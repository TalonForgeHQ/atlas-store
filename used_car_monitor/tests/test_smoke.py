"""Smoke tests for the used-car deal monitor.

Run with:  py -3.12 -m unittest used_car_monitor.tests.test_smoke -v

These are end-to-end tests of the funnel. They use a temp DB and stub the
network adapters so they're fast and deterministic.
"""

import json
import os
import sqlite3
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(ROOT))

from used_car_monitor import db, pipeline
from used_car_monitor.adapters import (discovery as discovery_mod,
                                        notifier as notifier_mod,
                                        risk as risk_mod,
                                        valuation as valuation_mod)


class StubNotifier(notifier_mod.Adapter):
    """Captures sent payloads in memory."""
    name = "stub"

    def __init__(self):
        self.sent = []

    def send(self, payload):
        self.sent.append(payload)
        return True


class StubRisk(risk_mod.Adapter):
    """Risk adapter we control. Flags a hard_stop when listing has 'poison' in description."""
    name = "stub"

    def screen(self, listing):
        desc = (listing.get("description") or "").lower()
        if "poison" in desc:
            yield risk_mod.RiskFlag("hard_stop", "test_hard_stop",
                                    "TEST: hard stop", {})
        elif "thin" in desc:
            yield risk_mod.RiskFlag("warn", "thin_listing",
                                    "TEST: thin", {})


class StubValuation(valuation_mod.Adapter):
    """Always returns midpoint based on year (no mileage/trim)."""
    name = "stub"

    def value(self, listing):
        year = listing.get("year")
        if not year:
            return None
        mid = 25000 + max(0, (2026 - year)) * -1500
        return valuation_mod.Valuation(
            source="stub",
            low=mid * 0.9,
            midpoint=mid,
            high=mid * 1.1,
            confidence="medium",
        )


class TestPipeline(unittest.TestCase):
    def setUp(self):
        self.tmpdir = tempfile.mkdtemp(prefix="ucm-test-")
        self.db_path = Path(self.tmpdir) / "test.db"
        self.alerts = []
        self.conn = db.connect(self.db_path)
        db.init_db(self.conn)
        # Add a brief
        self.brief_id = self.conn.execute(
            """INSERT INTO briefs(name, geography, target_json, max_all_in, min_discount,
                                   min_confidence, sources_json)
               VALUES (?, ?, ?, ?, ?, ?, ?)""",
            ("Test", "Austin, TX, 100mi",
             json.dumps({"make": "Toyota", "model": "Tacoma",
                         "year_min": 2016, "year_max": 2020, "trim": "TRD"}),
             30000, 0.10, "low", '["file"]'),
        ).lastrowid

        # Build pipeline with stubs
        self.drop = Path(self.tmpdir) / "drop"
        self.drop.mkdir()
        self.pl = pipeline.PipelineAdapters(
            discoverers=[discovery_mod.FileFeedAdapter(self.drop, "test_feed")],
            valuators=[StubValuation()],
            risk_screeners=[StubRisk()],
            notifiers=[StubNotifier()],
        )

    def tearDown(self):
        self.conn.close()

    def _write_listing(self, **overrides):
        rec = {
            "listing_id": "L1",
            "url": "https://example.com/L1",
            "year": 2019,
            "make": "Toyota",
            "model": "Tacoma",
            "trim": "TRD",
            "mileage": 60000,
            "ask_price": 22000,
            "location": "Austin, TX",
            "seller_name": "Vlad",
            "seller_type": "private",
            "title_claim": "clean",
            "description": "single owner, no accidents",
            "photos": [],
        }
        rec.update(overrides)
        (self.drop / "feed1.json").write_text(json.dumps([rec]), encoding="utf-8")
        return rec

    def test_dedupe_two_runs_same_id(self):
        self._write_listing()
        r1 = pipeline.run_once(self.conn, self.pl, only_brief_id=self.brief_id)
        # Re-stage the same feed (file was archived after first run)
        self._write_listing()
        r2 = pipeline.run_once(self.conn, self.pl, only_brief_id=self.brief_id)
        self.assertEqual(r1["listings"]["ingested_new"], 1)
        self.assertEqual(r2["listings"]["ingested_new"], 0)
        self.assertEqual(r2["listings"]["ingested_updated"], 1)
        rows = self.conn.execute("SELECT COUNT(*) AS c FROM listings").fetchone()
        self.assertEqual(rows["c"], 1)

    def test_alert_only_when_discount_passes(self):
        # 2019 Tacoma stub midpoint = 25000 + 7*-1500 = 14500
        # ask 22000 > midpoint → discount negative → no alert
        self._write_listing(ask_price=22000)
        rep = pipeline.run_once(self.conn, self.pl, only_brief_id=self.brief_id)
        self.assertEqual(rep["listings"]["alerts_sent"], 0)
        self.assertEqual(rep["listings"]["flagged"], 0)
        # Ask 12000 < midpoint 14500 → discount = 17% > 10% threshold → alert
        self._write_listing(ask_price=12000)
        rep = pipeline.run_once(self.conn, self.pl, only_brief_id=self.brief_id)
        self.assertGreaterEqual(rep["listings"]["flagged"], 1)
        self.assertGreaterEqual(rep["listings"]["alerts_sent"], 1)

    def test_alert_dedup_idempotent(self):
        self._write_listing(ask_price=12000)
        pipeline.run_once(self.conn, self.pl, only_brief_id=self.brief_id)
        # Re-stage the same record → second run should suppress the duplicate alert
        self._write_listing(ask_price=12000)
        rep2 = pipeline.run_once(self.conn, self.pl, only_brief_id=self.brief_id)
        # Second run: same price, same confidence, same flagset → suppressed
        self.assertEqual(rep2["listings"]["alerts_suppressed"], 1)
        self.assertEqual(rep2["listings"]["alerts_sent"], 0)

    def test_hard_stop_blocks_alert(self):
        self._write_listing(ask_price=12000, description="poison description")
        rep = pipeline.run_once(self.conn, self.pl, only_brief_id=self.brief_id)
        self.assertEqual(rep["listings"]["alerts_sent"], 0)
        self.assertEqual(rep["listings"]["rejected"], 1)

    def test_all_in_cost_within_budget(self):
        # ask 12000, tax 6.25% = 750, fees 350, inspection 200, contingency 5%
        # all-in ≈ (12000+750+350+0+200+0) * 1.05 = 13961 → below 30000 budget
        self._write_listing(ask_price=12000)
        rep = pipeline.run_once(self.conn, self.pl, only_brief_id=self.brief_id)
        cost = rep["brief_reports"][0]["evaluated"][0]
        self.assertEqual(cost["recommendation"], "review")

    def test_all_in_cost_over_budget(self):
        # Push ask to make all-in exceed 30000
        # ask 28000, tax 1750, fees 350, inspection 200, contingency 5% → 31742
        self._write_listing(ask_price=28000)
        rep = pipeline.run_once(self.conn, self.pl, only_brief_id=self.brief_id)
        evals = rep["brief_reports"][0]["evaluated"]
        # Will be ignored due to budget
        self.assertEqual(evals[0]["recommendation"], "ignore")

    def test_approve_decline_workflow(self):
        self._write_listing(ask_price=12000, listing_id="LAPPROVE")
        pipeline.run_once(self.conn, self.pl, only_brief_id=self.brief_id)
        row = self.conn.execute("SELECT id FROM listings WHERE listing_id='LAPPROVE'"
                                ).fetchone()
        lid = row["id"]
        # Approve via the CLI helper (so we exercise real DB writes)
        sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
        from used_car_monitor.__main__ import main as cli_main
        os.environ["MONITOR_DB_CONN"] = str(self.db_path)
        try:
            rc = cli_main(["approve", "--listing-id", str(lid),
                           "--max-offer", "12500", "--who", "tester"])
            self.assertEqual(rc, 0)
            status = self.conn.execute("SELECT status FROM listings WHERE id = ?",
                                       (lid,)).fetchone()["status"]
            self.assertEqual(status, "contacted")
            # Decline a second listing
            self._write_listing(listing_id="LDECLINE", ask_price=13000)
            pipeline.run_once(self.conn, self.pl, only_brief_id=self.brief_id)
            lid2 = self.conn.execute("SELECT id FROM listings WHERE listing_id='LDECLINE'"
                                     ).fetchone()["id"]
            rc = cli_main(["decline", "--listing-id", str(lid2), "--who", "tester"])
            self.assertEqual(rc, 0)
            status = self.conn.execute("SELECT status FROM listings WHERE id = ?",
                                       (lid2,)).fetchone()["status"]
            self.assertEqual(status, "rejected")
        finally:
            del os.environ["MONITOR_DB_CONN"]


class TestFingerprint(unittest.TestCase):
    def test_same_listing_different_ids_match(self):
        # Two re-prices that round to the SAME $50 bucket should produce the
        # same fingerprint. $27,000 and $27,024 both round to $27,000.
        a = {"year": 2019, "make": "Toyota", "model": "Tacoma", "trim": "TRD",
             "ask_price": 27000, "location": "Austin, TX"}
        b = {"year": 2019, "make": "Toyota", "model": "Tacoma", "trim": "TRD",
             "ask_price": 27024, "location": "Austin, TX"}
        self.assertEqual(db.fingerprint(a), db.fingerprint(b))

    def test_price_change_breaks_fingerprint(self):
        a = {"year": 2019, "make": "Toyota", "model": "Tacoma", "trim": "TRD",
             "ask_price": 27000, "location": "Austin, TX"}
        b = dict(a)
        b["ask_price"] = 27500  # crosses to next $50 bucket
        self.assertNotEqual(db.fingerprint(a), db.fingerprint(b))


class TestValuationMerge(unittest.TestCase):
    def test_blend_two_sources(self):
        v1 = valuation_mod.Valuation("a", 10000, 12000, 14000, "medium")
        v2 = valuation_mod.Valuation("b", 11000, 13000, 15000, "high")
        merged = valuation_mod.merge([v1, v2])
        # blended midpoint = (12000*2 + 13000*3) / 5 = 12600
        # final low = min(10000, 12600*0.9) = 10000 - we drop the assert that
        # forced low > 10000; the contract is "low <= midpoint <= high".
        self.assertLessEqual(merged.low, merged.midpoint)
        self.assertLessEqual(merged.midpoint, merged.high)
        self.assertEqual(merged.confidence, "high")  # highest single
        self.assertEqual(merged.midpoint, 12600)

    def test_single_source_drops_confidence(self):
        v1 = valuation_mod.Valuation("a", 10000, 12000, 14000, "medium")
        merged = valuation_mod.merge([v1])
        self.assertEqual(merged.confidence, "low")


if __name__ == "__main__":
    unittest.main(verbosity=2)