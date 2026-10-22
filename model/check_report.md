# Excel vs Python check - 2026-10-22

Method: `check_model.py` builds a copy of `financial_model.xlsx` per test case (scenario selector and/or values in the Override column), recalculates it with LibreOffice headless (`soffice --headless --convert-to xlsx`), reads the values with openpyxl (`data_only=True`) and compares them with `model_core.run()`. Tolerance: EUR 0.5 or relative 1e-07. Text results ('not reached', 'n/a') must match a Python `None`.

**Overall result: ALL CASES MATCH**

| Case | Result | NPV Python | NPV Excel | IRR Python | IRR Excel | max abs diff yearly lines (EUR) | max abs check row (EUR) | errors |
|---|---|---|---|---|---|---|---|---|
| Base (selector 2) | OK | -4,481,665 | -4,481,665 | -0.0706 | -0.0706 | 1.02e-08 | 6.40e-10 | 0 |
| Pessimistic (selector 1) | OK | -38,250,548 | -38,250,548 | - | - | 4.84e-08 | 0.00e+00 | 0 |
| Optimistic (selector 3) | OK | 29,963,057 | 29,963,057 | 1.1938 | 1.1938 | 4.66e-08 | 0.00e+00 | 0 |
| Override: 60k m3/yr | OK | -5,920,016 | -5,920,016 | -0.1389 | -0.1389 | 4.66e-09 | 8.15e-10 | 0 |
| Override: discount rate 10% | OK | -4,726,018 | -4,726,018 | -0.0706 | -0.0706 | 1.02e-08 | 6.40e-10 | 0 |
| Override: option hooks all non-zero | OK | -3,681,687 | -3,681,687 | -0.0252 | -0.0252 | 5.59e-09 | 0.00e+00 | 0 |
| Option O0 via selector (1) | OK | -4,383,366 | -4,383,366 | -0.0900 | -0.0900 | 1.02e-08 | 7.57e-10 | 0 |
| Option O1 via selector (2) | OK | -3,872,697 | -3,872,697 | -0.0340 | -0.0340 | 7.45e-09 | 0.00e+00 | 0 |
| Option O2 via selector (3) | OK | -3,087,305 | -3,087,305 | -0.0257 | -0.0257 | 6.52e-09 | 0.00e+00 | 0 |
| Option O3 via selector (4) | OK | -2,705,790 | -2,705,790 | -0.0567 | -0.0567 | 1.02e-08 | 0.00e+00 | 0 |
| Option O4 via selector (5) | OK | -4,142,336 | -4,142,336 | -0.0916 | -0.0916 | 1.02e-08 | 5.82e-11 | 0 |
| Option O5 via selector (6) | OK | -4,763,214 | -4,763,214 | -0.1035 | -0.1035 | 1.07e-08 | 5.24e-10 | 0 |
| Option O7 via selector (7) | OK | -3,827,811 | -3,827,811 | -0.0786 | -0.0786 | 1.02e-08 | 7.57e-10 | 0 |
| Option O8 via selector (8) | OK | -2,850,494 | -2,850,494 | -0.0197 | -0.0197 | 4.66e-09 | 1.86e-09 | 0 |
| Option O9 via selector (9) | OK | -5,472,676 | -5,472,676 | -0.1459 | -0.1459 | 5.59e-09 | 8.15e-10 | 0 |
| Option P1 via selector (10) | OK | -1,358,150 | -1,358,150 | 0.0211 | 0.0211 | 6.75e-09 | 4.66e-10 | 0 |
| Option P2 via selector (11) | OK | 414 | 414 | 0.0800 | 0.0800 | 5.82e-09 | 0.00e+00 | 0 |
| Pessimistic scenario + option P1 via selector | OK | -31,674,293 | -31,674,293 | - | - | 4.10e-08 | 0.00e+00 | 0 |

## Detail per case

### Base (selector 2) - OK

