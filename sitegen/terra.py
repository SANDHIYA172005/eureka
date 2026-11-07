import re,urllib.parse as U
WA='https://wa.me/919965032227?text='+U.quote('Hello Eureka Academy, I would like to enroll. Please share the details.')
clouds=lambda fill:f'<svg class="tr-cl" viewBox="0 0 1440 120" preserveAspectRatio="none" aria-hidden="true"><path fill="{fill}" d="M0 120V70c40-30 90-30 120 0 20-40 90-45 120-5 30-35 95-30 115 10 25-40 100-40 125 0 30-35 90-30 110 5 30-40 105-40 130 0 25-30 85-25 105 5 35-40 110-35 130 5 25-30 80-25 100 5 30-40 100-35 125 0 25-35 90-30 110 0 25-30 70-25 90 0 25-30 50-20 60-10v120z"/></svg>'
star=lambda x,y,s,c,d=0:f'<svg class="tr-st" style="left:{x}%;top:{y}%;width:{s}px;animation-delay:{d}s" viewBox="0 0 24 24"><path d="M12 2l2.9 6.3 6.9.7-5.2 4.6 1.5 6.8L12 17l-6.1 3.4 1.5-6.8L2.2 9l6.9-.7z" fill="{c}"/></svg>'
# original illustration: kid riding a pencil rocket with doodles
kid='''<svg class="tr-art" viewBox="0 0 520 440" aria-hidden="true">
<circle cx="380" cy="120" r="70" fill="#FFF3C4"/><circle cx="380" cy="120" r="46" fill="#FFE08A"/>
<g class="tr-trail"><path d="M60 360 C 160 300, 260 330, 330 250" stroke="#fff" stroke-width="10" stroke-dasharray="2 22" stroke-linecap="round" fill="none"/></g>
<g class="tr-ride">
<g transform="rotate(-24 260 300)"><rect x="110" y="270" width="290" height="56" rx="10" fill="#FBBF24"/><rect x="110" y="270" width="290" height="18" rx="9" fill="#FCD34D"/><rect x="90" y="270" width="34" height="56" rx="8" fill="#F472B6"/><rect x="122" y="270" width="14" height="56" fill="#CBD5E1"/><path d="M400 270 L460 298 L400 326Z" fill="#FDE7C2"/><path d="M440 289 L460 298 L440 307Z" fill="#334155"/>
<path d="M90 286 l-40 -14 M90 298 l-52 0 M90 310 l-40 14" stroke="#F97316" stroke-width="8" stroke-linecap="round"/></g>
<path d="M205 255 q-20 50 10 70 l40 -10 q-6 -40 -10 -60z" fill="#2563EB"/>
<path d="M248 300 l34 30 -10 10 -40 -26z" fill="#2563EB"/><ellipse cx="282" cy="338" rx="16" ry="8" fill="#EF4444"/>
<path d="M200 200 q35 -15 55 10 l-6 60 q-30 10 -52 -4z" fill="#EF4444"/>
<path d="M252 214 q34 -20 56 -56" stroke="#8B5A3C" stroke-width="13" stroke-linecap="round" fill="none"/><circle cx="310" cy="154" r="10" fill="#8B5A3C"/>
<path d="M205 220 q-26 20 -12 50" stroke="#8B5A3C" stroke-width="13" stroke-linecap="round" fill="none"/>
<circle cx="230" cy="160" r="38" fill="#8B5A3C"/>
<g fill="#1F2937"><circle cx="196" cy="140" r="16"/><circle cx="214" cy="120" r="16"/><circle cx="240" cy="116" r="16"/><circle cx="262" cy="130" r="15"/><circle cx="268" cy="152" r="12"/><circle cx="192" cy="164" r="13"/></g>
<circle cx="222" cy="166" r="4.5" fill="#111"/><circle cx="246" cy="166" r="4.5" fill="#111"/><path d="M224 182 q12 10 24 0" stroke="#111" stroke-width="3.5" fill="none" stroke-linecap="round"/><circle cx="214" cy="180" r="5" fill="#F9A8D4" opacity=".7"/><circle cx="256" cy="180" r="5" fill="#F9A8D4" opacity=".7"/>
</g>
<g class="tr-doo"><text x="330" y="70" font-size="34">🚀</text><text x="440" y="210" font-size="30">🎨</text><text x="420" y="300" font-size="30">🎵</text><text x="330" y="40" font-size="24">⭐</text><text x="470" y="140" font-size="26">🧮</text><text x="350" y="380" font-size="28">📚</text></g>
</svg>'''
ring='''<svg class="tr-ring" viewBox="0 0 400 400" aria-hidden="true"><circle cx="200" cy="200" r="150" fill="#E0F2FE"/><circle cx="200" cy="200" r="110" fill="#fff" stroke="#BAE6FD" stroke-width="4" stroke-dasharray="6 10"/>'''
import math
kids=[('#8B5A3C','#1F2937','#EF4444'),('#F1C27D','#7C2D12','#22C55E'),('#C68642','#111827','#3B82F6'),('#FFDBAC','#B45309','#A855F7'),('#E0AC69','#1F2937','#F97316'),('#8D5524','#111827','#EC4899')]
for i,(skin,hair,shirt) in enumerate(kids):
    a=i*60-90; x=200+120*math.cos(math.radians(a)); y=200+120*math.sin(math.radians(a))
    ring+=f'<g class="tr-k" style="animation-delay:{i*.3}s"><line x1="200" y1="200" x2="{x:.0f}" y2="{y:.0f}" stroke="{shirt}" stroke-width="18" stroke-linecap="round"/><circle cx="{x:.0f}" cy="{y:.0f}" r="40" fill="{hair}"/><circle cx="{x:.0f}" cy="{y+5:.0f}" r="32" fill="{skin}"/><circle cx="{x-10:.0f}" cy="{y+2:.0f}" r="4" fill="#111"/><circle cx="{x+10:.0f}" cy="{y+2:.0f}" r="4" fill="#111"/><path d="M{x-10:.0f} {y+16:.0f} q10 9 20 0" stroke="#111" stroke-width="3" fill="none" stroke-linecap="round"/></g>'
