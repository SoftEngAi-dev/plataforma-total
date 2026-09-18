# 2. computed, watch y las directivas esenciales

> 📚 Curso: **💚 Vue 3 — Composition API en Serio** · Lección 2 de 5
> 🗓 Exportado: 18/09/2026 desde Plataforma Total
> 🍅 Sugerencia: 1-2 pomodoros para leer + practicar

---

## 📖 Contenido

```text

VALORES DERIVADOS con computed (con caché: solo se recalcula si cambian
sus dependencias):
    import { computed } from "vue";
    const filtrados = computed(() =>
      tareas.value.filter(t => t.texto.includes(busqueda.value)));

EFECTOS con watch / watchEffect para reaccionar a cambios (fetch, logs…):
    watch(busqueda, (nuevo) => console.log("buscando", nuevo));

DIRECTIVAS del template:
  v-if / v-else-if / v-else   → render condicional real
  v-for="t in tareas" :key="t.id" → listas (¡key siempre!)
  v-model="texto"             → enlace bidireccional con inputs
  v-bind:src="url"  (o :src)  → atributos dinámicos
  v-on:click  (o @click)      → eventos; @submit.prevent, .stop

Patrón buscador: input con v-model + v-for sobre computed filtrado =
listas con filtro instantáneo sin librerías.
```

---

## 📝 Quiz de la lección

### 1. ¿Qué hace computed() en Vue 3?
- A) Calcula un valor derivado con caché, recalculando solo si cambian las dependencias
- B) Lanza peticiones HTTP
- C) Define rutas
- D) Compila CSS
### 2. ¿Qué hace v-model en un input?
- A) Enlace bidireccional: el input escribe el estado y el estado actualiza el input
- B) Importa módulos
- C) Crea bucles
- D) Registra eventos globales

---

## 🔑 Respuestas y explicaciones

**1.** ✅ Calcula un valor derivado con caché, recalculando solo si cambian las dependencias — El computed memoriza: si las dependencias no cambian, devuelve el valor cacheado.
**2.** ✅ Enlace bidireccional: el input escribe el estado y el estado actualiza el input — v-model azucara value + @input: la vía rápida para formularios.

---
✅ Al terminar, marca la lección como completada en la app (📚 Aprender → ✅ Completada)
