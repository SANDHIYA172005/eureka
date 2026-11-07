"""Adds: themed stage on every course page, room pages, minimal reference-style home."""
import json, re, html
exec(open('/home/claude/sitegen/build.py').read())   # builds base site, gives helpers
exec(open('/home/claude/sitegen/concepts.py').read())
VIS = json.load(open('/home/claude/sitegen/visuals.json'))
STAGE_CSS = open('/home/claude/sitegen/stage.css').read()

# ---- map every course to a stage visual ----
MAP_V = {'western-dance':'western','bharatanatyam':'classical','vocal-music':'vocal','zumba':'zumba','drawing':'drawing','abacus':'abacus',
 'handwriting':'english',
 'chess':'chess','hindi':'hindi','tuition':'tuition','montessori-teacher-training':'montessori'}
# generic themed stages: (bg gradient, glyph, light?)
GEN = {
 'tamil-phonics':('linear-gradient(135deg,#FFF1E6,#FFD9B8)','அ',0),'phonics-tamil-adults':('linear-gradient(135deg,#FFF1E6,#FFD9B8)','ஆ',0),
 'public-speaking':('linear-gradient(135deg,#1E3A8A,#3B82F6)','🎤',1),'mental-maths':('linear-gradient(135deg,#ECFDF5,#A7F3D0)','12+29',0),
 'vedic-maths':('linear-gradient(135deg,#FEF9C3,#FDE68A)','98×97',0),'rubiks-cube':('linear-gradient(135deg,#111827,#374151)','🟥🟨🟦',1),
 'play-code':('linear-gradient(135deg,#EDE9FE,#C4B5FD)','🧩',0),'boxing':('linear-gradient(135deg,#7F1D1D,#DC2626)','🥊',1),
 'karate':('linear-gradient(135deg,#F5F5F4,#D6D3D1)','🥋',0),'silambam':('linear-gradient(135deg,#78350F,#B45309)','🥢',1),
 'skating':('linear-gradient(135deg,#0EA5E9,#67E8F9)','🛼',1),'after-school-care':('linear-gradient(135deg,#FEF3C7,#FDBA74)','🏫',0),
 'aari-work':('linear-gradient(135deg,#4C0519,#9F1239)','🪡',1),'embroidery':('linear-gradient(135deg,#FDF2F8,#FBCFE8)','🧵',0),
 'yoga':('linear-gradient(135deg,#ECFDF5,#BBF7D0)','🧘',0)}
CODE = {'web-mobile-app-development':['<section class="hero">','  <h1>My First App</h1>','  <button>Launch</button>','</section>'],
 'video-editing':['timeline.add(clip1)','timeline.cut(00:12)','apply("fade")','export("final.mp4")'],
 'graphic-design':['poster.font = "Bold"','poster.color = #E3A008','layout.grid(12)','export("poster.png")'],
 'ux-ui-design':['wireframe.create()','user.research()','prototype.link(screens)','test.with(users)'],
 'digital-marketing':['campaign.target(audience)','post.schedule("9am")','seo.keywords([...])','report.reach()'],
 'ai-tools-tech':['ai.ask("Summarise this")','ai.create(image)','check(result)','use.responsibly()'],
 'project-management':['board.add("Plan")','task.move("Doing")','milestone.complete()','team.celebrate()']}

def stage(s, active=True, idx=0):
    c = BY[s]; k = c['cat']
    msg = wa(f'Hello Eureka Academy, I would like to know more about {c["name"]}. Please share batch timings and fees.')
    chips = ''.join(f'<li>{E(x)}</li>' for x in c['skills'][:3])
    if s in C:
        bg, light, vis = C[s]; cls = 'st-g" style="background:'+bg
    elif s in MAP_V:
        cls, vis = VIS[MAP_V[s]]; light = cls in ('st-w','st-v','st-z','st-ch','st-t')
    elif s in CODE:
        cls = 'st-cd'; light = True
        lines = ''.join(f'<p style="animation-delay:{.3+i*.35}s"><span>{i+1}</span>{E(l)}</p>' for i, l in enumerate(CODE[s]))
        vis = f'<div class="cd-grid"></div><div class="term"><div class="dots"><i></i><i></i><i></i></div>{lines}<b class="caret"></b></div>'
    else:
        bg, g, light = GEN[s]; cls = 'st-g'
        big = f'<span class="g-big{" txt" if len(g)>3 or g[0].isdigit() else ""}">{g}</span>'
        vis = f'<div class="g-ring"></div><div class="g-ring r2"></div>{big}' + ''.join(f'<span class="g-chip" style="--d:{i*1.2}s;--x:{x}%;--y:{y}%">{E(t)}</span>' for i,(t,x,y) in enumerate(zip(c['skills'][:3],[6,30,10],[14,30,76])))
        cls += f'" style="background:{bg}'
    return f'''<article class="{cls}" data-s="{s}" role="tabpanel"{"" if active else " hidden"}>{vis}
<div class="st-copy{" light" if light else ""}"><p class="st-k">{CATNAME[k]}</p><h3>{E(c["name"])}</h3><p>{E(c["short"])}</p><ul>{chips}</ul>
<div class="st-act"><a class="st-cta" href="{msg}" target="_blank" rel="noopener">Enquire on WhatsApp →</a>{'' if not idx else f'<a class="st-more" href="{{R}}courses/{s}.html">Full course page →</a>'}</div></div></article>'''

