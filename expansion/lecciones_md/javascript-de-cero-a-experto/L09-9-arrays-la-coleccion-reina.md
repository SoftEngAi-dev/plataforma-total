# 9. Arrays: la colección reina

> 📚 Curso: **JavaScript — De Cero a Experto** · Lección 9 de 18
> 🗓 Exportado: 18/09/2026 desde Plataforma Total
> 🍅 Sugerencia: 1-2 pomodoros para leer + practicar

---

## 📖 Contenido

```javascript
ARRAYS: LISTAS ORDENADAS DE CUALQUIER COSA
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  const numeros = [10, 20, 30];
  numeros[0]         → 10
  numeros.length     → 3

AGREGAR/QUITAR extremos
  numeros.push(40)   → agrega al final
  numeros.pop()      → quita el último
  numeros.shift()    → quita el primero
  numeros.unshift(5) → agrega al inicio

BUSCAR/CORTAR
  numeros.indexOf(20)     → 1
  numeros.includes(99)    → false
  numeros.slice(0, 2)     → [10, 20] (copia, no toca al original)
  numeros.splice(1, 1)    → quita (MUTA al original)

UNIR Y CONVERTIR
  [1,2].join("-")    → "1-2"
  [...a, ...b]       → fusionar arrays con spread
  [...numeros]       → copia superficial

TRAMPA: const a = [1]; const b = a; b.push(2) → a TIENE el 2 (¡misma referencia!). Copia con [...a].
```

---

## 📝 Quiz de la lección

### 1. ¿Qué métodos agregan/quitan AL FINAL de un array?
- A) shift/unshift
- B) push/pop
- C) slice/splice
- D) join/split
### 2. const b = a (arrays) — ¿qué relación tienen?
- A) Copia total
- B) Apuntan AL MISMO array: mutar uno muta el otro
- C) b es de solo lectura
- D) Ninguna

---

## 🔑 Respuestas y explicaciones

**1.** ✅ push/pop — push y pop operan en el extremo final; shift/unshift al inicio.
**2.** ✅ Apuntan AL MISMO array: mutar uno muta el otro — Los arrays son referencias. Copia real: [...a] o a.slice().

---
✅ Al terminar, marca la lección como completada en la app (📚 Aprender → ✅ Completada)
