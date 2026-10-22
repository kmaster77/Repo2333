"""Check that the Excel workbook (live formulas) and model_core.py give the same numbers.

    python3 model/check_model.py

For each test case it builds a copy of the workbook (scenario selector and/or the
Override column set), recalculates it with LibreOffice headless, reads the values
with openpyxl (data_only=True) and compares them with model_core.run().
Also checks the internal reconciliation rows (P&L sums, cash-flow reconciliation).
Writes model/check_report.md. Exit code 1 on any mismatch.
"""
from __future__ import annotations

import datetime as dt
import os
import shutil
import subprocess
import sys
import tempfile

from openpyxl import load_workbook

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import build_model as bm  # noqa: E402
import model_core as mc  # noqa: E402
import options as opts  # noqa: E402

REPORT = os.path.join(HERE, "check_report.md")
TOL_ABS = 0.5      # EUR
TOL_REL = 1e-7

CASES = [
    ("Base (selector 2)", 2, {}),
    ("Pessimistic (selector 1)", 1, {}),
    ("Optimistic (selector 3)", 3, {}),
    ("Override: 60k m3/yr", 2, {"output_steady_state": 60000}),
    ("Override: discount rate 10%", 2, {"discount_rate_real": 10}),
    ("Override: option hooks all non-zero", 2, {"opt_extra_capex_y0": 1_000_000, "opt_extra_revenue_per_yr": 200_000,
                                                "opt_extra_opex_per_yr": 50_000, "opt_price_delta_per_m3": 2,
                                                "opt_cost_delta_per_m3": -1}),
]
# Viability options (Agent 7): each option through the LIVE option selector (Inputs!I3), plus one
# combination of the pessimistic scenario with package P1. Tuple: (name, scenario, overrides, option no.)
CASES = [(n, s_, o, 0) for n, s_, o in CASES]
for i_, o_ in enumerate(opts.MODEL_OPTIONS):
    CASES.append((f"Option {o_[0]} via selector ({i_ + 1})", 2, {}, i_ + 1))
_P1 = [i_ + 1 for i_, o_ in enumerate(opts.MODEL_OPTIONS) if o_[0] == "P1"][0]
CASES.append(("Pessimistic scenario + option P1 via selector", 1, {}, _P1))
AL_KPIS = [("npv", "npv"), ("irr", "irr"), ("payback", "payback"), ("ebitda_y3", "ebitda_y3"), ("funding", "funding_need")]
SC = {1: "pessimistic", 2: "base", 3: "optimistic"}
YEARLY = [("revenue", "revenue"), ("ebitda", "ebitda"), ("ebit", "ebit"), ("tax", "tax"),
          ("net_income", "net_income"), ("fcf", "fcf"), ("cum", "cum_fcf")]
KPIS = [("npv", "npv"), ("irr", "irr"), ("payback", "payback"), ("dpayback", "discounted_payback"),
        ("ebitda_y3", "ebitda_y3"), ("funding", "funding_need"), ("be_vol", "be_volume_ebitda_y3")]
CHECK_ROWS = ["chk_rev", "chk_opex", "chk_ebitda", "chk_cf", "chk_cf2"]


def recalc(src, outdir):
    subprocess.run(["soffice", "--headless", "--calc", "--convert-to", "xlsx", "--outdir", outdir, src],
                   check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=180)
    return os.path.join(outdir, os.path.basename(src))


def same(a, b):
    if a is None or isinstance(a, str):
        return (b is None or isinstance(b, str)), a, b
    if b is None or isinstance(b, str):
        return False, a, b
    return abs(a - b) <= max(TOL_ABS if abs(a) > 1 else 1e-9, TOL_REL * abs(a)), a, b


def kpi_cell(wb, key):
    ref = wb.defined_names["kpi_" + key].attr_text
    sh, cell = ref.split("!")
    return wb[sh][cell.replace("$", "")]


