# 🎤 Banco de entrevista — 🍞 Bun & Deno — Los Nuevos Runtimes

> 8 preguntas esenciales + guía de respuestas las que ya sabes del curso

## 🔥 Fundamentales (del contenido del curso)

1. **¿Qué incluye Bun además del runtime?**
   - Bundler, test runner y gestor de paquetes  _(Bun unifica herramientas: bun install, bun test y el bundler vienen de serie, todo muy rápido.)_

2. **¿Cuál es el principio de seguridad por defecto de Deno?**
   - Permisos explícitos (--allow-net, --allow-read…)  _(Sin --allow-* el código no puede salir de su caja de arena: ideal para scripts de terceros.)_

3. **¿Qué comando ejecuta los tests integrados de Bun?**
   - bun test  _(bun test incluye runner con API estilo Jest (describe/test/expect), sin instalar nada.)_

4. **¿Cómo levanta Bun un servidor HTTP sin Express?**
   - Con Bun.serve({ fetch })  _(Bun.serve es el servidor nativo de alto rendimiento con handlers fetch estándar Web.)_

5. **¿Qué pasa si un script de Deno usa la red sin --allow-net?**
   - Deno lanza PermissionDenied y bloquea la operación  _(El sandbox de Deno exige permisos explícitos por recurso: seguridad real por defecto.)_

6. **¿Qué herramientas trae Deno integradas sin configuración?**
   - fmt, lint y test (además de compile)  _(deno fmt, deno lint, deno test y deno compile vienen de serie: toolchain todo-en-uno.)_

7. **¿Qué framework corre el MISMO código en Deno, Bun, Node y workers del edge?**
   - Hono  _(Hono es ultraligero y multi-runtime: una API escrita una vez despliega en todos los runtimes.)_

8. **¿Qué es Fresh?**
   - El framework de islas para Deno, sin paso de build  _(Fresh aplica arquitectura de islas (como Astro) sobre Deno con Preact: cero build, súper rápido.)_

## 🧗 Profundización (prepáralas explicando en voz alta)
- ¿Qué problema real resuelve 🍞 Bun & Deno y cuándo NO lo usarías?
- Explica el concepto más fuerte del curso sin usar jerga.
- Contrasta 🍞 Bun & Deno con una alternativa: pros/contras.
- Cuenta un error típico de novato en este tema y cómo lo evitas.

## ⭐ Método para contestarlas
1. **Responde en 60 segundos** cada una de las fundamentales, de memoria. Las que tartamudean → repásalas (flashcards/).
2. Graba tu voz en 2 y escúchate: claridad y precisión importan tanto como el contenido técnico.
3. Una respuesta buena = definición (1 línea) + ejemplo (1) + por qué importa (1).
