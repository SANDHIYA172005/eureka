"""Static multi-page site generator for Eureka Academy (minimal design)."""
import json, os, shutil, urllib.parse as U, html

OUT = '/home/claude/site'
shutil.rmtree(OUT, ignore_errors=True)
os.makedirs(f'{OUT}/courses', exist_ok=True)
os.makedirs(f'{OUT}/assets', exist_ok=True)
shutil.copy('/home/claude/pdfin/badge.png', f'{OUT}/assets/logo.png')

PH, WA = '9965032227', '919965032227'
MAP = 'https://maps.app.goo.gl/d6kSKBfJiE24eaty6'
IG = 'https://www.instagram.com/eurekaacademy_s3dancestudio'
IG2 = 'https://www.instagram.com/saranya.saran.140'
FB = 'https://www.facebook.com/share/1CvqzwCpfR/'
ADDR = 'Guru Moorthy Doctor Building, Moolapalayam, Poondurai Road, Erode – 638002'
def wa(t): return f'https://wa.me/{WA}?text=' + U.quote(t)
E = html.escape

# ---------------- course data ----------------
raw = json.load(open('/tmp/courses.json'))
NAME_FIX = {'Phonics English (Adults)': 'Phonics English', 'Phonics Tamil (Adults)': 'Phonics Tamil'}
courses = []
for c in raw:
    courses.append(dict(slug=c['slug'], name=NAME_FIX.get(c['name'], c['name']), cat=c['category'],
        headline=c['headline'], short=c['shortDescription'], skills=c['skills'],
        modules=[m['title'] for m in c['curriculum']], related=c['relatedSlugs']))
courses.append(dict(slug='vocal-music', name='Vocal Music', cat='kids', headline='Find Your Voice.',
    short='Voice training, sruthi, rhythm and songs to sing with confidence.',
    skills=['Breath control', 'Pitch & sruthi', 'Rhythm', 'Stage confidence'],
    modules=['Breathing & posture', 'Sruthi & swaras', 'Rhythm & tala', 'Songs', 'Performance'],
    related=['western-dance', 'bharatanatyam', 'public-speaking']))
# Eureka-specific notes
for c in courses:
    if c['slug'] == 'tuition': c['short'] = 'Subject-wise guidance for 3rd to 12th Std, alongside the school curriculum.'; c['for'] = 'Students of 3rd to 12th Std'
    if c['slug'] == 'western-dance': c['short'] += ' At our S3 Dance Studio.'
    if c['slug'] == 'zumba': c['name'] = 'Zumba & Aerobics'
BY = {c['slug']: c for c in courses}
CATS = [('kids', 'Kids Courses', 'Language, maths, arts, sport and confidence for young learners.'),
        ('adults', 'Adult Courses', 'Craft, wellness, phonics and teacher training for adults.'),
        ('code-crackers', 'Code Crackers', 'Coding, design, media and AI skills for the digital age.')]
CATNAME = {k: n for k, n, _ in CATS}
ORDER_KIDS = ['abacus','after-school-care','bharatanatyam','boxing','chess','creative-writing','drawing','handwriting','hindi','karate','mental-maths','play-code','english-phonics','tamil-phonics','public-speaking','rubiks-cube','silambam','skating','spoken-english','tuition','vedic-maths','vocal-music','western-dance']
ORDER_AD = ['aari-work','embroidery','montessori-teacher-training','phonics-english-adults','phonics-tamil-adults','yoga','zumba']
ORDER_CC = ['web-mobile-app-development','video-editing','graphic-design','ux-ui-design','digital-marketing','ai-tools-tech','project-management']
ORDERS = {'kids': ORDER_KIDS, 'adults': ORDER_AD, 'code-crackers': ORDER_CC}
assert all(s in BY for o in ORDERS.values() for s in o), [s for o in ORDERS.values() for s in o if s not in BY]
TOTAL = sum(len(o) for o in ORDERS.values())

