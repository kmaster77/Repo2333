"""Build the investor / jury pitch deck: deck/pitch_deck.pptx (16:9, 15 slides, speaker notes).

Numbers: model/results.json, model/results_options.json and model/model_summary.md
(post-critique base: first sales 2028). Charts: model/charts/*.png plus two deck-only
charts drawn here into deck/charts/ (realistic NPV range, options in short form).

Run:  python3 deck/build_deck.py
"""
from __future__ import annotations

import json
import os

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
from PIL import Image  # noqa: E402
from pptx import Presentation  # noqa: E402
from pptx.dml.color import RGBColor  # noqa: E402
from pptx.enum.shapes import MSO_SHAPE  # noqa: E402
from pptx.enum.text import MSO_ANCHOR, PP_ALIGN  # noqa: E402
from pptx.util import Emu, Inches, Pt  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
MODEL_CHARTS = os.path.join(ROOT, "model", "charts")
DECK_CHARTS = os.path.join(HERE, "charts")
OUT = os.path.join(HERE, "pitch_deck.pptx")
os.makedirs(DECK_CHARTS, exist_ok=True)

# --------------------------------------------------------------------------- numbers
R = json.load(open(os.path.join(ROOT, "model", "results.json")))
RO = json.load(open(os.path.join(ROOT, "model", "results_options.json")))
BASE = R["scenarios"]["base"]
OPT = RO["options"]
P2 = OPT["P2"]["stack"]
EXTRAS = {row[0]: row[1] for row in R["extras"]["rows"]}


def m(v, d=2):
    """EUR -> '−€5.33M' with a real minus sign."""
    s = f"{abs(v) / 1e6:.{d}f}"
    return ("−" if v < 0 else "+" if v > 0 else "") + f"€{s}M"


def mu(v, d=2):
    """Unsigned amount, e.g. a funding need: '€7.09M'."""
    return m(v, d).lstrip("+−")


NPV = BASE["npv"]
IRR = BASE["irr"]
EB3 = BASE["ebitda_y3"]
FUND = BASE["funding_need"]
CAPEX = BASE["capex_initial"]
BE_VOL = EXTRAS["NPV break-even steady-state volume (same ramp %)"]
BE_PRICE = EXTRAS["NPV break-even plant-average price (2026 basis)"]
BE_PREM = EXTRAS["NPV break-even public green premium (private 0%)"]
GATE0 = P2["gate_fee_for_npv0_base_terms"]
GATE0_UP = P2["gate_fee_for_npv0_upside_other"]

# Guard rails: the deck text below was written for these values (post-critique base).
assert round(NPV / 1e6, 2) == -5.33, NPV
assert round(IRR * 100, 1) == -13.9, IRR
assert BASE["payback"] is None
assert round(EB3 / 1e6, 2) == 0.32 and BASE["ebitda_y3_year"] == 2030
assert round(FUND / 1e6, 2) == 7.09
assert R["viability"]["verdict"] == "NOT VIABLE" and R["viability"]["c4_n_pass"] == 0
assert [round(P2[k]["npv"] / 1e6, 2) for k in ("downside", "base", "upside")] == [-6.77, -4.01, -1.42]
assert round(GATE0, 1) == 29.7
assert round(BE_VOL / 1e3) == 134 and round(BE_PRICE, 1) == 154.0

# --------------------------------------------------------------------------- style
INK = RGBColor(0x1B, 0x1F, 0x24)
MUTED = RGBColor(0x5F, 0x63, 0x68)
ACCENT = RGBColor(0x2A, 0x78, 0xD6)       # same blue as the model charts
TINT = RGBColor(0xEE, 0xF4, 0xFC)         # light accent tint for cards
LINE = RGBColor(0xDA, 0xDC, 0xE0)
NEG = RGBColor(0xC9, 0x4A, 0x16)          # used only for FAIL markers (darker chart orange)
DARK = RGBColor(0x14, 0x20, 0x2B)
WHITE = RGBColor(0xFF, 0xFF, 0xFF)
FONT = "Calibri"

prs = Presentation()
prs.slide_width = Inches(13.333)
prs.slide_height = Inches(7.5)
BLANK = prs.slide_layouts[6]
SW = 13.333
LM = 0.6                     # left margin
CW = SW - 2 * LM             # content width
slide_no = 0


def _run_fmt(run, size, color, bold=False, italic=False):
    f = run.font
    f.name = FONT
    f.size = Pt(size)
    f.bold = bold
    f.italic = italic
    f.color.rgb = color


def text(slide, x, y, w, h, paras, size=16, color=INK, bold=False, align=PP_ALIGN.LEFT,
         anchor=MSO_ANCHOR.TOP, space_after=6, margin=0.0, name=None):
    """paras: str or list of str / list of runs [(text, {opts})]. Leading '• ' => bullet-like hanging indent."""
    tb = slide.shapes.add_textbox(Inches(x), Inches(y), Inches(w), Inches(h))
    if name:
        tb.name = name
    tf = tb.text_frame
    tf.word_wrap = True
    tf.vertical_anchor = anchor
    for side in ("margin_left", "margin_right", "margin_top", "margin_bottom"):
        setattr(tf, side, Inches(margin))
    if isinstance(paras, str):
        paras = [paras]
    for i, p in enumerate(paras):
        para = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        para.alignment = align
        para.space_after = Pt(space_after)
        runs = p if isinstance(p, list) else [(p, {})]
        for t, o in runs:
            r = para.add_run()
            r.text = t
            _run_fmt(r, o.get("size", size), o.get("color", color), o.get("bold", bold), o.get("italic", False))
    return tb


def box(slide, x, y, w, h, fill=TINT, line=None, rounded=True, name=None):
    shp = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE if rounded else MSO_SHAPE.RECTANGLE,
                                 Inches(x), Inches(y), Inches(w), Inches(h))
    if rounded:
        shp.adjustments[0] = 0.06
    shp.shadow.inherit = False
    if fill is None:
        shp.fill.background()
    else:
        shp.fill.solid()
        shp.fill.fore_color.rgb = fill
    if line is None:
        shp.line.fill.background()
    else:
        shp.line.color.rgb = line
        shp.line.width = Pt(1)
    if name:
        shp.name = name
    return shp


def stat(slide, x, y, w, h, big, label, big_size=32, fill=TINT, big_color=ACCENT, label_size=14):
    box(slide, x, y, w, h, fill=fill)
    text(slide, x + 0.2, y + 0.15, w - 0.4, 0.75, big, size=big_size, color=big_color, bold=True,
         anchor=MSO_ANCHOR.TOP)
    text(slide, x + 0.2, y + 0.15 + big_size / 72 * 1.25, w - 0.4, h - 0.3 - big_size / 72 * 1.25, label,
         size=label_size, color=INK, space_after=0)


def picture(slide, path, x, y, w, h, alt=""):
    """Fit the image inside the box (x, y, w, h), keep its aspect ratio, centre it."""
    iw, ih = Image.open(path).size
    scale = min(w / iw, h / ih)
    pw, ph = iw * scale, ih * scale
    px, py = x + (w - pw) / 2, y + (h - ph) / 2
    pic = slide.shapes.add_picture(path, Inches(px), Inches(py), Inches(pw), Inches(ph))
    pic._element.nvPicPr.cNvPr.set("descr", alt)
    return pic


def caption(slide, t, x=LM, w=None):
    text(slide, x, 1.72, w or CW, 0.35, t, size=14, color=MUTED, space_after=0, name="Chart caption")