ring+='<circle cx="200" cy="200" r="26" fill="#FBBF24"/><text x="200" y="210" text-anchor="middle" font-size="26">💛</text></svg>'
progs=[('💃','Western Dance','Hip-hop, freestyle & choreography','#F97316','courses/western-dance.html'),
('🪷','Classical Dance','Bharatanatyam steps, mudras & rhythm','#EC4899','courses/classical-dance.html'),
('🎤','Vocal Music','Swaras, songs & voice training','#A855F7','courses/vocal-music.html'),
('🧮','Abacus','Mental maths speed & focus','#22C55E','courses/abacus.html'),
('🎨','Drawing','Sketching, colouring & art','#3B82F6','courses/drawing.html'),
('♟️','Chess','Strategy & thinking skills','#F59E0B','courses/chess.html')]
cards=''.join(f'<a class="tr-card" href="{h}" style="--c:{c}"><div class="tr-ci"><span>{e}</span></div><div class="tr-cb"><h3>{n}</h3><p class="tr-meta">● Kids &amp; adults&nbsp;&nbsp;● Weekday &amp; weekend batches</p><p>{d}</p><span class="tr-more">Learn more</span></div></a>' for e,n,d,c,h in progs)
html=f'''<section class="tr-hero"><div class="tr-in">
<div class="tr-txt"><span class="tr-kick">Welcome to Eureka Academy &amp; S3 Dance Studio</span>
<h1>Let’s become <em>more creative</em> with Eureka</h1>
<p>Dance, music, abacus, phonics, chess, art, sports, tuition &amp; coding — 37 courses for kids and adults in Moolapalayam, Erode. <b>Admissions open now.</b></p>
<div class="tr-cta"><a class="tr-btn" href="{WA}" target="_blank" rel="noopener">Enroll now ➤</a><a class="tr-link" href="courses.html"><span>▶</span> Explore courses</a></div></div>
<div class="tr-pic">{kid}</div></div>
{star(8,18,22,'#fff',0)}{star(46,12,16,'#FDE68A',.8)}{star(52,70,20,'#fff',1.4)}
{clouds('#fff')}</section>
<section class="tr-about"><div class="tr-in"><div class="tr-pic2">{ring}</div>
<div class="tr-txt2"><span class="tr-kick o">Study · Play · Explore</span><h2>A magical place to share, learn &amp; grow</h2>
<p class="tr-lead">Eureka Academy &amp; S3 Dance Studio brings dance, music, art, skills and tuition under one roof at Guru Moorthy Doctor Building, Poondurai Road.</p>
<p>Every program has its own room and its own playful way of teaching, so children look forward to class — from first dance steps to abacus speed and board-exam tuition (3rd–12th Std).</p>
<a class="tr-btn" href="about.html">Read more</a></div></div></section>
<section class="tr-cls">{clouds('#1E3A8A').replace('tr-cl','tr-cl top')}
{star(10,14,22,'#FDE68A')}{star(30,8,14,'#fff',.6)}{star(70,10,18,'#FDE68A',1.1)}{star(90,22,14,'#fff',.4)}{star(5,60,14,'#fff',1.6)}{star(95,70,20,'#FDE68A',.9)}
<div class="tr-in col"><span class="tr-kick o">Our classes</span><h2>Happy childhood memories start here</h2><p class="tr-sub">Pick a program — every class opens in its own page with timings and what kids learn.</p>
<div class="tr-grid">{cards}</div><a class="tr-btn" href="courses.html">See all 37 courses</a></div></section>'''
h=open('/home/claude/site/index.html').read()
h=re.sub(r'<section class="kb">.*?</section>',lambda m:html,h,count=1,flags=re.S)
open('/home/claude/site/index.html','w').write(h); print('ok')
