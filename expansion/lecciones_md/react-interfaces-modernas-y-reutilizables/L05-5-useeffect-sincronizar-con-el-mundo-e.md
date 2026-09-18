# 5. useEffect: sincronizar con el mundo exterior

> 📚 Curso: **React — Interfaces Modernas y Reutilizables** · Lección 5 de 8
> 🗓 Exportado: 18/09/2026 desde Plataforma Total
> 🍅 Sugerencia: 1-2 pomodoros para leer + practicar

---

## 📖 Contenido

```jsx
EFECTOS: DESPUÉS DEL RENDER
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
useEffect corre código DESPUÉS de que React pinta: fetch, timers, suscripciones, localStorage.

  useEffect(() => {
    // efecto
    return () => { /* limpieza opcional (cancela fetch, limpia timer) */ };
  }, [dependencias]);

EL ARRAY LO CAMBIA TODO
  useEffect(fn)           → tras CADA render (casi nunca lo quieres)
  useEffect(fn, [])       → UNA vez al montar (fetch inicial límpio)
  useEffect(fn, [id])     → cada vez que CAMBIA id

EJEMPLO REAL (con guardia para doble montaje en StrictMode):
  useEffect(() => {
    let cancelado = false;
    fetch(`/api/tareas/${id}`).then(r => r.json()).then(d => {
      if (!cancelado) setTarea(d);
    });
    return () => { cancelado = true; };
  }, [id]);

REGLAS: no sincronices React consigo mismo con effects (calcula en render); efectos = ir AFUERA (API, temporalización, DOM externo).
```

---

## 📝 Quiz de la lección

### 1. ¿Cuándo se ejecuta useEffect(fn, [])?
- A) Cada render
- B) Una vez al montar el componente
- C) Al desmontar
- D) Nunca
### 2. ¿Para qué sirve la función de limpieza del efecto?
- A) Borrar el estado
- B) Cancelar trabajo pendiente (fetch, timers, subscripciones) antes de re-ejecutar o desmontar
- C) Limpiar el JSX
- D) Es teórica

---

## 🔑 Respuestas y explicaciones

**1.** ✅ Una vez al montar el componente — Array vacío = sin dependencias: solo el montaje. La limpieza corre al desmontar.
**2.** ✅ Cancelar trabajo pendiente (fetch, timers, subscripciones) antes de re-ejecutar o desmontar — Evita race conditions y fugas: la respuesta tardía de un fetch viejo no pisa la nueva.

---
✅ Al terminar, marca la lección como completada en la app (📚 Aprender → ✅ Completada)
