# ⚠️ Errores comunes — 9. Arrays: la colección reina

> JavaScript — De Cero a Experto · Lección 9 · Aprender de los errores (propios y ajenos)

- ❌ «shift/unshift» → Frente a «¿Qué métodos agregan/quitan AL FINAL de un array?» lo fácil es confundirse. **Verdad**: push/pop. push y pop operan en el extremo final; shift/unshift al inicio.
- ❌ «slice/splice» → Frente a «¿Qué métodos agregan/quitan AL FINAL de un array?» lo fácil es confundirse. **Verdad**: push/pop. push y pop operan en el extremo final; shift/unshift al inicio.
- ❌ «Copia total» → Frente a «const b = a (arrays) — ¿qué relación tienen?» lo fácil es confundirse. **Verdad**: Apuntan AL MISMO array: mutar uno muta el otro. Los arrays son referencias. Copia real: [...a] o a.slice().
- ❌ «b es de solo lectura» → Frente a «const b = a (arrays) — ¿qué relación tienen?» lo fácil es confundirse. **Verdad**: Apuntan AL MISMO array: mutar uno muta el otro. Los arrays son referencias. Copia real: [...a] o a.slice().

## 🩹 Antídoto universal
1. Lee el mensaje de error COMPLETO antes de googlear.
2. Pon el error exacto a la IA local y pide explicación, no solución.
3. Documenta el error en tu bitácora: error → causa → fix.
