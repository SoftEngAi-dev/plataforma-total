# 3. Componentes: props, emits y slots

> 📚 Curso: **💚 Vue 3 — Composition API en Serio** · Lección 3 de 5
> 🗓 Exportado: 18/09/2026 desde Plataforma Total
> 🍅 Sugerencia: 1-2 pomodoros para leer + practicar

---

## 📖 Contenido

```text

JS baja por props, eventos suben por emits:
    <!-- Hijo.vue -->
    <script setup>
    const props = defineProps({ titulo: String, activa: Boolean });
    const emit = defineEmits(["guardar"]);
    </script>
    <template>
      <button @click="emit('guardar', { id: 1 })">💾 {{ titulo }}</button>
    </template>

    <!-- Padre.vue -->
    <Hijo titulo="Guardar borrador" @guardar="onGuardar" />

Las PROPS son de solo lectura en el hijo (flujo de datos predecible).
SLOTS para contenido flexible:
    <slot name="header" />  +  <template #header>…</template>

CICLO DE VIDA: onMounted(() => cargarDatos()) para iniciar fetch o
temporizadores (y onUnmounted para limpiar). Para datos que deben llegar
muy abajo sin prop drilling: provide("tema", tema) en el ancestro y
const tema = inject("tema") en cualquier descendiente.
```

---

## 📝 Quiz de la lección

### 1. ¿Cómo comunica un componente hijo a su padre en Vue?
- A) Emitiendo un evento personalizado con emit()
- B) Mutando la prop directamente
- C) Escribiendo en localStorage
- D) Con variables globales
### 2. ¿Para qué sirve provide/inject?
- A) Pasar datos a descendientes lejanos sin retransmitir props intermedias
- B) Hacer peticiones HTTP
- C) Definir rutas
- D) Ejecutar tests

---

## 🔑 Respuestas y explicaciones

**1.** ✅ Emitiendo un evento personalizado con emit() — Las props bajan, los eventos suben: el hijo emite, el padre decide qué hacer.
**2.** ✅ Pasar datos a descendientes lejanos sin retransmitir props intermedias — provide publica un valor en el árbol; inject lo consume a cualquier profundidad.

---
✅ Al terminar, marca la lección como completada en la app (📚 Aprender → ✅ Completada)
