# Phase 3 — Viability gate (orchestrator)

Date: 2026-10-22. Criteria were fixed in `plan.md` §2.1 before the model was built. Results come from `model/results.json` (re-run by the orchestrator with `python3 model/run_all.py`; Excel–Python check passed in all 6 cases, see `model/check_report.md`).

## Base case tested
B1 circular ready-mix plant, ~70k m³/yr, Zuid-Holland, recycled aggregate bought, CEM III/B binder, plant-average prices. Build year 2026, sales 2027–2036, 8% real discount rate.

## Result against the criteria

| # | Criterion | Result | Pass? |
|---|---|---|---|
| 1 | NPV > 0 at 8% real | NPV = −€4.48M (−81% of capex) | FAIL |
| 2 | Payback < 7 years | Not reached within 10 years | FAIL |
| 3 | EBITDA positive by year 3 | +€0.53M in 2029 | PASS |
| 4 | NPV > 0 with ≥2 of 6 drivers at pessimistic value | 0 of 6 | FAIL |

NPV is far outside the borderline band (−10% to 0% of capex).

## Verdict: **NOT VIABLE** (base case B1 as a stand-alone plant)

## Why (orchestrator reading)
- The circular mix itself is not the problem: it costs ~€2.5/m³ *less* than the Dutch standard CEM III/B mix.
- The problem is that a new stand-alone ready-mix plant earns ~€7.6/m³ EBITDA in a mature, shrinking, consolidating market, while ~€11.7/m³ is needed to recover the capex at 8%.
- The "green" story adds little cash: green premium swing ±€1.9M NPV, ETS ±€0.4M, MKI value to the supplier ~€0–1/m³ because CEM III/B competitors already have a similar MKI.
- NPV = 0 needs ~112k m³/yr (+60% volume) or ~€149/m³ average price (+10.5%).

## Known optimism in the base case (to carry into Phase 5)
- Sales from 2027 is optimistic: permit + build likely takes 12–18 months from late 2026. A one-year delay would make NPV worse.

## Next step
Start Agent 7 (viability strategist): ≥5 options, each tested in `model/model_core.py` via overrides / extra scenario sheets.
