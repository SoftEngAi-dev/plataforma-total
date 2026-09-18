# 1. El SFC y la reactividad con ref()

> 📚 Curso: **💚 Vue 3 — Composition API en Serio** · Lección 1 de 5
> 🗓 Exportado: 18/09/2026 desde Plataforma Total
> 🍅 Sugerencia: 1-2 pomodoros para leer + practicar

---

## 📖 Contenido

```text

Vue 3 gira alrededor del SINGLE FILE COMPONENT (.vue):
    <script setup>
    // <script setup> = Composition API sin ceremonia
    import { ref } from "vue";
    const contador = ref(0);          // estado reactivo
    import Header from "./Header.vue"; // auto-usable en template
    </script>
    <template>
      <button @click="contador++">Clicks: {{ contador }}</button>
    </template>
    <style scoped>
      button { font-size: 1.2rem; }
    </style>

ref() crea una referencia reactiva: en el <script> se lee/escribe con
.value; en el template se desenvuelve sola. Para objetos grandes, reactive()
evita el .value (pero cuidado al desestructurar). {{ }} interpola texto,
@click escucha eventos (shorthand de v-on).

Proyecto real: npm create vue@latest (Vite incluido). Vue es progresivo:
puedes empezar con una etiqueta script en una página y crecer a SPA.
```

---

## 📝 Quiz de la lección

### 1. ¿Cómo incrementas un ref dentro del <script setup>?
- A) contador++
- B) contador.value++
- C) setContador(contador + 1)
- D) this.contador++
### 2. ¿Qué tres bloques suele tener un Single File Component?
- A) script, template y style
- B) html, css y js
- C) setup, render y mount
- D) props, state y emits

---

## 🔑 Respuestas y explicaciones

**1.** ✅ contador.value++ — En el script los refs se manipulan con .value; en el template Vue lo desenvuelve automáticamente.
**2.** ✅ script, template y style — El SFC agrupa lógica (script), vista (template) y estilos (style) en un solo archivo .vue.

---
✅ Al terminar, marca la lección como completada en la app (📚 Aprender → ✅ Completada)
