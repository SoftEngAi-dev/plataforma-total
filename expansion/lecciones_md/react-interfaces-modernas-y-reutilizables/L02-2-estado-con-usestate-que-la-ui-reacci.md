# 2. Estado con useState: que la UI reaccione

> 📚 Curso: **React — Interfaces Modernas y Reutilizables** · Lección 2 de 8
> 🗓 Exportado: 18/09/2026 desde Plataforma Total
> 🍅 Sugerencia: 1-2 pomodoros para leer + practicar

---

## 📖 Contenido

```jsx
ESTADO: LA MEMORIA DEL COMPONENTE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Los datos LOCALES que cambian con el tiempo viven en estado:
  import { useState } from "react";

  function Contador() {
    const [cuenta, setCuenta] = useState(0);

    return (
      <button onClick={() => setCuenta(cuenta + 1)}>
        Clicks: {cuenta}
      </button>
    );
  }

REGLAS DE ORO
1. NUNCA mutar estado directamente: usa el setter (setCuenta(...))
2. Con estado previo: setCuenta(c => c + 1) (forma funcional, la segura)
3. Estado = inmutable mentalmente: arrays se reemplazan, no se les hace push:
     setTareas([...tareas, nueva])/ setTareas(tareas.filter(t => t.id !== id))

ESTADO vs VARIABLE: reasignar una variable NO re-renderiza. El estado SÍ.

SUBIR ESTADO: si dos componentes lo necesitan, vive en el padre COMÚN y baja por props.
```

---

## 📝 Quiz de la lección

### 1. ¿Por qué setTareas([...tareas, nueva]) y no tareas.push(nueva)?
- A) push está prohibido
- B) React detecta cambios por REFERENCIA: hay que pasarle un array NUEVO o no re-renderiza
- C) Es más corto
- D) Ambas funcionan igual
### 2. ¿Qué forma de actualización de estado es segura con valores previos?
- A) setCuenta(cuenta + 1)
- B) setCuenta(c => c + 1)
- C) cuenta++
- D) las dos primeras igual

---

## 🔑 Respuestas y explicaciones

**1.** ✅ React detecta cambios por REFERENCIA: hay que pasarle un array NUEVO o no re-renderiza — Inmutabilidad: nueva referencia = señal de re-render. push muta en silencio.
**2.** ✅ setCuenta(c => c + 1) — La forma funcional garantiza trabajar sobre el estado más reciente (clicks encolados).

---
✅ Al terminar, marca la lección como completada en la app (📚 Aprender → ✅ Completada)