EXTRA_CSS = STAGE_CSS + '''
.stage-wrap{position:relative;min-height:520px;border-radius:28px;overflow:hidden}
.stage-wrap>article{position:absolute;inset:0;display:grid;grid-template-columns:1.05fr 1fr;align-items:center;gap:20px;padding:44px;overflow:hidden;animation:stIn .55s cubic-bezier(.2,.7,.2,1)}
.stage-wrap>article[hidden]{display:none}
.stage-wrap .st-copy h3{font-family:var(--f-head)}
.st-act{display:flex;flex-wrap:wrap;gap:10px;align-items:center;margin-top:24px}.st-act .st-cta{margin-top:0}
.st-more{font-weight:600;font-size:14.5px;padding:12px 4px}.light .st-more{color:#fff}
/* generic */
.st-g{color:var(--ink)}.g-big{position:relative;z-index:2;margin:auto;font-size:120px;line-height:1;animation:float 5s ease-in-out infinite;filter:drop-shadow(0 20px 30px rgba(0,0,0,.18))}
.g-big.txt{font:800 64px var(--f-head);letter-spacing:-.03em;color:#16130F;background:#fff;padding:24px 34px;border-radius:28px;box-shadow:0 30px 50px -30px rgba(0,0,0,.4)}
.g-ring{position:absolute;left:25%;top:50%;width:340px;height:340px;margin:-170px 0 0 -170px;border-radius:50%;border:2px dashed rgba(255,255,255,.55);animation:spn 40s linear infinite}.g-ring.r2{width:240px;height:240px;margin:-120px 0 0 -120px;border-style:solid;border-color:rgba(255,255,255,.35);animation-direction:reverse}
.g-chip{position:absolute;left:var(--x);top:var(--y);z-index:3;padding:8px 14px;border-radius:999px;background:rgba(255,255,255,.9);font-weight:600;font-size:13.5px;color:#16130F;box-shadow:0 10px 20px -12px rgba(0,0,0,.4);animation:float 6s var(--d) ease-in-out infinite}
@keyframes spn{to{transform:rotate(360deg)}}@keyframes float{50%{transform:translateY(-10px)}}@keyframes stIn{from{opacity:0;transform:scale(.98)}}
/* code */
.st-cd{background:radial-gradient(70% 70% at 20% 50%,#2E2A6B,#0F1029)}
.cd-grid{position:absolute;inset:0;background-image:linear-gradient(rgba(104,220,235,.07) 1px,transparent 1px),linear-gradient(90deg,rgba(104,220,235,.07) 1px,transparent 1px);background-size:40px 40px}
.term{position:relative;z-index:2;margin:auto;width:100%;max-width:380px;background:#151634;border:1px solid rgba(255,255,255,.12);border-radius:18px;padding:20px 22px;font:14px/2 ui-monospace,Menlo,monospace;color:#7DE3EE;box-shadow:0 30px 60px -30px #000}
.term .dots{display:flex;gap:6px;margin-bottom:10px}.term .dots i{width:11px;height:11px;border-radius:50%;background:#FF6B6B}.term .dots i:nth-child(2){background:#FFD166}.term .dots i:nth-child(3){background:#4ADE80}
.term p{opacity:0;animation:typ .5s forwards;white-space:nowrap;overflow:hidden}.term p span{color:#ffffff40;margin-right:14px}@keyframes typ{to{opacity:1}}
.caret{display:inline-block;width:8px;height:16px;background:#7DE3EE;animation:bl 1s steps(2) infinite}@keyframes bl{50%{opacity:0}}
/* room explorer */
.rx{display:grid;grid-template-columns:260px 1fr;gap:20px}
.rx-list{display:flex;flex-direction:column;gap:6px;padding:12px;border:1px solid var(--line);border-radius:24px;background:#fff;align-self:start;position:sticky;top:96px}
.rx-list button{display:flex;align-items:center;gap:12px;min-height:48px;padding:0 14px;border:0;border-radius:14px;background:none;text-align:left;font:500 15px var(--f-body);cursor:pointer;color:var(--ink2)}
.rx-list button:hover{background:var(--alt)}.rx-list button[aria-selected=true]{background:var(--ink);color:#fff}
.rx-list button{gap:12px}.rx-list .bi{display:grid;place-items:center;width:34px;height:34px;border-radius:10px;background:color-mix(in srgb,var(--rc) 14%,#fff);font-size:17px;font-weight:700;color:var(--rc);flex:none;transition:.2s}
.rx-list small{margin-left:auto;font-size:11.5px;color:var(--muted);font-weight:600}
.rx-list button:hover .bi{transform:rotate(-6deg) scale(1.08)}
.rx-list button[aria-selected=true]{background:var(--rc);color:#fff;box-shadow:0 12px 24px -14px var(--rc)}.rx-list button[aria-selected=true] .bi{background:rgba(255,255,255,.22);color:#fff}.rx-list button[aria-selected=true] small{color:rgba(255,255,255,.8)}
.map .rm text{fill:#fff;font-family:var(--f-head);font-weight:700}.map .rm:hover path,.map .rm:focus path{filter:brightness(1.08)}
/* home: minimal reference layout */
.sky{position:relative;overflow:hidden;background:linear-gradient(180deg,#F2F8FC 0%,#FAFCF8 55%,#EEF6E6 100%)}
.sky .cl{position:absolute;opacity:.9;animation:drift 50s ease-in-out infinite}@keyframes drift{50%{transform:translateX(40px)}}
.hills{position:absolute;left:0;right:0;bottom:0;width:100%;height:260px}
.sky-in{position:relative;z-index:2;display:grid;grid-template-columns:1.1fr .9fr;gap:48px;align-items:center;padding:72px 0 150px}
.sky h1{font-size:clamp(2.4rem,1.3rem + 3.4vw,4rem);font-weight:500;letter-spacing:-.035em;line-height:1.1;margin-top:12px}.sky h1 b{display:block;font-weight:800}
.pop{position:relative;display:grid;grid-template-columns:1fr 48px;border-radius:26px;background:#fff;border:1px solid var(--line);box-shadow:0 30px 60px -36px rgba(22,19,15,.45);overflow:hidden;height:330px}
.pop-s{position:absolute;inset:0;right:48px;padding:24px;display:flex;flex-direction:column;opacity:0;transition:opacity .5s;pointer-events:none}.pop-s.on{opacity:1;pointer-events:auto}
.pop-art{flex:1;border-radius:18px;background:var(--bg);display:grid;place-items:center;font-size:64px}
.pop-s small{margin-top:16px;font-weight:600;font-size:12px;letter-spacing:.1em;text-transform:uppercase;color:var(--gold)}.pop-s h3{font-size:21px;margin-top:2px}.pop-s a{margin-top:8px;font-weight:600;font-size:14.5px;display:inline-flex;gap:6px;align-items:center}
.pop-side{grid-column:2;border-left:1px solid var(--line);display:flex;flex-direction:column;align-items:center;justify-content:space-between;padding:16px 0;background:var(--alt)}
.pop-side b{writing-mode:vertical-rl;font:700 12px var(--f-head);letter-spacing:.16em}.pop-side span{writing-mode:vertical-rl;font-size:12px;color:var(--muted)}
.pop-side button{width:30px;height:30px;border-radius:50%;border:1px solid var(--line);background:#fff;cursor:pointer}
.qb{position:relative;z-index:3;margin-top:-100px;display:grid;grid-template-columns:280px 1fr;border-radius:24px;overflow:hidden;background:#fff;border:1px solid var(--line);box-shadow:0 30px 60px -40px rgba(22,19,15,.5)}
.qb-l{display:flex;gap:16px;align-items:center;padding:24px;background:var(--ink);color:#fff}.qb-l h3{color:#fff;font-size:20px}.qb-l p{font-size:13px;color:#BDB6AC;margin-top:2px}
.cal{width:70px;flex:none;text-align:center;border-radius:14px;background:#fff;color:var(--ink);overflow:hidden}.cal i{display:block;font-style:normal;font-size:11px;font-weight:600;padding-top:7px;color:var(--muted)}.cal b{display:block;font:800 24px/1.1 var(--f-head)}.cal em{display:block;font-style:normal;font-size:10.5px;font-weight:600;background:var(--gold-soft);color:#7A5600;padding:3px 0;margin-top:4px}
.qb-r{display:grid;grid-template-columns:repeat(4,1fr)}.qb-r a{display:flex;flex-direction:column;align-items:center;justify-content:center;gap:4px;padding:18px 10px;text-align:center;border-left:1px solid var(--line);transition:background .2s}.qb-r a:first-child{border:0}.qb-r a:hover{background:var(--alt)}
.qb-r b{font:700 15.5px var(--f-head)}.qb-r span{font-size:12.5px;color:var(--muted)}.qb-r em{font-style:normal;font-size:12.5px;font-weight:600;margin-top:4px;padding:4px 12px;border:1px solid var(--line);border-radius:999px}
.inf{display:grid;grid-template-columns:repeat(3,1fr);margin-top:44px}.inf>div{padding:0 28px;border-left:1px solid var(--line)}.inf>div:first-child{padding-left:0;border:0}
.inf h4{display:flex;gap:8px;align-items:center;font:700 15px var(--f-head)}.inf h4 .i{color:var(--gold)}.inf p{margin-top:8px;font-size:14.5px;color:var(--muted)}.inf .big{font:800 22px var(--f-head);color:var(--ink)}
.village{display:grid;grid-template-columns:1.25fr .75fr;gap:40px;align-items:center}
.map{width:100%}.map .rm{cursor:pointer;transition:transform .3s}.map .rm:hover,.map .rm:focus{transform:translateY(-6px);outline:none}
.map .rm text{font:700 13px var(--f-head);fill:#fff;pointer-events:none}
.rlist{display:grid;gap:10px}.rlist a{display:flex;align-items:center;gap:16px;padding:16px 18px;border:1px solid var(--line);border-radius:18px;background:#fff;transition:.2s}.rlist a:hover{border-color:var(--ink);transform:translateX(4px)}
.rlist .n{display:grid;place-items:center;width:30px;height:30px;border-radius:50%;color:#fff;font:700 13px var(--f-head);background:var(--c)}.rlist b{display:block;font-weight:600}.rlist small{color:var(--muted);font-size:13.5px}.rlist .i{margin-left:auto;color:var(--muted)}
.bk3{display:grid;grid-template-columns:repeat(3,1fr);gap:20px}.bk{position:relative;overflow:hidden;min-height:200px;padding:30px;border-radius:24px;background:var(--c);color:#fff;transition:transform .25s}.bk:hover{transform:translateY(-4px)}
.bk h3{color:#fff;font-size:22px}.bk p{margin-top:6px;font-size:14.5px;opacity:.9;max-width:240px}.bk span{position:absolute;left:30px;bottom:26px;display:inline-flex;gap:6px;align-items:center;padding:8px 16px;border:1px solid rgba(255,255,255,.6);border-radius:999px;font-weight:600;font-size:14px}.bk em{position:absolute;right:24px;bottom:18px;font-size:64px;font-style:normal;opacity:.95}
.upd{border-top:2px solid var(--ink)}.upd li{border-bottom:1px solid var(--line)}.upd a{display:flex;gap:14px;align-items:center;padding:18px 0;font-weight:500}.upd a:hover{color:var(--gold)}.upd .nw{display:grid;place-items:center;width:22px;height:22px;border-radius:50%;background:#E11D48;color:#fff;font-size:11px;font-weight:700}.upd em{margin-left:auto;font-style:normal;font-size:13px;color:var(--muted)}
.sea{position:relative;height:150px;margin-top:40px;overflow:hidden}.sea svg{position:absolute;inset:0;width:100%;height:100%}
.ft{margin-top:0}
@media(max-width:900px){.stage-wrap>article{position:relative;inset:auto;grid-template-columns:1fr;padding:28px 22px}.stage-wrap{min-height:0}.st-copy{order:2;grid-column:1!important}.g-ring{left:50%}.g-big{font-size:90px}.g-big.txt{font-size:44px}
 .rx{grid-template-columns:1fr}.rx-list{position:static;flex-direction:row;overflow-x:auto;border-radius:18px;scrollbar-width:none}.rx-list button{flex:0 0 auto}
 .sky-in,.village{grid-template-columns:1fr}.sky-in{padding-bottom:130px}.qb{grid-template-columns:1fr}.qb-r{grid-template-columns:1fr 1fr}.qb-r a:nth-child(3){border-left:0}.qb-r a:nth-child(n+3){border-top:1px solid var(--line)}.inf{grid-template-columns:1fr;gap:20px}.inf>div{padding:0;border:0}.bk3{grid-template-columns:1fr}}
'''
open(f'{OUT}/assets/stage.css','w').write(EXTRA_CSS+CSS+'@media(max-width:900px){.g-chip{display:none}}')

