import os

files = ['index.html', 'seo-web.html', 'ai-consulting.html', 'custom-tools.html', 'privacy.html', 'terms.html']
base = os.path.expanduser('~/Desktop/ClaudeWork/Rich')

updated = []
skipped = []

for fname in files:
    path = os.path.join(base, fname)
    content = open(path).read()
    original = content

    # Fix nav: remove space-between, group logo+links together on left, CTA on right
    content = content.replace(
        'nav { position: fixed; top: 0; left: 0; right: 0; z-index: 100; padding: 1.25rem 2.5rem; display: flex; align-items: center; justify-content: space-between; background: rgba(24,24,22,0.90); backdrop-filter: blur(18px); border-bottom: 1px solid var(--border); }',
        'nav { position: fixed; top: 0; left: 0; right: 0; z-index: 100; padding: 0 2.5rem; height: 64px; display: flex; align-items: center; gap: 2rem; background: rgba(24,24,22,0.90); backdrop-filter: blur(18px); border-bottom: 1px solid var(--border); } nav .nav-cta { margin-left: auto; }'
    )

    # Restore gap on nav-links
    content = content.replace(
        '.nav-links { display: flex; gap: 0rem; list-style: none; }',
        '.nav-links { display: flex; gap: 0.25rem; list-style: none; }'
    )

    # Restore padding on nav links
    content = content.replace(
        '.nav-links a { color: var(--text2); text-decoration: none; font-size: 0.875rem; font-weight: 500; padding: 0.4rem 0.5rem; border-radius: 6px; transition: all 0.18s; }',
        '.nav-links a { color: var(--text2); text-decoration: none; font-size: 0.875rem; font-weight: 500; padding: 0.4rem 0.75rem; border-radius: 6px; transition: all 0.18s; }'
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

print("\nDone. Check locally then run deploy.py.")
