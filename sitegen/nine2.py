import re,os
S='/home/claude/site/'; os.chdir(S)
HOURS='Mon–Sat 5–8 pm · Sun 10:30 am–12 pm'
h=open('index.html').read()
# hero
h=re.sub(r'<p class="kick"><span class="live"></span>[^<]*</p>','<p class="kick"><span class="live"></span>Eureka Academy · A unit of Edu Well</p>',h,count=1)
h=re.sub(r'<h1>Learn, <span class="rw".*?</h1>','<h1>More than learning,<b>a journey of growth!</b></h1><p class="hx-tag">Discover <i>•</i> Learn <i>•</i> Create <i>•</i> Shine</p>',h,count=1,flags=re.S)
h=re.sub(r'<p class="lede">9 courses for[^<]*</p>','<p class="lede hx-pill"><span>Education</span><span>Arts</span><span>Dance</span><span>Skills</span><span>Fitness</span></p>',h,count=1)
h=h.replace('<span><b>9 courses</b> · Admissions open now</span>','<span><b>Since 2014</b> · Online &amp; offline classes</span>')
# popup slides
h=re.sub(r'<div class="pop-s"><div class="pop-art" style="--bg:#E0E7FF">💻</div>.*?</a></div>','<div class="pop-s"><div class="pop-art" style="--bg:#DCFCE7">🧮</div><small>Popup</small><h3>Abacus &amp; Drawing</h3><p class="muted sm">Tiny fingers, mighty minds · Little hands, big imagination</p><a href="rooms/skills-corner.html">Learn more →</a></div>',h,count=1,flags=re.S)
h=h.replace('<p class="muted sm">Western · Classical · Vocal · Zumba</p>','<p class="muted sm">Western Dance · Zumba Fitness — Vaanga Aadalam!</p>')
# quick bar
qb='<div class="qb-r"><a href="rooms/dance-studio.html"><b>Dance &amp; Fitness</b><span>Western · Zumba</span><em>Explore</em></a><a href="rooms/language-room.html"><b>Languages</b><span>Hindi · English · Phonics</span><em>Explore</em></a><a href="rooms/skills-corner.html"><b>Skills</b><span>Abacus · Drawing · Handwriting</span><em>Explore</em></a><a href="rooms/study-room.html"><b>Academics</b><span>Tuition</span><em>Explore</em></a></div>'
h=re.sub(r'<div class="qb-r">.*?</a></div>',qb,h,count=1,flags=re.S)
h=re.sub(r'(<h4>(?:<svg.*?</svg>)?Batch timings</h4>)<p class="big">[^<]*</p>',r'\1<p class="big">Mon–Sat 5–8 pm</p><p>Sunday 10:30 am – 12:00 pm</p>',h,count=1,flags=re.S)
h=re.sub(r'(<h4>(?:<svg.*?</svg>)?How it works</h4>)<p>[^<]*</p>',r'\1<p>Call 99650 32227 or visit the academy directly for admission. All sessions run online &amp; offline.</p>',h,count=1,flags=re.S)
# room list renumber
k=[0]
def rn(m):
    k[0]+=1; return f'<span class="n" style="--c:{m.group(1)}">{k[0]}</span>'
a=h.find('<div class="rlist">'); z=h.find('</div></div>',a)
seg=re.sub(r'<span class="n" style="--c:([^"]*)">\d+</span>',rn,h[a:z])
seg=re.sub(r'<small>\d+ courses? · [^<]*</small>','',seg)
for r,t in [('dance-studio','2 courses · Western Dance and Zumba Fitness.'),('language-room','4 courses · Hindi, Communication English, Phonics, Handwriting.'),('skills-corner','2 courses · Abacus and Drawing.'),('study-room','1 course · Tuition for school subjects.')]:
    seg=re.sub(rf'(href="rooms/{r}\.html">.*?</b>)',rf'\1<small>{t}</small>',seg,count=1,flags=re.S)