# ---------------- icons (minimal line set) ----------------
def ico(p, s=20): return f'<svg class="i" width="{s}" height="{s}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{p}</svg>'
I = dict(
 arrow='<path d="M5 12h14M13 6l6 6-6 6"/>', phone='<path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1.9.4 1.8.7 2.7a2 2 0 0 1-.5 2.1L8 9.8a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.7.7a2 2 0 0 1 1.7 2z"/>',
 pin='<path d="M20 10c0 6-8 12-8 12s-8-6-8-12a8 8 0 0 1 16 0z"/><circle cx="12" cy="10" r="3"/>', chat='<path d="M21 11.5a8.4 8.4 0 0 1-12.6 7.3L3 21l2.2-5.4A8.4 8.4 0 1 1 21 11.5z"/>',
 kids='<circle cx="12" cy="7" r="3"/><path d="M5 21v-1a7 7 0 0 1 14 0v1"/>', adults='<path d="M12 21c-4 0-8-3-9-8 3 0 6 1 9 4 3-3 6-4 9-4-1 5-5 8-9 8z"/><path d="M12 17c-2-3-2-7 0-11 2 4 2 8 0 11z"/>',
 code='<path d="M8 6l-6 6 6 6M16 6l6 6-6 6"/>', sun='<circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M2 12h2M20 12h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/>',
 check='<path d="M20 6 9 17l-5-5"/>', plus='<path d="M12 5v14M5 12h14"/>', menu='<path d="M4 7h16M4 12h16M4 17h16"/>', x='<path d="M6 6l12 12M18 6 6 18"/>',
 search='<circle cx="11" cy="11" r="7"/><path d="m20 20-3.5-3.5"/>', ig='<rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.5" cy="6.5" r=".8" fill="currentColor"/>',
 fb='<path d="M14 8h3V4h-3c-2.8 0-4 1.7-4 4v2H7v4h3v8h4v-8h3l1-4h-4V8.5c0-.3.2-.5.5-.5z"/>', clock='<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>',
 heart='<path d="M19 14c1.5-1.5 3-3.2 3-5.5A5.5 5.5 0 0 0 12 5.5 5.5 5.5 0 0 0 2 8.5c0 2.3 1.5 4 3 5.5l7 7z"/>', shield='<path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/>',
 spark='<path d="M12 3l1.9 5.8L20 11l-6.1 2.2L12 19l-1.9-5.8L4 11l6.1-2.2z"/>', users='<path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M22 21v-2a4 4 0 0 0-3-3.9M16 3.1a4 4 0 0 1 0 7.8"/>',
 book='<path d="M2 4h6a4 4 0 0 1 4 4v13a3 3 0 0 0-3-3H2z"/><path d="M22 4h-6a4 4 0 0 0-4 4v13a3 3 0 0 1 3-3h7z"/>', cal='<rect x="3" y="4" width="18" height="18" rx="2"/><path d="M16 2v4M8 2v4M3 10h18"/>')
CATICO = {'kids': 'kids', 'adults': 'adults', 'code-crackers': 'code'}

# ---------------- layout ----------------
def head(title, desc, root):
    return f'''<!DOCTYPE html><html lang="en-IN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{E(title)}</title><meta name="description" content="{E(desc)}">
<link rel="icon" href="{root}assets/logo.png"><link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=Plus+Jakarta+Sans:wght@500;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{root}assets/site.css"></head><body>'''

NAV = [('Home', 'index.html'), ('About', 'about.html'), ('Toddler Care', 'toddler-care.html'), ('Courses', 'courses.html'), ('Events', 'events.html'), ('Blog', 'blog.html'), ('FAQ', 'faq.html'), ('Contact', 'contact.html')]

