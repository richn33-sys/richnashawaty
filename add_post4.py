#!/usr/bin/env python3
"""
Adds fourth blog post card to blog/index.html.
Run: python3 ~/Desktop/ClaudeWork/Rich/add_post4.py
"""

import os

BASE = os.path.expanduser("~/Desktop/ClaudeWork/Rich")

NEW_CARD = """
      <!-- Post 4 — live -->
      <a href="google-may-2026-algorithm-update-boston-small-business.html" class="post-card" data-category="seo">
        <div class="post-card-top">
          <span class="post-tag">SEO</span>
          <span class="post-date">May 20, 2026</span>
          <span class="post-read">7 min read</span>
        </div>
        <h2 class="post-title">Google May 2026 Algorithm Update: What Boston Small Businesses Need to Know</h2>
        <p class="post-excerpt">The May 2026 core update is done rolling out. Rankings shifted significantly — roughly one in four pages fell out of the top 100. Here's what actually changed, who got hit, and exactly what to do about it.</p>
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

if "google-may-2026-algorithm-update" in content:
    print("  SKIP  blog/index.html — post 4 already present")
else:
    injected = False
    # Try to inject after post 3 closing </a>
    if "why-isnt-my-boston-business-ranking-on-google.html" in content:
        # Find the </a> that closes post 3's card
        marker = "why-isnt-my-boston-business-ranking-on-google.html"
        idx = content.find(marker)
        # Find the next </a> after this marker
        close_idx = content.find("</a>", idx)
        if close_idx != -1:
            content = content[:close_idx + 4] + NEW_CARD + content[close_idx + 4:]
            injected = True

    if not injected:
        # Fallback: inject before closing grid div
        marker = "    </div>\n  </div>\n</section>"
        if marker in content:
            content = content.replace(marker, NEW_CARD + "\n" + marker, 1)
            injected = True

    if injected:
        open(path, "w", encoding="utf-8").write(content)
        print("  OK    blog/index.html — post 4 card added")
    else:
        print("  WARN  blog/index.html — could not find injection point")

print("\nDone. Deploy next:")
print('  python3 ~/Desktop/ClaudeWork/Rich/deploy.py "add fourth blog post - Google May 2026 update"')
