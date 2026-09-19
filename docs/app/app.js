/* SPA Plataforma Total WEB — fetch por curso, rutas #/, freemium 15/32 */
const $ = s => document.querySelector(s);
const esc = s => s.replace(/[&<>"']/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
let INDICE = [], CK = {checkout_mensual:'../#precios',checkout_anual:'../#precios',checkout_lifetime:'../#precios'};

async function boot(){
  INDICE = await (await fetch('data/indice.json')).json();
  fetch('https://raw.githubusercontent.com/SoftEngAi-dev/plataforma-total-pro/main/monetizacion.json')
    .then(r=>r.json()).then(d=>{CK=d;}).catch(()=>{});
  window.addEventListener('hashchange', ruta);
  ruta();
}
function ruta(){
  const h = location.hash.slice(1).split('/').filter(Boolean);
  if (h[0]==='c' && h[2]!==undefined) return leccion(+h[1], +h[2]);
  if (h[0]==='c') return curso(+h[1]);
  return home();
}
function badge(f){return f?'<span class="badge b-free">🆓 GRATIS</span>':'<span class="badge b-pro">💎 PRO</span>'}

function home(){
  const q = arguments[0]||'';
  const lista = INDICE.map((c,i)=>({...c,i}))
    .filter(c=>c.n.toLowerCase().includes((q).toLowerCase()));
  const nGr = INDICE.filter(c=>c.free).length;
  $('#vista').innerHTML = `
    <h1 style="font-size:1.6rem;margin:.4rem 0 .2rem">📚 ${INDICE.length} cursos de programación, en español y gratis en tu navegador</h1>
    <p style="color:#94a3b8;margin-bottom:.6rem">${nGr} cursos completos GRATIS · los ${INDICE.length-nGr} avanzados son 💎 PRO · sin cuentas, sin registro.
    📱 Tip: usá "Añadir a pantalla principal" y queda instalada como app.</p>
    <input class="buscar" id="q" placeholder="🔍 Buscar curso… (Python, Docker, IA…)" value="${esc(q)}">
    <div class="grid">${lista.map(c=>`
      <div class="card" onclick="location.hash='#/c/${c.i}'">
        <h3>${esc(c.n)}</h3>${badge(c.free)} <span style="color:#64748b;font-size:.8rem">· ${c.l} lecciones</span>
      </div>`).join('') || '<p>Sin resultados 😅</p>'}</div>`;
  $('#q').addEventListener('input',e=>home(e.target.value));
  const el=$('#q'); el.focus(); el.setSelectionRange(el.value.length,el.value.length);
}

async function curso(i){
  const c = INDICE[i]; if(!c) return home();
  if(!c.free) return paywall(c);
  const d = await (await fetch(`data/cursos/${c.s}.json`)).json();
  $('#vista').innerHTML = `
    <a class="back" href="#/">← Todos los cursos</a>
    <h1 style="font-size:1.4rem">${esc(d.n)}</h1>
    <p style="color:#94a3b8;margin:.3rem 0 1rem">${badge(d.free)} · ${d.lecciones.length} lecciones con quiz</p>
    ${d.lecciones.map((l,j)=>`<a class="lec" href="#/c/${i}/${j}"><b>${j+1}.</b> ${esc(l.t)}</a>`).join('')}`;
}

async function leccion(i,j){
  const c = INDICE[i]; if(!c) return home();
  if(!c.free) return paywall(c);
  const d = await (await fetch(`data/cursos/${c.s}.json`)).json();
  const l = d.lecciones[j]; if(!l) return curso(i);
  const texto = esc(l.x).replace(/^.*━+.*$/gm,'<hr>').replace(/\n{2,}/g,'<br><br>').replace(/\n/g,'<br>');
  $('#vista').innerHTML = `
    <a class="back" href="#/c/${i}">← ${esc(d.n)}</a>
    <h1 style="font-size:1.25rem;margin-bottom:.8rem">${esc(l.t)}</h1>
    <div class="articulo">${texto}</div>
    ${l.q && l.q.length ? `<div class="quiz"><h2 style="font-size:1.1rem">🧠 Quiz rápido</h2>
      ${l.q.map((q,k)=>`<div class="q" data-ok="${q.ok}">
        <p>${k+1}. ${esc(q.p)}</p>
        ${q.ops.map((o,t)=>`<button class="op" data-i="${t}">${esc(o)}</button>`).join('')}
        <p class="exp">💡 ${esc(q.exp||'')}</p>
      </div>`).join('')}</div>`:''}
    <div class="row">
      ${j>0?`<a class="btn ghost" href="#/c/${i}/${j-1}">← Anterior</a>`:''}
      ${j<d.lecciones.length-1?`<a class="btn" href="#/c/${i}/${j+1}">Siguiente lección →</a>`:`<a class="btn" href="#/c/${i}">✔ Curso terminado — volver</a>`}
    </div>`;
  document.querySelectorAll('.q').forEach(qd=>{
    const ok = +qd.dataset.ok;
    qd.querySelectorAll('.op').forEach(b=>b.onclick=()=>{
      qd.querySelectorAll('.op').forEach(x=>x.disabled=true);
      if(+b.dataset.i===ok){b.classList.add('right')}else{b.classList.add('wrong');qd.querySelectorAll('.op')[ok].classList.add('right')}
      qd.querySelector('.exp').style.display='block';
    });
  });
  window.scrollTo(0,0);
}

function paywall(c){
  $('#vista').innerHTML = `
    <a class="back" href="#/">← Todos los cursos</a>
    <div class="pay">
      <h2>💎 «${esc(c.n)}» es un curso PRO</h2>
      <p style="margin:.6rem 0">Los <b>${INDICE.filter(x=>x.free).length} cursos de fundamentos son gratis aquí y para siempre</b>.
      PRO desbloquea los ${INDICE.filter(x=>!x.free).length} avanzados (y todos los futuros) en la app de escritorio:
      quizzes con IA, XP, rachas, pomodoro y certificados verificables — 100% offline.</p>
      <div class="row">
        <a class="btn ghost" id="bm" href="#">🗓️ Mensual</a>
        <a class="btn" id="ba" href="#">⭐ Anual — el favorito</a>
        <a class="btn ghost" id="bl" href="#">♾️ De por vida</a>
      </div>
      <a class="btn big" href="../">⬇️ Descargar la app gratis (15 cursos completos)</a>
      <p style="color:#64748b;font-size:.8rem;margin-top:.8rem">Tras pagar recibís tu clave por email y la activás en la app 💎</p>
    </div>`;
  $('#bm').href = CK.checkout_mensual||'../#precios';
  $('#ba').href = CK.checkout_anual||'../#precios';
  $('#bl').href = CK.checkout_lifetime||'../#precios';
}
boot();
