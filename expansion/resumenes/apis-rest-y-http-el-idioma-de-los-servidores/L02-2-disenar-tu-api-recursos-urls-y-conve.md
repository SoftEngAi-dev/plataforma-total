# ⚡ Cheatsheet — 2. Diseñar tu API: recursos, URLs y convenciones

> APIs REST y HTTP — El Idioma de los Servidores · Lección 2 · 18/09/2026

## 💡 Idea central
DISEÑO REST QUE LOS DEMÁS ENTIENDEN AL INSTANTE

## 🧠 Autoexamen (tápate la respuesta)
- **¿Cómo es una buena URL de API?** → /api/tareas (sustantivo plural; la ACCIÓN va en el método HTTP, no en la URL) _(Recursos=sustantivos; acciones=GET/POST/PATCH/DELETE: esa es la legibilidad REST.)_
- **¿Por qué responder 201 con el recurso creado en el POST?** → El cliente recibe inmediato el objeto recién creado CON su id asignado; sin nueva llamada gratuita _(El status informa lo ocurrido + la respuesta entrega el valor resultante.)_

## 🔁 Repaso espaciado sugerido
Hoy → mañana → dentro de 3 días → dentro de una semana. 5 minutos bastan.
