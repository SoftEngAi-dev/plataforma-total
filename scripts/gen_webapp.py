# -*- coding: utf-8 -*-
"""Genera docs/app/ — Plataforma Total WEB (SPA gratis) + PWA instalable (app móvil $0).
Uso: HOME=/tmp/x python scripts/gen_webapp.py"""
import json, re, unicodedata, pathlib, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
import main  # noqa

APP = ROOT / "docs" / "app"
DATA = APP / "data" / "cursos"
DATA.mkdir(parents=True, exist_ok=True)

def slug(t):
    t = unicodedata.normalize("NFKD", t).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]+", "-", t.lower()).strip("-")

def norm_quiz(q):
    """Normaliza preguntas: dict {p,ops,ok,exp} o tupla (p, ops, ok?, exp?)."""
    if isinstance(q, dict):
        return {"p": q.get("p", ""), "ops": list(q.get("ops", [])),
                "ok": int(q.get("ok", 0)), "exp": q.get("exp", "")}
    out = {"p": q[0], "ops": list(q[1]) if len(q) > 1 else [],
           "ok": int(q[2]) if len(q) > 2 and isinstance(q[2], int) else 0,
           "exp": q[3] if len(q) > 3 else ""}
    return out

# ═══ 1) datos: índice + un JSON por curso ═══
indice, slugs_gratis = [], []
for i, curso in enumerate(main._LECCIONES):
    nombre = re.sub(r"^[^\wÁÉÍÓÚáéíóúÑñüÜ]+", "", curso).strip()
    sl = f"{i+1:02d}-{slug(nombre)[:40]}"
    gratis = curso in main.CURSOS_GRATIS
    if gratis:
        slugs_gratis.append(sl)
    lecciones = []
    qmap = main.QUIZZES.get(curso, {})
    for j, tup in enumerate(main._LECCIONES[curso]):
        qs = qmap.get(j) or qmap.get(str(j)) or (tup[2] if len(tup) > 2 else [])
        lecciones.append({"t": tup[0], "x": tup[1],
                          "q": [norm_quiz(x) for x in (qs or [])]})
    (DATA / f"{sl}.json").write_text(json.dumps(
        {"n": nombre, "free": gratis, "lecciones": lecciones},
        ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
    indice.append({"s": sl, "n": nombre, "free": gratis, "l": len(lecciones)})

(APP / "data" / "indice.json").write_text(json.dumps(
    indice, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")

# ═══ 2) SPA (HTML + CSS + JS, sin dependencias) ═══
INDEX = r"""<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="theme-color" content="#0f172a">
<meta name="description" content="Plataforma Total WEB — 47 cursos de programación en español, 15 gratis para siempre, 100% en tu navegador. Instalación opcional como app.">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-title" content="Plataforma Total">
<link rel="manifest" href="manifest.webmanifest">
<link rel="icon" type="image/png" href="icon-192.png">
<link rel="apple-touch-icon" href="icon-192.png">
<title>🎓 Plataforma Total WEB — Cursos gratis en español</title>
<style>
  :root{color-scheme:dark}
  *{box-sizing:border-box;margin:0}
  body{font-family:system-ui,-apple-system,Segoe UI,Roboto,sans-serif;background:#020617;color:#e2e8f0;min-height:100vh}
  a{color:#a78bfa;text-decoration:none}
  header{position:sticky;top:0;z-index:5;background:rgba(2,6,23,.92);backdrop-filter:blur(8px);border-bottom:1px solid #1e293b;padding:.7rem 1rem;display:flex;gap:.8rem;align-items:center}
  header img{width:30px;height:30px;border-radius:8px}
  header b{font-size:1.05rem}
  header .sp{flex:1}
  .btn{background:#7c3aed;color:#fff;padding:.55rem 1rem;border-radius:.6rem;font-weight:700;border:0;cursor:pointer;font-size:.95rem}
  .btn.ghost{background:#1e293b}
  .btn.big{width:100%;padding:.8rem;font-size:1rem;margin-top:.5rem}
  main{max-width:900px;margin:0 auto;padding:1rem}
  .buscar{width:100%;background:#0f172a;border:1px solid #334155;color:#e2e8f0;border-radius:.7rem;padding:.7rem 1rem;font-size:1rem;margin:.6rem 0 1rem}
  .grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(170px,1fr));gap:.7rem}
  .card{background:#0f172a;border:1px solid #1e293b;border-radius:.8rem;padding:.9rem;cursor:pointer;transition:.15s}
  .card:hover{border-color:#7c3aed}
  .card h3{font-size:.95rem;margin-bottom:.35rem}
  .badge{display:inline-block;font-size:.7rem;padding:.15rem .5rem;border-radius:99px;font-weight:700}
  .b-free{background:#14532d;color:#bbf7d0}.b-pro{background:#4c1d95;color:#e9d5ff}
  .back{display:inline-block;margin-bottom:.8rem;font-size:.9rem}
  .lec{display:block;background:#0f172a;border:1px solid #1e293b;border-radius:.7rem;padding:.7rem .9rem;margin:.5rem 0;color:#e2e8f0;cursor:pointer;border-left:4px solid #334155}
  .lec:hover{border-left-color:#7c3aed}
  .articulo{background:#0f172a;border:1px solid #1e293b;border-radius:.9rem;padding:1.1rem;line-height:1.65;font-size:1rem;white-space:pre-wrap;word-break:break-word}
  .articulo hr{border:0;border-top:1px dashed #334155;margin:1rem 0}
  .quiz{margin-top:1.2rem;background:#0f172a;border:1px solid #334155;border-radius:.9rem;padding:1rem}
  .q{margin:1rem 0}
  .q p{font-weight:700;margin-bottom:.5rem}
  .op{display:block;width:100%;text-align:left;background:#1e293b;border:1px solid #334155;color:#e2e8f0;border-radius:.6rem;padding:.6rem .8rem;margin:.35rem 0;cursor:pointer;font-size:.95rem}
  .op.right{background:#14532d;border-color:#22c55e}
  .op.wrong{background:#7f1d1d;border-color:#ef4444}
  .exp{display:none;font-size:.9rem;color:#94a3b8;margin-top:.3rem}
  .pay{background:linear-gradient(135deg,#1e1038,#0f172a);border:1px solid #7c3aed;border-radius:1rem;padding:1.5rem;text-align:center}
  .pay h2{color:#a78bfa}
  .row{display:flex;gap:.5rem;flex-wrap:wrap;justify-content:center;margin-top:1rem}
  footer{text-align:center;color:#64748b;font-size:.8rem;padding:2rem 1rem}
  @media(max-width:520px){main{padding:.7rem}.grid{grid-template-columns:1fr 1fr}}
</style>
</head>
<body>
<header>
  <img src="icon-192.png" alt="logo">
  <b>🎓 Plataforma Total <span style="color:#a78bfa">WEB</span></b>
  <span class="sp"></span>
  <a class="btn ghost" href="../#precios" style="font-size:.85rem">💎 PRO</a>
  <a class="btn ghost" href="../" style="font-size:.85rem">⬇️ App Windows/Linux/Mac</a>
</header>
<main id="vista"></main>
<footer>Hecho en Uruguay 🇺🇾 · <a href="../">plataforma-total</a> · open-source · la app de escritorio trae quizzes con IA, XP, pomodoro y certificados</footer>
<script src="app.js"></script>
</body>
</html>
"""
(APP / "index.html").write_text(INDEX, encoding="utf-8")

APPJS = r"""/* SPA Plataforma Total WEB — fetch por curso, rutas #/, freemium 15/32 */
const $ = s => document.querySelector(s);
const esc = s => s.replace(/[&<>"']/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
let INDICE = [], CK = {checkout_mensual:'../#precios',checkout_anual:'../#precios',checkout_lifetime:'../#precios'};

async function boot(){
  INDICE = await (await fetch('data/indice.json')).json();
  fetch('https://raw.githubusercontent.com/SoftEngAi-dev/plataforma-total/main/monetizacion.json')
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
"""
(APP / "app.js").write_text(APPJS, encoding="utf-8")

# ═══ 3) PWA ═══
(APP / "manifest.webmanifest").write_text(json.dumps({
    "name": "Plataforma Total — Cursos de Programación",
    "short_name": "Plataforma",
    "description": "47 cursos de programación en español (15 gratis), offline y gratis en tu navegador.",
    "lang": "es", "start_url": "./index.html", "scope": "./",
    "display": "standalone", "orientation": "portrait",
    "background_color": "#020617", "theme_color": "#0f172a",
    "icons": [
        {"src": "icon-192.png", "sizes": "192x192", "type": "image/png", "purpose": "any"},
        {"src": "icon-512.png", "sizes": "512x512", "type": "image/png", "purpose": "any"},
        {"src": "icon-512.png", "sizes": "512x512", "type": "image/png", "purpose": "maskable"},
    ]}, ensure_ascii=False, indent=1), encoding="utf-8")

precache = ["./", "./index.html", "./app.js", "./data/indice.json",
            "./icon-192.png", "./icon-512.png"] + [f"./data/cursos/{s}.json" for s in slugs_gratis]
SW = """/* PWA offline: precache de la shell + cursos GRATIS; el resto cache-first dinámico */
const CACHE = 'pt-web-v1';
const PRE = %s;
self.addEventListener('install', e => {
  e.waitUntil(caches.open(CACHE).then(c => c.addAll(PRE)).then(() => self.skipWaiting()));
});
self.addEventListener('activate', e => {
  e.waitUntil(caches.keys().then(ks => Promise.all(ks.filter(k => k !== CACHE).map(k => caches.delete(k)))).then(() => self.clients.claim()));
});
self.addEventListener('fetch', e => {
  if (e.request.method !== 'GET') return;
  e.respondWith(caches.match(e.request).then(hit => hit || fetch(e.request).then(r => {
    if (r.ok && new URL(e.request.url).origin === location.origin) {
      const cl = r.clone(); caches.open(CACHE).then(c => c.put(e.request, cl));
    }
    return r;
  }).catch(() => hit)));
});
""" % json.dumps(precache, ensure_ascii=False)
(APP / "sw.js").write_text(SW, encoding="utf-8")

# ═══ 4) iconos ═══
from PIL import Image
src = Image.open(ROOT / "assets" / "icono-src.png").convert("RGBA")
for size in (192, 512):
    src.resize((size, size), Image.LANCZOS).save(APP / f"icon-{size}.png")

print(f"✅ WEB APP: {len(indice)} cursos ({len(slugs_gratis)} gratis), "
      f"{sum(x['l'] for x in indice)} lecciones → docs/app/")
print("   PWA: manifest + sw.js + iconos 192/512 listos")
