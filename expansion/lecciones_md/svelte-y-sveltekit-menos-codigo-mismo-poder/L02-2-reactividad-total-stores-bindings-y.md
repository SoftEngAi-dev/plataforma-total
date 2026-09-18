# 2. Reactividad total: stores, bindings y formularios

> 📚 Curso: **Svelte y SvelteKit — Menos Código, Mismo Poder** · Lección 2 de 3
> 🗓 Exportado: 18/09/2026 desde Plataforma Total
> 🍅 Sugerencia: 1-2 pomodoros para leer + practicar

---

## 📖 Contenido

```svelte
EL MODELO REACTIVO COMPLETO DE SVELTE
━━━━━━━━━━━━━━━━━━━━━━━━━━━
BINDINGS DOBLE VÍA (sin el rito de React)
  <input bind:value={nombre}>          <!-- escribes → variable cambia; y viceversa -->
  <input type="checkbox" bind:checked={acepta}>
  <select bind:value={color}>...</select>

  <script>
      let nombre = "";
      $: mayus = nombre.toUpperCase();  // derivado automático
  </script>
  <p>{nombre} → {mayus}</p>

STORES: estado compartido fuera del componente (equivalente a context/redux liviano)
  // stores.js
  import { writable } from "svelte/store";
  export const tema = writable("claro");
  // componente.svelte
  import { tema } from "./stores.js";
  $tema;                        // $prefijo = autosuscripción (¡magia!)
  tema.set("oscuro");  tema.update(t => t === "claro" ? "oscuro" : "claro");

BLOQUES NATIVOS (sintaxis de plantilla limpia)
  {#if cargando}<Spinner/>{:else if datos}<Lista {datos}/>{:else}<p>vacío</p>{/if}
  {#each tareas as t (t.id)}<li>{t.titulo}</li>{/each}
  {#await promesa then valor}<p>{valor}</p>{/await}
```

---

## 📝 Quiz de la lección

### 1. ¿Qué hace bind:value={nombre} en un input?
- A) Nada
- B) Binding doble vía: escribir actualiza la variable y cambiar la variable actualiza el input
- C) Submit
- D) CSS
### 2. ¿Qué es $tema con $ delante de un store?
- A) JQuery
- B) Autosuscripción de Svelte: lees el valor del store directo y se desuscribe solo al destruir
- C) Un bug
- D) Un import

---

## 🔑 Respuestas y explicaciones

**1.** ✅ Binding doble vía: escribir actualiza la variable y cambiar la variable actualiza el input — El formulario controlado más corto que existe: una directiva y sincronía total.
**2.** ✅ Autosuscripción de Svelte: lees el valor del store directo y se desuscribe solo al destruir — Los stores + $ = estado compartido sin boilerplate: context/redux incluido en el lenguaje.

---
✅ Al terminar, marca la lección como completada en la app (📚 Aprender → ✅ Completada)
