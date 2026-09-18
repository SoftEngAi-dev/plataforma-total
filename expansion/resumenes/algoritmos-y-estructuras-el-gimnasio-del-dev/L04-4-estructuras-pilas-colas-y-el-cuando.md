# ⚡ Cheatsheet — 4. Estructuras: pilas, colas y el cuándo elegirlas

> Algoritmos y Estructuras — El Gimnasio del Dev · Lección 4 · 18/09/2026

## 💡 Idea central
ESTRUCTURA CORRECTA = PROBLEMA MEDIO RESUELTO

## 🧠 Autoexamen (tápate la respuesta)
- **Stack o Queue para implementar UNDO (deshacer)?** → Stack: reverts the last action first (LIFO), el comportamiento natural del deshacer _(LIFO: la última acción sale primero cuando deshaces.)_
- **¿Por qué deque y no list para queue en Python?** → popleft() es O(1) en deque pero O(n) en list (remover del principio desplaza todo) _(El error rendimiento clásico: list.pop(0) en bucle = degradación invisible a O(n²).)_

## 🔁 Repaso espaciado sugerido
Hoy → mañana → dentro de 3 días → dentro de una semana. 5 minutos bastan.