| Item | Python | Excel (LibreOffice) | Match |
|---|---|---|---|
| npv | -4,481,665.3956 | -4,481,665.3956 | yes |
| irr | -0.0706 | -0.0706 | yes |
| payback | None | None | yes |
| dpayback | None | None | yes |
| ebitda_y3 | 530,374.2601 | 530,374.2601 | yes |
| funding | 6,835,872.7648 | 6,835,872.7648 | yes |
| be_vol | 50,731.9939 | 50,731.9939 | yes |
| revenue (11 years, max abs diff) | 0.0000 |  | yes |
| ebitda (11 years, max abs diff) | 0.0000 |  | yes |
| ebit (11 years, max abs diff) | 0.0000 |  | yes |
| tax (11 years, max abs diff) | 0.0000 |  | yes |
| net_income (11 years, max abs diff) | 0.0000 |  | yes |
| fcf (11 years, max abs diff) | 0.0000 |  | yes |
| cum (11 years, max abs diff) | 0.0000 |  | yes |
| asset-light npv | -2,512,811.1532 | -2,512,811.1532 | yes |
| asset-light irr | None | None | yes |
| asset-light payback | None | None | yes |
| asset-light ebitda_y3 | -282,200.0000 | -282,200.0000 | yes |
| asset-light funding | 3,346,049.3151 | 3,346,049.3151 | yes |
| Reconciliation rows (P&L sums, EBITDA, FCF = NI + D&A + dWC - capex + salvage), max abs | 6.40e-10 | | yes |
| UnitEconomics: avg EBITDA/m3 x volume - P&L EBITDA | 0.00e+00 | | yes |

### Pessimistic (selector 1) - OK

| Item | Python | Excel (LibreOffice) | Match |
|---|---|---|---|
| npv | -38,250,548.1817 | -38,250,548.1817 | yes |
| irr | None | None | yes |
| payback | None | None | yes |
| dpayback | None | None | yes |
| ebitda_y3 | -4,109,613.6761 | -4,109,613.6761 | yes |
| funding | 53,454,568.9718 | 53,454,568.9718 | yes |
| be_vol | None | None | yes |
| revenue (11 years, max abs diff) | 0.0000 |  | yes |
| ebitda (11 years, max abs diff) | 0.0000 |  | yes |
| ebit (11 years, max abs diff) | 0.0000 |  | yes |
| tax (11 years, max abs diff) | 0.0000 |  | yes |
| net_income (11 years, max abs diff) | 0.0000 |  | yes |
| fcf (11 years, max abs diff) | 0.0000 |  | yes |
| cum (11 years, max abs diff) | 0.0000 |  | yes |
| Reconciliation rows (P&L sums, EBITDA, FCF = NI + D&A + dWC - capex + salvage), max abs | 0.00e+00 | | yes |
| UnitEconomics: avg EBITDA/m3 x volume - P&L EBITDA | 0.00e+00 | | yes |

### Optimistic (selector 3) - OK

| Item | Python | Excel (LibreOffice) | Match |
|---|---|---|---|
| npv | 29,963,056.8777 | 29,963,056.8777 | yes |
| irr | 1.1938 | 1.1938 | yes |
| payback | 1.1227 | 1.1227 | yes |
| dpayback | 1.1901 | 1.1901 | yes |
| ebitda_y3 | 6,952,848.3796 | 6,952,848.3796 | yes |
| funding | 2,842,680.0000 | 2,842,680.0000 | yes |
| be_vol | 10,070.4467 | 10,070.4467 | yes |
| revenue (11 years, max abs diff) | 0.0000 |  | yes |
| ebitda (11 years, max abs diff) | 0.0000 |  | yes |
| ebit (11 years, max abs diff) | 0.0000 |  | yes |
| tax (11 years, max abs diff) | 0.0000 |  | yes |
| net_income (11 years, max abs diff) | 0.0000 |  | yes |
| fcf (11 years, max abs diff) | 0.0000 |  | yes |
| cum (11 years, max abs diff) | 0.0000 |  | yes |
| Reconciliation rows (P&L sums, EBITDA, FCF = NI + D&A + dWC - capex + salvage), max abs | 0.00e+00 | | yes |
| UnitEconomics: avg EBITDA/m3 x volume - P&L EBITDA | 0.00e+00 | | yes |

### Override: 60k m3/yr - OK

