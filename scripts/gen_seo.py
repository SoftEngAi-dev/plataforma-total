# -*- coding: utf-8 -*-
"""Inyecta sección SEO (47 cursos) + JSON-LD en docs/index.html. Idempotente."""
import json, re, unicodedata, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
import sys; sys.path.insert(0, str(ROOT))
import main  # noqa

IDX = ROOT / "docs" / "index.html"
html = IDX.read_text(encoding="utf-8")
if 'id="cursos-seo"' in html:
    print("⏭️  sección SEO ya existe — nada que hacer")
    sys.exit(0)

def slug(t):
    t = unicodedata.normalize("NFKD", t).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]+", "-", t.lower()).strip("-")

def limpio(t):  # nombre sin emojis para texto SEO
    return re.sub(r"[^\w\sÁÉÍÓÚáéíóúÑñüÜ#+./—'-]", "", t).strip()

cards, items = [], []
for i, curso in enumerate(main.CURSOS, 1):
    nombre = limpio(curso)
    gratis = curso in main.CURSOS_GRATIS
    badge = '<span class="badge" style="background:#14532d">🆓 GRATIS</span>' if gratis else '<span class="badge" style="background:#4c1d95">💎 PRO</span>'
    desc = (f"Curso completo de {nombre} en español: lecciones guiadas paso a paso, quizzes con IA, "
            f"práctica real y 100% disponible sin internet.")
    cards.append(f'''<div class="card" id="curso-{slug(nombre)}">
      <h3 style="font-size:1rem">{nombre} {badge}</h3>
      <p style="margin:.4rem 0 0">{desc}</p>
    </div>''')
    items.append({
        "@type": "Course", "name": nombre, "description": desc,
        "provider": {"@type": "Organization", "name": "Plataforma Total",
                     "sameAs": "https://github.com/SoftEngAi-dev/plataforma-total"},
        "isAccessibleForFree": gratis, "inLanguage": "es",
        "offers": {"@type": "Offer", "price": 0 if gratis else 79, "priceCurrency": "USD"},
    })

n_gr = len(main.CURSOS_GRATIS)
seo = f'''
  <h2 id="cursos-seo">🌍 Los 47 cursos — aprende programación en español, con o sin internet</h2>
  <p class="note">Buscabas <b>un curso de programación gratis en español</b> que funcione <b>offline</b>?
  Plataforma Total es la app de escritorio (Windows, Linux, macOS) con <b>{n_gr} cursos completos gratis para siempre</b>
  y 32 cursos PRO desde U$S 7,99/mes. Sin cuentas, sin streaming, sin límites de datos: la escuela vive en tu PC.
  Cada curso incluye lecciones guiadas, <b>538 quizzes con IA</b>, gamificación (XP, rachas, pomodoro) y <b>certificados verificables</b>.</p>
  <div class="grid" style="grid-template-columns: repeat(auto-fill, minmax(260px, 1fr)); display:grid; gap:1rem">
    {''.join(cards)}
  </div>

  <h2 id="faq">❓ Preguntas frecuentes</h2>
  <div class="card"><h3>¿Realmente es gratis?</h3><p>Sí: los {n_gr} cursos de fundamentos (HTML, CSS, JavaScript, Python, SQL, Git, Docker, Linux, DevOps…) son 100% gratis para siempre, sin tarjeta y sin cuenta. Los 32 cursos avanzados se desbloquean con PRO desde U$S 7,99/mes.</p></div>
  <div class="card"><h3>¿Funciona sin internet?</h3><p>Es nuestra especialidad: la app es 100% offline. Solo necesitas internet un minuto para descargarla, para auto-actualizarte a nuevas versiones y, si eres PRO, una sola vez para validar tu clave.</p></div>
  <div class="card"><h3>¿En qué sistemas anda?</h3><p>Windows (.exe), Linux y macOS. Una sola descarga desde GitHub Releases y listo — la app se actualiza sola.</p></div>
  <div class="card"><h3>¿Da certificados?</h3><p>Sí: cada curso completado genera un certificado con código verificable, más XP, rachas y pomodoro integrados.</p></div>
  <div class="card"><h3>¿Cómo activo PRO?</h3><p>Compras en la sección <a href="#precios">💎 Planes</a>, recibes tu clave por email en ~1 minuto y la pegas en el botón "💎 Ser PRO" de la app. Después todo sigue offline.</p></div>
'''

ld = {"@context": "https://schema.org", "@graph": [
    {"@type": "ItemList", "name": "Cursos de Plataforma Total", "itemListElement": items},
    {"@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": "¿Plataforma Total es gratis?",
         "acceptedAnswer": {"@type": "Answer", "text": f"Los {n_gr} cursos de fundamentos son 100% gratis para siempre; los 32 avanzados con PRO desde U$S 7,99/mes."}},
        {"@type": "Question", "name": "¿Funciona sin internet?",
         "acceptedAnswer": {"@type": "Answer", "text": "Sí, es 100% offline tras la descarga. La activación PRO requiere internet una sola vez."}},
        {"@type": "Question", "name": "¿En qué sistemas funciona?",
         "acceptedAnswer": {"@type": "Answer", "text": "Windows, Linux y macOS, con auto-actualización incluida."}},
    ]},
]}
seo += '\n<script type="application/ld+json">\n' + json.dumps(ld, ensure_ascii=False, indent=1) + "\n</script>\n"

MARKER = '  <h2>🚀 Empieza en 2 minutos</h2>'
assert MARKER in html, "marcador no encontrado"
html = html.replace(MARKER, seo + "\n" + MARKER, 1)
IDX.write_text(html, encoding="utf-8")
print(f"✅ SEO inyectado: {len(cards)} cursos + FAQ + JSON-LD ({len(html)} chars)")
