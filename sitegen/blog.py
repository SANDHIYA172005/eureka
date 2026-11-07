import re,os
S='/home/claude/site/'; os.chdir(S); os.makedirs('blog',exist_ok=True)
P=[
('abacus-benefits','abacus','Skills','5 ways abacus training builds sharper young minds','How sliding a few beads can boost concentration, memory and confidence with numbers.','12 Oct 2026',4,[
('p','Abacus may look like a simple counting frame, but for children it is a powerful brain workout. Every bead they move connects hand, eye and mind — and with practice, the abacus moves from the desk into their imagination.'),
('h','1. Faster, more accurate calculation'),('p','Children learn to add, subtract, multiply and divide by moving beads in a fixed pattern. Over time they calculate quickly and with fewer mistakes.'),
('h','2. Stronger concentration'),('p','Each step needs full attention. Regular practice trains children to stay focused for longer — a skill that helps in every subject.'),
('h','3. Better memory and visualisation'),('p','Advanced learners picture the abacus in their mind and solve sums mentally. This visual memory supports reading, spelling and problem-solving too.'),
('q','Tiny fingers, mighty minds — confidence with numbers starts early.'),
('h','4. Confidence in maths'),('p','When sums stop feeling scary, children enjoy maths class more and are happy to try harder problems.'),
('h','5. Learning feels like play'),('p','Colourful beads, speed games and small challenges make practice fun, so children want to come back for more.'),
]),
('why-phonics-first','english-phonics','Languages','Why phonics is the best first step to reading','Learning letter sounds helps children read, spell and pronounce words with confidence.','26 Oct 2026',3,[
('p','Before a child can read a word, they need to know the sounds its letters make. Phonics teaches exactly that — the link between letters and sounds — and it makes reading feel like cracking a fun code.'),
('h','Sounds before names'),('p','Instead of only learning “A, B, C”, children learn the sounds /a/, /b/, /k/. Blending those sounds together lets them read new words on their own.'),
('h','Spelling becomes easier'),('p','When children hear the sounds in a word, they can work out how to write it. Phonics builds both reading and spelling at the same time.'),
('q','A sound start for a smart future.'),
('h','Clearer pronunciation'),('p','Practising each sound out loud helps children speak English more clearly and confidently.'),
('h','How parents can help at home'),('ul',['Play “I spy” with sounds: “I spy something that starts with /m/”.','Read picture books together and point to words as you read.','Praise effort, not just correct answers.']),
]),
('handwriting-tips','handwriting','Skills','6 simple tips for neater handwriting at home','Small daily habits that help children write neatly, legibly and with confidence.','2 Nov 2026',3,[
('p','Good handwriting creates a lasting impression — on teachers, in exams and in everyday life. The good news: a few minutes of the right practice each day makes a big difference.'),
('h','1. Sit right'),('p','Feet flat on the floor, back straight and the notebook slightly tilted. Good posture means a steady hand.'),
('h','2. Hold the pencil gently'),('p','A relaxed tripod grip — thumb, index and middle finger — gives better control and less tiredness.'),
('h','3. Use ruled lines'),('p','Four-line or ruled notebooks guide letter height and keep words straight.'),
('q','Elegance in every curve.'),
('h','4. Mind the spacing'),('p','Leave a finger-width gap between words. Even spacing instantly makes writing easier to read.'),
('h','5. Slow down first'),('p','Neatness comes first; speed follows naturally with practice.'),
('h','6. Practise a little, every day'),('p','Ten focused minutes daily beats one long session a week. Celebrate improvement to keep children motivated.'),
]),
('zumba-for-everyone','zumba','Fitness','Zumba: the fun way for the whole family to stay fit','Dance your way to fitness — no dance experience needed.','4 Nov 2026',3,[
('p','Zumba turns a workout into a party. Set to energetic music with easy-to-follow moves, it is a joyful way to burn calories, stay active and feel refreshed.'),
('h','Fitness that doesn’t feel like exercise'),('p','Because you are dancing to music you love, an hour goes by quickly — and you still get a full cardio workout.'),
('h','Good for body and mind'),('ul',['Improves stamina, balance and coordination','Helps manage weight and tone muscles','Releases stress and lifts your mood']),
('q','Dance your way to fitness.'),
('h','For all ages'),('p','Zumba combines dance and fitness for people of all ages. Beginners simply follow along at their own pace and build up over time.'),
('h','Join a class'),('p','Our Zumba Fitness classes at S3 Dance Studio run online and offline. Call 99650 32227 or visit the academy to get started.'),
])]
TAG={'Skills':'#DCFCE7','Languages':'#E0F2FE','Fitness':'#FEF3C7'}
def body(blocks):
    o=''
    for t,v in blocks:
        if t=='p':o+=f'<p>{v}</p>'
        elif t=='h':o+=f'<h2>{v}</h2>'
        elif t=='q':o+=f'<blockquote>{v}</blockquote>'
        elif t=='ul':o+='<ul>'+''.join(f'<li>{x}</li>' for x in v)+'</ul>'
    return o