def header(root, active):
    mega = ''.join(f'''<div class="mg-col"><a class="mg-h" href="{root}courses.html#{k}">{ico(I[CATICO[k]],18)}{n}</a><ul>{''.join(f'<li><a href="{root}courses/{s}.html">{E(BY[s]["name"])}</a></li>' for s in ORDERS[k])}</ul></div>''' for k, n, _ in CATS)
    links = ''
    for n, h in NAV:
        cur = ' aria-current="page"' if n == active else ''
        if n == 'Courses':
            links += f'<li class="has-mg"><a href="{root}{h}"{cur}>Courses<svg width="10" height="10" viewBox="0 0 10 10" aria-hidden="true"><path d="M2 4l3 3 3-3" fill="none" stroke="currentColor" stroke-width="1.5"/></svg></a><div class="mg"><div class="mg-in">{mega}</div><div class="mg-f"><a href="{root}courses.html">View all {TOTAL} courses {ico(I["arrow"],16)}</a></div></div></li>'
        else:
            links += f'<li><a href="{root}{h}"{cur}>{n}</a></li>'
    mob = ''.join(f'<a href="{root}{h}">{n}</a>' for n, h in NAV)
    return f'''<a class="skip" href="#main">Skip to content</a>
<header class="hd" id="hd"><div class="w hd-in">
<a class="brand" href="{root}index.html" aria-label="Eureka Academy home"><img src="{root}assets/logo.png" alt="" width="40" height="40"><span>Eureka<b>Academy</b></span></a>
<nav aria-label="Main"><ul class="nav">{links}</ul></nav>
<div class="hd-r"><a class="hd-ph" href="tel:+91{PH}">{ico(I["phone"],16)}99650 32227</a><a class="btn btn-dark" href="{wa("Hello Eureka Academy, I would like to enquire about admissions.")}" target="_blank" rel="noopener">Enquire</a>
<button class="mb-t" id="mbT" aria-label="Open menu" aria-expanded="false">{ico(I["menu"],22)}</button></div></div>
<div class="mb" id="mb">{mob}<a class="btn btn-dark" href="{wa("Hello Eureka Academy!")}" target="_blank" rel="noopener">WhatsApp 99650 32227</a></div></header><main id="main">'''

def footer(root):
    col = lambda t, items: f'<div><h4>{t}</h4><ul>{items}</ul></div>'
    q = ''.join(f'<li><a href="{root}{h}">{n}</a></li>' for n, h in NAV)
    ck = lambda k: ''.join(f'<li><a href="{root}courses/{s}.html">{E(BY[s]["name"])}</a></li>' for s in ORDERS[k])
    return f'''</main><footer class="ft"><div class="w">
<div class="ft-top"><div class="ft-b"><a class="brand" href="{root}index.html"><img src="{root}assets/logo.png" alt="" width="44" height="44"><span>Eureka<b>Academy</b></span></a>
<p>Learning, dance and skill development in Moolapalayam, Erode. Home of S3 Dance Studio.</p>
<p class="ft-c">{ico(I["pin"],16)}<span>{ADDR}</span></p><p class="ft-c">{ico(I["phone"],16)}<a href="tel:+91{PH}">+91 99650 32227</a></p>
<div class="soc"><a href="{IG}" target="_blank" rel="noopener" aria-label="Instagram, S3 Dance Studio">{ico(I["ig"],18)}</a><a href="{FB}" target="_blank" rel="noopener" aria-label="Facebook">{ico(I["fb"],18)}</a><a href="{wa("Hello Eureka Academy!")}" target="_blank" rel="noopener" aria-label="WhatsApp">{ico(I["chat"],18)}</a></div></div>
{col("Quick Links", q)}{col("Kids Courses", ck("kids"))}<div>{col("Adult Courses", ck("adults"))}<div style="margin-top:28px">{col("Code Crackers", ck("code-crackers"))}</div></div></div>
<div class="ft-bt"><span>© <span class="yr">2026</span> Eureka Academy &amp; S3 Dance Studio</span><span><a href="{MAP}" target="_blank" rel="noopener">Get directions</a> · <a href="{root}contact.html">Contact</a></span></div></div></footer>
<a class="fab" href="{wa("Hello Eureka Academy!")}" target="_blank" rel="noopener" aria-label="Chat on WhatsApp">{ico(I["chat"],22)}</a>
<script src="{root}assets/site.js"></script></body></html>'''

def page(path, title, desc, active, body):
    root = '../' if '/' in path else ''
    open(f'{OUT}/{path}', 'w').write(head(title, desc, root) + header(root, active) + body.replace('{R}', root) + footer(root))

def card(s, root='{R}'):
    c = BY[s]
    return f'''<a class="cc" href="{root}courses/{s}.html" data-cat="{c["cat"]}" data-q="{E((c["name"]+" "+c["short"]+" "+" ".join(c["skills"])).lower())}">
<span class="cc-t">{ico(I[CATICO[c["cat"]]],15)}{CATNAME[c["cat"]].replace(" Courses","")}</span><h3>{E(c["name"])}</h3><p>{E(c["short"])}</p><span class="cc-a">View course {ico(I["arrow"],16)}</span></a>'''

