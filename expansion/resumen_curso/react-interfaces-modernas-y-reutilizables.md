# 📕 Resumen maestro — React — Interfaces Modernas y Reutilizables

> Todo el curso en una hoja: una idea núcleo por lección. Releer semanal.

## 1. 1. React: pensar en componentes
REACT EN UNA IDEA: UI = f(estado) ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ React es una librería para construir UIs con COMPONENTES: funciones que reciben datos (props) y devuelven descripc…

## 2. 2. Estado con useState: que la UI reaccione
ESTADO: LA MEMORIA DEL COMPONENTE ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ Los datos LOCALES que cambian con el tiempo viven en estado:   import { useState } from "react";    function Conta…

## 3. 3. Renderizar listas y condicionales
LISTAS: MAP + KEY ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━   {tareas.map(t => (     <li key={t.id} className={t.hecha ? "tachada" : ""}>       {t.texto}     </li>   ))}  KEY: identifica cad…

## 4. 4. Eventos, formularios y estado controlado
FORMULARIOS CONTROLADOS (EL PATRÓN REACT) ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ El ESTADO manda, el input solo lo refleja:   const [texto, setTexto] = useState("");   <input     value={t…

## 5. 5. useEffect: sincronizar con el mundo exterior
EFECTOS: DESPUÉS DEL RENDER ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ useEffect corre código DESPUÉS de que React pinta: fetch, timers, suscripciones, localStorage.    useEffect(() => {     …

## 6. 6. Composición, context y custom hooks: las 3 escaleras
CRECER SIN COLAPSAR ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1. COMPOSICIÓN — children:   function Card({ titulo, children }) {     return <section className="card"><h2>{titulo}</h2>{childr…

## 7. 7. Patrones reales: fetch con estados y manejo de errores
 FETCH EN REACT NIVEL PRODUCCIÓN ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━   const [datos, setDatos] = useState(null);   const [cargando, setCargando] = useState(true);   const [error, setEr…

## 8. 8. Proyecto: app de notas con todo el curso
CONSTRUYE: NOTAS REACT COMPLETAS ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ Requisitos (todo lo aprendido): 1. Estado: notas (array de {id, titulo, texto}) con useState 2. Persistencia: custo…

---
✅ 8 lecciones · 📝 16 preguntas de repaso en quizzes_html/ · tests/