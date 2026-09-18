# 🎤 Banco de entrevista — Algoritmos y Estructuras — El Gimnasio del Dev

> 10 preguntas esenciales + guía de respuestas las que ya sabes del curso

## 🔥 Fundamentales (del contenido del curso)

1. **¿Es rapidez absoluta lo que mide Big O?**
   - Cómo CRECE el costo al crecer n (escalabilidad), no tiempo exacto  _(Es la curva de crecimiento que decide si sirve para 10 datos o para 10 millones.)_

2. **¿Qué complejidad busca/accede en un dict/hash por clave?**
   - O(1) promedio: acces directo sin recorrer  _(Por eso los diccionarios/hashes dominan el código real: lookups instantáneos.)_

3. **¿Qué requisito tiene la búsqueda binaria?**
   - La lista DEBE estar ordenada (si no, divide mal)  _(binaria=O(log n) pero necesita order previamente: a veces n log n+bar vale)_

4. **¿Cómo convertir múltiples búsquedas O(n) cada una en O(1) cada una?**
   - Construir UN diccionario/hash indexado UNA vez y consultarlo en O(1) luego  _(Trade tiempo-por-memoria: indexar=prepagar para buscar barato.)_

5. **¿Qué complejidad garantiza un sort moderno (Timsort/Timsort-like)?**
   - O(n log n) en el peor caso, con adaptación en datos casi ordenados  _(Por eso los algoritmos de librería estándar superan siempre al casero.)_

6. **¿Cómo ordenar por edad descendente y desempatar por nombre?**
   - sorted(personas, key=lambda p: (-p.edad, p.nombre)) con tupla ascendente/descendente del mismo sort  _(Tuplas en key: orden multi-nivel en UNA Llamada, elegante y estable.)_

7. **Stack o Queue para implementar UNDO (deshacer)?**
   - Stack: reverts the last action first (LIFO), el comportamiento natural del deshacer  _(LIFO: la última acción sale primero cuando deshaces.)_

8. **¿Por qué deque y no list para queue en Python?**
   - popleft() es O(1) en deque pero O(n) en list (remover del principio desplaza todo)  _(El error rendimiento clásico: list.pop(0) en bucle = degradación invisible a O(n²).)_

9. **Two Sum con diccionario es O(n) porque...**
   - un solo paso por datos + lookup O(1) del complemento ya visto  _(Map de vistos → cada elemento se revisa UNA vez; la fuerza bruta anidada era O(n²).)_

10. **Dos punteros (izq/der) hacia el centro resuelven elegantemente...**
   - Invertir in-place, palíndromos, búsqueda en ordenados: patrón O(n) universal  _(Pattern reconocible: dos variables convergiendo por extremos aparecen en decenas de problemas.)_

## 🧗 Profundización (prepáralas explicando en voz alta)
- ¿Qué problema real resuelve Algoritmos y Estructuras y cuándo NO lo usarías?
- Explica el concepto más fuerte del curso sin usar jerga.
- Contrasta Algoritmos y Estructuras con una alternativa: pros/contras.
- Cuenta un error típico de novato en este tema y cómo lo evitas.

## ⭐ Método para contestarlas
1. **Responde en 60 segundos** cada una de las fundamentales, de memoria. Las que tartamudean → repásalas (flashcards/).
2. Graba tu voz en 2 y escúchate: claridad y precisión importan tanto como el contenido técnico.
3. Una respuesta buena = definición (1 línea) + ejemplo (1) + por qué importa (1).
