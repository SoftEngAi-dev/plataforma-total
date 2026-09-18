# ⚡ Cheatsheet — 4. Amenazas en el código diario: XSS, CSRF y uploads

> Seguridad para Desarrolladores — No Seas la Brecha · Lección 4 · 18/09/2026

## 💡 Idea central
LOS 3 MONSTRUOS COTIDIANOS DEL LADO CLIENTE

## 🧠 Autoexamen (tápate la respuesta)
- **¿En qué difiere XSS de CSRF?** → XSS roba/ejecuta en NAVEGADOR ajeno (inyectar JS); CSRF fuerza ACCIONES con tu sesión (abusa confianza del sitio) _(XSS=inyección de scripts en users finales; CSRF=peticiones falsificadas usando la sesión del usuario.)_
- **¿Cuál defensa mata CSRF de forma estructural?** → Token CSRF único por formulario/sesión que el atacante no puede conocer + SameSite en cookies _(El atacante puede enviar el request PERO no el token secreto del formulario legítimo.)_

## 🔁 Repaso espaciado sugerido
Hoy → mañana → dentro de 3 días → dentro de una semana. 5 minutos bastan.
