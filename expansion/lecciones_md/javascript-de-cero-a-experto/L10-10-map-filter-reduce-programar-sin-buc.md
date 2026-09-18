# 10. map, filter, reduce: programar sin bucles

> 📚 Curso: **JavaScript — De Cero a Experto** · Lección 10 de 18
> 🗓 Exportado: 18/09/2026 desde Plataforma Total
> 🍅 Sugerencia: 1-2 pomodoros para leer + practicar

---

## 📖 Contenido

```javascript
EL TRÍO FUNCIONAL (ÚSALOS SIEMPRE QUE PUEDAS)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  const nums = [1, 2, 3, 4, 5];

MAP — transformar cada elemento (mismo largo):
  nums.map(n => n * 10)            → [10, 20, 30, 40, 50]

FILTER — quedarse con los que cumplen:
  nums.filter(n => n % 2 === 0)    → [2, 4]

REDUCE — condensar todo a un valor:
  nums.reduce((total, n) => total + n, 0)   → 15
                             ↑ acumulador   ↑ valor inicial

ENCADENAR (lo verás en código real todo el tiempo):
  nums.filter(n => n > 2).map(n => n * 10).reduce((t, n) => t + n, 0)   → 120

FIND y SOME/EVERY (prima-hermanas útiles)
  nums.find(n => n > 3)     → 4 (el primero)
  nums.some(n => n > 4)     → true
  nums.every(n => n > 0)    → true

⚠ Ninguno muta el original. for muta silenciosamente; estos son declarativos y seguros.
```

---

## 📝 Quiz de la lección

### 1. ¿Qué devuelve [2,4,6].filter(n => n > 3)?
- A) 6
- B) [4, 6]
- C) 2
- D) 3
### 2. ¿Qué hace el segundo argumento de reduce?
- A) Nada, decorativo
- B) Es el valor inicial del acumulador
- C) Es el límite de iteraciones
- D) Es una función de fallback

---

## 🔑 Respuestas y explicaciones

**1.** ✅ [4, 6] — filter conserva los que cumplen la condición.
**2.** ✅ Es el valor inicial del acumulador — Sin valor inicial, reduce usa el primer elemento — que a veces es sorpresa. Escribe siempre el inicial.

---
✅ Al terminar, marca la lección como completada en la app (📚 Aprender → ✅ Completada)
