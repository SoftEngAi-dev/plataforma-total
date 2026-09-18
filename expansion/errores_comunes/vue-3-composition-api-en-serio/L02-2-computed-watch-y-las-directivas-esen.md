# ⚠️ Errores comunes — 2. computed, watch y las directivas esenciales

> 💚 Vue 3 — Composition API en Serio · Lección 2 · Aprender de los errores (propios y ajenos)

- ❌ «Lanza peticiones HTTP» → Frente a «¿Qué hace computed() en Vue 3?» lo fácil es confundirse. **Verdad**: Calcula un valor derivado con caché, recalculando solo si cambian las dependencias. El computed memoriza: si las dependencias no cambian, devuelve el valor cacheado.
- ❌ «Define rutas» → Frente a «¿Qué hace computed() en Vue 3?» lo fácil es confundirse. **Verdad**: Calcula un valor derivado con caché, recalculando solo si cambian las dependencias. El computed memoriza: si las dependencias no cambian, devuelve el valor cacheado.
- ❌ «Importa módulos» → Frente a «¿Qué hace v-model en un input?» lo fácil es confundirse. **Verdad**: Enlace bidireccional: el input escribe el estado y el estado actualiza el input. v-model azucara value + @input: la vía rápida para formularios.
- ❌ «Crea bucles» → Frente a «¿Qué hace v-model en un input?» lo fácil es confundirse. **Verdad**: Enlace bidireccional: el input escribe el estado y el estado actualiza el input. v-model azucara value + @input: la vía rápida para formularios.

## 🩹 Antídoto universal
1. Lee el mensaje de error COMPLETO antes de googlear.
2. Pon el error exacto a la IA local y pide explicación, no solución.
3. Documenta el error en tu bitácora: error → causa → fix.
