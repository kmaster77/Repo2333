# Assumptions — Agent 3 (Technology & supply chain)

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
