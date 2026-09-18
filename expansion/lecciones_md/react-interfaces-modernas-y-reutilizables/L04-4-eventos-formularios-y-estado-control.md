# 4. Eventos, formularios y estado controlado

> 📚 Curso: **React — Interfaces Modernas y Reutilizables** · Lección 4 de 8
> 🗓 Exportado: 18/09/2026 desde Plataforma Total
> 🍅 Sugerencia: 1-2 pomodoros para leer + practicar

---

## 📖 Contenido

```jsx
FORMULARIOS CONTROLADOS (EL PATRÓN REACT)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
El ESTADO manda, el input solo lo refleja:
  const [texto, setTexto] = useState("");
  <input
    value={texto}
    onChange={e => setTexto(e.target.value)}
    placeholder="Nueva tarea..."
  />
Cada tecla → setState → re-render → input muestra el nuevo valor. Simple y predecible.

FORMULARIO COMPLETO
  const manejarSubmit = (e) => {
    e.preventDefault();                        // siempre
    if (!texto.trim()) return;
    onAgregar(texto.trim());                   // avisa al padre
    setTexto("");                              // reset controlado
  };
  <form onSubmit={manejarSubmit}>...</form>

EVENTOS SYNTHETICS: React envuelve eventos nativos. Los usas igual; onClic se escribe onClick (camelCase).

UNIDIRECCIONAL = la paz mental: estado arriba; eventos abajo; nunca al revés. Cuando sientas que "empujamos datos hacia arriba", llamas a una función que el padre te pasó por props.
```

---

## 📝 Quiz de la lección

### 1. ¿Qué significa input 'controlado'?
- A) readonly
- B) Su value viene del estado y onChange lo actualiza: el estado es la fuente de verdad
- C) Que valida solo
- D) Que usa refs
### 2. ¿Cómo sabe el hijo que debe agregar una tarea si el estado está arriba?
- A) Accede al estado del padre directamente
- B) Llama a una función que el padre le pasó por props (onAgregar)
- C) Modifica el DOM del padre
- D) No puede

---

## 🔑 Respuestas y explicaciones

**1.** ✅ Su value viene del estado y onChange lo actualiza: el estado es la fuente de verdad — Estado ↔ input en bucle controlado. React manda; el DOM obedece.
**2.** ✅ Llama a una función que el padre le pasó por props (onAgregar) — Datos bajan por props; cambios suben ejecutando callbacks que bajaron por props.

---
✅ Al terminar, marca la lección como completada en la app (📚 Aprender → ✅ Completada)