base=open('blog.html').read()
a=base.index('<main'); z=base.index('</main>')+7
def card(s,img,tag,title,desc,date,mins,pre,big=False):
    return f'<a class="bl-c{" big" if big else ""}" href="{pre}{s}.html"><div class="bl-img"><img src="{"../" if pre=="" else ""}assets/img/{img}.jpg" alt="" loading="lazy"><span class="bl-tag" style="--bg:{TAG[tag]}">{tag}</span></div><div class="bl-b"><p class="bl-m">{date} · {mins} min read</p><h3>{title}</h3><p>{desc}</p><em>Read article →</em></div></a>'
# listing
cards=card(*P[0][:7],'blog/',True)+''.join(card(*x[:7],'blog/') for x in P[1:])
main=f'<main id="main"><section class="bl-hero"><div class="w"><p class="kick">Eureka blog</p><h1>Tips, ideas &amp; stories<br>for growing learners.</h1><p class="lede">Simple, practical reads for parents and students — from maths and reading to fitness and fun.</p></div></section><section class="sec" style="padding-top:10px"><div class="w"><div class="bl-g">{cards}</div></div></section></main>'
h=base[:a]+main+base[z:]
h=re.sub(r'<title>[^<]*</title>','<title>Blog — Eureka Academy, Moolapalayam</title>',h,count=1)
open('blog.html','w').write(h)
# post template: fix relative paths
def rel(t):
    return re.sub(r'(href|src)="(?!https?:|tel:|mailto:|#|\.\./|data:|//)([^"]+)"',r'\1="../\2"',t)
shell=rel(base[:a]),rel(base[z:])
for i,(s,img,tag,title,desc,date,mins,blocks) in enumerate(P):
    others=''.join(card(*x[:7],'') for j,x in enumerate(P) if j!=i)[:]
    hs=[v for t,v in blocks if t=='h']
    toc=''.join(f'<a href="#s{k+1}">{v}</a>' for k,v in enumerate(hs))
    bh=body(blocks)
    for k,v in enumerate(hs): bh=bh.replace(f'<h2>{v}</h2>',f'<h2 id="s{k+1}">{v}</h2>',1)
    art=f'''<main id="main"><div class="po-bar" aria-hidden="true"><i></i></div><article class="po po2">
<header class="po-h"><div class="w po2-h"><div><div class="po-top"><a class="po-back" href="../blog.html">← All articles</a><span class="bl-tag" style="--bg:{TAG[tag]}">{tag}</span></div><h1>{title}</h1><p class="po-d">{desc}</p>
<div class="po-a"><img src="../assets/logo.png" alt="" width="40" height="40"><div><b>Eureka Academy</b><small>{date} · {mins} min read</small></div></div></div>
<figure class="po-img"><img src="../assets/img/{img}.jpg" alt="{title}"></figure></div></header>
<div class="w po2-g"><div class="po-body">{bh}
<div class="po-cta"><div><b>Want your child to join?</b><small>Classes Mon–Sat 5–8 pm · Sun 10:30 am–12 pm · Online &amp; offline</small></div><a class="btn btn-dark" href="tel:+919965032227">Call 99650 32227</a></div></div>
<aside class="po-side"><div class="po-toc"><p>On this page</p>{toc}</div>
<div class="po-join"><b>Join a class</b><small>Admission by phone or direct visit</small><a class="btn btn-dark" href="../contact.html">Enquire now</a><a class="po-tel" href="tel:+919965032227">📞 99650 32227</a></div>
<div class="po-sh2"><span>Share</span><a href="https://wa.me/?text={title.replace(' ','%20')}" target="_blank" rel="noopener">WhatsApp</a><a href="../blog.html">All articles</a></div></aside></div>
<section class="sec po-more"><div class="w"><h2>More to read</h2><div class="bl-g three">{others}</div></div></section></article></main>
<script>(function(){{var b=document.querySelector('.po-bar i'),a=document.querySelector('.po-body'),l=[].slice.call(document.querySelectorAll('.po-toc a'));function f(){{var r=a.getBoundingClientRect(),p=Math.min(1,Math.max(0,-r.top/(r.height-innerHeight*.6)));b.style.transform='scaleX('+p+')';var cur=null;l.forEach(function(x){{var h=document.querySelector(x.getAttribute('href'));if(h&&h.getBoundingClientRect().top<140)cur=x}});l.forEach(function(x){{x.classList.toggle('on',x===cur)}})}}addEventListener('scroll',f,{{passive:true}});f()}})();</script>'''
    hh=shell[0]+art+shell[1]
    hh=re.sub(r'<title>[^<]*</title>',f'<title>{title} — Eureka Academy</title>',hh,count=1)
    hh=hh.replace('aria-current="page">Blog','>Blog')
    open(f'blog/{s}.html','w').write(hh)
print('ok')
