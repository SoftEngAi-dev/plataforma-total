# 4. Pinia: el store oficial de Vue

> 📚 Curso: **💚 Vue 3 — Composition API en Serio** · Lección 4 de 5
> 🗓 Exportado: 18/09/2026 desde Plataforma Total
> 🍅 Sugerencia: 1-2 pomodoros para leer + practicar

---

## 📖 Contenido

```text

Cuando el estado cruza muchos componentes → PINIA (sucesor de Vuex):
    // stores/tareas.js
    import { defineStore } from "pinia";
    export const useTareas = defineStore("tareas", () => {
      const lista = ref([]);                 // state
      const pendientes = computed(() =>      // getters
        lista.value.filter(t => !t.hecha));
      async function cargar() {              // actions
        lista.value = await (await fetch("/api/tareas")).json();
      }
      return { lista, pendientes, cargar };
    });

En cualquier componente:
    const tareas = useTareas();     // ¡ya está suscrito!
    tareas.cargar();

Estilo setup (como arriba) o estilo options (state/getters/actions).
Ventajas: estado central predecible, Devtools con time-travel, TypeScript
de primera y plugins (p. ej. persistencia en localStorage). Regla: el
estado LOCAL de un formulario no necesita store; el COMPARTIDO sí.
```

---

## 📝 Quiz de la lección

### 1. ¿Cuál es la forma reactiva de compartir estado global en Vue 3 moderno?
- A) Variables globales en window
- B) Un store de Pinia con defineStore
- C) Props encadenadas
- D) Cookies
### 2. En un store de Pinia, ¿qué es un getter?
- A) Un valor derivado del estado con caché (como computed)
- B) Una llamada HTTP
- C) Un middleware
- D) Un hook de montaje

---

## 🔑 Respuestas y explicaciones

**1.** ✅ Un store de Pinia con defineStore — Pinia es el store oficial: central, tipado y con Devtools; window es un hack frágil.
**2.** ✅ Un valor derivado del estado con caché (como computed) — Los getters son computed del store: se recalculan cuando cambia el estado base.

---
✅ Al terminar, marca la lección como completada en la app (📚 Aprender → ✅ Completada)