def phead(k, t, sub, extra=''):
    return f'<section class="ph"><div class="w"><p class="kick">{k}</p><h1>{t}</h1><p class="lede">{sub}</p>{extra}</div></section>'

def cta_band():
    return f'''<section class="sec"><div class="w"><div class="band"><div><h2>Ready to begin?</h2><p>Message us and we'll share batch timings, fees and the next steps.</p></div>
<div class="band-b"><a class="btn btn-dark" href="{wa("Hello Eureka Academy, I would like to enquire about admissions.")}" target="_blank" rel="noopener">{ico(I["chat"],18)}WhatsApp us</a><a class="btn btn-line" href="tel:+91{PH}">{ico(I["phone"],18)}Call 99650 32227</a></div></div></div></section>'''

FEAT = ['western-dance', 'bharatanatyam', 'abacus', 'chess', 'drawing', 'tuition']

# ---------------- HOME ----------------
home = f'''
<section class="hero"><div class="w hero-in">
<div class="hero-c">
<p class="kick"><span class="live"></span>Admissions open · Moolapalayam, Erode</p>
<h1>Where curiosity<br>becomes <em>capability.</em></h1>
<p class="lede">{TOTAL} courses for children, adults and future creators: dance, music, maths, languages, arts, coding and tuition, under one roof.</p>
<div class="row"><a class="btn btn-dark" href="{{R}}courses.html">Explore courses {ico(I["arrow"],18)}</a><a class="btn btn-line" href="{wa("Hello Eureka Academy, I would like to enquire about admissions.")}" target="_blank" rel="noopener">{ico(I["chat"],18)}WhatsApp</a></div>
<dl class="facts"><div><dt>{TOTAL}</dt><dd>Courses</dd></div><div><dt>3</dt><dd>Pathways</dd></div><div><dt>3rd–12th</dt><dd>Tuition</dd></div></dl>
</div>
<div class="hero-v" aria-hidden="true">
<div class="orb"><img src="{{R}}assets/logo.png" alt=""></div>
<a class="chip c1" href="{{R}}courses/western-dance.html" tabindex="-1">Western Dance</a><a class="chip c2" href="{{R}}courses/abacus.html" tabindex="-1">Abacus</a>
<a class="chip c3" href="{{R}}courses/tuition.html" tabindex="-1">Tuition 3rd–12th</a><a class="chip c4" href="{{R}}courses/ux-ui-design.html" tabindex="-1">UX/UI Design</a><a class="chip c5" href="{{R}}courses/yoga.html" tabindex="-1">Yoga</a>
</div></div></section>

<section class="sec"><div class="w">
<div class="sh"><div><p class="kick">Pathways</p><h2>Three ways to learn.</h2></div><a class="lnk" href="{{R}}courses.html">All courses {ico(I["arrow"],16)}</a></div>
<div class="g3">{"".join(f'<a class="path" href="{{R}}courses.html#{k}"><span class="path-i">{ico(I[CATICO[k]],22)}</span><h3>{n}</h3><p>{d}</p><span class="path-n">{len(ORDERS[k])} courses {ico(I["arrow"],16)}</span></a>' for k,n,d in CATS)}</div>
</div></section>

<section class="sec sec-alt"><div class="w">
<div class="sh"><div><p class="kick">Popular</p><h2>Start with a favourite.</h2></div><a class="lnk" href="{{R}}courses.html">View all {ico(I["arrow"],16)}</a></div>
<div class="g3">{"".join(card(s) for s in FEAT)}</div></div></section>

<section class="sec"><div class="w split">
<div><p class="kick">Toddler Care</p><h2>Little steps,<br>wonderful beginnings.</h2><p class="lede">A nurturing, play-based space where little ones explore, play, make friends and grow at their own pace.</p><a class="btn btn-line" href="{{R}}toddler-care.html">Learn about Toddler Care {ico(I["arrow"],18)}</a></div>
<ul class="ticks">{"".join(f'<li>{ico(I["check"],18)}<span><b>{a}</b>{b}</span></li>' for a,b in [("Learning through play","Stories, songs, colours and movement."),("Caring attention","Warm, patient guidance every day."),("Safe, calm spaces","Comfortable rooms designed for little ones."),("Early skills","Language, numbers and social confidence.")])}</ul>
</div></section>

<section class="sec sec-alt"><div class="w">
<div class="sh"><div><p class="kick">Why Eureka</p><h2>Learning that feels good.</h2></div></div>
<div class="g4">{"".join(f'<div class="why">{ico(I[i],22)}<h3>{t}</h3><p>{d}</p></div>' for i,t,d in [("spark","Hands-on learning","Practice, play and real-world application."),("users","Personal attention","Guidance that fits each learner's pace."),("heart","Confidence first","Dance, speaking and performance build self-belief."),("pin","Close to home","Moolapalayam, Poondurai Road, Erode.")])}</div></div></section>
{cta_band()}'''
page('index.html', 'Eureka Academy & S3 Dance Studio — Courses in Moolapalayam, Erode', f'{TOTAL} courses for kids and adults in Moolapalayam, Erode: dance, abacus, phonics, chess, tuition, coding, yoga and more.', 'Home', home)

