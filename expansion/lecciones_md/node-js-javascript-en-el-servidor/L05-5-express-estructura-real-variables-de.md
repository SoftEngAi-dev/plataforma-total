# 5. Express + estructura real + variables de entorno

> 📚 Curso: **Node.js — JavaScript en el Servidor** · Lección 5 de 6
> 🗓 Exportado: 18/09/2026 desde Plataforma Total
> 🍅 Sugerencia: 1-2 pomodoros para leer + practicar

---

## 📖 Contenido

```javascript
DE EJEMPLO A PROYECTO REAL
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ESTRUCTURA PROFESIONAL
  src/
    index.js          ← arranque (escucha puerto)
    app.js            ← configura express (testeable sin listen)
    rutas/tareas.js   ← router por recurso: express.Router()
    datos/db.js       ← acceso a datos
    middleware/auth.js
  tests/

ROUTER MODULAR
  // rutas/tareas.js
  import { Router } from "express";
  const r = Router();
  r.get("/", (req, res) => res.json(tareas));
  export default r;
  // app.js:  app.use("/api/tareas", rutasTareas);

VARIABLES DE ENTORNO — secretos FUERA del código
  .env:   DB_URL=postgres://...   JWT_SECRET=secreto
  npm i dotenv →  import "dotenv/config";  →  process.env.DB_URL
  .gitignore: .env   (NUNCA subas secretos)
  En producción: las variables reales las pone el servidor (Railway, VPS...).

CORS si tu frontend está en otro puerto:
  npm i cors → app.use(cors());
```

---

## 📝 Quiz de la lección

### 1. ¿Por qué los secretos van en variables de entorno y no en el código?
- A) Por velocidad
- B) Para no publicarlos en git y poder variarlos por entorno (dev/prod)
- C) Porque .env es más rápido
- D) No hay diferencia
### 2. ¿Qué aporta separar app.js de index.js (listen)?
- A) Nada útil
- B) Puedes importar y TESTEAR la app sin abrir puerto; separa configuración de ejecución
- C) Es solo estética
- D) Usa menos memoria

---

## 🔑 Respuestas y explicaciones

**1.** ✅ Para no publicarlos en git y poder variarlos por entorno (dev/prod) — Código público + secretos = filtración. .env + .gitignore es la norma; nunca commitees el .env.
**2.** ✅ Puedes importar y TESTEAR la app sin abrir puerto; separa configuración de ejecución — La app testeable se exporta sin listen; en tests corren peticiones contra ella con supertest.

---
✅ Al terminar, marca la lección como completada en la app (📚 Aprender → ✅ Completada)
