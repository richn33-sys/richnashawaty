#!/usr/bin/env python3
"""
Adds a checklist CTA block to seo-web.html before the contact/CTA section.
Run: python3 ~/Desktop/ClaudeWork/Rich/add_checklist_link.py
"""

import os, re

BASE = os.path.expanduser("~/Desktop/ClaudeWork/Rich")

CHECKLIST_BLOCK = """
  <!-- FREE RESOURCE BLOCK -->
  <section style="background:var(--bg2);padding:4rem 2.5rem;">
    <div class="container">
      <div style="background:var(--bg);border:1px solid var(--border);border-left:3px solid var(--accent);border-radius:0 14px 14px 0;padding:2rem 2.5rem;display:flex;align-items:center;justify-content:space-between;gap:2rem;flex-wrap:wrap;">
        <div>
          <span style="font-family:var(--mono);font-size:0.68rem;color:var(--accent);letter-spacing:0.1em;text-transform:uppercase;display:block;margin-bottom:0.5rem;">Free Resource</span>
          <h3 style="font-family:var(--serif);font-size:1.5rem;color:var(--text);margin-bottom:0.5rem;letter-spacing:-0.01em;">2026 Technical SEO Audit Checklist</h3>
          <p style="font-size:0.92rem;color:var(--text2);line-height:1.65;max-width:480px;">65 checklist items across 7 categories — Core Web Vitals thresholds, AI visibility signals, Boston-specific local SEO, schema markup, and more. Free download.</p>
        </div>
        <a href="seo-audit-checklist.html" style="display:inline-block;background:var(--accent);color:#181816;font-weight:600;font-size:0.92rem;padding:0.75rem 1.75rem;border-radius:7px;text-decoration:none;white-space:nowrap;transition:background 0.2s;" onmouseover="this.style.background='#a8d040'" onmouseout="this.style.background='#c8f060'">Get the checklist →</a>
      </div>
    </div>
  </section>"""

path = os.path.join(BASE, "seo-web.html")
content = open(path, encoding="utf-8").read()

if "seo-audit-checklist.html" in content:
    print("  SKIP  seo-web.html — checklist link already present")
else:
    # Inject before the contact/CTA section
    if 'id="contact"' in content:
        content = content.replace('<section id="contact"', CHECKLIST_BLOCK + '\n\n  <section id="contact"', 1)
    elif '<section class="cta' in content:
        content = re.sub(r'<section class="cta', CHECKLIST_BLOCK + '\n\n  <section class="cta', content, count=1)
    else:
        content = content.replace('<footer', CHECKLIST_BLOCK + '\n\n<footer', 1)

    open(path, "w", encoding="utf-8").write(content)
    print("  OK    seo-web.html — checklist CTA block added")

print("\nDone. Deploy next:")
print('  deploy-rich "add SEO audit checklist lead magnet"')
