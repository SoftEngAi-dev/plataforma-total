# 2. Problemas clásicos de código y cómo abordarlos

> 📚 Curso: **Entrevistas Técnicas — Demostrar lo que Sabes** · Lección 2 de 4
> 🗓 Exportado: 18/09/2026 desde Plataforma Total
> 🍅 Sugerencia: 1-2 pomodoros para leer + practicar

---

## 📖 Contenido

```text
PATRONES QUE CUBREN EL 70% DE ENTREVISTAS
━━━━━━━━━━━━━━━━━━━━━━━━━━━
FORMATO PARA CADA PROBLEMA (adapta uno y practías en voz alta)
  1. Repite el problema y CLARIFICA: ¿pueden ser negativos? ¿vacío? ¿unicidad?
  2. Di solución BRUTA primero ("la fuerza bruta sería O(n²): recorrer todos") ← muestra razonamiento
  3. Mejora con patrón conocido → implementa leyendo bien → testéalo con ejemplos tuyos
  4. Analiza complejidad y posibles bordes/extensión

LOS 6 PATRONES DE ORO
• TWO POINTERS: dos índices convergiendo → invertir, palíndromos, pares en ordenados
• HASH/SET: lookup O(1) → two sum, duplicates, anagramas
• SLIDING WINDOW: subcadena máxima continua → O(n) donde parecía O(n²)
• STACK: balancear paréntesis, next greater element, historial LIFO
• BFS/DFS: grafos y árboles en niveles (bfs) o caminos (dfs)
• ORDEN/GREEDY: ordenar + decisión local óptima → intervalos, reunión de llamadas

PRÁCTICA: LeetCode Easy con los 6 patrones: 5 por semana con tu patrón claro. Luego mediums.
FREECODE/Exercism NeetCode para estructura: aprender los patos, no memoriza respuestas."`
```

---

## 📝 Quiz de la lección

### 1. ¿Por qué decir PRIMERO la solución fuerza bruta agrea valor?
- A) No lo hace
- B) Muestra que razonas el espacio del problema y luego optimizas: evalúan proceso, no memoria
- C) Más lento
- D) Para tests
### 2. ¿Qué es sliding window?
- A) Nada
- B) Patrón O(n) que mantiene una ventana de elementos entre dos índices sin recorrer repetidamente para sumas/max de subcadena continuables',
- C) Un hash
- D) Un stack

---

## 🔑 Respuestas y explicaciones

**1.** ✅ Muestra que razonas el espacio del problema y luego optimizas: evalúan proceso, no memoria — Demuestras técnica desde lo simple→optimizado: el entrevistador ve tu mente.
**2.** ✅ Patrón O(n) que mantiene una ventana de elementos entre dos índices sin recorrer repetidamente para sumas/max de subcadena continuables', — Substrings continuas: expansión/contracción de dos punteros sin bucles anidados.

---
✅ Al terminar, marca la lección como completada en la app (📚 Aprender → ✅ Completada)
