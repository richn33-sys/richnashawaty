#!/usr/bin/env python3
"""
Fixes hamburger menu not showing on mobile.
Finds the existing 640px media block and ensures hamburger rules are correct.
Run: python3 ~/Desktop/ClaudeWork/Rich/fix_hamburger.py
"""

import re
import os

BASE = os.path.expanduser("~/Desktop/ClaudeWork/Rich")

ALL_FILES = [
    "index.html",
    "seo-web.html",
    "ai-consulting.html",
    "custom-tools.html",
    "about.html",
    "privacy.html",
    "terms.html",
    "blog/index.html",
    "blog/what-does-seo-consultant-do.html",
    "blog/how-much-does-seo-consultant-cost-boston.html",
    "blog/why-isnt-my-boston-business-ranking-on-google.html",
    "blog/google-may-2026-algorithm-update-boston-small-business.html",
]

updated = 0
skipped = 0

for fname in ALL_FILES:
    path = os.path.join(BASE, fname)
    if not os.path.exists(path):
        print(f"  SKIP  {fname} — not found"); skipped += 1; continue

    content = open(path, encoding="utf-8").read()
    original = content

    # Step 1: Remove any nested @media (max-width: 640px) blocks that contain nav-hamburger
    # These were incorrectly inserted inside other blocks by the previous script
    content = re.sub(
        r'\s*@media \(max-width: 640px\) \{\s*\.nav-hamburger \{ display: flex; \}[^}]*\}',
        '',
        content
    )

    # Step 2: Make sure .nav-hamburger base style has display:none (hidden on desktop)
    content = re.sub(
        r'(\.nav-hamburger \{[^}]*?)display: flex;',
        r'\1display: none;',
        content
    )
    # If no display property in .nav-hamburger block, add it
    if '.nav-hamburger {' in content:
        content = re.sub(
            r'(\.nav-hamburger \{)',
            r'\1\n      display: none;',
            content,
            count=1
        )
        # Clean up double display:none if it got added twice
        content = re.sub(r'display: none;\s*display: none;', 'display: none;', content)

    # Step 3: Find the 640px media query that has nav rules and inject hamburger fix
    # Pattern: look for the block containing .nav-links { display: none; }
    def fix_media_block(m):
        block = m.group(0)
        if '.nav-hamburger' not in block:
            # Add hamburger show rule
            block = block.replace(
                '.nav-links { display: none; }',
                '.nav-links { display: none; }\n    .nav-cta { display: none; }\n    .nav-hamburger { display: flex !important; }'
            )
        return block

    content = re.sub(
        r'@media \(max-width: 640px\) \{[^}]*\.nav-links \{ display: none; \}[^}]*\}',
        fix_media_block,
        content
    )

    if content != original:
        open(path, "w", encoding="utf-8").write(content)
        print(f"  OK    {fname}"); updated += 1
    else:
        print(f"  SKIP  {fname} — no changes needed"); skipped += 1

print(f"\n  {updated} files updated, {skipped} skipped")
print("\nDone. Deploy next:")
print('  python3 ~/Desktop/ClaudeWork/Rich/deploy.py "fix hamburger menu display on mobile"')
