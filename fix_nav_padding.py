import os

files = ['index.html', 'seo-web.html', 'ai-consulting.html', 'custom-tools.html', 'privacy.html', 'terms.html']
base = os.path.expanduser('~/Desktop/ClaudeWork/Rich')

updated = []
skipped = []

for fname in files:
    path = os.path.join(base, fname)
    content = open(path).read()
    original = content

    # Reduce padding on nav links so 4 items fit
    content = content.replace(
        '.nav-links a { color: var(--text2); text-decoration: none; font-size: 0.875rem; font-weight: 500; padding: 0.4rem 0.85rem; border-radius: 6px; transition: all 0.18s; }',
        '.nav-links a { color: var(--text2); text-decoration: none; font-size: 0.875rem; font-weight: 500; padding: 0.4rem 0.5rem; border-radius: 6px; transition: all 0.18s; }'
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

print("\nDone. Run deploy.py when ready.")
