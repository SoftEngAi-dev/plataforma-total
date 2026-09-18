# 5. Producción: shadcn/ui, accesibilidad y buenas prácticas

> 📚 Curso: **🎨 Tailwind CSS — Diseño a Velocidad** · Lección 5 de 5
> 🗓 Exportado: 18/09/2026 desde Plataforma Total
> 🍅 Sugerencia: 1-2 pomodoros para leer + practicar

---

## 📖 Contenido

```css

En producción el JIT genera solo lo usado: no hay "purgado" manual que
configurar; evita componer nombres de clase en strings dinámicos
(`bg-${color}-500` NO se detectará → usa objetos/mapas de clases completas).

El ecosistema moderno:
  · shadcn/ui: componentes ACCESIBLES (Radix) + Tailwind que COPIAS a tu
    repo (son tuyos, no una dependencia) → diálogos, menús, tablas…
  · Headless UI: comportamiento sin estilos para Vue/React.

Accesibilidad (no negociable en proyectos excelentes):
  · Contraste suficiente (text-slate-600 sobre blanco ≈ AA).
  · focus-visible:ring-2 para navegación con teclado.
  · sr-only para textos solo para lectores de pantalla.

Orden y legibilidad: agrupa clases por bloques (layout → box → texto →
visual → estados), usa el plugin oficial de Prettier para ordenarlas
automáticamente, y extrae componentes cuando la cadena supera lo cómodo.
```

---

## 📝 Quiz de la lección

### 1. ¿Qué es shadcn/ui?
- A) Componentes accesibles (Radix + Tailwind) que copias a tu proyecto y son tuyos
- B) Un framework de CSS rival
- C) Un plugin de jQuery
- D) Una librería de iconos
### 2. ¿Qué clase de Tailwind muestra un texto solo a lectores de pantalla?
- A) sr-only
- B) hidden
- C) invisible
- D) opacity-0

---

## 🔑 Respuestas y explicaciones

**1.** ✅ Componentes accesibles (Radix + Tailwind) que copias a tu proyecto y son tuyos — No es una dependencia: copia el código del componente a tu repo, con accesibilidad Radix y estilos Tailwind incluidos.
**2.** ✅ sr-only — sr-only lo oculta visualmente pero mantiene accesibilidad para tecnologías asistivas.

---
✅ Al terminar, marca la lección como completada en la app (📚 Aprender → ✅ Completada)