# ---------------- COURSES ----------------
sections = ''.join(f'''<section class="cat" id="{k}"><div class="sh"><div><h2>{n}</h2><p class="muted">{d}</p></div><span class="count">{len(ORDERS[k])} courses</span></div><div class="g3">{"".join(card(s) for s in ORDERS[k])}</div></section>''' for k, n, d in CATS)
filters = '<button aria-pressed="true" data-f="all">All</button>' + ''.join(f'<button aria-pressed="false" data-f="{k}">{n.replace(" Courses","")}</button>' for k, n, _ in CATS)
courses_body = phead('All Courses', f'{TOTAL} courses, one academy.', 'Browse by pathway or search by name or skill. Every course has its own page with what you will learn.') + f'''
<section class="sec" style="padding-top:20px"><div class="w">
<div class="tools"><div class="seg" role="group" aria-label="Filter by pathway">{filters}</div><label class="srch">{ico(I["search"],18)}<span class="sr">Search courses</span><input id="q" type="search" placeholder="Search courses or skills"></label></div>
<p class="muted sm" id="cnt" aria-live="polite"></p><div id="cats">{sections}</div>
<div class="empty" id="empty" hidden><h3>No courses match</h3><p class="muted">Try another word, or <a href="{wa("Hello Eureka Academy, I am looking for a course.")}" target="_blank" rel="noopener">ask us on WhatsApp</a>.</p></div>
</div></section>{cta_band()}'''
page('courses.html', f'All Courses ({TOTAL}) — Eureka Academy, Erode', 'Kids courses, adult courses and Code Crackers digital skills at Eureka Academy, Moolapalayam, Erode.', 'Courses', courses_body)

