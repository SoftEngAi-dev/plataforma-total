# 4. Frameworks modernos y despliegue edge

> 📚 Curso: **🍞 Bun & Deno — Los Nuevos Runtimes** · Lección 4 de 4
> 🗓 Exportado: 18/09/2026 desde Plataforma Total
> 🍅 Sugerencia: 1-2 pomodoros para leer + practicar

---

## 📖 Contenido

```text

El ecosistema moderno sobre estos runtimes:
  · FRESH (Deno): framework web de ISLAS como Astro, sin paso de build;
    escribes .tsx y despliegas al instante.
  · ELYSIA (Bun): estilo Express pero con tipos end-to-end y una
    velocidad asombrosa aprovechando Bun.
  · HONO: ultraligero y MULTI-RUNTIME: el mismo código corre en Deno,
    Bun, Node y workers del edge (Cloudflare, Vercel) — escribe una vez.

Despliegue moderno:
  · Deno Deploy: git push → tu app en el edge global en segundos, con
    KV/queues/cron integrados y TLS gratis.
  · Bun: Fly.io, Railway o tu VPS (arranque en frío casi instantáneo).

En serverless/edge el ARRANQUE EN FRÍO manda: Bun y Deno inician en
milisegundos frente a cientos de ms de un Node cargado de dependencias.
Por eso dominan en APIs pequeñas, webhooks y middlewares del edge.
```

---

## 📝 Quiz de la lección

### 1. ¿Qué framework corre el MISMO código en Deno, Bun, Node y workers del edge?
- A) Hono
- B) Rails
- C) Django
- D) Laravel
### 2. ¿Qué es Fresh?
- A) El framework de islas para Deno, sin paso de build
- B) Un gestor de paquetes
- C) Un bundler
- D) Una base de datos

---

## 🔑 Respuestas y explicaciones

**1.** ✅ Hono — Hono es ultraligero y multi-runtime: una API escrita una vez despliega en todos los runtimes.
**2.** ✅ El framework de islas para Deno, sin paso de build — Fresh aplica arquitectura de islas (como Astro) sobre Deno con Preact: cero build, súper rápido.

---
✅ Al terminar, marca la lección como completada en la app (📚 Aprender → ✅ Completada)