| Item | Python | Excel (LibreOffice) | Match |
|---|---|---|---|
| npv | -5,920,016.2445 | -5,920,016.2445 | yes |
| irr | -0.1389 | -0.1389 | yes |
| payback | None | None | yes |
| dpayback | None | None | yes |
| ebitda_y3 | 255,112.6380 | 255,112.6380 | yes |
| funding | 7,073,231.3003 | 7,073,231.3003 | yes |
| be_vol | 50,731.9939 | 50,731.9939 | yes |
| revenue (11 years, max abs diff) | 0.0000 |  | yes |
| ebitda (11 years, max abs diff) | 0.0000 |  | yes |
| ebit (11 years, max abs diff) | 0.0000 |  | yes |
| tax (11 years, max abs diff) | 0.0000 |  | yes |
| net_income (11 years, max abs diff) | 0.0000 |  | yes |
| fcf (11 years, max abs diff) | 0.0000 |  | yes |
| cum (11 years, max abs diff) | 0.0000 |  | yes |
| Reconciliation rows (P&L sums, EBITDA, FCF = NI + D&A + dWC - capex + salvage), max abs | 8.15e-10 | | yes |
| UnitEconomics: avg EBITDA/m3 x volume - P&L EBITDA | 0.00e+00 | | yes |

### Override: discount rate 10% - OK

| Item | Python | Excel (LibreOffice) | Match |
|---|---|---|---|
| npv | -4,726,018.2467 | -4,726,018.2467 | yes |
| irr | -0.0706 | -0.0706 | yes |
| payback | None | None | yes |
| dpayback | None | None | yes |
| ebitda_y3 | 530,374.2601 | 530,374.2601 | yes |
| funding | 6,835,872.7648 | 6,835,872.7648 | yes |
| be_vol | 50,731.9939 | 50,731.9939 | yes |
| revenue (11 years, max abs diff) | 0.0000 |  | yes |
| ebitda (11 years, max abs diff) | 0.0000 |  | yes |
| ebit (11 years, max abs diff) | 0.0000 |  | yes |
| tax (11 years, max abs diff) | 0.0000 |  | yes |
| net_income (11 years, max abs diff) | 0.0000 |  | yes |
| fcf (11 years, max abs diff) | 0.0000 |  | yes |
| cum (11 years, max abs diff) | 0.0000 |  | yes |
| Reconciliation rows (P&L sums, EBITDA, FCF = NI + D&A + dWC - capex + salvage), max abs | 6.40e-10 | | yes |
| UnitEconomics: avg EBITDA/m3 x volume - P&L EBITDA | 0.00e+00 | | yes |

### Override: option hooks all non-zero - OK

| Item | Python | Excel (LibreOffice) | Match |
|---|---|---|---|
| npv | -3,681,687.3454 | -3,681,687.3454 | yes |
| irr | -0.0252 | -0.0252 | yes |
| payback | None | None | yes |
| dpayback | None | None | yes |
| ebitda_y3 | 889,677.2201 | 889,677.2201 | yes |
| funding | 7,354,931.0172 | 7,354,931.0172 | yes |
| be_vol | 40,845.7446 | 40,845.7446 | yes |
| revenue (11 years, max abs diff) | 0.0000 |  | yes |
| ebitda (11 years, max abs diff) | 0.0000 |  | yes |
| ebit (11 years, max abs diff) | 0.0000 |  | yes |
| tax (11 years, max abs diff) | 0.0000 |  | yes |
| net_income (11 years, max abs diff) | 0.0000 |  | yes |
| fcf (11 years, max abs diff) | 0.0000 |  | yes |
| cum (11 years, max abs diff) | 0.0000 |  | yes |
| Reconciliation rows (P&L sums, EBITDA, FCF = NI + D&A + dWC - capex + salvage), max abs | 0.00e+00 | | yes |
| UnitEconomics: avg EBITDA/m3 x volume - P&L EBITDA | 1.00e+03 | | n/a (hook revenue) |

### Option O0 via selector (1) - OK

