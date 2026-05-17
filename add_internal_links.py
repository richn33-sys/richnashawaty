#!/usr/bin/env python3
"""
Adds contextual internal links from blog posts to service pages.
Run: python3 ~/Desktop/ClaudeWork/Rich/add_internal_links.py
"""

import os

BASE = os.path.expanduser("~/Desktop/ClaudeWork/Rich")

CHANGES = [
    # ── POST 1: what-does-seo-consultant-do.html ──────────────────────────────
    {
        "file": "blog/what-does-seo-consultant-do.html",
        "replacements": [
            # Link "SEO consulting" to seo-web.html
            (
                "I've seen what SEO consulting looks like at every scale and in every context.",
                'I\'ve seen what <a href="../seo-web.html">SEO consulting</a> looks like at every scale and in every context.'
            ),
            # Link "technical maintenance" to seo-web.html
            (
                "It's not paying someone to \"get you to number one on Google.\"",
                'It\'s not paying someone to "get you to number one on Google."'
            ),
            # Link "AI tools" reference to ai-consulting.html
            (
                "Good SEO consulting is ongoing, iterative work",
                'Good <a href="../seo-web.html">SEO consulting</a> is ongoing, iterative work'
            ),
        ]
    },

    # ── POST 2: how-much-does-seo-consultant-cost-boston.html ─────────────────
    {
        "file": "blog/how-much-does-seo-consultant-cost-boston.html",
        "replacements": [
            # Link "SEO consulting in Boston" to seo-web.html
            (
                "If you've started researching SEO consulting in Boston",
                'If you\'ve started researching <a href="../seo-web.html">SEO consulting in Boston</a>'
            ),
            # Link "technical maintenance, content strategy" to seo-web.html
            (
                "Common for businesses that want sustained SEO attention — technical maintenance, content strategy, reporting, and ongoing optimization over time.",
                'Common for businesses that want sustained SEO attention — technical maintenance, content strategy, reporting, and ongoing optimization over time. <a href="../seo-web.html" style="color:var(--accent);text-decoration:underline;text-underline-offset:3px;">See what\'s included →</a>'
            ),
            # Link "custom tools" mention to custom-tools.html
            (
                "A fixed fee for a defined deliverable — typically an SEO audit, a keyword strategy, a site migration plan, or a content audit.",
                'A fixed fee for a defined deliverable — typically an <a href="../seo-web.html">SEO audit</a>, a keyword strategy, a site migration plan, or a content audit.'
            ),
            # Link "AI consulting" to ai-consulting.html in tools section
            (
                "whether that's SEO strategy, site builds, or automation systems.",
                'whether that\'s SEO strategy, site builds, or <a href="../ai-consulting.html">automation systems</a>.'
            ),
        ]
    },
]

updated = 0
skipped = 0

for page in CHANGES:
    path = os.path.join(BASE, page["file"])

    if not os.path.exists(path):
        print(f"  SKIP  {page['file']} — file not found")
        skipped += 1
        continue

    content = open(path, encoding="utf-8").read()
    original = content
    links_added = 0

    for old, new in page["replacements"]:
        if old in content:
            content = content.replace(old, new, 1)
            links_added += 1
        else:
            print(f"  WARN  {page['file']} — string not found: {old[:60]}...")

    if content != original:
        open(path, "w", encoding="utf-8").write(content)
        print(f"  OK    {page['file']} — {links_added} links added")
        updated += 1
    else:
        print(f"  SKIP  {page['file']} — no changes made")
        skipped += 1

print(f"\n  {updated} files updated, {skipped} skipped")
print("\nDone. Deploy next:")
print('  python3 ~/Desktop/ClaudeWork/Rich/deploy.py "add internal links from blog posts to service pages"')
