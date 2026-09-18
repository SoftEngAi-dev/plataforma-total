# 3. Renderizar listas y condicionales

> 📚 Curso: **React — Interfaces Modernas y Reutilizables** · Lección 3 de 8
> 🗓 Exportado: 18/09/2026 desde Plataforma Total
> 🍅 Sugerencia: 1-2 pomodoros para leer + practicar

---

## 📖 Contenido

```jsx
LISTAS: MAP + KEY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  {tareas.map(t => (
    <li key={t.id} className={t.hecha ? "tachada" : ""}>
      {t.texto}
    </li>
  ))}

KEY: identifica cada elemento entre re-renders
• Debe ser estable y único: ID real, NO el índice del map (salvo lista estática inmutable)
• Sin key: React confunde elementos → bugs visuales y de formulario

CONDICIONALES (dentro del JSX siempre expresiones)
  {cargando && <Spinner />}                 // renderizar o no
  {usuario ? <Panel/> : <Login/>}            // una u otra
  {estado === "error" && <Alerta msg={error}/>}

⚠ VERDAD DEL if: no escribes if dentro del JSX; escribes expresiones boolean/ternarias.
Para ifs complejos: extrae a una función o variable ANTES del return:
  let contenido = estado === "ok" ? <Datos/> : <Vacio/>;
  return <div>{contenido}</div>;
```

---

## 📝 Quiz de la lección

### 1. ¿Qué prop requiere React al mapear elementos y por qué?
- A) id, por CSS
- B) key: identidad estable entre renders para emparejar el DOM correctamente
- C) className, por estilos
- D) index, por orden
### 2. ¿Cómo renderizar condicionalmente en JSX?
- A) Con if/else dentro de llaves
- B) Operador &&, ternario, o variable calculada ANTES del return
- C) Con v-if
- D) No se puede

---

## 🔑 Respuestas y explicaciones

**1.** ✅ key: identidad estable entre renders para emparejar el DOM correctamente — La key es DNI, no apellido: el índice del map cambia y traiciona con listas dinámicas.
**2.** ✅ Operador &&, ternario, o variable calculada ANTES del return — JSX admite expresiones, no sentencias: la lógica va en expresiones o antes del return.

---
✅ Al terminar, marca la lección como completada en la app (📚 Aprender → ✅ Completada)
