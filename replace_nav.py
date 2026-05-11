import os, re

files = ['index.html', 'seo-web.html', 'ai-consulting.html', 'custom-tools.html', 'privacy.html', 'terms.html']
base = os.path.expanduser('~/Desktop/ClaudeWork/Rich')

NEW_NAV_CSS = """  nav { position: sticky; top: 0; z-index: 100; display: flex; align-items: center; justify-content: space-between; padding: 0 2rem; height: 64px; border-bottom: 1px solid var(--border); background: rgba(24,24,22,0.82); backdrop-filter: blur(18px); -webkit-backdrop-filter: blur(18px); }
  .nav-logo { font-family: var(--serif); font-size: 1.15rem; color: var(--text); text-decoration: none; letter-spacing: -0.01em; }
  .nav-logo span { color: var(--accent); }
  .nav-links { display: flex; align-items: center; gap: 2rem; list-style: none; }
  .nav-links a { color: var(--text2); text-decoration: none; font-size: 0.88rem; font-weight: 500; transition: color 0.2s; }
  .nav-links a:hover { color: var(--text); }
  .nav-links a.active { color: var(--accent); }
  .nav-cta { background: var(--accent); color: #181816 !important; padding: 0.45rem 1.1rem; border-radius: 6px; font-weight: 600 !important; font-size: 0.85rem !important; transition: background 0.2s !important; }
  .nav-cta:hover { background: var(--accent2) !important; }"""

# Nav HTML per page — logo uses .nav-logo, links stay the same, CTA href varies
NAV_HTML = {
    'index.html': '''<nav>
    <a href="index.html" class="nav-logo">Rich Nashawaty<span>.</span></a>
    <ul class="nav-links">
      <li><a href="seo-web.html">SEO &amp; Web</a></li>
      <li><a href="ai-consulting.html">AI Consulting</a></li>
      <li><a href="custom-tools.html">Custom Tools</a></li>
      <li><a href="blog/">Blog</a></li>
    </ul>
    <a href="#contact" class="nav-cta">Let's Talk</a>
  </nav>''',
    'seo-web.html': '''<nav>
    <a href="index.html" class="nav-logo">Rich Nashawaty<span>.</span></a>
    <ul class="nav-links">
      <li><a href="seo-web.html" class="active">SEO &amp; Web</a></li>
      <li><a href="ai-consulting.html">AI Consulting</a></li>
      <li><a href="custom-tools.html">Custom Tools</a></li>
      <li><a href="blog/">Blog</a></li>
    </ul>
    <a href="index.html#contact" class="nav-cta">Let's Talk</a>
  </nav>''',
    'ai-consulting.html': '''<nav>
    <a href="index.html" class="nav-logo">Rich Nashawaty<span>.</span></a>
    <ul class="nav-links">
      <li><a href="seo-web.html">SEO &amp; Web</a></li>
      <li><a href="ai-consulting.html" class="active">AI Consulting</a></li>
      <li><a href="custom-tools.html">Custom Tools</a></li>
      <li><a href="blog/">Blog</a></li>
    </ul>
    <a href="index.html#contact" class="nav-cta">Let's Talk</a>
  </nav>''',
    'custom-tools.html': '''<nav>
    <a href="index.html" class="nav-logo">Rich Nashawaty<span>.</span></a>
    <ul class="nav-links">
      <li><a href="seo-web.html">SEO &amp; Web</a></li>
      <li><a href="ai-consulting.html">AI Consulting</a></li>
      <li><a href="custom-tools.html" class="active">Custom Tools</a></li>
      <li><a href="blog/">Blog</a></li>
    </ul>
    <a href="index.html#contact" class="nav-cta">Let's Talk</a>
  </nav>''',
    'privacy.html': '''<nav>
    <a href="index.html" class="nav-logo">Rich Nashawaty<span>.</span></a>
    <ul class="nav-links">
      <li><a href="seo-web.html">SEO &amp; Web</a></li>
      <li><a href="ai-consulting.html">AI Consulting</a></li>
      <li><a href="custom-tools.html">Custom Tools</a></li>
      <li><a href="blog/">Blog</a></li>
    </ul>
    <a href="index.html#contact" class="nav-cta">Let's Talk</a>
  </nav>''',
    'terms.html': '''<nav>
    <a href="index.html" class="nav-logo">Rich Nashawaty<span>.</span></a>
    <ul class="nav-links">
      <li><a href="seo-web.html">SEO &amp; Web</a></li>
      <li><a href="ai-consulting.html">AI Consulting</a></li>
      <li><a href="custom-tools.html">Custom Tools</a></li>
      <li><a href="blog/">Blog</a></li>
    </ul>
    <a href="index.html#contact" class="nav-cta">Let's Talk</a>
  </nav>''',
}

updated = []
skipped = []

for fname in files:
    path = os.path.join(base, fname)
    content = open(path).read()
    original = content

    # 1. Replace old nav CSS block (everything from nav { to nav-cta:hover })
    content = re.sub(
        r'  nav \{[^}]+\}.*?\.nav-cta:hover \{[^}]+\}',
        NEW_NAV_CSS,
        content,
        flags=re.DOTALL
    )

    # Also replace old .logo rules if present
    content = re.sub(r'  \.logo \{[^}]+\}\n', '', content)
    content = re.sub(r'  \.logo span \{[^}]+\}\n', '', content)

    # 2. Replace old <nav>...</nav> block
    content = re.sub(
        r'<nav>.*?</nav>',
        NAV_HTML[fname],
        content,
        count=1,
        flags=re.DOTALL
    )

    if content != original:
        open(path, 'w').write(content)
        updated.append(fname)
    else:
        skipped.append(fname)

print(f"\n✅ Updated ({len(updated)}):")
for f in updated: print(f"   {f}")

if skipped:
    print(f"\n⚠️  Skipped ({len(skipped)}):")
    for f in skipped: print(f"   {f}")

print("\nOpen locally to check, then run deploy.py.")
