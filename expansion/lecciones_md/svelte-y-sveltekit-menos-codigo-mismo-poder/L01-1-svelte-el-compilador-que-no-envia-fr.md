# 1. Svelte: el compilador que no envía framework

> 📚 Curso: **Svelte y SvelteKit — Menos Código, Mismo Poder** · Lección 1 de 3
> 🗓 Exportado: 18/09/2026 desde Plataforma Total
> 🍅 Sugerencia: 1-2 pomodoros para leer + practicar

---

## 📖 Contenido

```svelte
SVELTE: TU CÓDIGO SE CONVIERTE EN JS PURO VANILLA
━━━━━━━━━━━━━━━━━━━━━━━━━━━
Idea radical: React/Vue envían su runtime al navegador; Svelte COMPILA tus .svelte a JavaScript puro quirúrgico. Sin virtual DOM. Bundles minúsculos, velocidad por diseño.

  <!-- Contador.svelte — TODO vive en un archivo (script + plantilla + estilos) -->
  <script>
      let cuenta = 0;
      $: doble = cuenta * 2;                    // $: = reactivo puramente declarativo

      function incrementar() { cuenta += 1; }    // ¡asignar y listo! no setState
  </script>

  <h1>Clicks: {cuenta}</h1>
  <p>El doble es {doble}</p>
  <button on:click={incrementar}>+1</button>

  <style>
      h1 { color: purple; }                      /* estilos con SCOPE al componente */
      button { border-radius: 8px; }
  </style>

COMPARA LA MENTE:
• Estado: let x = 0 normal; modificar variable = re-render (sin setState, sin signals)
• $: etiqueta reactiva: corre de nuevo automáticamente cuando cambian sus dependencias
• on:evento · {expresión} en el markup · #if/#each/#await bloques nativos

SETUP: npm create vite@latest miblog -- --template svelte (o SvelteKit para app completa).
```

---

## 📝 Quiz de la lección

### 1. ¿Cuál es la gran diferencia técnica de Svelte?
- A) Usa Python
- B) Es un compilador: no hay runtime de framework en el navegador, genera JS vanilla quirúrgico
- C) Es más lento
- D) Usa virtual DOM
### 2. ¿Qué hace la etiqueta $: en el script?
- A) JQuery
- B) Declaración reactiva: re-ejecuta la línea automáticamente cuando cambian las variables que usa
- C) Un import
- D) CSS

---

## 🔑 Respuestas y explicaciones

**1.** ✅ Es un compilador: no hay runtime de framework en el navegador, genera JS vanilla quirúrgico — Menos código enviado + actualizaciones DOM precisas = apps veloces y bundles chicos.
**2.** ✅ Declaración reactiva: re-ejecuta la línea automáticamente cuando cambian las variables que usa — $: doble = cuenta * 2 → doble siempre fresco sin lógica manual. Elegancia mínima.

---
✅ Al terminar, marca la lección como completada en la app (📚 Aprender → ✅ Completada)
