#!/usr/bin/env python3
"""
Replaces broken hamburger nav code on all pages with the working pattern.
Run: python3 ~/Desktop/ClaudeWork/Rich/fix_hamburger_final.py
"""

import re
import os

BASE = os.path.expanduser("~/Desktop/ClaudeWork/Rich")

ROOT_FILES = [
    "index.html",
    "seo-web.html",
    "ai-consulting.html",
    "custom-tools.html",
    "about.html",
    "privacy.html",
    "terms.html",
]

BLOG_FILES = [
    "blog/index.html",
    "blog/what-does-seo-consultant-do.html",
    "blog/how-much-does-seo-consultant-cost-boston.html",
    "blog/why-isnt-my-boston-business-ranking-on-google.html",
    "blog/google-may-2026-algorithm-update-boston-small-business.html",
]

# Working CSS — clean, no nesting issues
HAMBURGER_CSS = """
  /* HAMBURGER NAV */
  .nav-hamburger { display: none; flex-direction: column; gap: 5px; cursor: pointer; padding: 4px; background: none; border: none; z-index: 200; }
  .nav-hamburger span { display: block; width: 22px; height: 2px; background: var(--text2); border-radius: 2px; transition: all 0.25s; }
  .nav-hamburger.open span:nth-child(1) { transform: translateY(7px) rotate(45deg); }
  .nav-hamburger.open span:nth-child(2) { opacity: 0; }
  .nav-hamburger.open span:nth-child(3) { transform: translateY(-7px) rotate(-45deg); }
  .nav-mobile-menu { display: none; position: fixed; top: 64px; left: 0; right: 0; background: rgba(24,24,22,0.98); backdrop-filter: blur(18px); -webkit-backdrop-filter: blur(18px); border-bottom: 1px solid var(--border); padding: 1.5rem 2rem; z-index: 99; flex-direction: column; gap: 0; }
  .nav-mobile-menu.open { display: flex; }
  .nav-mobile-menu a { color: var(--text2); text-decoration: none; font-size: 1rem; font-weight: 500; padding: 0.85rem 0; border-bottom: 1px solid var(--border); transition: color 0.2s; }
  .nav-mobile-menu a:last-child { border-bottom: none; }
  .nav-mobile-menu a:hover { color: var(--accent); }
  .nav-mobile-menu .mobile-cta { color: var(--accent) !important; font-weight: 600; margin-top: 0.5rem; }
  @media (max-width: 640px) {
    .nav-hamburger { display: flex; }
    .nav-links { display: none; }
    .nav-cta { display: none; }
  }"""

# Working hamburger button HTML
HAMBURGER_BTN = """  <button class="nav-hamburger" id="nav-hamburger" aria-label="Toggle navigation" aria-expanded="false">
    <span></span><span></span><span></span>
  </button>"""

# Working JS
HAMBURGER_JS = """
<script>
  (function() {
    var btn = document.getElementById('nav-hamburger');
    var menu = document.getElementById('nav-mobile-menu');
    if (!btn || !menu) return;
    btn.addEventListener('click', function() {
      var open = menu.classList.toggle('open');
      btn.classList.toggle('open', open);
      btn.setAttribute('aria-expanded', open);
    });
    menu.querySelectorAll('a').forEach(function(a) {
      a.addEventListener('click', function() {
        menu.classList.remove('open');
        btn.classList.remove('open');
        btn.setAttribute('aria-expanded', false);
      });
    });
  })();
</script>"""

def mobile_menu_html(is_blog):
    prefix = "../" if is_blog else ""
    contact_href = "mailto:contact@richnashawaty.com" if is_blog else "#contact"
    return f"""
<div class="nav-mobile-menu" id="nav-mobile-menu">
  <a href="{prefix}seo-web.html">SEO &amp; Web</a>
  <a href="{prefix}ai-consulting.html">AI Consulting</a>
  <a href="{prefix}custom-tools.html">Custom Tools</a>
  <a href="{prefix}blog/">Blog</a>
  <a href="{prefix}about.html">About</a>
  <a href="{contact_href}" class="mobile-cta">Let's Talk</a>
</div>"""

def clean_all_hamburger(content):
    """Remove ALL existing hamburger-related code from the file."""

    # Remove HAMBURGER NAV CSS block
    content = re.sub(
        r'/\* HAMBURGER NAV \*/.*?(?=\n  [a-z@/]|\Z)',
        '',
        content,
        flags=re.DOTALL
    )

    # Remove any stray .nav-hamburger blocks outside style tag
    content = re.sub(
        r'\n\.nav-hamburger \{[^}]*\}',
        '',
        content
    )

    # Remove nav-mobile-menu div
    content = re.sub(
        r'\n<div class="nav-mobile-menu"[^>]*>.*?</div>',
        '',
        content,
        flags=re.DOTALL
    )

    # Remove hamburger button
    content = re.sub(
        r'\s*<button class="nav-hamburger"[^>]*>.*?</button>',
        '',
        content,
        flags=re.DOTALL
    )

    # Remove hamburger JS
    content = re.sub(
        r'\n<script>\s*\(function\(\) \{[^}]*nav-hamburger[^<]*</script>',
        '',
        content,
        flags=re.DOTALL
    )

    # Fix any display:none !important on nav-links/nav-cta left from previous attempts
    content = content.replace('.nav-links { display: none !important; }', '.nav-links { display: none; }')
    content = content.replace('.nav-cta { display: none !important; }', '.nav-cta { display: none; }')

    # Remove the old hide-all mobile rule if still present
    content = content.replace('.nav-links li:not(:last-child) { display: none; }', '')

    return content

updated = 0
skipped = 0

all_files = [(f, False) for f in ROOT_FILES] + [(f, True) for f in BLOG_FILES]

for fname, is_blog in all_files:
    path = os.path.join(BASE, fname)
    if not os.path.exists(path):
        print(f"  SKIP  {fname} — not found"); skipped += 1; continue

    content = open(path, encoding="utf-8").read()
    original = content

    # Step 1: Strip all existing hamburger code
    content = clean_all_hamburger(content)

    # Step 2: Inject clean CSS before first </style>
    content = content.replace("</style>", HAMBURGER_CSS + "\n</style>", 1)

    # Step 3: Inject hamburger button before </nav>
    content = content.replace("</nav>", HAMBURGER_BTN + "\n</nav>", 1)

    # Step 4: Inject mobile menu after </nav>
    content = content.replace("</nav>", "</nav>\n" + mobile_menu_html(is_blog), 1)

    # Step 5: Inject JS before </body>
    content = content.replace("</body>", HAMBURGER_JS + "\n</body>")

    if content != original:
        open(path, "w", encoding="utf-8").write(content)
        print(f"  OK    {fname}"); updated += 1
    else:
        print(f"  SKIP  {fname} — no changes"); skipped += 1

print(f"\n  {updated} files updated, {skipped} skipped")
print("\nVerify on one file before deploying:")
print("  grep -n 'nav-hamburger\\|HAMBURGER' ~/Desktop/ClaudeWork/Rich/index.html | head -10")
print("\nThen deploy:")
print('  python3 ~/Desktop/ClaudeWork/Rich/deploy.py "fix hamburger nav - clean rebuild"')
