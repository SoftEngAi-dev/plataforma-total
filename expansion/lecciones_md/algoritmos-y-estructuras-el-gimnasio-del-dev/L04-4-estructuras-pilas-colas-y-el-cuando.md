# 4. Estructuras: pilas, colas y el cuándo elegirlas

> 📚 Curso: **Algoritmos y Estructuras — El Gimnasio del Dev** · Lección 4 de 5
> 🗓 Exportado: 18/09/2026 desde Plataforma Total
> 🍅 Sugerencia: 1-2 pomodoros para leer + practicar

---

## 📖 Contenido

```text
ESTRUCTURA CORRECTA = PROBLEMA MEDIO RESUELTO
━━━━━━━━━━━━━━━━━━━━━━━━━━━
STACK (pila, LIFO: último en entrar, primero en salir)
  pila = []; pila.append(x) ; pila.pop()
  CASOS: undo/redo · validar paréntesis balanceados · historial navegador · recorrido DFS

QUEUE (cola, FIFO: primero en entrar, primero en salir)
  from collections import deque
  cola = deque(); cola.append(x) ; cola.popleft()        # O(1) ambos extremos
  CASOS: procesar tareas en orden de llegada · BFS (recorrido por niveles) · colas de mensajes

  list.pop(0) es O(n) (desplaza todo) ← por qué existe deque en Python: O(1) a principios

SET: pertinencia ultra rápida O(1): if x in visitados (dedup directo: len(set(lista)))
Consejo maestro (pregunta de entrevista): N elementos donde hay duplicados en 1..N → set o frecuencia dict.

ÁRBOLES/GRAFOS (mención strategically importante): nodos con hijos (DOM, archivos, org. charts) y redes (amigos, mapas).
  DFS (profund) con pila/recursión; BFS (anchos/por niveles) con queue.
```

---

## 📝 Quiz de la lección

### 1. Stack o Queue para implementar UNDO (deshacer)?
- A) Queue
- B) Stack: reverts the last action first (LIFO), el comportamiento natural del deshacer
- C) Un dict
- D) List
### 2. ¿Por qué deque y no list para queue en Python?
- A) Es más corto
- B) popleft() es O(1) en deque pero O(n) en list (remover del principio desplaza todo)
- C) No hay list
- D) Por nada

---

## 🔑 Respuestas y explicaciones

**1.** ✅ Stack: reverts the last action first (LIFO), el comportamiento natural del deshacer — LIFO: la última acción sale primero cuando deshaces.
**2.** ✅ popleft() es O(1) en deque pero O(n) en list (remover del principio desplaza todo) — El error rendimiento clásico: list.pop(0) en bucle = degradación invisible a O(n²).

---
✅ Al terminar, marca la lección como completada en la app (📚 Aprender → ✅ Completada)
