# ⚡ Cheatsheet — 4. Fechas, strings y aplicaciones avanzadas (los .dt/.str)

> Pandas — Excel con Superpoderes en Python · Lección 4 · 18/09/2026

## 💡 Idea central
SERIES CON SUPERPODERES: .dt, .str, .apply

## 🧠 Autoexamen (tápate la respuesta)
- **¿Qué permite df['fecha'].dt.month después de to_datetime?** → Extraer partes de fecha (mes/año/día/nombre) VECTORIZADO sobre toda la columna _(El accesor .dt convierte fechas en datos analizables: estacionalidad, agrupar por mes...)_
- **df['email'].str.contains('silva', na=False) — ¿por qué na=False?** → contains con NA devuelve NA y rompe filtros booleanos: na=False lo maneja seguro _(Detalle que evita un error común al filtrar strings con valores faltantes.)_

## 🔁 Repaso espaciado sugerido
Hoy → mañana → dentro de 3 días → dentro de una semana. 5 minutos bastan.
