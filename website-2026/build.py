#!/usr/bin/env python3
"""
Kulé kulé Zanskar — static site generator.

Run:  python3 build.py          (writes the site next to this file)

Every page is defined in content_*.py as a Page object. This file owns the
shared layout: head, header, footer, breadcrumbs, JSON-LD and the sitemap.
"""

import os, re, shutil, html, json, datetime

HERE = os.path.dirname(os.path.abspath(__file__))
OUT  = HERE

SITE = "https://www.kulekulezanskar.com"
BRAND = "Kulé kulé Zanskar"
EMAIL = "hello@kulekulezanskar.com"
WHATSAPP = "919469588242"          # primary number, digits only
WHATSAPP_DISPLAY = "+91 94695 88242"

TODOS = []

# --------------------------------------------------------------------------
# page model
# --------------------------------------------------------------------------

class Page:
    def __init__(self, path, title, description, body,
                 crumbs=None, hero=None, section=None, schema=None,
                 og_image="/assets/images/itinerary/day-1.jpg"):
        self.path = path                 # "" for home, "zanskar/best-time-to-visit" otherwise
        self.title = title               # <title>
        self.description = description
        self.body = body
        self.crumbs = crumbs or []       # [(label, url), ...] excluding Home and self
        self.hero = hero                 # dict or None
        self.section = section           # top-level nav key for aria-current
        self.schema = schema or []
        self.og_image = og_image

    @property
    def url(self):
        return "/" if self.path == "" else "/%s/" % self.path


# --------------------------------------------------------------------------
# navigation
# --------------------------------------------------------------------------

NAV = [
    ("zanskar",  "Zanskar",   "/zanskar/"),
    ("guides",   "Guides",    "/guides/"),
    ("journeys", "Journeys",  "/journeys/"),
    ("stories",  "Stories",   "/stories/"),
    ("about",    "About",     "/about/"),
    ("plan",     "Plan",      "/plan/"),
]

FOOTER = [
    ("Zanskar", [
        ("The region and its valleys", "/zanskar/the-region/"),
        ("Villages and monasteries", "/zanskar/villages-and-monasteries/"),
        ("Culture and traditions", "/zanskar/culture-and-traditions/"),
        ("Best time to visit", "/zanskar/best-time-to-visit/"),
        ("Getting to Zanskar", "/zanskar/how-to-get-there/"),
    ]),
    ("Journeys", [
        ("Zangla to Phuktal", "/journeys/zangla-to-phuktal-trek/"),
        ("Phuktal to Tsokmichik", "/journeys/phuktal-to-tsokmichik-trek/"),
        ("Cultural journey", "/journeys/zanskar-cultural-journey/"),
        ("Tailor-made", "/journeys/tailor-made/"),
        ("All journeys", "/journeys/"),
    ]),
    ("Plan your trip", [
        ("Fitness and difficulty", "/plan/fitness-and-difficulty/"),
        ("Altitude and acclimatisation", "/plan/altitude-and-acclimatisation/"),
        ("Packing list", "/plan/packing-list/"),
        ("Safety in remote areas", "/plan/safety-in-remote-areas/"),
        ("Booking and payment", "/plan/booking-and-payment/"),
        ("Questions and answers", "/plan/faq/"),
    ]),
    ("Kulé kulé Zanskar", [
        ("About us", "/about/"),
        ("Our guides", "/guides/"),
        ("Responsible travel", "/about/responsible-travel/"),
        ("Contact", "/contact/"),
        ("Privacy", "/privacy/"),
        ("Terms and conditions", "/terms/"),
    ]),
]


# --------------------------------------------------------------------------
# helpers used by the content modules
# --------------------------------------------------------------------------

def todo(text):
    """Mark information that still has to come from the guides."""
    TODOS.append(text)
    return ('<mark class="todo" title="Still to be supplied">%s</mark>'
            % html.escape(text))


def wa_link(message="Hello! I have a question about a journey in Zanskar."):
    from urllib.parse import quote
    return "https://wa.me/%s?text=%s" % (WHATSAPP, quote(message))


