#!/usr/bin/env python3
"""
Adds GA4 tracking tag and fixes footer nav (adds Blog link) across all pages.
Run from anywhere: python3 add_ga4.py
"""

import os
import re

BASE = os.path.expanduser("~/Desktop/ClaudeWork/Rich")
GA4_ID = "G-6RDDSKTZ46"

GA4_SNIPPET = f"""<!-- Google Analytics -->
<script async src="https://www.googletagmanager.com/gtag/js?id={GA4_ID}"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){{dataLayer.push(arguments);}}
  gtag('js', new Date());
  gtag('config', '{GA4_ID}');
</script>"""

# All HTML files to update
ROOT_FILES = [
    "index.html",
    "seo-web.html",
    "ai-consulting.html",
    "custom-tools.html",
    "privacy.html",
    "terms.html",
]
BLOG_FILES = [
    "blog/index.html",
    "blog/what-does-seo-consultant-do.html",
]

ALL_FILES = ROOT_FILES + BLOG_FILES

# Footer nav fix — add Blog link to root pages
OLD_FOOTER_NAV = '<a href="custom-tools.html">Custom Tools</a>\n        <a href="#contact">Contact</a>'
NEW_FOOTER_NAV = '<a href="custom-tools.html">Custom Tools</a>\n        <a href="blog/">Blog</a>\n        <a href="#contact">Contact</a>'

# Footer nav fix for blog subpages
OLD_FOOTER_NAV_BLOG = '<a href="../custom-tools.html">Custom Tools</a>\n        <a href="#contact">Contact</a>'
NEW_FOOTER_NAV_BLOG = '<a href="../custom-tools.html">Custom Tools</a>\n        <a href="../blog/">Blog</a>\n        <a href="#contact">Contact</a>'

ga4_added = 0
ga4_skipped = 0
footer_fixed = 0

for filepath in ALL_FILES:
    full_path = os.path.join(BASE, filepath)

    if not os.path.exists(full_path):
        print(f"  SKIP  {filepath} — file not found")
        ga4_skipped += 1
        continue

    content = open(full_path, encoding="utf-8").read()
    original = content

    # Add GA4 if not already present
    if GA4_ID in content:
        print(f"  SKIP  {filepath} — GA4 already present")
        ga4_skipped += 1
    else:
        content = content.replace("</head>", f"{GA4_SNIPPET}\n</head>")
        ga4_added += 1

    # Fix footer nav
    if filepath in BLOG_FILES:
        if '<a href="../blog/">Blog</a>' not in content:
            content = content.replace(OLD_FOOTER_NAV_BLOG, NEW_FOOTER_NAV_BLOG)
            if content != original:
                footer_fixed += 1
    else:
        if '<a href="blog/">Blog</a>' not in content:
            content = content.replace(OLD_FOOTER_NAV, NEW_FOOTER_NAV)
            if content != original:
                footer_fixed += 1

    if content != original:
        open(full_path, "w", encoding="utf-8").write(content)
        print(f"  OK    {filepath}")

print(f"\n  GA4 added to {ga4_added} files, {ga4_skipped} skipped")
print(f"  Footer nav updated on {footer_fixed} files")
print("\nDone. Deploy next:")
print(f"  python3 ~/Desktop/ClaudeWork/Rich/deploy.py \"add GA4 tracking and fix footer nav\"")
