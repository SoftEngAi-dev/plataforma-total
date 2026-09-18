# 📜 Changelog — Plataforma Total

Todas las versiones publicadas en: https://github.com/SoftEngAi-dev/plataforma-total/releases

---

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
