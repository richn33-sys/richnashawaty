#!/usr/bin/env python3
"""
Adds fifth blog post card to blog/index.html.
Run: python3 ~/Desktop/ClaudeWork/Rich/add_post5.py
"""

import os

BASE = os.path.expanduser("~/Desktop/ClaudeWork/Rich")

NEW_CARD = """
      <!-- Post 5 — live -->
      <a href="what-is-geo-generative-engine-optimization-boston.html" class="post-card" data-category="seo">
        <div class="post-card-top">
          <span class="post-tag">SEO</span>
          <span class="post-date">May 21, 2026</span>
          <span class="post-read">7 min read</span>
        </div>
        <h2 class="post-title">What Is GEO (Generative Engine Optimization)? A Plain-English Guide for Boston Business Owners</h2>
        <p class="post-excerpt">GEO is the hottest acronym in digital marketing right now — and most of what's being sold under that label is just good SEO with a new name. Here's what's real, what's hype, and what Boston small businesses actually need to do.</p>
        <div class="post-card-footer">
          <div class="post-author">
            <div class="post-avatar">R</div>
            <span class="post-author-name">Rich Nashawaty</span>
          </div>
          <span class="post-arrow">→</span>
        </div>
      </a>"""

path = os.path.join(BASE, "blog/index.html")
content = open(path, encoding="utf-8").read()

if "what-is-geo-generative-engine-optimization" in content:
    print("  SKIP  blog/index.html — post 5 already present")
else:
    injected = False
    # Inject after post 4 closing </a>
    marker = "google-may-2026-algorithm-update-boston-small-business.html"
    idx = content.find(marker)
    if idx != -1:
        close_idx = content.find("</a>", idx)
        if close_idx != -1:
            content = content[:close_idx + 4] + NEW_CARD + content[close_idx + 4:]
            injected = True

    if not injected:
        # Fallback
        marker2 = "    </div>\n  </div>\n</section>"
        if marker2 in content:
            content = content.replace(marker2, NEW_CARD + "\n" + marker2, 1)
            injected = True

    if injected:
        open(path, "w", encoding="utf-8").write(content)
        print("  OK    blog/index.html — post 5 card added")
    else:
        print("  WARN  blog/index.html — could not find injection point")

print("\nDone. Deploy next:")
print('  python3 ~/Desktop/ClaudeWork/Rich/deploy.py "add fifth blog post - What Is GEO"')
