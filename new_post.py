#!/usr/bin/env python3
"""
new_post.py -- adds a blog index card and sitemap entry for a new post.
Usage: python3 new_post.py "filename.html" "Title" "Excerpt" "Tag" "Month DD, YYYY" "X min read"
"""
import sys, os, re
from datetime import datetime

if len(sys.argv) < 7:
    print("Usage: python3 new_post.py filename title excerpt tag date readtime")
    sys.exit(1)

filename  = sys.argv[1]
title     = sys.argv[2]
excerpt   = sys.argv[3]
tag       = sys.argv[4]
date_str  = sys.argv[5]
read_time = sys.argv[6]

BASE       = os.path.dirname(os.path.abspath(__file__))
blog_index = os.path.join(BASE, "blog", "index.html")
sitemap    = os.path.join(BASE, "sitemap.xml")

CARD = """
      <a href="{f}" class="post-card" data-category="{tc}">
        <div class="post-card-top">
          <span class="post-tag">{t}</span>
          <span class="post-date">{d}</span>
          <span class="post-read">{r}</span>
        </div>
        <h2 class="post-title">{ti}</h2>
        <p class="post-excerpt">{e}</p>
        <div class="post-card-footer">
          <div class="post-author">
            <div class="post-avatar">R</div>
            <span class="post-author-name">Rich Nashawaty</span>
          </div>
          <span class="post-arrow">-></span>
        </div>
      </a>""".format(f=filename, tc=tag.lower(), t=tag, d=date_str, r=read_time, ti=title, e=excerpt)

content = open(blog_index).read()
if filename in content:
    print("SKIP blog index -- already present")
else:
    cards = list(re.finditer(r'<a href="[^"]+\.html" class="post-card"', content))
    if cards:
        close = content.find("</a>", cards[-1].start())
        content = content[:close+4] + CARD + content[close+4:]
    else:
        content = content.replace("</main>", CARD + "\n  </main>", 1)
    open(blog_index, "w").write(content)
    print("OK  blog index -- added " + filename)

try:
    iso_date = datetime.strptime(date_str, "%B %d, %Y").strftime("%Y-%m-%d")
except:
    iso_date = datetime.today().strftime("%Y-%m-%d")

NEW_URL = """  <url>
    <loc>https://richnashawaty.com/blog/{f}</loc>
    <lastmod>{d}</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.7</priority>
  </url>""".format(f=filename, d=iso_date)

smap = open(sitemap).read()
if filename in smap:
    print("SKIP sitemap -- already present")
else:
    smap = smap.replace("</urlset>", NEW_URL + "\n</urlset>")
    open(sitemap, "w").write(smap)
    print("OK  sitemap -- added " + filename)

print("Done.")
