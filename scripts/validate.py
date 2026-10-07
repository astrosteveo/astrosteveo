#!/usr/bin/env python3
"""Validate the rendered portfolio's assets, navigation and publication boundary."""
import json
import re
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
data = json.loads((ROOT / "content/portfolio.json").read_text())


class Page(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids = []
        self.links = []
        self.assets = []
        self.h1 = 0

    def handle_starttag(self, tag, attributes):
        attrs = dict(attributes)
        if "id" in attrs:
            self.ids.append(attrs["id"])
        if tag == "a":
            self.links.append(attrs.get("href", ""))
        if tag == "link" and attrs.get("rel") in ("icon", "stylesheet"):
            self.assets.append(attrs["href"])
        self.h1 += tag == "h1"


page = Page()
source = (ROOT / "site/index.html").read_text()
page.feed(source)
assert page.h1 == 1, "The portfolio must have one primary heading"
assert len(page.ids) == len(set(page.ids)), "Duplicate HTML anchors"
for link in page.links:
    assert link, "Empty link"
    if link.startswith("#"):
        assert link[1:] in page.ids, f"Missing anchor: {link}"
    else:
        assert urlsplit(link).scheme in ("https", "mailto"), f"Unexpected link: {link}"
for asset in page.assets:
    assert (ROOT / "site" / asset).is_file(), f"Missing asset: {asset}"
assert f'mailto:{data["email"]}' in page.links, "Missing professional contact"
assert set(p["id"] for p in data["projects"]) <= set(page.ids)
assert len(data["projects"]) == 4
# Private work must never receive a source or deployment link here.
private = next(p for p in data["projects"] if p["id"] == "void-sector")
assert private["public_repo"] is None, "Void Sector must remain private"
assert not any("void-sector" in link for link in page.links)
for file in (ROOT / "README.md", ROOT / "site/index.html"):
    content = file.read_text()
    assert not re.search(r"/home/|ngc\.com|(?:ghp_|gho_|github_pat_)[A-Za-z0-9_]+", content), f"Non-public content in {file.name}"
    assert not re.search(r"https://[^\s\"<>)]*void-sector", content), "Private project link"
for asset in (ROOT / "assets").glob("*.svg"):
    ET.parse(asset)
ET.parse(ROOT / "site/favicon.svg")
ET.parse(ROOT / "site/sitemap.xml")
assert (ROOT / "site/social.png").read_bytes()[:8] == b"\x89PNG\r\n\x1a\n"
print("Validated project cards, anchors, contact link, local assets, XML, social image, and private-project link boundary.")
