#!/usr/bin/env python3
"""
Static wiki generator for the 中观 knowledge base.
Reads markdown from skills/buddhism/references/ and produces HTML in site/.

Usage: python wiki/build.py
Dependencies: markdown, pyyaml
"""

import json
import re
import shutil
import yaml
import markdown
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REFS = ROOT / "skills" / "buddhism" / "references"
SITE = ROOT / "site"
WIKI = ROOT / "wiki"

EXCLUDE = {"log.md", "verification-report.md", "public-api.md"}
COLLECTIONS = ["中论", "中观庄严论", "中观四百论", "解义慧剑", "定解宝灯论"]


# -- Parsing -----------------------------------------------------------------

def parse_md(path):
    raw = path.read_text("utf-8")
    if raw.startswith("---\n"):
        try:
            end = raw.index("\n---\n", 4)
            return yaml.safe_load(raw[4:end]) or {}, raw[end + 5:]
        except (ValueError, yaml.YAMLError):
            pass
    return {}, raw


def pick_title(fm, body, stem):
    if fm.get("title"):
        return fm["title"]
    m = re.match(r"#\s+(.+)", body)
    return m.group(1).strip() if m else stem


def sidebar_label(stem):
    label = re.sub(r"^(品?\d+|序)-", r"\1·", stem)
    if "·" not in label and "-" in label:
        label = label.replace("-", "·", 1)
    return label


def page_sort_key(name):
    if name == "结构总览.md":
        return (0, 0)
    if name.startswith("序"):
        return (1, 0)
    m = re.match(r"(?:品)?(\d+)", name)
    if m:
        return (3, int(m.group(1)))
    return (2, 0)


# -- Page model --------------------------------------------------------------

class Page:
    def __init__(self, src, rel):
        self.src = src
        self.rel = rel
        self.out = rel.with_suffix(".html")
        fm, self.body = parse_md(src)
        self.fm = fm
        self.title = pick_title(fm, self.body, src.stem)
        self.label = sidebar_label(src.stem)
        self.collection = None
        self.is_reasoning = False

    @property
    def depth(self):
        return len(self.out.parts) - 1

    @property
    def root(self):
        return "../" * self.depth if self.depth else ""

    @property
    def is_home(self):
        return str(self.rel) == "index.md"


# -- Discovery ---------------------------------------------------------------

def discover():
    pages = {}
    for path in sorted(REFS.rglob("*.md")):
        if path.name in EXCLUDE:
            continue
        rel = path.relative_to(REFS)
        pages[str(rel)] = Page(path, rel)
    return pages


def organize(pages):
    colls = {}
    for cname in COLLECTIONS:
        overview, chapters, reasoning = None, [], []
        prefix = f"collections/{cname}/"
        for key, pg in pages.items():
            if not key.startswith(prefix):
                continue
            pg.collection = cname
            parts = Path(key).parts
            if len(parts) == 3:
                if pg.src.name == "结构总览.md":
                    overview = pg
                else:
                    chapters.append(pg)
            elif len(parts) == 4 and parts[2] == "推理方法":
                pg.is_reasoning = True
                reasoning.append(pg)
        chapters.sort(key=lambda p: page_sort_key(p.src.name))
        reasoning.sort(key=lambda p: p.src.name)
        colls[cname] = {"overview": overview, "chapters": chapters, "reasoning": reasoning}
    return colls


def topic_pages(pages):
    result = []
    for key, pg in pages.items():
        if key.startswith("topics/"):
            result.append(pg)
    result.sort(key=lambda p: str(p.rel))
    return result


def all_coll_pages(coll):
    out = []
    if coll["overview"]:
        out.append(coll["overview"])
    out.extend(coll["chapters"])
    out.extend(coll["reasoning"])
    return out


# -- HTML builders -----------------------------------------------------------

def render_md(body):
    md = markdown.Markdown(extensions=["tables", "toc", "fenced_code"])
    html = md.convert(body)
    toc = getattr(md, "toc", "")
    heading_count = toc.count("<li>")
    html = re.sub(r'(href="[^"]*?)\.md([#"])', r'\1.html\2', html)
    return html, toc, heading_count


def breadcrumbs(page, colls):
    if page.is_home:
        return ""
    r = page.root
    crumbs = [f'<a href="{r}index.html">首页</a>']
    parts = page.rel.parts
    if parts[0] == "collections" and len(parts) >= 2:
        cname = parts[1]
        ov = colls[cname]["overview"]
        crumbs.append(f'<a href="{r}{ov.out}">{cname}</a>' if ov else cname)
        if page.is_reasoning:
            crumbs.append("推理方法")
        if page.src.name != "结构总览.md":
            crumbs.append(page.label)
    elif parts[0] == "topics":
        crumbs.append(f'<a href="{r}topics/madhyamaka/index.html">中观专题</a>')
        if page.src.name != "index.md":
            crumbs.append(page.label)
    elif parts[0] == "maps":
        crumbs.append(page.label)
    return " › ".join(crumbs)


