# 1. Big O: el idioma de la eficiencia

> 📚 Curso: **Algoritmos y Estructuras — El Gimnasio del Dev** · Lección 1 de 5
> 🗓 Exportado: 18/09/2026 desde Plataforma Total
> 🍅 Sugerencia: 1-2 pomodoros para leer + practicar

---

## 📖 Contenido

```text
BIG O: CUÁNTO CRECE EL COSTO CUANDO CRECEN LOS DATOS
━━━━━━━━━━━━━━━━━━━━━━━━━━━
No mide tiempo exacto, mide cómo ESCALA. Lo que importa en el mundo real.

LOS 5 QUE DEBES RECONOCER AL INSTANTE
  O(1)        constante      → dict[key], len(lista): mismo tiempo da igual el tamaño
  O(log n)    logarithmic    → BUSQUEDA binaria: 1 millón de datos → ~20 pasos
  O(n)        lineal         → for sobre la lista: n datos, n pasos
  O(n log n)  linealítmico   → los buenos sorts (merge, quicksort): casi lineal
  O(n²)       cuadrático     → for dentro de for (todos contra todos): 10.000 items = 100M pasos 💀
  O(2ⁿ) / O(n!)  exponencial → backtracking mal escrito (solo para problemas pequeños)

ESTIMARLO A OJO (regla mental)
• un bucle → O(n)·• bucle en bucle → O(n²)·• dividir a la mitad cada vez → O(log n)
• 1.000.000 de datos con O(n log n) = segundos; O(n²) = ¡horas!

ESPAZO (complejdad espacial): cuánta memoria EXTRA usa tu algoritmo (el trade space-time está siempre).

Pragmático real: para listas de ~10 elementos, O(n²) da igual; para un millón, eliges.
```

---

## 📝 Quiz de la lección

### 1. ¿Es rapidez absoluta lo que mide Big O?
- A) Sí exacto
- B) Cómo CRECE el costo al crecer n (escalabilidad), no tiempo exacto
- C) Solo memoria
- D) Solo CPU
### 2. ¿Qué complejidad busca/accede en un dict/hash por clave?
- A) O(n)
- B) O(1) promedio: acces directo sin recorrer
- C) O(log n)
- D) O(n²)

---

## 🔑 Respuestas y explicaciones

**1.** ✅ Cómo CRECE el costo al crecer n (escalabilidad), no tiempo exacto — Es la curva de crecimiento que decide si sirve para 10 datos o para 10 millones.
**2.** ✅ O(1) promedio: acces directo sin recorrer — Por eso los diccionarios/hashes dominan el código real: lookups instantáneos.

---
✅ Al terminar, marca la lección como completada en la app (📚 Aprender → ✅ Completada)
