# 🥊 Reto del día 290

> Hoy tu cerebro ataca: **2. Estado con useState: que la UI reaccione** (React — Interfaces Modernas y Reutilizables)

1. Explica en voz alta este tema durante 2 minutos, sin notas.
2. Relee la lección solo si el paso 1 trabó.
3. Reescribe desde cero el ejemplo clave de la lección.

## 🥊 Desafío exprés (sin mirar)
**¿Por qué setTareas([...tareas, nueva]) y no tareas.push(nueva)?**

<details><summary>👁 Ver respuesta</summary>

✅ React detecta cambios por REFERENCIA: hay que pasarle un array NUEVO o no re-renderiza — Inmutabilidad: nueva referencia = señal de re-render. push muta en silencio.
</details>

💰 Vale 1 punto de maestría. Acumula 30 → date un premio real.
