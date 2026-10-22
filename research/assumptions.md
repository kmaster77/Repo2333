# Assumptions register

Merged by the orchestrator from the per-agent logs (`assumptions_<agent>.md`). IDs are unique per agent prefix. Later phases append their own sections below.


## Policy (POL)

All money in real 2026 €, excl. VAT. Source IDs refer to `research/sources_policy.md`.

| ID | Description | Low | Base | High | Unit | Reasoning / source IDs | Confidence (L/M/H) |
|---|---|---|---|---|---|---|---|
| A-POL-01 | EU ETS allowance (EUA) price, 2027 | 65 | 88 | 105 | €/t CO₂ | Spot ~€85 on 22 Oct 2026 (POL-44, POL-45). SEB range €50–100, avg €75 (POL-47). Forecasts cut after July 2026 review (POL-48). | M |
| A-POL-02 | EUA price, 2030 | 70 | 100 | 130 | €/t CO₂ | LSEG pre-review €114 real-2025 (POL-46); PBL KEV €108 (POL-59); lowered by shallower LRF proposal (POL-42, POL-48). | M |
| A-POL-03 | EUA price, 2034–2036 | 85 | 125 | 180 | €/t CO₂ | LSEG €186 (2035, pre-review) (POL-46); PBL KEV €141 (2035) (POL-59); review proposal lowers path (POL-42). | L |
| A-POL-04 | CBAM factor path (share of free allocation kept by EU cement plants) | Current law: 97.5% 2026 → 51.5% 2030 → 0% 2034 | Current law until review adopted; from 2028 apply proposal (+15% of phased-out allocation back, end 2038) as 50/50 blend | Proposal fully adopted: end in 2038 | % | Current law POL-39; Proposal POL-42, POL-43. Trilogue from Jan 2027 (POL-45); adoption late 2027 likely. | M |
| A-POL-05 | Direct CO₂ intensity of grey clinker at EU plants supplying NL | 0.78 | 0.82 | 0.86 | t CO₂/t clinker | ASSUMPTION: typical EU kiln (process ~0.53 + fuel ~0.25–0.30). Benchmark top-10% avg 0.689 (POL-41) sets a floor. | M |
| A-POL-06 | Clinker share in cement | CEM I 0.95; CEM III/A 0.50; CEM III/B 0.30 | CEM I 0.93; CEM III/A 0.45; CEM III/B 0.25 | CEM I 0.90; CEM III/A 0.40; CEM III/B 0.20 | t clinker/t cement | ASSUMPTION based on EN 197-1 composition bands (CEM III/A 36–65% slag, CEM III/B 66–80%). Agent 3 to confirm. | M |
| A-POL-07 | Net carbon cost in CEM I (current-law CBAM path, base EUA) | 2027: 12; 2030: 31; 2034: 57 | 2027: 16; 2030: 45; 2034: 95 | 2027: 24; 2030: 65; 2034: 147 | €/t cement | ESTIMATE: (intensity − benchmark × CBAM factor) × EUA × clinker share. Base 2027: (0.82 − 0.656×0.95) × €88 × 0.93 = €16.1. Base 2030: (0.82 − 0.656×0.515) × €100 × 0.93 = €44.8. Base 2034: 0.82 × €125 × 0.93 = €95. Low 2034 uses the 2038 proposal (15% of a ~0.62 benchmark kept) and €85. High uses 0.86 t/t, clinker 0.95 and high EUA. See policy.md §5. | M |
| A-POL-08 | Net carbon cost in CEM III/B | 2030: 8; 2034: 12 | 2030: 12; 2034: 26 | 2030: 20; 2034: 46 | €/t cement | ESTIMATE: same formula × clinker share (0.20–0.30, base 0.25; A-POL-06). Base 2030: 0.482 × €100 × 0.25 = €12.1. Slag itself carries no ETS cost in the cement plant. | M |
| A-POL-09 | Share of carbon cost passed on in cement price | 50 | 85 | 100 | % | ASSUMPTION: CBAM protects EU producers from import competition, so pass-through should be high; competition between EU suppliers limits it. | L |
| A-POL-10 | Fictive discount factor in MKI-based tenders | 1 | 3 | 5 | € fictive discount per € MKI saved | ProRail factor 4 × reference MKI (POL-24); RWS MKW factor €2 (POL-23); example €5.13/MKI (POL-23); PIANOo examples 1/4/10 (POL-22). | M |
| A-POL-11 | MKI gap between Betonakkoord ceiling and front-runner value, 2026 | 2.4 | 2.8 | 3.1 | €/m³ concrete | POL-01: 2026 ceiling vs front-runner: unreinforced 9.5→7.1; inside 10.1→7.5; outside 10.9→8.0; aggressive 11.9→8.8. | H |
| A-POL-12 | Share of tender advantage the concrete supplier can capture as a price premium | 20 | 40 | 60 | % of contractor's fictive advantage | ASSUMPTION: the discount goes to the contractor's bid; supplier captures part through negotiation. No public data. | L |
| A-POL-13 | Start date of mandatory MKI ceiling values for concrete in all public GWW tenders (Besluit milieuprestatie-eisen GWW) | 2027-07-01 | 2028-01-01 | 2029-01-01 | date | Consultation closed 24 Aug 2026; levels still to be set in ministerial regulation; intended 2027 (POL-17, POL-18). Dutch rule-making usually slips 6–12 months. | M |
| A-POL-14 | Share of NL GWW market with MKI award criterion once law applies | 35 | 50 | 65 | % of GWW turnover | Only above EU works threshold; RWS + ProRail + large clients already use MKI (POL-20, POL-22). | L |
| A-POL-15 | MPG tightening for homes before 2030 | 0 | 0 (no tightening) | 20% probability of a tightening announced for ≥2029 | — | Tightening dropped June 2025; system kept to 2030; evaluation running (POL-10, POL-11). | H |
| A-POL-16 | Dutch GWP (whole-life carbon) limit values for new buildings in force | 2030 | 2032 | not before 2035 | year | EPBD: roadmap by Jan 2027, limit values from 2030 intended (POL-14); NL slow on MPG; Aedes: WLC "at the earliest 2030" (POL-11). | L |
| A-POL-17 | Landfill tax (afvalstoffenbelasting) 2030+ | 41 | 81 | 117 | €/t | 2026 €40.85 (POL-50); BP2027 proposal €81 from 2030 (POL-51, POL-52); old path €117 (POL-51). Low = proposal rejected and frozen. | M |
| A-POL-18 | National CO₂ levy (CO₂-heffing industrie) cost for this business | 0 | 0 | 0 | €/t | Not ETS-covered as a concrete plant; levy rate below ETS and to be abolished (POL-57, POL-58). Indirect via cement nil (no NL clinker kilns — ASSUMPTION, not re-checked). | H |
| A-POL-19 | Permit lead time, ready-mix or prefab plant on existing industrial zoning | 6 | 12 | 24 | months (application to final permit) | ASSUMPTION: regular procedure 8 (+6) weeks or extended 26 weeks (Awb 3.4) + preparation (AERIUS, noise, dust studies) + possible objections/appeal. Nitrogen floor not before end 2027 (POL-64). | M |
| A-POL-20 | Permit lead time, stationary crushing/recycling plant (option A) | 9 | 18 | 36 | months | ASSUMPTION: waste processing is permit-requiring (POL-62); CMP minimum-standard check (POL-55); noise/dust; often extended procedure and zoning change. | L |
| A-POL-21 | Net present value of MIA for eligible capex (36% category) | 7 | 9.3 | 11.6 | % of eligible capex | ESTIMATE: 36% × 25.8% CIT = 9.3%; 45% category → 11.6%; 27% → 7.0% (POL-68). Only if taxable profit. Vamil timing gain extra ~1–3% (ASSUMPTION). | M |
| A-POL-22 | Share of plant capex that qualifies for MIA | 0 | 20 | 50 | % of total capex | ASSUMPTION: only extra equipment for recycled input (A 1500) / recycling (A 1401) qualifies; standard batching plant does not (POL-69, POL-70). | L |
| A-POL-23 | WBSO benefit on R&D wage costs | 16 | 36 (50 if starter) | 50 | % of eligible R&D wage cost | POL-76: 36% first €391,020 (50% starters), 16% above. | H |
| A-POL-24 | DEI+ / VEKI grant obtained for first plant | 0 | 0.4 | 1.5 | € million | ASSUMPTION: competitive, first come first served, budget CE €60 m (POL-74) and VEKI €123 m (POL-75). Base assumes partial award for innovative recycled-fines/low-clinker line only. | L |
| A-POL-25 | Allowed recycled coarse aggregate in base product without extra design rules | 20 | 30 | 50 | % (V/V) of coarse aggregate | NEN 8005: Type A1 30% (non-X0), 50% (X0); Type A2 20% (POL-30). CUR 112: up to 50% without changed rules; up to 100% with adjusted values (POL-30). | H |
| A-POL-26 | Allowed recycled fine aggregate (sand) in structural concrete | 0 | 0–10 | 60 | % (V/V) of fine aggregate | Norm route limited; CROW-CUR 127 allows fines under its class system (research basis up to 60%) (POL-30, POL-36). Exact CUR 127 class table not verified. | L |
| A-POL-27 | Share of private B&U clients (by turnover) that ask for Betonakkoord ceiling/front-runner values by 2028 | 20 | 40 | 70 | % | Aim 70% via voluntary convenant (POL-02); 21 signatories June 2026 (POL-06). Voluntary, no sanction. | L |
| A-POL-28 | Slag (GGBS) supply risk for CEM III after Tata blast furnace 7 closure | +0 | +10 | +25 | % price change of slag cement vs today, 2031–2036 | ASSUMPTION: HO7 replacement by DRI+EAF planned (POL-94) but timeline slipping (POL-93). Less domestic slag → more imports. | L |
| A-POL-29 | EU harmonised end-of-waste criteria for recycled aggregates in force | 2028 | 2030 | after 2032 | year | No criteria yet (POL-84); CEA proposal due 18 Nov 2026 (POL-87) aims at harmonised EoW (POL-86). NL already has national EoW regime (POL-85). | L |


