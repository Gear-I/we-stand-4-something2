#!/usr/bin/env python3
"""Generates the static We Stand 4 Something website.

Every page is described below as a list of elements placed at the same
coordinates as the original Wix site (a 980px-wide canvas). Running

    python3 _build/build.py

rewrites the .html files in the repository root. You can also edit the
generated HTML directly; just remember a rebuild will overwrite it.
"""
import html
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CANVAS_LEFT = 142      # page x of the canvas' left edge in the captured layout
HEADER_H = 354
FOOTER_H = 236
SITE = "We Stand 4 Something"
WIX = "https://static.wixstatic.com/media/"

FONTS = {
    "os": "'Open Sans',sans-serif",
    "enr": "'Enriqueta',serif",
    "lb": "'Libre Baskerville',serif",
    "pop": "'Poppins',sans-serif",
    "jost": "'Jost','Futura',sans-serif",
    "lulo": "'Montserrat',sans-serif",
    "trend": "'Archivo Black',sans-serif",
    "cinzel": "'Cinzel',serif",
    "pf": "'Playfair Display',serif",
    "amatic": "'Amatic SC',cursive",
    "din": "'Barlow',sans-serif",
    "helv": "'Helvetica Neue',Helvetica,Arial,sans-serif",
    "didot": "'Playfair Display',serif",
    "avenir": "'Nunito Sans',sans-serif",
    "bree": "'Bree Serif',serif",
    "script": "'Lobster',cursive",
    "georgia": "Georgia,serif",
}
GOOGLE_FONTS = ("https://fonts.googleapis.com/css2?family=Amatic+SC&family=Archivo+Black"
                "&family=Barlow:ital,wght@0,300;0,700;1,300;1,700&family=Bree+Serif&family=Cinzel:wght@700"
                "&family=Enriqueta:wght@400;700&family=Jost:wght@400;700&family=Libre+Baskerville:wght@400;700"
                "&family=Lobster&family=Montserrat:wght@800&family=Nunito+Sans:wght@300;700"
                "&family=Open+Sans:ital,wght@0,400;0,600;0,700;1,400&family=Playfair+Display:ital,wght@0,400;1,700"
                "&family=Poppins:wght@600&display=swap")

# ---------------------------------------------------------------- icons
SVG = {
    "social": '<svg viewBox="0 0 143.901 145.9" aria-hidden="true"><path d="M130.8 0H12.3C5.4 0 0 5.7 0 12.6v91.6c0 6.9 5.4 11.7 12.3 11.7H41c6.9 0 15.1 5.5 18.2 11.7l6.7 13.6c3.1 6.2 8.2 6.3 11.2.1l6.7-13.8c3.1-6.2 11.3-11.6 18.2-11.6h28.7c6.9 0 13.2-4.8 13.2-11.7V12.6C144 5.7 137.7 0 130.8 0zM94 42.7a6.7 6.7 0 1 1 0 13.4 6.7 6.7 0 0 1 0-13.4zm-44.9 0a6.7 6.7 0 1 1 0 13.4 6.7 6.7 0 0 1 0-13.4zm60.7 30.6c-11.2 8.8-23.6 13.2-37 13.2-5.2 0-10.5-.7-15.8-2-14.1-3.7-23.6-10.9-24-11.2-1.8-1.4-2.1-3.9-.8-5.7.8-1 1.9-1.6 3.2-1.6.9 0 1.7.3 2.4.8.1.1 8.8 6.6 21.3 9.8 4.7 1.2 9.3 1.8 13.8 1.8 11.3 0 22.5-3.3 31.8-11.5 1.1-1 4-2.1 6.1.9 2.2 3-1 5.5-1 5.5z"/></svg>',
    "chat": '<svg viewBox="-0.015 21.485 200.051 156.915" aria-hidden="true"><path d="M188.6 71.1c-9.9-14.6-24.9-24.4-42.2-27.7-9.3-1.8-18.5-1.5-27.6.6-3.6-4-7.7-7.6-12.3-10.7-15.1-10.2-33.2-14-51.1-10.6C37.5 26.1 22 36.3 11.8 51.3s-14 33.2-10.6 51.1c2.5 13.4 9 25.5 18.6 35.2l.5 21.2c0 1 .5 2 1.4 2.6.6.4 1.2.6 1.9.6.4 0 .7-.1 1.1-.2l22.1-7.5c11 3.7 22.8 4.4 34.1 2.3 2.3-.4 4.5-1 6.7-1.6 9.3 9.3 21 15.5 34.1 17.9 11.2 2.1 22.9 1.3 33.7-2.4l22.9 7.8c.1 0 .2.1.4.1s.4-.1.6-.2c.3-.2.5-.5.5-.9l.5-22.1c9.6-9.5 16.1-21.4 18.6-34.7 3.2-17.2-.4-34.8-10.3-49.4zM79.7 150.2c-10.6 2-21.6 1.2-31.8-2.4-.7-.2-1.5-.2-2.2 0l-19 6.5-.4-18.1c0-.9-.4-1.7-1-2.3-9.2-8.9-15.3-20.2-17.6-32.6-3.1-16.2.3-32.6 9.6-46.2 9.3-13.6 23.2-22.8 39.4-25.9 3.9-.7 7.8-1.1 11.6-1.1 12.2 0 24.2 3.7 34.5 10.7 13.6 9.2 22.8 23.2 25.9 39.4 6.3 33.4-15.6 65.7-49 72zm117-30c-2.5 12.9-8.8 24.6-18.3 33.8-.2.2-.3.5-.3.8l-.5 21.1-21.8-7.4c-.2-.1-.5-.1-.7 0-10.6 3.7-22 4.6-32.9 2.5-12.2-2.3-23.3-8-32.1-16.5 31.8-10.7 51.6-43.5 45.2-77.3-2.2-11.6-7.3-22.3-14.7-31.1 8.4-1.8 17-2 25.5-.3 16.7 3.2 31.2 12.7 40.8 26.8 9.4 13.9 12.9 30.8 9.8 47.6z"/><path d="M54.2 88.8a6.2 6.2 0 1 1-12.4 0 6.2 6.2 0 0 1 12.4 0zM74.9 88.8a6.2 6.2 0 1 1-12.4 0 6.2 6.2 0 0 1 12.4 0zM95.6 88.8a6.2 6.2 0 1 1-12.4 0 6.2 6.2 0 0 1 12.4 0z"/></svg>',
    "megaphone": '<svg viewBox="0.1 0.1 200 200" aria-hidden="true"><path d="M133.6 54.9c-1.9-.9-4.6-.6-6.1.7L94 81.6v30.2l33.5 25.9c1.6 1.3 4.9 1.6 6.8.7 2-1 2.8-3 2.8-5V59.9c-.1-1.8-1.3-3.9-3.5-5z"/><path d="M144 87.9v17.5c6-.6 7.8-4.2 7.8-8.8 0-4.4-1.8-8.1-7.8-8.7z"/><path d="M48 87.2v18.9c0 2.8 3.5 5.9 5.2 5.9H65c1.4 0 2.5 1.5 2.9 2.8l8.9 36.2h12.8l-8.5-34.7c-.2-.9 0-2.2.5-2.9.6-.7 1.4-1.5 2.3-1.5H88V85H53.2c-3.6 0-5.2 1.4-5.2 2.2zm19 3.3c0-1.6.9-3 2.5-3s2.5 1.3 2.5 3v15.1c0 1.6-.9 3-2.5 3s-2.5-1.3-2.5-3V90.5zm-13 0c0-1.6 1.9-3 3.5-3s3.5 1.3 3.5 3v15.1c0 1.6-1.9 3-3.5 3s-3.5-1.3-3.5-3V90.5z"/><path d="M100.1.1C44.9.1.1 44.9.1 100.1s44.8 100 100 100 100-44.8 100-100S155.3.1 100.1.1zM144 111.4v22c0 4.3-2.6 8.3-6.7 10.3-1.5.7-3.1 1.1-5 1.1-2.9 0-5.8-.9-7.8-2.5l-31.4-24.6c-.3.1-.8.2-1.2.2h-4.3l8.4 33.7c.2.4.2.9.2 1.3 0 1.6-1.3 3.1-3 3.1H74.5c-1.4 0-2.5-1-2.9-2.3L62.7 118h-9.5c-5.6 0-10.2-6.2-10.2-11.9V87.2c0-5.4 4.5-8.2 10.2-8.2h36.7c.1 0 .1-.7.2-.8L124.2 51c3.3-2.6 9-3.2 12.8-1.4 4.2 2 7 6.1 7 10.3v22c8 .6 13.7 6.9 13.7 14.7 0 7.8-5.7 14.2-13.7 14.8z"/></svg>',
    "chevrons": '<svg viewBox="20 20 160 160" aria-hidden="true"><path d="M100 180c-44.28 0-80-35.72-80-80s35.72-80 80-80 80 35.72 80 80-35.72 80-80 80zm0-152.915c-40.148 0-72.915 32.768-72.915 72.915S59.852 172.915 100 172.915s72.915-32.768 72.915-72.915S140.148 27.085 100 27.085z"/><path d="M140.148 98.229l-1.476-1.476L105.018 63.1c-1.181-1.181-2.657-1.181-3.838 0l-1.476 1.476c-1.181 1.181-1.181 2.657 0 3.838L131.292 100l-31.587 31.587c-1.181 1.181-1.181 2.657 0 3.838l1.476 1.476c1.181 1.181 2.657 1.181 3.838 0l33.653-33.653 1.476-1.476a2.216 2.216 0 0 0 0-3.543z"/><path d="M111.218 98.229l-1.476-1.476L76.089 63.1c-1.181-1.181-2.657-1.181-3.838 0l-1.476 1.476c-1.181 1.181-1.181 2.657 0 3.838L102.362 100l-31.587 31.587c-1.181 1.181-1.181 2.657 0 3.838l1.476 1.476c1.181 1.181 2.657 1.181 3.838 0l33.653-33.653 1.476-1.476c.885-.886.885-2.658 0-3.543z"/></svg>',
    "network": '<svg viewBox="51.07 15.604 89.861 168.792" aria-hidden="true"><path d="M137.188 68.791h-14.977a3.742 3.742 0 0 0-3.744 3.744v14.977a3.742 3.742 0 0 0 3.744 3.744h3.744v19.789l-22.466 5.718V61.302h15.212a3.755 3.755 0 0 0 3.181-1.77 3.738 3.738 0 0 0 .175-3.635l-18.955-38.379c-1.258-2.552-5.455-2.552-6.714 0l-18.955 38.38a3.74 3.74 0 0 0 .176 3.635 3.756 3.756 0 0 0 3.181 1.77h15.211v70.439l-22.466-5.718v-16.425c8.535-1.74 14.977-9.302 14.977-18.341 0-10.326-8.398-18.721-18.721-18.721-10.322 0-18.721 8.395-18.721 18.721 0 9.039 6.443 16.601 14.977 18.341v19.336a3.746 3.746 0 0 0 2.819 3.627l26.682 6.787c.15.043.3.036.453.058v8.066c-8.293 1.924-14.509 9.332-14.509 18.202 0 10.326 8.399 18.721 18.721 18.721 10.323 0 18.721-8.395 18.721-18.721 0-9.2-6.684-16.835-15.445-18.385v-22.86c.154-.022.304-.015.454-.058l26.674-6.787a3.744 3.744 0 0 0 2.826-3.627V91.256h3.744a3.741 3.741 0 0 0 3.744-3.744V72.535a3.74 3.74 0 0 0-3.743-3.744z"/></svg>',
    "down": '<svg viewBox="20 20 160 160" aria-hidden="true"><path d="M136.156 82.349c-1.139-1.139-3.132-1.139-4.27 0L100 114.519l-31.886-32.17c-1.139-1.139-3.132-1.139-4.27 0l-2.277 2.277c-1.139 1.139-1.139 3.132 0 4.27l36.156 36.157c1.139 1.139 3.132 1.139 4.27 0l2.277-2.277 34.163-34.163c1.139-1.139 1.139-3.132 0-4.27l-2.277-1.994z"/><path d="M100 20c-44.128 0-80 35.872-80 80s35.872 80 80 80 80-35.872 80-80-35.873-80-80-80zm0 150.605c-39.003 0-70.605-31.601-70.605-70.605S60.997 29.395 100 29.395 170.605 60.997 170.605 100 139.003 170.605 100 170.605z"/></svg>',
    "square": '<svg viewBox="1.5 1.5 57 57" aria-hidden="true"><path d="M46.5 58.5h-33c-6.6 0-12-5.4-12-12v-33c0-6.6 5.4-12 12-12h33c6.6 0 12 5.4 12 12v33c0 6.6-5.4 12-12 12z"/></svg>',
    "arrow": '<svg viewBox="0 0 60 60" aria-hidden="true"><path d="M46.5 28.9L20.6 3c-.6-.6-1.6-.6-2.2 0l-4.8 4.8c-.6.6-.6 1.6 0 2.2l19.8 20-19.9 19.9c-.6.6-.6 1.6 0 2.2l4.8 4.8c.6.6 1.6.6 2.2 0l21-21 4.8-4.8c.8-.6.8-1.6.2-2.2z"/></svg>',
    "play": '<svg viewBox="0 0 60 60" aria-hidden="true"><circle cx="30" cy="30" r="30" fill="#080808"/><path d="M41.5 30l-17 10V20z" fill="#fff"/></svg>',
    "avatar": '<svg viewBox="0 0 1000 1000" aria-hidden="true"><circle cx="500" cy="500" r="500" fill="#ccc"/><path fill="#a0a09f" d="M830.8 874.927c-77.344-60.8-187.181-104.877-227.88-111.347-20.335-3.233-20.8-59.1-20.8-59.1s59.746-59.106 72.768-138.584c35.029 0 56.666-84.5 21.631-114.226C677.986 420.37 721.551 206 501 206S324.015 420.37 325.473 451.666c-35.033 29.729-13.4 114.226 21.632 114.226 13.021 79.478 72.77 138.584 72.77 138.584s-.464 55.871-20.8 59.1c-40.883 6.5-151.537 50.943-228.934 112.176C65.84 784.12 0 649.751 0 500 0 223.858 223.858 0 500 0s500 223.858 500 500c0 149.3-65.441 283.311-169.2 374.927z"/></svg>',
}