def new_slide(title, notes, source, dark=False):
    global slide_no
    slide_no += 1
    s = prs.slides.add_slide(BLANK)
    bg = s.background.fill
    bg.solid()
    bg.fore_color.rgb = DARK if dark else WHITE
    if not dark:
        text(s, LM, 0.4, CW, 1.2, title, size=30, bold=True, color=INK, anchor=MSO_ANCHOR.TOP,
             space_after=0, name="Title")
        text(s, LM, 6.98, CW - 1.0, 0.35, source, size=10, color=MUTED, anchor=MSO_ANCHOR.BOTTOM,
             space_after=0, name="Source")
        text(s, SW - LM - 0.8, 6.98, 0.8, 0.35, str(slide_no), size=10, color=MUTED,
             align=PP_ALIGN.RIGHT, anchor=MSO_ANCHOR.BOTTOM, space_after=0, name="Slide number")
    n_words = len(notes.split())
    assert 80 <= n_words <= 150, (slide_no, n_words)
    s.notes_slide.notes_text_frame.text = notes
    return s


def table(slide, x, y, w, col_w, rows, row_h=0.5, size=14, header_fill=DARK, cell_styles=None):
    nr, nc = len(rows), len(rows[0])
    gf = slide.shapes.add_table(nr, nc, Inches(x), Inches(y), Inches(w), Inches(row_h * nr))
    tbl = gf.table
    for j, cw in enumerate(col_w):
        tbl.columns[j].width = Inches(cw)
    for i in range(nr):
        tbl.rows[i].height = Inches(row_h)
        for j in range(nc):
            c = tbl.cell(i, j)
            c.margin_left = c.margin_right = Inches(0.1)
            c.margin_top = c.margin_bottom = Inches(0.04)
            c.vertical_anchor = MSO_ANCHOR.MIDDLE
            c.fill.solid()
            c.fill.fore_color.rgb = header_fill if i == 0 else (WHITE if i % 2 else RGBColor(0xF6, 0xF7, 0xF9))
            tf = c.text_frame
            tf.word_wrap = True
            tf.paragraphs[0].text = ""
            r = tf.paragraphs[0].add_run()
            r.text = rows[i][j]
            st = (cell_styles or {}).get((i, j), {})
            _run_fmt(r, st.get("size", size), WHITE if i == 0 else st.get("color", INK),
                     bold=(i == 0) or st.get("bold", False))
            tf.paragraphs[0].alignment = st.get("align", PP_ALIGN.LEFT)
    return tbl


# --------------------------------------------------------------------------- model charts, slide size
def model_charts():
    """Re-draw the model's charts (model/charts.py, same code and data) at slide size into deck/charts/.

    The PNGs in model/charts/ are report-sized: placed on a slide their labels shrink to ~7 pt. Here the
    same functions run with a smaller figure (so the fixed font sizes read larger) and without the in-chart
    title and subtitle, because the slide title and a caption carry that message.
    """
    import sys
    from matplotlib.axes import Axes
    from matplotlib.figure import Figure
    sys.path.insert(0, os.path.join(ROOT, "model"))
    import charts as ch  # noqa: E402  (model/charts.py)
    import model_core as mc  # noqa: E402
    tab = mc.load_inputs()
    ch.OUT = DECK_CHARTS
    orig_sub, orig_title, orig_sup, orig_subt = plt.subplots, Axes.set_title, Figure.suptitle, ch.subtitle

    drop_all = {"on": False}

    def no_main_title(self, label, *a, **k):
        return None if (drop_all["on"] or k.get("pad") == 28) else orig_title(self, label, *a, **k)

    orig_legend = Axes.legend

    def bigger_legend(self, *a, **k):   # legends in model charts are 9.5 pt; read larger on a slide
        k["fontsize"] = k.get("fontsize", 11) + 1.5
        return orig_legend(self, *a, **k)

    Axes.set_title = no_main_title
    Axes.legend = bigger_legend
    Figure.suptitle = lambda self, *a, **k: None
    ch.subtitle = lambda ax, t: None
    paths = {}
    try:
        for func, f in ((ch.unit_cost_stack, 0.8), (ch.ebitda, 0.72), (ch.cashflow, 0.85), (ch.tornado, 0.78),
                        (ch.breakeven, 0.75)):
            drop_all["on"] = func is ch.breakeven      # its panel titles repeat the table on the slide
            def sub(*a, _f=f, **k):
                if "figsize" in k:
                    k["figsize"] = (k["figsize"][0] * _f, k["figsize"][1] * _f)
                return orig_sub(*a, **k)
            plt.subplots = sub
            paths[func.__name__] = func(tab)
    finally:
        plt.subplots, Axes.set_title, Figure.suptitle, ch.subtitle = orig_sub, orig_title, orig_sup, orig_subt
        Axes.legend = orig_legend
    return paths


MCH = model_charts()

# --------------------------------------------------------------------------- deck-only charts
CC = {"blue": "#2a78d6", "navy": "#174a87", "grey": "#9e9e9e", "ink": "#0b0b0b", "ink2": "#52514e",
      "grid": "#e4e3df", "surf": "#fcfcfb"}
plt.rcParams.update({
    "font.family": "DejaVu Sans", "font.size": 12, "axes.labelcolor": CC["ink2"], "axes.edgecolor": CC["grid"],
    "xtick.color": CC["ink2"], "ytick.color": CC["ink"], "axes.grid": True, "grid.color": CC["grid"],
    "axes.axisbelow": True, "figure.facecolor": CC["surf"], "axes.facecolor": CC["surf"],
    "savefig.facecolor": CC["surf"], "axes.spines.top": False, "axes.spines.right": False,
    "axes.spines.left": False, "legend.frameon": False,
})


def chart_range():
    """Realistic NPV range (critique L4): no all-optimistic bar; ranges that a jury can trust."""
    rows = [  # label, low, mid, high
        ("Base case\n(greenfield plant)", None, NPV / 1e6, None),
        ("Base, every conservative\nchoice undone ¹", None, -3.42, None),
        ("Indicative spread,\n22 drivers ²", R["extras"]["rss_low"] / 1e6, NPV / 1e6, R["extras"]["rss_high"] / 1e6),
        ("Best package P2,\ndownside – upside ³", P2["downside"]["npv"] / 1e6, P2["base"]["npv"] / 1e6,
         P2["upside"]["npv"] / 1e6),
        ("Best single option O3\n(buy an existing plant)", None, OPT["O3"]["kpis"]["npv"] / 1e6, None),
    ]
    fig, ax = plt.subplots(figsize=(6.0, 4.7))
    for i, (lab, lo, mid, hi) in enumerate(rows):
        yy = len(rows) - 1 - i
        if lo is not None:
            ax.plot([lo, hi], [yy, yy], color=CC["blue"], lw=10, alpha=0.35, solid_capstyle="butt")
            ax.text(lo, yy - 0.22, f"{lo:.1f}", ha="center", va="top", fontsize=11, color=CC["ink2"])
            ax.text(hi, yy - 0.22, f"{hi:+.1f}", ha="center", va="top", fontsize=11, color=CC["ink2"])
        ax.plot([mid], [yy], "o", color=CC["navy"] if i else CC["ink"], ms=10, zorder=3)
        ax.text(mid, yy + 0.2, f"{mid:.1f}", ha="center", va="bottom", fontsize=12, color=CC["ink"],
                fontweight="bold")
    ax.axvline(0, color=CC["ink"], lw=1.4)
    ax.text(0.3, len(rows) - 0.55, "NPV = 0", fontsize=11, color=CC["ink"], va="bottom")
    ax.set_yticks(range(len(rows)), [r[0] for r in rows][::-1], fontsize=11.5)
    ax.tick_params(axis="y", length=0)
    ax.set_xlim(-17.5, 4.5)
    ax.set_xticks([-15, -10, -5, 0])
    ax.set_ylim(-0.7, len(rows) - 0.3)
    ax.set_xlabel("NPV at 8% real, € million", fontsize=11.5)
    ax.grid(axis="y", visible=False)
    p = os.path.join(DECK_CHARTS, "realistic_range.png")
    fig.savefig(p, dpi=200, bbox_inches="tight")
    plt.close(fig)
    return p


