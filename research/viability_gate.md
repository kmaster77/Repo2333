# Phase 3 — Viability gate (orchestrator)

Date: 2026-10-22. Criteria were fixed in `plan.md` §2.1 before the model was built. Results come from `model/results.json` (re-run by the orchestrator with `python3 model/run_all.py`; Excel–Python check passed in all 6 cases, see `model/check_report.md`).

> **Superseded numbers:** the sections below record the original gate (sales 2027). The current result after the red-team fixes is in "Re-run after critique" at the end of this file (verdict unchanged: NOT VIABLE).

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

> **Note:** this section and the next record the *original* gate (pre-critique base, sales from 2027). The current numbers are in the section "Re-run after critique" below and in `model/model_summary.md`: NPV −€5.33M, NPV = 0 needs 134k m³/yr or €154/m³.

## Why (orchestrator reading)
- The circular mix itself is not the problem: it costs ~€2.5/m³ *less* than the Dutch standard CEM III/B mix.
- The problem is that a new stand-alone ready-mix plant earns ~€7.6/m³ EBITDA in a mature, shrinking, consolidating market, while ~€11.7/m³ is needed to recover the capex at 8%.
- The "green" story adds little cash: green premium swing ±€1.9M NPV, ETS ±€0.4M, MKI value to the supplier ~€0–1/m³ because CEM III/B competitors already have a similar MKI.
- NPV = 0 needs ~112k m³/yr (+60% volume) or ~€149/m³ average price (+10.5%).

## Known optimism in the base case (to carry into Phase 5)
- Sales from 2027 is optimistic: permit + build likely takes 12–18 months from late 2026. (Tested after the critique: a one-year delay changes NPV only slightly, because deferring the capex roughly offsets the lost year of sales.)

## Next step
Start Agent 7 (viability strategist): ≥5 options, each tested in `model/model_core.py` via overrides / extra scenario sheets.

---

## Re-run after critique (2026-10-22, Phase 5)

The red-team critique (`review/critique.md`) found no arithmetic errors but some optimistic base inputs. The orchestrator's decisions (`review/response.md`) were implemented in `model/inputs.csv` and the model, and `python3 model/run_all.py` was re-run. Excel–Python check: **all 23 cases match** (`model/check_report.md`). The criteria in plan.md §2.1 were **not** changed.

**Base case changes:** first sales **2028** (permits 2026, build 2027; M1), average truck load **9 m³** (M2), public green premium **1.5%** (M3). The €135/m³ price is kept but is now labelled confidence L (H1); the likely error in it points down. The original base is kept as memo case `O_orig` (−€4.48M, unchanged to the euro).

| # | Criterion | Original base (sales 2027) | **New base (sales 2028)** | Pass? |
|---|---|---|---|---|
| 1 | NPV > 0 at 8% real | −€4.48M (−81% of capex) | **−€5.33M (−97% of capex)** | FAIL |
| 2 | Payback < 7 years | not reached | **not reached** | FAIL |
| 3 | EBITDA positive by year 3 | +€0.53M (2029) | **+€0.32M (2030)** | PASS (narrowly) |
| 4 | NPV > 0 with ≥2 of 6 drivers at pessimistic value | 0 of 6 | **0 of 6** | FAIL |

IRR −13.9% (was −7.1%). Funding need €7.09M (was €6.84M). EBITDA from 2030 is €0.2–0.3M a year (3.4% → 1.9% margin), against €0.4–0.5M before.

### Verdict after the fixes: **NOT VIABLE** (unchanged, and further from the borderline band)

- NPV = 0 now needs ~134k m³/yr (+92%) or a plant-average price of ~€154/m³ (+14%).
- Undoing every conservative choice the critique found (100% price pass-through, salvage at book value, working-capital release) still leaves NPV at −€3.4M.
- **Options:** no route is investable on present evidence. Every option has a negative NPV (−€2.5M to −€6.3M). The best plant routes are the acquisition routes (O3 −€3.5M, P1 −€4.0M, P2 −€4.0M; P2 range −€6.8M to −€1.4M). See `research/viability_options.md` §0 and §7: the acquisition route is worth only a small (€50–100k) due-diligence phase to test gates A–C, not an investment.