STAGE_JS = r'''(function(){
// room explorer tabs
document.querySelectorAll('.rx').forEach(function(rx){var bs=rx.querySelectorAll('.rx-list button'),ps=rx.querySelectorAll('.stage-wrap>article');
 function show(k){bs.forEach(function(b){b.setAttribute('aria-selected',b.dataset.k===k)});ps.forEach(function(p){p.hidden=p.dataset.s!==k});history.replaceState(null,'','#'+k)}
 bs.forEach(function(b){b.addEventListener('click',function(){show(b.dataset.k)})});var h=location.hash.slice(1);if(h&&rx.querySelector('[data-k="'+h+'"]'))show(h)});
// abacus
document.querySelectorAll('.ab-frame').forEach(function(f){var out=f.parentNode.querySelector('.ab-val b');function v(){var t=0;f.querySelectorAll('.rod').forEach(function(r){t+=r.querySelectorAll('.bead[aria-pressed=true]').length*+r.dataset.pv});out.textContent=t.toLocaleString('en-IN')}
 f.querySelectorAll('.rod').forEach(function(r){var bs=[].slice.call(r.querySelectorAll('.bead'));bs.forEach(function(b,i){b.onclick=function(){var up=b.getAttribute('aria-pressed')!=='true';bs.forEach(function(x,j){if(up?j>=i:j<=i)x.setAttribute('aria-pressed',up)});v()}})})});
// chess
document.querySelectorAll('.board').forEach(function(bd){var kn=[1,7];function draw(){bd.innerHTML='';var mv={};[[1,2],[2,1],[-1,2],[-2,1],[1,-2],[2,-1],[-1,-2],[-2,-1]].forEach(function(d){var x=kn[0]+d[0],y=kn[1]+d[1];if(x>=0&&x<8&&y>=0&&y<8)mv[x+','+y]=1});
 for(var y=0;y<8;y++)for(var x=0;x<8;x++)(function(x,y){var b=document.createElement('button');b.type='button';b.className=(x+y)%2?'d':'l';var sq='abcdefgh'[x]+(8-y);if(x===kn[0]&&y===kn[1]){b.textContent='♞';b.classList.add('kn');b.setAttribute('aria-label','Knight on '+sq)}else if(mv[x+','+y]){b.classList.add('mv');b.setAttribute('aria-label','Move to '+sq);b.onclick=function(){kn=[x,y];draw()}}else{b.tabIndex=-1;b.setAttribute('aria-label',sq)}bd.appendChild(b)})(x,y)}draw()});
// letters
document.querySelectorAll('.h-letters').forEach(function(L){var out=L.parentNode.querySelector('.h-word');L.querySelectorAll('button').forEach(function(b){b.onclick=function(){L.querySelectorAll('button').forEach(function(x){x.setAttribute('aria-pressed',x===b)});out.textContent=b.textContent+' for '+b.dataset.w}})});
// tuition
var S={3:['English','Tamil','Maths','EVS'],4:['English','Tamil','Maths','EVS'],5:['English','Tamil','Maths','Science','Social'],6:['English','Tamil','Maths','Science','Social'],7:['English','Tamil','Maths','Science','Social'],8:['English','Tamil','Maths','Science','Social'],9:['English','Tamil','Maths','Science','Social'],10:['English','Tamil','Maths','Science','Social'],11:['Maths','Physics','Chemistry','Biology','Accountancy','Commerce'],12:['Maths','Physics','Chemistry','Biology','Accountancy','Commerce']};
document.querySelectorAll('.chalk').forEach(function(c){var gs=c.querySelectorAll('.grades button'),sb=c.querySelector('.subs');function g(n){gs.forEach(function(b){b.setAttribute('aria-pressed',+b.dataset.g===n)});sb.innerHTML=S[n].map(function(s,i){return '<span style="animation-delay:'+i*.06+'s">'+s+'</span>'}).join('')}gs.forEach(function(b){b.onclick=function(){g(+b.dataset.g)}});g(6)});
// swatches
document.querySelectorAll('.swatches').forEach(function(w){var sp=w.parentNode.querySelector('.splash');w.querySelectorAll('button').forEach(function(b){b.onclick=function(){w.querySelectorAll('button').forEach(function(x){x.setAttribute('aria-pressed',x===b)});sp.setAttribute('fill',getComputedStyle(b).getPropertyValue('--c').trim())}})});
// home popup + date
var P=[].slice.call(document.querySelectorAll('.pop-s'));if(P.length){var i=0,n=document.getElementById('popN'),run=true;function go(k){i=(k+P.length)%P.length;P.forEach(function(p,j){p.classList.toggle('on',j===i)});n.textContent='0'+(i+1)+' / 0'+P.length}
 document.getElementById('popP').onclick=function(){go(i-1)};document.getElementById('popF').onclick=function(){go(i+1)};setInterval(function(){run&&go(i+1)},4500);document.querySelector('.pop').addEventListener('mouseenter',function(){run=false});document.querySelector('.pop').addEventListener('mouseleave',function(){run=true})}
var d=new Date(),cm=document.getElementById('calM');if(cm){cm.textContent=d.toLocaleString('en-IN',{month:'short'});document.getElementById('calD').textContent=String(d.getDate()).padStart(2,'0');document.getElementById('calW').textContent=d.toLocaleString('en-IN',{weekday:'long'})}
// map rooms
document.querySelectorAll('.map .rm').forEach(function(r){var go=function(){location.href=r.dataset.href};r.addEventListener('click',go);r.addEventListener('keydown',function(e){if(e.key==='Enter'||e.key===' '){e.preventDefault();go()}})});
})();'''
open(f'{OUT}/assets/stage.js','w').write(STAGE_JS+JS)