def img(src, alt, cls="", lazy=True, sizes="(max-width: 900px) 100vw, 800px"):
    """<img> with a 900w / 1800w srcset when the small variant exists on disk."""
    a = (' loading="lazy" decoding="async"' if lazy
         else ' fetchpriority="high" decoding="async"')
    c = ' class="%s"' % cls if cls else ""
    small = src[:-4] + "-900w.jpg" if src.endswith(".jpg") else None
    extra = ""
    if small and os.path.exists(os.path.join(OUT, small.lstrip("/"))):
        extra = ' srcset="%s 900w, %s 1800w" sizes="%s"' % (small, src, sizes)
    return '<img src="%s" alt="%s"%s%s%s>' % (src, html.escape(alt), c, a, extra)


# --------------------------------------------------------------------------
# layout
# --------------------------------------------------------------------------

HEAD = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{description}">
<link rel="canonical" href="{canonical}">
<meta name="theme-color" content="#1E5245">
<meta property="og:type" content="website">
<meta property="og:site_name" content="{brand}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{description}">
<meta property="og:url" content="{canonical}">
<meta property="og:image" content="{ogimage}">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="/assets/images/favicon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Familjen+Grotesk:wght@400;500;600;700&family=Source+Serif+4:opsz,wght@8..60,400;8..60,600&display=swap">
<link rel="stylesheet" href="/assets/site.css">
{schema}
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
"""

HEADER = """<header class="site-header">
  <div class="wrap">
    <div class="site-header__inner">
      <a class="brand" href="/">Kulé kulé<span>Zanskar</span></a>
      <button class="nav-toggle" type="button" aria-expanded="false" aria-controls="menu">Menu</button>
      <nav class="nav" id="menu" aria-label="Main">
        <ul>
{items}
          <li><a class="btn btn--primary" href="/contact/" style="color:#fff;padding:9px 16px">Plan your trip</a></li>
        </ul>
      </nav>
    </div>
  </div>
</header>
"""

FOOTER_HTML = """<footer class="site-footer">
  <div class="wrap">
    <div class="footer-grid">
{cols}
    </div>
    <div class="colophon">
      <p>&copy; {year} {brand}. Guided journeys in the Zanskar Valley, Ladakh, India.
         Operated by <strong>Ladakh Mountain Tour &amp; Travel</strong>. {legal}</p>
      <p>Photography &amp; route data &copy; Bram Schoonjans.</p>
    </div>
  </div>
