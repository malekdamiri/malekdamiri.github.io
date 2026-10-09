#!/usr/bin/env python3
"""Add Malek Damiri's HackerNoon stories to the site.

Reads the HackerNoon author feed and rewrites the marked lists on the home page and
/writing/, plus matching Article entries in the /writing/ JSON-LD. Writes nothing if
the feed can't be read or nothing changed. Standard library only.
"""
import html
import json
import re
import sys
import urllib.request
import xml.etree.ElementTree as ET
from datetime import date
from email.utils import parsedate_to_datetime
from pathlib import Path

FEED = "https://hackernoon.com/u/malekdamiri/feed"
AUTHOR = "Malek Damiri"
SITE = Path(__file__).resolve().parent.parent
PERSON = "https://malekdamiri.com/#person"
DC = "{http://purl.org/dc/elements/1.1/}creator"


def stories():
    req = urllib.request.Request(FEED, headers={"User-Agent": "Mozilla/5.0 (malekdamiri.com sync)"})
    with urllib.request.urlopen(req, timeout=30) as r:
        root = ET.fromstring(r.read())
    found = []
    for item in root.iter("item"):
        if (item.findtext(DC) or "").strip() != AUTHOR:
            continue
        url = (item.findtext("link") or "").split("?")[0].strip()
        title = (item.findtext("title") or "").strip()
        if url.startswith("https://hackernoon.com/") and title:
            found.append({"url": url, "title": title,
                          "date": parsedate_to_datetime(item.findtext("pubDate")).date().isoformat()})
    return sorted(found, key=lambda s: s["date"], reverse=True)


def fill(text, marker, items):
    rows = "".join(f'<li><a class="label" href="{html.escape(s["url"])}" rel="noopener">{html.escape(s["title"], quote=False)}</a></li>\n'
                   for s in items)
    pattern = re.compile(rf"(<!-- {marker}:start -->\n).*?(<!-- {marker}:end -->)", re.S)
    if not pattern.search(text):
        sys.exit(f"marker {marker} not found")
    return pattern.sub(lambda m: m[1] + rows + m[2], text)


def with_articles(text, items):
    m = re.search(r'(<script type="application/ld\+json">)(.*?)(</script>)', text, re.S)
    data = json.loads(m[2])
    graph = [n for n in data["@graph"]
             if not (n.get("@type") == "Article" and n.get("url", "").startswith("https://hackernoon.com/"))]
    graph += [{"@type": "Article", "@id": s["url"] + "#article", "url": s["url"], "headline": s["title"],
               "datePublished": s["date"], "author": {"@id": PERSON},
               "publisher": {"@type": "Organization", "name": "HackerNoon", "url": "https://hackernoon.com/"}}
              for s in items]
    data["@graph"] = graph
    blob = json.dumps(data, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
    return text[:m.start(2)] + blob + text[m.end(2):]


def main():
    try:
        items = stories()
    except Exception as e:  # network trouble or a changed feed: leave the site alone
        print(f"feed not read: {e}")
        return
    pages = {SITE / "index.html": lambda t: fill(t, "hackernoon-latest", items[:3]),
             SITE / "writing" / "index.html": lambda t: with_articles(fill(t, "hackernoon", items), items)}
    changed = []
    for path, update in pages.items():
        old = path.read_text()
        new = update(old)
        if new != old:
            path.write_text(new)
            changed.append(path)
    if changed:
        sitemap = SITE / "sitemap.xml"
        today = date.today().isoformat()
        text = sitemap.read_text()
        for loc in ("https://malekdamiri.com/", "https://malekdamiri.com/writing/"):
            text = re.sub(rf"(<loc>{re.escape(loc)}</loc>\s*<lastmod>)[^<]*", rf"\g<1>{today}", text)
        sitemap.write_text(text)
    print(f"{len(items)} stories in the feed; updated: {', '.join(p.relative_to(SITE).as_posix() for p in changed) or 'nothing'}")


if __name__ == "__main__":
    main()
