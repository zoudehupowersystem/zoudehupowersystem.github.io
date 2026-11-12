/* Theme preference shared with the Chinese and English homepages. */
(function () {
  'use strict';
  var button = document.getElementById('theme-toggle');
  if (!button) return;
  var root = document.documentElement;
  var icon = button.querySelector('.theme-toggle-icon');
  var label = button.querySelector('.theme-toggle-text');
  var themeMeta = document.querySelector('meta[name="theme-color"]');
  var english = (root.getAttribute('lang') || '').toLowerCase().indexOf('en') === 0;
  function refresh() {
    var dark = root.getAttribute('data-theme') === 'dark';
    button.setAttribute('aria-pressed', dark ? 'true' : 'false');
    button.setAttribute('aria-label', dark ? (english ? 'Switch to light mode' : '切换为浅色模式') : (english ? 'Switch to dark mode' : '切换为深色模式'));
    if (icon) icon.textContent = dark ? '☀' : '☾';
    if (label) label.textContent = dark ? (english ? 'Light mode' : '浅色模式') : (english ? 'Dark mode' : '深色模式');
    if (themeMeta) themeMeta.setAttribute('content', dark ? '#0B1220' : '#FFFFFF');
  }
  button.addEventListener('click', function () {
    var next = root.getAttribute('data-theme') === 'dark' ? 'light' : 'dark';
    root.setAttribute('data-theme', next);
    try { localStorage.setItem('dehu-homepage-theme', next); } catch (error) {}
    refresh();
  });
  refresh();
})();