def chart_options():
    """Short-label version of model/charts/options_npv.png for slide readability (same numbers)."""
    labels = {
        "O6": "Asset-light licence (O6)", "O3": "Buy an existing plant (O3)",
        "P1": "P1: buy + partner crushing + contracts", "P2": "P2: P1 scaled to 90k m³/yr",
        "O8": "Bigger plant, 100k m³/yr (O8)", "O7": "Maximum subsidies (O7)",
        "O4": "Framework contracts (O4)", "BASE": "Base case: new plant",
        "O2": "Crushing with partner (O2)", "O5": "Lower-CO₂ binder (O5)",
        "O1": "Own crushing line (O1)", "O9": "Urban site (O9)",
    }
    items = sorted(((k, OPT[k]["kpis"]["npv"] / 1e6) for k in labels), key=lambda t: t[1])
    fig, ax = plt.subplots(figsize=(8.2, 5.2))
    for yy, (k, v) in enumerate(items):
        col = CC["grey"] if k == "BASE" else CC["navy"] if k.startswith("P") else CC["blue"]
        ax.barh(yy, v, color=col, height=0.62)
        if k == "P2":
            lo, hi = P2["downside"]["npv"] / 1e6, P2["upside"]["npv"] / 1e6
            ax.plot([lo, hi], [yy, yy], color=CC["ink"], lw=1.6, zorder=3)
            for xx in (lo, hi):
                ax.plot([xx, xx], [yy - 0.2, yy + 0.2], color=CC["ink"], lw=1.6, zorder=3)
            ax.text(lo - 0.12, yy, f"{v:.1f}  (range {lo:.1f} to {hi:.1f})", ha="right", va="center",
                    fontsize=11.5, color=CC["ink"])
        else:
            ax.text(v - 0.12, yy, f"{v:.1f}", ha="right", va="center", fontsize=11.5, color=CC["ink"])
    ax.axvline(0, color=CC["ink"], lw=1.4)
    ax.set_yticks(range(len(items)), [labels[k] for k, _ in items], fontsize=12)
    ax.tick_params(axis="y", length=0)
    ax.set_xlim(-11.2, 0.4)
    ax.set_xlabel("NPV at 8% real, € million (2026–2036, salvage-only terminal value)", fontsize=11)
    ax.grid(axis="y", visible=False)
    p = os.path.join(DECK_CHARTS, "options_npv_short.png")
    fig.savefig(p, dpi=200, bbox_inches="tight")
    plt.close(fig)
    return p


RANGE_PNG = chart_range()
OPTIONS_PNG = chart_options()
MC = lambda name: os.path.join(DECK_CHARTS, name)  # noqa: E731  (slide-size re-draws of model/charts/)

# =========================================================================== slides
# 1 ---------------------------------------------------------------- title
s = new_slide(
    "", dark=True, source="",
    notes=(
        "Thank you for having us. This is a business case for a circular concrete plant in the Netherlands: "
        "a ready-mix plant that uses recycled concrete as aggregate. We set four viability tests before we built "
        "the model, and we kept them. The honest result is that a stand-alone plant does not pay. The base case "
        "has a net present value of minus 5.33 million euro at an 8% real discount rate, an IRR of minus 13.9%, "
        "no payback within ten years, and a funding need of 7.09 million euro. It passes only one of the four tests. "
        "So we are not asking you for an investment today. We will show why the plant fails, what would have to "
        "change, and the small, gated test we propose instead. Source: model/results.json, base case after the "
        "red-team review (first sales 2028)."
    ),
)
text(s, LM + 0.1, 0.9, 11.5, 0.4, "CIRCULAR CONCRETE · NETHERLANDS · BUSINESS CASE 2026–2036", size=14,
     color=RGBColor(0x8F, 0xB8, 0xEC), bold=True)
text(s, LM + 0.1, 1.45, 11.8, 1.9, "A stand-alone circular concrete plant in the Netherlands does not pay",
     size=42, bold=True, color=WHITE, space_after=0)
text(s, LM + 0.1, 3.3, 11.3, 1.0,
     "We tested one circular ready-mix plant in Zuid-Holland against four viability tests set in advance. "
     "Verdict: NOT VIABLE. Our ask is a €50–100k due-diligence phase, not an investment.",
     size=18, color=RGBColor(0xD6, 0xDE, 0xE8))
tiles = [(m(NPV), "NPV at 8% real"), (f"{IRR * 100:.1f}%".replace("-", "−"), "IRR (real)"),
         (mu(FUND), "funding need"), ("1 of 4", "viability tests passed")]
tw = (CW - 0.2 - 3 * 0.3) / 4
for i, (big, lab) in enumerate(tiles):
    x = LM + 0.1 + i * (tw + 0.3)
    box(s, x, 4.65, tw, 1.35, fill=RGBColor(0x22, 0x33, 0x44))
    text(s, x + 0.25, 4.75, tw - 0.5, 0.65, big, size=30, bold=True, color=WHITE)
    text(s, x + 0.25, 5.4, tw - 0.5, 0.45, lab, size=14, color=RGBColor(0xC4, 0xCF, 0xDB))
text(s, LM + 0.1, 6.55, 12, 0.4, "Investor and jury pitch · 22 October 2026 · real 2026 €, excl. VAT · "
     "base case: permits 2026, build 2027, first sales 2028", size=12, color=RGBColor(0x9F, 0xAE, 0xBE))

# 2 ---------------------------------------------------------------- problem
s = new_slide(
    "Concrete carries a large CO₂ load, and most Dutch concrete rubble is downcycled into road base",
    source="Sources: market.md §1–2 (MKT-01, MKT-03, MKT-05–MKT-09, MKT-11); CO₂ per m³ from price_breakdown.md §12 "
           "[ESTIMATE, Betonakkoord A1–A3 basis].",
    notes=(
        "Two problems meet here. First, CO₂. The Netherlands uses about 3.5 to 4 million tonnes of cement a year, "
        "and cement drives the CO₂ of concrete. A mix with pure Portland cement, CEM I, emits about 286 kg CO₂ per "
        "cubic metre. The Dutch standard blast-furnace cement mix, CEM III/B, is already much lower at about 129 kg. "
        "These per-m³ figures are our estimates on the Betonakkoord basis. Second, waste. Every year 11.5 to 15 "
        "million tonnes of concrete rubble are released. Almost none is landfilled, but only 8 to 15% goes back "
        "into new concrete. The rest is crushed into road base, which is a lower-value use. Road-base demand is "
        "shrinking, because few new roads are built and policy caps concrete in road-base granulate. "
        "Sources: market.md, MKT-01 to MKT-11."
    ),
)
cards = [("3.5–4 Mt", "cement used in the Netherlands each year; cement is the main CO₂ source in concrete"),
         ("11.5–15 Mt", "concrete rubble released each year (about 60% of all stony demolition waste)"),
         ("8–15%", "of that rubble goes back into new concrete today; the rest is mostly road base")]
