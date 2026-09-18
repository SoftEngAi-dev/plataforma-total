# 1. Por qué existen: más allá de Node

> 📚 Curso: **🍞 Bun & Deno — Los Nuevos Runtimes** · Lección 1 de 4
> 🗓 Exportado: 18/09/2026 desde Plataforma Total
> 🍅 Sugerencia: 1-2 pomodoros para leer + practicar

---

## 📖 Contenido

```text

Node.js (2009) no se diseñó para TypeScript, ESM primero ni seguridad
moderna. Dos runtimes modernos lo repiensan:

BUN (escrito en Zig): arranque en milisegundos, y es 4 herramientas en 1
— runtime, BUNDLER, TEST RUNNER y GESTOR DE PAQUETES (bun install es
muchísimo más rápido que npm). Compatible con APIs de Node y con tu
package.json: puedes probarlo en proyectos actuales casi sin cambios.

DENO (escrito en Rust, del creador original de Node): TypeScript NATIVO
sin paso de build, SEGURO por defecto (el código no toca red ni disco sin
permisos explícitos), estándar moderna (@std) y registro propio JSR.

¿Cuándo usar cada uno?
  · Bun: velocidad extrema y tooling en ecosistemas Node actuales.
  · Deno: proyectos TypeScript estrictos, scripts seguros y edge
    (Deno Deploy reparte tu app por el mundo sin servidores).
```

---

## 📝 Quiz de la lección

### 1. ¿Qué incluye Bun además del runtime?
- A) Bundler, test runner y gestor de paquetes
- B) Una base de datos
- C) Un editor de código
- D) Un navegador
### 2. ¿Cuál es el principio de seguridad por defecto de Deno?
- A) Permisos explícitos (--allow-net, --allow-read…)
- B) Ejecuta todo como root
- C) Bloquea la red para siempre
- D) Solo permite HTTPS

---

## 🔑 Respuestas y explicaciones

**1.** ✅ Bundler, test runner y gestor de paquetes — Bun unifica herramientas: bun install, bun test y el bundler vienen de serie, todo muy rápido.
**2.** ✅ Permisos explícitos (--allow-net, --allow-read…) — Sin --allow-* el código no puede salir de su caja de arena: ideal para scripts de terceros.

---
✅ Al terminar, marca la lección como completada en la app (📚 Aprender → ✅ Completada)
