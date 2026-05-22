#!/usr/bin/env python3
"""
Definitive hamburger fix — strips all broken hamburger code from older pages
and injects the exact working pattern from the GEO post.
Run: python3 ~/Desktop/ClaudeWork/Rich/fix_hamburger_definitive.py
"""

import re
import os

BASE = os.path.expanduser("~/Desktop/ClaudeWork/Rich")

# These pages need fixing — new pages (GEO post, AI Visibility) already work
ROOT_FILES = [
    ("index.html", False),
    ("seo-web.html", False),
    ("ai-consulting.html", False),
    ("custom-tools.html", False),
    ("about.html", False),
    ("privacy.html", False),
    ("terms.html", False),
]

BLOG_FILES = [
    ("blog/index.html", True),
    ("blog/what-does-seo-consultant-do.html", True),
    ("blog/how-much-does-seo-consultant-cost-boston.html", True),
    ("blog/why-isnt-my-boston-business-ranking-on-google.html", True),
]

# The exact working CSS from the GEO post
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

# Hamburger button HTML
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
    contact = "mailto:contact@richnashawaty.com" if is_blog else "#contact"
    return f"""<div class="nav-mobile-menu" id="nav-mobile-menu">
  <a href="{prefix}seo-web.html">SEO &amp; Web</a>
  <a href="{prefix}ai-consulting.html">AI Consulting</a>
  <a href="{prefix}custom-tools.html">Custom Tools</a>
  <a href="{prefix}seo-ai-visibility.html">AI Visibility</a>
  <a href="{prefix}blog/">Blog</a>
  <a href="{prefix}about.html">About</a>
  <a href="{contact}" class="mobile-cta">Let's Talk</a>
</div>"""

def strip_all_hamburger(content):
    """Remove every trace of previous hamburger attempts."""

    # Remove HAMBURGER NAV CSS block (with comment)
    content = re.sub(
        r'\s*/\* HAMBURGER NAV \*/.*?(?=\n  [a-z@/.]|\n</style>)',
        '',
        content,
        flags=re.DOTALL
    )

    # Remove any stray .nav-hamburger blocks outside <style>
    content = re.sub(r'\n\.nav-hamburger \{[^}]*\}', '', content)

    # Remove nav-mobile-menu div
    content = re.sub(
        r'\n?<div class="nav-mobile-menu"[^>]*>.*?</div>',
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

    # Remove hamburger JS block
    content = re.sub(
        r'\n<script>\s*\(function\(\)[^<]*nav-hamburger[^<]*</script>',
        '',
        content,
        flags=re.DOTALL
    )

    # Remove any @media 640px blocks that only contain nav-hamburger rules
    content = re.sub(
        r'\s*@media \(max-width: 640px\) \{\s*\.nav-hamburger \{ display: flex[^}]*\}\s*\.nav-links \{ display: none[^}]*\}\s*\.nav-cta \{ display: none[^}]*\}\s*\}',
        '',
        content
    )

    # Fix any existing 640px nav block — make sure it shows hamburger
    # Find 640px block that has nav padding and add hamburger rule if missing
    def fix_640_block(m):
        block = m.group(0)
        if '.nav-hamburger' not in block:
            block = block.replace(
                '.nav-links { display: none; }',
                '.nav-links { display: none; } .nav-cta { display: none; } .nav-hamburger { display: flex; }'
            )
        return block

    content = re.sub(
        r'@media \(max-width: 640px\) \{[^}]*nav[^}]*\}',
        fix_640_block,
        content
    )

    return content

updated = 0
skipped = 0

for fname, is_blog in ROOT_FILES + BLOG_FILES:
    path = os.path.join(BASE, fname)
    if not os.path.exists(path):
        print(f"  SKIP  {fname} — not found"); skipped += 1; continue

    content = open(path, encoding="utf-8").read()
    original = content

    # Step 1: Strip all existing hamburger code
    content = strip_all_hamburger(content)

    # Step 2: Inject clean CSS before LAST </style> (before GA tag etc)
    if "HAMBURGER NAV" not in content:
        content = content.replace("</style>", HAMBURGER_CSS + "\n</style>", 1)

    # Step 3: Add hamburger button before </nav>
    if 'nav-hamburger' not in content.split('</nav>')[0] if '</nav>' in content else True:
        content = content.replace("</nav>", HAMBURGER_BTN + "\n</nav>", 1)

    # Step 4: Add mobile menu after </nav>
    if 'nav-mobile-menu' not in content:
        content = content.replace("</nav>", "</nav>\n\n" + mobile_menu_html(is_blog), 1)

    # Step 5: Add JS before </body>
    if "(function()" not in content.split('</body>')[-2] if '</body>' in content else True:
        content = content.replace("</body>", HAMBURGER_JS + "\n</body>")

    if content != original:
        open(path, "w", encoding="utf-8").write(content)
        print(f"  OK    {fname}"); updated += 1
    else:
        print(f"  SKIP  {fname} — no changes"); skipped += 1

print(f"\n  {updated} files updated, {skipped} skipped")
print("\nVerify index.html:")
print("  grep -c 'nav-hamburger { display: flex' ~/Desktop/ClaudeWork/Rich/index.html")
print("\nTest locally:")
print("  Open file:///Users/richardnashawaty/Desktop/ClaudeWork/Rich/index.html in Safari")
print("  Resize to narrow — hamburger should appear")
print("\nThen deploy:")
print('  deploy-rich "fix hamburger nav on all older pages"')
