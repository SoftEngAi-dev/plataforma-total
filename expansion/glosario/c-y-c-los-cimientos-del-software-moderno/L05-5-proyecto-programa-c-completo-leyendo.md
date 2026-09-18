# 📖 Glosario — 5. Proyecto: programa C completo leyendo archivos

> C y C++ — Los Cimientos del Software Moderno · Lección 5 · Términos que debes poder definir sin mirar

- **0 = éxito; ≠0 = falló (la shell lo lee con $? — parte del protocolo Unix)** — El exit code es como los programas 'hablan' entre sí en batch/pipes: vital en scripts.
- **Sin cerrar, fopen queda abiertoy puede agotar file descriptors / corrupt data si escribías** — C no tiene with/auto-cleanup: cada recurso abierto necesita su cierre deliberado.

✍️ Ejercicio: añade debajo TU propia definición de cada término.
