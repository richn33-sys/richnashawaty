#!/usr/bin/env python3
"""
Adds "Last updated" byline to service pages and homepage.
Run: python3 ~/Desktop/ClaudeWork/Rich/add_bylines.py
"""

import os

BASE = os.path.expanduser("~/Desktop/ClaudeWork/Rich")

BYLINE = '<p style="font-family:var(--mono);font-size:0.72rem;color:var(--text3);margin-bottom:2rem;letter-spacing:0.04em;">Last updated: May 2026</p>'

# Each file + the unique string that appears just before where we inject
PAGES = [
    ("index.html",          '<h1>SEO & AI Automation'),
    ("seo-web.html",        '<h1>'),
    ("ai-consulting.html",  '<h1>'),
    ("custom-tools.html",   '<h1>'),
]

updated = 0
skipped = 0

for fname, marker in PAGES:
    path = os.path.join(BASE, fname)
    if not os.path.exists(path):
        print(f"  SKIP  {fname} — not found"); skipped += 1; continue
    content = open(path, encoding="utf-8").read()
    if "Last updated:" in content:
        print(f"  SKIP  {fname} — byline already present"); skipped += 1; continue

    # Find the h1 and inject byline after its closing tag
    import re
    # Match the first <h1...>...</h1> block
    pattern = r'(<h1[^>]*>.*?</h1>)'
    match = re.search(pattern, content, re.DOTALL)
    if not match:
        print(f"  WARN  {fname} — no h1 found"); skipped += 1; continue

    h1_block = match.group(1)
    content = content.replace(h1_block, h1_block + "\n        " + BYLINE, 1)
    open(path, "w", encoding="utf-8").write(content)
    print(f"  OK    {fname}"); updated += 1

print(f"\n  {updated} files updated, {skipped} skipped")
print("\nDone. Deploy next:")
print('  python3 ~/Desktop/ClaudeWork/Rich/deploy.py "add last updated bylines to service pages"')
