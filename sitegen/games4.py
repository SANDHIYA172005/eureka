import re
S='/home/claude/site/'
G={}
# ---------- HANDWRITING: trace the letter ----------
G['handwriting']=('''<article class="g-hw" data-s="handwriting" role="tabpanel">
<div class="hw-top"><span>Trace the letter</span><div class="hw-stars"><i>★</i><i>★</i><i>★</i></div></div>
<div class="hw-paper"><canvas class="hw-c" width="600" height="420" aria-label="Tracing area: draw over the dotted letter"></canvas><div class="hw-tip">✏️ Draw over the dots</div></div>
<div class="hw-bar"><div class="hw-prog"><i></i></div><b class="hw-pct">0%</b><button class="hw-clear">Clear</button><button class="hw-next">Next letter →</button></div>
<div class="hw-win" aria-live="polite"></div></article>''',
'''<script>(function(){var a=document.querySelector('.g-hw');if(!a)return;var c=a.querySelector('.hw-c'),x=c.getContext('2d'),L=['a','b','e','g','k','m','s','A','R','8'],li=0,pts=[],hit,drawing=false,done=false;
var off=document.createElement('canvas');off.width=600;off.height=420;var o=off.getContext('2d');
function font(ctx){ctx.font='700 320px "Caveat","Comic Sans MS",cursive';ctx.textAlign='center';ctx.textBaseline='alphabetic'}
function setup(){x.clearRect(0,0,600,420);o.clearRect(0,0,600,420);font(o);o.fillStyle='#000';o.fillText(L[li],300,330);
var d=o.getImageData(0,0,600,420).data;pts=[];for(var yy=0;yy<420;yy+=10)for(var xx=0;xx<600;xx+=10){if(d[(yy*600+xx)*4+3]>128)pts.push([xx,yy])}hit=new Array(pts.length).fill(false);
font(x);x.save();x.setLineDash([3,14]);x.lineCap='round';x.lineWidth=5;x.strokeStyle='#94A3B8';x.strokeText(L[li],300,330);x.restore();x.fillStyle='rgba(148,163,184,.10)';x.fillText(L[li],300,330);done=false;upd();a.querySelector('.hw-win').innerHTML='';a.classList.remove('won')}
function pos(e){var r=c.getBoundingClientRect(),t=e.touches?e.touches[0]:e;return[(t.clientX-r.left)*600/r.width,(t.clientY-r.top)*420/r.height]}
var last=null;function start(e){e.preventDefault();drawing=true;last=pos(e);a.querySelector('.hw-tip').style.opacity=0}
function move(e){if(!drawing)return;e.preventDefault();var p=pos(e);x.strokeStyle='#1D4ED8';x.lineWidth=16;x.lineCap='round';x.lineJoin='round';x.setLineDash([]);x.beginPath();x.moveTo(last[0],last[1]);x.lineTo(p[0],p[1]);x.stroke();
for(var i=0;i<pts.length;i++){if(!hit[i]){var dx=pts[i][0]-p[0],dy=pts[i][1]-p[1];if(dx*dx+dy*dy<26*26)hit[i]=true}}last=p;upd()}
function end(){drawing=false}
function upd(){var n=hit?hit.filter(Boolean).length:0,pc=pts.length?Math.min(100,Math.round(n/pts.length*115)):0;a.querySelector('.hw-prog i').style.width=pc+'%';a.querySelector('.hw-pct').textContent=pc+'%';
var st=a.querySelectorAll('.hw-stars i');st.forEach(function(s,k){s.classList.toggle('on',pc>=[40,70,92][k])});if(pc>=92&&!done){done=true;a.classList.add('won');a.querySelector('.hw-win').innerHTML='<span>Beautiful writing! ✨</span>'}}
c.addEventListener('mousedown',start);c.addEventListener('mousemove',move);addEventListener('mouseup',end);c.addEventListener('touchstart',start,{passive:false});c.addEventListener('touchmove',move,{passive:false});c.addEventListener('touchend',end);
a.querySelector('.hw-clear').onclick=setup;a.querySelector('.hw-next').onclick=function(){li=(li+1)%L.length;setup()};
(document.fonts&&document.fonts.ready?document.fonts.ready:Promise.resolve()).then(setup)})();</script>''',
'''.g-hw{position:relative;display:flex!important;flex-direction:column;gap:12px;height:100%;min-height:520px;padding:22px!important;background:linear-gradient(160deg,#FCE7F3,#FDF2F8 40%,#EDE9FE)!important}
.hw-top{display:flex;justify-content:space-between;align-items:center}.hw-top span{font:800 13px Inter,sans-serif;letter-spacing:.08em;text-transform:uppercase;color:#BE185D}
.hw-stars i{font-style:normal;font-size:26px;color:#E5E7EB;margin-left:4px;transition:.3s;display:inline-block}.hw-stars i.on{color:#FACC15;transform:scale(1.2) rotate(-8deg);text-shadow:0 0 12px #FDE047}
.hw-paper{position:relative;flex:1;border-radius:18px;overflow:hidden;background:#fff repeating-linear-gradient(#fff 0 39px,#BFDBFE 39px 41px);box-shadow:0 20px 34px -22px #0007;border-left:6px solid #F87171}
.hw-c{position:absolute;inset:0;width:100%;height:100%;cursor:crosshair;touch-action:none}
.hw-tip{position:absolute;left:50%;bottom:14px;transform:translateX(-50%);padding:6px 14px;border-radius:999px;background:#1E293B;color:#fff;font:600 13px Inter,sans-serif;pointer-events:none;transition:opacity .3s;animation:hwb 1.6s ease-in-out infinite}
@keyframes hwb{50%{transform:translate(-50%,-4px)}}
.hw-bar{display:flex;align-items:center;gap:10px}.hw-prog{flex:1;height:10px;border-radius:9px;background:#fff;overflow:hidden;box-shadow:inset 0 1px 3px #0002}.hw-prog i{display:block;height:100%;width:0;background:linear-gradient(90deg,#F472B6,#8B5CF6);transition:width .2s}
.hw-pct{min-width:44px;font:800 16px Inter,sans-serif;color:#6D28D9}
.hw-bar button{border:0;border-radius:999px;padding:9px 14px;font:700 13px Inter,sans-serif;cursor:pointer;background:#fff;color:#1C1917;box-shadow:0 4px 10px -6px #0005}.hw-bar .hw-next{background:#1C1917;color:#fff}
.hw-win{position:absolute;inset:0;pointer-events:none;display:grid;place-items:center}.hw-win span{padding:12px 22px;border-radius:999px;background:#8B5CF6;color:#fff;font:800 18px Inter,sans-serif;box-shadow:0 14px 30px -10px #8B5CF6;animation:sbpop .5s cubic-bezier(.3,1.6,.5,1)}
@media(max-width:600px){.g-hw{min-height:440px;padding:14px!important}.hw-bar button{padding:8px 10px;font-size:12px}}''')

