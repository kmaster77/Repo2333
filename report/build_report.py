"""Build report/business_plan.docx from report/business_plan.md.

The Markdown file is the single text source. This script converts the small
Markdown subset used there (headings, paragraphs, bullet and numbered lists,
pipe tables, block quotes, images with captions, **bold**, `code`, page-break
comments) into a formatted Word document with python-docx.

Usage:  python3 report/build_report.py
"""
from __future__ import annotations

import os
import re

from docx import Document
from docx.enum.section import WD_SECTION
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_BREAK
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Cm, Pt, RGBColor

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "business_plan.md")
OUT = os.path.join(HERE, "business_plan.docx")

NAVY = RGBColor(0x1F, 0x3A, 0x5F)
INK = RGBColor(0x22, 0x22, 0x22)
GREY = RGBColor(0x6B, 0x6B, 0x6B)
HEADER_FILL = "1F3A5F"
ZEBRA_FILL = "F2F5F9"
CALLOUT_FILL = "FDF3E7"
CALLOUT_BORDER = "C8641E"
TEXT_WIDTH_CM = 17.0  # A4 21 cm - 2 x 2 cm margins

TAG_RE = re.compile(r"\[(?:VERIFIED|ESTIMATE|ASSUMPTION)[^\]]*\]")
INLINE_RE = re.compile(r"(\*\*.+?\*\*|`[^`]+`|\[(?:VERIFIED|ESTIMATE|ASSUMPTION)[^\]]*\])")


# ---------------------------------------------------------------- helpers
def set_cell_shading(cell, fill):
    tc_pr = cell._tc.get_or_add_tcPr()
    shd = OxmlElement("w:shd")
    shd.set(qn("w:val"), "clear")
    shd.set(qn("w:color"), "auto")
    shd.set(qn("w:fill"), fill)
    tc_pr.append(shd)


TBLPR_ORDER = ["tblStyle", "tblpPr", "tblOverlap", "bidiVisual", "tblStyleRowBandSize", "tblStyleColBandSize",
               "tblW", "jc", "tblCellSpacing", "tblInd", "tblBorders", "shd", "tblLayout", "tblCellMar", "tblLook",
               "tblCaption", "tblDescription"]


def tblpr_insert(tbl_pr, el):
    """Insert a tblPr child in schema order (strict validators check the order)."""
    name = el.tag.split("}")[1]
    rank = TBLPR_ORDER.index(name)
    for old in tbl_pr.findall(qn(f"w:{name}")):
        tbl_pr.remove(old)
    for child in list(tbl_pr):
        cname = child.tag.split("}")[1]
        if cname in TBLPR_ORDER and TBLPR_ORDER.index(cname) > rank:
            child.addprevious(el)
            return
    tbl_pr.append(el)


def set_cell_margins(table, top=50, bottom=50, left=80, right=80):
    tbl_pr = table._tbl.tblPr
    mar = OxmlElement("w:tblCellMar")
    for side, val in (("top", top), ("left", left), ("bottom", bottom), ("right", right)):
        el = OxmlElement(f"w:{side}")
        el.set(qn("w:w"), str(val))
        el.set(qn("w:type"), "dxa")
        mar.append(el)
    tblpr_insert(tbl_pr, mar)


def set_table_borders(table, color="B7C3D0", size=4):
    tbl_pr = table._tbl.tblPr
    borders = OxmlElement("w:tblBorders")
    for edge in ("top", "left", "bottom", "right", "insideH", "insideV"):
        el = OxmlElement(f"w:{edge}")
        el.set(qn("w:val"), "single")
        el.set(qn("w:sz"), str(size))
        el.set(qn("w:space"), "0")
        el.set(qn("w:color"), color)
        borders.append(el)
    tblpr_insert(tbl_pr, borders)


def repeat_header(row):
    tr_pr = row._tr.get_or_add_trPr()
    el = OxmlElement("w:tblHeader")
    el.set(qn("w:val"), "true")
    tr_pr.append(el)


def no_split(row):
    tr_pr = row._tr.get_or_add_trPr()
    el = OxmlElement("w:cantSplit")
    el.set(qn("w:val"), "true")
    tr_pr.append(el)


