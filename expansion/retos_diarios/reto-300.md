# 🥊 Reto del día 300

> Hoy tu cerebro ataca: **4. Asincronía en Node: no congeles el servidor** (Node.js — JavaScript en el Servidor)

1. Explica en voz alta este tema durante 2 minutos, sin notas.
2. Relee la lección solo si el paso 1 trabó.
3. Reescribe desde cero el ejemplo clave de la lección.

## 🥊 Desafío exprés (sin mirar)
**¿Por qué prohibir readFileSync en un servidor (salvo arranque)?**

<details><summary>👁 Ver respuesta</summary>

✅ Bloquea el único hilo de Node: TODOS los usuarios esperan — El event loop único detenido = servidor congelado para todos.
</details>

💰 Vale 1 punto de maestría. Acumula 30 → date un premio real.
