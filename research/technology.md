# Technology, operations and supply chain — circular ready-mix (B1) vs prefab (B2)

Agent 3 (Technology & supply chain analyst). Date: 2026-10-22. Prices in 2026 €, excl. VAT.
Sources: `research/sources_technology.md` (TEC-xx). Assumptions: `research/assumptions_technology.md` (A-TEC-xx).
Labels: **[VERIFIED]** = source read; **[ESTIMATE]** = calculated from sources (calculation shown); **[ASSUMPTION]** = no source, reasoning given.

---

## 0. Summary (for the orchestrator and Agents 5–6)

1. **Recommendation: B1 ready-mix as the base case.** Base plant: one stationary 120 m³/h plant, ~70,000 m³/yr at steady state, ~1.5 ha (waterside preferred), ~10 FTE plus ~8 subcontracted truck mixers, capex ≈ **€5.5M** excl. land and trucks (range €4–8M) [ESTIMATE, A-TEC-21/24]. A prefab plant (B2) of 30,000 m³/yr needs ≈ **€25M** (range €18–40M) and ~75 FTE [ESTIMATE, A-TEC-34/35]. See §8.
2. **Recycled aggregate gives circularity, not CO₂.** In NMD data, replacing 30% of gravel with betongranulaat lowers MKI by only **€0.49/m³ (−2%)** [VERIFIED, TEC-04]. The binder is the CO₂ lever: CEM I → CEM III/B lowers MKI from **€34.59 to €26.01/m³ (−25%, A1-set)** and CO₂ from ≈276 to ≈126 kg/m³ (−55%) [VERIFIED MKI TEC-04; ESTIMATE CO₂ §4.4].
3. **Rules allow far more recycled aggregate than the market uses.** NEN 8005: 30% (Type A1) / 20% (A2) of coarse aggregate in most exposure classes, 50% in X0; CUR-Aanbeveling 112: up to 100% under conditions; CROW-CUR 127: 100% coarse + 60% fine at ~45 MPa [VERIFIED, TEC-01]. Actual use: only ~6% of aggregates in concrete are secondary [VERIFIED, TEC-68].
4. **Conventional crushing gives ~58% coarse RCA and ~38% 0/4 sand** per tonne of rubble [ESTIMATE, A-TEC-01/02]. Advanced dry processes (Smart Liberator, everox/ADR) also recover sand and a cement-paste fraction; everox guideline: 60% coarse, 15% sand, 20% activated cement paste, 5% filler [VERIFIED, TEC-21].
5. **Anchor corrections:** C2CA is now **everox** (C2CA Technology BV); its first commercial plant (JV with Dura Vermeer, 's-Gravendeel) is permitted for **100,000 t/yr** and due ~2027 [VERIFIED, TEC-22/23/25]. SmartCrusher/SlimBreker technology is run commercially as **"Smart Liberator" by Rutte Groep, spun off in 2026 as SL Materials** [VERIFIED, TEC-29]. NEN 8005 limits are by **RCA density type and exposure class, not by strength class** [VERIFIED, TEC-01]. MKI changes to the **A2 weighting set** (MPG since 1 July 2026; Rijkswaterstaat tenders from 2027) and values roughly **double** [VERIFIED, TEC-07/08]. Ready-mix open time in NL is **1.5–2 h**, not 60–90 min [VERIFIED, TEC-45/46].

---

## 1. Process flows

### 1.1 B1 — circular ready-mix plant (base case: recycled aggregate bought)

```
 DEMOLITION SITES ──► certified crushers (BRL 2506-1, KOMO)          own crushing = option A+B
                         │  betongranulaat 4/16, 4/22 type A1; fijngranulaat 0/4
                         ▼
 [1] SOURCING  frame contracts with 2–4 crushers within 30–50 km; truck or barge
                         ▼
 [2] INTAKE    weigh, visual check, lot certificate; own samples per lot:
               density + water absorption (EN 1097-6), constituents (EN 933-11),
               sulphate/chloride (EN 1744-1) at set frequency
                         ▼
 [3] STORAGE   separate covered bins per fraction AND per source; sprinklers keep
               RCA moist near saturated-surface-dry (SSD) so water demand is stable
                         ▼
 [4] BATCHING  moisture probes in bins → automatic water correction; weigh RCA,
               gravel, sand, binder(s) (CEM III/B, CEM I/III-A, SCM e.g. ACP), water,
               admixtures (superplasticiser, retarder)
                         ▼
 [5] MIXING    twin-shaft mixer 2–3 m³ per batch (≈120 m³/h); check consistency
                         ▼
 [6] LOADING   truck mixer 9–14 m³; delivery ticket (recipe, time of water addition)
                         ▼
 [7] DELIVERY  placed within 1.5–2 h of production → radius ≈25–50 km
                         ▼
 [8] SITE      chute / pump; contractor places and cures
 QC & certification (whole chain):
   • Factory production control to NEN-EN 206 + NEN 8005; cubes at 28 days
   • KOMO product certificate under BRL 1801 (Kiwa or SKG-IKOB audits). BRL 1801
     explicitly allows recycled granulates (not AEC granulate) [VERIFIED, TEC-58]
   • No CE marking: there is no harmonised EN for betonmortel [VERIFIED, TEC-59]
   • For tenders: product-specific LCA in NMD (category 1) or MKI certificate
     (Kiwa BRL K11002); optional CSC certificate with "R-module" for recycled content
```

### 1.2 B2 — circular prefab plant

```
 [1–4] same sourcing / intake / storage / batching as B1 (plant has its own mixer)
                         ▼
 [5] MIXING    in-plant mixer; concrete carried by bucket or conveyor to the line
                         ▼
 [6] MOULDS    carousel pallets or fixed steel moulds; shuttering robot; rebar cages
               or mesh, inserts, (pre)stressing strands for hollow-core / beams
                         ▼
 [7] CASTING   vibration or self-compacting concrete (SCC)
                         ▼
 [8] CURING    heated beds or curing chamber (≈30–60 °C), 12–24 h
                         ▼
 [9] DEMOULD   needs early strength (typ. 10–20 MPa) for lifting/turnover
               → low-clinker binders (slow early strength) are harder here
                         ▼
 [10] FINISH & INSPECT  dimensions, cracks, surface; labelling / material passport
                         ▼
 [11] YARD     days–weeks storage; 28-day strength reached
                         ▼
 [12] DELIVERY flatbed trucks, radius 100–200 km; crane assembly on site
 QC & certification:
   • CE marking + Declaration of Performance under harmonised precast standards
     (EN 13369 general rules + product standards, e.g. EN 1168 hollow-core,
     EN 13225 linear elements, EN 14992 wall elements) [ASSUMPTION: standard list
     from domain knowledge, not opened this session]
   • Voluntary KOMO product certificate + factory production control
```

### 1.3 Archetype A — recycling hub (upstream step that B depends on)

```
 [A1] PRE-DEMOLITION AUDIT  drawings, cores, XRF/petrography of concrete; asbestos
                            inventory; plan "harvest streams" per element type
 [A2] SELECTIVE DEMOLITION  strip-out (asbestos, gypsum, wood, plastics, insulation);
                            keep concrete streams separate (e.g. beams vs foundations)
 [A3] PRE-CRUSH ON SITE     hydraulic pulveriser / mobile jaw; remove rebar
 [A4] TRANSPORT             truck to hub (or mobile plant on site)
 [A5] HUB INTAKE            weigh, inspect, acceptance fee
 [A6] CRUSHING              primary jaw → magnet → secondary impact or cone crusher
 [A7] SCREENING & CLEANING  screens (0/4, 4/16, 4/22); wind sifter, hand picking,
                            float-sink or washing for light contaminants
 [A8] ADVANCED (option)     Smart Liberator / ADR + heating-air classifier → clean
                            gravel, sand and cement-paste fines; paste activation
 [A9] TESTING & CERT        BRL 2506-1 (KOMO) per fraction; EN 12620 + NEN 5905
 [A10] STOCK & SELL         coarse RCA to concrete plants; 0/4 to concrete (limited)
                            or road base / fill; fines to cement plants (option)
```
Why selective demolition matters: RCA from sorted structural members of a Dutch viaduct had water absorption of **1.5–4% (coarse)** and **2–6% (fine)**, against **~8%** for 0/4 from concrete rubble of unknown origin [VERIFIED, TEC-33].

### 1.4 Archetype C — element reuse (extra steps)

Based on CROW-CUR Richtlijn 4:2023 "Hergebruik constructieve prefab betonelementen" (annex A hollow-core slabs, annex B prestressed bridge girders) [VERIFIED, TEC-64]:
```
 [C1] Desk study: archive drawings, original calculations, element types
 [C2] On-site inspection: cracks, damage, carbonation, chlorides, connections
 [C3] Deconstruction plan: sequence, temporary stability, lifting points
 [C4] Disconnection: saw wet joints and structural topping; lift; label (RFID/BIM)
 [C5] Transport + temporary storage
 [C6] Assessment: geometry & tolerances; cores for strength; reinforcement and
      prestress condition; non-destructive + destructive tests; sometimes full-scale
      load tests (hollow-core)
 [C7] Refurbish: cut to new length, remove parapets/finishes, repair
 [C8] Re-design with measured properties; engineer's declaration (no standard CE route)
 [C9] Reuse in new structure; record in material passport
```
Evidence: in the Dutch ReCreate pilot (Prinsenhof, Arnhem) **707 elements** were deconstructed and **539 (76%) were classified technically reusable**; a smaller subset was actually re-used; issues were sawing of wet joints and dimensional mismatch [VERIFIED, TEC-65].

---

## 2. Mass balance per tonne of demolition-concrete input

Input = 1 t of "clean" concrete rubble (BRL 2506 quality, incl. reinforcement). Values are mass %. Base values; ranges in A-TEC-01…07.

### 2.1 Yields

| Output | (a) Conventional jaw + impact crushing, screening | (b) SmartCrusher / Smart Liberator (dry liberation) | (c) everox: ADR + HAS + activation (TU Delft origin) | (d) Thermal-mechanical (300–700 °C + rubbing) |
|---|---|---|---|---|
| Steel scrap (sold) | 3 | 3 | 3 | 3 |
| Light contaminants (to waste/energy) | 1 | 1 | 1 | 1 |
| Coarse aggregate (≥4 mm) | **58** (4/16–4/22, with adhered mortar) | **44** ("Freegravel", clean gravel) | **58** ("RCA", 4–16 mm) | **45** (very clean) |
| Sand (≈0.125/0.25–4 mm) | **38** as 0/4 incl. fines (one product) | **28** ("Freesand") | **14** ("RFA", 0.25–4 mm) | – (part of fines) |
| Cement-paste-rich fines (<0.125/0.25 mm) | in 0/4 above (≈5–10 of input) | **24** ("Freement" fine + coarse) | **19** ("ACP", activated SCM) + **5** inert quartz filler | **51** fines + sand mix |
| Source / label | ESTIMATE A-TEC-01/02 (TEC-35, TEC-36, TEC-18) | ASSUMPTION A-TEC-05 (no published balance) | VERIFIED guideline 60/20/15/5 of output (TEC-21), scaled to 96% recovered | ESTIMATE A-TEC-07 (TEC-34) |

Check: each column sums to 100.

### 2.2 Quality of each output

| Fraction | Conventional | Smart Liberator | everox / ADR-HAS | Thermal |
|---|---|---|---|---|
| Coarse: density (SSD) | ≈2,480 kg/m³ from rotor/impact crusher [VERIFIED, TEC-33]; must be ≥2,200 (Type A1) or ≥2,000 (A2) [VERIFIED, TEC-01] | 2,580–2,610 kg/m³ (highest of methods tested) [VERIFIED, TEC-33] | Clean 4–12 mm, ultrafines <1.5%, LA ≤40 [VERIFIED, TEC-18] | Near-natural |
| Coarse: water absorption | 1.5–4% (selected sources) to 5–7% (unknown rubble) [VERIFIED TEC-33; A-TEC-10] | low end (≈1.5–2.5%) [ESTIMATE from TEC-33 trend] | "reasonable", higher than natural [VERIFIED, TEC-18] | ≈1–3% [ASSUMPTION] |
| Coarse: adhered paste | 8.5–17% by mass [VERIFIED, TEC-33] | lower | low | very low |
| Sand: paste / WA | 0/4: 13–21% paste; WA 3–8%; sulphate up to 0.19% (limit 0.2%) in unknown rubble [VERIFIED, TEC-33] | 0.125–4 mm: 11.6–12.2% paste [VERIFIED, TEC-33] | 0.25–4 mm; WA high because dried and some paste left [VERIFIED, TEC-18] | – |
| Fines | mostly not separated → road base / fill | <0.125 mm: ~41% paste; sulphate 0.26% (above 0.2%) [VERIFIED, TEC-33]; Rutte claims ~50% of cement unhydrated (company claim, TEC-31) | ACP: "reactivity similar to fly ash", 11 kg CO₂/t, replaces up to 30% cement; certification pending [VERIFIED company claims, TEC-21/25] | large fines stream, cement-rich |
| Energy | ≈37 MJ/t primary (~0.1–0.6 l diesel/t incl. loaders) [VERIFIED TEC-34, TEC-39; A-TEC-08] | claim <1 kWh/t (SC1, 20 t/h) [VERIFIED claim TEC-28]; base 3 kWh/t [A-TEC-09] | HAS heated with diesel today (biofuel planned) [VERIFIED, TEC-18]; ACP process ~11 kg CO₂/t [claim TEC-25] | **1,400–2,300 MJ/t (36–62× conventional)**; ≈200 kg CO₂/t if fossil-fired [VERIFIED, TEC-34] |
| Capacity per unit | 150–600 t/h mobile [VERIFIED, TEC-39/40] | 20 t/h (SC1), ~40 t/h (SC2); ~130,000 t/yr per machine [VERIFIED, TEC-27, TEC-30] | ADR 50 t/h; HAS 3 t/h (2020); FOAK 100 kt/yr; "standard plant" up to 500 kt/yr [VERIFIED, TEC-18, TEC-22, TEC-24] | batch kilns |

**Implication for B1:** with bought conventional RCA, ~60% of each tonne of rubble becomes concrete-grade coarse aggregate. The 0/4 sand and fines are the bottleneck for "100% circular" (Betonakkoord targets: sand 50% by 2025, 100% by 2030; binder/filler 25% by 2025 [VERIFIED, TEC-67]). Only advanced processes deliver usable sand and paste at scale.

---

## 3. Quality issues, tests and effect on mix design

| Issue | Test (standard) | Typical RCA value | Limit / rule | Effect on mix design and operations |
|---|---|---|---|---|
| Particle density | EN 1097-6 | coarse 2,480–2,610 kg/m³ [TEC-33] | Type A1 ≥2,200; Type A2 ≥2,000 (NEN 8005) [TEC-01] | Sets the allowed replacement %; lower density → lower E-modulus |
| Water absorption (WA) | EN 1097-6 (WA24); WA at 60 min ≈ 90–100% of 24-h uptake [VERIFIED, TEC-33] | coarse 1.5–7%; fine 2–8% [TEC-33, TEC-38]; natural gravel ≈0.5–1.5% [ASSUMPTION] | none direct; drives water demand | Pre-wet RCA to SSD or add absorption water (≈15–40 l/m³, not counted in w/c) [ESTIMATE A-TEC-12, TEC-84]; risk of slump loss in the truck mixer; moisture probes needed; +0–0.5% superplasticiser [A-TEC-13] |
| Adhered mortar / cement paste | EN 1744-5 (acid-soluble) | coarse 8.5–17%; 0/4 11.6–21.5%; powder 27–41% [VERIFIED, TEC-33] | – | More paste → lower strength, more shrinkage and creep. CUR 112 gives adjusted design values above 50% replacement [VERIFIED, TEC-01] |
| Constituents / contamination (brick, asphalt, glass, wood, plastic, gypsum) | EN 933-11 | depends on demolition | BRL 2506; e.g. Rc+Ru ≥90%, Rb ≤10%, Ra ≤1%, X ≤1%, floating ≤2 cm³/kg (as used in EN 197-6 note) [VERIFIED, TEC-90] | Selective demolition + sorting; wind sifter; not for fair-faced (schoon) concrete [VERIFIED, TEC-02] |
| Sulphate (gypsum) | EN 1744-1 (water-soluble) | 0.19% in unknown 0/4; up to 0.26% in fines [VERIFIED, TEC-33] | ≤0.2% (SS0.2, NEN-EN 12620) [VERIFIED, TEC-33] | Limits fine-RCA share; source selection; testing per lot |
| Chlorides | EN 1744-1 / EN 1744-5 | ≤0.02% [VERIFIED, TEC-33]; marine structures 0.07–0.24% | concrete ≤0.4% of cement mass for reinforced (NEN-EN 206) | 100% RCA → ≈0.11% of cement: OK [VERIFIED, TEC-33]; avoid marine-origin rubble for reinforced work |
| Alkali-silica reaction (ASR) | Petrography; Dutch guidance CUR-Aanbeveling 89 [ASSUMPTION: not opened] | old gravel may be reactive; extra alkalis from paste | prevention measures | CEM III/B (slag ≥ ~65%) is the usual Dutch preventive measure [ASSUMPTION]; carbonation of RCA can cut ASR expansion 20–50% (lab) [VERIFIED, TEC-88] |
| Strength loss | cubes EN 12390-3 | −0.19% per 1% coarse RCA; −0.24% per 1% fine RCA [VERIFIED, TEC-37]; ≤30% often no significant loss [VERIFIED, TEC-38] | – | At 50% coarse RCA: lower w/c by ~0.02–0.04 ≈ **+15 kg/m³ binder** (range 0–30) [ESTIMATE, A-TEC-11] |
| Abrasion | LA, EN 1097-2 | within limits [TEC-18] | LA ≤40 for RCA [VERIFIED, TEC-18] | Wear surfaces / pavements: check |
| Fines content | EN 933-1 | coarse 1.3–1.5% (<0.063) [VERIFIED, TEC-36] | EN 12620 category | Higher water demand if high |

**Quality-control cost driver:** RCA properties vary per source and per lot. A plant using several RCA sources needs (a) separate bins per source, (b) per-lot density/WA tests, (c) automatic moisture correction. This is cheap at the plant (a lab technician, probes) but it is the main technical risk for ready-mix (slump drift during the 1.5–2 h open time).

---

## 4. Mix designs, binders, CO₂ and MKI

### 4.1 Allowed recycled aggregate (cross-check of the "NEN 8005 by strength/exposure class" anchor)

| Rule | Coarse RCA replacement (by volume of coarse aggregate) | Fine RCA | Notes |
|---|---|---|---|
| NEN 8005 (Dutch annex to NEN-EN 206) | Type A1 (ρ ≥2,200): **X0 50%, other exposure classes 30%**; Type A2 (ρ ≥2,000): X0 50%, others 20% [VERIFIED, TEC-01, TEC-02] | not in this table | Limit depends on **density type and exposure class**, not on strength class. Anchor corrected. |
| Betonhuis practice | "≤20% allowed in almost all concrete structures"; extra care for fair-faced concrete and de-icing salts [VERIFIED, TEC-03] | – | Producers sell "20% granulaat" mixes across C12/15–C55/67 [VERIFIED, TEC-75] |
| CUR-Aanbeveling 112 | up to **50%** without changing structural design rules; **50–100%** with adjusted design values, some exposure classes excluded [VERIFIED, TEC-01] | – | Main route for high-RCA ready-mix |
| CROW-CUR Aanbeveling 127:2021 | up to **100% coarse** | up to **60% fine** | Based on concrete of ~45 MPa made with two innovative recycling methods [VERIFIED, TEC-01] |
| CUR-Aanbeveling 80 / 106 | mixed granulate / fine aggregate | – | Mentioned as Dutch pre-standards [VERIFIED, TEC-76] |

### 4.2 Low-clinker binders

| Binder | Clinker | GWP (kg CO₂-eq/t) | Status in NL | Fit for B1 / B2 |
|---|---|---|---|---|
| CEM I | 95–100% | 700–880 (base 800) [A-TEC-14; TEC-11, TEC-13] | mainstream reference | high early strength (prefab) |
| CEM III/A | 35–64% | ≈440–560 [TEC-12, TEC-15] | mainstream | prefab/ready-mix |
| **CEM III/B** | 20–34% | 280–360 (base 320) [A-TEC-15; TEC-13, TEC-14] | **mainstream in NL** (TRL 9) | very good for ready-mix (slow early strength OK; ASR/chloride resistant). Weaker for prefab turnover. **Supply risk after ~2030**: Tata Steel replaces Blast Furnace 7 (≈60% of coal-based output) by DRI+EAF, first DRI 2028–2030 [VERIFIED, TEC-70, TEC-71]; Heidelberg Materials' IJmuiden plant (1.4 Mt/yr) grinds slag next door [VERIFIED, TEC-72] |
| CEM III/C | 5–19% | lower than III/B | available; NMD card exists (C30/37 MKI €23.64) [VERIFIED, TEC-04] | ready-mix massive / low-heat uses |
| CEM II/C-M, CEM VI (EN 197-5, 2021) | 50–64% / 35–49% | ≈454 / ≈340 [VERIFIED, TEC-16] | standard exists; NL use needs NEN 8005 / CROW-CUR 48 assessment [VERIFIED for EN 197-6 types, TEC-17] | **Not lower-CO₂ than CEM III/B**; a hedge if slag gets scarce |
| CEM II/A-F, B-F (EN 197-6, 2023): recycled concrete fines up to 35% | 65–94% | between CEM I and CEM II/B | new; needs NL assessment [VERIFIED, TEC-17] | outlet for paste fines |
| Activated cement paste (everox ACP) as SCM | 0% | ≈11 (claim) [TEC-25] | replaces up to 30% cement; certification via EN 197-6 / ETA in progress [VERIFIED, TEC-21, TEC-25]; TRL 6–7 | ready-mix and prefab, from ~2027–2028 if certified |
| Geopolymer / alkali-activated (slag + fly ash + waterglass/NaOH) | 0% | NMD C30/37 card exists | KOMO BRL 8803 for geopolymer concrete in draft (2025) [VERIFIED, TEC-61] | niche; mostly prefab/products; fly ash supply falling |
| Calcined clay (LC3) | ~50% | ≈CEM II/C | **no NL supply evidence found** — data gap | – |

Typical binder content for C30/37 in NMD reference mixes: **320 kg CEM I or 330 kg CEM III/B per m³**; minimum binder in NEN 8005 rises with exposure class (e.g. X0 200, XC1 260 kg/m³) [VERIFIED, TEC-04, TEC-75].

### 4.3 Reference and circular C30/37 mixes (per m³)

NMD category-3 mixes are VERIFIED (TEC-04, Table 6A/6C, v6 March 2025). "C2" and "C3" are this agent's proposed circular mixes [ESTIMATE].

| Mix | Gravel | Coarse RCA | Sand | Fine RCA | Binder | Water | Notes |
|---|---|---|---|---|---|---|---|
| R1 C30/37 CEM I | 1,241 | 0 | 639 | 0 | 320 CEM I | 165 | NMD reference |
| R2 C30/37 CEM III/B | 1,241 | 0 | 639 | 0 | 330 CEM III/B | 165 | NMD |
| C1 C30/37 CEM III/B – 30% granulaat | 760 | 330 | 810 | 0 | 320 CEM III/B | 170 | NMD (30% of coarse mass) |
| R3 C30/37 CEM I – 30% granulaat | 735 | 310 | 805 | 0 | 285 CEM I | 175 | NMD |
| G C30/37 geopolymer | 920 | 0 | 700 | 0 | 133 fly ash + 267 slag + 18.5 waterglass + 11.5 NaOH + 10 retarder | 150 | NMD |
| **C2 "Circular 50/25"** | 620 | 560 | 480 | 150 | 345 CEM III/B (+15 kg, A-TEC-11) | 165 eff. + ~28 absorption | 50% coarse vol (CUR 112), 25% fine (within CROW-CUR 127) [ESTIMATE] |
| **C3 "Circular-plus"** | 620 | 560 | 480 | 150 | 290 CEM III/B + 55 ACP | 165 eff. + ~28 absorption | needs ACP certification (≥2027–28) [ESTIMATE] |

Strength classes reachable: C30/37–C45/55 with ≤50% coarse RCA under CUR 112 [ESTIMATE from TEC-01, TEC-75]; ~45 MPa with 100% coarse + 60% fine (CROW-CUR 127) [VERIFIED, TEC-01]; everox best mixes 52.3 MPa (C40/50) [VERIFIED claim, TEC-24]; C2CA (FP7) found +4 mm RCA concrete 25–30% stronger than virgin in tests [VERIFIED claim, TEC-19].

### 4.4 CO₂ and MKI per m³

**MKI (A1 weighting set, NMD cat. 3, €/m³, modules A1–D)** [VERIFIED, TEC-04 Table 16A/C]:

| Mix | A1 | A2 | A3 | A1–A3 | Total A1–D | vs R1 |
|---|---|---|---|---|---|---|
| R1 CEM I | 24.96 | 1.55 | 0.19 | 26.70 | **34.59** | – |
| R3 CEM I – 30% granulaat | 22.04 | 1.63 | 0.19 | 23.86 | 31.71 | −8% |
| R2 CEM III/B | 16.72 | 1.60 | 0.19 | 18.51 | **26.01** | −25% |
| C1 CEM III/B – 30% granulaat | 15.85 | 1.81 | 0.19 | 17.85 | **25.52** | −26% |
| CEM III/C | 14.46 | 1.60 | 0.19 | 16.25 | 23.64 | −32% |
| G Geopolymer | 14.14 | 3.75 | 0.19 | 18.08 | 25.26 | −27% |
| C2 Circular 50/25 [ESTIMATE] | 16.24 | 2.25 | 0.19 | 18.68 | **≈26.4** | −24% |
| C3 Circular-plus [ESTIMATE] | 14.00 | 2.03 | 0.19 | 16.22 | **≈23.9** | −31% |

How C2/C3 were estimated: solving the NMD mix pairs gives A1 MKI factors of **€0.070/kg CEM I, €0.043/kg CEM III/B, €0.0014/kg primary aggregate, €0 for RCA** (NMD models betongranulaat burden-free) [ESTIMATE, A-TEC-17]. C2 A1 = 345×0.0426 + 1,100×0.0014 = 16.24. A2 = (345×0.3 t·km cement + 0.71 t×50 km RCA) × €0.0162/tkm = 2.25. A4–D taken from C1, the NMD mix with RCA (7.67). C3 adds 55 kg ACP at ~€0.002/kg [A-TEC-20].

**A2 weighting set (now in force):** NMD's impact analysis shows C30/37 CEM I **€32.48 → €70.61**, CEM III **€19.79 → €42.35**, CEM III + 30% granulaat **€19.75 → €42.30** (A1-set → A2-set) [VERIFIED, TEC-05]. Multiply A1-set values by ≈2.15 for 2027+ tenders [A-TEC-18]. Note: TEC-04 and TEC-05 use different card versions, so A1 values differ slightly (34.59 vs 32.48); use one dataset consistently in the model.

**Tender ceilings:** Rijkswaterstaat RTD 1033 caps MKI per m³ betonmortel (excl. reinforcement) for C30/37 at **€16.1 (2025–26), €15.4 (2027–28), €14.7 (2029–30)** [VERIFIED, TEC-06]. Generic cat-3 values above exceed these; producers meet them with product-specific (cat. 1) data, which carry no 30% cat-3 surcharge [ASSUMPTION A-TEC-19 — verify with Agent 1]. These ceilings were set in the A1-set and will need recalibration for the A2-set from 2027 [ESTIMATE from TEC-07].

**GWP (kg CO₂-eq/m³, A1–A3)** [ESTIMATE: binder × factor + 20 kg for aggregates, transport, plant; A-TEC-14/15/16]:

| Mix | Calculation | Base | Range |
|---|---|---|---|
| R1 CEM I | 320 × 0.80 + 20 | **276** | 239–312 |
| R2 CEM III/B | 330 × 0.32 + 20 | **126** | 107–149 |
| C1 CEM III/B 30% RCA | 320 × 0.32 + 21 | **123** | 105–146 |
| C2 Circular 50/25 | 345 × 0.32 + 21 | **131** | 113–145 |
| C3 Circular-plus | 290 × 0.32 + 55 × 0.011 + 21 | **114** | 97–126 |

Cross-checks: Dutch average concrete 266 kg/m³ in 2023 [VERIFIED, TEC-09]; CSC baseline for C30/37 318 kg/m³ (gross) [VERIFIED, TEC-10]. R1 at 276 sits between these.

**Key message for the business case:** the CO₂/MKI story must be sold on the **binder** (CEM III/B now, ACP/other SCMs later). Recycled aggregate adds a circularity claim (Betonakkoord, raw-material scarcity) but changes MKI by only ±2%. A high-RCA mix that needs extra cement can even be slightly worse than plain CEM III/B (C2 vs R2).

---

## 5. Equipment and plant

| Item | B1 ready-mix (base) | B2 prefab | Mobile crushing line (A, option) | Stationary high-grade RCA plant (A) | Advanced liberation plant (A) |
|---|---|---|---|---|---|
| Capacity | 120 m³/h; theoretical ~240,000 m³/yr per shift [A-TEC-23] | 30,000 m³/yr structural elements (walls, beams, slabs) | 250–350 t/h impact crusher [TEC-39, TEC-40] | 300–450 kt/yr | ~100 kt/yr (everox FOAK permit) [TEC-22] |
| Steady-state output | **70,000 m³/yr** (50–90k) [A-TEC-24] | 30,000 m³/yr | job-based | 300 kt/yr | 100 kt/yr |
| Capex | **€5.5M** (4–8) excl. land & trucks [A-TEC-21]; 8 mixers if bought ≈ €1.1M (€135k each) [TEC-49, A-TEC-31] | **€25M** (18–40) [A-TEC-34]; anchor VBI ~€20M for 1M m²/yr hollow-core [TEC-54] | €1.6M (1.0–2.5) [A-TEC-40] | €10M (6–15); anchor UK £8M for 450 kt/yr [TEC-74] | €15M (8–30), no public data [A-TEC-42] |
| Energy | 3.6 kWh electricity + 4.4 MJ diesel per m³ [VERIFIED, TEC-04] | + 10–50 kWh/m³ curing heat [A-TEC-37] | 0.11 l/t crusher; 0.15–0.6 l/t all-in [TEC-39, A-TEC-08] | similar + washing water | 1–8 kWh/t [A-TEC-09]; HAS heat extra |
| Wear parts | mixer liners/blades every 40–60k m³ [TEC-57, vendor] | moulds, pallets | €0.2–0.8/t blow bars, liners [A-TEC-43] | same | Hardox wear core (Smart Liberator) [TEC-31] |
| Staff | ~10 FTE + ~8 drivers (subcontracted) [A-TEC-25, A-TEC-30] | ~75 FTE [A-TEC-35] | 2–3 per shift | 10–20 | 10–20 [ASSUMPTION] |
| Footprint | 1.5 ha (1–2.5) [A-TEC-22] | 5 ha (3–8) [A-TEC-36]; Goldbeck plant ~2 ha [TEC-56] | on site | 2–4 ha [ASSUMPTION] | 1–3 ha; compact, container-size units [TEC-31, TEC-24] |
| Utilisation | 20–40% of theoretical (peaky demand) [A-TEC-24] | 60–80% (2 shifts possible) [ASSUMPTION] | 40–60% | 60–80% | ramp-up risk |
| Lifetime | plant 25 yr; truck mixer 10 yr [A-TEC-39] | carousel 25 yr; moulds 10 yr | 10–12 yr | 20 yr | unknown |
| Build time | ~12–18 months incl. permit [ASSUMPTION] | ~15 months build (VBI: first pile Mar 2025 → production Jun 2026) [VERIFIED, TEC-55] + permits | weeks | 1–2 yr | 2+ yr (everox JV 2024 → ~2027) [TEC-26, TEC-25] |

---

## 6. Logistics

| Item | Value | Label |
|---|---|---|
| Ready-mix open time | "about 1.5–2 hours after production", depends on admixtures and temperature | VERIFIED, TEC-45, TEC-46 |
| Delivery radius | ≈25–50 km in practice; NMD models ~50 km (118 tkm/m³ ÷ 2.37 t/m³) | ESTIMATE from TEC-04 |
| Truck mixer | 9–14 m³ per load; ~43 t loaded; 8x4 / 10x4 or semi-trailer | VERIFIED, TEC-47, TEC-48, TEC-51 |
| Truck mixer cost | €95–130/h all-in (base €110) | ESTIMATE, A-TEC-27 (TEC-47 €120–140/h retail; TEC-50 €85/h standby) |
| Delivery cost per m³ | ≈ **€9 + €0.5 × one-way km** → €14 at 10 km, €19 at 20 km, €26 at 35 km | ESTIMATE, A-TEC-28 |
| Fleet for base plant | 70,000 ÷ 9,000 m³/truck ≈ **8 mixers** | ESTIMATE, A-TEC-30 |
| Aggregate by road | ≈ **€0.25 per t per loaded km** + €1.5–3/t handling (KiM 2021 truck+trailer €0.246/tkm average, ×1.26) → 40 km ≈ €12/t | ESTIMATE, A-TEC-32 (TEC-41) |
| Aggregate by inland ship | ≈ **€0.015–0.05 per t·km** + €1.5–4/t transshipment (KiM 2021: small ship €0.036, push barge €0.010) | ESTIMATE, A-TEC-33 (TEC-41) |
| CO₂ per t·km | truck 106 g; inland ship 35 g | VERIFIED, TEC-15 |
| Typical distances | cement ~300 km (much from Germany/Belgium) [VERIFIED NMD assumption, TEC-04]; RCA ~50 km by truck [VERIFIED NMD assumption, TEC-04]; primary sand/gravel by ship from river/sea sources [ASSUMPTION] | |
| Prefab delivery | 100–200 km by flatbed; less time-critical | ASSUMPTION |

**Implications:** (1) a waterside plant can save ~€4–8/t on primary aggregate versus a 40 km truck haul (truck ≈€12/t; ship 100 km ≈€3/t + €2.5/t transshipment) → ~€5–10/m³ on ~1.3–1.9 t primary aggregate per m³ [ESTIMATE, A-TEC-32/33]; a Belgian example moves 300,000 t/yr by canal to a new plant [VERIFIED, TEC-52]. (2) RCA comes from crushers spread around cities, so RCA is usually trucked; locate within ~30 km of 2–3 certified crushers (BRL 2506 register lists many; e.g. TEC-62, TEC-63). (3) Base plant RCA demand ≈ 70,000 m³ × 60% circular share × 0.71 t ≈ **30 kt/yr** [ESTIMATE, A-TEC-44/45] — about 0.6% of the ~4.7 Mt/yr of coarse concrete aggregate released in NL [VERIFIED volume, TEC-10]. Supply volume is not the constraint; certified concrete-grade quality and consistency are.

---

## 7. Technology readiness (TRL) and what is proven at scale in NL

| Technology | TRL | Proven at scale in NL today? | Source |
|---|---|---|---|
| Crushing to road-base granulate | 9 | Yes; ~18 Mt/yr RCA produced in NL, mostly road base | VERIFIED, TEC-33 |
| Crushing/screening to concrete-grade coarse RCA (BRL 2506-1, Type A1) | 9 | Yes, many KOMO-certified suppliers; but only ~6% of aggregates in concrete are secondary (≈3.3 Mt betongranulaat in 2022) | VERIFIED, TEC-62, TEC-68, TEC-10 |
| Ready-mix with 20–30% coarse RCA | 9 | Yes, standard products | VERIFIED, TEC-75, TEC-04 |
| Ready-mix with 50–100% coarse RCA (CUR 112) | 8 | Project-based | ESTIMATE |
| Fine RCA in structural concrete (CROW-CUR 127) | 7–8 | Limited, project-based | ESTIMATE (TEC-01) |
| Smart Liberator / SmartCrusher | 7–8 | One commercial operator (Rutte / SL Materials, Amsterdam); ~40 t/h units; claims 50,000 m³ recycled materials; partner New Horizon claims ~150,000 m³ concrete/yr (2023) | VERIFIED claims, TEC-27, TEC-29, TEC-32 |
| ADR (coarse separation) | 7–8 | Demonstrated 50 t/h; pilot Hoorn; ProRail/Green Village projects | VERIFIED, TEC-18, TEC-78 |
| HAS (sand/paste separation by hot air) | 6 | 3 t/h pilot (2020) | VERIFIED, TEC-18 |
| everox full chain incl. ACP | 6–7 | FOAK 100 kt/yr under construction ('s-Gravendeel), operational ~2027; ACP not yet certified | VERIFIED, TEC-22, TEC-25 |
| Thermal-mechanical (heating + rubbing) | 6–7 abroad; low relevance NL | No; 36–62× energy | VERIFIED, TEC-34 |
| High-voltage pulse / microwave | 4–5 | No ("laboratory phase") | VERIFIED, TEC-69 |
| CEM III/B | 9 | Yes, mainstream | VERIFIED, TEC-73 |
| CEM II/C-M, CEM VI | 8 | Standard since 2021; NL assessment route needed | VERIFIED, TEC-16, TEC-17 |
| EN 197-6 recycled-fines cements | 6–7 | Not yet in NL use | VERIFIED, TEC-17 |
| Geopolymer concrete | 7–8 | Niche; KOMO BRL in draft | VERIFIED, TEC-61 |
| Calcined clay / LC3 | 7–8 globally | No NL evidence found | data gap |
| Reuse of precast elements | 7 | Pilots (Prinsenhof; RWS bridge girders); guideline exists | VERIFIED, TEC-64, TEC-65 |

---

## 8. Recommendation: B1 ready-mix as base case

| Criterion | B1 ready-mix | B2 prefab | Edge |
|---|---|---|---|
| Capex | ≈€5.5M (4–8) for 70k m³/yr | ≈€25M (18–40) for 30k m³/yr | **B1** (~4–5× less, faster to build) |
| Technical risk | Proven plant tech (TRL 9). Risk = RCA moisture/slump control in transit; manageable with covered bins, probes, per-lot tests | Proven tech. Risk = early-strength need for demoulding conflicts with CEM III/B; element design/engineering capability needed | **B1** for low-clinker binders |
| MKI / CO₂ benefit | Full binder lever (CEM III/B, later ACP); RWS sets MKI caps per m³ betonmortel (direct tender pull) [TEC-06] | Smaller binder lever (needs CEM I/III-A for turnover) unless heat-cured; benefit sold per element | **B1** |
| Margin potential | Low value per m³; margin from scale, logistics and green premium | Higher value per m³ (engineering, assembly); but labour-heavy | **B2** in theory; not testable with public data (Agent 5) |
| Market access | Local (25–50 km), fragmented; many projects, low switching cost; strong incumbents (e.g. Mebin, Cementbouw, Dyckerhoff Basal, Bruil [VERIFIED names, TEC-89]) | Long sales cycles; strong incumbents (e.g. VBI with 7 plants + new 2M m² plant [TEC-53]) | **B1** for a newcomer |
| Ramp-up / time to revenue | 12–18 months | 2–3 years incl. permit | **B1** |
| Link to options A/C/D | Natural buyer of hub RCA (A) and ACP; easy to add own crushing later | Natural fit with element reuse (C) | neutral |

**Base plant (input for Agents 5–6):**
- 1 stationary plant, twin-shaft mixer 3 m³ (≈120 m³/h), 6–8 aggregate bins (3 dedicated to RCA 4/16, 4/22, 0/4), 4–5 binder silos (CEM III/B, CEM I or III/A, SCM/ACP, filler), covered RCA storage with sprinklers, moisture probes, in-house lab, wash-water recycling.
- Output ramp: 35k → 55k → **70k m³/yr** from year 3 (Agent 6 to set); 60% sold as circular mixes (C1/C2), 40% standard CEM III/B.
- Site 1.5 ha on a quay (barge supply of sand, gravel, cement), within ~30 km of 2–3 BRL 2506 crushers and inside a dense demand area (region choice: Agent 2).
- Staff ~10 FTE; ~8 truck mixers subcontracted (or bought: +€1.1M).
- Certification: KOMO BRL 1801 from start; product-specific NMD LCA (cat. 1) for 3–5 product families (~€20k each, A-TEC-47); CSC with R-module optional.
- Binder strategy: CEM III/B now; contract ACP/EN 197-6 or CEM VI supply as a hedge for the post-2030 slag decline.

---

## 9. Biggest data gaps

1. No public capex for a Dutch ready-mix plant, a prefab element plant (only a trade-press ~€20M for VBI hollow-core) or advanced recycling plants (Smart Liberator, everox).
2. No published mass balance for Smart Liberator; everox yields are a company guideline.
3. Truck-mixer cost per m³ is derived (A-TEC-28), not quoted.
4. Product-specific (cat. 1) MKI values of Dutch competitors are not public; cat. 3 values carry a surcharge (A-TEC-19, unverified).
5. ACP certification date and price; GGBS supply/price after 2030.
6. Calcined clay availability in NL.