def page2(path, title, desc, active, body):
    root = '../' if '/' in path else ''
    h = head(title, desc, root).replace('</head>', f'<link href="https://fonts.googleapis.com/css2?family=Caveat:wght@600;700&family=Cormorant+Garamond:ital,wght@1,600&family=Fredoka:wght@600;700&family=Noto+Sans+Devanagari:wght@700&family=Noto+Sans+Tamil:wght@700&display=swap" rel="stylesheet"><link rel="stylesheet" href="{root}assets/stage.css"></head>')
    f = footer(root).replace('</body>', f'<script src="{root}assets/stage.js"></script></body>')
    open(f'{OUT}/{path}', 'w').write(h + header(root, active) + body.replace('{R}', root) + f)

# Tamil letters variant for the hindi visual
def tamilize(v): return v
# ---- ROOMS ----
ROOMS = [
 ('dance-studio','Dance Studio','S3 Dance Studio: dance, music and movement.','#8B5CF6',['western-dance','bharatanatyam','vocal-music','zumba']),
 ('sports-arena','Sports Arena','Martial arts, fitness and balance.','#DC2626',['karate','boxing','silambam','skating','yoga']),
 ('skills-corner','Skills Corner','Maths, puzzles, strategy and art.','#0E9F6E',['abacus','vedic-maths','mental-maths','chess','rubiks-cube','drawing','play-code']),
 ('language-room','Language Room','Reading, writing and speaking with confidence.','#2563EB',['english-phonics','tamil-phonics','hindi','handwriting','spoken-english','creative-writing','public-speaking']),
 ('study-room','Study Room','Academic support and care after school.','#F59E0B',['tuition','after-school-care']),
 ('craft-wellness','Craft & Teacher Studio','Craft, phonics and teacher training for adults.','#DB2777',['aari-work','embroidery','montessori-teacher-training','phonics-english-adults','phonics-tamil-adults']),
 ('code-lab','Code Lab','Code Crackers: build, design and create digitally.','#4F46E5',ORDER_CC)]
