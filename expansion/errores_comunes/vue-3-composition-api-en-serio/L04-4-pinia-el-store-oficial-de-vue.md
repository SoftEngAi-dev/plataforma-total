# ⚠️ Errores comunes — 4. Pinia: el store oficial de Vue

> 💚 Vue 3 — Composition API en Serio · Lección 4 · Aprender de los errores (propios y ajenos)

- ❌ «Variables globales en window» → Frente a «¿Cuál es la forma reactiva de compartir estado global en Vue 3 moderno?» lo fácil es confundirse. **Verdad**: Un store de Pinia con defineStore. Pinia es el store oficial: central, tipado y con Devtools; window es un hack frágil.
- ❌ «Props encadenadas» → Frente a «¿Cuál es la forma reactiva de compartir estado global en Vue 3 moderno?» lo fácil es confundirse. **Verdad**: Un store de Pinia con defineStore. Pinia es el store oficial: central, tipado y con Devtools; window es un hack frágil.
- ❌ «Una llamada HTTP» → Frente a «En un store de Pinia, ¿qué es un getter?» lo fácil es confundirse. **Verdad**: Un valor derivado del estado con caché (como computed). Los getters son computed del store: se recalculan cuando cambia el estado base.
- ❌ «Un middleware» → Frente a «En un store de Pinia, ¿qué es un getter?» lo fácil es confundirse. **Verdad**: Un valor derivado del estado con caché (como computed). Los getters son computed del store: se recalculan cuando cambia el estado base.

## 🩹 Antídoto universal
1. Lee el mensaje de error COMPLETO antes de googlear.
2. Pon el error exacto a la IA local y pide explicación, no solución.
3. Documenta el error en tu bitácora: error → causa → fix.
