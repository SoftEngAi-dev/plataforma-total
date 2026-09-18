# ⚠️ Errores comunes — 2. Reactividad total: stores, bindings y formularios

> Svelte y SvelteKit — Menos Código, Mismo Poder · Lección 2 · Aprender de los errores (propios y ajenos)

- ❌ «Nada» → Frente a «¿Qué hace bind:value={nombre} en un input?» lo fácil es confundirse. **Verdad**: Binding doble vía: escribir actualiza la variable y cambiar la variable actualiza el input. El formulario controlado más corto que existe: una directiva y sincronía total.
- ❌ «Submit» → Frente a «¿Qué hace bind:value={nombre} en un input?» lo fácil es confundirse. **Verdad**: Binding doble vía: escribir actualiza la variable y cambiar la variable actualiza el input. El formulario controlado más corto que existe: una directiva y sincronía total.
- ❌ «JQuery» → Frente a «¿Qué es $tema con $ delante de un store?» lo fácil es confundirse. **Verdad**: Autosuscripción de Svelte: lees el valor del store directo y se desuscribe solo al destruir. Los stores + $ = estado compartido sin boilerplate: context/redux incluido en el lenguaje.
- ❌ «Un bug» → Frente a «¿Qué es $tema con $ delante de un store?» lo fácil es confundirse. **Verdad**: Autosuscripción de Svelte: lees el valor del store directo y se desuscribe solo al destruir. Los stores + $ = estado compartido sin boilerplate: context/redux incluido en el lenguaje.

## 🩹 Antídoto universal
1. Lee el mensaje de error COMPLETO antes de googlear.
2. Pon el error exacto a la IA local y pide explicación, no solución.
3. Documenta el error en tu bitácora: error → causa → fix.