def main():
    table = mc.load_inputs()
    tmp = tempfile.mkdtemp(prefix="cc_check_")
    out = os.path.join(tmp, "out")
    os.makedirs(out)
    results, all_ok = [], True
    for i, (name, sel, ov, osel) in enumerate(CASES):
        src = os.path.join(tmp, f"case{i}.xlsx")
        bm.build_workbook(src, scenario_selector=sel, overrides=ov, table=table, option_selector=osel,
                          with_python_sheets=(i == 0))
        reg = dict(bm.REG)
        wb_f = load_workbook(src)                      # for defined names
        wb = load_workbook(recalc(src, out), data_only=True)
        ov_all = dict(opts.MODEL_OPTIONS[osel - 1][3]) if osel else {}
        ov_all.update(ov)
        py = mc.run(table, ov_all, SC[sel])
        rows, ok = [], True
        for xk, pk in KPIS:
            s, a, b = same(py["kpis"][pk], kpi_cell_val(wb, wb_f, xk))
            rows.append((xk, a, b, s)); ok &= s
        for xk, pk in YEARLY:
            sh, r = reg[xk]
            worst = 0.0; s_all = True
            for t in mc.T:
                s, a, b = same(py["years"][pk][t], wb[sh].cell(r, 3 + t).value)
                s_all &= s
                if isinstance(a, float) and isinstance(b, (int, float)):
                    worst = max(worst, abs(a - b))
            rows.append((f"{xk} (11 years, max abs diff)", worst, None, s_all)); ok &= s_all
        if i == 0:   # asset-light sheet (O6), independent of the selector
            al_py = opts.run_asset_light(table=table)["kpis"]
            for xk, pk in AL_KPIS:
                s, a, b = same(al_py[pk], kpi_cell_val(wb, wb_f, "al_" + xk))
                rows.append(("asset-light " + xk, a, b, s)); ok &= s
        chk_max = 0.0
        for k in CHECK_ROWS:
            sh, r = reg[k]
            chk_max = max(chk_max, max(abs(wb[sh].cell(r, 3 + t).value or 0) for t in mc.T))
        ue_chk = None
        uews = wb["UnitEconomics"]
        for rr in range(1, uews.max_row + 1):
            if str(uews.cell(rr, 1).value or "").startswith("Check: plant-average EBITDA"):
                ue_chk = uews.cell(rr, 5).value
        chk_ok = chk_max < 0.01 and (ue_chk is None or abs(ue_chk) < 0.01 or ov.get("opt_extra_revenue_per_yr"))
        ok &= bool(chk_ok)
        # errors anywhere in the workbook
        errs = [(ws.title, c.coordinate) for ws in wb for row in ws.iter_rows() for c in row
                if isinstance(c.value, str) and c.value.startswith(("#N/A", "#VALUE", "#REF", "#DIV", "#NAME", "Err:"))]
        ok &= not errs
        all_ok &= ok
        results.append((name, ok, rows, chk_max, ue_chk, errs))
        print(f"{name}: {'OK' if ok else 'MISMATCH'}")

    # Python-internal reconciliation (base)
    b = mc.run(table)["years"]
    py_rec = max(abs(b["fcf"][t] - (b["net_income"][t] + b["da"][t] - b["delta_wc"][t] - b["capex"][t]
                                    - b["sustaining_capex"][t] + b["salvage"][t])) for t in mc.T)
    py_pl = max(abs(b["ebitda"][t] - (b["revenue"][t] - b["opex_total"][t])) for t in mc.T)

    L = [f"# Excel vs Python check - {dt.date.today().isoformat()}", "",
         "Method: `check_model.py` builds a copy of `financial_model.xlsx` per test case (scenario selector "
         "and/or values in the Override column), recalculates it with LibreOffice headless "
         "(`soffice --headless --convert-to xlsx`), reads the values with openpyxl (`data_only=True`) and compares "
         f"them with `model_core.run()`. Tolerance: EUR {TOL_ABS} or relative {TOL_REL}. Text results "
         "('not reached', 'n/a') must match a Python `None`.", "",
         f"**Overall result: {'ALL CASES MATCH' if all_ok else 'MISMATCH FOUND'}**", "",
         "| Case | Result | NPV Python | NPV Excel | IRR Python | IRR Excel | max abs diff yearly lines (EUR) | max abs check row (EUR) | errors |",
         "|---|---|---|---|---|---|---|---|---|"]
    for name, ok, rows, chk_max, ue_chk, errs in results:
        d = {r[0]: r for r in rows}
        yd = max(r[1] for r in rows if "max abs diff" in r[0])
        f = lambda v, p=0: ("-" if v is None else v if isinstance(v, str) else f"{v:,.{p}f}")
        L.append(f"| {name} | {'OK' if ok else 'MISMATCH'} | {f(d['npv'][1])} | {f(d['npv'][2])} | "
                 f"{f(d['irr'][1], 4)} | {f(d['irr'][2], 4)} | {yd:.2e} | {chk_max:.2e} | {len(errs)} |")
    L += ["", "## Detail per case", ""]
    for name, ok, rows, chk_max, ue_chk, errs in results:
        L += [f"### {name} - {'OK' if ok else 'MISMATCH'}", "", "| Item | Python | Excel (LibreOffice) | Match |", "|---|---|---|---|"]
        for k, a, b2, s in rows:
            fa = a if isinstance(a, str) or a is None else f"{a:,.4f}"
            fb = "" if b2 is None and "max abs" in k else (b2 if isinstance(b2, str) or b2 is None else f"{b2:,.4f}")
            L.append(f"| {k} | {fa} | {fb} | {'yes' if s else 'NO'} |")
        L.append(f"| Reconciliation rows (P&L sums, EBITDA, FCF = NI + D&A + dWC - capex + salvage), max abs | {chk_max:.2e} | | {'yes' if chk_max < 0.01 else 'NO'} |")
        if ue_chk is not None:
            L.append(f"| UnitEconomics: avg EBITDA/m3 x volume - P&L EBITDA | {ue_chk:.2e} | | {'yes' if abs(ue_chk) < 0.01 else 'n/a (hook revenue)'} |")
        if errs:
            L.append(f"| Error cells | {errs[:10]} | | NO |")
        L.append("")
    L += ["## Python-internal reconciliation (base case)", "",
          f"- FCF vs (net income + D&A - change in WC - capex - sustaining capex + salvage): max abs diff {py_rec:.2e} EUR",
          f"- EBITDA vs (revenue - total opex): max abs diff {py_pl:.2e} EUR", "",
          "## What is and is not checked", "",
          "- Checked: every KPI on the Valuation sheet that drives the criteria, 7 yearly lines x 11 years, all check rows, "
          "for 3 scenarios, 3 override cases (incl. all original option hooks), every Agent-7 option through the live option "
          "selector (Inputs!I3), one pessimistic-scenario + package P1 case, and the asset-light sheet (O6) KPIs.",
          "- Not checked by recalculation: the Scenarios, Sensitivity, criterion-4 and Opt_Overview results values, because they "
          "are pasted from model_core.py / options.py (same code path as the cases above)."]
    with open(REPORT, "w", encoding="utf-8") as fh:
        fh.write("\n".join(L) + "\n")
    shutil.rmtree(tmp, ignore_errors=True)
    print("report:", REPORT)
    return 0 if all_ok else 1


def kpi_cell_val(wb_vals, wb_formulas, key):
    ref = wb_formulas.defined_names["kpi_" + key].attr_text
    sh, cell = ref.split("!")
    v = wb_vals[sh][cell.replace("$", "")].value
    if key in ("payback", "dpayback", "al_payback") and v == "not reached":
        return None
    if key in ("irr", "al_irr") and v == "n/a":
        return None
    if key == "be_vol" and v == "none":
        return None
    return v


if __name__ == "__main__":
    sys.exit(main())
