# ⚠️ Errores comunes — 5. useEffect: sincronizar con el mundo exterior

> React — Interfaces Modernas y Reutilizables · Lección 5 · Aprender de los errores (propios y ajenos)

- ❌ «Cada render» → Frente a «¿Cuándo se ejecuta useEffect(fn, [])?» lo fácil es confundirse. **Verdad**: Una vez al montar el componente. Array vacío = sin dependencias: solo el montaje. La limpieza corre al desmontar.
- ❌ «Al desmontar» → Frente a «¿Cuándo se ejecuta useEffect(fn, [])?» lo fácil es confundirse. **Verdad**: Una vez al montar el componente. Array vacío = sin dependencias: solo el montaje. La limpieza corre al desmontar.
- ❌ «Borrar el estado» → Frente a «¿Para qué sirve la función de limpieza del efecto?» lo fácil es confundirse. **Verdad**: Cancelar trabajo pendiente (fetch, timers, subscripciones) antes de re-ejecutar o desmontar. Evita race conditions y fugas: la respuesta tardía de un fetch viejo no pisa la nueva.
- ❌ «Limpiar el JSX» → Frente a «¿Para qué sirve la función de limpieza del efecto?» lo fácil es confundirse. **Verdad**: Cancelar trabajo pendiente (fetch, timers, subscripciones) antes de re-ejecutar o desmontar. Evita race conditions y fugas: la respuesta tardía de un fetch viejo no pisa la nueva.

## 🩹 Antídoto universal
1. Lee el mensaje de error COMPLETO antes de googlear.
2. Pon el error exacto a la IA local y pide explicación, no solución.
3. Documenta el error en tu bitácora: error → causa → fix.
