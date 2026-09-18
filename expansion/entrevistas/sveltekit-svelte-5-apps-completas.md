# 🎤 Banco de entrevista — 🔥 SvelteKit & Svelte 5 — Apps Completas

> 8 preguntas esenciales + guía de respuestas las que ya sabes del curso

## 🔥 Fundamentales (del contenido del curso)

1. **¿Cómo se declara estado reactivo en Svelte 5?**
   - Con la runa $state()  _($state(0) crea una variable reactiva; $derived deriva valores y $effect ejecuta efectos.)_

2. **¿Qué NO utiliza Svelte en tiempo de ejecución?**
   - El Virtual DOM  _(Svelte compila a actualizaciones quirúrgicas del DOM real: sin VDOM, menos memoria y más velocidad.)_

3. **¿Qué archivo dentro de src/routes/blog crea la ruta /blog?**
   - +page.svelte  _(La convención de SvelteKit: +page.svelte marca la página; los directorios definen el path.)_

4. **¿Cuándo se ejecuta la función load universal de +page.js?**
   - En la primera carga en el servidor y después en el cliente al navegar  _(Es universal: SSR primero, y hidratación cliente en las navegaciones siguientes (con fetch especial).)_

5. **¿Funciona un <form> de SvelteKit sin JavaScript?**
   - Sí: enhancement progresivo, funciona como formulario clásico  _(Ese es su punto fuerte: con JS es SPA; sin JS sigue funcionando vía POST estándar.)_

6. **¿Cómo devuelves un error de validación al formulario desde una action?**
   - Con fail(422, { error })  _(fail devuelve al navegador el estado y un objeto que la página lee en la prop form.)_

7. **¿Cómo creas un endpoint JSON en SvelteKit?**
   - Con un archivo +server.js que exporta funciones GET/POST  _(+server.js en una ruta define handlers HTTP que devuelven json() personalizados.)_

8. **¿Qué adapter eliges para desplegar SvelteKit en tu propio contenedor Docker?**
   - adapter-node  _(adapter-node genera un servidor Node independiente, perfecto para VPS o Docker.)_

## 🧗 Profundización (prepáralas explicando en voz alta)
- ¿Qué problema real resuelve 🔥 SvelteKit & Svelte 5 y cuándo NO lo usarías?
- Explica el concepto más fuerte del curso sin usar jerga.
- Contrasta 🔥 SvelteKit & Svelte 5 con una alternativa: pros/contras.
- Cuenta un error típico de novato en este tema y cómo lo evitas.

## ⭐ Método para contestarlas
1. **Responde en 60 segundos** cada una de las fundamentales, de memoria. Las que tartamudean → repásalas (flashcards/).
2. Graba tu voz en 2 y escúchate: claridad y precisión importan tanto como el contenido técnico.
3. Una respuesta buena = definición (1 línea) + ejemplo (1) + por qué importa (1).
