# 6. Composición, context y custom hooks: las 3 escaleras

> 📚 Curso: **React — Interfaces Modernas y Reutilizables** · Lección 6 de 8
> 🗓 Exportado: 18/09/2026 desde Plataforma Total
> 🍅 Sugerencia: 1-2 pomodoros para leer + practicar

---

## 📖 Contenido

```jsx
CRECER SIN COLAPSAR
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1. COMPOSICIÓN — children:
  function Card({ titulo, children }) {
    return <section className="card"><h2>{titulo}</h2>{children}</section>;
  }
  <Card titulo="Tareas"><ListaTareas/></Card>
Antes de context/estado global, llega lejos con children.

2. CONTEXT — datos que necesita mucha profundidad sin prop-drilling:
  const TemaContext = createContext("claro");
  <TemaContext.Provider value="oscuro">{app}</TemaContext.Provider>
  const tema = useContext(TemaContext);   // en cualquier nieto
Úsalo para: tema, usuario logueado, idioma. No para TODO (vuelve lento al re-render).

3. CUSTOM HOOKS — lógica reutilizable con estado:
  function useLocalStorage(clave, inicial) {
    const [valor, setValor] = useState(() =>
      JSON.parse(localStorage.getItem(clave)) ?? inicial);
    useEffect(() => localStorage.setItem(clave, JSON.stringify(valor)), [clave, valor]);
    return [valor, setValor];
  }
  // uso: const [tema, setTema] = useLocalStorage("tema", "claro");

Los hooks empiezan con "use" y solo se llaman en el nivel SUPERIOR (ni loops ni condicionales).
```

---

## 📝 Quiz de la lección

### 1. ¿Cuándo llegar a Context?
- A) Desde el primer día
- B) Cuando muchos componentes a mucha profundidad necesitan el mismo dato (tema, usuario, idioma)
- C) Para todo el estado
- D) Nunca
### 2. ¿Qué reglas tienen los hooks (useState, useEffect, customs)?
- A) Top-level del componente, sin loops/ifs, nombres use*
- B) Cualquier lugar del archivo
- C) Solo en useEffect
- D) Dentro de condicionales

---

## 🔑 Respuestas y explicaciones

**1.** ✅ Cuando muchos componentes a mucha profundidad necesitan el mismo dato (tema, usuario, idioma) — Context resuelve prop-drilling global; estado local y composición resuelven la mayoría de los casos.
**2.** ✅ Top-level del componente, sin loops/ifs, nombres use* — El orden fijo de llamadas es cómo React empareja hook con celda de estado: romperlo = caos.

---
✅ Al terminar, marca la lección como completada en la app (📚 Aprender → ✅ Completada)
