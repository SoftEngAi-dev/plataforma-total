# 7. Variables CSS y tipografía: sistemas de diseño mínimos

> 📚 Curso: **HTML y CSS — Diseño Web Total** · Lección 7 de 10
> 🗓 Exportado: 18/09/2026 desde Plataforma Total
> 🍅 Sugerencia: 1-2 pomodoros para leer + practicar

---

## 📖 Contenido

```html
DISEÑA CON SISTEMA, NO CON ADIVINANZAS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
VARIABLES CSS (custom properties)
  :root {
    --color-principal: #6f42c1;
    --espacio: 8px;
    --radio: 12px;
  }
  .boton { background: var(--color-principal); border-radius: var(--radio); }
Cambiar un valor en :root → rebranding completo en 1 línea.

ESCALA TIPOGRÁFICA (consistencia visual)
  --texto-sm: 0.875rem; --texto-base: 1rem; --texto-lg: 1.25rem; --texto-xl: 1.75rem;
Fundamentos: máximo 2-3 tamaños por página al empezar.

FONT
  font-family: system-ui, sans-serif;   ← fuente nativa del SO: carga 0 ms
  line-height: 1.6;                      ← lectura cómoda
  max-width: 65ch en párrafos;           ← líneas legibles

REGLA DEL DISEÑADOR NO-DISEÑADOR: elige UNA paleta (60-30-10: fondo/dominante/acento) y no improvises colores. El 80% del diseño bonito es consistencia.
```

---

## 📝 Quiz de la lección

### 1. ¿Qué ventaja da definir colores como variables en :root?
- A) Cargan más rápido
- B) Cambias una línea y actualizas toda la web (sistema de diseño)
- C) Es la única forma válida
- D) Ahorra memoria del navegador
### 2. ¿Cuál es el largo de línea recomendado para texto legible?
- A) Sin límite
- B) ~45-75 caracteres (65ch) por línea
- C) Exactamente 200px
- D) El ancho de la pantalla

---

## 🔑 Respuestas y explicaciones

**1.** ✅ Cambias una línea y actualizas toda la web (sistema de diseño) — Las variables convierten estilos sueltos en un sistema coherente y mantenible.
**2.** ✅ ~45-75 caracteres (65ch) por línea — Líneas demasiado largas cansan la vista: limita el ancho del texto.

---
✅ Al terminar, marca la lección como completada en la app (📚 Aprender → ✅ Completada)
