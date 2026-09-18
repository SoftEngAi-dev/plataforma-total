# 10. Accesibilidad básica: la web es para todas las personas

> 📚 Curso: **HTML y CSS — Diseño Web Total** · Lección 10 de 10
> 🗓 Exportado: 18/09/2026 desde Plataforma Total
> 🍅 Sugerencia: 1-2 pomodoros para leer + practicar

---

## 📖 Contenido

```html
A11Y: ACCESIBILIDAD (EL 15% DE PERSONAS LO NECESITA)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
No es opción ni caridad: es ingeniería correcta, y mejora la UX de TODOS.

CHECKLIST FUNDAMENTAL
1. HTML semántico: usa <nav>, <main>, <button> reales (no <div onclick>)
2. alt en TODAS las imágenes con información: alt="gráfico de ventas 2025"
3. Contraste: texto vs fondo mínimo 4.5:1 (WebAIM Contrast Checker)
4. Todo operable con teclado (tab, enter) — pruébalo sin ratón
5. Labels en formularios (for/id)
6. lang="es" en <html> — los lectores de pantalla pronuncian bien
7. No comuniques solo con color ("los campos rojos"): icono + texto también

PRUEBA 30 SEGUNDOS: aprieta TAB en tu web. ¿Ves el foco? ¿Tiene sentido el orden?
Nivel pro: Lighthouse (F12) → auditoría de accesibilidad automática.
```

---

## 📝 Quiz de la lección

### 1. ¿Qué elemento es correcto para acción clickeable accesible?
- A) <div onclick=...>
- B) <span onclick=...>
- C) <button>
- D) cualquiera
### 2. ¿Cuál es el contraste mínimo texto/fondo recomendado?
- A) 2:1
- B) 3:1
- C) 4.5:1
- D) 10:1

---

## 🔑 Respuestas y explicaciones

**1.** ✅ <button> — <button> trae gratis: foco de teclado, Enter/Espacio, y semántica para lectores de pantalla.
**2.** ✅ 4.5:1 — WCAG AA: 4.5:1 para texto normal (3:1 para texto grande).

---
✅ Al terminar, marca la lección como completada en la app (📚 Aprender → ✅ Completada)
