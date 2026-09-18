# ⚡ Cheatsheet — 2. Capturar grupos y.los casos reales: validación y extracción

> Expresiones Regulares — El Lenguaje de Patrones · Lección 2 · 18/09/2026

## 💡 Idea central
CAPTURAR SUSTANCIAS (LO QUE BUSCAS EXTRAER)

## 🧠 Autoexamen (tápate la respuesta)
- **¿Qué hace (?P<nombre>...) en Python regex?** → Grupo NOMBRADO: extraes por m.group('nombre') en vez de factores posición brittle _(Regex autocomentados: los nombres documentan cada parte que capturas.)_
- **¿Qué logra el lookahead (?=.*[A-Z]) en la contraseña?** → VERIFICA sin consumir: exige que exista una mayúscula en lo que sigue sin avanzar el cursor _(Lookaheads = 'debe cumplirse X adelante': validaciones compuestas sin complicar los grupos.)_

## 🔁 Repaso espaciado sugerido
Hoy → mañana → dentro de 3 días → dentro de una semana. 5 minutos bastan.
