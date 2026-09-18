# 18. Proyecto final: aplicación completa de tareas (DOM + eventos + JSON)

> 📚 Curso: **JavaScript — De Cero a Experto** · Lección 18 de 18
> 🗓 Exportado: 18/09/2026 desde Plataforma Total
> 🍅 Sugerencia: 1-2 pomodoros para leer + practicar

---

## 📖 Contenido

```javascript
CONSTRUYE: GESTOR DE TAREAS COMPLETO
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Todo el curso condensado en UNA app. Sin frameworks. Para tu portafolio.

MVP (versión mínima, 2 pomodoros)
1. index.html: input + botón + lista <ul>
2. app.js:
   const tareas = JSON.parse(localStorage.getItem("tareas") || "[]");
3. Agregar tarea (submit + preventDefault + push + render + save)
4. render(): limpiar ul, crear li por cada tarea (createElement + textContent ¡no innerHTML!)
5. Marcar completada (toggle class tachado; delegación de eventos)
6. Borrar (botón 🗑 por li; delegación)
7. Filtro: todas/pendientes/hechas (array.filter + render)
8. save(): localStorage.setItem("tareas", JSON.stringify(tareas))

CHECKLIST DE CALIDAD
• [ ] Funciona al recargar (persistencia JSON)
• [ ] Sin bugs con nombres raros (<script> como título → prueba el XSS)
• [ ] Código en: funciones puras tarea-objeto + render + listeners separados

🎓 Si pasaste TODOS los quizzes 🏆 del curso: genera tu certificado en 📚 Aprender.
```

---

## 📝 Quiz de la lección

### 1. ¿Qué dos llamadas sincronizan la app con localStorage?
- A) parse y stringify de JSON
- B) fetch GET y POST
- C) push y pop
- D) querySelector y createElement
### 2. ¿Por qué delegación de eventos en la lista en vez de listener por li?
- A) Es más corto
- B) Los li se recrean en cada render; un solo listener en el ul sigue funcionando siempre
- C) Es requisito del DOM
- D) No hay razón

---

## 🔑 Respuestas y explicaciones

**1.** ✅ parse y stringify de JSON — stringify al guardar, parse al cargar: JSON es el puente.
**2.** ✅ Los li se recrean en cada render; un solo listener en el ul sigue funcionando siempre — Contenido dinámico = listener en el padre estable, acción según e.target.

---
✅ Al terminar, marca la lección como completada en la app (📚 Aprender → ✅ Completada)