## Market (MKT)

All prices in 2026 €, excluding VAT. "Delivered" = franco building site / plant. Conversion of older prices uses CBS CPI (2025=100), January values from MKT-54; approximate annual factors to 2026: 2021→2026 ×1.27, 2023→2026 ×1.10, 2024→2026 ×1.06, 2025→2026 ×1.02 (assumes 2026 annual CPI ≈ 102).

| ID | Description | Low | Base | High | Unit | Reasoning / source IDs | Confidence (L/M/H) |
|---|---|---|---|---|---|---|---|
| A-MKT-01 | Total concrete use NL (all producers), 2026–2030 average | 13.0 | 14.0 | 15.0 | Mm³/yr | Betonhuis / C&BC "~14 Mm³, 13–14 long-run" (MKT-01, MKT-02); 12.9 Mm³ in 2017 (MKT-05); roadmap expects ~15 Mm³ by 2030 (MKT-10). EIB growth +2.5–4.5%/yr near term (MKT-32) supports upper half to 2028; demand for gravel falls after 2030 (MKT-15). | M |
| A-MKT-02 | Ready-mix (betonmortel) volume | 7.0 | 7.4 | 8.0 | Mm³/yr | 53% of 14 Mm³ = 7.4 (MKT-01); "7–7.5" (MKT-10); ACM long-run avg ~8 (MKT-04). | M |
| A-MKT-03 | Concrete products / prefab volume | 5.0 | 5.3 | 6.0 | Mm³/yr | 38% of 14 Mm³ = 5.3 (MKT-01); "6–6.5" in roadmap (MKT-10) is an older/higher figure. | M |
| A-MKT-04 | Split of products: structural B&U elements / paving & blocks / piles / sewer & other | — | 37% / 40% / 13% / 10% | — | % of products | MKT-01 (2021). | M |
| A-MKT-05 | GWW share of ready-mix volume | 8% | 13% | 19% | % | Conflict between sources: 8% (C&BC 2021, MKT-01) vs 95/510 = 19% (Betonhuis 2020 table, MKT-02). Base = midpoint. | L |
| A-MKT-06 | Cement use NL | 3.5 | 4.0 | 5.0 | Mt/yr | 3.5–4 Mt (Betonhuis 2024, MKT-03); "long-run ~5 Mt" (MKT-01) is an older average. Check: 14 Mm³ × 280–320 kg/m³ = 3.9–4.5 Mt. | M |
| A-MKT-07 | Stony C&D waste released (all puin) | 19 | 22 | 25 | Mt/yr | 19 Mt (2018) → 22 Mt (2025) → 25 Mt (2030) BRBS (MKT-09); TNO 22 Mt (MKT-08); ~23 Mt processed (MKT-59). | M |
| A-MKT-08 | Concrete rubble released (betonpuin) | 11.5 | 13.0 | 15.0 | Mt/yr | 60% of stony waste (MKT-09, MKT-10); 12 Mt (TNO, MKT-08); ~15 Mt (Betonakkoord, MKT-05, MKT-11). | M |
| A-MKT-09 | Recycled concrete aggregate used in new concrete today (high-grade) | 1.0 | 1.5 | 2.0 | Mt/yr | Monitoring 0.76 Mt betongranulaat at 60–65% coverage → ~1.2 Mt extrapolated (MKT-06); BRBS ~1.5 Mt (MKT-07); <15% of 15 Mt = <2.25 Mt (MKT-05); TNO "<2 Mt" (MKT-08). CSC slide figure 3.29 Mt (MKT-14) treated as outlier. | M |
| A-MKT-10 | High-grade share of concrete rubble (2025) | 8% | 11.5% | 15% | % | A-MKT-09 ÷ A-MKT-08. | M |
| A-MKT-11 | Primary gravel price delivered to a NL concrete plant (bulk, by ship or truck) | 25 | 32 | 40 | €/t | No public NL bulk price found (data gap). Proxy: Belgian Limburg pick-up list gravel 4/16 ~€36–37/t (MKT-20, retail-ish); bulk contracts usually below list; ~75% of coarse aggregate imported (MKT-17), so import logistics set the price. Arcadis: primary prices tracked construction costs (MKT-15). | L |
| A-MKT-12 | Primary concrete sand (betonzand 0/4) delivered | 14 | 19 | 25 | €/t | Proxy BE list sand 0/4 €24.5/t, Rijnzand €33/t pick-up (MKT-20); NL is near self-sufficient in sand (MKT-16), so lower than gravel. | L |
| A-MKT-13 | Certified betongranulaat (BRL 2506-1, 4/16–4/32) ex-works crusher | 10 | 15 | 25 | €/t | No public NL list (data gap). BE COPRO betongranulaat €9.5–18/t pick-up (MKT-20, MKT-21, MKT-22). Washed/certified NL product for concrete assumed at or above BE level. | L |
| A-MKT-14 | Menggranulaat (road base) ex-works | 0 | 3 | 8 | €/t | BE lists €1–10/t (MKT-20–22). Falling road-base outlet (MKT-11) puts downward pressure. | L |
| A-MKT-15 | Gate fee for clean concrete rubble at a crusher, bulk (>100 t) | −2 | 5 | 15 | €/t | BE: clean concrete accepted €0–1/t (MKT-20–22). NL counter tariff for small loads clean (meng)puin ~€20/t (MKT-23) is an upper bound for retail. Low = crusher pays for very clean feedstock once high-grade demand rises. | L |
| A-MKT-16 | Average delivered ready-mix project price, all classes | 115 | 135 | 155 | €/m³ | Indicative 2026 project prices C20/25 €110–130, C30/37 €140–165 (MKT-27). List prices (MKT-24) are ~€200–225/m³ → project ≈ 60–70% of list. | M |
| A-MKT-17 | Ready-mix C20/25 delivered project price | 105 | 120 | 135 | €/m³ | MKT-27; Heidelberg surcharge C20/25 XC2 +€3.50 vs C12/15 base (MKT-25). | M |
| A-MKT-18 | Ready-mix C30/37 delivered project price | 130 | 145 | 165 | €/m³ | MKT-27; C30/37 is +€10.50 vs C12/15 and +€7.50 vs C20/25 on Heidelberg list (MKT-25); Holcim list +€9 (MKT-24). | M |
| A-MKT-19 | CEM III/B 42.5 N bulk delivered price | 90 | 105 | 125 | €/t | No public NL cement list (data gap). Lower bound from Heidelberg "less cement" credit €0.09/kg; upper bound from "extra cement" €0.20/kg list (MKT-25); IndexBox CEM I €95–130/t (MKT-28, low reliability). Agent 1/5 to add ETS/CBAM effect. | L |
| A-MKT-20 | CEM I 52.5 R bulk delivered price | 105 | 125 | 150 | €/t | Heidelberg list: replacing CEM III/B by CEM I = +€22/m³ (~€70/t at ~300 kg/m³ — list, includes margin) (MKT-25); IndexBox €95–130/t (MKT-28). In NL, CEM III/B is the standard and CEM I costs more (IndexBox claim that blends carry a premium does not fit NL lists). | L |
| A-MKT-21 | Structural prefab elements average value (ex-works) | 350 | 450 | 600 | €/m³ concrete | Hollow-core €50–120/m² incl. delivery & placement (MKT-29) ÷ ~0.14 m³/m² ≈ €360–860/m³ incl. steel, prestress, transport, assembly; ex-works lower. | L |
| A-MKT-22 | Paving/blocks average value | 125 | 175 | 250 | €/m³ concrete | No source; typical paving €10–15/m² at 8 cm (0.08 m³/m²). | L |
| A-MKT-23 | Piles / sewer products average value | 220 / 350 | 300 / 450 | 400 / 600 | €/m³ concrete | No source; set between paving and structural elements. | L |
| A-MKT-24 | Public + semi-public (housing corporations) share of concrete volume | 30% | 40% | 50% | % | Bottom-up in market.md §5: GWW ready-mix, municipal paving/sewer, corporation housing (31% of new homes, MKT-30), public buildings. | M |
| A-MKT-25 | Cash green premium for circular ready-mix (≥30% recycled coarse aggregate + low-clinker binder), public/MKI-driven segment | 0% | 3% | 8% | % of conventional price | Supplier surcharges R30 +€3.30, R100 +€11, ECOPact +€5–9/m³ (MKT-24, MKT-25) = 2–8% of project price; PBL: recycled ~10% dearer but market buys on price (MKT-47); German DCE WTP ~€0.26/m³ per %-pt ≈ €8/m³ for 30% (MKT-48). Tender reward is mostly fictive (A-MKT-27). | L |
| A-MKT-26 | Cash green premium, private segment (developers, contractors, agri) | −2% | 0% | 3% | % | Private buyers mostly buy on price (MKT-47); MPG drives low-MKI binder choice, not recycled aggregate. Negative low = must discount to win. | L |
| A-MKT-27 | Tender "fictive" value of MKI reduction (factor × ΔMKI) | 2 | 4 | 5 | € fictive discount per € MKI saved | RWS proposal factor 2 (MKT-43); ProRail factor 4 (MKT-44); Betonakkoord X = 5 for ready-mix (MKT-42). | M |
| A-MKT-28 | ΔMKI per m³ of circular low-clinker ready-mix vs standard ready-mix | 2 | 5 | 8 | € MKI/m³ | Standard ready-mix MKI ~€10–25/m³ (MKT-46); ceiling 2021 €16–22/m³ (MKT-42); ceilings fall ≥7.5%/yr (MKT-56), so the gap vs the ceiling shrinks over time. | L |
| A-MKT-29 | Recycled aggregate per m³ of "circular" ready-mix | 0.30 | 0.40 | 0.55 | t/m³ | R30–R50 coarse replacement of ~1,000–1,100 kg coarse aggregate/m³ (MKT-25 R-grades; Agent 3 to confirm). | M |
| A-MKT-30 | First-plant region share of national ready-mix demand (Zuid-Holland) | 17% | 20% | 25% | % | New homes 2025: ZH 18.6% (12.9k/69.2k, MKT-35); woondeal share 25.0% (247.9k/992.9k, MKT-38, MKT-39). | M |
| A-MKT-31 | Share of regional demand inside a 25–50 km delivery radius of one plant | 55% | 70% | 85% | % | ACM: max truck time ~1.5 h (MKT-04); plan §2 radius 25–50 km. | L |
| A-MKT-32 | Mature output of one circular ready-mix plant (SOM) | 30 | 60 | 100 | k m³/yr | National avg ~37k m³/plant (7.4 Mm³ ÷ ~200 plants, MKT-04); 1994 avg 46k m³; a new entrant reaching 60k by year 3–4 is ambitious but possible with anchor clients. Agent 3/6 to align with capex. | L |
| A-MKT-33 | Population shares for regional rubble estimate (ZH / NH / NB) | — | 21% / 16% / 15% | — | % of NL population | Approximate CBS 2025 population (no source opened in this session — from general knowledge). Used only for a rough regional rubble estimate. | L |
| A-MKT-34 | Concrete demand trend 2030–2036 | −2%/yr | −0.5%/yr | +1%/yr | %/yr | Gravel demand falls after 2030 (9.3–10.1 → 7.3–8.9 Mt/yr, MKT-15); EIB: new homes dip around 2030 (MKT-34) but GWW renewal rises €2.4bn → €2.9bn/yr (MKT-40). | L |


