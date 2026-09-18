# 7. Bucles: for, while y recorrer colecciones

> 📚 Curso: **JavaScript — De Cero a Experto** · Lección 7 de 18
> 🗓 Exportado: 18/09/2026 desde Plataforma Total
> 🍅 Sugerencia: 1-2 pomodoros para leer + practicar

---

## 📖 Contenido

```javascript
REPETICIÓN CONTROLADA
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
FOR clásico (control total):
  for (let i = 0; i < 5; i++) { console.log(i); }

FOR...OF (elementos de un array, EL RECOMENDADO):
  for (const fruta of ["🍎", "🍌", "🥝"]) { console.log(fruta); }

FOR...IN (claves de un objeto):
  for (const clave in persona) { console.log(clave, persona[clave]); }

WHILE (no sabes cuántas vueltas):
  let n = 100;
  while (n > 1) { n = n / 2; }

DO...WHILE (ejecuta AL MENOS una vez).

CONTROL
  break;      → sale del bucle
  continue;   → salta a la siguiente vuelta

⚠ BUCLE INFINITO: condición que nunca cambia. while(true) + break apropiable; i olvidado en for = clásico.
REGLA: confirma que la condición de salida LLEGARÁ a cumplirse.
```

---

## 📝 Quiz de la lección

### 1. ¿Cuál es la forma moderna recomendada de recorrer un array?
- A) for clásico con índice
- B) for...of
- C) for...in
- D) while con contador
### 2. ¿Qué hace continue?
- A) Rompe el bucle
- B) Salta a la siguiente iteración
- C) Termina la función
- D) Pausa 1 segundo

---

## 🔑 Respuestas y explicaciones

**1.** ✅ for...of — for...of es directo y seguro; for...in es para CLAVES de objetos, no arrays.
**2.** ✅ Salta a la siguiente iteración — Omite el resto del bloque en esta vuelta y sigue con la próxima.

---
✅ Al terminar, marca la lección como completada en la app (📚 Aprender → ✅ Completada)
