#!/usr/bin/env python3
"""
Fixes duplicate content issue:
1. Adds canonical tags to all pages
2. Creates .htaccess to 301 redirect /index.html to /
3. Checks internal links for index.html references

Run: python3 ~/Desktop/ClaudeWork/Rich/fix_canonicals.py
"""

import os
import re

BASE = os.path.expanduser("~/Desktop/ClaudeWork/Rich")

# Canonical URLs for each page
CANONICALS = {
    "index.html":           "https://richnashawaty.com/",
    "seo-web.html":         "https://richnashawaty.com/seo-web.html",
    "ai-consulting.html":   "https://richnashawaty.com/ai-consulting.html",
    "custom-tools.html":    "https://richnashawaty.com/custom-tools.html",
    "about.html":           "https://richnashawaty.com/about.html",
    "privacy.html":         "https://richnashawaty.com/privacy.html",
    "terms.html":           "https://richnashawaty.com/terms.html",
    "blog/index.html":      "https://richnashawaty.com/blog/",
    "blog/what-does-seo-consultant-do.html":                        "https://richnashawaty.com/blog/what-does-seo-consultant-do.html",
    "blog/how-much-does-seo-consultant-cost-boston.html":           "https://richnashawaty.com/blog/how-much-does-seo-consultant-cost-boston.html",
    "blog/why-isnt-my-boston-business-ranking-on-google.html":      "https://richnashawaty.com/blog/why-isnt-my-boston-business-ranking-on-google.html",
    "blog/google-may-2026-algorithm-update-boston-small-business.html": "https://richnashawaty.com/blog/google-may-2026-algorithm-update-boston-small-business.html",
    "blog/what-is-geo-generative-engine-optimization-boston.html":  "https://richnashawaty.com/blog/what-is-geo-generative-engine-optimization-boston.html",
}

updated = 0
skipped = 0

# 1. Add canonical tags to all pages
for fname, canonical_url in CANONICALS.items():
    path = os.path.join(BASE, fname)
    if not os.path.exists(path):
        print(f"  SKIP  {fname} — not found"); skipped += 1; continue

    content = open(path, encoding="utf-8").read()

    if 'rel="canonical"' in content:
        print(f"  SKIP  {fname} — canonical already present"); skipped += 1; continue

    canonical_tag = f'  <link rel="canonical" href="{canonical_url}">'
    content = content.replace("</head>", canonical_tag + "\n</head>", 1)
    open(path, "w", encoding="utf-8").write(content)
    print(f"  OK    {fname}"); updated += 1

print(f"\n  Canonical tags: {updated} added, {skipped} skipped")

# 2. Create .htaccess with 301 redirect
htaccess_path = os.path.join(BASE, ".htaccess")
htaccess_content = """# Redirect index.html to canonical root
RedirectMatch 301 ^/index\\.html$ https://richnashawaty.com/

# Redirect blog/index.html to canonical blog URL
RedirectMatch 301 ^/blog/index\\.html$ https://richnashawaty.com/blog/

# Force HTTPS
RewriteEngine On
RewriteCond %{HTTPS} off
RewriteRule ^(.*)$ https://%{HTTP_HOST}%{REQUEST_URI} [L,R=301]
"""

if os.path.exists(htaccess_path):
    existing = open(htaccess_path).read()
    if "index.html" in existing:
        print("\n  SKIP  .htaccess — redirect already present")
    else:
        open(htaccess_path, "a").write("\n" + htaccess_content)
        print("\n  OK    .htaccess — redirect appended")
else:
    open(htaccess_path, "w").write(htaccess_content)
    print("\n  OK    .htaccess — created")

# 3. Check internal links for index.html references
print("\n  Checking internal links for index.html references...")
all_files = list(CANONICALS.keys())
for fname in all_files:
    path = os.path.join(BASE, fname)
    if not os.path.exists(path): continue
    content = open(path).read()
    # Find href="index.html" or href="../index.html" — these are fine for nav
    # But flag href="https://richnashawaty.com/index.html" in schema
    if 'richnashawaty.com/index.html' in content:
        print(f"  WARN  {fname} — contains absolute index.html link in schema/OG tags")

print("\nDone. Deploy next:")
print('  python3 ~/Desktop/ClaudeWork/Rich/deploy.py "add canonical tags and fix index.html duplicate"')