## Technology (TEC)

Prices in 2026 €, excl. VAT. Where an older price is converted, the factor is CBS CPI 2021→2026 = 134.56/110.39 × 1.034 ≈ **1.26** (CPI 2025 annual and 2026 inflation ~3.4%, TEC-43, TEC-44).

| ID | Description | Low | Base | High | Unit | Reasoning / source IDs | Confidence (L/M/H) |
|---|---|---|---|---|---|---|---|
| A-TEC-01 | Conventional jaw+impact crushing: coarse RCA 4/16–4/22 yield | 50 | 58 | 65 | % of input mass | Impact/jaw give ~30–45% 0–4 mm; cone gives ~25% less fines (TEC-35, TEC-36); TU Delft assumes fine fraction ~30% (TEC-18). Base = 100 − 38 fines − 3 steel − 1 contaminants | M |
| A-TEC-02 | Conventional crushing: 0/4 crusher sand (incl. <0.063 mm) | 30 | 38 | 45 | % of input mass | Same as above; balance item | M |
| A-TEC-03 | Steel reinforcement removed by magnet | 1 | 3 | 5 | % of input mass | Typical reinforcement 50–150 kg/m³ concrete (domain knowledge, not verified this session) | L |
| A-TEC-04 | Light contaminants removed (wood, plastic, gypsum, insulation) | 0.5 | 1 | 2 | % of input mass | Clean BRL 2506 concrete rubble; selective demolition lowers it (TEC-33, TEC-19) | L |
| A-TEC-05 | Smart Liberator yields: gravel / sand / paste-rich fines (per t input) | 40 / 25 / 18 | 44 / 28 / 24 | 48 / 32 / 28 | % of input mass | No published mass balance. Derived from typical concrete composition (cement 150, sand 330, gravel 461 kg per t, TEC-28) + hydrated paste ≈ cement + bound water ≈ 20–25%; liberation efficiency assumed 90–95% | L |
| A-TEC-06 | everox (ADR+HAS+activation) yields: RCA / ACP / RFA / filler (of recovered output) | 55 / 15 / 12 / 3 | 60 / 20 / 15 / 5 | 65 / 23 / 18 / 8 | % of output | Company guideline 60/20/15/5 (TEC-21); varies with input concrete | M |
| A-TEC-07 | Thermal-mechanical treatment: coarse aggregate yield | 30 | 45 | 60 | % of input mass | Fines rise to 40–70% when paste is removed (TEC-34) | M |
| A-TEC-08 | Diesel use, conventional crushing + screening + loading | 0.15 | 0.3 | 0.6 | l diesel per t input | SBM REMAX 600: 340 t/h at 38 l/h = 0.11 l/t for crusher only (TEC-39); + screens, loader, excavator; Quattrone ~37 MJ/t ≈ 1 l/t primary energy (TEC-34) | M |
| A-TEC-09 | Electricity, advanced dry liberation (Smart Liberator type) | 1 | 3 | 8 | kWh per t input | Company claim "<1 kWh/t" for SC1 (TEC-28) is a claim; base adds pre-crushing, sifting, refining | L |
| A-TEC-10 | Water absorption (WA24) of purchased coarse RCA type A1 | 3 | 5 | 7 | % by mass | Selective/advanced 1.5–4%, unknown-origin rubble higher; US data 6.5% (TEC-33, TEC-38) | M |
| A-TEC-11 | Extra cement needed for 50% coarse RCA at the same strength class | 0 | 15 | 30 | kg/m³ | Strength −0.19% per 1% coarse RCA (TEC-37) → −9.5% at 50%; compensate by lowering w/c ~0.02–0.04 at 330 kg binder | M |
| A-TEC-12 | Absorption water added for RCA (not counted in w/c) | 15 | 28 | 40 | l/m³ | = WA × RCA mass; 550–710 kg RCA × 3–6%; pre-soaking practice (TEC-84) | M |
| A-TEC-13 | Extra superplasticiser for RCA mixes | 0 | 0.2 | 0.5 | % of binder mass | Keep slump with higher water demand; general practice (TEC-84, TEC-38) | L |
| A-TEC-14 | GWP of CEM I supplied in NL | 700 | 800 | 880 | kg CO₂-eq/t | EU representative 732.5 (TEC-11); CE Delft ~900 (TEC-13); Heidelberg BG EPD 676 | M |
| A-TEC-15 | GWP of CEM III/B supplied in NL | 280 | 320 | 360 | kg CO₂-eq/t | CE Delft ~300 (TEC-13); UK CEM III/B 351 (TEC-14); EU CEM III average 450 at 48.5% clinker (TEC-12) | M |
| A-TEC-16 | GWP of aggregates + A2 transport + plant energy + admixture | 15 | 20 | 30 | kg CO₂-eq/m³ | ~1,900 kg aggregate × 2–5 kg/t; cement 300 km truck ≈ 96–99 tkm × 0.106 kg (TEC-04, TEC-15); A3 3.63 kWh + 4.43 MJ (TEC-04) | M |
| A-TEC-17 | MKI factors (A1-set, A1 module) derived from NMD cat. 3 | CEM I 0.070; CEM III/B 0.043; primary aggregate 0.0014; RCA 0 | same | same | €/kg | Solved from NMD Table 6A/16A mix pairs (TEC-04); see technology.md §4.4 | M |
| A-TEC-18 | MKI multiplier A1-set → A2-set (concrete) | 2.0 | 2.15 | 2.2 | × | NMD impact analysis: CEM I ×2.17, CEM III ×2.14 (TEC-05); RWS "≈2×" (TEC-07) | H |
| A-TEC-19 | NMD category 3 data include a safety surcharge vs product-specific (cat. 1) data | 20 | 30 | 30 | % | Domain knowledge of NMD Bepalingsmethode; NOT re-verified this session — check with Agent 1 | L |
| A-TEC-20 | ACP (activated cement paste) GWP and MKI | GWP 11; MKI 0.001 | GWP 15; MKI 0.002 | GWP 40; MKI 0.004 | kg CO₂/t ; €/kg | Company figure 11 kg CO₂/t (TEC-25); MKI scaled by analogy with slag-type SCMs | L |
| A-TEC-21 | Ready-mix plant capex, 120 m³/h, excl. land and trucks | 4.0 | 5.5 | 8.0 | M€ | No NL figure found. Anchors: BE site €11M incl. builders' merchant on 6.5 ha for >150k m³/yr (TEC-52); US turnkey $1.2–6.5M (vendor data); extra bins/covered storage for RCA fractions | L |
| A-TEC-22 | Ready-mix plant site area | 1.0 | 1.5 | 2.5 | ha | Bins, covered RCA storage, silos, truck wash, parking 8–10 mixers; quay if waterside | L |
| A-TEC-23 | Theoretical capacity of base plant (1 shift) | 200,000 | 240,000 | 280,000 | m³/yr | 120 m³/h × ~2,000 h/yr | M |
| A-TEC-24 | Base plant output at steady state (year 3+) | 50,000 | 70,000 | 90,000 | m³/yr | Utilisation 20–40% of theoretical is normal for ready-mix (peaky demand); NL ~14 Mm³/yr total concrete (TEC-73) — volume ranking is Agent 2's task | L |
| A-TEC-25 | Plant staff excl. mixer drivers (manager, sales/planning 2–3, batchers 2, lab 1–2, loader drivers 2, maintenance 1) | 7 | 10 | 13 | FTE | Expert estimate; no source found | L |
| A-TEC-26 | Truck mixer effective load | 9 | 10 | 12 | m³/trip | Mixers carry 9–14 m³ (TEC-48, TEC-47, TEC-51); part loads common | M |
| A-TEC-27 | Truck mixer all-in hourly cost incl. driver (2026) | 95 | 110 | 130 | €/h | Retail €120–140/h (TEC-47, VAT status unclear); Holcim standby €85/h (TEC-50) | M |
| A-TEC-28 | Delivery cost formula per m³ | fixed 7 + 0.4/km | fixed 9 + 0.5/km | fixed 11 + 0.6/km | €/m³ (km = one-way) | Fixed time 50 min (load, unload, wash) and 45 km/h average speed at A-TEC-27 cost and 10 m³ load | M |
| A-TEC-29 | Average one-way delivery distance | 10 | 20 | 35 | km | Open time 1.5–2 h (TEC-45, TEC-46); NMD models ~50 km (118 tkm/m³ ÷ 2.37 t, TEC-04) | M |
| A-TEC-30 | Annual output per truck mixer | 7,000 | 9,000 | 11,000 | m³/truck/yr | ~4 trips/day × 10 m³ × 220–250 days | L |
| A-TEC-31 | New 12 m³ truck mixer price | 125,000 | 135,000 | 150,000 | € | Dealer listing €133,800 ex VAT (TEC-49) | M |
| A-TEC-32 | Road haulage of aggregates, full load one-way | 0.18 | 0.25 | 0.35 | €/t·km + €1.5–3/t handling | KiM 2021 truck+trailer €0.246/tkm (avg. load, incl. empty return) and €2.85/km (TEC-41) → full 28 t load ×2 km per loaded km ≈ €0.20/t·km ×1.26 ≈ €0.25 | M |
| A-TEC-33 | Inland shipping of aggregates | 0.015 | 0.03 | 0.05 | €/t·km + €1.5–4/t transshipment | KiM 2021: small ship €0.036/tkm, push barge €0.010/tkm (TEC-41), ×1.26 | M |
| A-TEC-34 | Prefab plant capex (structural elements: walls, columns, beams, solid slabs), 30,000 m³/yr | 18 | 25 | 40 | M€ | VBI ~€20M for 1M m² hollow-core (~120–150k m³) phase 1 (TEC-54, trade press) — extrusion is the cheapest per m³; carousel/fixed-mould element plants cost more per m³ | L |
| A-TEC-35 | Prefab staff at 30,000 m³/yr | 50 | 75 | 110 | FTE | Productivity 270–600 m³/FTE/yr (expert estimate; not sourced) | L |
| A-TEC-36 | Prefab site area | 3 | 5 | 8 | ha | Goldbeck plant on ~20,000 m² site area (TEC-56) + storage yard | L |
| A-TEC-37 | Prefab curing energy (heat) | 10 | 25 | 50 | kWh/m³ | Heated beds/chambers 30–60 °C; not sourced | L |
| A-TEC-38 | Ready-mix plant energy | 3.5 kWh + 0.1 l diesel | 3.6 kWh + 0.12 l | 4.5 kWh + 0.25 l oil/diesel | per m³ | NMD A3 3.63 kWh + 4.43 MJ diesel (TEC-04); DE study 4.43 kWh + 0.26 l oil + 0.07 l diesel (TEC-83) | H |
| A-TEC-39 | Economic lifetimes | plant 20 / mixer truck 8 / crusher 10 / carousel 20 / moulds 5 | 25 / 10 / 12 / 25 / 10 | 30 / 12 / 15 / 30 / 15 | years | Expert estimate; mixer liners 40–60k m³ (TEC-57, vendor) | L |
| A-TEC-40 | Mobile crushing line (impact crusher 250–350 t/h + screen + loader + excavator) | 1.0 | 1.6 | 2.5 | M€ | Machine sizes TEC-39, TEC-40; prices on request — estimate | L |
| A-TEC-41 | Stationary high-grade RCA plant (crush, magnet, wind-sift, wash), 300–450 kt/yr | 6 | 10 | 15 | M€ | B&A UK wash plant £8M (≈€9.3M) for 450 kt/yr (TEC-74) | L |
| A-TEC-42 | Advanced liberation plant (Smart Liberator / everox type), ~100 kt/yr | 8 | 15 | 30 | M€ | No public capex. everox raised €10M + EIC €2.5M (TEC-23) for company, not plant | L |
| A-TEC-43 | Crusher wear parts (blow bars, liners) | 0.2 | 0.4 | 0.8 | €/t | Expert estimate | L |
| A-TEC-44 | Share of base-plant volume sold as circular mix (≥30–50% coarse RCA) | 40 | 60 | 80 | % | Exposure class limits (TEC-01) and client acceptance | L |
| A-TEC-45 | RCA purchased per m³ of circular mix (coarse + fine) | 330 | 710 | 900 | kg/m³ | 30% coarse (NMD, TEC-04) to 50% coarse + 25% fine (§4.3) to CROW-CUR 127 level (TEC-01) | M |
| A-TEC-46 | Fall in GGBS (blast-furnace slag) supply from IJmuiden after BF7 → DRI/EAF (~2030) | 0 | 50 | 60 | % | BF7 ≈ 60% of coal-based steel output (TEC-70); DRI 2028–2030 (TEC-71). Price effect on CEM III/B to be set by Agent 5 | L |
| A-TEC-47 | Cost of product-specific LCA/EPD (NMD cat. 1) per product family | 10,000 | 20,000 | 40,000 | € one-off + ~€3–5k/yr | Expert estimate; not sourced | L |