# ---------------------------------------------------------------- helpers
def esc(s):
    return html.escape(s, quote=True)


def pos(x, y, w=None, h=None, top=HEADER_H):
    s = f"left:{round(x - CANVAS_LEFT)}px;top:{round(y - top)}px;"
    if w is not None:
        s += f"width:{round(w)}px;"
    if h is not None:
        s += f"height:{round(h)}px;"
    return s


class El:
    def __init__(self, y, markup):
        self.y, self.markup = y, markup


def T(x, y, w, content, font="enr", size=14, weight=400, color="#292F33", align=None,
      lh="normal", ls=None, italic=False, tag="div", cls="", style="", raw=False, h=None):
    """Text block. `content` is plain text unless raw=True (then trusted HTML)."""
    body = content if raw else esc(content).replace("\n", "<br>")
    st = pos(x, y, w, h) + f"font:{'italic ' if italic else ''}{weight} {size}px/{lh} {FONTS[font]};color:{color};"
    if align:
        st += f"text-align:{align};"
    if ls:
        st += f"letter-spacing:{ls};"
    st += style
    return El(y, f'<{tag} class="a {cls}" style="{st}">{body}</{tag}>')


def I(x, y, w, h, src, alt="", href=None, radius=None, cls="", ext=False, fit="cover"):
    r = f"border-radius:{radius};" if radius else ""
    attrs = f'src="{esc(src)}" alt="{esc(alt)}" width="{w}" height="{h}" loading="lazy"'
    if href:
        tgt = ' target="_blank" rel="noopener"' if ext else ""
        return El(y, f'<a class="a {cls}" href="{esc(href)}"{tgt} style="{pos(x, y, w, h)}{r}">'
                     f'<img {attrs} style="width:100%;height:100%;object-fit:{fit};{r}"></a>')
    return El(y, f'<img class="a {cls}" {attrs} style="{pos(x, y, w, h)}object-fit:{fit};{r}">')


def BOX(x, y, w, h, style, cls="deco"):
    return El(y, f'<div class="a {cls}" style="{pos(x, y, w, h)}{style}"></div>')


def RAW(y, markup):
    return El(y, markup)


def LINK(x, y, w, text, href, cls="view-link", ext=False, style=""):
    tgt = ' target="_blank" rel="noopener"' if ext else ""
    return El(y, f'<a class="a {cls}" href="{esc(href)}"{tgt} style="{pos(x, y, w)}{style}">{esc(text)}</a>')


def stack_shadow(c):
    return ", ".join(f"{c} {n}px {n}px 0 0" for n in (1, 3, 5, 7, 9))


def STACKBTN(x, y, w, h, label, href, bg, sh, icon, ix, iy, isz, lx, ly, size=25, lh="27.5px"):
    st = pos(x, y, w, h) + f"background:{bg};box-shadow:{stack_shadow(sh)};"
    return El(y, (
        f'<a class="a stack-btn" href="{esc(href)}" style="{st}">'
        f'<svg style="left:{ix - x}px;top:{iy - y}px;width:{isz}px;height:{isz}px" {SVG[icon][5:]}'
        f'<span style="left:{lx - x}px;top:{ly - y}px;font-size:{size}px;line-height:{lh}">{esc(label)}</span></a>'))


def BAND(y, h, color):
    """Full-width coloured strip behind the canvas (y in page coordinates)."""
    return f'<div class="full" style="top:{y - HEADER_H}px;height:{h}px;background:{color}"></div>'


# ---------------------------------------------------------------- shell
NAV = [
    ("Home", ""),
    ("Resources", "resources/", [("Local Legislation", "legislation/"), ("Feedback!", "feedback/")]),
    ("About/Board Members", "about/"),
    ("More", None, [("Services", "services/"), ("Events", "events/"), ("Support Us!", "blank/"),
                    ("Photo Gallery", "photo-gallery/"), ("Shop", "shop/"), ("Blog", "blog-1/")]),
]


def nav_html(p, current):
    out = []
    for item in NAV:
        label, href = item[0], item[1]
        subs = item[2] if len(item) > 2 else []
        cur = ' aria-current="page"' if href is not None and href == current else ""
        if href is None:
            top = f'<button type="button" aria-haspopup="true">{esc(label)}</button>'
        else:
            top = f'<a href="{p}{href}"{cur}>{esc(label)}</a>'
        sub = ""
        if subs:
            sub = '<ul class="sub">' + "".join(
                f'<li><a href="{p}{h}"{" aria-current=page" if h == current else ""}>{esc(l)}</a></li>' for l, h in subs) + "</ul>"
        out.append(f"<li>{top}{sub}</li>")
    return '<ul class="nav">' + "".join(out) + "</ul>"