cw3 = (CW - 2 * 0.3) / 3
for i, (big, lab) in enumerate(cards):
    stat(s, LM + i * (cw3 + 0.3), 1.85, cw3, 1.5, big, lab, big_size=34)
text(s, LM, 3.75, CW, 0.4, "Where Dutch concrete rubble goes today (2023–2025, share of tonnes)", size=16,
     bold=True)
bar_y, bar_h = 4.25, 0.7
box(s, LM, bar_y, CW * 0.885, bar_h, fill=RGBColor(0xB9, 0xBE, 0xC5), rounded=False)
box(s, LM + CW * 0.885, bar_y, CW * 0.115, bar_h, fill=ACCENT, rounded=False)
text(s, LM + 0.2, bar_y, 8, bar_h, "Road base and fill: ~85–90%", size=16, bold=True, color=INK,
     anchor=MSO_ANCHOR.MIDDLE)
text(s, LM + CW * 0.885 - 3.0, bar_y + bar_h + 0.08, 4.4, 0.4, "Back into new concrete: ~8–15%",
     size=14, bold=True, color=ACCENT, align=PP_ALIGN.RIGHT)
text(s, LM, 5.6, CW, 0.9,
     [[("CO₂ per m³ depends on the cement: ", {"bold": True}),
       ("a CEM I mix emits ~286 kg CO₂/m³; the Dutch standard CEM III/B mix ~129 kg. Landfill is near zero, "
        "so the issue is downcycling, not dumping.", {})]], size=16)

# 3 ---------------------------------------------------------------- policy
s = new_slide(
    "Policy will push rubble out of road base and into new concrete from 2027 onwards",
    source="Sources: policy.md §1, §3, §5, §10 (POL-01, POL-17, POL-18, POL-39, POL-42); market.md §2 (MKT-05, MKT-11). "
           "GWW decree start date is assumption A-POL-13.",
    notes=(
        "Policy is the tailwind. The Betonakkoord, the Dutch concrete agreement, caps concrete in mixed road-base "
        "granulate at 30% in 2025, 15% in 2027 and 5% in 2030. Its target for rubble going back into concrete rises "
        "from 20% in 2026 to more than 60% in 2030. A draft decree will make maximum MKI values, a shadow-cost "
        "measure of environmental impact, compulsory for concrete in every public civil-works tender. We assume a "
        "start on 1 January 2028; the levels are not set yet. EU ETS free allocation for cement ends in 2034 under "
        "current law, but a July 2026 proposal would slow this to 2038. The catch: these rules push supply of "
        "recycled aggregate up. They do not raise the price we can charge. Sources: policy.md, POL-01, POL-17, "
        "POL-39, POL-42; MKT-11."
    ),
)
events = [("2025", "Road-base cap: max 30% concrete in mixed granulate"),
          ("2027", "Cap falls to 15%; target 30% of rubble back into concrete"),
          ("2028", "GWW decree: max MKI for concrete in every public civil-works tender (base date)"),
          ("2030", "Cap 5%; target >60% of rubble back into concrete"),
          ("2034", "EU ETS free allocation for cement ends (may slip to 2038)")]
ly = 2.55
line = s.shapes.add_connector(1, Inches(LM + 0.3), Inches(ly), Inches(SW - LM - 0.3), Inches(ly))
line.line.color.rgb = LINE
line.line.width = Pt(3)
ew = CW / len(events)
for i, (yr, lab) in enumerate(events):
    cx = LM + ew * i + ew / 2
    dot = s.shapes.add_shape(MSO_SHAPE.OVAL, Inches(cx - 0.14), Inches(ly - 0.14), Inches(0.28), Inches(0.28))
    dot.fill.solid()
    dot.fill.fore_color.rgb = ACCENT
    dot.line.fill.background()
    dot.shadow.inherit = False
    text(s, cx - ew / 2 + 0.1, 1.8, ew - 0.2, 0.5, yr, size=22, bold=True, color=ACCENT, align=PP_ALIGN.CENTER)
    text(s, cx - ew / 2 + 0.12, 2.85, ew - 0.24, 1.3, lab, size=14, color=INK, align=PP_ALIGN.CENTER)
box(s, LM, 4.45, CW, 1.95, fill=TINT)
text(s, LM + 0.3, 4.6, CW - 0.6, 0.45, "But policy pushes supply, not our selling price", size=18, bold=True)
text(s, LM + 0.3, 5.1, CW / 2 - 0.5, 1.6,
     ["• MPG tightening for new homes was cancelled (June 2025).",
      "• The new waste plan (CMP) still counts road base as recycling."], size=15, space_after=6)
text(s, LM + CW / 2 + 0.1, 5.1, CW / 2 - 0.4, 1.6,
     ["• No levy on primary sand and gravel is proposed.",
      "• MKI rewards depend on the binder, and competitors use the same CEM III/B."], size=15, space_after=6)

# 4 ---------------------------------------------------------------- product
s = new_slide(
    "Our product is standard ready-mix in which half of the coarse gravel is recycled concrete",
    source="Sources: technology.md §1.1, §8; price_breakdown.md §2–3, §12; model/inputs.csv (A-CST-09, A-CST-11, "
           "A-TEC-28, A-FIX-02); model_summary.md §1.",
    notes=(
        "Here is how it works. A certified recycler crushes clean demolition concrete. We buy the coarse recycled "
        "aggregate at about 24.5 euro per tonne delivered, which is cheaper than barge gravel at 32 euro. Our plant "
        "mixes it with CEM III/B cement. The plant runs 120 cubic metres an hour on a 1.5-hectare waterside site in "
        "the Rotterdam–Drechtsteden area, and costs 5.5 million euro. Subcontracted truck mixers deliver about 20 "
        "kilometres. At full output we sell 70,000 cubic metres a year, 60% of it circular mixes. Be clear on one "
        "point: recycled aggregate gives circularity, not lower CO₂. Our circular mix emits about 132 kg CO₂ per "
        "cubic metre, against 129 kg for the standard mix, because it needs a little more cement. Sources: "
        "technology.md, price_breakdown.md, A-CST-09."
    ),
)
steps = [("1", "Demolition rubble", "Clean concrete from demolition sites"),
         ("2", "Certified recycler", "Crushes and certifies coarse aggregate (BRL 2506)"),
         ("3", "Recycled aggregate", "We buy it at €24.5/t delivered; gravel costs €32/t"),
         ("4", "Our mixing plant", "120 m³/h, waterside, Zuid-Holland, CEM III/B"),
         ("5", "Delivery", "Subcontracted truck mixers, ~20 km to contractors")]