| Item | Python | Excel (LibreOffice) | Match |
|---|---|---|---|
| npv | -4,383,366.2445 | -4,383,366.2445 | yes |
| irr | -0.0900 | -0.0900 | yes |
| payback | None | None | yes |
| dpayback | None | None | yes |
| ebitda_y3 | 506,811.9050 | 506,811.9050 | yes |
| funding | 6,855,141.7535 | 6,855,141.7535 | yes |
| be_vol | 51,397.7535 | 51,397.7535 | yes |
| revenue (11 years, max abs diff) | 0.0000 |  | yes |
| ebitda (11 years, max abs diff) | 0.0000 |  | yes |
| ebit (11 years, max abs diff) | 0.0000 |  | yes |
| tax (11 years, max abs diff) | 0.0000 |  | yes |
| net_income (11 years, max abs diff) | 0.0000 |  | yes |
| fcf (11 years, max abs diff) | 0.0000 |  | yes |
| cum (11 years, max abs diff) | 0.0000 |  | yes |
| Reconciliation rows (P&L sums, EBITDA, FCF = NI + D&A + dWC - capex + salvage), max abs | 7.57e-10 | | yes |
| UnitEconomics: avg EBITDA/m3 x volume - P&L EBITDA | -1.37e-09 | | yes |

### Option O1 via selector (2) - OK

| Item | Python | Excel (LibreOffice) | Match |
|---|---|---|---|
| npv | -3,872,697.2136 | -3,872,697.2136 | yes |
| irr | -0.0340 | -0.0340 | yes |
| payback | None | None | yes |
| dpayback | None | None | yes |
| ebitda_y3 | 1,028,218.1999 | 1,028,218.1999 | yes |
| funding | 8,581,964.1586 | 8,581,964.1586 | yes |
| be_vol | 46,887.2882 | 46,887.2882 | yes |
| revenue (11 years, max abs diff) | 0.0000 |  | yes |
| ebitda (11 years, max abs diff) | 0.0000 |  | yes |
| ebit (11 years, max abs diff) | 0.0000 |  | yes |
| tax (11 years, max abs diff) | 0.0000 |  | yes |
| net_income (11 years, max abs diff) | 0.0000 |  | yes |
| fcf (11 years, max abs diff) | 0.0000 |  | yes |
| cum (11 years, max abs diff) | 0.0000 |  | yes |
| Reconciliation rows (P&L sums, EBITDA, FCF = NI + D&A + dWC - capex + salvage), max abs | 0.00e+00 | | yes |
| UnitEconomics: avg EBITDA/m3 x volume - P&L EBITDA | 0.00e+00 | | yes |

### Option O2 via selector (3) - OK

| Item | Python | Excel (LibreOffice) | Match |
|---|---|---|---|
| npv | -3,087,304.6044 | -3,087,304.6044 | yes |
| irr | -0.0257 | -0.0257 | yes |
| payback | None | None | yes |
| dpayback | None | None | yes |
| ebitda_y3 | 950,321.7699 | 950,321.7699 | yes |
| funding | 7,004,140.4661 | 7,004,140.4661 | yes |
| be_vol | 42,737.7646 | 42,737.7646 | yes |
| revenue (11 years, max abs diff) | 0.0000 |  | yes |
| ebitda (11 years, max abs diff) | 0.0000 |  | yes |
| ebit (11 years, max abs diff) | 0.0000 |  | yes |
| tax (11 years, max abs diff) | 0.0000 |  | yes |
| net_income (11 years, max abs diff) | 0.0000 |  | yes |
| fcf (11 years, max abs diff) | 0.0000 |  | yes |
| cum (11 years, max abs diff) | 0.0000 |  | yes |
| Reconciliation rows (P&L sums, EBITDA, FCF = NI + D&A + dWC - capex + salvage), max abs | 0.00e+00 | | yes |
| UnitEconomics: avg EBITDA/m3 x volume - P&L EBITDA | 0.00e+00 | | yes |

### Option O3 via selector (4) - OK

