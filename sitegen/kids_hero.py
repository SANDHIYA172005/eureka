import re,urllib.parse as U
WA='https://wa.me/919965032227?text='+U.quote('Hello Eureka Academy, I would like to enroll. Please share the details.')
cloud='M60 20 C 80 0,120 0,135 22 C 160 10,195 25,195 55 C 220 65,222 105,198 118 C 205 150,175 170,148 160 C 135 185,95 188,80 168 C 55 182,20 168,22 140 C -2 128,-2 90,22 80 C 12 50,35 22,60 20Z'
def frame(cls,bg,emo,lab,c,extra=''):
    return f'''<a class="cf {cls}" href="{lab[1]}" aria-label="{lab[0]}"><svg viewBox="-5 -5 230 200" aria-hidden="true"><defs><clipPath id="cp-{cls}"><path d="{cloud}"/></clipPath><linearGradient id="g-{cls}" x1="0" y1="0" x2="1" y2="1">{bg}</linearGradient></defs>
<path d="{cloud}" fill="#fff" transform="translate(-4 -4) scale(1.04)"/><g clip-path="url(#cp-{cls})"><rect x="-10" y="-10" width="240" height="210" fill="url(#g-{cls})"/>{extra}</g></svg><span class="cf-e">{emo}</span><span class="cf-l" style="--c:{c}">{lab[0]}</span></a>'''
G=lambda a,b:f'<stop offset="0" stop-color="{a}"/><stop offset="1" stop-color="{b}"/>'
dots='<circle cx="40" cy="40" r="6" fill="#fff6"/><circle cx="170" cy="60" r="9" fill="#fff5"/><circle cx="150" cy="150" r="7" fill="#fff4"/>'
F=[frame('f1',G('#FDE68A','#FB923C'),'💃',('Western Dance','courses/western-dance.html'),'#F97316',dots),
 frame('f2',G('#BFDBFE','#818CF8'),'🧮',('Abacus','courses/abacus.html'),'#4F46E5',dots),
 frame('f3',G('#BBF7D0','#34D399'),'🎨',('Drawing','courses/drawing.html'),'#059669',dots),
 frame('f4',G('#FBCFE8','#F472B6'),'🥋',('Karate','courses/karate.html'),'#DB2777',dots)]