# ---------------- COURSE PAGES ----------------
for k in ORDERS:
    for s in ORDERS[k]:
        c = BY[s]
        rel = [r for r in c['related'] if r in BY][:3]
        if len(rel) < 3: rel += [x for x in ORDERS[k] if x != s and x not in rel][:3 - len(rel)]
        msg = f'Hello Eureka Academy, I would like to know more about {c["name"]} ({CATNAME[k]}). Please share batch timings and fees.'
        body = f'''<section class="ph ph-c"><div class="w ch">
<nav class="bc" aria-label="Breadcrumb"><a href="../index.html">Home</a><span>/</span><a href="../courses.html#{k}">{CATNAME[k]}</a><span>/</span><span aria-current="page">{E(c["name"])}</span></nav>
<div class="ch-g"><div><p class="kick">{ico(I[CATICO[k]],16)}{CATNAME[k]}</p><h1>{E(c["name"])}</h1><p class="ch-hl">{E(c["headline"])}</p><p class="lede">{E(c["short"])}</p>
<div class="row"><a class="btn btn-dark" href="{wa(msg)}" target="_blank" rel="noopener">{ico(I["chat"],18)}Enquire on WhatsApp</a><a class="btn btn-line" href="tel:+91{PH}">{ico(I["phone"],18)}Call us</a></div></div>
<aside class="facts-card"><h2 class="sr">Course details</h2><dl>
<div><dt>{ico(I["users"],18)}Who it's for</dt><dd>{E(c.get("for", {"kids":"Children","adults":"Adults","code-crackers":"Teens & adults"}[k]))}</dd></div>
<div><dt>{ico(I["clock"],18)}Batch timings</dt><dd>Contact us for current slots</dd></div>
<div><dt>{ico(I["cal"],18)}Duration &amp; fees</dt><dd>Shared on enquiry</dd></div>
<div><dt>{ico(I["pin"],18)}Where</dt><dd>Moolapalayam, Erode</dd></div></dl></aside></div></div></section>

<section class="sec"><div class="w g-2">
<div><p class="kick">Curriculum</p><h2>What you'll learn</h2><ol class="mods">{"".join(f'<li><span>{i:02d}</span><b>{E(m)}</b></li>' for i, m in enumerate(c["modules"], 1))}</ol><p class="muted sm">Proposed outline. The final syllabus is confirmed by Eureka Academy.</p></div>
<div><p class="kick">Outcomes</p><h2>Skills you'll build</h2><ul class="ticks">{"".join(f'<li>{ico(I["check"],18)}<span><b>{E(x)}</b></span></li>' for x in c["skills"])}</ul>
<div class="faq-mini"><details><summary>Is there a demo or trial class?{ico(I["plus"],18)}</summary><p>Please message us on WhatsApp and we'll let you know about trial options for {E(c["name"])}.</p></details>
<details><summary>What are the fees and timings?{ico(I["plus"],18)}</summary><p>Fees and batch timings are shared on enquiry, so you always get the current details.</p></details></div></div></div></section>

<section class="sec sec-alt"><div class="w"><div class="sh"><div><p class="kick">Explore more</p><h2>Related courses</h2></div><a class="lnk" href="../courses.html">All courses {ico(I["arrow"],16)}</a></div><div class="g3">{"".join(card(r, "../") for r in rel)}</div></div></section>
{cta_band()}'''
        page(f'courses/{s}.html', f'{c["name"]} Classes in Erode — Eureka Academy', f'{c["short"]} {c["name"]} at Eureka Academy, Moolapalayam, Erode.', 'Courses', body)

# ---------------- ABOUT ----------------
about = phead('About Eureka', 'Where curiosity finds its direction.', 'Eureka Academy is a learning and skill development centre in Moolapalayam, Erode, and home of S3 Dance Studio.') + f'''
<section class="sec"><div class="w g-2">
<div><h2>Our approach</h2><p class="lede">We believe every learner is a natural explorer. Classes focus on doing, practising and creating, so skills grow with confidence.</p></div>
<ul class="ticks">{"".join(f'<li>{ico(I["check"],18)}<span><b>{a}</b>{b}</span></li>' for a,b in [("Mission","Make meaningful, hands-on learning accessible at every stage of life."),("Vision","A community where curiosity becomes capability."),("Our studio","S3 Dance Studio brings dance, music and fitness under the same roof."),("Our centre","Guru Moorthy Doctor Building, Poondurai Road, Moolapalayam.")])}</ul>
</div></section>
<section class="sec sec-alt"><div class="w"><div class="sh"><div><p class="kick">What we offer</p><h2>Three pathways.</h2></div></div>
<div class="g3">{"".join(f'<a class="path" href="courses.html#{k}"><span class="path-i">{ico(I[CATICO[k]],22)}</span><h3>{n}</h3><p>{d}</p><span class="path-n">{len(ORDERS[k])} courses {ico(I["arrow"],16)}</span></a>' for k,n,d in CATS)}</div></div></section>
<section class="sec"><div class="w"><div class="note">Our story, team and milestones will be added here once shared by Eureka Academy.</div></div></section>{cta_band()}'''
page('about.html', 'About Eureka Academy — Moolapalayam, Erode', 'About Eureka Academy & S3 Dance Studio, a learning and skill development centre in Moolapalayam, Erode.', 'About', about)

