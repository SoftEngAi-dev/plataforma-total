# 📕 Resumen maestro — 💚 Vue 3 — Composition API en Serio

> Todo el curso en una hoja: una idea núcleo por lección. Releer semanal.

## 1. 1. El SFC y la reactividad con ref()
 Vue 3 gira alrededor del SINGLE FILE COMPONENT (.vue):     <script setup>     // <script setup> = Composition API sin ceremonia     import { ref } from "vue";     const contador =…

## 2. 2. computed, watch y las directivas esenciales
 VALORES DERIVADOS con computed (con caché: solo se recalcula si cambian sus dependencias):     import { computed } from "vue";     const filtrados = computed(() =>       tareas.va…

## 3. 3. Componentes: props, emits y slots
 JS baja por props, eventos suben por emits:     <!-- Hijo.vue -->     <script setup>     const props = defineProps({ titulo: String, activa: Boolean });     const emit = defineEmi…

## 4. 4. Pinia: el store oficial de Vue
 Cuando el estado cruza muchos componentes → PINIA (sucesor de Vuex):     // stores/tareas.js     import { defineStore } from "pinia";     export const useTareas = defineStore("tar…

## 5. 5. Nuxt 3: Vue full-stack
 Nuxt convierte Vue en un framework full-stack de producción:    pages/               → rutas automáticas (pages/index.vue → /)   server/api/hola.ts   → endpoint Node: export defau…

---
✅ 5 lecciones · 📝 10 preguntas de repaso en quizzes_html/ · tests/