| Item | Python | Excel (LibreOffice) | Match |
|---|---|---|---|
| npv | -2,705,789.5615 | -2,705,789.5615 | yes |
| irr | -0.0567 | -0.0567 | yes |
| payback | None | None | yes |
| dpayback | None | None | yes |
| ebitda_y3 | 532,874.2601 | 532,874.2601 | yes |
| funding | 4,661,681.4444 | 4,661,681.4444 | yes |
| be_vol | 50,641.1713 | 50,641.1713 | yes |
| revenue (11 years, max abs diff) | 0.0000 |  | yes |
| ebitda (11 years, max abs diff) | 0.0000 |  | yes |
| ebit (11 years, max abs diff) | 0.0000 |  | yes |
| tax (11 years, max abs diff) | 0.0000 |  | yes |
| net_income (11 years, max abs diff) | 0.0000 |  | yes |
| fcf (11 years, max abs diff) | 0.0000 |  | yes |
| cum (11 years, max abs diff) | 0.0000 |  | yes |
| Reconciliation rows (P&L sums, EBITDA, FCF = NI + D&A + dWC - capex + salvage), max abs | 0.00e+00 | | yes |
| UnitEconomics: avg EBITDA/m3 x volume - P&L EBITDA | 0.00e+00 | | yes |

### Option O4 via selector (5) - OK

| Item | Python | Excel (LibreOffice) | Match |
|---|---|---|---|
| npv | -4,142,336.4496 | -4,142,336.4496 | yes |
| irr | -0.0916 | -0.0916 | yes |
| payback | None | None | yes |
| dpayback | None | None | yes |
| ebitda_y3 | 436,660.4250 | 436,660.4250 | yes |
| funding | 6,439,041.5285 | 6,439,041.5285 | yes |
| be_vol | 53,360.5613 | 53,360.5613 | yes |
| revenue (11 years, max abs diff) | 0.0000 |  | yes |
| ebitda (11 years, max abs diff) | 0.0000 |  | yes |
| ebit (11 years, max abs diff) | 0.0000 |  | yes |
| tax (11 years, max abs diff) | 0.0000 |  | yes |
| net_income (11 years, max abs diff) | 0.0000 |  | yes |
| fcf (11 years, max abs diff) | 0.0000 |  | yes |
| cum (11 years, max abs diff) | 0.0000 |  | yes |
| Reconciliation rows (P&L sums, EBITDA, FCF = NI + D&A + dWC - capex + salvage), max abs | 5.82e-11 | | yes |
| UnitEconomics: avg EBITDA/m3 x volume - P&L EBITDA | 1.63e-09 | | yes |

### Option O5 via selector (6) - OK

| Item | Python | Excel (LibreOffice) | Match |
|---|---|---|---|
| npv | -4,763,213.9616 | -4,763,213.9616 | yes |
| irr | -0.1035 | -0.1035 | yes |
| payback | None | None | yes |
| dpayback | None | None | yes |
| ebitda_y3 | 466,496.9050 | 466,496.9050 | yes |
| funding | 7,093,571.9734 | 7,093,571.9734 | yes |
| be_vol | 52,874.6643 | 52,874.6643 | yes |
| revenue (11 years, max abs diff) | 0.0000 |  | yes |
| ebitda (11 years, max abs diff) | 0.0000 |  | yes |
| ebit (11 years, max abs diff) | 0.0000 |  | yes |
| tax (11 years, max abs diff) | 0.0000 |  | yes |
| net_income (11 years, max abs diff) | 0.0000 |  | yes |
| fcf (11 years, max abs diff) | 0.0000 |  | yes |
| cum (11 years, max abs diff) | 0.0000 |  | yes |
| Reconciliation rows (P&L sums, EBITDA, FCF = NI + D&A + dWC - capex + salvage), max abs | 5.24e-10 | | yes |
| UnitEconomics: avg EBITDA/m3 x volume - P&L EBITDA | 0.00e+00 | | yes |

### Option O7 via selector (7) - OK