def sidebar(page, colls, topic_pgs):
    r = page.root
    current_coll = page.collection
    parts = page.rel.parts
    in_topics = parts[0] == "topics" if parts else False
    lines = []

    # Home link
    cls = ' class="active"' if page.is_home else ''
    lines.append(f'<div class="sb-home"><a href="{r}index.html"{cls}>首页</a></div>')

    # Topics section
    lines.append(f'<div class="sb-section-title">中观专题</div>')
    if in_topics:
        lines.append('<ul class="sb-pages">')
        for tp in topic_pgs:
            cls = ' class="active"' if tp is page else ""
            lines.append(f'  <li{cls}><a href="{r}{tp.out}">{tp.label}</a></li>')
        lines.append("</ul>")

    # Each collection
    for cname in COLLECTIONS:
        coll = colls[cname]
        ov = coll["overview"]
        expanded = (current_coll == cname)

        if ov:
            cls = ' class="active"' if ov is page else ""
            lines.append(f'<div class="sb-coll-title{"" if not expanded else " sb-expanded"}"><a href="{r}{ov.out}"{cls}>{cname}</a></div>')
        else:
            lines.append(f'<div class="sb-coll-title">{cname}</div>')

        if expanded:
            lines.append('<ul class="sb-pages">')
            for pg in all_coll_pages(coll):
                if pg is ov:
                    continue
                cls = ' class="active"' if pg is page else ""
                indent = "sb-indent " if pg.is_reasoning else ""
                if pg.is_reasoning and pg is coll["reasoning"][0]:
                    lines.append(f'  <li class="sb-sub-title">推理方法</li>')
                lines.append(f'  <li{cls}><a class="{indent}" href="{r}{pg.out}">{pg.label}</a></li>')
            lines.append("</ul>")

    return "\n".join(lines)


def toc_box(toc_html, count, is_home):
    if is_home or count < 4:
        return ""
    return (
        '<div class="toc-box">\n'
        '  <div class="toc-heading">目录 <span class="toc-toggle" onclick="'
        "this.parentElement.nextElementSibling.classList.toggle('hidden');"
        "this.textContent=this.textContent==='[隐藏]'?'[显示]':'[隐藏]'"
        '">[隐藏]</span></div>\n'
        f'  <div class="toc-body">{toc_html}</div>\n'
        '</div>\n'
    )


def prev_next(page, colls):
    if not page.collection:
        return ""
    seq = all_coll_pages(colls[page.collection])
    try:
        idx = seq.index(page)
    except ValueError:
        return ""
    r = page.root
    parts = []
    if idx > 0:
        p = seq[idx - 1]
        parts.append(f'<a class="pn-prev" href="{r}{p.out}">← {p.label}</a>')
    else:
        parts.append("<span></span>")
    if idx < len(seq) - 1:
        p = seq[idx + 1]
        parts.append(f'<a class="pn-next" href="{r}{p.out}">{p.label} →</a>')
    else:
        parts.append("<span></span>")
    return f'<nav class="prev-next">{"".join(parts)}</nav>'


# -- Search index ------------------------------------------------------------

def build_search_index(pages):
    index = []
    for key, pg in pages.items():
        index.append({
            "t": pg.title,
            "l": pg.label,
            "u": str(pg.out),
            "c": pg.collection or "",
        })
    return json.dumps(index, ensure_ascii=False)


# -- Assemble ----------------------------------------------------------------

def render_page(page, template, colls, topic_pgs):
    content, toc_html, hcount = render_md(page.body)
    sb = sidebar(page, colls, topic_pgs)
    bc = breadcrumbs(page, colls)
    bc_html = f'<nav class="breadcrumbs">{bc}</nav>' if bc else ""

    html = template
    for key, val in {
        "{{TITLE}}": page.title if not page.is_home else "中观知识库",
        "{{ROOT}}": page.root,
        "{{BODY_CLASS}}": "has-sidebar",
        "{{BREADCRUMBS}}": bc_html,
        "{{SIDEBAR}}": f'<aside class="sidebar">{sb}</aside>',
        "{{TOC_BOX}}": toc_box(toc_html, hcount, page.is_home),
        "{{CONTENT}}": content,
        "{{PREV_NEXT}}": prev_next(page, colls),
    }.items():
        html = html.replace(key, val)
    return html


def build():
    if SITE.exists():
        shutil.rmtree(SITE)
    SITE.mkdir()

    template = (WIKI / "template.html").read_text("utf-8")
    shutil.copy(WIKI / "style.css", SITE / "style.css")

    pages = discover()
    colls = organize(pages)
    topic_pgs = topic_pages(pages)

    for key, page in pages.items():
        html = render_page(page, template, colls, topic_pgs)
        out = SITE / page.out
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(html, "utf-8")

    # Search index
    idx = build_search_index(pages)
    (SITE / "search-index.json").write_text(idx, "utf-8")

    print(f"Built {len(pages)} pages → {SITE}/")


if __name__ == "__main__":
    build()
