# ⚠️ Errores comunes — 7. Patrones reales: fetch con estados y manejo de errores

> React — Interfaces Modernas y Reutilizables · Lección 7 · Aprender de los errores (propios y ajenos)

- ❌ «vacio, ok, no» → Frente a «¿Qué 3 estados mínimos modelan cualquier fetch en UI?» lo fácil es confundirse. **Verdad**: cargando, error, datos. Con esos tres discriminas exáctamente qué pintar: spinner, mensaje de error o contenido.
- ❌ «init, run, end» → Frente a «¿Qué 3 estados mínimos modelan cualquier fetch en UI?» lo fácil es confundirse. **Verdad**: cargando, error, datos. Con esos tres discriminas exáctamente qué pintar: spinner, mensaje de error o contenido.
- ❌ «Cancela la red» → Frente a «¿Por qué la bandera 'cancelado' en el efecto de fetch?» lo fácil es confundirse. **Verdad**: Evita que una respuesta tardía actualice estado de un componente desmontado (warning + race). En StrictMode y navegación rápida los componentes se montan/desmontan: la guardia lo hace robusto.
- ❌ «Acelera fetch» → Frente a «¿Por qué la bandera 'cancelado' en el efecto de fetch?» lo fácil es confundirse. **Verdad**: Evita que una respuesta tardía actualice estado de un componente desmontado (warning + race). En StrictMode y navegación rápida los componentes se montan/desmontan: la guardia lo hace robusto.

## 🩹 Antídoto universal
1. Lee el mensaje de error COMPLETO antes de googlear.
2. Pon el error exacto a la IA local y pide explicación, no solución.
3. Documenta el error en tu bitácora: error → causa → fix.
