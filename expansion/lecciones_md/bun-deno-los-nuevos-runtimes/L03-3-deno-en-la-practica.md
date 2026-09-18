# 3. Deno en la práctica

> 📚 Curso: **🍞 Bun & Deno — Los Nuevos Runtimes** · Lección 3 de 4
> 🗓 Exportado: 18/09/2026 desde Plataforma Total
> 🍅 Sugerencia: 1-2 pomodoros para leer + practicar

---

## 📖 Contenido

```text

Seguridad primero: un script no tiene permisos hasta que los pides:
    deno run --allow-net --allow-read server.ts
Si el código intenta usar red sin --allow-net → PermissionDenied, y tú
decides. --allow-read=./datos limita incluso el directorio.

TypeScript nativo:
    // hola.ts — se ejecuta tal cual, sin tsc ni build
    const saludar = (n: string): string => `Hola ${n}`;
    console.log(saludar("Deno"));

Imports modernos: URLs, npm:, jsr: (registro de Deno) y deno.json para
mapear imports y tareas ("tasks": { "dev": "deno run --watch main.ts" }).

HTTP estándar:
    Deno.serve({ port: 8000 }, (_req) => new Response("Hola Deno"));

Herramientas de serie (cero configuración): deno fmt (formatea),
deno lint (analiza), deno test (tests), deno compile (un binario
ejecutable de tu app). Menos node_modules, más estándares Web.
```

---

## 📝 Quiz de la lección

### 1. ¿Qué pasa si un script de Deno usa la red sin --allow-net?
- A) Deno lanza PermissionDenied y bloquea la operación
- B) Funciona igual
- C) Lo reporta por email
- D) Se reinicia el PC
### 2. ¿Qué herramientas trae Deno integradas sin configuración?
- A) fmt, lint y test (además de compile)
- B) Solo el runtime
- C) Photoshop
- D) Docker

---

## 🔑 Respuestas y explicaciones

**1.** ✅ Deno lanza PermissionDenied y bloquea la operación — El sandbox de Deno exige permisos explícitos por recurso: seguridad real por defecto.
**2.** ✅ fmt, lint y test (además de compile) — deno fmt, deno lint, deno test y deno compile vienen de serie: toolchain todo-en-uno.

---
✅ Al terminar, marca la lección como completada en la app (📚 Aprender → ✅ Completada)
