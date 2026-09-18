# ⚡ Cheatsheet — 2. Errores a la vista: el if err != nil filosófico

> Go — El Lenguaje de la Nube · Lección 2 · 18/09/2026

## 💡 Idea central
LA FILOSOFÍA GO: SIN EXCEPCIONES OCULTAS

## 🧠 Autoexamen (tápate la respuesta)
- **¿Por qué Go no tiene excepciones para errores esperables?** → Diseño deliberado: errores como valores devueltos obligan a manejarlos conscientemente y flujo de control visible _(En Go el manejo de error no se esconde en catch lejanos: está cara a cara contigo.)_
- **if err != nil es...** → El patrón universal de Go para comprobar y manejar errores devueltos por cada operación fallible _(Todos los libros lo bromean, todos los proyectos sanos lo escriben sin pereza.)_

## 🔁 Repaso espaciado sugerido
Hoy → mañana → dentro de 3 días → dentro de una semana. 5 minutos bastan.
