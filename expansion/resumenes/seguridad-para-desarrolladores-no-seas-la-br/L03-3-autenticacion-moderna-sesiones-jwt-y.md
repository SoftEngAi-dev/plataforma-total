# ⚡ Cheatsheet — 3. Autenticación moderna: sesiones, JWT y OAuth

> Seguridad para Desarrolladores — No Seas la Brecha · Lección 3 · 18/09/2026

## 💡 Idea central
LOGIN 2026: 3 FORMAS, TODAS COMPRENDIDAS

## 🧠 Autoexamen (tápate la respuesta)
- **¿Qué diferencia sesión-clásica de JWT?** → Sesión clásica guarda estado en el servidor con ID en cookie; JWT firma y viaja el estado EN EL TOKEN (stateless) _(Trade: estado revocable/central vs escalabilidad sin estado ni revocación simple.)_
- **¿Por qué JWT en localStorage es riesgoso?** → Cualquier XSS puede JavaScript-leerlo y robar identidad; cookie HttpOnly no es legible por JS _(El trade de seguridad: lo que JavaScript toca, un XSS también toca.)_

## 🔁 Repaso espaciado sugerido
Hoy → mañana → dentro de 3 días → dentro de una semana. 5 minutos bastan.
