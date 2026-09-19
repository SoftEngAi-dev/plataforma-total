# 🌐📱 WEB APP + APP MÓVIL — Plataforma Total (100% gratis, costo $0)
### Guía de qué se lanzó, URLs oficiales y cómo usarlas (incluye campo "website" de Lemon Squeezy)

---

## 1. 🚀 Qué se lanzó (Septiembre 2026)

| Producto | URL | Costo | Qué es |
|---|---|---|---|
| 🌐 **Landing** | https://softengai-dev.github.io/plataforma-total-pro/ | $0 (GitHub Pages) | Portada + descargas + 💎 planes + SEO 47 cursos |
| 🌐 **Web App** | https://softengai-dev.github.io/plataforma-total-pro/app/ | $0 | La plataforma **en el navegador**: buscador, 47 cursos listados, 15 gratis completos (269 lecciones disponibles en las FREE), quizzes interactivos |
| 📱 **App móvil (PWA)** | la misma URL `/app/` desde el celular | $0 | Se instala como app nativa (icono, pantalla completa, modo offline) — sin stores, sin cuentas de desarrollador |

> Arquitectura: una SPA vanilla (sin frameworks, sin build) + JSON estáticos generados desde el mismo contenido de la app de escritorio (`scripts/gen_webapp.py`). Se sirve gratis desde GitHub Pages para siempre.

## 2. 🆓💎 Cómo funciona el freemium en la web

- **GRATIS en web/PWA**: los 15 cursos de fundamentos completos (lecciones + quizzes) — el mejor gancho: "una escuela gratis que funciona sin internet, desde cualquier dispositivo".
- **💎 PRO**: los 32 cursos avanzados muestran en la web el mismo paywall → botones de compra (leen `monetizacion.json`) → la clave se activa en la **app de escritorio** (experiencia completa: XP, rachas, pomodoro, IA local, certificados). La web vende, el desktop retiene.

## 3. 📲 Cómo instalarla en el celular (para vos y los usuarios)

- **Android (Chrome):** abrir https://softengai-dev.github.io/plataforma-total-pro/app/ → menú ⋮ → **«Instalar app»** o «Añadir a pantalla principal». Listo: icono, fullscreen y **modo offline** (los 15 cursos gratis quedan en caché).
- **iPhone (Safari):** abrir la URL → botón **Compartir** → **«Añadir a pantalla de inicio»**.
- Funciona gracias a `manifest.webmanifest` + `sw.js` (service worker con los cursos gratis en pre-caché).

## 4. 🍋 Para Lemon Squeezy — los campos exactos al crear la cuenta

Cuando LS te pida datos de la tienda/producto, usá:

| Campo | Valor |
|---|---|
| **Store name** | `Plataforma Total` |
| **Website URL** | `https://softengai-dev.github.io/plataforma-total-pro/` |
| **Product URL** (si lo pide por producto) | `https://softengai-dev.github.io/plataforma-total-pro/app/` |
| Descripción corta | "Escuela de programación en español y offline: app de escritorio + web/PWA con 47 cursos (15 gratis). Suscripción PRO mensual/anual/lifetime desbloquea los 32 avanzados." |
| País | Uruguay 🇺🇾 |

Con esa web **ya "tenés algo"**: producto funcionando gratis, descargas reales y precios visibles — la verificación de tiendas así se aprueba rápido.

## 5. 🗺️ Roadmap móvil (honesto)

| Fase | Estado | Costo |
|---|---|---|
| **PWA instalable (Android+iOS)** | ✅ **YA LIVE** | $0 |
| Web PRO con clave (validar licencia también en la web) | 🔜 mejora futura | $0 |
| Flutter nativa + Play Store/App Store | Fase 3 — solo cuando factures ≥ U$S 50K/año (comisiones de store 15% y port dedicado; ver MONETIZACION.md §7) | 💸 |

**Regenerar tras agregar cursos:** `HOME=/tmp/x python scripts/gen_webapp.py` → commit → push (queda nuevo contenido en web/PWA automáticamente).
