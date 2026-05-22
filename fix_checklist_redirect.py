#!/usr/bin/env python3
"""
Replaces Formspree _next redirect with JS-based redirect on checklist landing page.
Run: python3 ~/Desktop/ClaudeWork/Rich/fix_checklist_redirect.py
"""

import os

BASE = os.path.expanduser("~/Desktop/ClaudeWork/Rich")
path = os.path.join(BASE, "seo-audit-checklist.html")

content = open(path, encoding="utf-8").read()

# Remove the _next hidden field
content = content.replace(
    '        <input type="hidden" name="_next" value="https://richnashawaty.com/seo-audit-checklist-full.html">\n',
    ''
)

# Replace form tag with one that has an id, remove action/method
OLD_FORM = '<form action="https://formspree.io/f/mrejawnb" method="POST">'
NEW_FORM = '<form id="checklist-form">'
content = content.replace(OLD_FORM, NEW_FORM)

# Replace submit button with one that shows loading state
OLD_BTN = '        <button type="submit" class="form-submit">Send me the checklist →</button>'
NEW_BTN = '        <button type="submit" class="form-submit" id="submit-btn">Send me the checklist →</button>'
content = content.replace(OLD_BTN, NEW_BTN)

# Add JS before </body>
JS = """
<script>
  document.getElementById('checklist-form').addEventListener('submit', function(e) {
    e.preventDefault();
    var btn = document.getElementById('submit-btn');
    btn.textContent = 'Sending...';
    btn.disabled = true;

    var data = new FormData(this);

    fetch('https://formspree.io/f/mrejawnb', {
      method: 'POST',
      body: data,
      headers: { 'Accept': 'application/json' }
    })
    .then(function(res) {
      if (res.ok) {
        window.location.href = 'seo-audit-checklist-full.html';
      } else {
        btn.textContent = 'Something went wrong — try again';
        btn.disabled = false;
      }
    })
    .catch(function() {
      btn.textContent = 'Something went wrong — try again';
      btn.disabled = false;
    });
  });
</script>"""

content = content.replace("</body>", JS + "\n</body>")

open(path, "w", encoding="utf-8").write(content)
print("  OK    seo-audit-checklist.html — JS redirect added")
print("\nDeploy next:")
print('  deploy-rich "fix checklist form redirect"')