# ---------------- TODDLER CARE ----------------
tod = phead('Toddler Care', 'Little steps, wonderful beginnings.', 'A nurturing, play-based early learning space designed to encourage curiosity, play and meaningful connections.',
    f'<div class="row"><a class="btn btn-dark" href="{wa("Hello Eureka Academy, I would like to know about Toddler Care admissions.")}" target="_blank" rel="noopener">{ico(I["chat"],18)}Enquire about Toddler Care</a></div>') + f'''
<section class="sec"><div class="w"><div class="sh"><div><p class="kick">The program</p><h2>A day full of gentle discovery.</h2></div></div>
<div class="g4">{"".join(f'<div class="why">{ico(I[i],22)}<h3>{t}</h3><p>{d}</p></div>' for i,t,d in [("sun","Learning through play","Play-based activities that build curiosity and motor skills."),("book","Early learning","Sounds, words, numbers, shapes and colours."),("spark","Creative time","Art, music, stories and pretend play."),("users","Social skills","Sharing, friendship and confidence with others.")])}</div></div></section>
<section class="sec sec-alt"><div class="w g-2">
<div><p class="kick">Daily rhythm</p><h2>A calm, happy routine.</h2><p class="muted">An example flow. Actual timings are shared on enquiry.</p></div>
<ol class="mods">{"".join(f'<li><span>{i:02d}</span><b>{t}</b></li>' for i,t in enumerate(["Welcome & free play","Circle time: songs and stories","Activity: art, sensory or movement","Snack & rest","Outdoor or indoor play","Pick-up"],1))}</ol></div></section>
<section class="sec"><div class="w g-2">
<div><p class="kick">Safety &amp; care</p><h2>Peace of mind for parents.</h2><p class="lede">A clean, comfortable and closely supervised environment for every child.</p></div>
<div class="note">Age eligibility, timings, caregiver details and facilities will be listed here once confirmed by Eureka Academy.</div></div></section>
<section class="sec sec-alt"><div class="w narrow"><p class="kick">Parent FAQs</p><h2>Questions parents ask.</h2><div class="faq">{"".join(f'<details><summary>{q}{ico(I["plus"],18)}</summary><p>{a}</p></details>' for q,a in [("What age can my child join?","Please contact us for current age eligibility."),("What are the timings?","Half-day and full-day options are shared on enquiry."),("Can we visit before joining?","Yes. Message or call us to arrange a visit to the centre."),("What should my child bring?","We'll share a simple checklist when you enquire.")])}</div></div></section>{cta_band()}'''
page('toddler-care.html', 'Toddler Care in Moolapalayam, Erode — Eureka Academy', 'Play-based toddler care at Eureka Academy, Moolapalayam, Erode.', 'Toddler Care', tod)

# ---------------- EVENTS / BLOG / FAQ / CONTACT ----------------
page('events.html', 'Events & Workshops — Eureka Academy', 'Upcoming events, workshops and summer camps at Eureka Academy, Erode.', 'Events',
 phead('Events', 'Workshops, camps &amp; celebrations.', 'Only real, upcoming events are listed here.') + f'''<section class="sec" style="padding-top:20px"><div class="w"><div class="empty">{ico(I["cal"],28)}<h3>No upcoming events right now</h3><p class="muted">New workshops and summer camps will be announced here and on <a href="{IG}" target="_blank" rel="noopener">Instagram</a>.</p>
<a class="btn btn-dark" href="{wa("Hello Eureka Academy, please notify me about upcoming events and summer camps.")}" target="_blank" rel="noopener">Notify me on WhatsApp</a></div></div></section>{cta_band()}''')
page('blog.html', 'Blog — Eureka Academy', 'Learning ideas from Eureka Academy.', 'Blog',
 phead('Blog', 'Ideas for curious minds.', 'Articles on learning, parenting, dance and skills.') + f'''<section class="sec" style="padding-top:20px"><div class="w"><div class="empty">{ico(I["book"],28)}<h3>Articles coming soon</h3><p class="muted">We're preparing our first posts. Meanwhile, follow class moments on <a href="{IG}" target="_blank" rel="noopener">@eurekaacademy_s3dancestudio</a>.</p></div></div></section>{cta_band()}''')
FAQS = [('General', [('Where is Eureka Academy?', f'{ADDR}. <a href="{MAP}" target="_blank" rel="noopener">Get directions</a>.'), ('How do I contact you?', 'Call or WhatsApp <a href="tel:+919965032227">+91 99650 32227</a>.')]),
        ('Courses', [('How many courses do you offer?', f'{TOTAL} courses across Kids, Adults and Code Crackers. <a href="courses.html">Browse all courses</a>.'), ('How do I choose the right course?', 'Message us with the learner\'s age and interests and we\'ll suggest a fit.'), ('Do you offer tuition?', 'Yes, subject-wise tuition for 3rd to 12th Std.')]),
        ('Admissions & fees', [('How do I enrol?', 'Message us on WhatsApp, visit the centre and join your batch.'), ('What are the fees?', 'Fees vary by course and are shared on enquiry.'), ('Are there demo classes?', 'Please ask us on WhatsApp about trial options.')]),
        ('Timings', [('What are the batch timings?', 'Batch timings vary by course. Contact us for current slots.')])]
