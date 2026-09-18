# 3. Tipos de datos y operadores

> 📚 Curso: **JavaScript — De Cero a Experto** · Lección 3 de 18
> 🗓 Exportado: 18/09/2026 desde Plataforma Total
> 🍅 Sugerencia: 1-2 pomodoros para leer + practicar

---

## 📖 Contenido

```javascript
LOS 8 TIPOS QUE IMPORTAN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PRIMITIVOS: string, number, boolean, undefined, null, bigint, symbol
  "hola" · 42 · 3.14 · true · undefined (no asignado) · null (ausencia intencional)
OBJETO (todo lo demás): { }, [ ], funciones...

OPERADORES
  + - * / % **        % = resto (12 % 5 → 2), ** = potencia (2**3 → 8)
  === vs ==  → ESTRICTA compara valor Y tipo (úsala siempre):
    5 === "5"   → false   (tipo distinto)
    5 ==  "5"   → true    (¡convierte! fuente infinita de bugs)
  !==, >, <, >=, <=
  && (y) || (o) ! (no)

DETECCIÓN DE TIPO
  typeof "hola"   → "string"
  typeof undefined → "undefined"

TRAMPA CLÁSICA
  null == undefined  → true ;   null === undefined → false
  NaN === NaN        → false  (usa Number.isNaN(x))
```

---

## 📝 Quiz de la lección

### 1. ¿Por qué usar === y no ==?
- A) Es más rápido
- B) == convierte tipos automáticamente y genera bugs sutiles; === compara valor y tipo
- C) Por estilo
- D) == está obsoleto
### 2. ¿Qué valor representa la ausencia intencional?
- A) 0
- B) ''
- C) null
- D) NaN

---

## 🔑 Respuestas y explicaciones

**1.** ✅ == convierte tipos automáticamente y genera bugs sutiles; === compara valor y tipo — "5" == 5 da true; con === da false. Predicibilidad > comodidad.
**2.** ✅ null — null = 'vacío a propósito'; undefined = 'aún no se le asignó nada'.

---
✅ Al terminar, marca la lección como completada en la app (📚 Aprender → ✅ Completada)