## Competitors (CMP)

All values are for the Netherlands unless stated. Prices are € 2026, excl. VAT.

| ID | Description | Low | Base | High | Unit | Reasoning / source IDs | Confidence (L/M/H) |
|---|---|---|---|---|---|---|---|
| A-CMP-01 | Discount that large contractors get below public list prices for ready-mix | 10 | 20 | 35 | % below list | No source found. List prices (CMP-35) are for small/ad-hoc buyers. Large project prices are negotiated. Range is judgement. Agent 2/5 should replace with market data. | L |
| A-CMP-02 | Current national ready-mix market share of Heidelberg Materials (ex-Mebin) | 20 | 28 | 35 | % of NL m³ | Mebin estimated its own share at 30–40% in an old ACM case (CMP-31). Today ~30 of 178 plants (CMP-28, CMP-43) = 17% of plants, but its plants are larger than average. It still buys competitors (CMP-33). | L |
| A-CMP-03 | Combined share of the 5 largest ready-mix groups (Heidelberg, De Hoop, Dyckerhoff Basal, Van Nieuwpoort, plus one of Rouwmaat/Kijlstra/Theo Pouw) | 50 | 60 | 70 | % of NL m³ | No public market-share data after ~2011. Based on plant networks (CMP-28, CMP-36, CMP-39, CMP-40, CMP-42) and fragmented tail of local plants. | L |
| A-CMP-04 | Green premium a circular ready-mix supplier can charge over standard concrete of the same class | 0 | 5 | 12 | €/m³ | Holcim 2026 list: ECOPact +€5 (C30/37 XC2) to +€9 (C20/25 XC2) (CMP-35). SL Materials says it is "priced competitively" with conventional concrete (CMP-06). Holcim even adds +€4/m³ for ≤30% recycled granulate (CMP-35). | M |
| A-CMP-05 | CO₂ cut from replacing primary gravel (and part of sand) with recycled concrete aggregate only, binder unchanged | 5 | 10 | 12 | % of A1–A3 GWP per m³ | Van Nieuwpoort EPD: −8% to −12% (CMP-41); Mebin: "extra 11%" with 100% recycled coarse aggregate (CMP-29); Rouwmaat: "up to 11%" (CMP-42). | M |
| A-CMP-06 | Actual concrete-rubble throughput of SL Materials Zaandam | 130 | 250 | 400 | kt/yr | 130 kt/yr for the first Smart Liberator (2018, CMP-08); "400,000 t/yr can be recycled" (2023, CMP-07). Real utilisation not public. | L |
| A-CMP-07 | Start of commercial output at everox/Dura Vermeer 's-Gravendeel plant | 2027 H1 | 2027 H2 | 2028 | date | Plan was Q2 2025, then "2026"; still under construction in Sept 2026 (CMP-15, CMP-16, CMP-17, CMP-88). Permitted 100 kt/yr. | M |
| A-CMP-08 | Circulair Mineraal output in 2026 | 50 | 75 | 100 | kt/yr | Company target "50–100 kt" (CMP-75). | M |
| A-CMP-09 | Number of firms in NL producing recycled sand and/or cement-paste fines ("level 3+") at industrial scale by 2028 | 4 | 6 | 9 | firms | Today: SL Materials, Renewi, Circulair Mineraal, everox (building), Twee "R" (Mangeler), Heidelberg (separation, CMP-60). Renewi says 95% of NL is still at level 2 (CMP-67). | L |
| A-CMP-10 | Time for a new ready-mix plant to get product certification (KOMO) and first EPD in the NMD | 6 | 12 | 18 | months | No source checked by this agent. Judgement from typical certification cycles. Agent 1 should confirm (BRL/KOMO scheme for betonmortel). | L |
| A-CMP-11 | Effective competitive radius of a ready-mix plant | 25 | 35 | 50 | km | Plan.md states ~25–50 km. Ready-mix must be placed within ~1.5–2 h of mixing. | M |
| A-CMP-12 | Share of NL ready-mix volume owned by groups that also own cement (Heidelberg, Buzzi/Dyckerhoff, Holcim) | 30 | 40 | 50 | % of m³ | Heidelberg (ENCI + Mebin), Buzzi (Dyckerhoff Basal), Holcim (small, Landgraaf). CRH (Cementbouw) sold its ready-mix (CMP-38). Derived from A-CMP-02 plus estimate for Dyckerhoff Basal. | L |
| A-CMP-13 | Porter's Five Forces ratings (1 = weak, 5 = strong force against the entrant) | – | see competitors.md §7 | – | score | Analyst judgement on the verified facts in competitors.md. | M |
| A-CMP-14 | SmartCrusher bv is active only as a licence/IP holder, not as an operator | – | yes | – | – | Website news stops in Dec 2020 (CMP-01); inventor died 2023 (CMP-04); PitchBook lists the firm as private, no recent deals seen. No bankruptcy notice found, but none searched in the insolvency register. | L |
| A-CMP-15 | CPI factor to bring 2025 retail prices to 2026 € | 1.02 | 1.03 | 1.04 | factor | This agent did not open a CBS CPI table. Placeholder only; Agent 5 must replace with CBS CPI. | L |
| A-CMP-16 | Ready-mix list price for C30/37 (standard, delivered, 2026, regional independent/integrated plant) | 195 | 212 | 225 | €/m³ excl. VAT | Holcim Landgraaf 2026 list: €212.50 (XC2/XC3), €224.50 (XC4) (CMP-35). Retail web prices C30/37 ~€178 excl. VAT in 2025 (Mols €215 incl. VAT, CMP-83; €215/1.21 = €177.7) plus delivery fees. Low end reflects retail web offers (CMP-84). | M |
| A-CMP-17 | Supply of fly ash and blast-furnace slag (main clinker substitutes in NL) falls over 2027–2036 | −10 | −30 | −60 | % change vs 2026 | EIC/CORDIS says fly ash and slag are "being phased out" (CMP-14). NL cement relies on blast-furnace slag (IJmuiden next to Tata Steel, CMP-59; Mebin CEM III/B ~85% of products, CMP-27). Size and timing not verified by this agent; Agent 1/3 should check Tata Steel plans. | L |