def add_field(paragraph, instr):
    run = paragraph.add_run()
    b = OxmlElement("w:fldChar")
    b.set(qn("w:fldCharType"), "begin")
    run._r.append(b)
    run2 = paragraph.add_run()
    it = OxmlElement("w:instrText")
    it.set(qn("xml:space"), "preserve")
    it.text = instr
    run2._r.append(it)
    run3 = paragraph.add_run()
    s = OxmlElement("w:fldChar")
    s.set(qn("w:fldCharType"), "separate")
    run3._r.append(s)
    run4 = paragraph.add_run("1")
    run5 = paragraph.add_run()
    e = OxmlElement("w:fldChar")
    e.set(qn("w:fldCharType"), "end")
    run5._r.append(e)
    return [run, run2, run3, run4, run5]


def add_inline(paragraph, text, size=None, color=None, bold=False):
    """Add text with **bold**, `code` and claim-tag styling."""
    for part in INLINE_RE.split(text):
        if not part:
            continue
        if part.startswith("**") and part.endswith("**"):
            run = paragraph.add_run(part[2:-2])
            run.bold = True
        elif part.startswith("`") and part.endswith("`"):
            run = paragraph.add_run(part[1:-1])
            run.font.name = "Consolas"
            run._element.rPr.rFonts.set(qn("w:eastAsia"), "Consolas")
            run.font.size = Pt((size or 10.5) - 1.5)
            run.font.color.rgb = GREY
            continue
        elif TAG_RE.fullmatch(part):
            run = paragraph.add_run(part)
            run.font.size = Pt(max((size or 10.5) - 2, 7))
            run.font.color.rgb = GREY
            continue
        else:
            run = paragraph.add_run(part)
            if bold:
                run.bold = True
        if size:
            run.font.size = Pt(size)
        if color is not None:
            run.font.color.rgb = color


def para_spacing(p, before=0, after=4, line=1.15):
    pf = p.paragraph_format
    pf.space_before = Pt(before)
    pf.space_after = Pt(after)
    pf.line_spacing = line


# ---------------------------------------------------------------- styles
def setup_document():
    doc = Document()
    sec = doc.sections[0]
    sec.page_height, sec.page_width = Cm(29.7), Cm(21.0)
    sec.left_margin = sec.right_margin = Cm(2.0)
    sec.top_margin = Cm(2.0)
    sec.bottom_margin = Cm(1.8)

    st = doc.styles["Normal"]
    st.font.name = "Calibri"
    st.element.rPr.rFonts.set(qn("w:eastAsia"), "Calibri")
    st.font.size = Pt(10.5)
    st.font.color.rgb = INK
    para_spacing(st, 0, 5, 1.15)

    for name, size, before, after in (("Heading 1", 16, 6, 8), ("Heading 2", 12.5, 10, 4), ("Heading 3", 11, 8, 3)):
        h = doc.styles[name]
        h.font.name = "Calibri"
        h.element.rPr.rFonts.set(qn("w:eastAsia"), "Calibri")
        h.element.rPr.rFonts.set(qn("w:ascii"), "Calibri")
        h.element.rPr.rFonts.set(qn("w:hAnsi"), "Calibri")
        h.font.size = Pt(size)
        h.font.bold = True
        h.font.color.rgb = NAVY
        h.paragraph_format.space_before = Pt(before)
        h.paragraph_format.space_after = Pt(after)
        h.paragraph_format.keep_with_next = True

    lb = doc.styles["List Bullet"]
    lb.font.size = Pt(10.5)
    para_spacing(lb, 0, 3, 1.15)

    # header / footer
    header_p = sec.header.paragraphs[0]
    header_p.text = ""
    r = header_p.add_run("Circular concrete NL — business plan and viability assessment")
    r.font.size = Pt(8)
    r.font.color.rgb = GREY
    header_p.alignment = WD_ALIGN_PARAGRAPH.RIGHT

    foot = sec.footer.paragraphs[0]
    foot.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = foot.add_run("Page ")
    r.font.size = Pt(8)
    r.font.color.rgb = GREY
    for run in add_field(foot, "PAGE"):
        run.font.size = Pt(8)
        run.font.color.rgb = GREY
    return doc


