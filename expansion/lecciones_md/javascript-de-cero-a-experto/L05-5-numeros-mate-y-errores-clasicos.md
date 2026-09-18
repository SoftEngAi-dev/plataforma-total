# 5. Números, mate y errores clásicos

> 📚 Curso: **JavaScript — De Cero a Experto** · Lección 5 de 18
> 🗓 Exportado: 18/09/2026 desde Plataforma Total
> 🍅 Sugerencia: 1-2 pomodoros para leer + practicar

---

## 📖 Contenido

```javascript
NÚMEROS Y SUS TRAMPAS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Un solo tipo number para enteros y decimales (punto flotante de 64 bits).

  const precio = 19.99;
  Math.round(precio)     → 20
  Math.floor(precio)     → 19
  Math.ceil(precio)      → 20
  Math.random()          → decimal [0, 1)
  Math.floor(Math.random() * 6) + 1   → dado de 1 a 6
  Math.max(3, 9, 4)      → 9

FORMATEAR
  precio.toFixed(2)      → "19.99" (string, ojo)

LA TRAMPA DEL FLOTANTE (universal en programación)
  0.1 + 0.2 === 0.3      → false  (!)
  (0.1 + 0.2).toFixed(2) → "0.30"
Dinero real: trabaja en CENTAVOS enteros (1999) y divide al mostrar.

CONVERSIONES
  Number("42") → 42 ·  parseInt("42px") → 42 ·  String(42) → "42"
  Number("hola") → NaN ·  Number.isNaN(x) para comprobar
```

---

## 📝 Quiz de la lección

### 1. ¿Por qué 0.1 + 0.2 !== 0.3 en JS (y casi todo lenguaje)?
- A) Bug de JavaScript
- B) Representación binaria de punto flotante: 0.1 y 0.2 no son exactos en base 2
- C) La consola miente
- D) Falta de redondeo
### 2. ¿Cómo generar un entero aleatorio entre 1 y 6?
- A) Math.random(1,6)
- B) Math.floor(Math.random() * 6) + 1
- C) random(6)
- D) Math.ceil(Math.random()*6)+1

---

## 🔑 Respuestas y explicaciones

**1.** ✅ Representación binaria de punto flotante: 0.1 y 0.2 no son exactos en base 2 — Como 1/3 en decimal, algunos decimales son infinitos en binario. Solución: enteros (centavos) o toFixed.
**2.** ✅ Math.floor(Math.random() * 6) + 1 — random()*6 ∈ [0,6); floor → 0-5; +1 → dado de 1 a 6.

---
✅ Al terminar, marca la lección como completada en la app (📚 Aprender → ✅ Completada)