## Cost & price (CST)

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

## Viability options (OPT)

All values real 2026 €, excl. VAT. They are used only in option scenarios (`model/options.py`, sheet `Opt_Overview`); the base case is unchanged.

| ID | Description | Low | Base | High | Unit | Reasoning / source IDs | Confidence (L/M/H) |
|---|---|---|---|---|---|---|---|
| A-OPT-01 | Delay of first sales vs base (corrected base reference O0) | 0 | 1 | 2 | years | technology.md: build ~12–18 months incl. permit; permit for a ready-mix plant from late 2026 → first full sales year 2028. Permits/engineering stay in 2026; plant capex, start-up costs, grant, MIA move to 2027. Horizon stays 2036 (9 operating years). | M |
| A-OPT-02 | First year of on-site crushing (waste-processing permit) | 2028 | 2029 | 2031 | year | A-POL-20 permit lead time 9 / 18 / 36 months from late 2026 (environmental activity "waste processing", noise, dust). | L |
| A-OPT-03 | Site works for rubble acceptance (paved stockpile, drainage, weighbridge, fencing) | 0.25 | 0.40 | 0.70 | M€ | ASSUMPTION: 1 ha extra paving and drainage + weighbridge; scaled from capex_site_prep_civil (€1.0M for 1.5 ha). Own-line option adds the mobile crusher €1.6M (A-TEC-40) → €2.0M. | L |
| A-OPT-04 | Salvage value of crushing line in 2036 | 5 | 10 | 20 | % of capex | Mobile crusher 10–15 yr life (A-TEC-39) with heavy wear; site works have little resale value. | L |
| A-OPT-05 | Contract (campaign) crushing rate, rubble on our site | 5 | 7.5 | 10 | €/t rubble | OPT-04: UK on-site crushing £7/t ≈ €8/t. No Dutch tariff found. Rate includes machine, operator, diesel and wear; we provide a loader driver (1 FTE). | L |
| A-OPT-06 | Purchase price of an existing ready-mix plant (equipment, site rights, permit, customer book) | 1.5 | 2.5 | 4.0 | M€ | ESTIMATE: average NL plant ~34k m³/yr (CMP-43) × EBITDA €6–8/m³ (ready-mix margin ~8%, OPT-02) ≈ €0.2–0.3M EBITDA; at 5–8× → €1.0–2.4M, plus asset value. Sellers exist in a shrinking, consolidating market (CMP-33, CMP-38). Upper reference: Cementir paid ≈€18M for one larger Danish plant + a minority stake (OPT-01), so good plants cost much more. | L |
| A-OPT-07 | Conversion of the acquired plant to circular mixes (3 RCA bins, covered RCA store, moisture probes, sprinklers, wash water) + civil 0.2 + permit change/transaction 0.2 | 0.5 (+0.4) | 0.8 (+0.4) | 1.2 (+0.4) | M€ | Subset of the greenfield equipment list in A-TEC-21/A-CST-02. Model: capex_plant_equipment = 2.5 + 0.8 = 3.3; civil 0.2; permits 0.2; pre-opening €100k (trial mixes, initial type testing; staff already in place). | L |
| A-OPT-08 | Ramp-up of an acquired plant (yr1 / yr2) | 50 / 79 | 55 / 85 | 65 / 90 | % of 70k m³ | Existing customer book ≈ 35k m³ (average plant) is partly kept; circular growth on top. Year 1 is also the takeover year. | L |
| A-OPT-09 | Maintenance of an older acquired plant | 2.5 | 3.5 | 5.0 | % of physical capex/yr | Older equipment; A-CST-22 range 1.5–4%. | L |
| A-OPT-10 | Salvage value of acquired plant in 2036 | 10 | 15 | 25 | % of capex | Older plant, lower resale value than new (A-CST-06 base 25%). | L |
| A-OPT-11 | Ramp-up with framework/offtake contracts signed before opening (yr1 / yr2) | 60 / 85 | 75 / 95 | 85 / 100 | % of steady state | MKT §8: a newcomer needs anchor clients (corporation, GWW contractor framework, municipality); framework fills part of year-1 capacity. | L |
| A-OPT-12 | Framework discount, expressed on ALL volume | 0 | −1.0 | −2.0 | €/m³ | ~3% (€4/m³) discount on about one third of volume. Buyer power 4/5 (competitors.md §9). | L |
| A-OPT-13 | MKI/low-CO₂ value captured per CIRCULAR m³ with a lower-CO₂ binder (from 2029) | 0 | 1.5 | 4.5 | €/m³ | ESTIMATE: −40 kg CO₂/m³ vs CEM III/B → ΔMKI (A1) 0.058 × 40 = €2.3 → A2 set ×2.15 ≈ €5.0 MKI/m³ (A-TEC-18, A-CST-29). Fictive discount €1–5 per € MKI (base 3, POL-23/24) → €15/m³ for the contractor; supplier captures 30% (15–50%) → €4.5/m³ on MKI-tender volume. MKI tenders = 50% of public (A-POL-14), public = 40% → €0.9 per circular m³; + private €1/m³ on 60% → €0.6. Total ≈ €1.5. | L |
| A-OPT-14 | Extra binder cost per CIRCULAR m³ (ACP / ACT-type binder, extra admixture) | 0 | 1.5 | 4.0 | €/m³ | No price found for everox ACP or Ecocem ACT; Ecocem claims "minimal" cost impact (OPT-05/06). +€0–12/t on 325 kg binder. TRL 6–7, certification via EN 197-6 / ETA pending (technology.md §7). | L |
| A-OPT-15 | Binder certification, ETA support, extra EPDs | 0.10 + 0.02/yr | 0.15 + 0.04/yr | 0.30 + 0.06/yr | M€ one-off + M€/yr | ASSUMPTION; one-off modelled as opt_extra_capex_y0. | L |
| A-OPT-16 | "Maximum realistic" subsidies | grant 0.4, MIA 20% | grant 1.0, MIA 50% | grant 1.5, MIA 50% | M€ / % eligible capex | A-POL-24 (DEI+/VEKI 0–1.5), A-POL-22 (MIA share 0–50%). VEKI caps at €80/t CO₂ avoided — our standard circular mix avoids almost no CO₂ vs CEM III/B, so VEKI does not fit. EU Innovation Fund is for large binder projects (POL-77/78). | L |
| A-OPT-17 | Bigger plant: steady volume, extra staff, delivery distance | 90k, +1 FTE, 22 km | 100k, +2 FTE, 23 km | 112k, +2 FTE, 25 km | m³/yr | SOM high = 100k (A-MKT-32) = ~10% of all ready-mix in one plant's radius (MKT §8); a larger radius is needed to sell it. One shift can make ~240k m³ (A-TEC-23), so no extra plant capex. | L |
| A-OPT-18 | Urban inland site closer to demand | 12 km, €12/m², +€3/t | 15 km, €15/m², +€5/t | 18 km, €18/m², +€8/t | delivery km, lease, gravel by truck | inputs.csv note: truck-fed site gravel +€5–8/t; CST-09/10 lease range €6–15/m². | L |
| A-OPT-19 | Asset-light: licensee plants at maturity (+1 per year from 2027) and circular volume per licensee | 2 / 8k | 4 / 15k | 8 / 25k | plants / m³/yr | Average plant 34k m³ (CMP-43); circular share ~45%. Incumbents (Heidelberg, Holcim) have their own lines; licensees would be independents. | L |
| A-OPT-20 | Asset-light licence/service fee | 1.0 | 2.0 | 3.5 | €/m³ | Must stay below the licensee's own gain: ~€2.5/m³ cheaper mix + ~€1.7/m³ premium (price_breakdown.md §0). | L |
| A-OPT-21 | Asset-light RCA brokerage margin | 0.5 | 1.5 | 3.0 | €/t | ASSUMPTION: trading margin on certified RCA (ex-works €15/t, A-MKT-13). | L |
| A-OPT-22 | Asset-light LCA/EPD/MKI project services (from 2028) | 0 | 100k | 200k | €/yr | ~20 projects × €5k; ASSUMPTION. | L |
| A-OPT-23 | Asset-light team and costs | 3 FTE, €100k ovh, €250k start-up, €100k capex | 4 FTE × €90k, €150k ovh, €350k start-up, €200k capex | 5 FTE, €200k ovh, €500k start-up, €300k capex | | ASSUMPTION: concrete technologist, LCA expert, technical sales, logistics planner. | L |
| A-OPT-24 | Steel yield from clean concrete rubble (kept at inputs value, flagged) | 1 | 3 | 5 | % of input | A-TEC-03 (ASSUMPTION). Steel sales are ~40% of the crushing line's net result; at 1% the P2 NPV falls by €0.43M. Much rebar is often removed at the demolition site. | L |

