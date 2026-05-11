import os

files = ['index.html', 'seo-web.html', 'ai-consulting.html', 'custom-tools.html', 'privacy.html', 'terms.html']
base = os.path.expanduser('~/Desktop/ClaudeWork/Rich')

# Matched to actual nav pattern in the files
old = '<a href="#contact" class="nav-cta">Let\'s Talk</a>'
new = '<a href="blog/">Blog</a>\n  <a href="#contact" class="nav-cta">Let\'s Talk</a>'

old2 = '<a href="index.html#contact" class="nav-cta">Let\'s Talk</a>'
new2 = '<a href="blog/">Blog</a>\n  <a href="index.html#contact" class="nav-cta">Let\'s Talk</a>'

updated = []
skipped = []

for fname in files:
    path = os.path.join(base, fname)
    content = open(path).read()

    if old in content:
        content = content.replace(old, new)
        open(path, 'w').write(content)
        updated.append(fname)
    elif old2 in content:
        content = content.replace(old2, new2)
        open(path, 'w').write(content)
        updated.append(fname)
    else:
        skipped.append(fname)

print(f"\n✅ Updated ({len(updated)}):")
for f in updated:
    print(f"   {f}")

if skipped:
    print(f"\n⚠️  Skipped — nav pattern not found ({len(skipped)}):")
    for f in skipped:
        print(f"   {f}")

print("\nDone. Run deploy.py when ready.")
