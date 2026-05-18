#!/usr/bin/env python3
"""
Adds third blog post card to blog/index.html.
Run: python3 ~/Desktop/ClaudeWork/Rich/add_post3.py
"""

import os

BASE = os.path.expanduser("~/Desktop/ClaudeWork/Rich")

NEW_CARD = """
      <!-- Post 3 — live -->
      <a href="why-isnt-my-boston-business-ranking-on-google.html" class="post-card" data-category="seo">
        <div class="post-card-top">
          <span class="post-tag">SEO</span>
          <span class="post-date">May 17, 2026</span>
          <span class="post-read">8 min read</span>
        </div>
        <h2 class="post-title">Why Isn't My Boston Business Ranking on Google?</h2>
        <p class="post-excerpt">If your business isn't showing up when Boston customers search for what you offer, there's always a reason. Here's how to diagnose the most common causes — and what to actually do about them.</p>
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

if "why-isnt-my-boston-business-ranking" in content:
    print("  SKIP  blog/index.html — post 3 already present")
else:
    # Inject after post 2 card closing </a>
    marker = '</a>\n\n    </div>'
    if marker in content:
        content = content.replace(marker, '</a>' + NEW_CARD + '\n\n    </div>', 1)
        open(path, "w", encoding="utf-8").write(content)
        print("  OK    blog/index.html — post 3 card added")
    else:
        # fallback: inject before closing grid div
        marker2 = '    </div>\n  </div>\n</section>'
        content = content.replace(marker2, NEW_CARD + '\n    </div>\n  </div>\n</section>', 1)
        open(path, "w", encoding="utf-8").write(content)
        print("  OK    blog/index.html — post 3 card added (fallback)")

print("\nDone. Deploy next:")
print('  python3 ~/Desktop/ClaudeWork/Rich/deploy.py "add third blog post"')
