import re,glob,os,urllib.parse as U
S='/home/claude/site/'; os.chdir(S)
KEEP=['western-dance','zumba','hindi','spoken-english','english-phonics','handwriting','abacus','drawing','tuition']
C={ # slug: (name, emoji, tagline, description, room, colour)
'western-dance':('Western Dance','💃','Unleash the dancer in you','Step into the world of rhythm and style. We train students in various dance forms that build confidence, fitness and stage presence — classes full of energy, fun and creativity that help dancers express themselves through movement.','dance-studio','#FFEDD5'),
'zumba':('Zumba Fitness','🔥','Dance your way to fitness','Turn your workout into a party! Set to energetic music with easy-to-follow moves, Zumba is a fun way to burn calories, stay fit and feel refreshed. It combines dance and fitness for people of all ages — no dance experience required.','dance-studio','#FEF3C7'),
'hindi':('Hindi Classes','🇮🇳','Bhasha mein ho dum, tabhi toh aayega fun','Our Hindi classes help students read, write and speak Hindi with confidence. We build a strong foundation in grammar, vocabulary, pronunciation and communication — for school, exams or everyday use, we make learning Hindi simple and enjoyable.','language-room','#FFE4E6'),
'spoken-english':('Communication English','🗣️','From hesitant to fluent — let’s make English easy','Boost your confidence and fluency in English. Designed for students, professionals and beginners, our classes focus on practical speaking, listening, reading and writing skills so you can use English effectively in everyday life.','language-room','#E0F2FE'),
'english-phonics':('Phonics','🔤','A sound start for a smart future','Our Phonics classes help children read, spell and pronounce words with confidence. Using fun, interactive methods, we teach the relationship between letters and sounds, making reading an enjoyable experience.','language-room','#F3E8FF'),
'handwriting':('Handwriting','✍️','Elegance in every curve','Good handwriting creates a lasting impression! Our classes help children develop neat, legible and confident writing through structured practice — focusing on letter formation, spacing, speed and presentation.','language-room','#FAE8FF'),
'abacus':('Abacus','🧮','Tiny fingers, mighty minds','Our Abacus program helps children build a strong foundation in mathematics through fun, interactive learning. Using the abacus, kids learn to calculate quickly and accurately while boosting concentration, memory and problem-solving skills.','skills-corner','#DCFCE7'),
'drawing':('Drawing','🎨','Little hands, big imagination','Our Drawing classes bring out the creativity and imagination in every child. With step-by-step guidance, kids learn sketching, colouring, shading and painting techniques that help them express their ideas beautifully on paper.','skills-corner','#DBEAFE'),
'tuition':('Tuition','📚','Concept clarity, regular practice, exam success','Our classes focus on concept clarity, regular practice and exam preparation. With interactive learning methods, we help students build confidence in Mathematics, Science, English and Social Studies.','study-room','#ECFCCB')}
ROOMS={'dance-studio':('Dance Studio','S3 Dance Studio: Western Dance and Zumba Fitness.','#8B5CF6'),'language-room':('Language Room','Hindi, Communication English, Phonics and Handwriting.','#2563EB'),
'skills-corner':('Skills Corner','Abacus and Drawing for sharp minds and creative hands.','#0E9F6E'),'study-room':('Study Room','Tuition in Maths, Science, English and Social Studies.','#F59E0B')}
DROPR=['sports-arena','craft-wellness','code-lab']
HOURS='Mon–Sat 5–8 pm · Sun 10:30 am–12 pm'
allc=[os.path.basename(f)[:-5] for f in glob.glob('courses/*.html')]
DROP=[c for c in allc if c not in KEEP]
dro='|'.join(map(re.escape,DROP)); drr='|'.join(DROPR)
for c in DROP: os.remove(f'courses/{c}.html')
for r in DROPR: os.remove(f'rooms/{r}.html')

def mega(p):
    lis=''.join(f'<li><a href="{p}courses/{k}.html">{C[k][1]} {C[k][0]}</a></li>' for k in KEEP)
    return f'<div class="mg-in"><div class="mg-col"><a class="mg-h" href="{p}courses.html">Our courses</a><ul class="mg-9">{lis}</ul></div></div><div class="mg-f">'

for f in glob.glob('**/*.html',recursive=True):
    p='../' if '/' in f else ''
    h=open(f).read()
    h=re.sub(r'<div class="mg-in">.*?</div><div class="mg-f">',lambda m:mega(p),h,count=1,flags=re.S)
    h=re.sub(rf'<li><a href="[^"]*courses/(?:{dro})\.html"[^>]*>.*?</a></li>','',h)
    h=re.sub(rf'<a class="(?:cc|pc|ab-cc)" href="[^"]*courses/(?:{dro})\.html".*?</a>','',h,flags=re.S)
    h=re.sub(rf'<a href="[^"]*courses/(?:{dro})\.html" style="--d:[^"]*">.*?</a>','',h)
    h=re.sub(rf'<a [^>]*href="[^"]*rooms/(?:{drr})\.html".*?</a>','',h,flags=re.S)
    for a,b in [('View all 37 courses','View all 9 courses'),('All 37 courses','All 9 courses'),('See all 37 courses','See all 9 courses'),('37 courses','9 courses'),('7 themed rooms','4 themed rooms'),('7 rooms','4 rooms'),
                ('>Spoken English<','>Communication English<'),('>English Phonics<','>Phonics<'),('Zumba &amp; Aerobics','Zumba Fitness'),
                ('<dd>Contact us for current slots</dd>',f'<dd>{HOURS}</dd>'),('<dd>Shared on enquiry</dd>','<dd>Varies by course &amp; programme — call us</dd>')]:
        h=h.replace(a,b)
    h=h.replace('<div><dt>','<div><dt>',1)
    if 'Online &amp; offline</dd>' not in h:
        h=re.sub(r'(<div><dt>(?:<svg.*?</svg>)?Where</dt><dd>[^<]*</dd></div>)',r'\1<div><dt>Mode</dt><dd>Online &amp; offline</dd></div>',h,count=1,flags=re.S)
    h=h.replace('Copyright © 2026 Eureka Academy.','Copyright © 2026 Eureka Academy · A unit of Edu Well.')
    open(f,'w').write(h)

