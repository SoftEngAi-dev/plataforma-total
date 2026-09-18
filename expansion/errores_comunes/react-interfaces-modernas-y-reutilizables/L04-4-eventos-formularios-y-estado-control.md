# ⚠️ Errores comunes — 4. Eventos, formularios y estado controlado

> React — Interfaces Modernas y Reutilizables · Lección 4 · Aprender de los errores (propios y ajenos)

- ❌ «readonly» → Frente a «¿Qué significa input 'controlado'?» lo fácil es confundirse. **Verdad**: Su value viene del estado y onChange lo actualiza: el estado es la fuente de verdad. Estado ↔ input en bucle controlado. React manda; el DOM obedece.
- ❌ «Que valida solo» → Frente a «¿Qué significa input 'controlado'?» lo fácil es confundirse. **Verdad**: Su value viene del estado y onChange lo actualiza: el estado es la fuente de verdad. Estado ↔ input en bucle controlado. React manda; el DOM obedece.
- ❌ «Accede al estado del padre directamente» → Frente a «¿Cómo sabe el hijo que debe agregar una tarea si el estado está arriba?» lo fácil es confundirse. **Verdad**: Llama a una función que el padre le pasó por props (onAgregar). Datos bajan por props; cambios suben ejecutando callbacks que bajaron por props.
- ❌ «Modifica el DOM del padre» → Frente a «¿Cómo sabe el hijo que debe agregar una tarea si el estado está arriba?» lo fácil es confundirse. **Verdad**: Llama a una función que el padre le pasó por props (onAgregar). Datos bajan por props; cambios suben ejecutando callbacks que bajaron por props.

## 🩹 Antídoto universal
1. Lee el mensaje de error COMPLETO antes de googlear.
2. Pon el error exacto a la IA local y pide explicación, no solución.
3. Documenta el error en tu bitácora: error → causa → fix.
