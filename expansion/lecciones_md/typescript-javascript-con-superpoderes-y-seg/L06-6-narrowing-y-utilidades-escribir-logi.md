# 6. Narrowing y utilidades: escribir lógica segura

> 📚 Curso: **TypeScript — JavaScript con Superpoderes y Seguridad** · Lección 6 de 7
> 🗓 Exportado: 18/09/2026 desde Plataforma Total
> 🍅 Sugerencia: 1-2 pomodoros para leer + practicar

---

## 📖 Contenido

```javascript
NARROWING: DESECHAR CASOS Y GANAR CERTEZA
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
TS VIGILA tu código y afina el tipo dentro de condicionales:

  function procesar(x: string | number) {
    if (typeof x === "string") { x.toUpperCase(); }   // aquí x ES string ✅
    else                       { x.toFixed(2); }       // aquí x ES number ✅
  }

OPERADORES DE NARROWING
  typeof · instanceof · "prop" in obj · truthiness (if (user))
  Discriminated unions — el PATTERN estrella para estados:
  type Estado =
    | { kind: "cargando" }
    | { kind: "ok"; datos: string[] }
    | { kind: "error"; mensaje: string };
  if (estado.kind === "ok") estado.datos;              // ✅ TS lo sabe
  else if (estado.kind === "error") estado.mensaje;    // ✅

TYPE GUARDS (función que certifica):
  function esString(x: unknown): x is string { return typeof x === "string"; }

⚠ CASTING (as) → último recurso; "tú sabes más que el compilador" suele envejecer mal:
  (valor as Usuario).nombre
```

---

## 📝 Quiz de la lección

### 1. ¿Qué es una discriminated union?
- A) Unir objetos con &
- B) Una unión donde cada variante tiene una clave literal común (kind) que permite narrowing
- C) Una clase abstracta
- D) Un enum
### 2. ¿Qué significa x is string en un type guard?
- A) Una comparación
- B) Le dice a TS: si esta función devuelve true, trata x como string de ahí en adelante
- C) Convierte el tipo
- D) Un error de sintaxis

---

## 🔑 Respuestas y explicaciones

**1.** ✅ Una unión donde cada variante tiene una clave literal común (kind) que permite narrowing — El patrón de modelado de estados favorito en TS: cada rama decide la forma disponible.
**2.** ✅ Le dice a TS: si esta función devuelve true, trata x como string de ahí en adelante — Los guards personalizados enseñan al compilador a razonar sobre tus datos.

---
✅ Al terminar, marca la lección como completada en la app (📚 Aprender → ✅ Completada)
