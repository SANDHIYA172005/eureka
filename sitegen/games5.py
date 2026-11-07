import re
S='/home/claude/site/'
G={}
G['english-phonics']=('''<article class="g-ph" data-s="english-phonics" role="tabpanel">
<div class="ph-hud"><span>Sound Match</span><div class="ph-sc">⭐ <b>0</b></div></div>
<div class="ph-q"><button class="ph-play" aria-label="Hear the sound"><span>🔊</span></button><div><small>Listen &amp; find the picture that starts with</small><b class="ph-l">A</b></div></div>
<div class="ph-g"></div>
<p class="ph-fb" aria-live="polite">Tap 🔊 to hear the sound</p></article>''',
'''<script>(function(){var a=document.querySelector('.g-ph');if(!a)return;var W={a:['🍎','Apple'],b:['⚽','Ball'],c:['🐱','Cat'],d:['🐶','Dog'],e:['🐘','Elephant'],f:['🐟','Fish'],g:['🍇','Grapes'],h:['🎩','Hat'],k:['🪁','Kite'],l:['🦁','Lion'],m:['🐒','Monkey'],o:['🐙','Octopus'],r:['🐰','Rabbit'],s:['☀️','Sun'],t:['🐯','Tiger'],u:['☂️','Umbrella']},K=Object.keys(W),C=['#F87171','#60A5FA','#4ADE80','#FBBF24','#C084FC','#F472B6'],sc=0,cur,g=a.querySelector('.ph-g'),fb=a.querySelector('.ph-fb'),lk=false;
var SND={a:'a, as in apple',b:'buh',c:'kuh',d:'duh',e:'eh',f:'fff',g:'guh',h:'huh',k:'kuh',l:'lll',m:'mmm',o:'o, as in octopus',r:'rrr',s:'sss',t:'tuh',u:'uh'};
function say(t){try{speechSynthesis.cancel();var u=new SpeechSynthesisUtterance(t);u.lang='en-IN';u.rate=.85;speechSynthesis.speak(u)}catch(e){}}
function sh(x){return x.sort(function(){return Math.random()-.5})}
function round(){lk=false;cur=K[Math.floor(Math.random()*K.length)];var opts=sh([cur].concat(sh(K.filter(function(k){return k!==cur})).slice(0,3)));a.querySelector('.ph-l').textContent=cur.toUpperCase()+' '+cur;
g.innerHTML=opts.map(function(k,i){return '<button class="ph-o" data-k="'+k+'" style="--c:'+C[(i+K.indexOf(k))%6]+';--d:'+i*.07+'s"><span>'+W[k][0]+'</span><b>'+W[k][1]+'</b></button>'}).join('');fb.textContent='Tap 🔊 to hear the sound';fb.className='ph-fb'}
g.addEventListener('click',function(e){var b=e.target.closest('.ph-o');if(!b||lk)return;if(b.dataset.k===cur){lk=true;b.classList.add('ok');sc++;a.querySelector('.ph-sc b').textContent=sc;fb.textContent=['Brilliant! 🎉','Yes! '+W[cur][1]+' 👏','Super! 🌟'][sc%3];fb.className='ph-fb good';say(cur.toUpperCase()+' is for '+W[cur][1]);setTimeout(round,1400)}else{b.classList.add('no');fb.textContent='Try again! 💪';fb.className='ph-fb bad';setTimeout(function(){b.classList.remove('no')},500)}});
a.querySelector('.ph-play').onclick=function(){say(SND[cur]);this.classList.remove('pl');void this.offsetWidth;this.classList.add('pl')};round()})();</script>''',
'''.g-ph{position:relative;display:flex!important;flex-direction:column;gap:14px;height:100%;min-height:520px;padding:22px!important;background:radial-gradient(120% 90% at 20% 0%,#FEF9C3,#FDE68A 55%,#FBBF24)!important}
.ph-hud{display:flex;justify-content:space-between;align-items:center}.ph-hud span{font:800 13px Inter,sans-serif;letter-spacing:.08em;text-transform:uppercase;color:#92400E}
.ph-sc{padding:6px 14px;border-radius:999px;background:#fff;font:800 15px Inter,sans-serif;box-shadow:0 6px 14px -8px #0006}
.ph-q{display:flex;align-items:center;gap:16px;padding:14px 18px;border-radius:22px;background:#fff;box-shadow:0 16px 30px -20px #92400E}
.ph-play{flex:none;width:64px;height:64px;border:0;border-radius:50%;background:linear-gradient(145deg,#F97316,#EA580C);font-size:28px;cursor:pointer;box-shadow:0 10px 20px -8px #EA580C}
.ph-play.pl{animation:sbpop .4s}.ph-q small{display:block;font-size:13px;color:#78716C}.ph-l{font:900 40px "Fredoka",Inter,sans-serif;color:#EA580C;letter-spacing:.04em}
.ph-g{flex:1;display:grid;grid-template-columns:1fr 1fr;gap:12px}
.ph-o{display:flex;flex-direction:column;align-items:center;justify-content:center;gap:6px;border:0;border-radius:22px;background:#fff;cursor:pointer;box-shadow:0 8px 0 var(--c),0 18px 26px -16px #0006;transition:transform .15s;animation:phin .45s var(--d) both cubic-bezier(.3,1.5,.5,1)}
@keyframes phin{from{opacity:0;transform:scale(.6)}}
.ph-o:hover{transform:translateY(-3px)}.ph-o span{font-size:52px;line-height:1}.ph-o b{font:800 15px Inter,sans-serif;color:#44403C}
.ph-o.ok{background:#DCFCE7;box-shadow:0 8px 0 #16A34A,0 0 30px #4ADE80;animation:sbpop .4s}.ph-o.no{animation:phno .4s}@keyframes phno{25%,75%{transform:translateX(-8px)}50%{transform:translateX(8px)}}
.ph-fb{text-align:center!important;font:800 16px Inter,sans-serif;color:#92400E;min-height:22px}.ph-fb.good{color:#15803D}.ph-fb.bad{color:#DC2626}
@media(max-width:600px){.g-ph{min-height:480px;padding:14px!important}.ph-o span{font-size:40px}.ph-l{font-size:32px}.ph-play{width:54px;height:54px}}''')