| Item | Python | Excel (LibreOffice) | Match |
|---|---|---|---|
| npv | -3,827,810.6889 | -3,827,810.6889 | yes |
| irr | -0.0786 | -0.0786 | yes |
| payback | None | None | yes |
| dpayback | None | None | yes |
| ebitda_y3 | 506,811.9050 | 506,811.9050 | yes |
| funding | 6,255,141.7535 | 6,255,141.7535 | yes |
| be_vol | 51,397.7535 | 51,397.7535 | yes |
| revenue (11 years, max abs diff) | 0.0000 |  | yes |
| ebitda (11 years, max abs diff) | 0.0000 |  | yes |
| ebit (11 years, max abs diff) | 0.0000 |  | yes |
| tax (11 years, max abs diff) | 0.0000 |  | yes |
| net_income (11 years, max abs diff) | 0.0000 |  | yes |
| fcf (11 years, max abs diff) | 0.0000 |  | yes |
| cum (11 years, max abs diff) | 0.0000 |  | yes |
| Reconciliation rows (P&L sums, EBITDA, FCF = NI + D&A + dWC - capex + salvage), max abs | 7.57e-10 | | yes |
| UnitEconomics: avg EBITDA/m3 x volume - P&L EBITDA | -1.37e-09 | | yes |

### Option O8 via selector (8) - OK

| Item | Python | Excel (LibreOffice) | Match |
|---|---|---|---|
| npv | -2,850,494.0406 | -2,850,494.0406 | yes |
| irr | -0.0197 | -0.0197 | yes |
| payback | None | None | yes |
| dpayback | None | None | yes |
| ebitda_y3 | 1,031,330.6715 | 1,031,330.6715 | yes |
| funding | 6,683,326.7675 | 6,683,326.7675 | yes |
| be_vol | 59,940.0178 | 59,940.0178 | yes |
| revenue (11 years, max abs diff) | 0.0000 |  | yes |
| ebitda (11 years, max abs diff) | 0.0000 |  | yes |
| ebit (11 years, max abs diff) | 0.0000 |  | yes |
| tax (11 years, max abs diff) | 0.0000 |  | yes |
| net_income (11 years, max abs diff) | 0.0000 |  | yes |
| fcf (11 years, max abs diff) | 0.0000 |  | yes |
| cum (11 years, max abs diff) | 0.0000 |  | yes |
| Reconciliation rows (P&L sums, EBITDA, FCF = NI + D&A + dWC - capex + salvage), max abs | 1.86e-09 | | yes |
| UnitEconomics: avg EBITDA/m3 x volume - P&L EBITDA | 0.00e+00 | | yes |

### Option O9 via selector (9) - OK

| Item | Python | Excel (LibreOffice) | Match |
|---|---|---|---|
| npv | -5,472,675.5148 | -5,472,675.5148 | yes |
| irr | -0.1459 | -0.1459 | yes |
| payback | None | None | yes |
| dpayback | None | None | yes |
| ebitda_y3 | 302,871.9050 | 302,871.9050 | yes |
| funding | 7,168,062.7913 | 7,168,062.7913 | yes |
| be_vol | 58,077.1584 | 58,077.1584 | yes |
| revenue (11 years, max abs diff) | 0.0000 |  | yes |
| ebitda (11 years, max abs diff) | 0.0000 |  | yes |
| ebit (11 years, max abs diff) | 0.0000 |  | yes |
| tax (11 years, max abs diff) | 0.0000 |  | yes |
| net_income (11 years, max abs diff) | 0.0000 |  | yes |
| fcf (11 years, max abs diff) | 0.0000 |  | yes |
| cum (11 years, max abs diff) | 0.0000 |  | yes |
| Reconciliation rows (P&L sums, EBITDA, FCF = NI + D&A + dWC - capex + salvage), max abs | 8.15e-10 | | yes |
| UnitEconomics: avg EBITDA/m3 x volume - P&L EBITDA | -1.21e-09 | | yes |

### Option P1 via selector (10) - OK