# ---------------------------------------------------------------- blocks
def col_widths(rows, size):
    """Width per column: never below the longest word; extra space goes to text-heavy columns."""
    ncol = len(rows[0])
    cw = size * 0.5 / 72 * 2.54  # cm per character (Calibri average)
    pad = 0.35
    mins, nats = [], []
    for c in range(ncol):
        cells = [re.sub(r"\*\*|`", "", r[c]) for r in rows]
        longest_word = max((len(w) for cell in cells for w in cell.split()), default=3)
        longest_cell = max((len(x) for x in cells[1:]), default=3)
        mins.append(min(longest_word * cw + pad, 4.0))
        nats.append(max(longest_cell * cw + pad, mins[-1]))
    W = TEXT_WIDTH_CM
    if sum(nats) <= W:
        extra = W - sum(nats)
        tot = sum(nats)
        return [n + extra * n / tot for n in nats]
    if sum(mins) >= W:
        return [m * W / sum(mins) for m in mins]
    spare = W - sum(mins)
    need = [n - m for n, m in zip(nats, mins)]
    tot = sum(need) or 1
    return [m + spare * d / tot for m, d in zip(mins, need)]


NUMERIC_RE = re.compile(r"^[\s+−\-–~≈<>≤≥€$£(]*[\d.,]+[\d.,\s%kMm³/a-z€()−–+-]*$")


def add_table(doc, rows):
    ncol = max(len(r) for r in rows)
    rows = [r + [""] * (ncol - len(r)) for r in rows]
    size = 9 if ncol <= 4 else 8.5 if ncol <= 7 else 8 if ncol <= 9 else 7.5
    table = doc.add_table(rows=len(rows), cols=ncol)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    table.autofit = False
    set_table_borders(table)
    set_cell_margins(table)
    widths = col_widths(rows, size)
    for i, row in enumerate(rows):
        tr = table.rows[i]
        no_split(tr)
        if i == 0:
            repeat_header(tr)
        for j, text in enumerate(row):
            cell = tr.cells[j]
            cell.width = Cm(widths[j])
            p = cell.paragraphs[0]
            para_spacing(p, 0, 0, 1.05)
            clean = re.sub(r"\*\*", "", text).strip()
            if i == 0:
                set_cell_shading(cell, HEADER_FILL)
                add_inline(p, clean, size=size, color=RGBColor(0xFF, 0xFF, 0xFF), bold=True)
            else:
                if i % 2 == 0:
                    set_cell_shading(cell, ZEBRA_FILL)
                add_inline(p, text.strip(), size=size)
                if j > 0 and NUMERIC_RE.match(clean) and len(clean) <= 22:
                    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    # widths on the grid too (Word and LibreOffice read different places)
    grid = table._tbl.tblGrid
    for j, gc in enumerate(grid.findall(qn("w:gridCol"))):
        gc.set(qn("w:w"), str(int(widths[j] / 2.54 * 1440)))
    spacer = doc.add_paragraph()
    para_spacing(spacer, 0, 2, 1.0)


def add_callout(doc, lines):
    table = doc.add_table(rows=1, cols=1)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    table.autofit = False
    tbl_pr = table._tbl.tblPr
    borders = OxmlElement("w:tblBorders")
    for edge in ("top", "left", "bottom", "right"):  # schema order
        el = OxmlElement(f"w:{edge}")
        if edge == "left":
            el.set(qn("w:val"), "single")
            el.set(qn("w:sz"), "24")
            el.set(qn("w:space"), "0")
            el.set(qn("w:color"), CALLOUT_BORDER)
        else:
            el.set(qn("w:val"), "nil")
        borders.append(el)
    tblpr_insert(tbl_pr, borders)
    set_cell_margins(table, 90, 90, 160, 120)
    cell = table.rows[0].cells[0]
    cell.width = Cm(TEXT_WIDTH_CM)
    set_cell_shading(cell, CALLOUT_FILL)
    first = True
    for line in lines:
        p = cell.paragraphs[0] if first else cell.add_paragraph()
        first = False
        para_spacing(p, 0, 2, 1.15)
        add_inline(p, line, size=10.5)
    spacer = doc.add_paragraph()
    para_spacing(spacer, 0, 4, 1.0)


def add_image(doc, caption, path):
    full = os.path.normpath(os.path.join(HERE, path))
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    para_spacing(p, 6, 2, 1.0)
    p.paragraph_format.keep_with_next = True
    p.add_run().add_picture(full, width=Cm(16.5))
    cap = doc.add_paragraph()
    para_spacing(cap, 0, 10, 1.1)
    add_inline(cap, caption, size=9)
    for run in cap.runs:
        run.italic = True
        run.font.color.rgb = GREY