# ---------- SPOKEN ENGLISH: speak & listen cards ----------
G['spoken-english']=('''<article class="g-se" data-s="spoken-english" role="tabpanel">
<div class="se-tabs" role="tablist"><button class="on" data-i="0">👋 Greeting</button><button data-i="1">🛒 At a shop</button><button data-i="2">🏫 In class</button></div>
<div class="se-card"><span class="se-lvl">Say it aloud</span><p class="se-ph">Hello! My name is Priya. Nice to meet you.</p><p class="se-tm">வணக்கம்! என் பெயர் பிரியா. உங்களை சந்தித்ததில் மகிழ்ச்சி.</p>
<div class="se-wave" aria-hidden="true">'''+''.join(f'<i style="--d:{i*0.06:.2f}s"></i>' for i in range(28))+'''</div></div>
<div class="se-ctl"><button class="se-listen">🔊 Listen</button><button class="se-mic" aria-label="Record yourself"><span>🎤</span></button><button class="se-nx">Next →</button></div>
<p class="se-fb" aria-live="polite">Tap 🔊 to hear it, then 🎤 to practise</p></article>''',
'''<script>(function(){var a=document.querySelector('.g-se');if(!a)return;var D=[[['Hello! My name is Priya. Nice to meet you.','வணக்கம்! என் பெயர் பிரியா. உங்களை சந்தித்ததில் மகிழ்ச்சி.'],['How are you today? I am doing great, thank you!','இன்று எப்படி இருக்கிறீர்கள்? நான் நன்றாக இருக்கிறேன், நன்றி!'],['Good morning! Have a wonderful day.','காலை வணக்கம்! இனிய நாளாக அமையட்டும்.']],[['How much does this cost?','இது எவ்வளவு விலை?'],['Can I have two of these, please?','எனக்கு இதில் இரண்டு கொடுங்கள்.'],['Thank you! Have a nice day.','நன்றி! நல்ல நாளாக அமையட்டும்.']],[['May I ask a question, please?','நான் ஒரு கேள்வி கேட்கலாமா?'],['Could you repeat that, please?','தயவுசெய்து மீண்டும் சொல்ல முடியுமா?'],['I have finished my homework.','நான் என் வீட்டுப்பாடத்தை முடித்துவிட்டேன்.']]],t=0,k=0,ph=a.querySelector('.se-ph'),tm=a.querySelector('.se-tm'),fb=a.querySelector('.se-fb'),busy=false;
function show(){ph.textContent=D[t][k][0];tm.textContent=D[t][k][1];ph.classList.remove('in');void ph.offsetWidth;ph.classList.add('in');fb.textContent='Tap 🔊 to hear it, then 🎤 to practise';a.classList.remove('rec','talk')}
a.querySelectorAll('.se-tabs button').forEach(function(b){b.onclick=function(){a.querySelectorAll('.se-tabs button').forEach(function(y){y.classList.toggle('on',y===b)});t=+b.dataset.i;k=0;show()}});
a.querySelector('.se-nx').onclick=function(){k=(k+1)%3;show()};
a.querySelector('.se-listen').onclick=function(){if(!window.speechSynthesis){fb.textContent='Audio not supported on this browser';return}speechSynthesis.cancel();var u=new SpeechSynthesisUtterance(D[t][k][0]);u.lang='en-IN';u.rate=.9;a.classList.add('talk');fb.textContent='Listen carefully… 👂';u.onend=function(){a.classList.remove('talk');fb.textContent='Your turn! Tap 🎤 and say it'};speechSynthesis.speak(u)};
a.querySelector('.se-mic').onclick=function(){if(busy)return;busy=true;a.classList.add('rec');fb.textContent='Recording… speak now 🎙️';var w=ph.textContent.split(' '),i=0;ph.innerHTML=w.map(function(x){return '<span>'+x+'</span>'}).join(' ');var s=ph.querySelectorAll('span'),iv=setInterval(function(){if(i<s.length){s[i].classList.add('hl');i++}else{clearInterval(iv);a.classList.remove('rec');busy=false;var m=['Excellent! 🌟','Great pronunciation! 👏','Super clear! 💯','Well spoken! 🎉'];fb.textContent=m[Math.floor(Math.random()*m.length)];a.classList.add('ok');setTimeout(function(){a.classList.remove('ok')},1200)}},260)};show()})();</script>''',
'''.g-se{position:relative;display:flex!important;flex-direction:column;justify-content:center;gap:16px;height:100%;min-height:520px;padding:24px!important;background:radial-gradient(120% 90% at 20% 0%,#DBEAFE,#E0E7FF 50%,#C7D2FE)!important}
.se-tabs{display:flex;gap:6px;padding:5px;border-radius:999px;background:#ffffffaa;align-self:center}.se-tabs button{border:0;border-radius:999px;padding:8px 14px;background:none;font:700 13px Inter,sans-serif;color:#3730A3;cursor:pointer;white-space:nowrap}.se-tabs button.on{background:#4F46E5;color:#fff;box-shadow:0 6px 14px -6px #4F46E5}
.se-card{position:relative;padding:26px 24px 20px;border-radius:24px;background:#fff;box-shadow:0 24px 40px -26px #312E81;text-align:center}
.se-lvl{display:inline-block;padding:4px 10px;border-radius:999px;background:#EEF2FF;color:#4F46E5;font:800 11px Inter,sans-serif;letter-spacing:.08em;text-transform:uppercase}
.se-ph{margin-top:12px;font:800 clamp(1.25rem,1rem + .9vw,1.7rem)/1.35 Inter,sans-serif;color:#1E1B4B;text-align:center!important}.se-ph.in{animation:sein .4s ease}@keyframes sein{from{opacity:0;transform:translateY(8px)}}
.se-ph span{transition:color .2s,background .2s;border-radius:6px;padding:0 2px}.se-ph span.hl{background:#FDE68A;color:#92400E}
.se-tm{margin-top:8px;font-size:14px;color:#6B7280;text-align:center!important}
.se-wave{display:flex;align-items:center;justify-content:center;gap:4px;height:44px;margin-top:16px}.se-wave i{width:5px;height:6px;border-radius:3px;background:#C7D2FE;transition:background .2s}
.g-se.talk .se-wave i,.g-se.rec .se-wave i{animation:sew .6s var(--d) ease-in-out infinite alternate}.g-se.talk .se-wave i{background:#4F46E5}.g-se.rec .se-wave i{background:#EF4444}
@keyframes sew{to{height:38px}}
.se-ctl{display:flex;align-items:center;justify-content:center;gap:14px}
.se-listen,.se-nx{border:0;border-radius:999px;padding:11px 18px;font:700 14px Inter,sans-serif;cursor:pointer;background:#fff;color:#312E81;box-shadow:0 6px 14px -8px #0006}
.se-mic{position:relative;width:74px;height:74px;border:0;border-radius:50%;background:linear-gradient(145deg,#F43F5E,#DC2626);color:#fff;font-size:30px;cursor:pointer;box-shadow:0 14px 26px -10px #DC2626}
.g-se.rec .se-mic::before,.g-se.rec .se-mic::after{content:"";position:absolute;inset:-8px;border-radius:50%;border:3px solid #F87171;animation:sep 1.2s ease-out infinite}.g-se.rec .se-mic::after{animation-delay:.6s}
@keyframes sep{to{inset:-26px;opacity:0}}
.se-fb{text-align:center!important;font:700 15px Inter,sans-serif;color:#3730A3;min-height:22px}.g-se.ok .se-fb{color:#16A34A;animation:sbpop .4s}
@media(max-width:600px){.g-se{min-height:460px;padding:16px!important;gap:12px}.se-tabs button{padding:7px 9px;font-size:11.5px}.se-mic{width:62px;height:62px;font-size:24px}.se-listen,.se-nx{padding:9px 12px;font-size:13px}}''')