</footer>
<script src="/assets/site.js" defer></script>
</body>
</html>
"""


def render(page):
    # --- head -------------------------------------------------------------
    schema_blocks = ""
    for s in page.schema:
        schema_blocks += ('<script type="application/ld+json">%s</script>\n'
                          % json.dumps(s, ensure_ascii=False, indent=None))

    head = HEAD.format(
        title=html.escape(page.title),
        description=html.escape(page.description),
        canonical=SITE + page.url,
        ogimage=SITE + page.og_image,
        brand=BRAND,
        schema=schema_blocks.rstrip(),
    )

    # --- header -----------------------------------------------------------
    items = ""
    for key, label, url in NAV:
        cur = ' aria-current="true"' if key == page.section else ""
        items += '          <li><a href="%s"%s>%s</a></li>\n' % (url, cur, label)
    header = HEADER.format(items=items.rstrip("\n"))

    # --- hero or page head ------------------------------------------------
    top = ""
    crumbs = ""
    if page.crumbs:
        lis = '<li><a href="/">Home</a></li>'
        for label, url in page.crumbs[:-1]:
            lis += '<li><a href="%s">%s</a></li>' % (url, html.escape(label))
        lis += '<li>%s</li>' % html.escape(page.crumbs[-1][0])
        crumbs = '<ol class="crumbs">%s</ol>' % lis

    if page.hero:
        h = page.hero
        cls = "hero " + h.get("class", "hero--page")
        buttons = h.get("buttons", "")
        eyebrow = ('<p class="label hero__eyebrow">%s</p>' % h["eyebrow"]) if h.get("eyebrow") else ""
        top = (
            '<div class="%s">\n'
            '  <div class="hero__media">%s</div>\n'
            '  <div class="wrap"><div class="hero__body">%s<h1>%s</h1><p>%s</p>%s</div></div>\n'
            '</div>\n' % (
                cls,
                img(h["image"], h["alt"], lazy=False, sizes="100vw"),
                eyebrow, h["h1"], h["intro"],
                ('<div class="btn-row">%s</div>' % buttons) if buttons else "",
            )
        )
        if crumbs:
            top += '<div class="wrap">%s</div>\n' % crumbs
    else:
        top = ('<div class="pagehead"><div class="wrap">%s<h1>%s</h1>%s</div></div>\n'
               % (crumbs,
                  page.h1 if hasattr(page, "h1") else html.escape(page.title.split(" | ")[0]),
                  ('<p class="lede">%s</p>' % page.lede) if getattr(page, "lede", None) else ""))

    # --- footer -----------------------------------------------------------
    cols = ""
    for heading, links in FOOTER:
        cols += '      <div>\n        <h4>%s</h4>\n        <ul>\n' % html.escape(heading)
        for label, url in links:
            cols += '          <li><a href="%s">%s</a></li>\n' % (url, html.escape(label))
        cols += '        </ul>\n      </div>\n'
    footer = FOOTER_HTML.format(
        cols=cols.rstrip("\n"),
        year=datetime.date.today().year,
        brand=BRAND,
        legal=todo("Company registration number, registered address and the name of the "
                   "contracting entity go here."),
    )

    return head + header + top + '<main id="main">\n' + page.body + '\n</main>\n' + footer


# --------------------------------------------------------------------------
# writing
# --------------------------------------------------------------------------

def write(page):
    rel = "index.html" if page.path == "" else os.path.join(page.path, "index.html")
    dest = os.path.join(OUT, rel)
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    with open(dest, "w", encoding="utf-8") as f:
        f.write(render(page))
    return rel


def build():
    import content_home, content_zanskar, content_guides, content_journeys, content_plan, content_misc

    pages = []
    for mod in (content_home, content_zanskar, content_guides,
                content_journeys, content_plan, content_misc):
        pages.extend(mod.pages())

    written = [write(p) for p in pages]

    # sitemap ---------------------------------------------------------------
    today = datetime.date.today().isoformat()
    urls = "".join(
        "  <url><loc>%s%s</loc><lastmod>%s</lastmod></url>\n" % (SITE, p.url, today)
        for p in pages if p.path not in ("privacy", "terms")
    )
    with open(os.path.join(OUT, "sitemap.xml"), "w", encoding="utf-8") as f:
        f.write('<?xml version="1.0" encoding="UTF-8"?>\n'
                '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
                + urls + '</urlset>\n')

    with open(os.path.join(OUT, "robots.txt"), "w", encoding="utf-8") as f:
        f.write("User-agent: *\nAllow: /\n\nSitemap: %s/sitemap.xml\n" % SITE)

    # 404 -------------------------------------------------------------------
    nf = Page("404", "Page not found | " + BRAND,
              "This page does not exist. Find your way back to the journeys or the region guide.",
              '<div class="section"><div class="wrap wrap--narrow prose">'
              '<h2>That page is not here</h2>'
              '<p>The link may be old, or we may have moved something. These are good places to start again:</p>'
              '<ul><li><a href="/zanskar/">Discover Zanskar</a></li>'
              '<li><a href="/journeys/">All journeys</a></li>'
              '<li><a href="/guides/">The guides</a></li>'
              '<li><a href="/contact/">Contact us</a></li></ul></div></div>')
    nf.h1 = "Page not found"
    with open(os.path.join(OUT, "404.html"), "w", encoding="utf-8") as f:
        f.write(render(nf))

    # report ----------------------------------------------------------------
    seen, uniq = set(), []
    for t in TODOS:
        if t not in seen:
            seen.add(t); uniq.append(t)
    with open(os.path.join(OUT, "OPENSTAANDE-PUNTEN.md"), "w", encoding="utf-8") as f:
        f.write("# Openstaande punten\n\n"
                "Automatisch verzameld bij het bouwen van de site op %s.\n"
                "Elk punt staat op de site geel gemarkeerd. Zolang deze lijst niet leeg is, "
                "is de site niet klaar om te publiceren.\n\n" % today)
        for i, t in enumerate(uniq, 1):
            f.write("%d. %s\n" % (i, t))

    print("pages : %d" % (len(written) + 1))
    print("todos : %d" % len(uniq))
    return pages


if __name__ == "__main__":
    # Re-enter through the module object so that content modules doing
    # `from build import ...` share one TODOS list with us.
    import build as _self
    _self.build()
