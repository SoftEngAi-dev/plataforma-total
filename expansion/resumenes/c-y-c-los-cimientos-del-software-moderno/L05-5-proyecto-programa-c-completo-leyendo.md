# ⚡ Cheatsheet — 5. Proyecto: programa C completo leyendo archivos

> C y C++ — Los Cimientos del Software Moderno · Lección 5 · 18/09/2026

## 💡 Idea central
CONSTRUYE: CONTADOR DE PALABRAS EN C puro

## 🧠 Autoexamen (tápate la respuesta)
- **¿Qué return values significan en main C?** → 0 = éxito; ≠0 = falló (la shell lo lee con $? — parte del protocolo Unix) _(El exit code es como los programas 'hablan' entre sí en batch/pipes: vital en scripts.)_
- **¿Por qué fclose(f) explícito importa en C?** → Sin cerrar, fopen queda abiertoy puede agotar file descriptors / corrupt data si escribías _(C no tiene with/auto-cleanup: cada recurso abierto necesita su cierre deliberado.)_

## 🔁 Repaso espaciado sugerido
Hoy → mañana → dentro de 3 días → dentro de una semana. 5 minutos bastan.
