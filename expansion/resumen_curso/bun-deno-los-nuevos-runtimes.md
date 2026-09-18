# 📕 Resumen maestro — 🍞 Bun & Deno — Los Nuevos Runtimes

> Todo el curso en una hoja: una idea núcleo por lección. Releer semanal.

## 1. 1. Por qué existen: más allá de Node
 Node.js (2009) no se diseñó para TypeScript, ESM primero ni seguridad moderna. Dos runtimes modernos lo repiensan:  BUN (escrito en Zig): arranque en milisegundos, y es 4 herramie…

## 2. 2. Bun en la práctica
 Flujo diario con Bun:     bun init                 → proyecto nuevo (index.ts listo)     bun run index.ts         → ejecuta TS directamente     bun add express          → instala …

## 3. 3. Deno en la práctica
 Seguridad primero: un script no tiene permisos hasta que los pides:     deno run --allow-net --allow-read server.ts Si el código intenta usar red sin --allow-net → PermissionDenie…

## 4. 4. Frameworks modernos y despliegue edge
 El ecosistema moderno sobre estos runtimes:   · FRESH (Deno): framework web de ISLAS como Astro, sin paso de build;     escribes .tsx y despliegas al instante.   · ELYSIA (Bun): e…

---
✅ 4 lecciones · 📝 8 preguntas de repaso en quizzes_html/ · tests/