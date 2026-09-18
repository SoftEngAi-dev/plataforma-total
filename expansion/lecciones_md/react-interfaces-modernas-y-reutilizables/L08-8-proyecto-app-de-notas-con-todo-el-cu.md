# 8. Proyecto: app de notas con todo el curso

> 📚 Curso: **React — Interfaces Modernas y Reutilizables** · Lección 8 de 8
> 🗓 Exportado: 18/09/2026 desde Plataforma Total
> 🍅 Sugerencia: 1-2 pomodoros para leer + practicar

---

## 📖 Contenido

```jsx
CONSTRUYE: NOTAS REACT COMPLETAS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Requisitos (todo lo aprendido):
1. Estado: notas (array de {id, titulo, texto}) con useState
2. Persistencia: custom hook useLocalStorage("notas", [])
3. UI: formulario controlado (submit + validar trim) · lista con map+key · borrar por nota
4. Filtro de búsqueda: notas.filter(n => n.texto.toLowerCase().includes(busqueda))
5. Edición: estado editando; reemplazar con map(n => n.id === id ? {...n, texto} : n)
6. UI por estados: vacío / lista / editando (ternarios antes del return o componentes)
7. CSS: una clase .nota:hover con transition; responsive mínimo
8. Opcional subidón: useEffect que sincronice al cerrar la pestaña con beforeunload

ENTREGA (para portafolio)
• npm run build → carpeta dist estática
• Despliegue gratis: GitHub Pages / Vercel / Netlify (curso Despliegue)
• README con screenshot y lista de patrones usados

Dales las gracias después: si la terminaste SIN mirar soluciones, ya piensas en React.
```

---

## 📝 Quiz de la lección

### 1. ¿Cómo editar una nota inmutablemente en un array de estado?
- A) notas[idx].texto = x
- B) map que devuelve objeto nuevo {...n, texto: x} solo para el id coincidente
- C) splice y setState
- D) push y pop
### 2. ¿Qué dos APIs persisten las notas en esta app?
- A) fetch + axios
- B) useState + useEffect dentro de un custom hook useLocalStorage
- C) Redux + thunk
- D) Context + reducer

---

## 🔑 Respuestas y explicaciones

**1.** ✅ map que devuelve objeto nuevo {...n, texto: x} solo para el id coincidente — map con spread: reemplazas el objeto con uno NUEVO; referencias nuevas → React entiende y la UI se actualiza.
**2.** ✅ useState + useEffect dentro de un custom hook useLocalStorage — Estado + efecto que escribe a localStorage: patrón simple, potente y reutilizable.

---
✅ Al terminar, marca la lección como completada en la app (📚 Aprender → ✅ Completada)
