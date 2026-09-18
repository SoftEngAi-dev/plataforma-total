# ⚠️ Errores comunes — 3. Form actions: el regreso glorioso del <form>

> 🔥 SvelteKit & Svelte 5 — Apps Completas · Lección 3 · Aprender de los errores (propios y ajenos)

- ❌ «No, siempre requiere JS» → Frente a «¿Funciona un <form> de SvelteKit sin JavaScript?» lo fácil es confundirse. **Verdad**: Sí: enhancement progresivo, funciona como formulario clásico. Ese es su punto fuerte: con JS es SPA; sin JS sigue funcionando vía POST estándar.
- ❌ «Solo en Chrome» → Frente a «¿Funciona un <form> de SvelteKit sin JavaScript?» lo fácil es confundirse. **Verdad**: Sí: enhancement progresivo, funciona como formulario clásico. Ese es su punto fuerte: con JS es SPA; sin JS sigue funcionando vía POST estándar.
- ❌ «Con alert()» → Frente a «¿Cómo devuelves un error de validación al formulario desde una action?» lo fácil es confundirse. **Verdad**: Con fail(422, { error }). fail devuelve al navegador el estado y un objeto que la página lee en la prop form.
- ❌ «Con console.log» → Frente a «¿Cómo devuelves un error de validación al formulario desde una action?» lo fácil es confundirse. **Verdad**: Con fail(422, { error }). fail devuelve al navegador el estado y un objeto que la página lee en la prop form.

## 🩹 Antídoto universal
1. Lee el mensaje de error COMPLETO antes de googlear.
2. Pon el error exacto a la IA local y pide explicación, no solución.
3. Documenta el error en tu bitácora: error → causa → fix.
