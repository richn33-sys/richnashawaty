#!/usr/bin/env python3
"""
Precise fix — moves hamburger CSS inside </style> and adds correct 640px show rule.
Run: python3 ~/Desktop/ClaudeWork/Rich/fix_hamburger2.py
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

# The misplaced CSS block to find and remove from outside </style>
MISPLACED_CSS = """.nav-hamburger {
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

# Clean CSS to inject properly before </style>
CLEAN_CSS = """
  /* HAMBURGER NAV */
  .nav-hamburger {
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
  .nav-mobile-menu .mobile-cta { color: var(--accent) !important; font-weight: 600; margin-top: 0.5rem; }
  @media (max-width: 640px) {
    .nav-hamburger { display: flex; }
    .nav-links { display: none !important; }
    .nav-cta { display: none !important; }
  }"""

updated = 0
skipped = 0

for fname in ALL_FILES:
    path = os.path.join(BASE, fname)
    if not os.path.exists(path):
        print(f"  SKIP  {fname} — not found"); skipped += 1; continue

    content = open(path, encoding="utf-8").read()
    original = content

    # Step 1: Remove the misplaced CSS block (outside </style>)
    content = content.replace(MISPLACED_CSS, "")

    # Step 2: Inject clean CSS properly before first </style>
    if "HAMBURGER NAV" not in content:
        content = content.replace("</style>", CLEAN_CSS + "\n</style>", 1)

    if content != original:
        open(path, "w", encoding="utf-8").write(content)
        print(f"  OK    {fname}"); updated += 1
    else:
        print(f"  SKIP  {fname} — no changes"); skipped += 1

print(f"\n  {updated} files updated, {skipped} skipped")
print("\nDone. Deploy next:")
print('  python3 ~/Desktop/ClaudeWork/Rich/deploy.py "fix hamburger CSS placement"')
