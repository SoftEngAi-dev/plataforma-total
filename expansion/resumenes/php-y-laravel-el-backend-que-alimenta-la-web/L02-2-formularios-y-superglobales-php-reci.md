# ⚡ Cheatsheet — 2. Formularios y superglobales: PHP recibe datos

> PHP y Laravel — El Backend Que Alimenta la Web · Lección 2 · 18/09/2026

## 💡 Idea central
$_GET, $_POST, $_FILES: EL PAN DE CADA DÍA

## 🧠 Autoexamen (tápate la respuesta)
- **¿Qué hace htmlentities($texto) antes de un echo?** → Escapa <script> etc. evitando XSS: HTML inyectado queda como texto inofensivo _(La regla de vida PHP: toda salida con datos del usuario pasa por escaping.)_
- **$_POST["email"] ?? "" significa...** → Si no viene email, usa '' (null coalescing ?? en vez de undefined/index notice) _(?? evita avisos por índices faltantes — desde PHP 7 la forma elegante.)_

## 🔁 Repaso espaciado sugerido
Hoy → mañana → dentro de 3 días → dentro de una semana. 5 minutos bastan.
