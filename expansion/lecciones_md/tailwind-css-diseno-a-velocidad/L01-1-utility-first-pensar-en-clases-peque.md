# 1. Utility-first: pensar en clases pequeñas

> 📚 Curso: **🎨 Tailwind CSS — Diseño a Velocidad** · Lección 1 de 5
> 🗓 Exportado: 18/09/2026 desde Plataforma Total
> 🍅 Sugerencia: 1-2 pomodoros para leer + practicar

---

## 📖 Contenido

```css

Tailwind rompe con el CSS tradicional: en vez de inventar clases
(.boton-primario con 8 propiedades), COMPONES con utilidades de un solo
propósito directamente en el HTML:
    <button class="px-4 py-2 rounded-lg bg-indigo-600 text-white
                   font-semibold hover:bg-indigo-500 transition">
      Guardar
    </button>

Ventajas reales: no hay nombres que inventar ni CSS muerto que nadie
borra, la escala de espaciados/colores fuerza consistencia de diseño, y
prototipas pantallas completas sin salir del HTML.

Instalación moderna (v4) con Vite: importas "tailwindcss" y en tu CSS:
@import "tailwindcss"; — el motor genera SOLO las clases que usas.
Para jugar sin instalar nada: <script src="https://cdn.tailwindcss.com">.

Vocabulario esencial: p-4 m-2 (padding/margin), w-full max-w-md,
text-lg font-bold text-slate-600, bg-white, rounded-xl shadow-lg,
border border-slate-200, flex (¡la siguiente lección profundiza!).
```

---

## 📝 Quiz de la lección

### 1. ¿Qué es el enfoque utility-first de Tailwind?
- A) Componer el diseño con muchas clases de un solo propósito en el HTML
- B) Escribir todo el CSS a mano con !important
- C) Usar solo CSS-in-JS
- D) Poner estilos inline en cada etiqueta
### 2. ¿Por qué el CSS final en producción con Tailwind es pequeño?
- A) Porque solo se generan las clases que realmente usas
- B) Porque se borra todo el CSS
- C) Porque se usa el CDN
- D) Porque Tailwind no genera CSS

---

## 🔑 Respuestas y explicaciones

**1.** ✅ Componer el diseño con muchas clases de un solo propósito en el HTML — Muchas utilidades pequeñas y predecibles que se combinan: el diseño vive junto al marcado.
**2.** ✅ Porque solo se generan las clases que realmente usas — El compilador detecta las clases presentes en tus archivos y emite únicamente esas reglas.

---
✅ Al terminar, marca la lección como completada en la app (📚 Aprender → ✅ Completada)