sw5 = (CW - 4 * 0.25) / 5
for i, (n, head, sub) in enumerate(steps):
    x = LM + i * (sw5 + 0.25)
    box(s, x, 1.85, sw5, 2.05, fill=TINT)
    circ = s.shapes.add_shape(MSO_SHAPE.OVAL, Inches(x + 0.2), Inches(2.0), Inches(0.45), Inches(0.45))
    circ.fill.solid()
    circ.fill.fore_color.rgb = ACCENT
    circ.line.fill.background()
    circ.shadow.inherit = False
    ctf = circ.text_frame
    ctf.margin_left = ctf.margin_right = ctf.margin_top = ctf.margin_bottom = 0
    ctf.paragraphs[0].alignment = PP_ALIGN.CENTER
    _r = ctf.paragraphs[0].add_run()
    _r.text = n
    _run_fmt(_r, 14, WHITE, bold=True)
    text(s, x + 0.2, 2.55, sw5 - 0.35, 0.4, head, size=15, bold=True)
    text(s, x + 0.2, 2.9, sw5 - 0.35, 0.95, sub, size=14, color=MUTED, space_after=0)
    if i < 4:
        arr = s.shapes.add_shape(MSO_SHAPE.RIGHT_ARROW, Inches(x + sw5 + 0.03), Inches(2.6), Inches(0.19),
                                 Inches(0.25))
        arr.fill.solid()
        arr.fill.fore_color.rgb = ACCENT
        arr.line.fill.background()
        arr.shadow.inherit = False
half = (CW - 0.4) / 2
text(s, LM, 4.2, half, 0.45, "What it is", size=18, bold=True, color=ACCENT)
text(s, LM, 4.7, half, 2.1,
     ["• 70,000 m³ a year at full output (from 2030); 60% circular mixes, 40% standard.",
      "• Circular mix: 50% of the coarse aggregate is recycled (560 kg per m³).",
      "• Capex €5.5M; 10 staff; trucks subcontracted.",
      "• Price: €135/m³ plant average, the same as a standard mix."], size=15, space_after=7)
text(s, LM + half + 0.4, 4.2, half, 0.45, "What it is not", size=18, bold=True, color=ACCENT)
text(s, LM + half + 0.4, 4.7, half, 2.1,
     ["• Not lower-CO₂ than the Dutch standard: ~132 vs ~129 kg CO₂/m³.",
      "• Not a premium product: base premium is 1.5% on public work only.",
      "• Not a recycler: in the base case we buy recycled aggregate; own crushing is an option we tested."],
     size=15, space_after=7)

# 5 ---------------------------------------------------------------- market
s = new_slide(
    "The market is worth €2.5bn a year, but one plant can realistically win only about 60–70k m³",
    source="Sources: market.md §1, §8 [ESTIMATE; ERMCO 2023 basis, CMP-43, A-MKT-30–32]; model/inputs.csv "
           "(steady-state output 70k m³, A-CST-01).",
    notes=(
        "The total Dutch market for ready-mix and prefab concrete is about 2.5 billion euro a year, or 11.3 million "
        "cubic metres. The circular-addressable ready-mix part, where a buyer has a reason to choose circular and "
        "the norms allow recycled aggregate, is about 2.6 million cubic metres, or 0.35 billion euro. Ready-mix is "
        "local: trucks drive 25 to 50 kilometres at most. Inside one Zuid-Holland plant's radius the addressable "
        "volume is about 0.36 million cubic metres. A realistic share for a newcomer is about 60,000 cubic metres, "
        "or 8 million euro a year. Our model uses 70,000, which is already twice the average Dutch plant of 33,700 "
        "cubic metres. The market is mature: ready-mix volume fell from 7.5 to 6.0 million cubic metres in 2023. "
        "All TAM, SAM and SOM values are estimates."
    ),
)
funnel = [("TAM  ≈ €2.5bn / yr", "All Dutch ready-mix and prefab concrete, 11.3 Mm³"),
          ("SAM  ≈ €0.35bn / yr", "Circular-addressable ready-mix, 2.6 Mm³ (43%)"),
          ("Regional SAM  ≈ €49M / yr", "Within one plant's radius in Zuid-Holland, ~0.36 Mm³"),
          ("SOM  ≈ €8M / yr", "One plant: ~60k m³ a year")]
fw = [8.2, 7.1, 6.0, 4.9]
for i, ((head, sub), w) in enumerate(zip(funnel, fw)):
    y = 1.85 + i * 1.2
    shade = [RGBColor(0xD6, 0xE6, 0xF8), RGBColor(0xA9, 0xC9, 0xF0), RGBColor(0x6D, 0xA3, 0xE4), ACCENT][i]
    box(s, LM, y, w, 1.0, fill=shade)
    text(s, LM + 0.25, y + 0.08, w - 0.4, 0.45, head, size=18, bold=True, color=WHITE if i == 3 else INK)
    text(s, LM + 0.25, y + 0.5, w - 0.4, 0.45, sub, size=14, color=WHITE if i == 3 else INK)
text(s, LM + 8.6, 1.85, CW - 8.6, 0.45, "Reality check", size=18, bold=True, color=ACCENT)
text(s, LM + 8.6, 2.35, CW - 8.6, 4.3,
     ["• Our model plant sells 70k m³ a year: 2.1× the average Dutch plant (33.7k m³).",
      "• 178 plants share 6.0 Mm³; volume fell 20% in 2023.",
      "• Ready-mix is local (25–50 km), so the regional figure is what counts.",
      "• Recycled feedstock is plentiful; certified supply and contracts are the constraint."],
     size=15, space_after=9)

# 6 ---------------------------------------------------------------- competition
s = new_slide(
    "Incumbents already sell recycled and low-CO₂ mixes, and a specialist has just raised €100M",
    source="Sources: competitors.md §1–2, §9 (CMP-04, CMP-05, CMP-16, CMP-17, CMP-28, CMP-29, CMP-35, CMP-43). "
           "Ratings are analyst judgement.",
    notes=(
        "We are not alone. SL Materials, formerly Urban Mine and spun off from Rutte Groep, received a 100 million "
        "euro commitment from Aviva Investors and ABN AMRO in October 2026. It recovers sand, gravel and cement from "
        "rubble. everox, formerly C2CA from TU Delft, is building a plant with Dura Vermeer in 's-Gravendeel, "
        "permitted for 100,000 tonnes a year but delayed. The incumbents already sell what we would sell. "
        "Heidelberg Materials, with about 30 plants, offers EcoCrete with 30 to 100% recycled aggregate. Holcim "
        "lists its low-CO₂ ECOPact at only 5 to 9 euro more per cubic metre. Rivalry, supplier power and buyer power "
        "are all high. For a stand-alone newcomer the market is low to medium attractive. Sources: competitors.md, "
        "CMP-04, CMP-05, CMP-17, CMP-35."
    ),
)
comp = [("SL Materials (ex-Urban Mine)", "Specialist · Zaandam",
         "€100M commitment from Aviva Investors and ABN AMRO (Oct 2026). Recovers sand, gravel and cement."),
        ("everox (ex-C2CA)", "Specialist · 's-Gravendeel",
         "Plant with Dura Vermeer, permitted for 100 kt/yr; delayed, still being built in Sept 2026."),
        ("Heidelberg Materials: EcoCrete", "Incumbent · ~30 plants",
         "Ready-mix with 30, 50 or 100% recycled aggregate; claims up to −70% CO₂."),
        ("Holcim: ECOPact", "Incumbent · public price list",
         "Low-CO₂ line at only +€5–9/m³; +€4/m³ for up to 30% recycled granulate.")]
