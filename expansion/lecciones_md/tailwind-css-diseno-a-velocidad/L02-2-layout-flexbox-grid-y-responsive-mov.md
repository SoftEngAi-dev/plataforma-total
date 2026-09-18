# 2. Layout: flexbox, grid y responsive móvil primero

> 📚 Curso: **🎨 Tailwind CSS — Diseño a Velocidad** · Lección 2 de 5
> 🗓 Exportado: 18/09/2026 desde Plataforma Total
> 🍅 Sugerencia: 1-2 pomodoros para leer + practicar

---

## 📖 Contenido

```css

Maquetar con Tailwind es aplicar flexbox/grid por utilidades:
    <nav class="flex items-center justify-between gap-4 px-6 py-3">
    <section class="grid grid-cols-3 gap-6">
    <main class="container mx-auto px-4">

flex items-center justify-between  → barra con logo a un lado y menú al otro
grid grid-cols-3 gap-6             → tarjetas en 3 columnas
container mx-auto px-4             → contenido centrado y acolchado

RESPONSIVE móvil primero (los prefijos significan "desde esta medida
HACIA ARRIBA"):
    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4">
  · sin prefijo → estilo base para móvil
  · md: → a partir de 768px   · lg: → a partir de 1024px

Visibilidad: hidden md:block (oculto en móvil, visible en escritorio)
para menús hamburguesa. Diseña primero la pantalla pequeña y escala.
```

---

## 📝 Quiz de la lección

### 1. ¿Qué significa la clase md:grid-cols-3?
- A) 3 columnas a partir del breakpoint md (768px) hacia arriba
- B) 3 columnas solo en móvil
- C) 3 filas
- D) Un margen de 3 píxeles
### 2. ¿Cómo centras horizontalmente un contenedor con ancho máximo?
- A) con la clase mx-auto (más max-w-* o container)
- B) con text-center
- C) con float:center
- D) con grid

---

## 🔑 Respuestas y explicaciones

**1.** ✅ 3 columnas a partir del breakpoint md (768px) hacia arriba — Tailwind es mobile-first: el base es móvil y los prefijos md:/lg: aplican hacia arriba.
**2.** ✅ con la clase mx-auto (más max-w-* o container) — mx-auto reparte el margen lateral; text-center solo alinea texto en línea.

---
✅ Al terminar, marca la lección como completada en la app (📚 Aprender → ✅ Completada)
