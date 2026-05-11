import os, re

files = ['index.html', 'seo-web.html', 'ai-consulting.html', 'custom-tools.html', 'privacy.html', 'terms.html']
base = os.path.expanduser('~/Desktop/ClaudeWork/Rich')

updated = []
skipped = []

for fname in files:
    path = os.path.join(base, fname)
    content = open(path).read()
    original = content

    # Remove all injected blog links (may be doubled)
    content = re.sub(r'\s*<a href="blog/">Blog</a>\n?', '', content)
    content = re.sub(r'\s*<a href="\.\.\/blog\/">Blog</a>\n?', '', content)

    # Now insert cleanly inside the ul, before Let's Talk
    # Two patterns depending on page
    for old, new in [
        (
            '<li><a href="custom-tools.html">Custom Tools</a></li>\n  </ul>',
            '<li><a href="custom-tools.html">Custom Tools</a></li>\n    <li><a href="blog/">Blog</a></li>\n  </ul>'
        ),
        (
            '<li><a href="../custom-tools.html">Custom Tools</a></li>\n  </ul>',
            '<li><a href="../custom-tools.html">Custom Tools</a></li>\n    <li><a href="../blog/">Blog</a></li>\n  </ul>'
        ),
    ]:
        if old in content:
            content = content.replace(old, new)
            break

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