def header(p, current):
    logo = WIX + "996292_c27297a55ebd4707ba1e7e31cc39572e~mv2.png/v1/fill/w_236,h_154,al_c,q_85,usm_0.66_1.00_0.01/logo.png"
    paypal = WIX + "996292_f4100cd3c3ee4b45940f760277026f63~mv2.jpg/v1/fill/w_228,h_78,al_c,q_80,usm_0.66_1.00_0.01/paypal.jpg"
    return f'''<header class="band site-header" id="top">
  <div class="canvas">
    <a class="a" href="{p}" style="{pos(178, 8, 118, 77, 0)}"><img src="{logo}" alt="We Stand 4 Something logo" width="118" height="77"></a>
    <a class="a brand-title" href="{p}" style="{pos(301, 81, None, None, 0)}">We <b>Stand</b> 4 Something</a>
    <a class="a brand-tag" href="{p}" style="{pos(301, 119, None, None, 0)}">"Enhancing Independence for People with Disabilities."</a>
    <button class="menu-toggle" type="button" aria-expanded="false" aria-controls="site-nav">&#9776; Menu</button>
    <nav class="a" id="site-nav" aria-label="Main" style="{pos(729, 113, None, 40, 0)}">{nav_html(p, current)}</nav>
    <div class="a dotted" style="{pos(190, 223, 462, None, 0)}"></div>
    <a class="a pp" href="{p}blank/" style="{pos(897, 247, 114, 39, 0)}"><img src="{paypal}" alt="PayPal" width="114" height="39"></a>
    <a class="a pp" href="{p}blank/" style="{pos(1021, 247, 92, 26, 0)}"><img src="https://www.paypalobjects.com/en_US/i/btn/btn_donate_LG.gif" alt="Donate with PayPal" width="92" height="26"></a>
  </div>
</header>'''


def footer():
    return f'''<footer class="band site-footer">
  <div class="canvas">
    <p class="a ft-logo" style="{pos(149, 39, None, None, 0)}">WS<span>4</span>S</p>
    <p class="a ft-txt" style="{pos(149, 152, 260, None, 0)}">Education, Advocacy, Empowerment</p>
    <div class="a ft-txt" style="{pos(910, 20, 210, None, 0)}">We Stand 4 Something<br>PO Box 207, Greenwood,<br>Delaware 19950<br>302. 669 WS4S (9747)<br><a href="mailto:info@westand4something.org">info@westand4something.org</a></div>
    <p class="a ft-txt" style="{pos(562, 152, 230, None, 0)}">&copy; 2025 by We Stand 4 Something</p>
  </div>
</footer>'''


MENU_JS = """<script>
document.querySelector('.menu-toggle').addEventListener('click', function () {
  var h = document.querySelector('.site-header');
  var open = h.classList.toggle('open');
  this.setAttribute('aria-expanded', open);
});
</script>"""


def page(slug, title, content_h, elements, bands="", main_bg="#fff", desc=None, extra_head="", extra_body=""):
    depth = 0 if slug == "" else slug.strip("/").count("/") + 1
    p = "../" * depth
    body_els = "\n".join("    " + e.markup for e in sorted(elements, key=lambda e: e.y))
    d = desc or "We Stand 4 Something — Enhancing Independence for People with Disabilities. Education, Advocacy, Empowerment."
    doc = f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)}</title>
<meta name="description" content="{esc(d)}">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(d)}">
<meta property="og:image" content="{WIX}996292_29f929dcf65f4b76b7d5e6343b237bca~mv2.png">
<link rel="icon" href="{WIX}996292_c27297a55ebd4707ba1e7e31cc39572e~mv2.png/v1/fill/w_64,h_64,al_c,q_85/favicon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="{GOOGLE_FONTS}">
<link rel="stylesheet" href="{p}assets/css/site.css">
{extra_head}</head>
<body>
<a class="skip" href="#main">Skip to content</a>
{header(p, slug)}
<main id="main" class="band page" style="height:{content_h}px;background:{main_bg}">
  {bands}
  <div class="canvas">
{body_els}
  </div>
