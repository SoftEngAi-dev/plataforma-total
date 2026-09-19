# Changelog

## [4.2.0] - 2026-09-18
### 🚚 Mudanza — nuevo repo canónico: SoftEngAi-dev/plataforma-total-pro
- Todo el proyecto (historial completo, releases, web/PWA, marketing) migrado a **github.com/SoftEngAi-dev/plataforma-total-pro**
- La app y la web ahora leen actualizaciones, licencias y `monetizacion.json` desde el nuevo hogar
- Repo anterior queda como histórico (v4.1.0 = última release allí)
## [4.1.0] - 2026-09-18
### 🪟 ¡Ejecutable Windows de doble clic!
- **`PlataformaTotal-Windows.exe`** compilado gratis en GitHub Actions (PyInstaller onefile, icono oficial) — descarga y úsala como cualquier app, sin Python
- Auto-update consciente del formato: si la app corre como `.exe`, descarga y reemplaza el propio ejecutable (rama frozen en `_url_asset` + `_lanzar_reinstalador`)
- GitHub Pages estrena **Web App gratis + PWA instalable** (la `app/` generada en el ciclo anterior se mantiene vigente)
- FIX: paquetes de Release vuelven a llevar carpeta `PlataformaTotal/` interna (formato que espera el auto-instalador)
## [4.0.0] - 2026-09-18
### 💎 Monetización — la app ahora factura
- **Modelo freemium**: 15 cursos de fundamentos GRATIS · 32 cursos PRO (desbloqueo con clave de licencia)
- **Paywall en la app**: gate en cargador de lecciones + guarda en buscador (🔒 en cursos PRO), pantalla de conversión con beneficios, 3 planes y entrada de clave
- **Activación con Lemon Squeezy** (Merchant of Record): validación de clave online una sola vez; tras activar la app sigue 100% offline
- **`monetizacion.json` remoto**: precios y enlaces de checkout editables en el repo sin recompilar (cache 24 h)
- **Sidebar**: badge FREE/PRO + botón "💎 Ser PRO / Activar clave"
- **Landing**: nueva sección #precios (Free / Mensual 7,99 / Anual 79 / Lifetime 169 / packs 24) que lee los enlaces desde monetizacion.json
- **`MONETIZACION.md`**: análisis de mercado completo (Platzi, Codecademy, ZTM, Scrimba, Código Facilito…), justificación de precios, matemática de facturación y plan fase $0 → stores
g — Plataforma Total

Todas las versiones publicadas en: https://github.com/SoftEngAi-dev/plataforma-total-pro/releases

---

## [3.3.0] — 2026-09-18 · 🔄 Auto-actualización desde la app

### Añadido
- 🔄 **La app se actualiza a sí misma**: chequea GitHub Releases al iniciar (silencioso) y con botón "🔄 Buscar actualización" en el sidebar
- ⬇ **Instalación con 1 clic**: descarga la Release correcta para tu SO y se reinstala sola mediante un reinstalador externo (`.bat`/`.sh`) que reemplaza la app al cerrarse y la relanza
- 💻 Modo código fuente: el botón guía con `git pull`
- Indicador de versión v3.3.0 en el sidebar

## [3.2.0] — 2026-09-18 · 🚀 Stack Moderno (Astro & friends)

### Añadido
- 🚀 **Curso de Astro** (5 lecciones): islas, .astro, rutas, Content Collections y despliegue
- 💚 **Curso de Vue 3** (5): SFC, Composition API, Pinia y Nuxt 3
- ▲ **Curso de Next.js** (5): App Router, Server Components, Server Actions, SEO
- 🎨 **Curso de Tailwind CSS** (5): utility-first, responsive, dark:, @theme y shadcn/ui
- 🔥 **Curso de SvelteKit & Svelte 5** (4): runas, +page, form actions, adapters
- 🍞 **Curso de Bun & Deno** (4): los nuevos runtimes, Fresh, Elysia, Hono, edge
- **47 cursos · 269 lecciones · 538 quizzes** · **3.941 archivos** de material de expansión

## [3.1.0] — 2026-09-18 · 🏁 Proyecto Final

### Añadido
- 📖 README con insignias (release, CI, licencia), icono del proyecto y **tabla de descarga directa** con enlaces permanentes `/releases/latest/`
- 🏷️ Topics y homepage configurados en el repositorio de GitHub
- 📜 Este CHANGELOG documentando todo el recorrido
- ©️ Licencia MIT personalizada

## [3.0.3] — 2026-09-18 · 🎨 Icono oficial

### Añadido
- 🖼️ Icono oficial de la app (birrete de graduación + llaves de código `{ }`): `.ico` multi-tamaño (Windows), `.icns` (macOS) y PNG 16–512 px
- Icono **incrustado en los 3 ejecutables** (`--icon` en PyInstaller) y en la **ventana/barra de tareas** de la app (`iconphoto` con PNG empaquetado vía `--add-data`)
- Scripts de build locales actualizados con icono

## [3.0.1 → 3.0.2] — 2026-09-18 · 🔧 CI/CD

### Corregido
- El workflow ahora se dispara también con **tags `v*`** → Release automática con los 3 ejecutables adjuntos (descargas permanentes, sin caducidad)
- `actions/checkout` añadido al job de Release (`gh` necesita un repo git)

## [3.0.0] — 2026-09-18 · 🚀 Reconstrucción total

### Añadido
- 🎓 App completa: **41 cursos · 241 lecciones · 482 quizzes** (100% cobertura, validado por test)
- Buscador global 🔍 · Quizzes con IA 🤖 · Pomodoro 🍅 · Racha 🔥 · Certificados SHA-256 🎓 · Chat IA con memoria SQLite · Recomendador 🧭
- 🌱 3.601 archivos de material de estudio (`expansion/`): flashcards, ejercicios, cheatsheets, roadmaps, retos diarios, entrevistas…
- 🖥️ Ejecutable Linux compilado + workflow CI que compila **Windows/macOS/Linux** en la nube
- 🚀 Scripts guiados de subida a GitHub (PowerShell + bash) y guía paso a paso
