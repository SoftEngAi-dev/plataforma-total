# 7. Patrones reales: fetch con estados y manejo de errores

> 📚 Curso: **React — Interfaces Modernas y Reutilizables** · Lección 7 de 8
> 🗓 Exportado: 18/09/2026 desde Plataforma Total
> 🍅 Sugerencia: 1-2 pomodoros para leer + practicar

---

## 📖 Contenido

```jsx
 FETCH EN REACT NIVEL PRODUCCIÓN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  const [datos, setDatos] = useState(null);
  const [cargando, setCargando] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    let cancelado = false;
    (async () => {
      try {
        setCargando(true); setError(null);
        const resp = await fetch("/api/tareas");
        if (!resp.ok) throw new Error(`HTTP ${resp.status}`);
        if (!cancelado) setDatos(await resp.json());
      } catch (e) {
        if (!cancelado) setError(e.message);
      } finally {
        if (!cancelado) setCargando(false);
      }
    })();
    return () => { cancelado = true; };
  }, []);

RENDERIZAR POR ESTADOS (discrimina siempre)
  if (cargando) return <Spinner/>;
  if (error)    return <Alerta texto={error} reintentar={refetch}/>;
  if (!datos?.length) return <Vacio texto="Sin tareas todavía 🌱"/>;
  return <Lista items={datos}/>;

MEJORA MADURA (proyectos grandes): React Query/SWR cachean, reintentan y sincronizan solos — pero primero domina esto a mano para entenderlos.
```

---

## 📝 Quiz de la lección

### 1. ¿Qué 3 estados mínimos modelan cualquier fetch en UI?
- A) vacio, ok, no
- B) cargando, error, datos
- C) init, run, end
- D) get, post, delete
### 2. ¿Por qué la bandera 'cancelado' en el efecto de fetch?
- A) Cancela la red
- B) Evita que una respuesta tardía actualice estado de un componente desmontado (warning + race)
- C) Acelera fetch
- D) No es necesaria

---

## 🔑 Respuestas y explicaciones

**1.** ✅ cargando, error, datos — Con esos tres discriminas exáctamente qué pintar: spinner, mensaje de error o contenido.
**2.** ✅ Evita que una respuesta tardía actualice estado de un componente desmontado (warning + race) — En StrictMode y navegación rápida los componentes se montan/desmontan: la guardia lo hace robusto.

---
✅ Al terminar, marca la lección como completada en la app (📚 Aprender → ✅ Completada)