h=h[:a]+seg+h[z:]
# why
h=h.replace('<h3>For kids and adults</h3><p>From toddler care and phonics to Montessori teacher training.</p>','<h3>Online &amp; offline</h3><p>Every session is available at the academy and online.</p>')
h=h.replace('<h3>Everything under one roof</h3><p>Dance, music, art, skills, sports and tuition in one centre at Moolapalayam.</p>','<h3>Since 2014</h3><p>Education, arts, dance, skills and fitness under one roof in Moolapalayam.</p>')
h=h.replace('<h3>Easy enquiry</h3><p>Message us on WhatsApp for timings and fees, then visit the centre.</p>','<h3>Easy admission</h3><p>Call 99650 32227 or walk in to the academy to enrol.</p>')
# updates
ups=['Admissions are open — call 99650 32227 or visit the academy.','S3 Dance Studio: Western Dance and Zumba Fitness — Vaanga Aadalam!',f'Class timings: {HOURS}.','All sessions are available online and offline.']
items=re.findall(r'<li[^>]*>.*?</li>',h[h.index('Latest updates'):h.index('</section>',h.index('Latest updates'))],flags=re.S)
for old,new in zip(items,ups):
    nn=re.sub(r'(<span class="[^"]*">N</span>)?([^<>]*)(</a>|</span>|</p>)',lambda m:m.group(0),old)
    h=h.replace(old,re.sub(r'>[^<>]{12,}<','>'+new+'<',old,count=1))
# home faq answers
fq={'What age groups do you cater to?':'Our classes are for school children and adults — Zumba Fitness and Communication English welcome all ages. We also run Toddler Care for little ones. Call us to find the right batch.',
'Which programs do you offer?':'Western Dance, Zumba Fitness, Hindi, Communication English, Phonics, Handwriting, Abacus, Drawing and Tuition (Maths, Science, English &amp; Social Studies). See the <a href="courses.html">course list</a>.',
'Do you offer online classes?':'Yes — all our sessions are available both online and offline at the academy.',
'What are the fees and batch timings?':f'Classes run {HOURS}. Fees and payments vary by course and programme — call <a href="tel:+919965032227">99650 32227</a> for current details.',
'How do I enroll my child in a course?':'Admission and enquiry is by phone or a direct visit. Call <a href="tel:+919965032227">99650 32227</a> or walk in to Guru Moorthy Doctor Building, Moolapalayam.',
'What is Eureka Academy all about?':'Eureka Academy — a unit of Edu Well — has been nurturing learners in Moolapalayam, Erode since 2014. Together with S3 Dance Studio we offer education, arts, dance, skills and fitness: more than learning, a journey of growth.'}
for q,a in fq.items():
    h=re.sub(rf'(<b>{re.escape(q)}</b><i aria-hidden="true">\+</i></summary><p>).*?(</p>)',lambda m:m.group(1)+a+m.group(2),h,count=1,flags=re.S)
h=h.replace('Can’t find your answer? Call or WhatsApp us on 99650 32227.','Can’t find your answer? Call us on 99650 32227 or visit the academy.')
h=h.replace('Message us for batch timings and fees, or visit us at Guru Moorthy Doctor Building, Poondurai Road.',f'Call us or walk in to Guru Moorthy Doctor Building, Poondurai Road. Open {HOURS}.')
open('index.html','w').write(h)

# about page
a=open('about.html').read()
a=a.replace('<div class="ab-facts"><div><b>9</b><span>Courses</span></div><div><b>4</b><span>Themed rooms</span></div><div><b>3rd–12th</b><span>Std tuition</span></div><div><b>Erode</b><span>Moolapalayam</span></div></div>',
 '<div class="ab-facts"><div><b>2014</b><span>Started</span></div><div><b>9</b><span>Courses</span></div><div><b>Online</b><span>&amp; offline sessions</span></div><div><b>Erode</b><span>Moolapalayam</span></div></div>')
