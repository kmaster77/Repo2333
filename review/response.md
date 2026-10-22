# Orchestrator response to the red-team critique

Date: 2026-10-22. Responds to `review/critique.md` (24 issues: 5 High, 10 Medium, 9 Low).
Rule from plan.md: all High issues are fixed; all others get a response.

## Decisions (made by the orchestrator before re-running the model)

### Base case changes (apply to `inputs.csv` base column; the old base stays reported as "original base" for traceability)
| Issue | Decision |
|---|---|
| M1 | **First sales in 2028** (build/permit 2026–2027). Becomes the new base. The 2027-start result is kept as a memo. |
| M2 | **Average truck load 9 m³** (range 8–10) in the delivery cost formula. |
| M3 | **Public green premium base 1.5%** (low 0%, high 3%). Add the GWL "recup" concrete discount as counter-evidence in market.md. |
| H1 | Keep €135/m³ as base, but re-label **confidence L**, add GWL primary list (C20/25 €130, C30/37 €139.5–144.5 retail, delivered ≤20 km) as triangulation, remove the unsourced "project ≈ 60–70% of list" claim or mark it [ASSUMPTION]. State that the price is more likely at/above the B2B average, so the error direction strengthens NOT VIABLE. |
| M9/L7 | Use ERMCO 2023 everywhere for ready-mix (6.0 Mm³, 178 plants, 33.7k m³/plant); explain that 14 Mm³ includes prefab and other concrete. |

### P2 and option fixes
| Issue | Decision |
|---|---|
| H3 | **Gate fee base €1/t** (low €0, high €10). **Steel yield 1%** base (low 0.5%, high 3%), and steel value **split 50/50 with the partner** in the base. €5/t and 3% move to the upside case. |
| M5 | Add **RCA washing/screening cost €3/t** (range 2–4) to own-crushed RCA. |
| H4 | P2 inherits first sales 2028 and uses an **acquisition ramp of 55% / 85% / 100%** of target volume. The override order is documented in `options.py` (later merge wins, explicit). |
| H5 | Use the exact formula for delivery distance (no rounding: 22.7 km at 90k, 23.9 km at 100k). Remove the "+€414" and "break-even" wording. Present P2 explicitly as a combination of favourable inputs. |
| M6 | Re-label OPT-01/OPT-02 as unverified. Add the 4K-Beton 5.7% EBITDA margin data point (from critique). State that ~€2.5M buys a ~35k m³ plant; reaching 90k needs extra capex. Add **+€1.0M** expansion capex to P2 (range 0.5–2.0), labelled [ASSUMPTION]. |
| H2 | Report P2 as a **range** (stacked downside / base / upside) and add the gate-fee-for-NPV=0 figure. Gates for "go": gate fee and steel split become hard gates. |
| M7 | O5: net the MKI value against the public premium (no double count). |
| M10 | Re-frame the recommendation: "No route is investable on present evidence. The integrated acquisition route is the only one that comes close; it is worth a small (€50–100k) due-diligence phase to test gates A–C, not an investment." |

### Presentation fixes
| Issue | Decision |
|---|---|
| M4 | Label both pass-through rates as key judgement calls; add a "100% pass-through" sensitivity line in model_summary.md. |
| M8 | Label the RSS range "indicative, not a probability interval". |
| L1, L2 | Disclose in model_summary.md: salvage-only terminal value and no WC release are conservative (memo values given). |
| L3 | Chart shows one decimal place. |
| L4 | Deck does not show the all-optimistic +€30M bar; it shows the realistic range instead. The model keeps it. |
| L5, L6 | Mark OPT-04 unverified; correct MKT-27 wording. |
| L8 | Note that EUA forecasts are probably nominal; effect ≤ €0.1M NPV. |
| L9 | Footnote in model_summary.md linking tornado and criterion-4 drivers. |

## Status
The table above records the decisions. Results after implementation are in section "Results after fixes" below (filled after re-running the model).
