# ⚡ Cheatsheet — 3. Result y Option: errores como parte del tipo

> Rust — Velocidad de C sin Miedo a los Crashes · Lección 3 · 18/09/2026

## 💡 Idea central
RESULT/OPTION: NULL Y EXCEPCIONES, PERO TIPADOS

## 🧠 Autoexamen (tápate la respuesta)
- **¿Qué hace el operador ? tras una llamada Result?** → Si es Ok, desenvuelve el valor; si es Err, lo retorna inmediatamente a la función llamante (propagación elegante) _(El equivalente Go-verboso pero sin boilerplate: error handling conciso y explícito.)_
- **¿En qué consiste la seguridad adicional de Option<T> vs null?** → No hay null: la AUSENCIA es parte del TIPO y el compilador EXIGE manejar el caso None _(Null = 'agujero invisible'; None = 'la firma te avisa y obliga'. Billion-dollar mistake corregida.)_

## 🔁 Repaso espaciado sugerido
Hoy → mañana → dentro de 3 días → dentro de una semana. 5 minutos bastan.
