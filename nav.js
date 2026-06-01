(function () {
  var loc = window.location.pathname;
  var isBlog = loc.indexOf('/blog/') !== -1;
  var base = isBlog ? '../' : '';

  var links = [
    { href: 'seo-web.html',           label: 'SEO \u0026 Web' },
    { href: 'local-seo-audit.html',   label: 'Local SEO Audit' },
    { href: 'ai-consulting.html',     label: 'AI Consulting' },
    { href: 'custom-tools.html',      label: 'Custom Tools' },
    { href: 'seo-ai-visibility.html', label: 'AI Visibility' },
    { href: 'blog/',                  label: 'Blog' },
    { href: 'about.html',             label: 'About' },
  ];

  function isActive(href) {
    if (href === 'blog/') return loc.indexOf('/blog') !== -1;
    return loc.indexOf(href) !== -1;
  }

  // Inject nav CSS once
  if (!document.getElementById('nav-styles')) {
    var style = document.createElement('style');
    style.id = 'nav-styles';
    style.textContent = [
      'nav{position:sticky;top:0;z-index:100;display:flex;align-items:center;justify-content:space-between;padding:0 2rem;height:64px;border-bottom:1px solid var(--border);background:rgba(24,24,22,0.82);backdrop-filter:blur(18px);-webkit-backdrop-filter:blur(18px);}',
      '.nav-logo{font-family:var(--serif);font-size:1.15rem;color:var(--text);text-decoration:none;letter-spacing:-0.01em;}',
      '.nav-logo span{color:var(--accent);}',
      '.nav-links{display:flex;align-items:center;gap:2rem;list-style:none;}',
      '.nav-links a{color:var(--text2);text-decoration:none;font-size:0.88rem;font-weight:500;transition:color 0.2s;}',
      '.nav-links a:hover{color:var(--text);}',
      '.nav-cta{background:var(--accent);color:#181816!important;padding:0.45rem 1.1rem;border-radius:6px;font-weight:600!important;font-size:0.85rem!important;transition:background 0.2s!important;}',
      '.nav-cta:hover{background:var(--accent2)!important;}',
      '.nav-hamburger{display:none;flex-direction:column;gap:5px;cursor:pointer;padding:4px;background:none;border:none;z-index:200;}',
      '.nav-hamburger span{display:block;width:22px;height:2px;background:var(--text2);border-radius:2px;transition:all 0.25s;}',
      '.nav-hamburger.open span:nth-child(1){transform:translateY(7px) rotate(45deg);}',
      '.nav-hamburger.open span:nth-child(2){opacity:0;}',
      '.nav-hamburger.open span:nth-child(3){transform:translateY(-7px) rotate(-45deg);}',
      '.nav-mobile-menu{display:none;position:fixed;top:64px;left:0;right:0;background:rgba(24,24,22,0.98);backdrop-filter:blur(18px);-webkit-backdrop-filter:blur(18px);border-bottom:1px solid var(--border);padding:1.5rem 2rem;z-index:99;flex-direction:column;gap:0;}',
      '.nav-mobile-menu.open{display:flex;}',
      '.nav-mobile-menu a{color:var(--text2);text-decoration:none;font-size:1rem;font-weight:500;padding:0.85rem 0;border-bottom:1px solid var(--border);transition:color 0.2s;}',
      '.nav-mobile-menu a:last-child{border-bottom:none;}',
      '.nav-mobile-menu a:hover{color:var(--accent);}',
      '.nav-mobile-menu .mobile-cta{color:var(--accent)!important;font-weight:600;margin-top:0.5rem;}',
      '@media(max-width:640px){.nav-hamburger{display:flex;}.nav-links{display:none;}.nav-cta{display:none;}}'
    ].join('');
    document.head.appendChild(style);
  }

  var desktopItems = links.map(function (l) {
    var active = isActive(l.href) ? ' style="color:var(--accent);"' : '';
    return '<li><a href="' + base + l.href + '"' + active + '>' + l.label + '</a></li>';
  }).join('');

  var mobileItems = links.map(function (l) {
    return '<a href="' + base + l.href + '">' + l.label + '</a>';
  }).join('');

  var logoHref = isBlog ? '../' : '/';
  var ctaHref = 'mailto:contact@richnashawaty.com';

  var navHTML =
    '<nav>' +
    '<a href="' + logoHref + '" class="nav-logo">Rich Nashawaty<span>.</span></a>' +
    '<ul class="nav-links">' + desktopItems + '</ul>' +
    '<a href="' + ctaHref + '" class="nav-cta">Let\'s Talk</a>' +
    '<button class="nav-hamburger" id="nav-hamburger" aria-label="Toggle navigation" aria-expanded="false">' +
    '<span></span><span></span><span></span>' +
    '</button>' +
    '</nav>' +
    '<div class="nav-mobile-menu" id="nav-mobile-menu">' +
    mobileItems +
    '<a href="' + ctaHref + '" class="mobile-cta">Let\'s Talk</a>' +
    '</div>';

  var placeholder = document.getElementById('nav-root');
  if (placeholder) {
    placeholder.outerHTML = navHTML;
  } else {
    document.write(navHTML);
  }
})();
