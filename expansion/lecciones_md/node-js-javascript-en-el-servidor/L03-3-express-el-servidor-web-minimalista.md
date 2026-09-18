# 3. Express: el servidor web minimalista

> 📚 Curso: **Node.js — JavaScript en el Servidor** · Lección 3 de 6
> 🗓 Exportado: 18/09/2026 desde Plataforma Total
> 🍅 Sugerencia: 1-2 pomodoros para leer + practicar

---

## 📖 Contenido

```javascript
EXPRESS EN 20 LÍNEAS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  import express from "express";
  const app = express();
  app.use(express.json());                 // parsea JSON del body (middleware)

  const tareas = [];

  app.get("/api/tareas", (req, res) => res.json(tareas));

  app.post("/api/tareas", (req, res) => {
    const { titulo } = req.body;
    if (!titulo) return res.status(400).json({ error: "titulo requerido" });
    const tarea = { id: Date.now(), titulo, hecha: false };
    tareas.push(tarea);
    res.status(201).json(tarea);
  });

  app.delete("/api/tareas/:id", (req, res) => {
    const i = tareas.findIndex(t => t.id === Number(req.params.id));
    if (i === -1) return res.status(404).json({ error: "no existe" });
    res.json(tareas.splice(i, 1)[0]);
  });

  app.listen(3000, () => console.log("API en http://localhost:3000"));

CONCEPTOS: rutas (método+path → función) · params (:id) · status HTTP (200 ok, 201 creado, 400 mal pedido, 404 no hay) · middleware (código que se ejecuta ANTES: json, auth, logs).
```

---

## 📝 Quiz de la lección

### 1. ¿Qué es un middleware en Express?
- A) Una base de datos
- B) Función que se ejecuta entre la petición y la ruta (JSON, auth, logs...)
- C) Un tipo de error
- D) Un plugin de VS Code
### 2. ¿Qué código HTTP corresponde a 'recurso creado'?
- A) 200
- B) 201
- C) 400
- D) 404

---

## 🔑 Respuestas y explicaciones

**1.** ✅ Función que se ejecuta entre la petición y la ruta (JSON, auth, logs...) — app.use(express.json()) transforma req.body en datos listos — ejemplo clásico.
**2.** ✅ 201 — 201 Created: convención para POST exitoso de recursos nuevos.

---
✅ Al terminar, marca la lección como completada en la app (📚 Aprender → ✅ Completada)