assert sorted(sum((r[4] for r in ROOMS), [])) == sorted(sum(ORDERS.values(), [])), 'room coverage'
os.makedirs(f'{OUT}/rooms', exist_ok=True)
COL = {'western':'#8B5CF6','classical':'#B4233C','vocal':'#12A39A','zumba':'#FF3D7F','drawing':'#3B82F6','abacus':'#F5A800','english':'#2563EB','chess':'#7C4A1E','hindi':'#EA580C','tuition':'#16A34A','montessori':'#EC4899'}
def dotc(s): return COL.get(MAP_V.get(s), '#4F46E5' if s in CODE else '#E3A008')
seen_vis = set()
EMO={'western-dance':'💃','bharatanatyam':'🪷','vocal-music':'🎤','zumba':'🔥','karate':'🥋','boxing':'🥊','silambam':'🥢','skating':'🛼','yoga':'🧘','abacus':'🧮','vedic-maths':'✖️','mental-maths':'🧠','chess':'♞','rubiks-cube':'🟨','drawing':'🎨','play-code':'🧩','english-phonics':'🔤','tamil-phonics':'அ','hindi':'क','handwriting':'✍️','spoken-english':'💬','creative-writing':'📖','public-speaking':'📣','tuition':'📚','after-school-care':'🏫','aari-work':'🪡','embroidery':'🧵','montessori-teacher-training':'🧸','phonics-english-adults':'🔤','phonics-tamil-adults':'ஆ','web-mobile-app-development':'💻','video-editing':'🎬','graphic-design':'🖌️','ux-ui-design':'📱','digital-marketing':'📈','ai-tools-tech':'🤖','project-management':'📋'}
for slug, name, desc, col, cs in ROOMS:
    lst = ''.join(f'<button role="tab" aria-selected="{"true" if i==0 else "false"}" data-k="{s}" style="--rc:{col}"><span class="bi">{EMO.get(s,"✦")}</span><span>{E(BY[s]["name"])}</span><small>{i+1:02d}</small></button>' for i, s in enumerate(cs))
    st = ''.join(stage(s, i == 0, 1) for i, s in enumerate(cs))
    others = ''.join(f'<a class="btn btn-line" href="{r[0]}.html">{r[1]}</a>' for r in ROOMS if r[0] != slug)
    body = phead(f'Room · Eureka Academy', E(name), E(desc) + f' Tap a course to step inside. {len(cs)} courses in this room.') + f'''
<section class="sec" style="padding-top:10px"><div class="w"><div class="rx"><div class="rx-list" role="tablist" aria-label="{E(name)} courses">{lst}</div><div class="stage-wrap" aria-live="polite">{st}</div></div>
<div style="margin-top:56px"><p class="kick">Other rooms</p><div class="row" style="margin-top:14px">{others}</div></div></div></section>{cta_band()}'''
    page2(f'rooms/{slug}.html', f'{name} — Eureka Academy, Erode', desc, 'Courses', body)

