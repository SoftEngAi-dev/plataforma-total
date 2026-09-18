# ⚡ Cheatsheet — 3. Los 5 errores clásicos de regex (no sufras estos)

> Expresiones Regulares — El Lenguaje de Patrones · Lección 3 · 18/09/2026

## 💡 Idea central
ASÍ SE ROMPE EL REGEX EN PRODUCCIÓN — TUS SALVADOS AQUÍ

## 🧠 Autoexamen (tápate la respuesta)
- **¿Qué arregla .*? frente a .*?** → ? lo vuelve LAZY/no-greedy: captura el MÍNIMO posible en vez de todo lo posible _(La diferencia entre 'primer cierre que encuentras' y 'último del documento': regex es codiciosa por defecto y se come todo.)_
- **¿Cuándo NO usarías regex?** → Para estructuras complejas anidadas como HTML/JSON reales: usa parseadores diseñados, regex se rompe en los bordes _(Zawinski: 'ahora tienes dos problemas'. Texto libre ↔ regex; formato estructurado ↔ parser real.)_

## 🔁 Repaso espaciado sugerido
Hoy → mañana → dentro de 3 días → dentro de una semana. 5 minutos bastan.
