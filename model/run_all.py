"""Run the whole model pipeline end-to-end:
build workbook (+LibreOffice recalc) -> charts -> Excel/Python check -> results.json."""
import json
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import build_model as bm  # noqa: E402
import model_core as mc  # noqa: E402

py = sys.executable
subprocess.run([py, os.path.join(HERE, "build_model.py")], check=True)
subprocess.run([py, os.path.join(HERE, "charts.py")], check=True)
rc = subprocess.run([py, os.path.join(HERE, "check_model.py")]).returncode

tab = mc.load_inputs()
out = {"scenarios": {s: mc.run(tab, scenario=s)["kpis"] for s in mc.SCENARIOS},
       "base_years": {k: mc.run(tab)["years"][k] for k in ("year", "volume", "revenue", "ebitda", "ebit", "net_income", "fcf", "cum_fcf")},
       "sensitivity": mc.sensitivity(tab)}
v = mc.viability(tab)
out["viability"] = {k: v[k] for k in ("c1_npv_pos", "c2_payback_lt7", "c3_ebitda_y3_pos", "c4_n_pass", "c4_pass", "verdict")}
ex = bm.python_extras(tab)
out["extras"] = {"rows": ex["rows"], "rss_low": ex["rss_low"], "rss_high": ex["rss_high"]}
with open(os.path.join(HERE, "results.json"), "w") as f:
    json.dump(out, f, indent=1, default=str)
print("results.json written; check exit code", rc)
sys.exit(rc)
