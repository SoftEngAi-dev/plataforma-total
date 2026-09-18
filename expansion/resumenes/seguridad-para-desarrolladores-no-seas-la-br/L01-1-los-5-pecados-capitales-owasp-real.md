# ⚡ Cheatsheet — 1. Los 5 pecados capitales (OWASP real)

> Seguridad para Desarrolladores — No Seas la Brecha · Lección 1 · 18/09/2026

## 💡 Idea central
SEGURIDAD SIN PARANOIA: LO QUE ROMPE EL MUNDO

## 🧠 Autoexamen (tápate la respuesta)
- **¿Qué es IDOR?** → Broken Access Control: cambiar el ID en la URL y acceder a datos de OTROS usuarios porque el servidor no verifica propiedad _(/perfil/1 → cambias a /perfil/2 y ves datos ajenos si el servidor no checkea dueño.)_
- **¿Cómo se guardan contraseñas correctamente?** → Hash con bcrypt/argon2 + salt: ni siquiera tú (admin) puedes leerlas _(El hash robusto es irreversible y lento a propósito: el que dicen los propios hashes débiles.)_

## 🔁 Repaso espaciado sugerido
Hoy → mañana → dentro de 3 días → dentro de una semana. 5 minutos bastan.
