#!/usr/bin/env python3
"""
Adds About link to nav across all pages.
Run: python3 ~/Desktop/ClaudeWork/Rich/add_about_nav.py
"""

import os

BASE = os.path.expanduser("~/Desktop/ClaudeWork/Rich")

# Root pages — flat paths
ROOT_FILES = ["index.html", "seo-web.html", "ai-consulting.html", "custom-tools.html", "privacy.html", "terms.html"]
OLD_ROOT = '<li><a href="blog/">Blog</a></li>'
NEW_ROOT = '<li><a href="blog/">Blog</a></li>\n    <li><a href="about.html">About</a></li>'

# Blog subpages — ../ prefix
BLOG_FILES = ["blog/index.html", "blog/what-does-seo-consultant-do.html", "blog/how-much-does-seo-consultant-cost-boston.html"]
OLD_BLOG = '<li><a href="../blog/">Blog</a></li>'
NEW_BLOG = '<li><a href="../blog/">Blog</a></li>\n    <li><a href="../about.html">About</a></li>'

updated = 0
skipped = 0

for fname in ROOT_FILES:
    path = os.path.join(BASE, fname)
    if not os.path.exists(path):
        print(f"  SKIP  {fname} — not found"); skipped += 1; continue
    content = open(path, encoding="utf-8").read()
    if 'href="about.html"' in content:
        print(f"  SKIP  {fname} — already has About link"); skipped += 1; continue
    new_content = content.replace(OLD_ROOT, NEW_ROOT)
    if new_content == content:
        print(f"  WARN  {fname} — nav pattern not found"); skipped += 1; continue
    open(path, "w", encoding="utf-8").write(new_content)
    print(f"  OK    {fname}"); updated += 1

for fname in BLOG_FILES:
    path = os.path.join(BASE, fname)
    if not os.path.exists(path):
        print(f"  SKIP  {fname} — not found"); skipped += 1; continue
    content = open(path, encoding="utf-8").read()
    if 'href="../about.html"' in content:
        print(f"  SKIP  {fname} — already has About link"); skipped += 1; continue
    new_content = content.replace(OLD_BLOG, NEW_BLOG)
    if new_content == content:
        print(f"  WARN  {fname} — nav pattern not found"); skipped += 1; continue
    open(path, "w", encoding="utf-8").write(new_content)
    print(f"  OK    {fname}"); updated += 1

print(f"\n  {updated} files updated, {skipped} skipped")
print("\nDone. Deploy next:")
print('  python3 ~/Desktop/ClaudeWork/Rich/deploy.py "add About to nav across all pages"')
