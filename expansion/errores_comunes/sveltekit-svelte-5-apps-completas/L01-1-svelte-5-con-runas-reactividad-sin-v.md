# ⚠️ Errores comunes — 1. Svelte 5 con runas: reactividad sin Virtual DOM

> 🔥 SvelteKit & Svelte 5 — Apps Completas · Lección 1 · Aprender de los errores (propios y ajenos)

- ❌ «Con setState()» → Frente a «¿Cómo se declara estado reactivo en Svelte 5?» lo fácil es confundirse. **Verdad**: Con la runa $state(). $state(0) crea una variable reactiva; $derived deriva valores y $effect ejecuta efectos.
- ❌ «Con data()» → Frente a «¿Cómo se declara estado reactivo en Svelte 5?» lo fácil es confundirse. **Verdad**: Con la runa $state(). $state(0) crea una variable reactiva; $derived deriva valores y $effect ejecuta efectos.
- ❌ «JavaScript» → Frente a «¿Qué NO utiliza Svelte en tiempo de ejecución?» lo fácil es confundirse. **Verdad**: El Virtual DOM. Svelte compila a actualizaciones quirúrgicas del DOM real: sin VDOM, menos memoria y más velocidad.
- ❌ «CSS» → Frente a «¿Qué NO utiliza Svelte en tiempo de ejecución?» lo fácil es confundirse. **Verdad**: El Virtual DOM. Svelte compila a actualizaciones quirúrgicas del DOM real: sin VDOM, menos memoria y más velocidad.

## 🩹 Antídoto universal
1. Lee el mensaje de error COMPLETO antes de googlear.
2. Pon el error exacto a la IA local y pide explicación, no solución.
3. Documenta el error en tu bitácora: error → causa → fix.
