#!/usr/bin/env python3
"""
Update title tags across all richnashawaty.com pages.
Run from anywhere: python3 update_titles.py
"""

import os
import re

BASE = os.path.expanduser("~/Desktop/ClaudeWork/Rich")

TITLES = {
    "index.html": "SEO Consultant Boston — 20 Years Experience, Small Business Focus",
    "seo-web.html": "Boston SEO & Web Design — Technical SEO That Moves Rankings",
    "ai-consulting.html": "AI Consulting for Small Businesses — Automate & Scale in 2026",
    "custom-tools.html": "Custom AI Tools & Automation — Built for Boston Small Businesses",
    "privacy.html": "Privacy Policy — richnashawaty.com",
    "terms.html": "Terms of Service — richnashawaty.com",
    "blog/index.html": "SEO, AI & Automation Insights for Boston Small Business Owners",
    "blog/what-does-seo-consultant-do.html": "What Does an SEO Consultant Actually Do? (And Is It Worth It?)",
}

updated = 0
skipped = 0

for filepath, new_title in TITLES.items():
    full_path = os.path.join(BASE, filepath)

    if not os.path.exists(full_path):
        print(f"  SKIP  {filepath} — file not found")
        skipped += 1
        continue

    content = open(full_path, encoding="utf-8").read()
    new_content = re.sub(r"<title>.*?</title>", f"<title>{new_title}</title>", content, flags=re.DOTALL)

    if new_content == content:
        print(f"  SKIP  {filepath} — no <title> tag found")
        skipped += 1
        continue

    open(full_path, "w", encoding="utf-8").write(new_content)
    print(f"  OK    {filepath}")
    updated += 1

print(f"\n  {updated} updated, {skipped} skipped")
print("\nDone. Run deploy.py next:\n  python3 ~/Desktop/ClaudeWork/Rich/deploy.py \"update title tags for SEO\"")
