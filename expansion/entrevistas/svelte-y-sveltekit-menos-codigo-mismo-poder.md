# 🎤 Banco de entrevista — Svelte y SvelteKit — Menos Código, Mismo Poder

> 6 preguntas esenciales + guía de respuestas las que ya sabes del curso

## 🔥 Fundamentales (del contenido del curso)

1. **¿Cuál es la gran diferencia técnica de Svelte?**
   - Es un compilador: no hay runtime de framework en el navegador, genera JS vanilla quirúrgico  _(Menos código enviado + actualizaciones DOM precisas = apps veloces y bundles chicos.)_

2. **¿Qué hace la etiqueta $: en el script?**
   - Declaración reactiva: re-ejecuta la línea automáticamente cuando cambian las variables que usa  _($: doble = cuenta * 2 → doble siempre fresco sin lógica manual. Elegancia mínima.)_

3. **¿Qué hace bind:value={nombre} en un input?**
   - Binding doble vía: escribir actualiza la variable y cambiar la variable actualiza el input  _(El formulario controlado más corto que existe: una directiva y sincronía total.)_

4. **¿Qué es $tema con $ delante de un store?**
   - Autosuscripción de Svelte: lees el valor del store directo y se desuscribe solo al destruir  _(Los stores + $ = estado compartido sin boilerplate: context/redux incluido en el lenguaje.)_

5. **¿Qué hace una función load en +page.server.js?**
   - Corre en el SERVIDOR antes de renderizar y pasa datos a la página (SSR + SEO + sin flicker)  _(Datos en el server, HTML listo al llegar: la app rápida y el SEO contento.)_

6. **¿Qué es progressive enhancement con form actions?**
   - El formulario funciona sin JavaScript (POST clásico del servidor, JS solo lo acelera cuando existe)  _(Robustez por diseño: tu app no se rompe si falla/red no carga el bundle JS.)_

## 🧗 Profundización (prepáralas explicando en voz alta)
- ¿Qué problema real resuelve Svelte y SvelteKit y cuándo NO lo usarías?
- Explica el concepto más fuerte del curso sin usar jerga.
- Contrasta Svelte y SvelteKit con una alternativa: pros/contras.
- Cuenta un error típico de novato en este tema y cómo lo evitas.

## ⭐ Método para contestarlas
1. **Responde en 60 segundos** cada una de las fundamentales, de memoria. Las que tartamudean → repásalas (flashcards/).
2. Graba tu voz en 2 y escúchate: claridad y precisión importan tanto como el contenido técnico.
3. Una respuesta buena = definición (1 línea) + ejemplo (1) + por qué importa (1).
