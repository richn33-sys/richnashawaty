#!/usr/bin/env python3
"""
Fixes CLS by adding font-display=swap and preconnect hints to Google Fonts
across all pages.
Run: python3 ~/Desktop/ClaudeWork/Rich/fix_cls.py
"""

import os

BASE = os.path.expanduser("~/Desktop/ClaudeWork/Rich")

ALL_FILES = [
    "index.html",
    "seo-web.html",
    "ai-consulting.html",
    "custom-tools.html",
    "privacy.html",
    "terms.html",
    "about.html",
    "blog/index.html",
    "blog/what-does-seo-consultant-do.html",
    "blog/how-much-does-seo-consultant-cost-boston.html",
]

OLD_FONTS = '<link href="https://fonts.googleapis.com/css2?family=Instrument+Serif:ital@0;1&family=DM+Sans:opsz,wght@9..40,300;9..40,400;9..40,500;9..40,600&family=DM+Mono:wght@400;500&display=swap" rel="stylesheet">'

NEW_FONTS = """<link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Instrument+Serif:ital@0;1&family=DM+Sans:opsz,wght@9..40,300;9..40,400;9..40,500;9..40,600&family=DM+Mono:wght@400;500&display=swap" rel="stylesheet" media="print" onload="this.media='all'">
  <noscript><link href="https://fonts.googleapis.com/css2?family=Instrument+Serif:ital@0;1&family=DM+Sans:opsz,wght@9..40,300;9..40,400;9..40,500;9..40,600&family=DM+Mono:wght@400;500&display=swap" rel="stylesheet"></noscript>"""

updated = 0
skipped = 0

for fname in ALL_FILES:
    path = os.path.join(BASE, fname)
    if not os.path.exists(path):
        print(f"  SKIP  {fname} — not found"); skipped += 1; continue
    content = open(path, encoding="utf-8").read()
    if 'media="print"' in content:
        print(f"  SKIP  {fname} — already fixed"); skipped += 1; continue
    if OLD_FONTS not in content:
        print(f"  WARN  {fname} — font link not found"); skipped += 1; continue
    content = content.replace(OLD_FONTS, NEW_FONTS)
    open(path, "w", encoding="utf-8").write(content)
    print(f"  OK    {fname}"); updated += 1

print(f"\n  {updated} files updated, {skipped} skipped")
print("\nDone. Deploy next:")
print('  python3 ~/Desktop/ClaudeWork/Rich/deploy.py "fix CLS with async font loading"')
