# 2. Variables: let, const y por qué var quedó atrás

> 📚 Curso: **JavaScript — De Cero a Experto** · Lección 2 de 18
> 🗓 Exportado: 18/09/2026 desde Plataforma Total
> 🍅 Sugerencia: 1-2 pomodoros para leer + practicar

---

## 📖 Contenido

```javascript
LET Y CONST (y olvida var por ahora)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  const nombre = "Ada";       // NO se puede reasignar. EL POR DEFECTO.
  let edad = 36;              // reasignable. Cuándo necesitas cambiarla.
  var  vieja = "evítala";     // scope confuso; existe solo en código legado

  edad = 37;                  // ✅ let permite
  nombre = "Otra";            // ❌ TypeError

🚨 const no significa inmutable por dentro:
  const lista = [1, 2, 3];
  lista.push(4);              // ✅ permitido (muta el contenido)
  lista = [];                 // ❌ prohibido (reasignar)

ÁMBITO (scope)
  { let x = 1; }              // x solo vive entre llaves (bloque)
Funciones también crean su propio ámbito.

REGLA PROFESIONAL: const por defecto; let solo si vas a reasignar; var nunca (código nuevo). Hace tu intención legible y previene bugs.
```

---

## 📝 Quiz de la lección

### 1. ¿Cuál es la regla moderna para declarar variables?
- A) var siempre
- B) let siempre
- C) const por defecto; let solo si reasignas; var nunca
- D) No declarar, usar globales
### 2. ¿Qué pasa con const arr = [1]; arr.push(2)?
- A) Error: const es inmutable
- B) Funciona: const prohíbe reasignar, no mutar el contenido
- C) Duplica el array
- D) Lo convierte en string

---

## 🔑 Respuestas y explicaciones

**1.** ✅ const por defecto; let solo si reasignas; var nunca — const comunica 'esto no cambia': menos sorpresas, bugs más difíciles.
**2.** ✅ Funciona: const prohíbe reasignar, no mutar el contenido — const congela la REFERENCIA, no el objeto: puedes mutar por dentro.

---
✅ Al terminar, marca la lección como completada en la app (📚 Aprender → ✅ Completada)