# ---------- WESTERN DANCE: rhythm tap ----------
G['western-dance']=('''<article class="g-rh" data-s="western-dance" role="tabpanel">
<div class="rh-hud"><div><small>Score</small><b class="rh-sc">0</b></div><div class="rh-cb"><small>Combo</small><b class="rh-cm">×0</b></div><div><small>Best</small><b class="rh-bs">0</b></div></div>
<div class="rh-stage"><div class="rh-lights" aria-hidden="true"><i></i><i></i><i></i></div>
<button class="rh-pad" aria-label="Tap on the beat"><span class="rh-ring"></span><span class="rh-core">TAP</span></button>
<p class="rh-judge" aria-live="polite"></p></div>
<div class="rh-foot"><button class="rh-go">▶ Start the beat</button><span>Tap when the ring meets the circle</span></div></article>''',
'''<script>(function(){var a=document.querySelector('.g-rh');if(!a)return;var pad=a.querySelector('.rh-pad'),ring=a.querySelector('.rh-ring'),j=a.querySelector('.rh-judge'),sc=0,cm=0,bs=0,P=750,t0=0,on=false,raf,ac,lastBeat=-1,tapped=-1;
function beep(f,d){try{ac=ac||new (window.AudioContext||window.webkitAudioContext)();var o=ac.createOscillator(),g=ac.createGain();o.frequency.value=f;o.type='triangle';g.gain.setValueAtTime(.18,ac.currentTime);g.gain.exponentialRampToValueAtTime(.001,ac.currentTime+d);o.connect(g);g.connect(ac.destination);o.start();o.stop(ac.currentTime+d)}catch(e){}}
function loop(t){var e=(t-t0)%P,b=Math.floor((t-t0)/P),k=e/P;ring.style.transform='translate(-50%,-50%) scale('+(2.6-1.6*k)+')';ring.style.opacity=.25+.75*k;
if(b!==lastBeat){lastBeat=b;beep(b%4===0?660:440,.08);a.classList.remove('pulse');void a.offsetWidth;a.classList.add('pulse');if(tapped<b-1&&b>1){cm=0;upd()}}raf=requestAnimationFrame(loop)}
function upd(){a.querySelector('.rh-sc').textContent=sc;a.querySelector('.rh-cm').textContent='×'+cm;a.querySelector('.rh-bs').textContent=bs;a.querySelector('.rh-cb').classList.toggle('hot',cm>=5)}
function judge(){if(!on){go();return}var t=performance.now(),e=(t-t0)%P,d=Math.min(e,P-e),beat=Math.round((t-t0)/P);if(tapped===beat)return;tapped=beat;var r,c;if(d<70){r='PERFECT!';c='#FDE047';cm++;sc+=100+cm*10;beep(880,.12)}else if(d<150){r='GOOD';c='#86EFAC';cm++;sc+=50}else{r='MISS';c='#FCA5A5';cm=0}
bs=Math.max(bs,sc);j.textContent=r;j.style.color=c;j.classList.remove('pop');void j.offsetWidth;j.classList.add('pop');pad.classList.remove('hit');void pad.offsetWidth;pad.classList.add('hit');upd()}
function go(){if(on){on=false;cancelAnimationFrame(raf);a.classList.remove('live');a.querySelector('.rh-go').textContent='▶ Start the beat';return}on=true;sc=0;cm=0;tapped=-1;lastBeat=-1;t0=performance.now();a.classList.add('live');a.querySelector('.rh-go').textContent='■ Stop';upd();raf=requestAnimationFrame(loop)}
pad.addEventListener('pointerdown',function(e){e.preventDefault();judge()});a.querySelector('.rh-go').onclick=go;
document.addEventListener('keydown',function(e){if(e.code==='Space'&&a.getBoundingClientRect().top<innerHeight&&a.getBoundingClientRect().bottom>0&&on){e.preventDefault();judge()}})})();</script>''',
'''.g-rh{position:relative;display:flex!important;flex-direction:column;height:100%;min-height:520px;padding:18px!important;overflow:hidden;background:radial-gradient(100% 70% at 50% 45%,#3B0764,#1E1B4B 60%,#0B0820)!important;color:#fff}
.rh-hud{display:grid;grid-template-columns:repeat(3,1fr);gap:8px;position:relative;z-index:2}.rh-hud div{padding:8px;border-radius:14px;background:#ffffff14;text-align:center}.rh-hud small{display:block;font:700 10.5px Inter,sans-serif;letter-spacing:.08em;text-transform:uppercase;color:#C4B5FD}.rh-hud b{font:800 22px Inter,sans-serif}
.rh-cb.hot{background:linear-gradient(135deg,#F97316,#EC4899)!important;animation:sbpop .3s}
.rh-stage{position:relative;flex:1;display:grid;place-items:center}
.rh-lights i{position:absolute;top:-30%;width:120px;height:160%;background:linear-gradient(180deg,#F0ABFC55,transparent);transform-origin:50% 0;filter:blur(2px);animation:dfbeam 6s ease-in-out infinite}.rh-lights i:nth-child(1){left:10%}.rh-lights i:nth-child(2){left:44%;background:linear-gradient(180deg,#67E8F955,transparent);animation-delay:-2s}.rh-lights i:nth-child(3){right:10%;background:linear-gradient(180deg,#FDE04755,transparent);animation-delay:-4s}
.rh-pad{position:relative;width:150px;height:150px;border:0;border-radius:50%;cursor:pointer;background:radial-gradient(circle at 35% 30%,#F0ABFC,#A855F7 45%,#6D28D9);box-shadow:0 0 0 8px #ffffff1a,0 0 60px 10px #A855F755;touch-action:manipulation}
.rh-core{font:900 26px Inter,sans-serif;letter-spacing:.1em;color:#fff;text-shadow:0 2px 6px #0006}
.rh-ring{position:absolute;left:50%;top:50%;width:150px;height:150px;border-radius:50%;border:5px solid #FDE047;transform:translate(-50%,-50%) scale(2.6);opacity:0;pointer-events:none;box-shadow:0 0 18px #FDE047}
.g-rh:not(.live) .rh-ring{opacity:0!important}
.g-rh.pulse .rh-pad{animation:rhp .25s ease}@keyframes rhp{50%{box-shadow:0 0 0 14px #ffffff26,0 0 90px 20px #A855F799}}
.rh-pad.hit{animation:rhh .2s ease}@keyframes rhh{50%{transform:scale(.92)}}
.rh-judge{position:absolute;top:14%;left:0;right:0;text-align:center!important;font:900 30px Inter,sans-serif;letter-spacing:.06em;text-shadow:0 0 20px currentColor;opacity:0}.rh-judge.pop{animation:rhj .7s ease forwards}@keyframes rhj{0%{opacity:1;transform:scale(1.4)}100%{opacity:0;transform:translateY(-20px) scale(1)}}
.rh-foot{position:relative;z-index:2;display:flex;align-items:center;justify-content:center;gap:12px;flex-wrap:wrap}.rh-foot span{font-size:13px;color:#C4B5FD}
.rh-go{border:0;border-radius:999px;padding:11px 20px;background:#FDE047;color:#1E1B4B;font:800 14px Inter,sans-serif;cursor:pointer;box-shadow:0 10px 22px -10px #FDE047}
@media(max-width:600px){.g-rh{min-height:440px}.rh-pad,.rh-ring{width:120px;height:120px}.rh-hud b{font-size:18px}}''')

