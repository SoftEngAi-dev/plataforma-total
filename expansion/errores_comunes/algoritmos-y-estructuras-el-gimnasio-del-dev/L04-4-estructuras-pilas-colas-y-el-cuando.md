# ⚠️ Errores comunes — 4. Estructuras: pilas, colas y el cuándo elegirlas

> Algoritmos y Estructuras — El Gimnasio del Dev · Lección 4 · Aprender de los errores (propios y ajenos)

- ❌ «Queue» → Frente a «Stack o Queue para implementar UNDO (deshacer)?» lo fácil es confundirse. **Verdad**: Stack: reverts the last action first (LIFO), el comportamiento natural del deshacer. LIFO: la última acción sale primero cuando deshaces.
- ❌ «Un dict» → Frente a «Stack o Queue para implementar UNDO (deshacer)?» lo fácil es confundirse. **Verdad**: Stack: reverts the last action first (LIFO), el comportamiento natural del deshacer. LIFO: la última acción sale primero cuando deshaces.
- ❌ «Es más corto» → Frente a «¿Por qué deque y no list para queue en Python?» lo fácil es confundirse. **Verdad**: popleft() es O(1) en deque pero O(n) en list (remover del principio desplaza todo). El error rendimiento clásico: list.pop(0) en bucle = degradación invisible a O(n²).
- ❌ «No hay list» → Frente a «¿Por qué deque y no list para queue en Python?» lo fácil es confundirse. **Verdad**: popleft() es O(1) en deque pero O(n) en list (remover del principio desplaza todo). El error rendimiento clásico: list.pop(0) en bucle = degradación invisible a O(n²).

## 🩹 Antídoto universal
1. Lee el mensaje de error COMPLETO antes de googlear.
2. Pon el error exacto a la IA local y pide explicación, no solución.
3. Documenta el error en tu bitácora: error → causa → fix.
