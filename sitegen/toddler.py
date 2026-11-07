import re
P='/home/claude/site/'
WA='https://wa.me/919965032227'
main='''<main id="main">
<section class="td-hero"><div class="w td-hi">
<div><p class="kick">Toddler Care · Moolapalayam</p><h1>Where little learners feel at home.</h1>
<p class="lede">A warm, play-based first classroom that eases your child from home into learning — through sensory discovery, movement and happy friendships.</p>
<div class="row"><a class="btn btn-dark" href="#enroll">Enroll in Toddler Care →</a><a class="btn btn-line" href="#process">How admission works</a></div>
<p class="td-age">👶 For toddlers — ask us about age groups and batch timings</p></div>
<div class="td-art" aria-hidden="true"><span class="b1">🧸</span><span class="b2">🎨</span><span class="b3">🎵</span><span class="b4">🧩</span><div class="td-c">🌱</div></div></div></section>

<section class="sec"><div class="w"><div class="sh"><div><p class="kick">Every milestone</p><h2>Key areas of development.</h2></div></div>
<div class="td-g3">
<div class="td-a" style="--c:#F3E8FF;--t:#7C3AED"><span>🧠</span><h3>Senses &amp; thinking</h3><p>Creative play, art and sensory exploration that keep young minds curious.</p></div>
<div class="td-a" style="--c:#DCFCE7;--t:#15803D"><span>🤸</span><h3>Movement &amp; coordination</h3><p>Purposeful activities that build balance, agility and fine and gross motor skills.</p></div>
<div class="td-a" style="--c:#FFEDD5;--t:#C2410C"><span>💬</span><h3>Language &amp; social skills</h3><p>Songs, stories and group play that help children speak up and make friends.</p></div>
</div></div></section>

<section class="sec sec-alt"><div class="w"><div class="sh"><div><p class="kick">Why parents choose us</p><h2>Confidence for parents, joy for children.</h2></div></div>
<div class="td-g3 why6">
<div class="td-w"><span>🛡️</span><h3>Safe, child-friendly space</h3><p>Rooms set up for little ones, with caring staff watching over every child.</p></div>
<div class="td-w"><span>🤗</span><h3>Teachers who care like family</h3><p>Patience, encouragement and individual attention for every child.</p></div>
<div class="td-w"><span>🔍</span><h3>Learning through exploration</h3><p>Activities that spark curiosity and strengthen thinking and coordination.</p></div>
<div class="td-w"><span>🧼</span><h3>Clean &amp; hygienic</h3><p>Tidy classrooms, cleaned toys and good hygiene habits every day.</p></div>
<div class="td-w"><span>📖</span><h3>Learning made fun</h3><p>Storytelling, music, art and hands-on play instead of rote lessons.</p></div>
<div class="td-w"><span>👨‍👩‍👧</span><h3>Growing together</h3><p>We keep parents in the loop on how their child is settling in and growing.</p></div>
</div></div></section>

<section class="sec" id="process"><div class="w"><div class="sh"><div><p class="kick">Admission</p><h2>Four simple steps.</h2></div></div>
<ol class="td-steps">
<li><b>01</b><h3>Fill the form</h3><p>Share your child's and your details in the form below.</p></li>
<li><b>02</b><h3>Share documents</h3><p>We'll tell you which documents to bring, such as a birth certificate and photos.</p></li>
<li><b>03</b><h3>Friendly visit</h3><p>A relaxed meeting so our teachers can get to know your child.</p></li>
<li><b>04</b><h3>Admission confirmed</h3><p>We share the fees and the start date, and your child begins.</p></li>
</ol></div></section>

<section class="sec sec-alt" id="enroll"><div class="w td-fw">
<div class="td-fi"><p class="kick">Enrollment form</p><h2>Enroll in 3 easy steps.</h2><p class="muted">Your details are sent to us on WhatsApp — nothing is stored on this website.</p>
<div class="td-help"><a href="'''+WA+'''?text=Hello%20Eureka%20Academy%2C%20I%20have%20a%20question%20about%20Toddler%20Care." target="_blank" rel="noopener"><span>💬</span><div><small>Quick chat</small><b>WhatsApp enquiry</b></div></a>
<a href="tel:+919965032227"><span>📞</span><div><small>Call us</small><b>99650 32227</b></div></a>
<a href="https://maps.app.goo.gl/d6kSKBfJiE24eaty6" target="_blank" rel="noopener"><span>📍</span><div><small>Visit with your little one</small><b>Guru Moorthy Doctor Building, Poondurai Rd</b></div></a></div></div>
<form class="td-form" id="tdf" novalidate>
<div class="td-prog"><span id="tdS">Step 1 of 3</span><div><i id="tdB"></i></div></div>
<fieldset class="td-st on" data-t="Child's information"><legend>Child's information</legend>
<label>Child's full name *<input name="child" required autocomplete="off"></label>
<label>Gender *<select name="gender" required><option value="">Select</option><option>👦 Boy</option><option>👧 Girl</option><option>✨ Other</option></select></label>
<div class="td-2"><label>Date of birth *<input type="date" name="dob" id="tdDob" required></label><label>Age<input name="age" id="tdAge" readonly placeholder="auto"></label></div></fieldset>
<fieldset class="td-st" data-t="Parent details"><legend>Parent details</legend>
<label>Parent / guardian name *<input name="parent" required autocomplete="name"></label>
<label>Phone number *<input name="phone" type="tel" required pattern="[0-9+ ]{10,14}" autocomplete="tel"></label>
<label>Area / locality<input name="area" placeholder="e.g. Moolapalayam"></label></fieldset>
<fieldset class="td-st" data-t="Preferences"><legend>Preferences</legend>
<label>Preferred start<select name="start"><option>As soon as possible</option><option>Next month</option><option>Just exploring</option></select></label>
<label>Anything we should know?<textarea name="note" rows="3" placeholder="Allergies, habits, interests…"></textarea></label>
<label class="td-chk"><input type="checkbox" name="visit" checked> I'd like to visit the centre first</label></fieldset>
<p class="td-err" id="tdE" role="alert"></p>
<div class="td-nav"><button type="button" class="btn btn-line" id="tdP" hidden>← Back</button><button type="button" class="btn btn-dark" id="tdN">Next →</button></div>
</form></div></section>
</main>'''
js='''<script>(function(){var f=document.getElementById('tdf');if(!f)return;var s=[].slice.call(f.querySelectorAll('.td-st')),i=0,N=document.getElementById('tdN'),P=document.getElementById('tdP'),E=document.getElementById('tdE');
function show(){s.forEach(function(x,k){x.classList.toggle('on',k===i)});document.getElementById('tdS').textContent='Step '+(i+1)+' of 3 · '+s[i].dataset.t;document.getElementById('tdB').style.width=((i+1)/3*100)+'%';P.hidden=i===0;N.textContent=i===2?'Send on WhatsApp ➤':'Next →';E.textContent=''}
function ok(){var bad=[].slice.call(s[i].querySelectorAll('[required]')).filter(function(x){return !x.checkValidity()});bad.forEach(function(x){x.classList.add('bad')});if(bad.length){E.textContent='Please fill the highlighted fields.';bad[0].focus();return false}return true}
f.addEventListener('input',function(e){e.target.classList.remove('bad')});
document.getElementById('tdDob').addEventListener('change',function(){var d=new Date(this.value),n=new Date();if(isNaN(d))return;var m=(n.getFullYear()-d.getFullYear())*12+n.getMonth()-d.getMonth()-(n.getDate()<d.getDate()?1:0);document.getElementById('tdAge').value=m<0?'':Math.floor(m/12)+' yrs '+(m%12)+' mo'});
P.onclick=function(){i--;show()};
N.onclick=function(){if(!ok())return;if(i<2){i++;show();return}var v=new FormData(f);var t='Toddler Care enrollment%0A'+['Child: '+v.get('child'),'Gender: '+v.get('gender'),'DOB: '+v.get('dob')+' ('+v.get('age')+')','Parent: '+v.get('parent'),'Phone: '+v.get('phone'),'Area: '+(v.get('area')||'-'),'Start: '+v.get('start'),'Visit first: '+(v.get('visit')?'Yes':'No'),'Notes: '+(v.get('note')||'-')].map(encodeURIComponent).join('%0A');window.open('https://wa.me/919965032227?text='+t,'_blank')};show()})();</script>'''
h=open(P+'toddler-care.html').read()
a=h.index('<main'); b=h.index('</main>')+7
h=h[:a]+main+h[b:]
h=h.replace('</body>',js+'</body>',1)
open(P+'toddler-care.html','w').write(h)

# home teaser
x=open(P+'index.html').read()
teaser='''<section class="sec hx-td"><div class="w"><div class="tdh">
<div class="tdh-art" aria-hidden="true"><span>🧸</span><span>🧩</span><span>🎨</span><span>🎵</span></div>
<div class="tdh-t"><p class="kick">Toddler Care</p><h2>Where little learners feel at home.</h2><p>A warm, play-based first classroom for toddlers — sensory play, movement, songs and stories with caring teachers.</p>
<ul><li>🧠 Senses &amp; thinking</li><li>🤸 Movement &amp; coordination</li><li>💬 Language &amp; social skills</li></ul>
<div class="row"><a class="btn btn-dark" href="toddler-care.html#enroll">Enroll now →</a><a class="btn btn-line" href="toddler-care.html">Learn more</a></div></div></div></div></section>'''
if 'hx-td' not in x:
    k=x.index('<section class="sec hx-why"'); x=x[:k]+teaser+x[k:]
open(P+'index.html','w').write(x); print('ok')
