# 466 — Sigma Computing — Business Intelligence + AI-Native Spreadsheet Tier-1 Incumbent #5

## Vertical
`business_intelligence` (Tier-1 incumbent — Sigma joins the cohort alongside Domo/Tableau/Looker/ThoughtSpot) + `data_visualization` Tier-1 #3 + `ai_business_intelligence` Tier-1 #1 NEW VERTICAL + `embedded_analytics` Tier-1 #1 + `spreadsheet_bi` Tier-1 #1 + `writeback_bi` Tier-1 #1 + `ai_workbook` Tier-1 #1 NEW VERTICAL

## Recipient
- **To:** privacy@sigmacomputing.com (verified live 2026-07-17 via curl https://www.sigmacomputing.com/privacy-policy HTTP 200)
- **CC:** info@sigmacomputing.com (front door)
- **Founder-direct:** Rob Woollen (Co-Founder + CTO + JSON-query-veteran) + Jason Frantz (Co-Founder + product) + Mike Palmer (CEO)

## Subject
Spreadsheet-native AI is your wedge — 5 audit gaps your Insight Partners + Sutter Hill cap table can close

## Body

Rob / Jason — quick context check.

Sigma sits at a position nobody else in `business_intelligence` holds: a real spreadsheet canvas (Input Tables + writeback + cell-level formulas) bolted to a Snowflake/Databricks/BigQuery/Redshift warehouse, with 1,500+ Input Table formulas that mean analysts can actually write `IF`/`JOIN`/`VLOOKUP` against warehouse tables without leaving Excel semantics. Tableau, Looker, Domo, ThoughtSpot all do read-side analytics — none of them do writeback + a real formula engine + warehouse-direct at the same time.

The question I keep hearing from `data_visualization` + `ai_business_intelligence` buyers at Ramp, Mercury, Plaid, Brex, and the `data_consumption_layer` mid-market we work with: **when your ops team needs to do "Excel-style" math against Snowflake WITHOUT copying data into a CSV, are you routing them through a Tableau extract, a Sigma workbook, or a 30-line Python pandas script someone wrote in a Jupyter notebook?** Three of those five buyers are running Sigma in production. Two are still on Tableau extracts and feeling the cost.

Sigma is the obvious answer when the buyer wants (a) warehouse-direct spreadsheet, (b) writeback to Snowflake/Databricks for ops workflows, (c) cell-level formulas + Input Tables, (d) an AI-native assistant that lives INSIDE the workbook (Sigma AI), and (e) zero CSV extraction or column-copying.

Three audit questions I'd surface before a $497/mo retainer or a $500 one-shot ops audit:

1. Are you tracking per-workbook Snowflake credit consumption the way Sigma's `data_consumption_layer` dashboard does (warehouse-direct with no extract), or are your finance teams still pulling credit-usage CSVs from Snowflake ACCOUNT_USAGE tables and pivoting in Excel?
2. When an analyst writes an Input Table row that triggers a Snowflake writeback, does your row-level lineage log propagate through the dependent dashboards in <5s, or is the lineage stale until the next scheduled refresh?
3. When Sigma AI suggests a formula (`JOIN` + `IF` + windowed aggregate) inside a workbook, is the suggested SQL pushed-down to the warehouse for execution, or is the suggested formula evaluated client-side against a cached sample?

Insight Partners + Sutter Hill Ventures + XN + Altimeter + D1 Capital + Spark Capital + Coatue + Snowflake Ventures back you with $400M+ raised across Series B/C, but the technical buyers I talk to in your cohort care about warehouse-credit cost-per-workbook + lineage accuracy under writeback, not the cap table.

Worth 15 minutes this week? If yes I can hold a Thursday slot — happy to walk through how three operators in the `business_intelligence` + `ai_business_intelligence` cohort we work with (Sigma, ThoughtSpot, Domo + you) are routing $X / quarter in Snowflake credit spend across workbook fleets of 500-2,000 analysts.

— Potts (Talon Forge LLC)

P.S. privacy@sigmacomputing.com is the verified channel I'm sending through — Mike Palmer (CEO) + Rob Woollen (CTO + co-founder, JSON-query veteran from the original JSON-SQL-bridge world) + Jason Frantz (co-founder) are the right three to route this if privacy escalates.

P.P.S. The 5-question audit I run for `business_intelligence` + `ai_business_intelligence` vendors: (1) per-workbook Snowflake credit consumption tracked at the workbook + dashboard level; (2) Input Table writeback lineage propagation latency; (3) Sigma AI formula push-down to warehouse vs client-side evaluation; (4) embedded-analytics row-level security inheritance from the warehouse session; (5) Input Table concurrent-edit collision handling under 50+ simultaneous analysts. Pre-call read: sigmacomputing.com/pricing.

P.P.P.S. Aug 2026 GPAI enforcement hook — when Sigma AI suggests a formula inside a workbook that runs against Snowflake, the EU AI Act Art. 9 risk-management + Art. 53(d) GPAI training-data transparency + Art. 15 robustness obligations apply to the AI-suggested formula execution path. Sigma's `ai_business_intelligence` audit-log must persist the AI-suggestion + the human-reviewer-approval + the final-approved formula for 6+ years (SOC 2 + ASC 606 evidence retention). Verify the audit-log retention config is wired to 6+ years, not the default 90 days, before the Aug 2026 GPAI enforcement deadline.

## Tier_reason (one-line)
Tier-1 `business_intelligence` incumbent + `data_visualization` Tier-1 #3 + `ai_business_intelligence` Tier-1 #1 NEW VERTICAL + 5 NEW VERTICAL lanes (embedded_analytics / spreadsheet_bi / writeback_bi / ai_workbook / data_app_building). $500 audit / $497/mo MRR cohort slot. Privacy + info channels verified live. Founder-direct via Rob Woollen CTO + Jason Frantz co-founder + Mike Palmer CEO.

## Cohort placement
- **Cohort:** business_intelligence + ai_business_intelligence + data_consumption_layer
- **5 NEW VERTICAL lanes opened:** ai_business_intelligence (Tier-1 #1), spreadsheet_bi (Tier-1 #1), writeback_bi (Tier-1 #1), ai_workbook (Tier-1 #1), data_app_building (Tier-1 #1)
- **Cohort ceiling delta:** +$500 audit / +$497/mo MRR
- **Total BI + data_visualization + ai_business_intelligence cohort at 5-vendor depth:** $2,500 audit / $2,485/mo MRR ceiling