faq_body = phead('FAQ', 'Questions, answered.', "Can't find what you need? Message us any time.") + f'''<section class="sec" style="padding-top:20px"><div class="w narrow">
<label class="srch" style="margin-bottom:34px">{ico(I["search"],18)}<span class="sr">Search questions</span><input id="fq" type="search" placeholder="Search questions"></label>
{"".join(f'<div class="faq-g"><h2 class="h3">{g}</h2><div class="faq">{"".join(f"<details><summary>{q}{ico(I['plus'],18)}</summary><p>{a}</p></details>" for q,a in items)}</div></div>' for g,items in FAQS)}
<div class="empty" id="fempty" hidden><h3>No matching questions</h3><p class="muted"><a href="{wa("Hello Eureka Academy, I have a question.")}" target="_blank" rel="noopener">Ask us on WhatsApp</a></p></div></div></section>{cta_band()}'''
page('faq.html', 'FAQ — Eureka Academy, Erode', 'Answers about courses, admissions, fees and timings at Eureka Academy.', 'FAQ', faq_body)
opts = ''.join(f'<optgroup label="{n}">' + ''.join(f'<option>{E(BY[s]["name"])}</option>' for s in ORDERS[k]) + '</optgroup>' for k, n, _ in CATS)
contact = phead('Contact', "Let's talk.", 'Questions about courses, admissions or a visit? We usually reply quickly on WhatsApp.') + f'''<section class="sec" style="padding-top:20px"><div class="w g-2 ct">
<div class="ct-l">
<a class="ct-r" href="{MAP}" target="_blank" rel="noopener">{ico(I["pin"],20)}<span><small>Address</small>{ADDR}<em>Open in Google Maps →</em></span></a>
<a class="ct-r" href="tel:+91{PH}">{ico(I["phone"],20)}<span><small>Phone</small>+91 99650 32227</span></a>
<a class="ct-r" href="{wa("Hello Eureka Academy!")}" target="_blank" rel="noopener">{ico(I["chat"],20)}<span><small>WhatsApp</small>+91 99650 32227</span></a>
<a class="ct-r" href="{IG}" target="_blank" rel="noopener">{ico(I["ig"],20)}<span><small>Instagram</small>@eurekaacademy_s3dancestudio</span></a>
<a class="ct-r" href="{IG2}" target="_blank" rel="noopener">{ico(I["ig"],20)}<span><small>Instagram</small>@saranya.saran.140</span></a>
<a class="ct-r" href="{FB}" target="_blank" rel="noopener">{ico(I["fb"],20)}<span><small>Facebook</small>Eureka Academy</span></a></div>
<form class="form" id="enq" novalidate><h2 class="h3">Send an enquiry</h2>
<label>Name *<input id="fn" autocomplete="name"><small class="er" id="en"></small></label>
<label>Phone *<input id="fp" type="tel" inputmode="tel" placeholder="98765 43210"><small class="er" id="ep"></small></label>
<label>Course *<select id="fc"><option value="">Choose a course</option><option>Toddler Care</option>{opts}</select><small class="er" id="ec"></small></label>
<label>Learner age / class<input id="fa" placeholder="e.g. 8 years or 6th Std"></label>
<label>Message<textarea id="fm" rows="3"></textarea></label>
<button class="btn btn-dark" type="submit">{ico(I["chat"],18)}Send on WhatsApp</button><a id="wl" hidden target="_blank" rel="noopener">open</a>
<p class="muted sm">Opens WhatsApp with your message ready to send.</p></form></div></section>'''
page('contact.html', 'Contact Eureka Academy — Moolapalayam, Erode', f'Contact Eureka Academy: {ADDR}. Phone and WhatsApp +91 99650 32227.', 'Contact', contact)
print('pages:', len(os.listdir(OUT)) - 1 + len(os.listdir(OUT + '/courses')), 'courses:', TOTAL)
