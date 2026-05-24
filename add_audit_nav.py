#!/usr/bin/env python3
"""
1. Adds Local SEO Audit to nav on all pages
2. Adds callout box to why-isnt-my-boston-business-ranking post
Run: python3 ~/Desktop/ClaudeWork/Rich/add_audit_nav.py
"""

import os, re

BASE = os.path.expanduser("~/Desktop/ClaudeWork/Rich")

ROOT_FILES = ["index.html", "seo-web.html", "ai-consulting.html", "custom-tools.html",
              "seo-ai-visibility.html", "about.html", "privacy.html", "terms.html",
              "seo-audit-checklist.html", "seo-audit-checklist-full.html"]

BLOG_FILES = ["blog/index.html", "blog/what-does-seo-consultant-do.html",
              "blog/how-much-does-seo-consultant-cost-boston.html",
              "blog/why-isnt-my-boston-business-ranking-on-google.html",
              "blog/what-is-geo-generative-engine-optimization-boston.html",
              "blog/how-much-does-ai-automation-cost-small-business.html",
              "blog/questions-to-ask-before-hiring-seo-consultant-boston.html"]

# --- NAV UPDATE ---
# Root pages: insert after seo-web.html li
OLD_ROOT_NAV = '<li><a href="seo-web.html">SEO &amp; Web</a></li>'
NEW_ROOT_NAV = '<li><a href="seo-web.html">SEO &amp; Web</a></li>\n    <li><a href="local-seo-audit.html">Local SEO Audit</a></li>'

OLD_ROOT_MOBILE = '<a href="seo-web.html">SEO &amp; Web</a>'
NEW_ROOT_MOBILE = '<a href="seo-web.html">SEO &amp; Web</a>\n  <a href="local-seo-audit.html">Local SEO Audit</a>'

# Blog pages: insert after seo-web link
OLD_BLOG_NAV = '<li><a href="../seo-web.html">SEO &amp; Web</a></li>'
NEW_BLOG_NAV = '<li><a href="../seo-web.html">SEO &amp; Web</a></li>\n    <li><a href="../local-seo-audit.html">Local SEO Audit</a></li>'

OLD_BLOG_MOBILE = '<a href="../seo-web.html">SEO &amp; Web</a>'
NEW_BLOG_MOBILE = '<a href="../seo-web.html">SEO &amp; Web</a>\n  <a href="../local-seo-audit.html">Local SEO Audit</a>'

updated = 0

for fname in ROOT_FILES:
    path = os.path.join(BASE, fname)
    if not os.path.exists(path): continue
    content = open(path).read()
    if 'local-seo-audit.html' in content:
        print(f"  SKIP  {fname}"); continue
    content = content.replace(OLD_ROOT_NAV, NEW_ROOT_NAV, 1)
    content = content.replace(OLD_ROOT_MOBILE, NEW_ROOT_MOBILE, 1)
    open(path, "w").write(content)
    print(f"  OK    {fname}"); updated += 1

for fname in BLOG_FILES:
    path = os.path.join(BASE, fname)
    if not os.path.exists(path): continue
    content = open(path).read()
    if 'local-seo-audit.html' in content:
        print(f"  SKIP  {fname}"); continue
    content = content.replace(OLD_BLOG_NAV, NEW_BLOG_NAV, 1)
    content = content.replace(OLD_BLOG_MOBILE, NEW_BLOG_MOBILE, 1)
    open(path, "w").write(content)
    print(f"  OK    {fname}"); updated += 1

# --- CALLOUT BOX in ranking post ---
RANKING_POST = os.path.join(BASE, "blog/why-isnt-my-boston-business-ranking-on-google.html")
CALLOUT = """
      <div style="background:var(--bg2);border:1px solid var(--border);border-left:3px solid var(--accent);border-radius:0 10px 10px 0;padding:1.25rem 1.5rem;margin:2.5rem 0;">
        <div style="font-family:var(--mono);font-size:0.7rem;letter-spacing:0.08em;text-transform:uppercase;color:var(--accent);margin-bottom:0.5rem;">Local SEO Audit — $497</div>
        <p style="font-size:0.95rem;color:var(--text2);margin-bottom:0.75rem;">Not sure which of these issues is hurting your rankings most? I audit your Google Business Profile and local search presence against your top 3 competitors — and give you a prioritized list of exactly what to fix. 5–7 day turnaround.</p>
        <a href="../local-seo-audit.html" style="font-family:var(--mono);font-size:0.82rem;color:var(--accent);text-decoration:none;font-weight:600;">See what's included →</a>
      </div>"""

if os.path.exists(RANKING_POST):
    content = open(RANKING_POST).read()
    if 'local-seo-audit.html' not in content:
        # Inject before the article CTA at the bottom
        content = content.replace('<div class="article-cta">', CALLOUT + '\n    <div class="article-cta">', 1)
        open(RANKING_POST, "w").write(content)
        print(f"  OK    callout added to ranking post")
    else:
        print(f"  SKIP  callout already in ranking post")

print(f"\n  {updated} nav files updated")
print("\nDeploy next:")
print('  deploy-rich "add Local SEO Audit page and nav links"')
