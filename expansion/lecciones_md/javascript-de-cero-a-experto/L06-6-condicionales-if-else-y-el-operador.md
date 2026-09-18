# 6. Condicionales: if, else y el operador ternario

> 📚 Curso: **JavaScript — De Cero a Experto** · Lección 6 de 18
> 🗓 Exportado: 18/09/2026 desde Plataforma Total
> 🍅 Sugerencia: 1-2 pomodoros para leer + practicar

---

## 📖 Contenido

```javascript
DECISIONES
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  if (edad >= 18) {
    acceso = "permitido";
  } else if (edad >= 13) {
    acceso = "con tutor";
  } else {
    acceso = "denegado";
  }

TERNARIO (asignación corta y elegante)
  const mensaje = edad >= 18 ? "mayor" : "menor";
Solo para casos simples; si anidas ternarios, vuelve a if.

SWITCH (varias opciones del mismo valor)
  switch (dia) {
    case "lunes":  actividad(); break;
    case "viernes": fiesta(); break;
    default: descansar();
  }
⚠ Sin break, CASCADA engañosa ("fall-through").

FALSY (valores que if trata como falso): false, 0, "", null, undefined, NaN
  if (nombre) { ... }   // pasa solo si nombre tiene contenido
?? (nullish): valor ?? "por defecto"  → solo captura null/undefined (¡más preciso que ||!).
```

---

## 📝 Quiz de la lección

### 1. ¿Cuáles valores son falsy en JS?
- A) Solo false
- B) false, 0, "", null, undefined, NaN
- C) Solo null y undefined
- D) Cualquier número
### 2. ¿Qué hace nombre ?? "invitado"?
- A) Siempre da "invitado"
- B) Usa "invitado" SOLO si nombre es null o undefined (no si es "" o 0)
- C) Es un error de sintaxis
- D) Compara nombre con invitado

---

## 🔑 Respuestas y explicaciones

**1.** ✅ false, 0, "", null, undefined, NaN — if(x) con x falsy no ejecuta el bloque — revisa esta lista cuando te sorprenda.
**2.** ✅ Usa "invitado" SOLO si nombre es null o undefined (no si es "" o 0) — ?? es el default preciso: || también rechazaría '' y 0 que podrías querer conservar.

---
✅ Al terminar, marca la lección como completada en la app (📚 Aprender → ✅ Completada)