# ---------- ZUMBA: energy burner ----------
G['zumba']=('''<article class="g-zb" data-s="zumba" role="tabpanel">
<div class="zb-moves" role="group" aria-label="Pick a move"><button class="on" data-m="Salsa" data-k="1">💃 Salsa</button><button data-m="Merengue" data-k="1.2">🕺 Merengue</button><button data-m="Cumbia" data-k="1.4">🔥 Cumbia</button></div>
<div class="zb-mid"><div class="zb-meter"><svg viewBox="0 0 200 200" aria-hidden="true"><circle cx="100" cy="100" r="84" class="zb-bg"/><circle cx="100" cy="100" r="84" class="zb-fg"/></svg>
<button class="zb-btn" aria-label="Tap to move"><span class="zb-e">💃</span><b>MOVE!</b></button></div>
<div class="zb-stats"><div><span>❤️</span><b class="zb-hr">72</b><small>bpm</small></div><div><span>🔥</span><b class="zb-cal">0</b><small>kcal</small></div><div><span>⚡</span><b class="zb-pc">0%</b><small>energy</small></div></div></div>
<p class="zb-msg" aria-live="polite">Tap MOVE! as fast as you can</p></article>''',
'''<script>(function(){var a=document.querySelector('.g-zb');if(!a)return;var en=0,cal=0,k=1,fg=a.querySelector('.zb-fg'),C=2*Math.PI*84,hr=a.querySelector('.zb-hr'),cl=a.querySelector('.zb-cal'),pc=a.querySelector('.zb-pc'),msg=a.querySelector('.zb-msg'),btn=a.querySelector('.zb-btn'),em=a.querySelector('.zb-e'),hit=false;fg.style.strokeDasharray=C;
var M=[['Tap MOVE! as fast as you can',0],['Nice warm-up! 🙌',20],['Keep going! 💪',45],['You are on fire! 🔥',75],['ZUMBA STAR! 🌟',98]];
function draw(){fg.style.strokeDashoffset=C*(1-en/100);hr.textContent=Math.round(72+en*1.1);cl.textContent=cal.toFixed(1);pc.textContent=Math.round(en)+'%';var m=M[0][0];M.forEach(function(x){if(en>=x[1])m=x[0]});msg.textContent=m;a.classList.toggle('max',en>=98);a.style.setProperty('--e',en/100)}
btn.addEventListener('pointerdown',function(e){e.preventDefault();en=Math.min(100,en+4*k);cal+=.12*k;btn.classList.remove('b');void btn.offsetWidth;btn.classList.add('b');var s=document.createElement('i');s.className='zb-fx';s.textContent=['+1','💦','✨','🔥'][Math.floor(Math.random()*4)];s.style.left=(30+Math.random()*40)+'%';a.querySelector('.zb-meter').appendChild(s);setTimeout(function(){s.remove()},900);draw()});
a.querySelectorAll('.zb-moves button').forEach(function(b){b.onclick=function(){a.querySelectorAll('.zb-moves button').forEach(function(y){y.classList.toggle('on',y===b)});k=+b.dataset.k;em.textContent=b.textContent.split(' ')[0]}});
setInterval(function(){if(en>0){en=Math.max(0,en-1.2);draw()}},120);draw()})();</script>''',
'''.g-zb{--e:0;position:relative;display:flex!important;flex-direction:column;justify-content:center;gap:16px;height:100%;min-height:520px;padding:22px!important;overflow:hidden;background:linear-gradient(150deg,#FB7185,#F97316 55%,#FACC15)!important;color:#fff}
.g-zb::before{content:"";position:absolute;inset:-20%;background:radial-gradient(circle at 50% 50%,#fff3 0,transparent 55%);transform:scale(calc(.8 + var(--e)*.6));transition:transform .2s}
.zb-moves{position:relative;display:flex;gap:6px;align-self:center;padding:5px;border-radius:999px;background:#ffffff33;backdrop-filter:blur(6px)}.zb-moves button{border:0;border-radius:999px;padding:8px 13px;background:none;color:#fff;font:800 13px Inter,sans-serif;cursor:pointer;white-space:nowrap}.zb-moves button.on{background:#fff;color:#EA580C}
.zb-mid{position:relative;display:grid;grid-template-columns:auto 1fr;gap:22px;align-items:center}
.zb-meter{position:relative;width:220px;height:220px}.zb-meter svg{position:absolute;inset:0;width:100%;height:100%;transform:rotate(-90deg)}
.zb-bg{fill:none;stroke:#ffffff40;stroke-width:16}.zb-fg{fill:none;stroke:#fff;stroke-width:16;stroke-linecap:round;transition:stroke-dashoffset .15s;filter:drop-shadow(0 0 8px #fff)}
.zb-btn{position:absolute;inset:26px;border:0;border-radius:50%;cursor:pointer;background:radial-gradient(circle at 35% 30%,#fff,#FFE4E6 50%,#FDBA74);color:#C2410C;display:flex;flex-direction:column;align-items:center;justify-content:center;box-shadow:0 16px 30px -12px #9A3412;touch-action:manipulation}
.zb-btn .zb-e{font-size:46px;line-height:1}.zb-btn b{font:900 20px Inter,sans-serif;letter-spacing:.08em}
.zb-btn.b{animation:zbb .18s ease}@keyframes zbb{50%{transform:scale(.9)}}
.zb-fx{position:absolute;bottom:60%;font-style:normal;font:900 18px Inter,sans-serif;pointer-events:none;animation:zbfx .9s ease-out forwards}@keyframes zbfx{to{transform:translateY(-90px);opacity:0}}
.zb-stats{display:grid;gap:10px}.zb-stats div{display:grid;grid-template-columns:34px auto 1fr;align-items:baseline;gap:6px;padding:12px 14px;border-radius:16px;background:#ffffff2e;backdrop-filter:blur(6px)}
.zb-stats span{font-size:20px}.zb-stats b{font:900 26px Inter,sans-serif}.zb-stats small{font:700 12px Inter,sans-serif;opacity:.85}
.zb-msg{position:relative;text-align:center!important;font:900 18px Inter,sans-serif;text-shadow:0 2px 8px #0003}
.g-zb.max .zb-msg{animation:sbpop .4s}.g-zb.max .zb-btn{box-shadow:0 0 0 6px #fff8,0 0 50px 10px #FDE047}
@media(max-width:600px){.g-zb{min-height:480px;padding:14px!important}.zb-mid{grid-template-columns:1fr;justify-items:center;gap:14px}.zb-meter{width:180px;height:180px}.zb-btn{inset:22px}.zb-stats{grid-template-columns:repeat(3,1fr);width:100%;gap:6px}.zb-stats div{grid-template-columns:1fr;text-align:center;padding:8px 4px}.zb-stats b{font-size:20px}.zb-moves button{padding:7px 9px;font-size:12px}}''')

css=''
for k,(art,js,c) in G.items():
    f=S+f'courses/{k}.html'; h=open(f).read()
    h=re.sub(r'<article [^>]*data-s="'+k+r'".*?</article>',lambda m:art,h,count=1,flags=re.S)
    # remove previous custom game scripts for these
    h=re.sub(r"<script>\(function\(\)\{var a=document\.querySelector\('\.st-df'\).*?</script>",'',h,flags=re.S)
    h=h.replace('</body>',js+'</body>',1); open(f,'w').write(h); css+=c+'\n'
open(S+'assets/site.css','a').write('\n/* games v4 */\n'+css+'.cv-stage .g-hw,.cv-stage .g-se,.cv-stage .g-rh,.cv-stage .g-zb{width:100%}\n')
print('ok')
