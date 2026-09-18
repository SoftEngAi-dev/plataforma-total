# 8. Funciones y arrow functions: el corazón de JS

> 📚 Curso: **JavaScript — De Cero a Experto** · Lección 8 de 18
> 🗓 Exportado: 18/09/2026 desde Plataforma Total
> 🍅 Sugerencia: 1-2 pomodoros para leer + practicar

---

## 📖 Contenido

```javascript
FUNCIONES: HAY 3 SABORES
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1. Declarada (con hoisting: puedes llamarla antes de definirla)
  function sumar(a, b) { return a + b; }

2. Expresada
  const sumar = function(a, b) { return a + b; };

3. ARROW (la moderna, más corta, hereda `this`)
  const sumar = (a, b) => { return a + b; };
  const doble = n => n * 2;                   // 1 parámetro + 1 línea: súper corta
  const saludar = () => "¡Hola!";             // sin parámetros

PARÁMETROS POR DEFECTO Y RESTO
  const precioConIva = (precio, iva = 0.22) => precio * (1 + iva);
  const maximo = (...numeros) => Math.max(...numeros);

RETURN: toda función devuelve undefined salvo que digas return.

REGLA: funciones CORTAS que hacen UNA cosa bien con nombre verbo+qué (calcularTotal, validarEmail).
```

---

## 📝 Quiz de la lección

### 1. ¿Qué devuelve una función sin return?
- A) null
- B) 0
- C) undefined
- D) Error
### 2. ¿Qué diferencia clave tiene una arrow function?
- A) Es más lenta
- B) No tiene su propio this: usa el del contexto que la rodea
- C) No acepta parámetros
- D) No puede devolver valores

---

## 🔑 Respuestas y explicaciones

**1.** ✅ undefined — Sin return explícito, toda función JS devuelve undefined.
**2.** ✅ No tiene su propio this: usa el del contexto que la rodea — Crucial en callbacks y objetos: la arrow no 'secuestra' el this como hace function.

---
✅ Al terminar, marca la lección como completada en la app (📚 Aprender → ✅ Completada)
