# ⚠️ Errores comunes — 1. Svelte: el compilador que no envía framework

> Svelte y SvelteKit — Menos Código, Mismo Poder · Lección 1 · Aprender de los errores (propios y ajenos)

- ❌ «Usa Python» → Frente a «¿Cuál es la gran diferencia técnica de Svelte?» lo fácil es confundirse. **Verdad**: Es un compilador: no hay runtime de framework en el navegador, genera JS vanilla quirúrgico. Menos código enviado + actualizaciones DOM precisas = apps veloces y bundles chicos.
- ❌ «Es más lento» → Frente a «¿Cuál es la gran diferencia técnica de Svelte?» lo fácil es confundirse. **Verdad**: Es un compilador: no hay runtime de framework en el navegador, genera JS vanilla quirúrgico. Menos código enviado + actualizaciones DOM precisas = apps veloces y bundles chicos.
- ❌ «JQuery» → Frente a «¿Qué hace la etiqueta $: en el script?» lo fácil es confundirse. **Verdad**: Declaración reactiva: re-ejecuta la línea automáticamente cuando cambian las variables que usa. $: doble = cuenta * 2 → doble siempre fresco sin lógica manual. Elegancia mínima.
- ❌ «Un import» → Frente a «¿Qué hace la etiqueta $: en el script?» lo fácil es confundirse. **Verdad**: Declaración reactiva: re-ejecuta la línea automáticamente cuando cambian las variables que usa. $: doble = cuenta * 2 → doble siempre fresco sin lógica manual. Elegancia mínima.

## 🩹 Antídoto universal
1. Lee el mensaje de error COMPLETO antes de googlear.
2. Pon el error exacto a la IA local y pide explicación, no solución.
3. Documenta el error en tu bitácora: error → causa → fix.
