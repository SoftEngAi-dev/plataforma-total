# 📖 Glosario — 5. Proyecto: API Go real + binario listo para producción

> Go — El Lenguaje de la Nube · Lección 5 · Términos que debes poder definir sin mirar

- **Un único binario estático por SO/arquitectura sin dependencias: deployment es 'copiar y correr'** — produce.exe final: sin JVM/python en el server — eso lo aprecian mucho en operaciones.
- **Lecturas/escrituras concurrentes sobre memoria compartida pueden corromperse: el mutex las sincroniza** — Varios requests golpean la misma estructura a la vez: sincronización obligatoria o data race.

✍️ Ejercicio: añade debajo TU propia definición de cada término.