def add_numbered(doc, num, text):
    p = doc.add_paragraph()
    para_spacing(p, 0, 3, 1.15)
    pf = p.paragraph_format
    pf.left_indent = Cm(0.75)
    pf.first_line_indent = Cm(-0.6)
    run = p.add_run(f"{num}.\t")
    pf.tab_stops.add_tab_stop(Cm(0.75))
    add_inline(p, text)


def add_bullet(doc, text):
    p = doc.add_paragraph(style="List Bullet")
    add_inline(p, text)


def add_title_page(doc, lines):
    for _ in range(5):
        para_spacing(doc.add_paragraph(), 0, 6)
    for line in lines:
        if line.startswith("# "):
            p = doc.add_paragraph()
            para_spacing(p, 0, 18, 1.05)
            r = p.add_run(line[2:].split("—")[0].strip())
            r.bold = True
            r.font.size = Pt(28)
            r.font.color.rgb = NAVY
            if "—" in line:
                p2 = doc.add_paragraph()
                para_spacing(p2, 0, 30, 1.1)
                r2 = p2.add_run(line.split("—", 1)[1].strip())
                r2.font.size = Pt(16)
                r2.font.color.rgb = GREY
        elif line.strip():
            p = doc.add_paragraph()
            para_spacing(p, 0, 8, 1.2)
            add_inline(p, line, size=11 if line.startswith("**How") is False else 9.5)


# ---------------------------------------------------------------- parser
def build():
    with open(SRC, encoding="utf-8") as f:
        lines = f.read().splitlines()

    doc = setup_document()

    # title page = everything before the first page break
    idx = lines.index("<!-- pagebreak -->")
    add_title_page(doc, lines[:idx])
    i = idx

    buf: list[str] = []

    def flush_para():
        if buf:
            p = doc.add_paragraph()
            add_inline(p, " ".join(s.strip() for s in buf))
            buf.clear()

    while i < len(lines):
        line = lines[i]
        s = line.strip()
        if s == "<!-- pagebreak -->":
            flush_para()
            doc.add_paragraph().add_run().add_break(WD_BREAK.PAGE)
            # remove the empty paragraph spacing effect
            i += 1
            continue
        if not s:
            flush_para()
            i += 1
            continue
        if s.startswith("## "):
            flush_para()
            doc.add_heading(s[3:], level=1)
            i += 1
            continue
        if s.startswith("### "):
            flush_para()
            doc.add_heading(s[4:], level=2)
            i += 1
            continue
        if s.startswith("|"):
            flush_para()
            rows = []
            while i < len(lines) and lines[i].strip().startswith("|"):
                row = lines[i].strip()
                cells = [c.strip() for c in row.strip("|").split("|")]
                if not all(re.fullmatch(r":?-{3,}:?", c) for c in cells):
                    rows.append(cells)
                i += 1
            add_table(doc, rows)
            continue
        if s.startswith(">"):
            flush_para()
            quote = []
            while i < len(lines) and lines[i].strip().startswith(">"):
                quote.append(lines[i].strip().lstrip(">").strip())
                i += 1
            add_callout(doc, [q for q in quote if q])
            continue
        m = re.match(r"!\[(.*)\]\((.*)\)", s)
        if m:
            flush_para()
            add_image(doc, m.group(1), m.group(2))
            i += 1
            continue
        if s.startswith("- "):
            flush_para()
            add_bullet(doc, s[2:])
            i += 1
            continue
        m = re.match(r"(\d+)\.\s+(.*)", s)
        if m:
            flush_para()
            add_numbered(doc, m.group(1), m.group(2))
            i += 1
            continue
        buf.append(s)
        i += 1
    flush_para()

    zoom = doc.settings.element.find(qn("w:zoom"))
    if zoom is not None and zoom.get(qn("w:percent")) is None:
        zoom.set(qn("w:percent"), "100")

    props = doc.core_properties
    props.title = "Circular Concrete in the Netherlands — Business Plan and Viability Assessment"
    props.subject = "Circular ready-mix concrete business case, verdict NOT VIABLE"
    props.author = "Business case team"
    doc.save(OUT)
    print(f"wrote {OUT}")


if __name__ == "__main__":
    build()