## Value proposition (VP)

All values are in real 2026 €, excl. VAT. They are used only in `research/value_proposition.md`. The model inputs (`model/inputs.csv`) are not changed. No new web sources were used, so there is no `sources_vp.md`. Model runs R-01 … R-20 are listed in value_proposition.md, Appendix A.

| ID | Description | Low | Base | High | Unit | Reasoning / source IDs | Confidence (L/M/H) |
|---|---|---|---|---|---|---|---|
| A-VP-01 | Concrete use per m² gross floor area in a concrete-frame apartment building (only used for the MPG estimate) | 0.3 | 0.5 | 0.8 | m³/m² GFA | ASSUMPTION. Typical range for Dutch apartment blocks with concrete floors and walls. No source was checked in this session. Used only to show the order of size of the MPG effect. | L |
| A-VP-02 | Reference service life in the MPG calculation for homes | 50 | 75 | 75 | years | ASSUMPTION from the MPG method (Bepalingsmethode): homes 75 years, offices 50 years. Not re-checked in this session. | M |
| A-VP-03 | Tightening of the Betonakkoord / GWW MKI and CO₂ ceiling after 2027 | 5 | 7.5 | 10 | %/yr | POL-02, POL-05: the peloton MKI is tightened by at least 7.5%/yr. The 2025→2027 ceiling path in POL-01 ("outside": 183 → 169 → 155 kg CO₂/m³) is −7.6% and −8.3%/yr. Extrapolation from 2027: "outside" 143 (2028), 133 (2029), 123 kg (2030); "inside" 132 (2028), 122 kg (2029). The real GWW-decree levels are not set yet (POL-17). | L |
| A-VP-04 | Make-up of the 90k m³/yr P2 volume | – | ~35k existing customer book + ≥40k frameworks + ~15k new project/spot sales | – | m³/yr | ESTIMATE. Existing book ≈ an average plant, 33.7k m³ (CMP-43), partly kept (A-OPT-08). Frameworks = pre-condition (c). The rest is the gap to 90k. | L |
| A-VP-05 | Maximum spend before all three gates pass (due diligence, legal, LOIs, crushing-permit pre-study, first EPD scoping) | 0.15 | 0.25 | 0.35 | M€ | ASSUMPTION. Close to the €0.2M transaction/permit-change budget in P2 (A-OPT-07). This is the money at risk if the project stops at a gate. | L |
| A-VP-06 | Demolition partner's alternative ("road-base route"): crush itself and sell mixed granulate | – | crushing cost €7.5/t, granulate value €3/t, steel 3% × €150/t kept by partner | – | €/t rubble | ESTIMATE from A-OPT-05 / OPT-04 (contract crushing €7.5/t), A-MKT-14 (menggranulaat €3/t, €0–8), A-TEC-03 and A-CST-32 (steel). Partner net on the road-base route ≈ 3 − 7.5 + 4.5 = **€0/t**. With us (gate fee G, we pay €7.5/t crushing, we keep steel): partner net = 7.5 − G. So the partner is better off with us while G < ~€7.5/t (steel to us) or G < ~€12/t (steel to partner). The road-base value of concrete-rich granulate should fall as the cap goes 30% → 15% → 5% (MKT-11), which raises the gate fee the partner will accept. | L |
| A-VP-07 | Gate-fee tiers by rubble quality | clean A1-type €5; reinforced €3; mixed/out of spec: rejected or €20+ | clean €7.5; reinforced €5 | clean €10; reinforced €7.5 | €/t | ASSUMPTION for the contract design. Anchors: BE clean concrete €0–1/t, reinforced €2–5.5/t (MKT-20–22); NL small-load counter tariff ~€20/t (MKT-23); disposal of contaminants €120/t (A-CST-33). The model uses one blended gate fee (A-MKT-15). | L |
| A-VP-08 | Delivery-zone surcharge above the average distance | €0.4 | €0.5 | €0.6 | €/m³ per extra km one-way | ESTIMATE from the delivery-cost formula €9 + €0.5 × km (A-TEC-28; price_breakdown.md §6). P2 average distance is 22 km (A-OPT-17). | M |
| A-VP-09 | Stop rule for the asset-light fallback pilot (O6) | – | max €0.5M over 2 years; continue only with ≥3 paying licensee plants signed by end-2028 | – | – | ASSUMPTION. O6 breaks even at ≈10 licensees and has NPV −€2.51M in the model (viability_options.md §3, O6). A capped pilot limits the loss. | L |
| A-VP-10 | Framework clause: pass binder cost changes (carbon + slag) 100% into the framework price | 80 | 100 | 100 | % pass-through | ASSUMPTION for the contract design. The model's market pass-through is 80% (A-CST-13). Run R-15: 100% on all volume → P2 NPV +€0.38M. | L |
