# 2. Bun en la práctica

> 📚 Curso: **🍞 Bun & Deno — Los Nuevos Runtimes** · Lección 2 de 4
> 🗓 Exportado: 18/09/2026 desde Plataforma Total
> 🍅 Sugerencia: 1-2 pomodoros para leer + practicar

---

## 📖 Contenido

```text

Flujo diario con Bun:
    bun init                 → proyecto nuevo (index.ts listo)
    bun run index.ts         → ejecuta TS directamente
    bun add express          → instala rapidísimo (bun.lock)
    bun run dev              → corre scripts del package.json
    bun test                 → tests integrados API tipo Jest
                              (import { test, expect } from "bun:test")

Ejecuta TypeScript y JSX SIN configurar transpiladores: escribes .ts y
corre. También trae watch mode (--watch) y hot reload.

Servidor HTTP nativo sin frameworks, rapidísimo:
    Bun.serve({
      port: 3000,
      fetch(req) {
        return new Response("Hola desde Bun");
      },
    });
    console.log("http://localhost:3000");

APIs modernas de Web (fetch, Response, Request) son ciudadanos de
primera clase; muchas APIs de Node (fs, path, process) también funcionan.
```

---

## 📝 Quiz de la lección

### 1. ¿Qué comando ejecuta los tests integrados de Bun?
- A) bun test
- B) npm test
- C) bun check
- D) deno test
### 2. ¿Cómo levanta Bun un servidor HTTP sin Express?
- A) Con Bun.serve({ fetch })
- B) Con http.createServer solamente
- C) Con nginx
- D) No puede

---

## 🔑 Respuestas y explicaciones

**1.** ✅ bun test — bun test incluye runner con API estilo Jest (describe/test/expect), sin instalar nada.
**2.** ✅ Con Bun.serve({ fetch }) — Bun.serve es el servidor nativo de alto rendimiento con handlers fetch estándar Web.

---
✅ Al terminar, marca la lección como completada en la app (📚 Aprender → ✅ Completada)
