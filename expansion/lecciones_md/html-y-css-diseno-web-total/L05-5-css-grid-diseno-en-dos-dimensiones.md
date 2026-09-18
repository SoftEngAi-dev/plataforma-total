# 5. CSS Grid: diseño en dos dimensiones

> 📚 Curso: **HTML y CSS — Diseño Web Total** · Lección 5 de 10
> 🗓 Exportado: 18/09/2026 desde Plataforma Total
> 🍅 Sugerencia: 1-2 pomodoros para leer + practicar

---

## 📖 Contenido

```html
GRID: EL LAYOUT PROFESIONAL
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Cuando hay filas Y columnas (galerías, dashboards, páginas enteras): Grid.

  .galeria {
    display: grid;
    grid-template-columns: repeat(3, 1fr);   /* 3 columnas iguales */
    gap: 15px;
  }

  /* El clásico responsive sin media queries: */
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));

LAYOUT DE PÁGINA COMPLETA
  .app { display: grid; grid-template-areas:
    "header header"
    "sidebar main"
    "footer footer"; }
  header  { grid-area: header; }

FLEX vs GRID (regla de bolsillo)
• Una fila/columna de cosas → Flexbox (navbar, botones, centrado)
• Retícula de ambas dimensiones → Grid (galerías, páginas)
Conviven: Grid para la página, Flex dentro de cada card.
```

---

## 📝 Quiz de la lección

### 1. ¿Qué hace repeat(auto-fit, minmax(250px, 1fr))?
- A) 3 columnas fijas
- B) Columnas dinámicas: entran las quepan con mínimo 250px y rellenan el espacio
- C) 250px de alto
- D) Nada sin media queries
### 2. ¿Cuándo elegir Grid sobre Flexbox?
- A) Siempre
- B) Nunca
- C) Cuando el diseño es bidimensional (filas y columnas)
- D) Solo para tablas

---

## 🔑 Respuestas y explicaciones

**1.** ✅ Columnas dinámicas: entran las quepan con mínimo 250px y rellenan el espacio — El patrón responsive por excelencia: se adapta solo al ancho disponible.
**2.** ✅ Cuando el diseño es bidimensional (filas y columnas) — Flex = una dimensión; Grid = dos. Conviven felices.

---
✅ Al terminar, marca la lección como completada en la app (📚 Aprender → ✅ Completada)
