# 1. Node: sacar JS del navegador

> 📚 Curso: **Node.js — JavaScript en el Servidor** · Lección 1 de 6
> 🗓 Exportado: 18/09/2026 desde Plataforma Total
> 🍅 Sugerencia: 1-2 pomodoros para leer + practicar

---

## 📖 Contenido

```javascript
NODE: V8 EN LA TERMINAL
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Node.js corre JavaScript fuera del navegador: servidores, CLIs, scripts. Mismo lenguaje, otro hogar.

SETUP + PRIMER SCRIPT
  # instalar: nodejs.org o nvm (gestor de versiones, recomendado)
  node --version
  node app.js                  # ejecutar archivos

MÓDULOS NATIVOS CLAVE (sin instalar nada)
  const fs = require("fs");            // sistema de archivos (CommonJS clásico)
  import fs from "node:fs/promises";   // ES Modules moderno (package.json: "type": "module")
  const path = require("path");        // rutas portables
  const http = require("http");        // servidor crudo

HOLA SERVIDOR (el famoso):
  import http from "node:http";
  http.createServer((req, res) => {
    res.writeHead(200, { "Content-Type": "text/plain; charset=utf-8" });
    res.end("Hola desde Node 🚀");
  }).listen(3000, () => console.log("http://localhost:3000"));

ARCHIVOS
  await fs.writeFile("nota.txt", "hola");
  const txt = await fs.readFile("nota.txt", "utf-8");
```

---

## 📝 Quiz de la lección

### 1. ¿Qué es Node.js?
- A) Un framework
- B) Un runtime que ejecuta JS fuera del navegador (motor V8)
- C) Un editor
- D) Una base de datos
### 2. ¿Cómo activar ES Modules (import/export) en Node?
- A) npm i esm
- B) "type": "module" en package.json (o usar .mjs)
- C) No se puede
- D) Con require

---

## 🔑 Respuestas y explicaciones

**1.** ✅ Un runtime que ejecuta JS fuera del navegador (motor V8) — Mismo motor V8 de Chrome, liberado para servidores y scripts.
**2.** ✅ "type": "module" en package.json (o usar .mjs) — Con esa flag, import from 'node:fs/promises' y top-level await funcionan nativamente.

---
✅ Al terminar, marca la lección como completada en la app (📚 Aprender → ✅ Completada)