H=[('क','Kamal','Lotus','🪷'),('ग','Gaay','Cow','🐄'),('च','Chammach','Spoon','🥄'),('ज','Jahaaz','Ship','🚢'),('प','Patang','Kite','🪁'),('म','Machhli','Fish','🐟'),('अ','Anaar','Pomegranate','🍎'),('आ','Aam','Mango','🥭'),('घ','Ghar','House','🏠')]
HW={'क':'कमल','ग':'गाय','च':'चम्मच','ज':'जहाज़','प':'पतंग','म':'मछली','अ':'अनार','आ':'आम','घ':'घर'}
cards=''.join(f'<button class="hi-c" style="--d:{i*.06:.2f}s" aria-label="Letter {l}"><span class="hi-f"><b>{l}</b></span><span class="hi-bk"><i>{e}</i><b>{HW[l]}</b><small>{r} · {en}</small></span></button>' for i,(l,r,en,e) in enumerate(H))
G['hindi']=(f'''<article class="g-hi" data-s="hindi" role="tabpanel">
<div class="hi-hud"><span>अक्षर कार्ड · Letter cards</span><div class="hi-sc"><b>0</b>/9 learnt</div></div>
<div class="hi-g">{cards}</div>
<p class="hi-fb" aria-live="polite">Tap a card to flip it and hear the word</p></article>''',
'''<script>(function(){var a=document.querySelector('.g-hi');if(!a)return;var seen={},fb=a.querySelector('.hi-fb');function say(t){try{speechSynthesis.cancel();var u=new SpeechSynthesisUtterance(t);u.lang='hi-IN';u.rate=.8;speechSynthesis.speak(u)}catch(e){}}
a.querySelectorAll('.hi-c').forEach(function(c,i){c.onclick=function(){c.classList.toggle('fl');if(c.classList.contains('fl')){var w=c.querySelector('.hi-bk b').textContent;say(c.querySelector('.hi-f b').textContent+'. '+w);seen[i]=1;var n=Object.keys(seen).length;a.querySelector('.hi-sc b').textContent=n;fb.textContent=c.querySelector('.hi-bk small').textContent;if(n===9){fb.textContent='शाबाश! All 9 letters learnt 🎉';a.classList.add('done')}}}})})();</script>''',
'''.g-hi{position:relative;display:flex!important;flex-direction:column;gap:14px;height:100%;min-height:520px;padding:22px!important;background:radial-gradient(120% 90% at 30% 0%,#FFEDD5,#FED7AA 55%,#FB923C)!important}
.hi-hud{display:flex;justify-content:space-between;align-items:center;gap:10px}.hi-hud span{font:800 13px "Noto Sans Devanagari",Inter,sans-serif;color:#9A3412}
.hi-sc{padding:6px 14px;border-radius:999px;background:#fff;font:700 13px Inter,sans-serif;color:#57534E;box-shadow:0 6px 14px -8px #0006}.hi-sc b{font-size:16px;color:#C2410C}
.hi-g{flex:1;display:grid;grid-template-columns:repeat(3,1fr);gap:12px;perspective:900px}
.hi-c{position:relative;border:0;padding:0;background:none;cursor:pointer;transform-style:preserve-3d;transition:transform .55s cubic-bezier(.3,1.3,.5,1);animation:phin .45s var(--d) both}
.hi-c.fl{transform:rotateY(180deg)}
.hi-f,.hi-bk{position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center;border-radius:20px;backface-visibility:hidden;-webkit-backface-visibility:hidden}
.hi-f{background:#fff;box-shadow:0 7px 0 #FDBA74,0 16px 24px -14px #0006}.hi-f b{font:800 46px "Noto Sans Devanagari",sans-serif;color:#C2410C}
.hi-c:hover .hi-f{box-shadow:0 7px 0 #F97316,0 20px 28px -14px #0007}
.hi-bk{transform:rotateY(180deg);background:linear-gradient(150deg,#C2410C,#EA580C);color:#fff;box-shadow:0 7px 0 #7C2D12,0 16px 24px -14px #0006;gap:2px}
.hi-bk i{font-style:normal;font-size:34px;line-height:1}.hi-bk b{font:800 20px "Noto Sans Devanagari",sans-serif}.hi-bk small{font:600 11px Inter,sans-serif;opacity:.9;text-align:center;padding:0 4px}
.hi-fb{text-align:center!important;font:800 15px Inter,sans-serif;color:#7C2D12;min-height:22px}.g-hi.done .hi-fb{color:#15803D;animation:sbpop .4s}
@media(max-width:600px){.g-hi{min-height:480px;padding:14px!important}.hi-g{gap:8px}.hi-f b{font-size:36px}.hi-bk i{font-size:26px}.hi-bk b{font-size:16px}.hi-bk small{font-size:9.5px}}''')
css=''
for k,(art,js,c) in G.items():
    f=S+f'courses/{k}.html'; h=open(f).read()
    h=re.sub(r'<article [^>]*data-s="'+k+r'".*?</article>',lambda m:art,h,count=1,flags=re.S)
    h=h.replace('</body>',js+'</body>',1); open(f,'w').write(h); css+=c+'\n'
open(S+'assets/site.css','a').write('\n/* games v5 */\n'+css+'.cv-stage .g-ph,.cv-stage .g-hi{width:100%;align-items:stretch!important;border-radius:28px!important}\n')
print('ok')
