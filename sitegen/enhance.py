import re,urllib.parse as U
WA='https://wa.me/919965032227?text='+U.quote('Hello Eureka Academy, I would like to know about admissions.')
p='/home/claude/site/index.html'; h=open(p).read()

# 1. headline: rotating highlighted word
h=h.replace('<h1>Learn, dance and grow,<b>',
 '<h1>Learn, <span class="rw" aria-label="dance"><span class="rw-i"><i>dance</i><i>sing</i><i>draw</i><i>code</i><i>dance</i></span></span> and grow,<b>',1)

# 2. course chips under CTA
chips=[('💃','western-dance'),('🎤','vocal-music'),('🧮','abacus'),('♟️','chess'),('🎨','drawing'),('🥋','karate')]
chip=''.join(f'<a href="courses/{s}.html" style="--d:{i*.08:.2f}s">{e}</a>' for i,(e,s) in enumerate(chips))
h=h.replace('href="#rooms">Explore by room</a></div></div>',
 f'href="#rooms">Explore by room</a></div><div class="hx-chips"><div class="hx-av">{chip}</div><span><b>37 courses</b> · Admissions open now</span></div></div>',1)

# 3. floating badges + progress bar on popup
h=h.replace('<div class="pop" aria-roledescription="carousel" aria-label="Highlights">',
 '<div class="pop-wrap"><span class="pop-blob" aria-hidden="true"></span><span class="pb pb1">✨ Admissions open</span><span class="pb pb2">📚 Tuition 3rd–12th</span><div class="pop" aria-roledescription="carousel" aria-label="Highlights"><span class="pop-bar" aria-hidden="true"><i></i></span>',1)
h=h.replace('<button id="popF" aria-label="Next">›</button></div></div></div></div></section>',
 '<button id="popF" aria-label="Next">›</button></div></div></div></div></div></section>',1)

# 4. new sections after the info row
pop=[('💃','Western Dance','western-dance','#FFEDD5'),('🪷','Bharatanatyam','bharatanatyam','#FCE7F3'),('🎤','Vocal Music','vocal-music','#F3E8FF'),('🧮','Abacus','abacus','#DCFCE7'),
     ('🎨','Drawing','drawing','#DBEAFE'),('♟️','Chess','chess','#FEF3C7'),('🥋','Karate','karate','#FEE2E2'),('🔤','English Phonics','english-phonics','#E0F2FE'),
     ('✍️','Handwriting','handwriting','#FAE8FF'),('🇮🇳','Hindi','hindi','#FFEDD5'),('📚','Tuition 3rd–12th','tuition','#DCFCE7'),('💻','Play & Code','play-code','#E0E7FF')]
tiles=''.join(f'<a class="pc" href="courses/{s}.html" style="--bg:{c}"><span>{e}</span><b>{n}</b><em>→</em></a>' for e,n,s,c in pop)
why=[('🏫','Everything under one roof','Dance, music, art, skills, sports and tuition in one centre at Moolapalayam.'),
     ('🚪','7 themed rooms','Each room has its own look and its own way of teaching.'),
     ('👧','For kids and adults','From toddler care and phonics to Montessori teacher training.'),
     ('💬','Easy enquiry','Message us on WhatsApp for timings and fees, then visit the centre.')]
whyh=''.join(f'<div class="why-i"><span>{e}</span><h3>{t}</h3><p>{d}</p></div>' for e,t,d in why)
new=f'''<section class="sec hx-pop"><div class="w"><div class="sec-h"><div><p class="kick">Popular programs</p><h2>Find your class.</h2></div><a class="lnk" href="courses.html">All 37 courses →</a></div>
<div class="pc-g">{tiles}</div></div></section>
<section class="sec hx-why"><div class="w"><p class="kick">Why Eureka</p><h2>A friendly place to learn.</h2><div class="why-g">{whyh}</div></div></section>'''
i=h.index('<section class="sec"'); h=h[:i]+new+h[i:]

# 5. admissions CTA band before latest updates
band=f'''<section class="hx-band"><div class="w"><div class="band"><div><p class="kick lt">Admissions open</p><h2>Ready to join a class?</h2><p>Message us for batch timings and fees, or visit us at Guru Moorthy Doctor Building, Poondurai Road.</p></div>
<div class="band-b"><a class="btn band-wa" href="{WA}" target="_blank" rel="noopener">💬 WhatsApp us</a><a class="btn band-ph" href="tel:+919965032227">📞 99650 32227</a></div></div></div></section>'''
m=[x.start() for x in re.finditer(r'<section class="sec"',h)]
k=[s for s in m if 'Latest updates' in h[s:s+1500]][0]
h=h[:k]+band+h[k:]
open(p,'w').write(h); print('ok')
