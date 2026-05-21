#!/usr/bin/env python3
"""
Adds hamburger menu for mobile nav across all pages.
Run: python3 ~/Desktop/ClaudeWork/Rich/add_hamburger.py
"""

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

# CSS to add — replaces the hide-all mobile rule
OLD_MOBILE_NAV_CSS = ".nav-links li:not(:last-child) { display: none; }"

NEW_MOBILE_NAV_CSS = """.nav-hamburger {
      display: none;
      flex-direction: column;
      gap: 5px;
      cursor: pointer;
      padding: 4px;
      background: none;
      border: none;
      z-index: 200;
    }
    .nav-hamburger span {
      display: block;
      width: 22px;
      height: 2px;
      background: var(--text2);
      border-radius: 2px;
      transition: all 0.25s;
    }
    .nav-hamburger.open span:nth-child(1) { transform: translateY(7px) rotate(45deg); }
    .nav-hamburger.open span:nth-child(2) { opacity: 0; }
    .nav-hamburger.open span:nth-child(3) { transform: translateY(-7px) rotate(-45deg); }
    .nav-mobile-menu {
      display: none;
      position: fixed;
      top: 64px;
      left: 0;
      right: 0;
      background: rgba(24,24,22,0.98);
      backdrop-filter: blur(18px);
      -webkit-backdrop-filter: blur(18px);
      border-bottom: 1px solid var(--border);
      padding: 1.5rem 2rem;
      z-index: 99;
      flex-direction: column;
      gap: 0;
    }
    .nav-mobile-menu.open { display: flex; }
    .nav-mobile-menu a {
      color: var(--text2);
      text-decoration: none;
      font-size: 1rem;
      font-weight: 500;
      padding: 0.85rem 0;
      border-bottom: 1px solid var(--border);
      transition: color 0.2s;
    }
    .nav-mobile-menu a:last-child { border-bottom: none; }
    .nav-mobile-menu a:hover { color: var(--accent); }
    .nav-mobile-menu .mobile-cta {
      color: var(--accent) !important;
      font-weight: 600;
      margin-top: 0.5rem;
    }"""

# Hamburger button HTML — inserted before closing </nav>
HAMBURGER_BTN = """
  <button class="nav-hamburger" id="nav-hamburger" aria-label="Toggle navigation" aria-expanded="false">
    <span></span>
    <span></span>
    <span></span>
  </button>"""

# JS to add before </body>
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
    // Close on link click
    menu.querySelectorAll('a').forEach(function(a) {
      a.addEventListener('click', function() {
        menu.classList.remove('open');
        btn.classList.remove('open');
        btn.setAttribute('aria-expanded', false);
      });
    });
  })();
</script>"""

updated = 0
skipped = 0

for fname in ALL_FILES:
    path = os.path.join(BASE, fname)
    is_blog = fname.startswith("blog/")

    if not os.path.exists(path):
        print(f"  SKIP  {fname} — not found"); skipped += 1; continue

    content = open(path, encoding="utf-8").read()

    if 'nav-hamburger' in content:
        print(f"  SKIP  {fname} — hamburger already present"); skipped += 1; continue

    original = content

    # 1. Replace mobile nav hide rule with hamburger CSS
    if OLD_MOBILE_NAV_CSS in content:
        content = content.replace(OLD_MOBILE_NAV_CSS, NEW_MOBILE_NAV_CSS)
    else:
        # Fallback — inject before </style>
        content = content.replace("</style>", NEW_MOBILE_NAV_CSS + "\n  </style>", 1)

    # 2. Show hamburger button on mobile — add display:flex rule
    content = content.replace(
        ".nav-hamburger {",
        ".nav-hamburger {"
    )

    # 3. Add @media rule to show hamburger button
    MEDIA_RULE = """
    @media (max-width: 640px) {
      .nav-hamburger { display: flex; }
      .nav-links { display: none; }
      .nav-cta { display: none; }
    }"""

    # inject before </style>
    content = content.replace("</style>", MEDIA_RULE + "\n  </style>", 1)

    # 4. Add hamburger button before </nav>
    content = content.replace("</nav>", HAMBURGER_BTN + "\n</nav>", 1)

    # 5. Build mobile menu based on page location
    if is_blog:
        MOBILE_MENU = """
<div class="nav-mobile-menu" id="nav-mobile-menu">
  <a href="../seo-web.html">SEO &amp; Web</a>
  <a href="../ai-consulting.html">AI Consulting</a>
  <a href="../custom-tools.html">Custom Tools</a>
  <a href="../blog/">Blog</a>
  <a href="../about.html">About</a>
  <a href="mailto:contact@richnashawaty.com" class="mobile-cta">Let's Talk</a>
</div>"""
    else:
        MOBILE_MENU = """
<div class="nav-mobile-menu" id="nav-mobile-menu">
  <a href="seo-web.html">SEO &amp; Web</a>
  <a href="ai-consulting.html">AI Consulting</a>
  <a href="custom-tools.html">Custom Tools</a>
  <a href="blog/">Blog</a>
  <a href="about.html">About</a>
  <a href="#contact" class="mobile-cta">Let's Talk</a>
</div>"""

    # Insert mobile menu after </nav>
    content = content.replace("</nav>", "</nav>" + MOBILE_MENU, 1)

    # 6. Add JS before </body>
    content = content.replace("</body>", HAMBURGER_JS + "\n</body>")

    if content != original:
        open(path, "w", encoding="utf-8").write(content)
        print(f"  OK    {fname}"); updated += 1
    else:
        print(f"  WARN  {fname} — no changes made"); skipped += 1

print(f"\n  {updated} files updated, {skipped} skipped")
print("\nDone. Deploy next:")
print('  python3 ~/Desktop/ClaudeWork/Rich/deploy.py "add hamburger menu for mobile nav"')
