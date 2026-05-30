#!/usr/bin/env python3
"""
Replaces all hardcoded nav blocks in richnashawaty.com HTML files
with a single <script src="nav.js"> tag.
Run: python3 ~/Desktop/ClaudeWork/Rich/replace_navs.py
"""

import os, re

BASE = os.path.expanduser("~/Desktop/ClaudeWork/Rich")

# The single replacement tag — paths are relative per depth
ROOT_TAG = '<script src="nav.js"></script>'
BLOG_TAG = '<script src="../nav.js"></script>'

# Pattern to match everything from <nav> through the closing </div> of nav-mobile-menu
# Handles both orderings (nav before or after mobile menu div)
NAV_PATTERN = re.compile(
    r'<nav\b.*?</nav>\s*<div class="nav-mobile-menu".*?</div>',
    re.DOTALL
)

updated = 0
skipped = 0
errors = []

for root, dirs, files in os.walk(BASE):
    dirs[:] = [d for d in dirs if d not in ['.git', 'node_modules', '__pycache__']]
    for f in files:
        if not f.endswith('.html'):
            continue
        path = os.path.join(root, f)
        rel = os.path.relpath(path, BASE)

        try:
            content = open(path, encoding='utf-8', errors='ignore').read()
        except Exception as e:
            errors.append(f"  ERROR reading {rel}: {e}")
            continue

        # Skip if already converted
        if 'nav.js' in content:
            print(f"  SKIP  {rel} — already using nav.js")
            skipped += 1
            continue

        # Skip if no nav block found
        if '<nav' not in content:
            continue

        is_blog = rel.startswith('blog/')
        tag = BLOG_TAG if is_blog else ROOT_TAG

        new_content = NAV_PATTERN.sub(tag, content)

        if new_content == content:
            # Pattern didn't match — try alternate: mobile menu BEFORE nav
            ALT_PATTERN = re.compile(
                r'<div class="nav-mobile-menu".*?</div>\s*<nav\b.*?</nav>',
                re.DOTALL
            )
            new_content = ALT_PATTERN.sub(tag, content)

        if new_content == content:
            errors.append(f"  WARN  {rel} — nav pattern not matched, skipping")
            continue

        # Also remove any orphaned mobile menu divs that may remain
        new_content = re.sub(
            r'\s*<div class="nav-mobile-menu"[^>]*>.*?</div>',
            '',
            new_content,
            flags=re.DOTALL
        )

        # Remove old hamburger JS if it's standalone at bottom of page
        new_content = re.sub(
            r'\s*\(function\s*\(\s*\)\s*\{[^}]*nav-hamburger[^}]*(?:\{[^}]*\}[^}]*)*\}\s*\)\s*\(\s*\)\s*;',
            '',
            new_content,
            flags=re.DOTALL
        )

        open(path, 'w', encoding='utf-8').write(new_content)
        print(f"  OK    {rel}")
        updated += 1

print(f"\n  {updated} files updated, {skipped} already converted")
if errors:
    print("\nWarnings/Errors:")
    for e in errors:
        print(e)

print("\nNext steps:")
print("  1. Copy nav.js to ~/Desktop/ClaudeWork/Rich/")
print('  2. deploy-rich "replace hardcoded navs with nav.js — single source of truth"')
print("  3. Test a root page and a blog page in browser")
