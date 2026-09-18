# 2. npm: el universo de paquetes

> 📚 Curso: **Node.js — JavaScript en el Servidor** · Lección 2 de 6
> 🗓 Exportado: 18/09/2026 desde Plataforma Total
> 🍅 Sugerencia: 1-2 pomodoros para leer + practicar

---

## 📖 Contenido

```javascript
NPM: DEPENDENCIAS Y SCRIPTS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
INICIALIZAR PROYECTO
  npm init -y                    → package.json (el manifiesto)

INSTALAR
  npm install express            → dependencia de producción (dependencies)
  npm install -D jest            → solo desarrollo (devDependencies: tests, builds)
  npm install                    → restaura TODO desde package.json (node_modules NO se sube a git)

  .gitignore OBLIGADO: node_modules/   (¡pesa cientos de MB!)

SCRIPTS (automatiza tu flujo)
  "scripts": {
    "dev": "node --watch src/index.js",
    "start": "node src/index.js",
    "test": "node --test"
  }
  npm run dev          (npm test va sin 'run')

VERSIONES (semver): "express": "^4.19.2"
  ^4.19.2 = 4.x.x compatible · package-lock.json fija la instalación EXACTA (súbelo a git sí).

SEGURIDAD: revisa paquetes antes de instalar; npm audit reporta vulnerabilidades.
```

---

## 📝 Quiz de la lección

### 1. ¿Por qué node_modules NUNCA va a git?
- A) Porque es secreto
- B) Es enorme y reproducible: package.json + package-lock permiten recrearlo con npm install
- C) Por licencias
- D) Porque git no lo soporta
### 2. ¿Qué significa "express": "^4.19.2"?
- A) Exactamente 4.19.2
- B) Cualquier versión 4.x.x compatible desde 4.19.2
- C) Mayor a 5
- D) Versión aleatoria

---

## 🔑 Respuestas y explicaciones

**1.** ✅ Es enorme y reproducible: package.json + package-lock permiten recrearlo con npm install — El manifiesto viaja; el contenido se instala. Así mantienen repos livianos TODOS los equipos.
**2.** ✅ Cualquier versión 4.x.x compatible desde 4.19.2 — ^ permite parches y menores compatibles; el lock file congela la realidad exacta.

---
✅ Al terminar, marca la lección como completada en la app (📚 Aprender → ✅ Completada)
