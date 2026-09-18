# 3. CSS: selectores, cascada y el modelo de caja

> 📚 Curso: **HTML y CSS — Diseño Web Total** · Lección 3 de 10
> 🗓 Exportado: 18/09/2026 desde Plataforma Total
> 🍅 Sugerencia: 1-2 pomodoros para leer + practicar

---

## 📖 Contenido

```html
CSS: CÓMO SE DECIDE QUÉ GANA
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  selector { propiedad: valor; }
  p { color: navy; }            /* todas las <p> */
  .nota { font-size: 20px; }    /* class= (reutilizable) */
  #principal { width: 90%; }    /* id= (único en la página) */
  div p { ... }                 /* p DENTRO de div */
  a:hover { color: red; }       /* estado */

LA CASCADA (quién gana si hay choque)
1. Especificidad: inline > #id > .clase > etiqueta
2. A igual especificidad: gana la última escrita

EL MODELO DE CAJA (¡ESTO ES CSS!)
Todo elemento es una caja:
  contenido → padding (aire INTERNO) → border → margin (aire EXTERNO)
  box-sizing: border-box;   ← ponlo SIEMPRE: width incluye padding y border

  * { box-sizing: border-box; }

PRUEBA: background-color es la linterna del layout — pinta las cajas para ver qué pasa.
```

---

## 📝 Quiz de la lección

### 1. ¿Qué selector tiene más especificidad?
- A) etiqueta (p)
- B) clase (.nota)
- C) id (#principal)
- D) universal (*)
### 2. ¿Qué hace box-sizing: border-box?
- A) Elimina los bordes
- B) width/height incluyen padding y border (lo intuitivo)
- C) Añade sombras
- D) Redondea esquinas

---

## 🔑 Respuestas y explicaciones

**1.** ✅ id (#principal) — id gana sobre clase y etiqueta. Inline style gana sobre todos.
**2.** ✅ width/height incluyen padding y border (lo intuitivo) — Sin él, width:100px + padding te da una caja de más de 100px; con él, es exacto.

---
✅ Al terminar, marca la lección como completada en la app (📚 Aprender → ✅ Completada)
