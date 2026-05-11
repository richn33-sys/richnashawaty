import os

files = ['index.html', 'seo-web.html', 'ai-consulting.html', 'custom-tools.html', 'privacy.html', 'terms.html']
base = os.path.expanduser('~/Desktop/ClaudeWork/Rich')

updated = []
skipped = []

for fname in files:
    path = os.path.join(base, fname)
    content = open(path).read()
    original = content

    # Fix merged </ul><a on same line — both CTA variants
    content = content.replace(
        '</ul>  <a href="#contact" class="nav-cta">Let\'s Talk</a>',
        '</ul>\n  <a href="#contact" class="nav-cta">Let\'s Talk</a>'
    )
    content = content.replace(
        '</ul>  <a href="index.html#contact" class="nav-cta">Let\'s Talk</a>',
        '</ul>\n  <a href="index.html#contact" class="nav-cta">Let\'s Talk</a>'
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
