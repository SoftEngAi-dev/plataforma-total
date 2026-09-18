# 📖 Glosario — 5. MVC en Laravel: flujo completo de una petición

> PHP y Laravel — El Backend Que Alimenta la Web · Lección 5 · Términos que debes poder definir sin mirar

- **Inyecta directo el modelo por ID (404 automático si no existe) sin hacer find manual** — function show(Tarea $tarea) — el framework busca el id y te da el modelo o 404.
- **Anti mass-assignment: lista blanca de campos rellenables vía create/update (evita inyectar campos no previstos)** — Tarea::create($request->all()) protegido: solo pasa lo autorizado.

✍️ Ejercicio: añade debajo TU propia definición de cada término.
