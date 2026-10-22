# Assumptions — Agent 5 (Cost & price analyst)

All money in real 2026 €, excl. VAT. "Low / high" = low and high value of the parameter (not always the pessimistic case). Machine-readable values are in `model/inputs.csv`.

| ID | Description | Low | Base | High | Unit | Reasoning / source IDs | Confidence (L/M/H) |
|---|---|---|---|---|---|---|---|
| A-CST-01 | Output ramp-up, % of steady-state volume (yr1 / yr2 / yr3+) | 35 / 60 / 85 | 50 / 79 / 100 | 65 / 90 / 100 | % | TEC §8 ramp 35k → 55k → 70k m³. A newcomer needs anchor clients (MKT §8). Low = slow client acquisition. | L |
| A-CST-02 | Capex split of the €5.5M plant (equipment / civil & site / permits & engineering) | 3.0 / 0.6 / 0.4 | 4.0 / 1.0 / 0.5 | 5.5 / 1.8 / 0.7 | M€ | Split of A-TEC-21 (€4–8M) so that totals stay 4.0 / 5.5 / 8.0. Civil incl. grid connection and quay works on a waterside site. No vendor quote. | L |
| A-CST-03 | Product LCA/EPD (NMD cat. 1) one-off | 40 | 80 | 160 | k€ | 4 product families × €20k (A-TEC-47); needed because generic cat-3 data carry ×1.3 (CST-01). | L |
| A-CST-04 | Pre-opening costs (staff before start, trial mixes, initial type testing) | 200 | 300 | 500 | k€ | Judgement: ~3 months of staff + lab programme for KOMO admission. | L |
| A-CST-05 | Land | leased | leased | leased | — | Waterside industrial land in Rotterdam region is usually ground-leased (CST-09, CST-10). | M |
| A-CST-06 | Salvage value of plant + civil works after 10 years | 10 | 25 | 40 | % of capex | Book value at 25-yr life would be 60%; second-hand batching plants and site works fetch much less. | L |
| A-CST-07 | Working capital: receivables / payables / inventory | 45 / 21 / 7 | 60 / 30 / 10 | 75 / 45 / 15 | days | Dutch contractors pay late (judgement); cement/aggregate suppliers ~30 days; little stock in ready-mix. | L |
| A-CST-08 | Sustaining capex | 0.5 | 1.0 | 2.0 | % of capex/yr | Control systems, loaders' replacement parts; judgement. | L |
| A-CST-09 | Circular C30/37 mix: 50% coarse RCA (V/V), +15 kg CEM III/B, no fine RCA | 30% RCA, +0 kg | 50% RCA, +15 kg | 50% coarse + 25% fine RCA, +30 kg | — | Based on TEC §4.3 mix C2 without fine RCA (fine RCA needs CROW-CUR 127, POL-30). 50% needs CUR 112 outside X0 (POL-30). | M |
| A-CST-10 | Superplasticiser: price and dose | €1.0/kg; 0.5% (ref) | €1.4/kg; 0.7% ref, 0.9% circular | €2.0/kg; 0.9% ref, 1.2% circular | €/kg; % of binder | Sika dose range 0.4–2.0% (CST-12); Chinese liquid PCE $0.7–1.1/kg is a floor (CST-13); EU price higher. Extra +0.2 pt for RCA (A-TEC-13). | L |
| A-CST-11 | Plant-average binder content (all strength classes) | 290 | 310 | 330 | kg/m³ | ERMCO 2023: NL average cement ~310 kg/m³ (CMP-43). Use with plant-average price €135 (A-MKT-16). | M |
| A-CST-12 | Cement prices 2026, delivered bulk, incl. 2026 carbon cost: CEM III/B / CEM I | 95 / 120 | 110 / 140 | 130 / 165 | €/t | Raised from A-MKT-19/20 (105/125): Argus says EU cement mid-to-high US$100s/t ex-works and +10–15% planned in 2026 (CST-14); Sika uses ~€150/t CEM I (CST-11). CEM I–CEM III/B spread €30/t sits between the market agent's €20 and Heidelberg's list +€22/m³ (~€70/t incl. margin, MKT-25). No Dutch price list exists. | L |
| A-CST-13 | Share of market-wide binder cost increases passed into concrete prices | 50 | 80 | 100 | % | CEM III/B is the Dutch default (CMP-27), so every producer faces the same carbon/slag cost; competition limits full pass-through. | L |
| A-CST-14 | RCA truck distance crusher → plant | 15 | 30 | 50 | km | Locate within ~30 km of 2–3 BRL 2506 crushers (TEC §6); NMD assumes 50 km (TEC-04). | M |
| A-CST-15 | Certified recycled sand 0/4 ex-works | 3 | 8 | 15 | €/t | No public NL price; crusher sand now mostly goes to fill/road base (≈ menggranulaat €3/t, A-MKT-14); washed/certified product dearer. | L |
| A-CST-16 | Water price | 0.8 | 1.2 | 2.0 | €/m³ | Business mains water ~€1–1.5/m³ excl. VAT (judgement); part from recycled wash water. Immaterial (€0.2/m³ concrete). | L |
| A-CST-17 | Extra per-lot testing of bought RCA | 0.5 | 0.8 | 1.5 | €/t RCA | ~€400 per 500 t lot for density/WA (EN 1097-6), constituents (EN 933-11), sulphate/chloride (EN 1744-1) — TEC §3 test list; lab price is judgement. | L |
| A-CST-18 | RCA handling at plant (separate bins per source, sprinkling to SSD, extra loader moves, moisture control) | 0.5 | 1.0 | 2.0 | €/t RCA | TEC §1.1/§3: separate storage + pre-wetting needed; cost is judgement. | L |
| A-CST-19 | Diesel price excl. VAT, bulk | 1.30 | 1.55 | 1.80 | €/l | Judgement from 2026 pump levels minus VAT; bulk discount. | M |
| A-CST-20 | Staff split of 10 FTE: production 7 / SG&A 3 | 6 / 2 | 7 / 3 | 9 / 4 | FTE | A-TEC-25 list: manager, sales/planning 2–3, batchers 2, lab 1–2, loader 2, maintenance 1. | L |
| A-CST-21 | Employer cost per FTE: production / SG&A | 62k / 80k | 70k / 90k | 78k / 110k | €/yr | CAO Mortelbedrijven 2026 guaranteed €3,394–3,770/month (CST-06). Real pay ~€4,000 × 12 × 1.08 holiday × ~1.30 employer charges ≈ €67k + overtime/early starts (30% unsocial-hours bonus) ≈ €70k. | M |
| A-CST-22 | Maintenance & wear (plant + civil) | 1.5 | 2.5 | 4.0 | % of capex/yr | Judgement; mixer liners/blades every 40–60k m³ (TEC-57). | L |
| A-CST-23 | Fixed certification & testing (KOMO BRL 1801 audits, CSC, NMD fees, external tests, LCA upkeep) | 30 | 50 | 80 | k€/yr | CSC licence €1,230 per 3 yr (CST-20) + certifier costs; NMD €587/yr (CST-03); KOMO audit cost by quotation (CST-21) — judgement. | L |
| A-CST-24 | Waterside site lease | 6 | 10 | 15 | €/m²/yr | Rotterdam canon 3.81% of ground value (CST-09) × assumed industrial ground value €150–300/m² = €5.7–11.4; + quay premium. Port canon not public (CST-10). | L |
| A-CST-25 | SG&A non-staff (insurance, ERP/dispatch software, audit, legal, marketing, cars, office) | 200 | 300 | 450 | k€/yr | Judgement for a €9–10M revenue SME. | L |
| A-CST-26 | Bad debt | 0.3 | 0.5 | 1.0 | % of revenue | Judgement; construction insolvencies are frequent in NL. | L |
| A-CST-27 | Average one-way delivery distance | 10 | 20 | 35 | km | For uniform demand in a disc of radius R the mean distance is 2R/3: R = 30 km → 20 km. Consistent with A-TEC-29 and A-CMP-11. | M |
| A-CST-28 | MKI tender value reaching the supplier | 0 | 0.5 | 3.4 | €/m³ | POL §3: €3.4 is the value vs a ceiling-level mix. Our circular mix has about the same MKI as a Dutch CEM III/B mix (§12 of price_breakdown.md), so vs a typical Dutch competitor ΔMKI ≈ €0–0.3 → value ≈ €0–1. Not additive to the green premium. | L |
| A-CST-29 | Betonakkoord-basis MKI as a function of CO₂ | — | MKI ≈ €1.10 + €0.058 × kg CO₂/m³ | — | €/m³ | Linear fit to the 24 ceiling/front-runner pairs in POL-01 (e.g. 169 kg ↔ €10.9; 119 kg ↔ €8.0; 145 kg ↔ €9.5). Fits all rows within ±€0.1. | M |
| A-CST-30 | Dutch corporate income tax (Vpb) | 19% / 25.8% | 19% up to €200k; 25.8% above | same | % | Rates in force 2023–2026 (general knowledge; not re-checked this session). | M |
| A-CST-31 | Outlet price for conventional crusher sand 0/4 (A+B option) | 0 | 3 | 8 | €/t | As fill/road base (A-MKT-14); concrete use limited by norms (POL-30). | L |
| A-CST-32 | Value of steel recovered from rubble (A+B option) | 100 | 150 | 220 | €/t | Yard prices HMS €150–240/t (CST-16, CST-17); export HMS 1/2 ~$370–400/t CFR Turkey (CST-18); rebar from rubble is dirtier, so below yard HMS. | M |
| A-CST-33 | Disposal cost of light contaminants (A+B option) | 90 | 120 | 160 | €/t | Incl. landfill/incineration tax €40.85 (2026) rising to €64–81 (POL-50, POL-51) + gate of waste processor; judgement. | L |
| A-CST-34 | Own crushing line opex (A+B): 3 FTE, maintenance 3% of capex, BRL 2506 certification €25k/yr, extra 1 ha | 2 FTE; 2%; €15k; 0.5 ha | 3 FTE; 3%; €25k; 1 ha | 4 FTE; 5%; €40k; 2 ha | — | Judgement; TEC §5 staff 2–3 per shift for a mobile line. | L |
