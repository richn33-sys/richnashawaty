import os

files = ['index.html', 'seo-web.html', 'ai-consulting.html', 'custom-tools.html', 'privacy.html', 'terms.html']
base = os.path.expanduser('~/Desktop/ClaudeWork/Rich')

updated = []
skipped = []

for fname in files:
    path = os.path.join(base, fname)
    content = open(path).read()
    original = content

    # Reduce gap so all 4 nav items fit
    content = content.replace(
        '.nav-links { display: flex; gap: 0.25rem; list-style: none; }',
        '.nav-links { display: flex; gap: 0rem; list-style: none; }'
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
