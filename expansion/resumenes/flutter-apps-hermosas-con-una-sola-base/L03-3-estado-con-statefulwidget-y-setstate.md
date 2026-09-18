# ⚡ Cheatsheet — 3. Estado con StatefulWidget y setState

> Flutter — Apps Hermosas con Una Sola Base · Lección 3 · 18/09/2026

## 💡 Idea central
ESTADO: QUE LA APP REACCIONE

## 🧠 Autoexamen (tápate la respuesta)
- **¿Por qué dentro de setState(() { cuenta++; })?** → setState marca el widget como sucio para que Flutter lo redibuje con el valor nuevo _(Mutación sin setState = estado cambiado pero UI vieja: el bug de todo novato.)_
- **¿Dónde inicias un fetch o timer en un StatefulWidget?** → En initState (corre una vez al crearse); y liberas sus recursos en dispose _(build se ejecuta muchas veces: inicialización va en initState, limpieza en dispose.)_

## 🔁 Repaso espaciado sugerido
Hoy → mañana → dentro de 3 días → dentro de una semana. 5 minutos bastan.
