# ⚡ Cheatsheet — 2. HTTPS, headers y sanitización: cimientos prácticos

> Seguridad para Desarrolladores — No Seas la Brecha · Lección 2 · 18/09/2026

## 💡 Idea central
DEFENSA EN CAPAS (LO QUE CONFIGURAS HOY)

## 🧠 Autoexamen (tápate la respuesta)
- **¿Qué hace el atributo HttpOnly en una cookie?** → El JavaScript NO puede leerla: si un atacante ejecuta XSS no te roba la sesión _(Las cookies de sesión SIEMPRE HttpOnly + Secure + SameSite.)_
- **¿Qué defensa da Content-Security-Policy?** → Limita de QUÉ orígenes pueden cargarse scripts/recursos: corta de raíz muchísimos XSS _(CSP bien puesta desactiva la ejecución de scripts inyectados inline.)_

## 🔁 Repaso espaciado sugerido
Hoy → mañana → dentro de 3 días → dentro de una semana. 5 minutos bastan.