| Item | Python | Excel (LibreOffice) | Match |
|---|---|---|---|
| npv | -1,358,150.0163 | -1,358,150.0163 | yes |
| irr | 0.0211 | 0.0211 | yes |
| payback | 9.8021 | 9.8021 | yes |
| dpayback | None | None | yes |
| ebitda_y3 | 906,587.9214 | 906,587.9214 | yes |
| funding | 4,719,594.9740 | 4,719,594.9740 | yes |
| be_vol | 43,633.5293 | 43,633.5293 | yes |
| revenue (11 years, max abs diff) | 0.0000 |  | yes |
| ebitda (11 years, max abs diff) | 0.0000 |  | yes |
| ebit (11 years, max abs diff) | 0.0000 |  | yes |
| tax (11 years, max abs diff) | 0.0000 |  | yes |
| net_income (11 years, max abs diff) | 0.0000 |  | yes |
| fcf (11 years, max abs diff) | 0.0000 |  | yes |
| cum (11 years, max abs diff) | 0.0000 |  | yes |
| Reconciliation rows (P&L sums, EBITDA, FCF = NI + D&A + dWC - capex + salvage), max abs | 4.66e-10 | | yes |
| UnitEconomics: avg EBITDA/m3 x volume - P&L EBITDA | 0.00e+00 | | yes |

### Option P2 via selector (11) - OK

| Item | Python | Excel (LibreOffice) | Match |
|---|---|---|---|
| npv | 414.2765 | 414.2765 | yes |
| irr | 0.0800 | 0.0800 | yes |
| payback | 7.2803 | 7.2803 | yes |
| dpayback | None | None | yes |
| ebitda_y3 | 1,276,012.6270 | 1,276,012.6270 | yes |
| funding | 4,579,629.1374 | 4,579,629.1374 | yes |
| be_vol | 48,119.4145 | 48,119.4145 | yes |
| revenue (11 years, max abs diff) | 0.0000 |  | yes |
| ebitda (11 years, max abs diff) | 0.0000 |  | yes |
| ebit (11 years, max abs diff) | 0.0000 |  | yes |
| tax (11 years, max abs diff) | 0.0000 |  | yes |
| net_income (11 years, max abs diff) | 0.0000 |  | yes |
| fcf (11 years, max abs diff) | 0.0000 |  | yes |
| cum (11 years, max abs diff) | 0.0000 |  | yes |
| Reconciliation rows (P&L sums, EBITDA, FCF = NI + D&A + dWC - capex + salvage), max abs | 0.00e+00 | | yes |
| UnitEconomics: avg EBITDA/m3 x volume - P&L EBITDA | 0.00e+00 | | yes |

### Pessimistic scenario + option P1 via selector - OK

| Item | Python | Excel (LibreOffice) | Match |
|---|---|---|---|
| npv | -31,674,293.4802 | -31,674,293.4802 | yes |
| irr | None | None | yes |
| payback | None | None | yes |
| dpayback | None | None | yes |
| ebitda_y3 | -3,494,483.9791 | -3,494,483.9791 | yes |
| funding | 44,995,616.8082 | 44,995,616.8082 | yes |
| be_vol | None | None | yes |
| revenue (11 years, max abs diff) | 0.0000 |  | yes |
| ebitda (11 years, max abs diff) | 0.0000 |  | yes |
| ebit (11 years, max abs diff) | 0.0000 |  | yes |
| tax (11 years, max abs diff) | 0.0000 |  | yes |
| net_income (11 years, max abs diff) | 0.0000 |  | yes |
| fcf (11 years, max abs diff) | 0.0000 |  | yes |
| cum (11 years, max abs diff) | 0.0000 |  | yes |
| Reconciliation rows (P&L sums, EBITDA, FCF = NI + D&A + dWC - capex + salvage), max abs | 0.00e+00 | | yes |
| UnitEconomics: avg EBITDA/m3 x volume - P&L EBITDA | 0.00e+00 | | yes |

## Python-internal reconciliation (base case)

- FCF vs (net income + D&A - change in WC - capex - sustaining capex + salvage): max abs diff 0.00e+00 EUR
- EBITDA vs (revenue - total opex): max abs diff 0.00e+00 EUR

## What is and is not checked

- Checked: every KPI on the Valuation sheet that drives the criteria, 7 yearly lines x 11 years, all check rows, for 3 scenarios, 3 override cases (incl. all original option hooks), every Agent-7 option through the live option selector (Inputs!I3), one pessimistic-scenario + package P1 case, and the asset-light sheet (O6) KPIs.
- Not checked by recalculation: the Scenarios, Sensitivity, criterion-4 and Opt_Overview results values, because they are pasted from model_core.py / options.py (same code path as the cases above).