# room pages
for r,(nm,ds,col) in ROOMS.items():
    f=f'rooms/{r}.html'; h=open(f).read()
    for k in re.findall(r'data-k="([a-z-]+)"',h):
        if k in KEEP: continue
        h=re.sub(rf'<button role="tab"[^>]*data-k="{k}".*?</button>','',h,flags=re.S)
        h=re.sub(rf'<article [^>]*data-s="{k}".*?</article>','',h,flags=re.S)
    n=len([k for k in KEEP if C[k][4]==r])
    h=re.sub(r'<p class="lede">.*?</p>',f'<p class="lede">{ds} Tap a course to step inside. {n} course{"s" if n>1 else ""} in this room.</p>',h,count=1,flags=re.S)
    i=0
    def num(m):
        global i; i+=1; return f'<small>{i:02d}</small>'
    a=h.find('class="rx-list"'); z=h.find('</div>',a)
    seg=re.sub(r'<small>\d+</small>',num,h[a:z]); h=h[:a]+seg+h[z:]
    open(f,'w').write(h)

# course pages: rename h1/crumb, add poster + flyer text section
for k in KEEP:
    f=f'courses/{k}.html'; h=open(f).read(); nm,e,tg,ds,rm,col=C[k]
    h=re.sub(r'<h1>[^<]*</h1>',f'<h1>{nm}</h1>',h,count=1)
    h=re.sub(r'<span aria-current="page">[^<]*</span>',f'<span aria-current="page">{nm}</span>',h,count=1)
    h=re.sub(r'<p class="ch-hl">[^<]*</p>',f'<p class="ch-hl">{tg}</p>',h,count=1)
    h=re.sub(r'(<p class="ch-hl">[^<]*</p>)<p class="lede">[^<]*</p>',rf'\1<p class="lede">{ds}</p>',h,count=1)
    img=f'<img src="../assets/img/{k}.jpg" alt="{nm} class at Eureka Academy" loading="lazy" width="900" height="900">' if os.path.exists(f'assets/img/{k}.jpg') else f'<div class="cp-e" style="--bg:{col}">{e}</div>'
    sec=f'<section class="sec cp-sec"><div class="w cp"><figure class="cp-img">{img}</figure><div class="cp-t"><p class="kick">About this class</p><h2>{tg}.</h2><p>{ds}</p><ul class="cp-f"><li>🕔 {HOURS}</li><li>💻 Online &amp; offline sessions</li><li>📞 Admission by phone or direct visit</li></ul><div class="row"><a class="btn btn-dark" href="tel:+919965032227">Call 99650 32227</a><a class="btn btn-line" href="https://maps.app.goo.gl/d6kSKBfJiE24eaty6" target="_blank" rel="noopener">Visit the academy</a></div></div></div></section>'
    if 'cp-sec' not in h: h=h.replace('</section>\n\n<section class="sec" style="padding:28px 0 0">','</section>'+sec+'\n\n<section class="sec" style="padding:28px 0 0">',1)
    h=re.sub(r'<title>[^<|—-]*',f'<title>{nm} ',h,count=1)
    open(f,'w').write(h)

# courses.html grid
cards=''.join(f'<a class="cg" href="courses/{k}.html"><div class="cg-i" style="--bg:{C[k][5]}">'+(f'<img src="assets/img/{k}.jpg" alt="" loading="lazy">' if os.path.exists(f'assets/img/{k}.jpg') else f'<span>{C[k][1]}</span>')+f'</div><div class="cg-b"><small>{ROOMS[C[k][4]][0]}</small><h3>{C[k][0]}</h3><p>{C[k][2]}</p><em>View course →</em></div></a>' for k in KEEP)
h=open('courses.html').read()
a=h.index('<section class="sec" style="padding-top:20px">'); z=h.index('</section>',h.index('id="empty"'))+10
h=h[:a]+f'<section class="sec" style="padding-top:20px"><div class="w"><div class="cg-g">{cards}</div><p class="muted sm" style="margin-top:24px">🕔 {HOURS} · 💻 All sessions available online &amp; offline</p></div></section>'+h[z:]
h=re.sub(r'<h1>[^<]*</h1>','<h1>9 courses, one academy.</h1>',h,count=1)
h=re.sub(r'(<section class="ph">.*?<p class="lede">)[^<]*',r'\1Education, arts, dance, skills and fitness — every course has its own page with what you will learn.',h,count=1,flags=re.S)
open('courses.html','w').write(h)
print('dropped',len(DROP),'courses')
