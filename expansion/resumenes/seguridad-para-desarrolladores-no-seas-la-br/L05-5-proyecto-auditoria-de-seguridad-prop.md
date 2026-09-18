# ⚡ Cheatsheet — 5. Proyecto: auditoría de seguridad propia

> Seguridad para Desarrolladores — No Seas la Brecha · Lección 5 · 18/09/2026

## 💡 Idea central
AUDITA TU PROPÍA APP (LO QUE HACE UN BLUE TEAM JUNIOR)

## 🧠 Autoexamen (tápate la respuesta)
- **¿Qué descubre pegar <script>alert(1)</script> en un campo y probar?** → Si ves el alert: tu app ejecuta código de usuario = XSS confirmado _(La prueba ácida manual del XSS: si JS injectado corre, tu escape no es suficiente.)_
- **¿Por qué testear IDOR es tan crítico para endpoints con IDs?** → Es la vulnerabilidad web nº1 real: chequear que solo el DUEÑO accede a su recurso por cada request _(La lección: no confíes en la URL escondida: cada query/id verifica ownership server-side.)_

## 🔁 Repaso espaciado sugerido
Hoy → mañana → dentro de 3 días → dentro de una semana. 5 minutos bastan.
