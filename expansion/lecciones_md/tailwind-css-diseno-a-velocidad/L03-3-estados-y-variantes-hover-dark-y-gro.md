# 3. Estados y variantes: hover, dark: y group

> 📚 Curso: **🎨 Tailwind CSS — Diseño a Velocidad** · Lección 3 de 5
> 🗓 Exportado: 18/09/2026 desde Plataforma Total
> 🍅 Sugerencia: 1-2 pomodoros para leer + practicar

---

## 📖 Contenido

```css

Los pseudo-estados CSS son prefijos:
    <button class="bg-indigo-600 hover:bg-indigo-500 active:scale-95
                   focus:ring-2 ring-indigo-300 transition">
    <input class="border focus:border-indigo-500 focus:outline-none" />

Soporte oscuro con dark: (modo clase, recomendado):
    <html class="dark">  →  <body class="bg-white dark:bg-slate-900
                                         text-slate-900 dark:text-slate-100">

GRUPOS: el hijo reacciona al estado del padre:
    <a class="group p-4 hover:bg-slate-100">
      <span class="group-hover:text-indigo-600">Ver más →</span>
    </a>

Listas y posiciones: odd:bg-slate-50 even:bg-white (tablas cebra),
first:rounded-t-xl last:rounded-b-xl.

Y anima cambios con transition, duration-300, ease-out: dale vida sin
escribir keyframes (aunque también existen: animate-pulse, animate-spin).
```

---

## 📝 Quiz de la lección

### 1. ¿Cómo haces que un hijo cambie cuando el padre recibe hover?
- A) Con group en el padre y group-hover: en el hijo
- B) Con JavaScript obligatorio
- C) Con media queries
- D) No se puede con CSS
### 2. ¿Qué hace la clase transition en un botón?
- A) Anima suavemente los cambios de propiedades (color, escala…) entre estados
- B) Oculta el botón
- C) Cambia el tipo de letra
- D) Añade un borde

---

## 🔑 Respuestas y explicaciones

**1.** ✅ Con group en el padre y group-hover: en el hijo — group marca el contenedor; group-hover:aplica-estilo solo cuando el grupo está en hover.
**2.** ✅ Anima suavemente los cambios de propiedades (color, escala…) entre estados — transition + duration-* suaviza hover/active/focus sin escribir @keyframes.

---
✅ Al terminar, marca la lección como completada en la app (📚 Aprender → ✅ Completada)
