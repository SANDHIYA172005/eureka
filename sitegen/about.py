P='/home/claude/site/'
WA='https://wa.me/919965032227?text=Hello%20Eureka%20Academy%2C%20I%20would%20like%20to%20join%20a%20course.'
why=[('Personal attention','Every learner is guided at their own pace and level.'),('Learn by doing','Practice, activities and performances — not just theory.'),
('Friendly community','Learn alongside other motivated children and adults.'),('Guidance at every step','From choosing a course to moving up to the next level.'),
('Skill-focused','Real abilities you can see — on stage, on paper and in class.'),('Everything in one place','Dance, music, art, skills, sports and tuition under one roof.')]
whyh=''.join(f'<div class="ab-why"><b>{i+1:02d}</b><h3>{t}</h3><p>{d}</p></div>' for i,(t,d) in enumerate(why))
do=[('🎯','Practical training','Hands-on classes focused on real, visible progress.'),('📈','Progress you can see','Regular practice and feedback so learners keep improving.'),
('🤝','Personal guidance','Teachers who support each learner’s own journey.'),('🏆','Room to grow','Support for school studies, hobbies and new skills alike.')]
doh=''.join(f'<div class="ab-do"><span>{e}</span><h3>{t}</h3><p>{d}</p></div>' for e,t,d in do)
tabs={'Kids courses':[('♟️','Thinking','Chess','Strategy, critical thinking and problem solving.','chess'),('🥢','Heritage','Silambam','The traditional martial art for agility and focus.','silambam'),('🗣️','Communication','Spoken English','Fluency, grammar and confident speaking.','spoken-english')],
'Adult courses':[('🎓','Teaching','Montessori Teacher Training','Prepare for a career in early childhood teaching.','montessori-teacher-training'),('🔤','Language','Phonics for Adults','Learn to read and teach English phonics.','phonics-english-adults'),('💃','Fitness','Zumba &amp; Aerobics','Fun, high-energy workouts set to music.','zumba')],
'Digital courses':[('💻','Code','Web &amp; App Development','Build websites and mobile apps step by step.','web-mobile-app-development'),('🎨','Design','Graphic Design','Posters, logos and social media designs.','graphic-design'),('🎬','Media','Video Editing','Edit reels, short films and videos.','video-editing')]}
tb=''.join(f'<button role="tab" class="ab-tb{" on" if i==0 else ""}" data-i="{i}">{k}</button>' for i,k in enumerate(tabs))
pan=''.join(f'<div class="ab-pn{" on" if i==0 else ""}" role="tabpanel">'+''.join(f'<a class="ab-cc" href="courses/{s}.html"><span class="e">{e}</span><small>{c}</small><h3>{n} <i>✓</i></h3><p>{d}</p><em>View details →</em></a>' for e,c,n,d,s in v)+'</div>' for i,v in enumerate(tabs.values()))
who=[('🧒','Kids','Fun, play-based classes that build strong foundations.'),('🎒','Students','Tuition for 3rd–12th Std plus skills beyond school.'),('🧑','Adults','Hobbies, fitness and new skills for self-growth.'),('💼','Professionals','Digital and teaching courses to grow your career.')]
whoh=''.join(f'<div class="ab-who"><span>{e}</span><h3>{t}</h3><p>{d}</p></div>' for e,t,d in who)
main=f'''<main id="main">
<section class="ab-hero"><div class="w"><nav class="crumb" aria-label="Breadcrumb"><a href="index.html">Home</a> / <span>About us</span></nav>
<h1>Transforming lives<br><em>through practical learning.</em></h1><p class="lede">Building children and adults with real skills, confidence and joy for a future-ready world.</p>
<div class="row"><a class="btn btn-dark" href="courses.html">Explore programs →</a></div>
<div class="ab-facts"><div><b>37</b><span>Courses</span></div><div><b>7</b><span>Themed rooms</span></div><div><b>3rd–12th</b><span>Std tuition</span></div><div><b>Erode</b><span>Moolapalayam</span></div></div></div></section>

<section class="sec"><div class="w ab-story"><div class="ab-pic" aria-hidden="true"><span>💃</span><span>🎤</span><span>🧮</span><span>🎨</span></div>
<div><p class="kick">Our story</p><h2>Shaping futures with purpose.</h2>
<p>Eureka Academy &amp; S3 Dance Studio is more than a class centre. It is a place where children and adults grow into confident, skilled and independent people.</p>
<p>From Moolapalayam, Erode, we bring traditional arts like Bharatanatyam, Silambam and vocal music together with modern skills like coding, design and spoken English — guiding every learner towards meaningful growth.</p>
<a class="btn btn-line" href="#approach">Our approach →</a></div></div></section>

<section class="sec sec-alt"><div class="w"><p class="kick">Why choose us</p><h2>Why Eureka Academy?</h2><div class="ab-g3">{whyh}</div></div></section>

<section class="sec"><div class="w"><p class="kick">What we do</p><h2>Learning that shows results.</h2><div class="ab-g4">{doh}</div></div></section>

<section class="sec sec-alt"><div class="w"><div class="ab-th"><div><p class="kick">Our courses</p><h2>Specialised courses.</h2></div><div class="ab-tbs" role="tablist">{tb}</div></div>
{pan}<div class="ab-c"><a class="btn btn-dark" href="courses.html">View all 37 courses →</a></div></div></section>

<section class="sec" id="approach"><div class="w"><p class="kick">Our teaching approach</p><h2>Discover. Develop. Deliver.</h2>
<ol class="ab-ap"><li><b>01</b><h3>Discover</h3><p>We get to know each learner’s strengths, interests and natural potential.</p></li>
<li><b>02</b><h3>Develop</h3><p>Structured practice and steady feedback build the skill step by step.</p></li>
<li><b>03</b><h3>Deliver</h3><p>Learners use what they learn with confidence — on stage, in exams and in life.</p></li></ol></div></section>

<section class="sec sec-alt"><div class="w"><p class="kick">Who can join</p><h2>A class for everyone.</h2><div class="ab-g4">{whoh}</div></div></section>

<section class="sec"><div class="w ab-mv"><div class="ab-m"><span>🎯</span><h3>Our mission</h3><p>To give every learner practical skills, caring guidance and hands-on experience that help them shine in real life.</p></div>
<div class="ab-m v"><span>🔭</span><h3>Our vision</h3><p>A future where skill-based learning is open to everyone, helping people lead confident, independent and purposeful lives.</p></div></div></section>

<section class="sec sec-alt"><div class="w"><p class="kick">What we stand for</p><h2>Our values.</h2><div class="ab-g3">
<div class="ab-val"><i>01</i><h3>Trust</h3><p>Honest, open and consistent — so parents and learners feel confident with us.</p></div>
<div class="ab-val"><i>02</i><h3>Quality</h3><p>High standards in every class, so learning is meaningful and lasting.</p></div>
<div class="ab-val"><i>03</i><h3>Growth</h3><p>Always improving, helping every learner reach their full potential.</p></div></div></div></section>

<section class="sec"><div class="w"><div class="band"><div><p class="kick lt">Begin your journey</p><h2>Learn skills that shape your future.</h2><p>Take the first step with Eureka Academy &amp; S3 Dance Studio today.</p></div>
<div class="band-b"><a class="btn band-wa" href="{WA}" target="_blank" rel="noopener">Join now</a><a class="btn band-ph" href="courses.html">Browse courses</a></div></div></div></section>
</main>'''
js='''<script>(function(){var b=[].slice.call(document.querySelectorAll('.ab-tb')),p=[].slice.call(document.querySelectorAll('.ab-pn'));b.forEach(function(x){x.onclick=function(){b.forEach(function(y,k){y.classList.toggle('on',y===x);p[k].classList.toggle('on',y===x)})}})})();</script>'''
h=open(P+'about.html').read(); a=h.index('<main'); z=h.index('</main>')+7
h=h[:a]+main+h[z:]; h=h.replace('</body>',js+'</body>',1); open(P+'about.html','w').write(h); print('ok')
