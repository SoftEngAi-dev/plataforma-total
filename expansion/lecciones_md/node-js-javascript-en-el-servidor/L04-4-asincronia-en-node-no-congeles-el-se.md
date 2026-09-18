# 4. Asincronía en Node: no congeles el servidor

> 📚 Curso: **Node.js — JavaScript en el Servidor** · Lección 4 de 6
> 🗓 Exportado: 18/09/2026 desde Plataforma Total
> 🍅 Sugerencia: 1-2 pomodoros para leer + practicar

---

## 📖 Contenido

```javascript
EL EVENT LOOP: EL MOTOR DE NODE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Node corre TODO en un hilo. Una operación lenta sincrónica CONGELA a todos los usuarios a la vez. Solución: async SIEMPRE en I/O.

  // ❌ bloqueante
  const datos = fs.readFileSync("grande.txt", "utf-8");

  // ✅ no bloqueante (promesas)
  const datos = await fs.readFile("grande.txt", "utf-8");

EN RUTAS EXPRESS: async handlers
  app.get("/api/datos", async (req, res, next) => {
    try {
      const datos = await db.query("SELECT * FROM tareas");
      res.json(datos);
    } catch (e) { next(e); }              // pásalo al middleware de errores
  });

MIDDLEWARE DE ERRORES (al final, con 4 parámetros — así lo reconoce Express)
  app.use((err, req, res, next) => {
    console.error(err);
    res.status(500).json({ error: "Error interno" });
  });

IMAGINA: camarero único (Node). Si se queda limpiando una mesa, toda la fila espera. I/O async = toma el pedido y sigue; la cocina avisa cuando está listo.
```

---

## 📝 Quiz de la lección

### 1. ¿Por qué prohibir readFileSync en un servidor (salvo arranque)?
- A) Es más lento
- B) Bloquea el único hilo de Node: TODOS los usuarios esperan
- C) Está deprecado
- D) Usa mucha RAM
### 2. ¿Cómo reconoce Express un middleware de errores?
- A) Por su nombre
- B) Tiene exactamente 4 parámetros (err, req, res, next)
- C) Está primero
- D) Lleva try/catch

---

## 🔑 Respuestas y explicaciones

**1.** ✅ Bloquea el único hilo de Node: TODOS los usuarios esperan — El event loop único detenido = servidor congelado para todos.
**2.** ✅ Tiene exactamente 4 parámetros (err, req, res, next) — La firma de 4 argumentos es el contrato; se registra DESPUÉS de las rutas.

---
✅ Al terminar, marca la lección como completada en la app (📚 Aprender → ✅ Completada)