</main>
{footer()}
{MENU_JS}
{extra_body}</body>
</html>
'''
    doc = doc.replace("{{P}}", p)
    path = os.path.join(ROOT, slug, "index.html")
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(doc)
    return path


def ch(total_h):
    """Content height from the original page height (header + content + footer)."""
    return total_h - HEADER_H - FOOTER_H


# ================================================================ PAGES
def build_home():
    W = "#F0FAFF"
    big_logo = WIX + "996292_c27297a55ebd4707ba1e7e31cc39572e~mv2.png/v1/fill/w_960,h_960,al_c,q_90,usm_0.66_1.00_0.01/logo.png"
    emm = WIX + "f45d39_0f746333cff946bda5b82c822bd27a7e~mv2.jpeg/v1/fill/w_328,h_308,al_c,q_80,usm_0.66_1.00_0.01/Emmanuel%20Jenkins.jpeg"
    els = [
        I(142, 520, 480, 480, big_logo, "We Stand 4 Something logo: a raised hand holding the globe", radius="7px"),
        T(629, 364, 208, "Click to learn more!", "trend", 21, 400, W, lh="21px", style="text-transform:uppercase", cls="m-big"),
        STACKBTN(626, 458, 224, 71, "Friday Feast", "friday-feast/", "#006C6D", "#003637", "chevrons", 626, 465, 55, 685, 479),
        STACKBTN(629, 565, 224, 71, "Social", "services/", "#6DCFB6", "#37685B", "social", 653, 573, 55, 760, 586),
        STACKBTN(629, 648, 221, 72, "Coaching", "services/", "#01B1AF", "#015958", "chat", 649, 656, 55, 718, 670),
        STACKBTN(634, 815, 224, 71, "Advocacy", "services/", "#006C6D", "#003637", "megaphone", 653, 823, 55, 723, 836),
        STACKBTN(634, 1001, 221, 71, "Life Skills", "services/", "#123636", "#091B1B", "network", 649, 1009, 55, 724, 1022),
        STACKBTN(627, 1139, 219, 74, "Resources", "resources/", "#6DCFB6", "#37685B", "down", 656, 1154, 43, 705, 1159, 24, "33.6px"),
        BOX(869, 361, 13, 526, "border-left:6.67px solid #CADDE6"),
        T(918, 374, 194, "Leave Your Mark", "os", 25, 400, "#CADDE6", "center", tag="h2", style="margin:0"),
        I(914, 427, 164, 154, emm, "Emmanuel Jenkins", href="emmanuel/"),
        T(876, 610, 240, "Emmanuel Jenkins is a dedicated advocate and the founder of We Stand 4 Something. With over 20 years of experience in public speaking and community leadership, he works tirelessly to support individuals with disabilities and their families.",
          "enr", 18, 400, "#fff", "center", "23.4px", cls="m-text"),
        RAW(873, f'<a class="a" href="emmanuel/" style="{pos(921, 873, 151, 33)}background:#282626;color:{W};font:300 18px/33px {FONTS["avenir"]};letter-spacing:.9px;text-align:center">Read More</a>'),
    ]
    icons = [("8d6893330740455c96d218258a458aa4.png", "https://www.instagram.com/westand4somthing/", "Instagram"),
             ("9c4b521dd2404cd5a05ed6115f3a0dc8.png", "https://twitter.com/4Westand", "Twitter"),
             ("e316f544f9094143b9eac01f1f19e697.png", "https://www.facebook.com/westand4something", "Facebook")]
    social = '<div class="a" style="' + pos(686, 1549, 100, 30) + 'display:flex;gap:5px">' + "".join(
        f'<a href="{h}" target="_blank" rel="noopener" aria-label="{n}"><img src="{WIX}{f}/v1/fill/w_60,h_60,al_c,q_85/{f}" alt="{n}" width="30" height="30"></a>'
        for f, h, n in icons) + "</div>"
    els.append(RAW(1549, social))
    page("", "Home | ws4s", ch(1815), els, main_bg="#000")


def build_resources():
    items = [
        (526, 608, 328, "The Division of Developmental Disabilities Services Handbook for Renters", 51,
         "f45d39_c14795d3ad5b49e6a1c885f660148fe7~mv2.png/v1/fill/w_510,h_380,al_c,lg_1,q_85/House-removebg-preview.png", 504, 601, 255, 190, 812,
         "https://docs.wixstatic.com/ugd/1829a9_888cd069874748a98f5e40334c013705.pdf"),
        (893, 225, 520, "Delaware Disability Hub", 25,
         "f45d39_92794a9a269a4f4b9a09152d51dafb81~mv2.png/v1/fill/w_562,h_450,al_c,lg_1,q_85/DDH_edited.png", 491, 947, 281, 225, 1201,
         "https://deldhub.gacec.delaware.gov/"),
        (1302, 365, 449, "Guide to Services For Delawareans and\nPersons with Disabilities", 51,
         "f45d39_ea356b7e1af94a81817b2c9fc5f79e69~mv2.png/v1/fill/w_324,h_422,al_c,lg_1,q_85/DHSS_edited.png", 550, 1400, 162, 211, 1669,
         "https://dhss.delaware.gov/dhss/dsaapd/files/aging_and_disabilities_guide.pdf"),
        (1724, 160, 552, "DART Paratransit", 25,
         "f45d39_3c9f6a123f204a3c8ac51008f288276d~mv2.jpg/v1/fill/w_450,h_450,al_c,lg_1,q_80/DART.jpg", 519, 1783, 225, 225, 2057,
         "https://dartfirststate.com/services/para_services.shtml"),
        (2130, 259, 503, "Traumatic brain injury (TBI)", 25,
         "f45d39_e219687224c343498d0e3be8ca6d015d~mv2.jpg/v1/fill/w_346,h_346,al_c,lg_1,q_80/SCPD-Logo.jpg", 545, 2188, 173, 173, 2422,
         "https://scpd.delaware.gov/brain-injury-funds.shtml"),
        (2495, 232, 517, "Mid-Atlantic ADA Center", 25,
         "f45d39_f53e48d8dab143ca8cc233664f037c2d~mv2.png/v1/fill/w_320,h_320,al_c,q_85,usm_0.66_1.00_0.01/ADA.png", 551, 2552, 160, 160, 2770,
         "https://www.adainfo.org/"),
        (2841, 162, 551, "Autism Delaware", 25,
         "f45d39_953c5bcfa6284d16a500b58d8295ff76~mv2.png/v1/fill/w_302,h_302,al_c,q_85,usm_0.66_1.00_0.01/Autism-Delaware_edited.png", 556, 2905, 151, 151, 3091,
         "https://www.autismdelaware.org/about/autism-in-delaware/"),
        (3151, 312, 476, "The Delaware Disabilities Council (DDC)", 51,
         "f45d39_db45f4c8bf184859bf41cbad3e4db663~mv2.png/v1/fill/w_474,h_284,al_c,lg_1,q_85/agency-logo.png", 513, 3228, 237, 142, 3416,
         "https://ddc.delaware.gov/"),
        (3488, 60, 602, "EPIC", 25,
         "f45d39_069b81adcc4f4094aec4c3efb5d0905d~mv2.png/v1/fill/w_316,h_230,al_c,q_85,usm_0.66_1.00_0.01/EPIC-Logo_edited.png", 553, 3536, 158, 115, 3685,
         "https://www.epicdelaware.org/"),
    ]
    els = [
        T(424, 349, 420, "Resources", "lulo", 44, 800, "#203931", tag="h1", style="margin:0;text-transform:uppercase;letter-spacing:2px", cls="m-big"),
        BOX(424, 418, 375, 5, "border-top:2px solid #01B1AF"),
        T(339, 432, 547, "We Stand 4 Something non-profit will continually be updating the resources on this page to help those with access and functional needs to gain the appropriate services that you are entitled to.",
          "lb", 15, 400, "#292F33", "center", cls="m-text"),
    ]
    for ty, tw, tx, title, th, img, ix, iy, iw, ih, vy, url in items:
        cx = 632  # centre line of the column
        els.append(T(cx - 304, ty, 608, title, "pop", 18, 600, "#292F33", "center", ls="0.18px", tag="h2", style="margin:0"))
        els.append(I(ix, iy, iw, ih, WIX + img, title, href=url, ext=True, fit="contain"))
        els.append(LINK(cx - 60, vy, 120, "VIEW", url, ext=True))
    els += [
        BOX(348, 3743, 568, 173, "background:#CADDE6"),
        RAW(3784, f'<a class="a" href="../feedback/" style="{pos(406, 3784, 452)}font:400 20px/normal {FONTS["lb"]};color:#515E65;text-align:center">If there are any other resources that you feel are important and do not see listed above, please click here to let us know on our feedback page!</a>'),
    ]
    page("resources/", "Resources | ws4s", ch(4152), els, main_bg="#A4F7D5")


def build_legislation():
    seal = WIX + "0bae78_b5a13387533c405987c97ce6f0c5c84f~mv2.png/v1/fill/w_300,h_298,al_c,q_85,usm_0.66_1.00_0.01/Seal_of_Delaware.png"
    thumb = WIX + "0bae78_10a419dc9cd84e21b8a7c458a2f30f24~mv2.jpg/v1/fill/w_526,h_298,al_c,q_80,usm_0.66_1.00_0.01/bill-signing.jpg"
    video = ("https://livestream.com/StateofDelaware/aug6/videos/194701430")
    news = "https://news.delaware.gov/2019/08/07/icymi-governor-carney-signs-legislation-protecting-health-care-for-delawareans/"
    flourish = ('<svg class="a deco" style="' + pos(558, 445, 194, 50) + '" viewBox="0 0 194 50" aria-hidden="true" fill="none" stroke="#6D706C" stroke-width="1.6">'
                '<path d="M8 25h62M124 25h62"/><path d="M70 25c8-14 20-14 27 0 7 14 19 14 27 0"/><path d="M70 25c8 14 20 14 27 0 7-14 19-14 27 0"/>'
                '<circle cx="97" cy="25" r="3" fill="#6D706C"/><circle cx="8" cy="25" r="2" fill="#6D706C"/><circle cx="186" cy="25" r="2" fill="#6D706C"/></svg>')
    els = [
        I(206, 362, 150, 149, seal, "Seal of the State of Delaware", cls="deco"),
        T(470, 393, 360, "Legislative news", "cinzel", 28, 700, "#6D706C", "center", "28px", ls="3.36px", tag="h1", style="margin:0"),
        RAW(445, flourish),
        I(909, 362, 150, 149, seal, "Seal of the State of Delaware", cls="deco"),
        BOX(153, 542, 273, 410, "background:#F0FAFF"),
        T(160, 542, 259, "(Click picture to watch video)", "enr", 10, 400, "#000", "center"),
        I(157, 560, 263, 149, thumb, "Governor Carney signing Senate Bills 35 and 92", href=video, ext=True),
        T(179, 720, 215, f'On August, 7th 2019, Governor John Carney signed Senate Bill 35 and Senate Substitute 1 for Senate Bill 92 into effect. Both bills were passed to ensure that individuals with pre-existing conditions are protected and do not have limited access to health care. <a href="{news}" target="_blank" rel="noopener" style="text-decoration:underline">Click here to learn more!</a>',
          "pf", 15, 400, "#000", lh="19.6px", ls="0.45px", raw=True, cls="m-text"),
    ]
    page("legislation/", "Local Legislation | ws4s", ch(1201), els, main_bg="#B6CDE1")


def contact_form(action_subject, x, y, w, h, fields, button, style_input, btn_style, heading=None):
    """A form that opens the visitor's email app addressed to WS4S (no server needed)."""
    inner = []
    if heading:
        inner.append(heading)
    for fx, fy, fw, fh, name, ph, kind in fields:
        st = f"position:absolute;left:{fx - x}px;top:{fy - y}px;width:{fw}px;height:{fh}px;{style_input}"
        lbl = f' aria-label="{esc(ph)}"'
        if kind == "textarea":
            inner.append(f'<textarea name="{name}" placeholder="{esc(ph)}"{lbl} style="{st}" required></textarea>')
        else:
            req = " required" if name in ("name", "first", "email") else ""
            inner.append(f'<input type="{kind}" name="{name}" placeholder="{esc(ph)}"{lbl} style="{st}"{req}>')
    bx, by, bw, bh, label = button
    inner.append(f'<button type="submit" style="position:absolute;left:{bx - x}px;top:{by - y}px;width:{bw}px;height:{bh}px;{btn_style}">{esc(label)}</button>')
    return (f'<form class="a wform" data-subject="{esc(action_subject)}" style="{pos(x, y, w, h)}" '
            f'action="mailto:info@westand4something.org" method="post" enctype="text/plain">' + "".join(inner) + "</form>")


FORM_JS = """<script>
// Turns form submissions into a pre-filled email to info@westand4something.org
document.querySelectorAll('form[data-subject]').forEach(function (f) {
  f.addEventListener('submit', function (e) {
    e.preventDefault();
    var lines = [];
    f.querySelectorAll('input,textarea').forEach(function (el) {
      if (el.value) lines.push((el.getAttribute('placeholder') || el.name) + ': ' + el.value);
    });
    location.href = 'mailto:info@westand4something.org?subject=' + encodeURIComponent(f.dataset.subject) +
      '&body=' + encodeURIComponent(lines.join('\\n'));
  });
});
</script>"""


def build_feedback():
    inp = "border:2px solid #373B4D;background:#fff"
    form = contact_form("Website feedback", 317, 782, 630, 497, [
        (351, 855, 280, 66, "first", "First Name", "text"),
        (629, 855, 280, 66, "last", "Last Name", "text"),
        (351, 919, 280, 66, "email", "Email", "email"),
        (629, 919, 280, 66, "phone", "Phone", "tel"),
        (351, 983, 558, 126, "message", "Type your message here...", "textarea"),
    ], (723, 1109, 186, 52, "Submit"), inp, "background:#373B4D;color:#fff;font:400 14px Georgia,serif",
        heading='<h2 style="position:absolute;left:36px;top:0;margin:0;font:400 30px Georgia,serif;color:#000">Contact Us</h2>')
    els = [
        T(400, 361, 441, "Your Feedback Matters!", "os", 50, 700, "#01B1AF", "center", tag="h1", style="margin:0", cls="m-big"),
        T(387, 533, 484, "We Stand 4 Something appreciates and encourages any feedback that you can provide to us, including ways to make our website more accessible and easier to navigate. We strive to offer the best services and resources, so let us know below how we are doing and how we can improve!",
          "lb", 20, 700, "#515E65", "center", cls="m-text"),
        BOX(317, 782, 630, 497, "background:#fff"),
        RAW(782, form),
    ]
    bands = BAND(509, 3, "#61AA93")
    page("feedback/", "Feedback! | ws4s", ch(1576), els, bands, main_bg="#00E689", extra_body=FORM_JS)


def build_about():
    H = "#292F33"
    G = "#515E65"
    els = [
        T(400, 408, 463, "MISSION STATEMENT", "os", 25, 700, H, "center", tag="h2", style="margin:0"),
        BOX(168, 442, 920, 1, "border-top:0.67px solid rgba(154,174,184,.8)"),
        T(254, 468, 790, "We Stand 4 Something, Inc. provides the bridge between traditional services and the full, engaged lives people want. We have first-hand experiences understanding people with disabilities because we are people with disabilities and their families.  We pledge to primarily employ people with disabilities to deliver our services. We empower people and their families to use advocacy to tailor their environments to supplement their strengths. We support people to live lives of quality, fully included within their communities.",
          "enr", 20, 400, G, cls="m-text"),
        T(400, 664, 463, "VISION STATEMENT", "os", 25, 700, H, "center", tag="h2", style="margin:0"),
        BOX(172, 699, 920, 1, "border-top:0.67px solid rgba(154,174,184,.8)"),
        T(258, 720, 759, "To enhance the lives of people with disabilities by teaching them skills they can use to speak for themselves for their whole lives.",
          "enr", 20, 400, G, italic=True, cls="m-text"),
        T(400, 798, 420, "Values and Beliefs", "os", 25, 700, H, "center", "27.5px", tag="h2", style="margin:0"),
        T(203, 848, 896, "We believe everyone is entitled to an individualized education that plays to their strengths. We provide education and advocacy services for families and assist them through the IEP process. We value the voices of people with disabilities and know that each person has a story to tell. We provide teaching self-advocacy skills and coaching in public speaking so people can find their own voice and share it with others. We believe all people should have a safe environment in which to live that is suited to their unique needs and to live where they desire. We provide assistance with locating housing, supporting people throughout the process, from finding a great location to move-in day and beyond. We believe all people should be able to access public services.",
          "enr", 20, 400, G, lh="26px", cls="m-text"),
        T(203, 1106, 889, "We provide assistance to navigate application and eligibility requirements for assistance programs. We believe all people need to get out and have fun! We provide opportunities for people to get together in their communities, connect with others, and have a good time! We value the safeguards provided to us by the ADA. We believe all people should be educated about the ADA. Our approved ADA trainers provide information to individuals and organizations using the Mid-Atlantic ADA Center and Cornell University’s training materials. We believe every person who wants to work must have the opportunity to work. We help people find employment while offering training to develop needed skills,  including resume writing, dressing for success, communicating at work, etc. that will help them to be great employees. We believe everyone needs a safe space and the opportunity to talk to others experiencing the same life circumstances.",
          "enr", 20, 400, G, lh="26px", cls="m-text"),
        T(203, 1364, 889, "We offer services to help families connect to one another so they can share experiences and learn from each other.",
          "enr", 20, 400, G, lh="26px", cls="m-text", style="padding-top:2px"),
        T(400, 1462, 463, "Board Members' Biography", "os", 25, 700, H, "center", tag="h2", style="margin:0"),
    ]
    members = [
        ("Emmanuel Jenkins", "emmanuel/", 1515, 535, 1546, 180, 180, "0bae78_65688fe79512416aabb7ebcc737b1519~mv2_d_1440_1440_s_2.jpg/v1/fill/w_360,h_360,al_c,q_80,usm_0.66_1.00_0.01/emmanuel.jpg", "50%"),
        ("Marissa Castello", "marissa/", 1756, 535, 1793, 200, 188, "b08a92_e0b91d78637244ef8ad543b47224477c~mv2.jpeg/v1/fill/w_400,h_376,al_c,q_80,usm_0.66_1.00_0.01/Marissa.jpeg", "50%"),
        ("Selena Butcher", "se/", 2018, 549, 2061, 163, 200, "f45d39_72d0328eadc24cb7bbab3ae79294a8ce~mv2.jpg/v1/crop/x_0,y_0,w_967,h_1165/fill/w_326,h_400,al_c,q_80,usm_0.66_1.00_0.01/selena.jpg", None),
        ("Dielle De Noon", "dielle/", 2282, 550, 2322, 163, 163, "f45d39_1f23f76352474dd3b8ddf23fa1303ab4~mv2.jpg/v1/crop/x_0,y_505,w_3024,h_3022/fill/w_326,h_326,al_c,q_80,usm_0.66_1.00_0.01/dielle.jpg", None),
    ]
    for name, href, ny, ix, iy, iw, ih, img, r in members:
        els.append(LINK(482, ny, 300, name, "../" + href, cls="navy-link"))
        els.append(I(ix, iy, iw, ih, WIX + img, name, href="../" + href, radius=r))
    els.append(LINK(981, 2881, 100, "Next", "../emmanuel/", cls="pager"))
    bands = BAND(354, 435, "#F0FAFF") + BAND(2967, 5, "#CADDE6")
    page("about/", "About/Board Members | ws4s", ch(3208), els, bands, main_bg="#CADDE6")


def popup(pid, title):
    return f'''<dialog class="popup" id="{pid}" aria-labelledby="{pid}-t">
  <button class="x" type="button" aria-label="Close" onclick="this.closest('dialog').close()">&times;</button>
  <h2 id="{pid}-t">{esc(title)}</h2>
  <p class="contact">Tel: <a href="tel:+13026699747">302-669-9747</a> &nbsp;|&nbsp; <a href="mailto:info@westand4something.org">info@westand4something.org</a></p>
  <form class="wform" data-subject="{esc(title)}" action="mailto:info@westand4something.org" method="post" enctype="text/plain">
    <input type="text" name="name" placeholder="Name" aria-label="Name" required>
    <input type="email" name="email" placeholder="Email" aria-label="Email" required>
    <textarea name="message" placeholder="Type your message here..." aria-label="Message" rows="5"></textarea>
    <button type="submit">Submit</button>
  </form>