a=re.sub(r'<h1>Transforming lives<br><em>through practical learning.</em></h1><p class="lede">[^<]*</p>','<h1>More than learning,<br><em>a journey of growth.</em></h1><p class="lede">Eureka Academy — a unit of Edu Well · Discover • Learn • Create • Shine</p>',a,count=1)
story='''<p>Since 2014, Eureka Academy &amp; S3 Dance Studio has been a place in Moolapalayam, Erode where children grow into confident, skilled and independent individuals.</p>
<p>We bring together education, arts, dance, skills and fitness — from Abacus, Phonics and Handwriting to Western Dance and Zumba — with every session available online and offline.</p>'''
a=re.sub(r'(<h2>Shaping futures with purpose.</h2>)\s*<p>.*?</p>\s*<p>.*?</p>',lambda m:m.group(1)+story,a,count=1,flags=re.S)
founder='''<section class="sec" id="founder"><div class="w fd"><div class="fd-c"><div class="fd-av" aria-hidden="true">SL</div><div class="fd-b"><p class="kick">Founder &amp; Director</p><h2>Saranya Loganathan</h2><p class="fd-q">M.Sc (IT), MCA, B.Ed, DMT</p>
<ul class="fd-l"><li><b>15 years</b><span>experience in teaching</span></li><li><b>Vice Principal</b><span>&amp; Co-ordinator</span></li><li><b>12 years</b><span>as an entrepreneur</span></li></ul></div></div></div></section>'''
pil=[('🧠','Skill enhancement','Developing essential skills through phonics, abacus, handwriting, communication and other programmes.'),('🧘','Physical &amp; mental wellness','Promoting healthy lifestyles through yoga, Zumba and physical activities.'),('🌟','Confidence building','Opportunities for children to explore, perform, participate and showcase their talents.'),('🌱','Holistic development','Shaping children into independent, confident and responsible individuals.')]
pilh=''.join(f'<div class="ab-do"><span>{e}</span><h3>{t}</h3><p>{d}</p></div>' for e,t,d in pil)
a=re.sub(r'<section class="sec"><div class="w"><p class="kick">What we do</p>.*?</section>',lambda m:f'<section class="sec"><div class="w"><p class="kick">Mission &amp; vision</p><h2>What we work towards.</h2><div class="ab-g4">{pilh}</div></div></section>',a,count=1,flags=re.S)
a=a.replace('<section class="sec sec-alt"><div class="w"><p class="kick">Why choose us</p>',founder+'<section class="sec sec-alt"><div class="w"><p class="kick">Why choose us</p>',1)
# courses tabs -> simple 9 grid
from nine_data import C,KEEP
cc=''.join(f'<a class="ab-cc" href="courses/{k}.html"><span class="e">{C[k][1]}</span><h3>{C[k][0]}</h3><p>{C[k][2]}</p><em>View details →</em></a>' for k in KEEP)
a=re.sub(r'<div class="ab-th">.*?<div class="ab-c">',lambda m:f'<div class="ab-th"><div><p class="kick">Our courses</p><h2>What we teach.</h2></div></div><div class="ab-pn on">{cc}</div><div class="ab-c">',a,count=1,flags=re.S)
phil='''<section class="sec"><div class="w ph-b"><p class="kick">Our philosophy</p><h2>Every child is unique.<br>Every talent deserves an opportunity.</h2><p>At Eureka Academy, we believe every child has something special within them. Our goal is not just to teach, but to identify, nurture and develop each child’s unique potential through education, creativity and discipline.</p></div></section>'''
a=re.sub(r'<section class="sec"><div class="w ab-mv">.*?</section>',phil,a,count=1,flags=re.S)
vals=[('Care &amp; commitment','💛'),('Creativity &amp; innovation','💡'),('Quality education','📘'),('Inclusivity &amp; teamwork','🤝'),('Excellence &amp; growth','🚀')]
vh=''.join(f'<div class="ab-val"><i>{e}</i><h3>{t}</h3></div>' for t,e in vals)
a=re.sub(r'(<p class="kick">What we stand for</p><h2>)Our values.(</h2>)<div class="ab-g3">.*?</div></div></div></section>',lambda m:m.group(1)+'Our core values.'+m.group(2)+f'<div class="ab-g5">{vh}</div></div></section>',a,count=1,flags=re.S)
a=a.replace('<li><b>02</b><h3>Develop</h3>','<li><b>02</b><h3>Develop</h3>')
a=a.replace('<div class="ab-who"><span>💼</span><h3>Professionals</h3><p>Digital and teaching courses to grow your career.</p></div>','<div class="ab-who"><span>💻</span><h3>Online learners</h3><p>Every session is also available online.</p></div>')
a=a.replace('<p>Tuition for 3rd–12th Std plus skills beyond school.</p>','<p>Tuition in Maths, Science, English &amp; Social Studies.</p>')
a=a.replace('<p>Hobbies, fitness and new skills for self-growth.</p>','<p>Communication English and Zumba Fitness.</p>')
a=a.replace('href="https://wa.me/919965032227?text=Hello%20Eureka%20Academy%2C%20I%20would%20like%20to%20join%20a%20course." target="_blank" rel="noopener">Join now</a>','href="tel:+919965032227">Call to join</a>')
open('about.html','w').write(a)
print('ok')