title=''.join(f'<span style="--c:{c};--d:{i*.06:.2f}s">{ch}</span>' for i,(ch,c) in enumerate(zip('Eureka',['#F97316','#22C55E','#3B82F6','#A855F7','#EC4899','#F59E0B'])))
balloon=lambda c,x,y,s,d:f'<svg class="bln" style="left:{x}%;top:{y}%;width:{s}px;animation-delay:{d}s" viewBox="0 0 60 110" aria-hidden="true"><path d="M30 70 C 34 85 24 95 32 110" stroke="#94A3B8" stroke-width="1.5" fill="none"/><ellipse cx="30" cy="34" rx="26" ry="32" fill="{c}"/><path d="M26 66 l4 6 4-6z" fill="{c}"/><circle cx="20" cy="22" r="4" fill="#fff9"/><circle cx="36" cy="18" r="3" fill="#fff9"/><circle cx="32" cy="38" r="4" fill="#fff9"/></svg>'
stars=''.join(f'<svg class="stx" style="left:{x}%;top:{y}%;width:{s}px;animation-delay:{d}s" viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2l2.9 6.3 6.9.7-5.2 4.6 1.5 6.8L12 17l-6.1 3.4 1.5-6.8L2.2 9l6.9-.7z" fill="{c}"/></svg>' for x,y,s,c,d in [(21,8,34,'#A78BFA',0),(57,6,26,'#FACC15',.6),(93,22,26,'#F472B6',1.2),(30,82,18,'#FACC15',.3),(74,74,16,'#8B5CF6',1.6),(65,24,14,'#60A5FA',.9)])
toys='''<div class="toys" aria-hidden="true">
<svg class="ty t1" viewBox="0 0 100 100"><circle cx="50" cy="62" r="30" fill="#C08457"/><circle cx="26" cy="30" r="13" fill="#C08457"/><circle cx="74" cy="30" r="13" fill="#C08457"/><circle cx="26" cy="30" r="6" fill="#E9C29A"/><circle cx="74" cy="30" r="6" fill="#E9C29A"/><circle cx="50" cy="44" r="24" fill="#D29B67"/><ellipse cx="50" cy="52" rx="10" ry="8" fill="#F1D3AE"/><circle cx="42" cy="40" r="3" fill="#3B2410"/><circle cx="58" cy="40" r="3" fill="#3B2410"/><circle cx="50" cy="49" r="3" fill="#3B2410"/><path d="M38 66 l12 6 12-6 -12 -4z" fill="#EF4444"/></svg>
<svg class="ty t2" viewBox="0 0 80 110"><rect x="37" y="10" width="6" height="90" rx="3" fill="#F59E0B"/><ellipse cx="40" cy="96" rx="34" ry="10" fill="#22C55E"/><ellipse cx="40" cy="80" rx="28" ry="9" fill="#3B82F6"/><ellipse cx="40" cy="65" rx="23" ry="8" fill="#FACC15"/><ellipse cx="40" cy="51" rx="18" ry="7" fill="#F97316"/><ellipse cx="40" cy="38" rx="13" ry="6" fill="#EC4899"/><circle cx="40" cy="22" r="10" fill="#A855F7"/></svg>
<svg class="ty t3" viewBox="0 0 120 115"><path d="M60 4l16 34 37 4-28 25 8 37-33-19-33 19 8-37L7 42l37-4z" fill="#FFC83D" stroke="#F59E0B" stroke-width="4" stroke-linejoin="round"/><circle cx="48" cy="56" r="5" fill="#3B2410"/><circle cx="72" cy="56" r="5" fill="#3B2410"/><path d="M50 70 q10 8 20 0" stroke="#3B2410" stroke-width="4" fill="none" stroke-linecap="round"/></svg>
<svg class="ty t4" viewBox="0 0 120 110"><rect x="6" y="54" width="50" height="50" rx="8" fill="#FDBA74"/><text x="31" y="92" text-anchor="middle" font-size="34" font-weight="800" fill="#fff" font-family="Poppins,sans-serif">A</text><rect x="62" y="54" width="50" height="50" rx="8" fill="#F9A8D4"/><text x="87" y="92" text-anchor="middle" font-size="34" font-weight="800" fill="#fff" font-family="Poppins,sans-serif">C</text><rect x="34" y="2" width="50" height="50" rx="8" fill="#A78BFA"/><text x="59" y="40" text-anchor="middle" font-size="34" font-weight="800" fill="#fff" font-family="Poppins,sans-serif">B</text></svg>
<svg class="ty t5" viewBox="0 0 160 100"><rect x="20" y="40" width="70" height="36" rx="6" fill="#EF4444"/><rect x="70" y="14" width="44" height="62" rx="6" fill="#3B82F6"/><rect x="78" y="22" width="28" height="20" rx="4" fill="#BFDBFE"/><rect x="30" y="20" width="14" height="22" rx="3" fill="#1F2937"/><rect x="110" y="48" width="30" height="28" rx="5" fill="#FACC15"/><circle cx="38" cy="82" r="12" fill="#1F2937"/><circle cx="78" cy="82" r="12" fill="#1F2937"/><circle cx="122" cy="82" r="10" fill="#1F2937"/><circle cx="38" cy="82" r="5" fill="#22C55E"/><circle cx="78" cy="82" r="5" fill="#22C55E"/><circle cx="122" cy="82" r="4" fill="#22C55E"/></svg>
<svg class="ty t6" viewBox="0 0 120 110"><rect x="10" y="92" width="100" height="14" rx="7" fill="#F472B6"/><path d="M24 92 C 24 20, 60 20, 60 60 S 96 10, 96 92" stroke="#60A5FA" stroke-width="4" fill="none"/><path d="M40 92 C 40 40, 80 40, 80 92" stroke="#F59E0B" stroke-width="4" fill="none"/><circle cx="30" cy="50" r="7" fill="#EF4444"/><circle cx="62" cy="58" r="7" fill="#22C55E"/><circle cx="88" cy="40" r="7" fill="#A855F7"/><circle cx="50" cy="62" r="7" fill="#FACC15"/><circle cx="76" cy="70" r="7" fill="#3B82F6"/></svg>
<span class="ball b1"></span><span class="ball b2"></span></div>'''
rainbow=''.join(f'<path d="M{20+i*16} 160 A {130-i*16} {130-i*16} 0 0 1 {280-i*16} 160" stroke="{c}"/>' for i,c in enumerate(['#F87171','#FB923C','#FACC15','#4ADE80','#60A5FA','#A78BFA']))
hero=f'''<section class="kb"><div class="kb-bg" aria-hidden="true"><svg class="rb" viewBox="0 0 300 160"><g fill="none" stroke-width="16" stroke-linecap="round">{rainbow}</g></svg>
<svg class="cl1" viewBox="0 0 120 60"><path d="M20 55a18 18 0 0 1 2-36 24 24 0 0 1 44-6 20 20 0 0 1 36 9 16 16 0 0 1 4 33z" fill="#fff"/></svg>
{balloon('#F472B6',60,6,62,0)}{balloon('#60A5FA',65.5,10,56,.8)}{balloon('#FACC15',61.5,22,52,1.6)}{stars}
<svg class="plane" viewBox="0 0 80 50"><path d="M2 24 78 2 52 46 38 30z" fill="#fff" stroke="#F87171" stroke-width="2.5" stroke-linejoin="round"/><path d="M38 30 78 2" stroke="#F87171" stroke-width="2"/></svg>
<svg class="dash d1" viewBox="0 0 200 120"><path d="M10 110 C 60 10, 140 130, 190 20" fill="none" stroke="#FDBA74" stroke-width="2.5" stroke-dasharray="6 8"/></svg></div>
<div class="kb-in">
<div class="kb-side l">{F[0]}{F[1]}</div>
<div class="kb-c">
<a class="kb-logo" href="index.html"><img src="assets/logo.png" alt="Eureka Academy logo" width="64" height="64"><span><b>EUREKA ACADEMY</b><small>&amp; S3 Dance Studio · Moolapalayam</small></span></a>
<h1 class="kb-h"><span class="kb-t1">{title}</span><span class="kb-t2">Learn <i>·</i> Dance <i>·</i> Shine</span></h1>
<div class="kb-rib"><span>✦ Admissions Open Now ✦</span></div>
<p class="kb-sub">37 courses for kids &amp; adults: dance, music, abacus, phonics, chess, art, sports, tuition &amp; coding.</p>
<div class="kb-cta"><a class="kb-btn" href="{WA}" target="_blank" rel="noopener">ENROLL NOW</a><a class="kb-btn2" href="courses.html">Explore courses →</a></div>
</div>
<div class="kb-side r">{F[2]}{F[3]}</div>
</div>{toys}
<svg class="kb-wave" viewBox="0 0 1440 120" preserveAspectRatio="none" aria-hidden="true"><path d="M0 60 C 200 20, 360 100, 560 70 S 900 10, 1100 60 S 1360 90, 1440 50 V120 H0Z" fill="#FDE7B0"/><path d="M0 90 C 260 60, 520 120, 780 90 S 1240 60, 1440 90 V120 H0Z" fill="#BAE6FD"/></svg></section>'''
h=open('index.html').read()
h=re.sub(r'<section class="hx2">.*?</section>',lambda m:hero,h,count=1,flags=re.S)
h=re.sub(r"<script>\(function\(\)\{var T=\[\]\.slice\.call\(document\.querySelectorAll\('\.hx2-tabs.*?</script>",'',h,flags=re.S)
if 'Fredoka' not in h:
    h=h.replace('<link rel="stylesheet" href="assets/site.css">','<link href="https://fonts.googleapis.com/css2?family=Fredoka:wght@500;600;700&display=swap" rel="stylesheet"><link rel="stylesheet" href="assets/site.css">',1)
open('index.html','w').write(h); print('ok', 'hx2' in h, 'class="kb"' in h)
