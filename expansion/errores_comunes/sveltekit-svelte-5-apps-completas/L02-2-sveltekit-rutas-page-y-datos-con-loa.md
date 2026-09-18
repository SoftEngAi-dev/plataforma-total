# ⚠️ Errores comunes — 2. SvelteKit: rutas +page y datos con load

> 🔥 SvelteKit & Svelte 5 — Apps Completas · Lección 2 · Aprender de los errores (propios y ajenos)

- ❌ «index.html» → Frente a «¿Qué archivo dentro de src/routes/blog crea la ruta /blog?» lo fácil es confundirse. **Verdad**: +page.svelte. La convención de SvelteKit: +page.svelte marca la página; los directorios definen el path.
- ❌ «routes.js» → Frente a «¿Qué archivo dentro de src/routes/blog crea la ruta /blog?» lo fácil es confundirse. **Verdad**: +page.svelte. La convención de SvelteKit: +page.svelte marca la página; los directorios definen el path.
- ❌ «Solo en build» → Frente a «¿Cuándo se ejecuta la función load universal de +page.js?» lo fácil es confundirse. **Verdad**: En la primera carga en el servidor y después en el cliente al navegar. Es universal: SSR primero, y hidratación cliente en las navegaciones siguientes (con fetch especial).
- ❌ «Nunca en el servidor» → Frente a «¿Cuándo se ejecuta la función load universal de +page.js?» lo fácil es confundirse. **Verdad**: En la primera carga en el servidor y después en el cliente al navegar. Es universal: SSR primero, y hidratación cliente en las navegaciones siguientes (con fetch especial).

## 🩹 Antídoto universal
1. Lee el mensaje de error COMPLETO antes de googlear.
2. Pon el error exacto a la IA local y pide explicación, no solución.
3. Documenta el error en tu bitácora: error → causa → fix.
