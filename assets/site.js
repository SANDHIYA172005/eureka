(function(){var m=document.getElementById('mb');if(m&&m.parentNode!==document.body)document.body.appendChild(m)})();
(function () {
  // Always open pages at the top
  if ('scrollRestoration' in history) history.scrollRestoration = 'manual';
  var toTop = function () { window.scrollTo(0, 0); };
  toTop(); addEventListener('DOMContentLoaded', toTop); addEventListener('load', function () { setTimeout(toTop, 0); });
  addEventListener('pageshow', function (e) { if (e.persisted) toTop(); });
  var hd = document.getElementById('hd');
  addEventListener('scroll', function () { hd.classList.toggle('sc', scrollY > 4); }, { passive: true });

  // mobile menu
  var t = document.getElementById('mbT'), m = document.getElementById('mb');
  if (t) t.addEventListener('click', function () {
    var o = m.classList.toggle('open'); t.setAttribute('aria-expanded', o);
    document.body.style.overflow = o ? 'hidden' : '';
  });
  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape' && m.classList.contains('open')) { m.classList.remove('open'); t.setAttribute('aria-expanded', false); document.body.style.overflow = ''; t.focus(); }
  });

  document.querySelectorAll('.yr').forEach(function (y) { y.textContent = new Date().getFullYear(); });

  // reveal
  var io = 'IntersectionObserver' in window ? new IntersectionObserver(function (es) {
    es.forEach(function (x) { if (x.isIntersecting) { x.target.classList.add('in'); io.unobserve(x.target); } });
  }, { threshold: .08 }) : null;
  document.querySelectorAll('.sec .g3, .sec .g4, .sec .split, .sec .g-2, .band, .cat').forEach(function (el) {
    el.classList.add('rv'); if (io) io.observe(el); else el.classList.add('in');
  });

  // courses: filter + search
  var q = document.getElementById('q');
  if (q) {
    var seg = document.querySelectorAll('.seg button'), cats = document.querySelectorAll('.cat'), cnt = document.getElementById('cnt'), empty = document.getElementById('empty'), f = 'all';
    var fromHash = location.hash.slice(1); if (['kids', 'adults', 'code-crackers'].indexOf(fromHash) > -1) f = fromHash;
    function run() {
      var term = q.value.trim().toLowerCase(), n = 0;
      seg.forEach(function (b) { b.setAttribute('aria-pressed', b.dataset.f === f); });
      cats.forEach(function (c) {
        var vis = 0; var show = f === 'all' || c.dataset.catId === f;
        c.querySelectorAll('.cc').forEach(function (k) { var ok = show && (!term || term.split(/\s+/).every(function (w) { return k.dataset.q.indexOf(w) > -1; })); k.hidden = !ok; if (ok) vis++; });
        c.hidden = vis === 0; n += vis;
      });
      cnt.textContent = n + (n === 1 ? ' course' : ' courses'); empty.hidden = n > 0;
    }
    seg.forEach(function (b) { b.addEventListener('click', function () { f = b.dataset.f; history.replaceState(null, '', f === 'all' ? location.pathname : '#' + f); run(); }); });
    q.addEventListener('input', run); run();
    
  }

  // faq search
  var fq = document.getElementById('fq');
  if (fq) fq.addEventListener('input', function () {
    var term = fq.value.trim().toLowerCase(), n = 0;
    document.querySelectorAll('.faq-g').forEach(function (g) {
      var v = 0; g.querySelectorAll('details').forEach(function (d) { var ok = !term || d.textContent.toLowerCase().indexOf(term) > -1; d.hidden = !ok; if (ok) v++; });
      g.hidden = v === 0; n += v;
    });
    document.getElementById('fempty').hidden = n > 0;
  });

  // contact form -> WhatsApp
  var form = document.getElementById('enq');
  if (form) {
    var p = new URLSearchParams(location.search).get('course'); if (p) document.getElementById('fc').value = p;
    var PH = /^(?:\+91[\s-]?|91[\s-]?|0)?[6-9]\d{4}[\s-]?\d{5}$/;
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var v = function (id) { return document.getElementById(id).value.trim(); }, ok = true;
      var set = function (fid, eid, msg) { document.getElementById(eid).textContent = msg; document.getElementById(fid).classList.toggle('bad', !!msg); if (msg && ok) { ok = false; document.getElementById(fid).focus(); } };
      set('fn', 'en', v('fn').length < 2 ? 'Please enter your name' : '');
      set('fp', 'ep', PH.test(v('fp')) ? '' : 'Enter a valid 10-digit mobile number');
      set('fc', 'ec', v('fc') ? '' : 'Please choose a course');
      if (!ok) return;
      var msg = 'Hello Eureka Academy! I would like to enquire about ' + v('fc') + '.\nName: ' + v('fn') + '\nPhone: ' + v('fp') + (v('fa') ? '\nLearner: ' + v('fa') : '') + (v('fm') ? '\nMessage: ' + v('fm') : '');
      var a = document.getElementById('wl'); a.href = 'https://wa.me/919965032227?text=' + encodeURIComponent(msg); a.click();
    });
  }
})();
document.addEventListener('click',function(e){var a=e.target.closest('a[href^="#"]');if(!a)return;var id=a.getAttribute('href').slice(1);var el=id&&document.getElementById(id);if(el){e.preventDefault();scrollTo({top:el.getBoundingClientRect().top+scrollY-90,behavior:'smooth'})}});

