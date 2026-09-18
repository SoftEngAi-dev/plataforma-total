# 4. Strings: la caja de herramientas del texto

> 📚 Curso: **JavaScript — De Cero a Experto** · Lección 4 de 18
> 🗓 Exportado: 18/09/2026 desde Plataforma Total
> 🍅 Sugerencia: 1-2 pomodoros para leer + practicar

---

## 📖 Contenido

```javascript
TEXTO COMO DATO
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  const nombre = "Ada Lovelace";

PLANTILLAS LITERALES (backticks): las usarás siempre
  `Hola ${nombre}, tienes ${2026 - 1815} años.`   // interpolación

MÉTODOS ESENCIALES
  nombre.length             → 12
  nombre.toUpperCase()      → "ADA LOVELACE"
  nombre.toLowerCase()      → "ada lovelace"
  nombre.includes("Love")   → true
  nombre.startsWith("Ad")   → true
  nombre.slice(0, 3)        → "Ada"
  nombre.split(" ")         → ["Ada", "Lovelace"]
  "  sobrante  ".trim()     → "sobrante"
  nombre.replace("Ada", "Grace")  → "Grace Lovelace"

INMUTABILIDAD: los métodos devuelven NUEVO string; el original nunca cambia.
  let s = "hola";  let t = s.toUpperCase();  // s sigue siendo "hola"

Acceso por índice: nombre[0] → "A". Último: nombre[nombre.length-1].
```

---

## 📝 Quiz de la lección

### 1. ¿Qué es una plantilla literal?
- A) Un string común
- B) Backticks con ${} para interpolar variables/expresiones
- C) Una función
- D) Un comentario
### 2. Tras let s="hola"; s.toUpperCase(); ¿qué vale s?
- A) "HOLA"
- B) "hola" — los strings son inmutables
- C) Error
- D) undefined

---

## 🔑 Respuestas y explicaciones

**1.** ✅ Backticks con ${} para interpolar variables/expresiones — `Hola ${nombre}` — la forma moderna de construir texto dinámico.
**2.** ✅ "hola" — los strings son inmutables — toUpperCase devuelve un NUEVO string; s no cambia salvo que lo reasignes.

---
✅ Al terminar, marca la lección como completada en la app (📚 Aprender → ✅ Completada)
