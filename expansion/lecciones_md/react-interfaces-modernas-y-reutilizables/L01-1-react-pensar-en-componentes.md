# 1. React: pensar en componentes

> 📚 Curso: **React — Interfaces Modernas y Reutilizables** · Lección 1 de 8
> 🗓 Exportado: 18/09/2026 desde Plataforma Total
> 🍅 Sugerencia: 1-2 pomodoros para leer + practicar

---

## 📖 Contenido

```jsx
REACT EN UNA IDEA: UI = f(estado)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
React es una librería para construir UIs con COMPONENTES: funciones que reciben datos (props) y devuelven descripciones de qué mostrar (JSX). Cuando el estado cambia, React re-renderiza lo necesario. Tú no tocas el DOM a mano.

SETUP MODERNO (Vite)
  npm create vite@latest mi-app -- --template react
  cd mi-app && npm install && npm run dev

TU PRIMER COMPONENTE
  // App.jsx
  function Saludo({ nombre }) {
    return <h1>¡Hola, {nombre}!</h1>;
  }
  export default Saludo;

JSX = mezcla HTML con JS (entre llaves):
  <p>2 + 2 = {2 + 2}</p>
  <img src={url} alt={texto} />
⚠ className (no class) · todas las etiquetas se cierran · un solo padre raíz (o <>fragment</>)

EL CICLO: escribes componentes → compones → React se encarga del DOM.
```

---

## 📝 Quiz de la lección

### 1. ¿Qué es JSX?
- A) Un lenguaje aparte
- B) Sintaxis que escribe HTML dentro de JS y llama funciones de React para construir el DOM
- C) CSS en JS
- D) Un compilador
### 2. ¿Qué son las props?
- A) Variables globales
- B) Los datos que un componente recibe de su padre (parámetros del componente)
- C) Estilos del componente
- D) Funciones internas

---

## 🔑 Respuestas y explicaciones

**1.** ✅ Sintaxis que escribe HTML dentro de JS y llama funciones de React para construir el DOM — JSX describe la UI; Babel/Vite lo convierte en llamadas a funciones.
**2.** ✅ Los datos que un componente recibe de su padre (parámetros del componente) — Componente = función; props = sus argumentos. Comunicación de padre a hijo.

---
✅ Al terminar, marca la lección como completada en la app (📚 Aprender → ✅ Completada)