</dialog>'''


def build_services():
    D = "#292F33"
    cl = 'style="color:#8B0000;text-decoration:underline;cursor:pointer;background:none;border:0;padding:0;font:inherit"'
    els = [
        T(400, 358, 465, "All services are free of charge for our clients...", "din", 20, 700, "#00995B", "center", italic=True),
        T(149, 391, 300, "OUR SERVICES", "os", 25, 400, D, tag="h1", style="margin:0"),
    ]
    blocks = [
        (448, 461, "chat", "Advocacy", 443, 519, 801,
         "“Teach a man to fish and he eats for a lifetime...”  We are firm believers in self advocacy.  Learning to speak up for yourself is the first step to true independence.  We also work with our state legislators and community partners to increase service offerings throughout Delaware."),
        (699, 711, "network", "Resource Connection", 686, 814, 828,
         "Are you looking for access to financial, educational, life skills, and/or social development resources?  At We Stand 4 Something, we open the door to possibilities that allow those we serve to be more independent and live the life he/she deserves.  If you or someone you know is looking for access to services, we are here to assist you."),
        (1047, 1060, "social", "Social interaction groups", 1045, None, None, None),
    ]
    for sy, iy, icon, title, ty, dy, dw, desc in blocks:
        els.append(RAW(sy, f'<div class="a deco" style="{pos(159, sy, 82, 82)}"><svg style="width:82px;height:82px;fill:#00995B" {SVG["square"][5:]}<svg style="position:absolute;left:13px;top:{iy - sy}px;width:55px;height:55px;fill:#004D2E" {SVG[icon][5:]}</div>'))
        els.append(T(250, ty, 400, title, "amatic", 40, 400, D, tag="h2", style="margin:0"))
        if desc:
            els.append(T(253, dy, dw, desc, "din", 26, 300, D, cls="m-text"))
    els.append(T(292, 1181, 781, f'Brain Injury Survivor Group:  Our brain injury social interaction group meets virtually on the 1st and 3rd Tuesday of each month.  If you are interested in joining, please <button type="button" {cl} onclick="document.getElementById(\'brain-injury\').showModal()">click here</button> to register',
                 "din", 26, 300, D, raw=True, cls="m-text"))
    els.append(T(292, 1294, 781, f'Parent/Caregiver Social Interaction Group:  If you would like to join our parent/caregiver group, please <button type="button" {cl} onclick="document.getElementById(\'caregiver\').showModal()">click here</button> to register',
                 "din", 26, 300, D, raw=True, cls="m-text"))
    extra = popup("brain-injury", "Join our Brain Injury Group") + "\n" + popup("caregiver", "Parent/Caregiver Group") + "\n" + FORM_JS
    page("services/", "Services | ws4s", ch(1849), els, main_bg="#CADDE6", extra_body=extra)


CAL_JS = """<script>
(function () {
  var cal = document.getElementById('cal'), shown = new Date(); shown.setDate(1);
  var months = ['January','February','March','April','May','June','July','August','September','October','November','December'];
  function draw() {
    var y = shown.getFullYear(), m = shown.getMonth(), today = new Date();
    cal.querySelector('.cal-title').textContent = months[m] + ' ' + y;
    cal.querySelector('.cal-today i').textContent = today.getDate();
    var grid = cal.querySelector('.cal-grid'), html = '';
    ['Sun','Mon','Tue','Wed','Thu','Fri','Sat'].forEach(function (d) { html += '<div class="cal-dow">' + d + '</div>'; });
    var start = new Date(y, m, 1 - new Date(y, m, 1).getDay());
    for (var i = 0; i < 42; i++) {
      var d = new Date(start); d.setDate(start.getDate() + i);
      var cls = 'cal-day' + (d.getMonth() !== m ? ' muted' : '') + (d.toDateString() === today.toDateString() ? ' today' : '') + (i >= 35 ? ' last' : '');
      html += '<div class="' + cls + '"><span>' + d.getDate() + '</span></div>';
    }
    grid.innerHTML = html;
  }
  cal.querySelector('.prev').onclick = function () { shown.setMonth(shown.getMonth() - 1); draw(); };
  cal.querySelector('.next').onclick = function () { shown.setMonth(shown.getMonth() + 1); draw(); };
  cal.querySelector('.cal-today').onclick = function () { shown = new Date(); shown.setDate(1); draw(); };
  draw();
})();
</script>"""


def build_events():
    calendar = (f'<section class="a cal m-full" id="cal" aria-label="Events calendar" style="{pos(238, 380, 797)}">'
                '<div class="cal-head"><button type="button" class="cal-today"><i>15</i>TODAY</button>'
                '<button type="button" class="prev" aria-label="Previous month">&#10094;</button>'
                '<button type="button" class="next" aria-label="Next month">&#10095;</button>'
                '<span class="cal-title" aria-live="polite"></span></div><div class="cal-grid"></div></section>')
    inp = "border:0.67px solid #67D6D6;box-shadow:0 2px 0 0 #67D6D6;background:#fff"
    form = contact_form("Event registration", 277, 1081, 710, 423, [
        (291, 1158, 680, 60, "name", "Name", "text"),
        (291, 1230, 680, 60, "email", "Email", "email"),
        (291, 1302, 680, 129, "message", "Tell us which event you are registering for", "textarea"),
    ], (291, 1428, 340, 53, "Submit"), inp,
        f"background:#6DCFB6;color:#F0FAFF;border-radius:5px;box-shadow:{stack_shadow('#37685B')};font:400 25px 'Open Sans',sans-serif",
        heading=f'<h2 style="position:absolute;left:14px;top:27px;margin:0;font:italic 700 25px {FONTS["bree"]};color:#00E689">Register for events</h2>')
    els = [
        RAW(380, calendar),
        BOX(277, 1081, 710, 423, "background:#fff"),
        RAW(1081, form),
    ]
    page("events/", "Events | ws4s", ch(1780), els, main_bg="#CADDE6", extra_body=CAL_JS + FORM_JS)


def build_support():
    G = "#515E65"
    els = [
        I(554, 382, 196, 89, WIX + "996292_06854b9ca8db4d7f869b681f8c7a22e7~mv2.jpg/v1/fill/w_392,h_178,al_c,lg_1,q_80/support.jpg", "Support Us"),
        T(166, 512, 160, "Donate!", "script", 38, 400, "#004D2E", tag="h2", style="margin:0"),
        T(333, 513, 665, "We rely heavily on the support of the community!  Show your love today - send us a donation - no matter what size!  Rest assured your funds will go directly to support our programs and bring someone with a disability one step closer to realizing the dream of living a full, active and rewarding life!",
          "enr", 14, 400, G, cls="m-text"),
        RAW(600, f'<div class="a" style="{pos(544, 600, 216, 39)}display:flex;align-items:center;gap:10px">'
                 f'<img src="{WIX}996292_f4100cd3c3ee4b45940f760277026f63~mv2.jpg/v1/fill/w_228,h_78,al_c,q_80/paypal.jpg" alt="PayPal" width="114" height="39">'
                 '<img src="https://www.paypalobjects.com/en_US/i/btn/btn_donate_LG.gif" alt="Donate" width="92" height="26" style="margin-top:6px"></div>'),
        T(333, 682, 665, 'When shopping on Amazon, use Amazon Smile! Each time you shop with Amazon smile, Amazon donates 0.5% of the price of your purchase to your favorite charity, We Stand 4 Something! All that you have to do is log onto <a href="https://smile.amazon.com/" target="_blank" rel="noopener" style="text-decoration:underline">smile.amazon.com</a>. On your first visit you will be able to select your charitable organization of choice. Simply put We Stand 4 Something and then shop away!',
          "enr", 14, 400, G, raw=True, cls="m-text"),
        I(585, 775, 133, 73, WIX + "0bae78_e2b8f9a41bfc4f9da784553a86369c5e~mv2.png/v1/fill/w_266,h_146,al_c,q_85,usm_0.66_1.00_0.01/amazon.png", "Amazon Smile", href="https://smile.amazon.com/", ext=True, fit="contain"),
        T(161, 915, 160, "Volunteer!", "script", 38, 400, "#004D2E", tag="h2", style="margin:0"),
        T(321, 910, 665, "Everyone has something to offer!  We currently have a need for office help (filing, phones, etc), media mavens (website, facebook, twitter), and probably some other things that we don't even know we need!  <a href=\"mailto:volunteer@westand4something.org?subject=Hi!%20%20I%20have%20amazing%20skills%20and%20I%20would%20like%20to%20volunteer!\" style=\"text-decoration:underline\">Contact us</a> today and find out how you fit in.",
          "enr", 14, 400, G, raw=True, cls="m-text"),
    ]
    page("blank/", "Support Us! | ws4s", ch(1232), els, main_bg="#CADDE6")


GALLERY = """0bae78_60187f8ba06641419b8c11b3edaf49eb 0bae78_76674be9d4e24ba582d18c120463b366 0bae78_2eb74808965b49b7bc249c91adcb8865 0bae78_037e22db4a6f4c0ab5fc19523a19ff66 0bae78_03167f7903bf451b98540b0b8bb4e51b 0bae78_ec68d3ad545e456bb3691168c33f745d 0bae78_d594271b8691449cae5095a29bd2b2c6 0bae78_099b4507329d4837a1908fa9b02b23c6 0bae78_e8e13482b692441493322a9e4610bbf2 0bae78_6ba72f74242d436291d64c5cbedf1db1 0bae78_e637d20b747d4590832e0457da09488f 0bae78_d9064c1af2db41caa591f85b541605f4 0bae78_d1ced7ef1e8743d0a4df5343806d371c 0bae78_1d47c556a67d47eb9062b550ab2840e9 0bae78_6ce987d738c04bb59756104eb3e0c204 0bae78_940d72b2a83f4a45838518e5e143374e 0bae78_1943e9ce30fd4e5bb4cb008e6e78f7d2 0bae78_7580c96add4c45df945d0c4e1fbcf118 0bae78_15d74f3c753a4d498e8cd6a67b09e3d1 0bae78_25358f8fde79450fadba9178a1ba836b 0bae78_b83b094fc1224884beb451ea4cbf981d 0bae78_337f58be37664b73869b6a4006bcb44a 0bae78_8c976e44cbb747dca38c2f839826e834 0bae78_e51e5279a03a47f6a57c43c55c625a78 0bae78_f1a72dce4ffb434e9145deba9b874f98 0bae78_d73e890bd5cb4dd6904261fca9eb88b6 0bae78_18995b281a0e450da4bf764798c879f0 0bae78_63864d30d1f1457f8f9ba0ab25c2b105 0bae78_a1fd8fec05834ab884330175284f3650 0bae78_cf5c3b263516499bb005a030bfe4b941 0bae78_1ae20fd216f741c984176b73f8c9db45 0bae78_966e5952b7ab43299047383bfc57a165 0bae78_31998cc77b0d43fcba88e5a58da44fdd 0bae78_488e37aa36d84f7199b5dc72dc160637 0bae78_baa85ec1a8d04f9c88ff4628fd103fc4 0bae78_35a60ac215714d4a9a34ade929d40e41 0bae78_ffa493ab04484e5998311bc9dda79e40 0bae78_9aced1a9272442439493dede4430dd8e 0bae78_7bcd1e4696ce4b85b94af631a8a5acad 0bae78_866c5cac6a744b17aa5ae92903612672 0bae78_afb48f5dc9f24e918119ecba71d8cb7a 0bae78_927ec0db8ff94e56a3c900502d16b823 0bae78_ffd71f09589c479f9c103093c02769ed 0bae78_89a80475ebad4dd5a8760359a6714703 0bae78_e4f26335235b4991b440e673787bad84 0bae78_b399dd513b3e414ca37066d4a7725058 0bae78_0e099b0c5e0843f89ed329df73a888c5 0bae78_6bc289c035464ab6a1d08b1c571bb932 0bae78_d177026b0ba648b0b86534994d0c5c27 0bae78_80994b832a214e06a5fbd1c78962101a 0bae78_186b59824aeb4c658fb54096a451b6e8 0bae78_24f5dfa0390d4081a1a1a5d992290cfa 0bae78_276d1521b9af431ea558f468c82711c9 0bae78_319ef4851f0141afac32e200301ca3c8 0bae78_269602d2684c427f98ce64f4552161a5 0bae78_4c1ac0168c724d2ab04f862b2f4bdc0f 0bae78_3135bf186ab040cf9bc187fb3ac89018 0bae78_196baae517d94383b3a06d3c1edac499 0bae78_2434fb1db7264fada1e5e38ddbc058ed 0bae78_e330d9d3f8a54131b4d90f812e8de7ec 0bae78_1b8ca1eb8ac741d0a1884ba694aeaa70 0bae78_90df960bc58c44109974e6107496a4e8 0bae78_2b09f4497f4b45628d378d702381ef7a 0bae78_70c1771370d7435688d36fe509bfe002 0bae78_e75d76d54a5a4dd0bb67c2216081e36f 0bae78_1f258204bbbe4cc99e96c52297b78440 0bae78_d4b5e8d4efb0443380e74baa7546d889 0bae78_3969717347984d5c99f17ed54382babd 0bae78_72b8e000cecc4614860c87b24c57ad5c 0bae78_e8a4e84aea6149009f04fc4c978987fe 0bae78_e409053f6582404ebd68204253f69e7a 0bae78_8b4270eb37ae4f96933829697aee8b7f 0bae78_2d46beff9ad14b3c97b293cb528ed02c 0bae78_c1088cf519674305bf18023bb6ef4124 0bae78_d9091cf04b984769879ffa9f9adb99a2 0bae78_94340a756bda41119ef1e397e6ab2a81 0bae78_b5ea75bfb1144f73a82376a466eb02a0 0bae78_cc2e15b7d07e4a4d98166ecd84913177 0bae78_04facbe0a4de48d6999d0fa4382f4c45 0bae78_649c5aca0f2e43f082d32619ef9c6a80 0bae78_f292668273fb4bc5986cc265f4f9ea5a 0bae78_a25258e0b7c04c97b2b08336eccf5fd0 0bae78_c62de83ade6348ba8a136fc22272d803 0bae78_15d41ecbb660409d913b580c9a5d4575 0bae78_102de19352e6421db6a593b262fc03ad 0bae78_ab096b3d6daa45e5b9385f28760cc2b9 0bae78_54c35070d9a4494cbb785c4c586ce9a7 0bae78_b5064d16875241e387ffe8203e7e5d5e 0bae78_6f7aefd42b0f4b20957bfba8bf2a1a59 0bae78_6ef207cf512c4a03868267104f87072f 0bae78_646b493843934978a2699db11800869e 0bae78_1e72dff2720f4e54958de620c21cd23a 0bae78_fb8b1e4b8be7400d9bccee1cb7e85b36 0bae78_ad937637f5c14c1790344ea2a19ff54f 0bae78_7b79a66ee5674f90adc9d208ab249c74 0bae78_b425f63823c644da9db0234863e01558""".split()

SLIDER_JS = """<script>
(function () {
  var s = document.querySelector('.slider'), t = s.querySelector('.slider-track'), i = 0;
  function step() { var f = t.querySelector('figure'); return f.getBoundingClientRect().width + 30; }
  function max() { return Math.max(0, t.children.length - Math.floor(s.clientWidth / step())); }
  function go(n) { i = Math.min(Math.max(n, 0), max()); t.style.transform = 'translateX(' + (-i * step()) + 'px)'; }
  s.querySelector('.prev').onclick = function () { go(i - 1); };
  s.querySelector('.next').onclick = function () { go(i + 1); };
  s.addEventListener('keydown', function (e) { if (e.key === 'ArrowLeft') go(i - 1); if (e.key === 'ArrowRight') go(i + 1); });
  window.addEventListener('resize', function () { go(i); });
})();
</script>"""


def build_gallery():
    figs = "".join(
        f'<figure><img src="{WIX}{g}~mv2.jpg/v1/fill/w_564,h_564,al_c,q_80,usm_0.66_1.00_0.01/{g}.jpg" alt="2018 Friday Feast photo {n}" width="376" height="376" loading="lazy"></figure>'
        for n, g in enumerate(GALLERY, 1))
    # the slider runs edge to edge across the window (25px in from each side), like the original
    slider = (f'<div class="a slider m-full" tabindex="0" aria-roledescription="carousel" aria-label="2018 Friday Feast photos" '
              f'style="left:calc(25px - (100vw - 980px) / 2);right:calc(32px - (100vw - 980px) / 2);top:{414 - HEADER_H}px;height:376px">'
              '<button type="button" class="slider-btn prev" style="left:0" aria-label="Previous photos">&#10094;</button>'
              '<button type="button" class="slider-btn next" style="right:0" aria-label="Next photos">&#10095;</button>'
              f'<div class="slider-track">{figs}</div></div>')
    els = [
        T(400, 365, 465, "2018 fRIDAY fEAST", "trend", 27, 400, "#292929", "center", "27px", tag="h1", style="margin:0;text-transform:uppercase"),
        BOX(154, 809, 937, 1, "border-top:0.67px solid #00E689"),
        RAW(414, slider),
    ]
    page("photo-gallery/", "Photo Gallery | ws4s", ch(1090), els, main_bg="#CADDE6", extra_body=SLIDER_JS)


def build_shop():
    els = [T(152, 444, 960, "We don’t have any products to\nshow here right now.", "enr", 24, 400, "#CADDE6", "center", tag="h1", style="margin:0")]
    page("shop/", "Shop | ws4s", ch(1090), els, main_bg="#000")


POSTS = [
    dict(slug="post/2016/07/20/for-those-of-you-who-missed-emmanuel-on-delmarva-life-check-the-video-out-here",
         title="For those of you, who missed Emmanuel on Delmarva life. Check the video out here",
         date="Jul 20, 2016", read="0 min read", youtube="37wSDJ7Un_U", excerpt="", body=""),
    dict(slug="post/2016/06/23/emmanuel-is-live-on-wboc-tv", title="Emmanuel is Live on WBOC TV!",
         date="Jun 23, 2016", read="1 min read",
         image="996292_9dae49e74efe4d098adb14ae92d754fa~mv2.jpg",
         excerpt="Congratulations to We Stand 4 Something Inc. Owner Emmanuel Jenkins! Watch him on ➡WBOC Delmarva Life June 30th @ 5:00pm⬅ he will be...",
         body="Congratulations to We Stand 4 Something Inc. Owner Emmanuel Jenkins! Watch him on ➡WBOC Delmarva Life June 30th @ 5:00pm⬅ he will be talking about his Nonporfit and what is has to offer to our community, as well as the 3rd Annual Friday Feast for people with disabilities and their family's. DON'T FORGET TO TUNE IN!"),
]


def build_blog():
    els = [
        RAW(385, f'<a class="a" href="./" style="{pos(162, 385)}font:400 14px/19.6px {FONTS["enr"]};color:#00E689">All Posts</a>'),
    ]
    for i, post in enumerate(POSTS):
        y = 454 + i * 373
        if post.get("youtube"):
            media = (f'<span style="position:relative;display:block;width:454px;height:341px;flex:none">'
                     f'<img src="https://img.youtube.com/vi/{post["youtube"]}/hqdefault.jpg" alt="" width="454" height="341" style="width:100%;height:100%;object-fit:cover">'
                     f'<svg style="position:absolute;left:197px;top:140px;width:60px;height:60px" {SVG["play"][5:]}</span>')
        else:
            media = (f'<img src="{WIX}{post["image"]}/v1/fill/w_908,h_682,fp_0.50_0.50,lg_1,q_90/post.jpg" alt="" width="454" height="341" '
                     'style="width:454px;height:341px;object-fit:cover;flex:none">')
        excerpt = f'<p style="margin:12px 0 0;font:400 16px/24px {FONTS["enr"]};color:#292F33">{esc(post["excerpt"])}</p>' if post["excerpt"] else ""
        card = (f'<article class="a post-card" style="{pos(162, y, 940, 341)}">'
                f'<a href="../{post["slug"]}/" tabindex="-1" aria-hidden="true">{media}</a>'
                f'<div style="width:486px;background:#F0FAFF;padding:26px 36px;display:flex;flex-direction:column">'
                f'<div style="display:flex;gap:10px;align-items:center"><svg style="width:32px;height:32px" {SVG["avatar"][5:]}'
                f'<div class="post-meta">intern679<br>{post["date"]} &middot; {post["read"]}</div></div>'
                f'<h2 class="post-title" style="margin-top:14px"><a href="../{post["slug"]}/">{esc(post["title"])}</a></h2>{excerpt}</div></article>')
        els.append(RAW(y, card))
    bands = f'<div class="full deco" style="top:0;height:{1188 - HEADER_H}px;left:50%;right:auto;width:980px;margin-left:-490px;background:#F0FAFF"></div>'
    page("blog-1/", "Blog | ws4s", ch(1424), els, bands, main_bg="#000")

    for post in POSTS:
        if post.get("youtube"):
            media = (f'<div class="a m-full" style="{pos(222, 560, 820, 461)}"><iframe src="https://www.youtube-nocookie.com/embed/{post["youtube"]}" '
                     f'title="{esc(post["title"])}" width="820" height="461" style="width:100%;height:100%;border:0" allowfullscreen loading="lazy"></iframe></div>')
            h = 1300
        else:
            media = (f'<img class="a" src="{WIX}{post["image"]}/v1/fill/w_790,h_848,al_c,lg_1,q_80/post.jpg" alt="Emmanuel Jenkins" width="395" height="424" '
                     f'style="{pos(434, 560, 395, 424)}object-fit:cover">')
            h = 1450
        els = [
            RAW(400, f'<div class="a post-meta" style="{pos(222, 400, 820)}display:flex;gap:10px;align-items:center"><svg style="width:32px;height:32px" {SVG["avatar"][5:]}<span>intern679<br>{post["date"]} &middot; {post["read"]}</span></div>'),
            T(222, 460, 820, post["title"], "os", 32, 400, "#292F33", tag="h1", style="margin:0", cls="m-big"),
            RAW(560, media),
        ]
        if post["body"]:
            els.append(T(222, 1010, 820, post["body"], "enr", 18, 400, "#292F33", lh="1.6", cls="m-text"))
        els.append(RAW(h - 120, f'<a class="a" href="{{{{P}}}}blog-1/" style="{pos(222, h - 120)}font:400 14px {FONTS["enr"]};color:#00995B;text-decoration:underline">&larr; All Posts</a>'))
        bands = f'<div class="full deco" style="top:0;bottom:0;left:50%;right:auto;width:980px;margin-left:-490px;background:#F0FAFF"></div>'
        page(post["slug"] + "/", post["title"] + " | ws4s", h - HEADER_H, els, bands, main_bg="#000", desc=post["body"][:150] or None)


def bio_page(slug, title, total_h, els):
    page(slug, title, ch(total_h), els, main_bg="#CADDE6")


def build_bios():
    H = "#292F33"
    emm_bio = ("Emmanuel Jenkins, the dynamic driving force behind the transformative nonprofit We Stand 4 Something, is a beacon of support for individuals with disabilities and their families, spreading positivity and hope. In Delaware, he stands out as the Community Relations Officer for the Delaware Developmental Disabilities Council and serves influentially as the vice-chair of the Delaware Developmental Disabilities Services Advisory Committee. An alumnus of the Partners in Policymaking program since 2014, Emmanuel's unwavering dedication to advocacy is evident in his ongoing roles on the Advisory Committee for the Self-Advocacy Resource and Technical Assistance Center and as chair of the National Association of Councils on Developmental Disabilities (NACDD) Leaders with Lived Experiences (LLE) Committee. He also serves on the NACDD board. In 2024, Emmanuel was appointed by President Joe Biden to serve on the President’s Committee for People with Intellectual Disabilities (PCPID), further amplifying his national impact. As the founder of E Jenkins Solutions, LLC, Emmanuel leverages his expertise to provide a wide range of services, including leadership training and development, business development, quality assurance, plain language document creation, and policy and procedure development. Through his LLC, he works with organizations to ensure accessibility, clarity, and excellence in their operations. In academia, Emmanuel is a distinguished LEND Faculty Member at the University of Delaware. A devoted family man, married since 2009 and father to a 19-year-old, he exemplifies the transformative power of motivation. With over two decades as a motivational speaker, Emmanuel envisions a future in Congress where his tireless advocacy can reach new heights, embodying resilience, determination, and the belief in standing for something greater.")
    bio_page("emmanuel/", "About Emmanuel Jenkins", 1764, [
        T(172, 397, 600, "Emmanuel Jenkins- Founder &amp; Director", "os", 25, 700, "#004D2E", tag="h1", style="margin:0", raw=True),
        BOX(171, 438, 920, 1, "border-top:0.67px solid rgba(154,174,184,.8)"),
        I(188, 489, 327, 317, WIX + "f45d39_0f746333cff946bda5b82c822bd27a7e~mv2.jpeg/v1/fill/w_654,h_634,al_c,lg_1,q_85/Emmanuel%20Jenkins.jpeg", "Emmanuel Jenkins", radius="7px"),
        T(568, 490, 530, emm_bio, "helv", 18, 400, H, lh="23.4px", cls="m-text"),
        LINK(178, 1346, 100, "Back", "../about/", cls="pager"),
        LINK(981, 1346, 100, "Next", "../marissa/", cls="pager"),
    ])
    mar = [
        "Marissa Castello is an Administrative Assistant at Benton Lynn Law, P.A. Firm in Dover, DE.  She’s also the founder and CEO of ConfidenceNUrShine Outreach Ministry and founder and CEO of MCassociates, a virtual administrative assistant business.",
        "Marissa is a mother of three daughters and a grandmother of two grandsons. Marissa has been advocating for her daughter, and others, since the inception of her daughter's IEP in 3rd grade. Marissa became an advocate after experiencing firsthand how the school systems were handling her child’s learning disabilities and became passionate for speaking up for those who were unable to articulate for themselves. She lives by these core principles of life…” always stand on the truth”, “say what you mean and mean what you say”, “if you say you’re going to do something do it”, “everyone’s time is valuable, so be on time”, “most of all treat people how you want to be treated with dignity, respect and love”. Marissa is honored and excited, as this is a blessing to be able to serve on the board and be a part of WS4S. She looks forward to the bright future within the organization.",
    ]
    bio_page("marissa/", "Marissa | ws4s", 1090, [
        T(200, 373, 520, "Marissa Castello- Administrative Support/Secretary", "didot", 20, 700, "#000", "center", "26px", italic=True, tag="h1", style="margin:0"),
        I(190, 438, 200, 188, WIX + "b08a92_e0b91d78637244ef8ad543b47224477c~mv2.jpeg/v1/fill/w_400,h_376,al_c,q_80,usm_0.66_1.00_0.01/Marissa.jpeg", "Marissa Castello", radius="50%"),
        T(442, 434, 645, mar[0], "helv", 18, 400, "#515E65", "center", cls="m-text"),
        T(427, 530, 675, mar[1], "helv", 18, 400, "#515E65", "center", cls="m-text"),
        LINK(177, 820, 100, "Back", "../emmanuel/", cls="pager"),
        LINK(974, 820, 100, "Next", "../dielle/", cls="pager"),
    ])
    bio_page("dielle/", "Dielle | ws4s", 1060, [
        T(162, 385, 600, "Dielle De Noon- Member Website Manager", "os", 25, 400, H, lh="32.5px", tag="h1", style="margin:0"),
        I(182, 435, 214, 214, WIX + "f45d39_2e77752fec1347b1b50ddb302f678ce0~mv2.jpeg/v1/fill/w_428,h_428,al_c,q_80,usm_0.66_1.00_0.01/dielle.jpeg", "Dielle De Noon"),
        T(453, 437, 592, "Hello! My name is Dielle De Noon; I am currently attending Western Governors University (WGU) for my 2nd bachelors degree in Cybersecurity and Information Assurance, I have a strong passion for working with computers and have been for many years. It is fascinating how technology has evolved and is continuing to evolve. I have a passion for helping others resolve computing technical issues, from hardware to security. I am always eager to learn new things related to technologies and cybersecurity. Furthermore, I have a passion for working as a team and offering and accepting various ideas and suggestions on various topics and tasks. I am also the Chair for Delaware Developmental Disabilities Council.",
          "helv", 18, 400, H, lh="23.4px", ls="0.18px", cls="m-text"),
        LINK(186, 757, 100, "Back", "../marissa/", cls="pager"),
        LINK(953, 757, 100, "Next", "../se/", cls="pager"),
    ])
    bio_page("se/", "Selena | ws4s", 1201, [
        T(186, 383, 400, "Selena Butcher - Member", "os", 25, 400, H, lh="32.5px", tag="h1", style="margin:0"),
        I(214, 419, 190, 230, WIX + "f45d39_72d0328eadc24cb7bbab3ae79294a8ce~mv2.jpg/v1/crop/x_0,y_0,w_967,h_1165/fill/w_380,h_460,al_c,q_80,usm_0.66_1.00_0.01/selena.jpg", "Selena Butcher"),
        T(469, 464, 595, "Selina Butcher, a woman with cerebral palsy. Born and raised in Wilmington Delaware. Growing up, had its Challenges… Being the “different one“, but her advocacy journey started from these experiences, she had  to grow her alligator skin at a young age… Asserting her needs and opinions, so that she would not be rolled over in the world that was not made for her. Relying on a wheelchair to get her from point B she has carved out a simple life that she enjoys. Selina is a graduate of Temple university, with a BA in criminal justice. She was told that she was not going to survive the demand of school and being in the city! She proved all of her guidance counselors Wrong! She loves to travel and make good friends! Not shy, but reserved. She is a firm believer that your voice is your first tool to becoming a great advocate… Use it or lose it! she stands firm in her belief that persons with disabilities have a right to live and enjoy the pleasures of life as everyone else, and no need to be shy or bashful or afraid… it is time for persons with disabilities to come out of the shadows. We all deserve to live life on our own terms! Selina is an advocate for persons with disabilities, because she is a person with a disability herself! “Nothing about us, without Us“ Life is a journey, there will be bumps ahead, lace up your shoes and get ready, the journey begins and advocating will never end!",
          "helv", 18, 400, H, lh="23.4px", ls="0.18px", cls="m-text"),
        LINK(299, 918, 100, "Back", "../dielle/", cls="pager"),
        LINK(960, 918, 100, "Next", "../services/", cls="pager"),
    ])


def build_friday_feast():
    H = "#292F33"
    G = "#515E65"
    zeffy = "https://www.zeffy.com/en-US/donation-form/3036b57a-b266-4240-97ab-7b99843ce6d8"
    els = [
        T(200, 392, 864, "\U0001F983 The Friday Feast is Back! \U0001F983", "os", 50, 700, H, "center", "55px", tag="h1", style="margin:0", cls="m-big"),
        T(200, 479, 864, "Friday, November 21, 2025", "os", 50, 700, H, "center", "55px", tag="h2", style="margin:0", cls="m-big"),
        T(267, 605, 757, "We Stand 4 Something is proud to bring back The Friday Feast — a night of food, fun, and community!", "enr", 30, 400, G, "justify", "39px", cls="m-text"),
        T(267, 683, 757, "This free celebration is more than just a meal — it’s a space where everyone belongs. People with and without disabilities come together to share joy, connection, and holiday cheer. For many, this is the only holiday celebration where they feel truly welcomed. It’s a night where strangers become friends, families come together, and everyone has a seat at the table.",
          "enr", 30, 400, G, "justify", "39px", cls="m-text"),
        T(225, 1015, 841, "Click the button below if you would like to donate. Thank you for your donation!", "os", 40, 700, H, "center", "44px", cls="m-big"),
        RAW(1165, f'<a class="a" href="{zeffy}" target="_blank" rel="noopener" style="{pos(455, 1165, 354, 76)}display:flex;align-items:center;justify-content:center;gap:10px;background:#00995B;border-radius:50px;color:#F0FAFF;font:700 30px {FONTS["avenir"]};letter-spacing:7.5px">Donate<svg style="width:37px;height:37px;fill:#F0FAFF" {SVG["arrow"][5:]}</a>'),
    ]
    page("friday-feast/", "Friday Feast | ws4s", ch(2504), els, main_bg="#F0FAFF")


def build_404():
    els = [
        T(200, 420, 864, "Page not found", "os", 40, 700, "#292F33", "center", tag="h1", style="margin:0", cls="m-big"),
        RAW(500, f'<p class="a" style="{pos(200, 500, 864)}font:400 18px {FONTS["enr"]};color:#515E65;text-align:center">Sorry, we couldn’t find that page. <a href="./" style="text-decoration:underline;color:#00995B">Go to the home page</a>.</p>'),
    ]
    path = page("404/", "Page not found | ws4s", 400, els, main_bg="#F0FAFF")
    # GitHub Pages serves 404.html for any missing URL, at any depth. Links are made relative to a
    # <base> pointing at the site root (/<repo>/ on github.io project sites, / on a custom domain).
    with open(path, encoding="utf-8") as f:
        doc = f.read().replace('"../', '"')
    base = ("<script>(function(){var s=location.pathname.split('/')[1];"
            "var b=(/github\\.io$/.test(location.hostname)&&s)?'/'+s+'/':'/';"
            "document.write('<base href=\"'+b+'\">');})();</script>\n")
    doc = doc.replace("<head>\n", "<head>\n" + base, 1)
    os.remove(path)
    os.rmdir(os.path.dirname(path))
    with open(os.path.join(ROOT, "404.html"), "w", encoding="utf-8") as f:
        f.write(doc)


if __name__ == "__main__":
    build_home()
    build_resources()
    build_legislation()
    build_feedback()
    build_about()
    build_services()
    build_events()
    build_support()
    build_gallery()
    build_shop()
    build_blog()
    build_bios()
    build_friday_feast()
    build_404()
    print("Site built.")
