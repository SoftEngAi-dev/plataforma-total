# 📖 Glosario — 3. Estado con StatefulWidget y setState

> Flutter — Apps Hermosas con Una Sola Base · Lección 3 · Términos que debes poder definir sin mirar

- **setState marca el widget como sucio para que Flutter lo redibuje con el valor nuevo** — Mutación sin setState = estado cambiado pero UI vieja: el bug de todo novato.
- **En initState (corre una vez al crearse); y liberas sus recursos en dispose** — build se ejecuta muchas veces: inicialización va en initState, limpieza en dispose.

✍️ Ejercicio: añade debajo TU propia definición de cada término.