gw, gh = (CW - 0.3) / 2, 1.55
for i, (name, tag, desc) in enumerate(comp):
    x = LM + (i % 2) * (gw + 0.3)
    y = 1.85 + (i // 2) * (gh + 0.25)
    box(s, x, y, gw, gh, fill=TINT)
    text(s, x + 0.25, y + 0.12, gw - 0.5, 0.42, name, size=18, bold=True)
    text(s, x + 0.25, y + 0.52, gw - 0.5, 0.35, tag, size=14, color=ACCENT, bold=True)
    text(s, x + 0.25, y + 0.88, gw - 0.5, 0.65, desc, size=14)
text(s, LM, 5.65, CW, 0.4, "Five forces for a new stand-alone ready-mix entrant (5 = bad for us)", size=16,
     bold=True)
forces = [("Rivalry", "4/5"), ("Supplier power", "4/5"), ("Buyer power", "4/5"), ("New entrants", "3/5"),
          ("Substitutes", "3/5")]
fw5 = (CW - 4 * 0.2) / 5
for i, (f, r) in enumerate(forces):
    x = LM + i * (fw5 + 0.2)
    box(s, x, 6.1, fw5, 0.6, fill=None, line=LINE)
    text(s, x + 0.15, 6.1, fw5 - 0.3, 0.6, [[(f + "  ", {}), (r, {"bold": True, "color": ACCENT})]], size=15,
         anchor=MSO_ANCHOR.MIDDLE, space_after=0)

# 7 ---------------------------------------------------------------- unit economics
s = new_slide(
    "Our circular mix is €2.5/m³ cheaper to make, but every mix leaves only a thin margin",
    source="Source: model UnitEconomics sheet, 2030 (first full-output year), model_summary.md §2; chart "
           "model/charts/unit_cost_stack.png (full cost incl. depreciation).",
    notes=(
        "This is cost per cubic metre in 2030, the first year at full output. The circular mix is not the problem. "
        "Its cash cost is 131.6 euro per cubic metre, against 134.1 for the standard mix, so it is 2.5 euro "
        "cheaper. The reason is simple: recycled aggregate at 24.5 euro a tonne is cheaper than gravel at 32. "
        "It also earns a small green premium of about 0.8 euro per cubic metre. The problem is the margin for "
        "every mix. Cement, aggregates and delivery take about three quarters of the price. After all costs the "
        "plant average earns 4.6 euro EBITDA per cubic metre, a 3.4% margin. The chart shows full cost including "
        "depreciation, so its cost labels are slightly higher than cash cost. Source: model UnitEconomics sheet, "
        "model_summary.md section 2."
    ),
)
caption(s, "€ per m³ delivered in 2030 (first full year, 70k m³). Black line = selling price; cost includes depreciation.", w=9.2)
picture(s, MC("unit_cost_stack.png"), LM - 0.1, 2.15, 9.3, 4.65,
        alt="Stacked cost per m3 in 2030 for circular mix, standard mix and plant average, with selling price lines")
rx, rw = LM + 9.45, CW - 9.45
for i, (big, lab) in enumerate([("−€2.5/m³", "cash cost of the circular mix vs the standard mix (131.6 vs 134.1)"),
                                ("+€0.8/m³", "green premium on circular volume (1.5% on public work only)"),
                                ("€4.6/m³", "plant-average EBITDA in 2030, a 3.4% margin")]):
    stat(s, rx, 1.85 + i * 1.65, rw, 1.5, big, lab, big_size=28, label_size=14)

# 8 ---------------------------------------------------------------- why it fails
s = new_slide(
    "The plant earns €4.6 per m³ but needs about €11.7 per m³ to pay back its capital",
    source="Source: model_summary.md §2 (capital recovery over 10 years at 8% real); chart deck/charts/"
           "ebitda_by_year.png; pass-through rates are key judgement calls (A-POL-09, A-CST-13).",
    notes=(
        "This is why the plant fails. EBITDA turns positive in 2030, the third operating year, at 0.32 million "
        "euro. Then it slowly falls to about 0.19 million, because cement carbon and slag costs rise faster than "
        "the 80% we assume we can pass on in prices. That pass-through rate is a judgement call without a source; "
        "at 100% NPV improves by only 0.4 million. Per cubic metre the plant earns 4.6 euro EBITDA. To recover "
        "5.5 million euro of capex over ten years at 8%, it would need about 11.7 euro. The gap is about 7 euro "
        "per cubic metre, or 5% of the selling price. A mature, price-driven market does not give a newcomer 5% "
        "extra. Source: model_summary.md section 2, ebitda_by_year chart."
    ),
)
caption(s, "EBITDA per year, € million (margin as % of revenue). Volume 35k / 55k / 70k m³ in 2028 / 2029 / 2030+.", w=8.3)
picture(s, MC("ebitda_by_year.png"), LM - 0.1, 2.15, 8.4, 4.65,
        alt="EBITDA by year 2028-2036: negative in 2028 and 2029, then 0.32M in 2030 falling to 0.19M")
gx, gw2 = LM + 8.6, CW - 8.6
text(s, gx, 1.85, gw2, 0.45, "Per m³, 2030", size=18, bold=True, color=ACCENT)
scale = 2.9 / 11.7
for i, (lab, val, col) in enumerate([("Earned (EBITDA)", 4.6, ACCENT), ("Needed to repay capex", 11.7, DARK)]):
    y = 2.45 + i * 1.05
    text(s, gx, y, gw2, 0.35, lab, size=14, color=MUTED)
    box(s, gx, y + 0.38, val * scale, 0.45, fill=col, rounded=False)
    text(s, gx + val * scale + 0.1, y + 0.36, 1.0, 0.5, f"€{val}", size=18, bold=True, anchor=MSO_ANCHOR.MIDDLE)
box(s, gx, 4.75, gw2, 1.85, fill=TINT)
text(s, gx + 0.2, 4.85, gw2 - 0.4, 0.6, "Gap ≈ €7/m³", size=28, bold=True, color=ACCENT)
text(s, gx + 0.2, 5.45, gw2 - 0.4, 1.1, "about 5% of the selling price, every year, in a mature market",
     size=15)

# 9 ---------------------------------------------------------------- financials
s = new_slide(
    f"The base case destroys {mu(NPV)} of value and needs {mu(FUND)} of funding",
    source="Source: model/results.json (base case: permits 2026, build 2027, first sales 2028; unlevered; "
           "salvage-only terminal value); chart deck/charts/cashflow_10yr.png.",
    notes=(
        "The headline numbers. Net present value at 8% real is minus 5.33 million euro, which is minus 97% of the "
        "capex. The IRR is minus 13.9%. Cumulative cash never turns positive within the ten years, so there is no "
        "payback. EBITDA in the third operating year, 2030, is plus 0.32 million euro. The funding need, the "
        "deepest point of cumulative free cash flow, is 7.09 million euro, reached in 2029. Even with the 1.25 "
        "million euro salvage value in 2036, cumulative cash ends at minus 4.9 million. Two conservative choices "
        "were fixed in our plan: terminal value is salvage only, and working capital is not released. Undoing "
        "both, plus full price pass-through, still leaves NPV at minus 3.4 million. Source: model/results.json, "
        "model_summary.md section 2."
    ),
)
kpis = [(m(NPV), "NPV at 8% real (−97% of capex)"), (f"{IRR * 100:.1f}%".replace("-", "−"), "IRR, real"),
        ("Not reached", "payback within 10 years"), (m(EB3), "EBITDA 2030 (3rd operating year)"),
        (mu(FUND), "funding need (lowest point, 2029)"), (m(CAPEX, 1).replace("+", ""), "initial capex")]
kw = 2.25
for i, (big, lab) in enumerate(kpis):
    x = LM + (i % 2) * (kw + 0.2)
    y = 1.85 + (i // 2) * 1.6
    stat(s, x, y, kw, 1.45, big, lab, big_size=24, label_size=14)
caption(s, "Free cash flow per year (bars) and cumulative (line), € million. Build 2027, first sales 2028.", x=LM + 4.85, w=CW - 4.85)
picture(s, MC("cashflow_10yr.png"), LM + 4.75, 2.15, CW - 4.75, 4.65,
        alt="Free cash flow per year and cumulative free cash flow 2026-2036; lowest point -7.1M in 2029")

# 10 --------------------------------------------------------------- tornado
s = new_slide(
    "Selling price is the only single input that lifts NPV above zero; the green levers barely move it",
    source="Source: model/results.json → sensitivity (one input group at a time, low / high column of inputs.csv); "
           "chart deck/charts/tornado_npv.png. Price base €135/m³ has confidence L (A-MKT-16).",
    notes=(
        "We moved each input to its low and high value, one at a time. Selling price dominates. At 155 euro per "
        "cubic metre, 15% above base, NPV just reaches plus 0.25 million. No other single change gets above zero. "
        "Delivery distance, gravel price, utilisation, capex and cement price each move NPV by about 4 to 5 "
        "million, but all stay negative. The two circular levers matter little. The green premium from 0 to 3% "
        "swings NPV by only 1.2 million. The whole ETS and CBAM carbon path swings it by 0.45 million, because "
        "competitors pay the same carbon cost. And the price risk points down, not up. Our 135 euro base sits at "
        "or above the market average. At 130 euro, NPV is minus 7.1 million. Source: model sensitivity, A-MKT-16."
    ),
)
caption(s, "NPV at 8% real (€ million) when one input moves to its low (blue) or high (orange) value.", w=8.8)
picture(s, MC("tornado_npv.png"), LM - 0.1, 2.15, 8.9, 4.65,
        alt="Tornado chart of NPV sensitivity; selling price has by far the largest swing")
rx, rw = LM + 9.0, CW - 9.0
for i, (big, lab) in enumerate([("+€0.25M", "NPV at €155/m³: the only single change above zero"),
                                ("€1.2M", "total swing from the green premium (0% to 3%)"),
                                ("−€7.1M", "NPV at €130/m³; the price risk points down")]):
    stat(s, rx, 1.85 + i * 1.65, rw, 1.5, big, lab, big_size=28, label_size=14)

# 11 --------------------------------------------------------------- scorecard + realistic range
s = new_slide(
    "The base case fails three of the four viability tests that we fixed before modelling",
    source="Sources: plan.md §2.1; model/results.json; results_options.json. ¹ 100% price pass-through, book-value "
           "salvage, working capital released. ² Base ± root-sum-square. ³ Stacked inputs.",
    notes=(
        "We wrote these four tests into our plan before any result existed, and we did not change them. NPV is "
        "negative, so test 1 fails. There is no payback within ten years, so test 2 fails. EBITDA is positive in "
        "the third operating year, but only just, so test 3 passes narrowly. Test 4 asks for a positive NPV with "
        "at least two of six main drivers at their pessimistic value. We get zero of six. NPV is minus 97% of "
        "capex, far outside the borderline band of minus 10% to zero. The right-hand chart shows the realistic "
        "range. Every point estimate is below zero. Only the top end of a rough, indicative spread crosses zero. "
        "The spread treats drivers as independent, so it is not a probability. Sources: plan.md, model results."
    ),
)
rows = [["#", "Test (fixed in plan.md before results)", "Base case", "Result"],
        ["1", "NPV > 0 at 8% real", m(NPV), "FAIL"],
        ["2", "Payback < 7 years", "not reached", "FAIL"],
        ["3", "EBITDA > 0 by 3rd operating year", f"{m(EB3)} (2030)", "PASS, narrowly"],
        ["4", "NPV > 0 with ≥ 2 of 6 drivers at pessimistic value", "0 of 6", "FAIL"]]
styles = {}
for i in range(1, 5):
    res = rows[i][3]
    styles[(i, 3)] = {"bold": True, "color": NEG if res == "FAIL" else ACCENT}
    styles[(i, 0)] = {"bold": True}
table(s, LM, 1.9, 6.6, [0.4, 3.2, 1.5, 1.5], rows, row_h=0.72, size=15, cell_styles=styles)
box(s, LM, 5.75, 6.6, 0.95, fill=TINT)
text(s, LM + 0.25, 5.75, 6.1, 0.95,
     [[("Borderline band: ", {"bold": True}), ("NPV between −10% and 0% of capex. We are at −97%.", {})]],
     size=15, anchor=MSO_ANCHOR.MIDDLE, space_after=0)
text(s, LM + 6.95, 1.8, CW - 6.95, 0.4, "Realistic NPV range, € million", size=16, bold=True, color=ACCENT)
picture(s, RANGE_PNG, LM + 6.85, 2.25, CW - 6.85, 4.55,
        alt="Realistic NPV range: base -5.3, all conservative choices undone -3.4, indicative spread -15.3 to +2.1, "
            "P2 -6.8 to -1.4, O3 -3.5")

# 12 --------------------------------------------------------------- options
s = new_slide(
    "We tested ten options and two packages in the model, and every one has a negative NPV",
    source="Source: model/results_options.json; research/viability_options.md §2, §4 (same numbers as "
           "model/charts/options_npv.png, shorter labels). P2 range = stacked downside / upside inputs.",
    notes=(
        "We did not stop at no. We tested ten single options and two packages in the same model. All have a "
        "negative NPV, between minus 2.5 and minus 6.3 million euro, and none passes the robustness test. "
        "Asset-light licensing loses least only because it invests almost nothing; its EBITDA never turns "
        "positive. The best plant route is buying an existing plant instead of building one: minus 3.5 million. "
        "Our best package, P2, buys a plant, crushes rubble with a demolition partner, signs framework contracts "
        "and scales to 90,000 cubic metres. That is a stack of favourable inputs, not a likely case. It gives "
        "minus 4.0 million, with a range of minus 6.8 to minus 1.4 million. The green levers, such as a "
        "lower-CO₂ binder, lose money. Source: results_options.json, viability_options.md."
    ),
)
caption(s, "NPV at 8% real per option, € million. Grey = base case; dark blue = packages.", w=8.6)
picture(s, OPTIONS_PNG, LM - 0.1, 2.15, 8.6, 4.65,
        alt="Bar chart of NPV per option; all negative from -2.5 (asset-light) to -6.3 (urban site)")
rx, rw = LM + 8.75, CW - 8.75
for i, (big, lab) in enumerate([(m(OPT["O3"]["kpis"]["npv"], 1), "best plant route: buy an existing plant (O3)"),
                                (m(P2["base"]["npv"], 1), ["best package (P2),", "range −€6.8M to −€1.4M"]),
                                ("0 of 12", "options that pass the robustness test")]):
    stat(s, rx, 1.85 + i * 1.65, rw, 1.5, big, lab, big_size=28, label_size=14)

# 13 --------------------------------------------------------------- what would have to be true
s = new_slide(
    "Break-even needs conditions that the Dutch market does not offer today",
    source="Source: model/results.json → extras; results_options.json → P2 stack and policy tests; gate-fee evidence "
           "market.md (MKT-20); chart deck/charts/breakeven.png (other inputs at base).",
    notes=(
        "What would have to be true for NPV to reach zero? Taking one condition at a time: volume of 134,000 cubic "
        "metres a year, almost four times an average Dutch plant. Or an average price of 154 euro, 14% above our "
        "base, which is already at or above the market. Or a public green premium of 59%, against 1.5% assumed. "
        "For our best package the key is the gate fee, the fee a demolition firm pays us to take clean rubble. "
        "NPV zero needs about 30 euro a tonne on base terms, or 15 euro if everything else goes our way. Bulk "
        "evidence today is 0 to 1 euro. Policy does not close the gap: a levy on primary aggregates hits us as "
        "much as competitors, and a faster ETS phase-out hurts. Sources: model extras, results_options.json, MKT-20."
    ),
)
caption(s, "NPV at 8% real (€ million) against volume and price; other inputs at base.", w=6.5)
picture(s, MC("breakeven.png"), LM - 0.1, 2.15, 6.7, 4.65,
        alt="NPV against volume and against price; NPV = 0 at 134k m3 and at EUR 154/m3")
rows = [["NPV = 0 would need", "Today / base"],
        [f"{BE_VOL / 1e3:.0f}k m³ a year (+92%)", "70k base; average plant 33.7k"],
        [f"€{BE_PRICE:.0f}/m³ average price (+14%)", "€135, likely at or above market"],
        [f"{BE_PREM:.0f}% public green premium", "1.5% assumed (0–3%)"],
        [f"Gate fee ≈ €{GATE0:.0f}/t (best package P2)", "€0–1/t for clean rubble in bulk"],
        ["A policy rescue", "Aggregate levy: no level works; faster ETS: hurts"]]
st = {(i, 0): {"bold": True} for i in range(1, 6)}
table(s, LM + 6.75, 1.9, CW - 6.75, [2.9, CW - 6.75 - 2.9], rows, row_h=0.8, size=14, cell_styles=st)

# 14 --------------------------------------------------------------- recommendation
s = new_slide(
    "Our ask: no investment now, only a €50–100k due-diligence phase with hard stop rules",
    source="Sources: research/viability_options.md §7; value_proposition.md §6; review/response.md (M10). Gate B is "
           "expected to fail on today's evidence (MKT-20).",
    notes=(
        "Our recommendation follows the evidence. Do not build a greenfield plant. No route is investable today. "
        "The integrated acquisition route comes closest, so it is worth a small due-diligence phase of 50 to 100 "
        "thousand euro, not an investment. It tests three gates by the second quarter of 2027. Gate A: a "
        "waterside plant for 2.5 million euro or less. Gate B, the hard gate: a seven to ten year rubble contract "
        "with a gate fee and steel split that bring NPV to zero or above. Gate C: framework contracts for at least "
        "40,000 cubic metres a year. If any gate fails, we stop, and the loss is capped at the diligence budget. "
        "Even if all pass, we invest only if the re-run model passes all four tests. On today's evidence, gate B "
        "fails."
    ),
)
status = ["Status: untested", "Status: likely fails on today's evidence", "Status: untested"]
gates = [("Gate A — plant", "A waterside ready-mix plant in Zuid-Holland for ≤ €2.5M, with space and a permit "
          "route for rubble; expansion quote ≤ €1.0M."),
         ("Gate B — rubble (hard gate)", f"A 7–10-year contract with a gate fee and steel split that give NPV ≥ 0 "
          f"(≈\u00a0€{GATE0_UP:.0f}–{GATE0:.0f}/t). Evidence today: €0–1/t."),
         ("Gate C — volume", "Framework or offtake contracts for ≥ 40k m³ a year with civil-works contractors or "
          "public clients, signed before any purchase.")]
gw3 = (CW - 2 * 0.3) / 3
for i, (head, body) in enumerate(gates):
    x = LM + i * (gw3 + 0.3)
    box(s, x, 1.85, gw3, 2.6, fill=TINT)
    text(s, x + 0.25, 3.85, gw3 - 0.5, 0.45, status[i], size=14, bold=True, color=NEG if i == 1 else MUTED)
    text(s, x + 0.25, 1.98, gw3 - 0.5, 0.45, head, size=18, bold=True, color=ACCENT)
    text(s, x + 0.25, 2.5, gw3 - 0.5, 1.9, body, size=15)
box(s, LM, 4.7, CW, 2.0, fill=DARK)
text(s, LM + 0.35, 4.82, CW - 0.7, 0.5, "Stop rules", size=18, bold=True, color=WHITE)
text(s, LM + 0.35, 5.3, CW - 0.7, 1.35,
     ["• Any gate fails → stop. The loss is capped at the €50–100k diligence budget.",
      "• All gates pass → invest only if the model, re-run with the signed terms, passes all four tests.",
      "• Never: a greenfield plant. Asset-light licensing only as a capped pilot (max €0.5M)."],
     size=15, color=WHITE, space_after=5)

# 15 --------------------------------------------------------------- appendix
s = new_slide(
    "Appendix: the key assumptions behind these numbers, and how sure we are",
    source="Full lists: research/assumptions.md, research/sources.md, model/inputs.csv. Labels: VERIFIED = source read; "
           "ESTIMATE = derived; ASSUMPTION = no source. Confidence H / M / L.",
    notes=(
        "This appendix lists the inputs that matter most, with their labels. The selling price of 135 euro per "
        "cubic metre is the most important and the least certain input: confidence low, and the error probably "
        "points down. Capex and the ramp-up have no vendor quote. The two pass-through rates are judgement calls "
        "without a source. For completeness: the model also has stress bounds where every input goes wrong or "
        "right at the same time, minus 35.5 and plus 24.5 million euro. These are not likely cases, so we do not "
        "use them in the pitch. The interviews that would change our view fastest are bulk gate fees for clean "
        "rubble, prices paid for small ready-mix plants, and real project prices by strength class. Sources: "
        "assumptions.md, inputs.csv, model_summary.md."
    ),
)
rows = [["Input", "Base (low–high)", "Label, ID", "Conf."],
        ["Average selling price, delivered", "€135/m³ (115–155)", "ESTIMATE, A-MKT-16", "L"],
        ["Steady-state volume; ramp 2028/29/30", "70k m³; 50/79/100%", "ESTIMATE, A-CST-01", "L"],
        ["Capex: plant + civil + permits", "€5.5M (4.0–8.0)", "ESTIMATE, A-CST-02", "L"],
        ["Cement CEM III/B; carbon pass-through", "€110/t (95–130); 85%", "ESTIMATE; judgement A-POL-09", "M / L"],
        ["Concrete price pass-through of binder cost", "80%", "Judgement call, A-CST-13", "L"],
        ["Recycled aggregate delivered vs gravel", "€24.5/t vs €32/t", "ESTIMATE, price_breakdown §3", "M"],
        ["Delivery cost (9 m³ loads, 20 km)", "€21.1/m³", "ESTIMATE, A-TEC-28, A-FIX-02", "M"],
        ["Public green premium (private 0%)", "1.5% (0–3%)", "ASSUMPTION, A-FIX-03", "L"],
        ["Discount rate; terminal value", "8% real; salvage 25%", "Client choice, plan.md §2", "–"],
        ["Gate fee for clean rubble (bulk)", "€1/t (0–10)", "ESTIMATE, A-MKT-15, MKT-20", "L"]]
st = {(i, 3): {"align": PP_ALIGN.CENTER} for i in range(0, 11)}
table(s, LM, 1.8, CW, [4.4, 2.9, 3.85, CW - 4.4 - 2.9 - 3.85], rows, row_h=0.45, size=14, cell_styles=st)

prs.save(OUT)
print(f"wrote {OUT} ({slide_no} slides)")
