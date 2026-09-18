# ⚠️ Errores comunes — 2. Estado con useState: que la UI reaccione

> React — Interfaces Modernas y Reutilizables · Lección 2 · Aprender de los errores (propios y ajenos)

- ❌ «push está prohibido» → Frente a «¿Por qué setTareas([...tareas, nueva]) y no tareas.push(nueva)?» lo fácil es confundirse. **Verdad**: React detecta cambios por REFERENCIA: hay que pasarle un array NUEVO o no re-renderiza. Inmutabilidad: nueva referencia = señal de re-render. push muta en silencio.
- ❌ «Es más corto» → Frente a «¿Por qué setTareas([...tareas, nueva]) y no tareas.push(nueva)?» lo fácil es confundirse. **Verdad**: React detecta cambios por REFERENCIA: hay que pasarle un array NUEVO o no re-renderiza. Inmutabilidad: nueva referencia = señal de re-render. push muta en silencio.
- ❌ «setCuenta(cuenta + 1)» → Frente a «¿Qué forma de actualización de estado es segura con valores previos?» lo fácil es confundirse. **Verdad**: setCuenta(c => c + 1). La forma funcional garantiza trabajar sobre el estado más reciente (clicks encolados).
- ❌ «cuenta++» → Frente a «¿Qué forma de actualización de estado es segura con valores previos?» lo fácil es confundirse. **Verdad**: setCuenta(c => c + 1). La forma funcional garantiza trabajar sobre el estado más reciente (clicks encolados).

## 🩹 Antídoto universal
1. Lee el mensaje de error COMPLETO antes de googlear.
2. Pon el error exacto a la IA local y pide explicación, no solución.
3. Documenta el error en tu bitácora: error → causa → fix.