# ---- COURSE PAGES: add stage hero ----
import glob
for s in BY:
    p = f'{OUT}/courses/{s}.html'
    if not os.path.exists(p): continue
    h = open(p).read()
    room = next(r for r in ROOMS if s in r[4])
    st = f'<section class="sec" style="padding:28px 0 0"><div class="w"><div class="stage-wrap">{stage(s)}</div><p class="muted sm" style="margin-top:14px">Part of the <a href="../rooms/{room[0]}.html" style="color:var(--ink);font-weight:600;text-decoration:underline">{room[1]}</a>. Explore the other courses in this room.</p></div></section>'
    h = h.replace('<section class="sec"><div class="w g-2">', st.replace('{R}','../') + '<section class="sec"><div class="w g-2">', 1)
    h = h.replace('</head>', '<link href="https://fonts.googleapis.com/css2?family=Caveat:wght@600;700&family=Cormorant+Garamond:ital,wght@1,600&family=Fredoka:wght@600;700&family=Noto+Sans+Devanagari:wght@700&display=swap" rel="stylesheet"><link rel="stylesheet" href="../assets/stage.css"></head>')
    h = h.replace('</body>', '<script src="../assets/stage.js"></script></body>')
    open(p, 'w').write(h)

# ---- HOME (minimal reference layout) ----
cl = lambda x, y, w, d: f'<svg class="cl" style="left:{x}%;top:{y}px;width:{w}px;animation-delay:{d}s" viewBox="0 0 120 50" aria-hidden="true"><path d="M20 45a16 16 0 0 1 2-32 22 22 0 0 1 40-6 18 18 0 0 1 32 8 15 15 0 0 1 6 30z" fill="#fff"/></svg>'
pops = [('S3 Dance Studio','Western · Classical · Vocal · Zumba','#F3E8FF','💃','rooms/dance-studio.html'),('Tuition 3rd–12th Std','Subject-wise guidance after school','#DCFCE7','📚','courses/tuition.html'),('Code Lab','Web, design, video and AI skills','#E0E7FF','💻','rooms/code-lab.html')]
pop_html = ''.join(f'<div class="pop-s{" on" if i==0 else ""}"><div class="pop-art" style="--bg:{bg}">{e}</div><small>Popup</small><h3>{t}</h3><p class="muted sm">{d}</p><a href="{{R}}{u}">Learn more {ico(I["arrow"],16)}</a></div>' for i,(t,d,bg,e,u) in enumerate(pops))
qb = ''.join(f'<a href="{{R}}rooms/{r}.html"><b>{t}</b><span>{d}</span><em>Explore</em></a>' for r,t,d in [('dance-studio','Dance &amp; Music','Western · Classical · Vocal'),('sports-arena','Sports &amp; Fitness','Karate · Yoga · Zumba'),('skills-corner','Skills','Abacus · Chess · Drawing'),('study-room','Academics','Tuition 3rd–12th')])
# isometric map with 7 rooms
pos = [(60,190),(250,95),(440,190),(250,285),(440,380),(630,285),(630,95)]
tiles = ''
for i,((x,y),(slug,name,_,col,cs)) in enumerate(zip(pos, ROOMS)):
    lab = name.replace(" & Teacher Studio","").replace("Craft","Craft Studio")
    tiles += f'''<g class="rm" tabindex="0" role="link" aria-label="{E(name)}, {len(cs)} courses" data-href="rooms/{slug}.html">
<path d="M{x} {y} l95 -48 l95 48 l-95 48z" fill="{col}"/><path d="M{x} {y} l95 48 v22 l-95 -48z" fill="{col}" style="filter:brightness(.78)"/><path d="M{x+190} {y} l-95 48 v22 l95 -48z" fill="{col}" style="filter:brightness(.62)"/>
<circle cx="{x+95}" cy="{y-22}" r="14" fill="#fff"/><text x="{x+95}" y="{y-17}" text-anchor="middle" style="fill:{col};font-size:14px">{i+1}</text>
<text x="{x+95}" y="{y+12}" text-anchor="middle" style="font-size:17px">{E(lab)}</text></g>'''
trees = ''.join(f'<path d="M{x} {y} l12 -30 l12 30z" fill="#22A06B"/>' for x,y in [(70,250),(110,232),(820,250),(780,170),(560,480),(160,360)])
dots = ''.join(f'<circle cx="{x}" cy="{y}" r="6" fill="#fff"/>' for x,y in [(345,190),(368,202),(391,214),(535,238),(558,250),(345,330),(368,342)])
mapsvg = f'<svg class="map" viewBox="20 20 860 480" role="group" aria-label="Map of Eureka rooms. Tap a room."><path d="M30 240 L450 30 L870 240 L450 450Z" fill="#EAF6DC" stroke="#CFE6B5" stroke-width="3"/><path d="M30 240 L450 450 v18 L30 258Z" fill="#CFE6B5"/><path d="M870 240 L450 450 v18 L870 258Z" fill="#B9D99A"/>{dots}{trees}<circle cx="300" cy="60" r="16" fill="#FFC21A"/>{tiles}</svg>'
rlist = ''.join(f'<a href="{{R}}rooms/{r[0]}.html"><span class="n" style="--c:{r[3]}">{i+1}</span><span><b>{E(r[1])}</b><small>{len(r[4])} courses · {E(r[2])}</small></span>{ico(I["arrow"],18)}</a>' for i, r in enumerate(ROOMS))
bk = ''.join(f'<a class="bk" style="--c:{c}" href="{{R}}{u}"><h3>{t}</h3><p>{d}</p><span>Go {ico(I["arrow"],16)}</span><em>{e}</em></a>' for c,t,d,u,e in [('#E3A008','Course Enquiry','Pick a course and message us for timings and fees.','courses.html','🎯'),('#0E9F6E','Toddler Care','Play-based early learning for little ones.','toddler-care.html','🧸'),('#F97316','Visit Us','Moolapalayam, Poondurai Road, Erode.','contact.html','📍')])
upd = ''.join(f'<li><a href="{{R}}{u}">{"<span class=nw>N</span>" if n else ""}<span>{t}</span><em>Eureka Academy</em></a></li>' for t,u,n in [('Admissions are open for dance, music, skills and tuition batches.','courses.html',1),('S3 Dance Studio: Western, Classical, Vocal and Zumba.','rooms/dance-studio.html',0),('Subject-wise tuition available for 3rd to 12th Std.','courses/tuition.html',0),('New: Code Lab courses in web, design, video and AI.','rooms/code-lab.html',0)])
home = f'''<section class="sky">{cl(8,50,140,0)}{cl(46,26,100,-10)}{cl(78,70,150,-20)}
<svg class="hills" viewBox="0 0 1440 260" preserveAspectRatio="none" aria-hidden="true"><path d="M0 140 C 200 60, 380 90, 520 140 C 680 70, 860 60, 1020 130 C 1180 80, 1340 90, 1440 120 V260 H0Z" fill="#E3F0D6"/><path d="M0 190 C 260 150, 520 170, 760 190 C 1000 160, 1240 170, 1440 185 V260 H0Z" fill="#D5E9C2"/></svg>
<div class="w sky-in"><div><p class="kick"><span class="live"></span>Eureka Academy · S3 Dance Studio</p><h1>Learn, dance and grow,<b>Eureka Academy Moolapalayam</b></h1><p class="lede">{TOTAL} courses for children, adults and future creators, arranged in 7 rooms you can explore.</p>
<div class="row"><a class="btn btn-dark" href="{{R}}courses.html">Explore courses {ico(I["arrow"],18)}</a><a class="btn btn-line" href="#rooms">Explore by room</a></div></div>
<div class="pop" aria-roledescription="carousel" aria-label="Highlights">{pop_html}<div class="pop-side"><b>POPUP ZONE</b><span id="popN">01 / 03</span><div style="display:grid;gap:6px"><button id="popP" aria-label="Previous">‹</button><button id="popF" aria-label="Next">›</button></div></div></div></div></section>
<div class="w"><div class="qb"><div class="qb-l"><div class="cal" aria-hidden="true"><i id="calM"></i><b id="calD"></b><em id="calW"></em></div><div><h3>Quick Enquiry</h3><p>Choose a room to see its courses.</p></div></div><div class="qb-r">{qb}</div></div>
<div class="inf"><div><h4>{ico(I["clock"],18)}Batch timings</h4><p class="big">Contact for slots</p></div><div><h4>{ico(I["pin"],18)}Location</h4><p>{ADDR}</p></div><div><h4>{ico(I["book"],18)}How it works</h4><p>Choose a course, message or call us, visit the centre and join your batch.</p></div></div></div>
<section class="sec" id="rooms"><div class="w village"><div><p class="kick">Eureka Discovery Village</p><h2 style="font-size:clamp(1.9rem,1.3rem + 2vw,2.8rem);font-weight:800;margin-top:10px">Explore by room.</h2><p class="lede">Every room holds a different set of courses. Tap a room on the map or in the list.</p>{mapsvg}</div><div class="rlist">{rlist}</div></div></section>
<section class="sec sec-alt"><div class="w"><div class="sh"><div><p class="kick">Get started</p><h2>Program enquiry</h2></div></div><div class="bk3">{bk}</div></div></section>
<section class="sec"><div class="w"><div class="sh"><div><p class="kick">News</p><h2>Latest updates</h2></div><a class="lnk" href="{IG}" target="_blank" rel="noopener">Instagram {ico(I["arrow"],16)}</a></div><ul class="upd">{upd}</ul></div></section>
<div class="sea" aria-hidden="true"><svg viewBox="0 0 1440 150" preserveAspectRatio="none"><path d="M0 70 C 240 20, 480 110, 720 70 S 1200 30, 1440 70 V150 H0Z" fill="#DCEEF7"/><path d="M0 105 C 300 70, 600 140, 900 105 S 1300 80, 1440 105 V150 H0Z" fill="#FAF7F2"/></svg></div>'''
page2('index.html', 'Eureka Academy & S3 Dance Studio — Moolapalayam, Erode', f'{TOTAL} courses in 7 rooms at Eureka Academy, Moolapalayam, Erode.', 'Home', home)
print('rooms done')
