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
