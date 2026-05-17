#!/usr/bin/env python3
"""
Adds missing schema and creates robots.txt:
- ProfilePage schema on about.html
- BreadcrumbList schema on both blog posts
- Organization schema on index.html
- robots.txt in site root

Run: python3 ~/Desktop/ClaudeWork/Rich/add_schema.py
"""

import os

BASE = os.path.expanduser("~/Desktop/ClaudeWork/Rich")

# ── 1. ProfilePage schema for about.html ──────────────────────────────────────

PROFILE_PAGE_SCHEMA = """
  <!-- ProfilePage Schema -->
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "ProfilePage",
    "dateCreated": "2026-05-14",
    "dateModified": "2026-05-17",
    "mainEntity": {
      "@type": "Person",
      "@id": "https://richnashawaty.com/about.html",
      "name": "Rich Nashawaty",
      "givenName": "Rich",
      "familyName": "Nashawaty",
      "jobTitle": "SEO Consultant",
      "description": "SEO consultant with 20 years of experience across freelance, agency, and enterprise. Former Director of SEO at Ziff Davis. Based in Boston, MA, serving small businesses across Greater New England.",
      "url": "https://richnashawaty.com",
      "email": "contact@richnashawaty.com",
      "address": {
        "@type": "PostalAddress",
        "addressLocality": "Boston",
        "addressRegion": "MA",
        "addressCountry": "US"
      },
      "knowsAbout": [
        "Search Engine Optimization",
        "Technical SEO",
        "Local SEO",
        "AI Consulting",
        "Marketing Automation",
        "Content Strategy",
        "Web Design"
      ],
      "alumniOf": [
        { "@type": "Organization", "name": "Ziff Davis" },
        { "@type": "Organization", "name": "Monster" },
        { "@type": "Organization", "name": "Kayak" },
        { "@type": "Organization", "name": "Care.com" },
        { "@type": "Organization", "name": "Catalyst" },
        { "@type": "Organization", "name": "451 Marketing" },
        { "@type": "Organization", "name": "Charles River Interactive" }
      ]
    }
  }
  </script>"""

# ── 2. BreadcrumbList schema for blog posts ───────────────────────────────────

BREADCRUMB_POST1 = """
  <!-- BreadcrumbList Schema -->
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "BreadcrumbList",
    "itemListElement": [
      {
        "@type": "ListItem",
        "position": 1,
        "name": "Home",
        "item": "https://richnashawaty.com/"
      },
      {
        "@type": "ListItem",
        "position": 2,
        "name": "Blog",
        "item": "https://richnashawaty.com/blog/"
      },
      {
        "@type": "ListItem",
        "position": 3,
        "name": "What Does an SEO Consultant Actually Do?",
        "item": "https://richnashawaty.com/blog/what-does-seo-consultant-do.html"
      }
    ]
  }
  </script>"""

BREADCRUMB_POST2 = """
  <!-- BreadcrumbList Schema -->
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "BreadcrumbList",
    "itemListElement": [
      {
        "@type": "ListItem",
        "position": 1,
        "name": "Home",
        "item": "https://richnashawaty.com/"
      },
      {
        "@type": "ListItem",
        "position": 2,
        "name": "Blog",
        "item": "https://richnashawaty.com/blog/"
      },
      {
        "@type": "ListItem",
        "position": 3,
        "name": "How Much Does an SEO Consultant Cost in Boston?",
        "item": "https://richnashawaty.com/blog/how-much-does-seo-consultant-cost-boston.html"
      }
    ]
  }
  </script>"""

# ── 3. Organization schema for index.html ─────────────────────────────────────

ORGANIZATION_SCHEMA = """
  <!-- Organization Schema -->
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "Organization",
    "name": "Rich Nashawaty Consulting",
    "url": "https://richnashawaty.com",
    "logo": "https://richnashawaty.com/favicon.ico",
    "description": "SEO consulting and AI automation for small businesses in Boston and Greater New England. 20 years of experience across freelance, agency, and enterprise.",
    "email": "contact@richnashawaty.com",
    "founder": {
      "@type": "Person",
      "name": "Rich Nashawaty",
      "jobTitle": "SEO Consultant",
      "url": "https://richnashawaty.com/about.html"
    },
    "address": {
      "@type": "PostalAddress",
      "addressLocality": "Boston",
      "addressRegion": "MA",
      "addressCountry": "US"
    },
    "areaServed": [
      "Boston, MA",
      "Greater Boston",
      "New England",
      "Massachusetts"
    ],
    "sameAs": [
      "https://richnashawaty.com"
    ],
    "knowsAbout": [
      "Search Engine Optimization",
      "Technical SEO",
      "Local SEO",
      "AI Consulting",
      "Marketing Automation",
      "Web Design"
    ]
  }
  </script>"""

# ── 4. robots.txt ─────────────────────────────────────────────────────────────

ROBOTS_TXT = """User-agent: *
Allow: /

User-agent: Googlebot
Allow: /

User-agent: Google-Extended
Allow: /

User-agent: GPTBot
Allow: /

User-agent: ClaudeBot
Allow: /

User-agent: PerplexityBot
Allow: /

Sitemap: https://richnashawaty.com/sitemap.xml
"""

# ── Run updates ───────────────────────────────────────────────────────────────

updated = 0
skipped = 0

def inject_schema(filepath, schema, marker="ProfilePage schema" ):
    global updated, skipped
    path = os.path.join(BASE, filepath)
    if not os.path.exists(path):
        print(f"  SKIP  {filepath} — file not found"); skipped += 1; return
    content = open(path, encoding="utf-8").read()
    if marker in content:
        print(f"  SKIP  {filepath} — schema already present"); skipped += 1; return
    content = content.replace("</head>", schema + "\n</head>")
    open(path, "w", encoding="utf-8").write(content)
    print(f"  OK    {filepath}"); updated += 1

# ProfilePage on about.html
inject_schema("about.html", PROFILE_PAGE_SCHEMA, "ProfilePage")

# BreadcrumbList on blog posts
inject_schema("blog/what-does-seo-consultant-do.html", BREADCRUMB_POST1, "BreadcrumbList")
inject_schema("blog/how-much-does-seo-consultant-cost-boston.html", BREADCRUMB_POST2, "BreadcrumbList")

# Organization on index.html
inject_schema("index.html", ORGANIZATION_SCHEMA, "Organization")

# robots.txt
robots_path = os.path.join(BASE, "robots.txt")
if os.path.exists(robots_path):
    print(f"  SKIP  robots.txt — already exists"); skipped += 1
else:
    open(robots_path, "w", encoding="utf-8").write(ROBOTS_TXT)
    print(f"  OK    robots.txt created"); updated += 1

print(f"\n  {updated} files updated, {skipped} skipped")
print("\nDone. Deploy next:")
print('  python3 ~/Desktop/ClaudeWork/Rich/deploy.py "add ProfilePage/BreadcrumbList/Organization schema and robots.txt"')