/* Enquire contact card */
(function(){
  var html='<div class="eq-bg" id="eqM" hidden><div class="eq-c" role="dialog" aria-modal="true" aria-labelledby="eqT">'+
  '<button class="eq-x" aria-label="Close">×</button><p class="eq-k">Admissions &amp; enquiry</p><h3 id="eqT">Contact Eureka Academy</h3>'+
  '<p class="eq-s">Call us or visit the academy directly. All sessions available online &amp; offline.</p>'+
  '<div class="eq-b"><a class="eq-call" href="tel:+919965032227"><span></span><b>Call us</b><small>+91 99650 32227</small></a>'+
  '<a class="eq-wa" href="https://wa.me/919965032227?text=Hello%20Eureka%20Academy%2C%20I%20would%20like%20to%20enquire." target="_blank" rel="noopener"><span>💬</span><b>WhatsApp</b><small>99650 32227</small></a></div>'+
  '<ul class="eq-l"><li><span>📍</span><div><b>Guru Moorthy Doctor Building</b><small>Moolapalayam, Poondurai Road, Erode – 638002</small><a href="https://maps.app.goo.gl/d6kSKBfJiE24eaty6" target="_blank" rel="noopener">Get directions →</a></div></li>'+
  '<li><span>🕔</span><div><b>Mon – Sat · 5:00 – 8:00 pm</b><small>Sunday · 10:30 am – 12:00 pm</small></div></li></ul>'+
  '<div class="eq-so"><a href="https://www.instagram.com/eurekaacademy_s3dancestudio" target="_blank" rel="noopener">Instagram</a><a href="https://www.facebook.com/share/1CvqzwCpfR/" target="_blank" rel="noopener">Facebook</a></div></div></div>';
  document.body.insertAdjacentHTML('beforeend',html);
  var m=document.getElementById('eqM'),last;
  function open(e){e.preventDefault();last=document.activeElement;m.hidden=false;document.body.style.overflow='hidden';m.querySelector('.eq-x').focus();var mb=document.getElementById('mb');if(mb)mb.classList.remove('open')}
  function close(){m.hidden=true;document.body.style.overflow='';if(last)last.focus()}
  document.querySelectorAll('[data-enq]').forEach(function(b){b.addEventListener('click',open)});
  m.addEventListener('click',function(e){if(e.target===m||e.target.classList.contains('eq-x'))close()});
  document.addEventListener('keydown',function(e){if(e.key==='Escape'&&!m.hidden)close()});
})();

/* mobile header polish */
(function(){
  var t=document.getElementById('mbT');if(!t)return;
  t.innerHTML='<span class="hb"><i></i><i></i><i></i></span>';
  var c=document.createElement('a');c.className='hd-call';c.href='tel:+919965032227';c.setAttribute('aria-label','Call Eureka Academy');
  c.innerHTML='<svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1.9.4 1.8.7 2.7a2 2 0 0 1-.5 2.1L8 9.8a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.7.7a2 2 0 0 1 1.7 2z"/></svg>';
  t.parentNode.insertBefore(c,t);
  var h=document.getElementById('hd');function s(){h&&h.classList.toggle('sc2',scrollY>8)}addEventListener('scroll',s,{passive:true});s();
})();
(function(){var f=document.querySelector('.nf'),b=document.querySelector('.fab');if(!f||!b||!('IntersectionObserver'in window))return;new IntersectionObserver(function(e){b.classList.toggle('fab-off',e[0].isIntersecting)}).observe(f)})();
