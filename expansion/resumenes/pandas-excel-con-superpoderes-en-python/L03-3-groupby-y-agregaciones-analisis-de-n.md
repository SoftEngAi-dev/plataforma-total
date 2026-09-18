# ⚡ Cheatsheet — 3. groupby y agregaciones: análisis de negocio directo

> Pandas — Excel con Superpoderes en Python · Lección 3 · 18/09/2026

## 💡 Idea central
GROUPBY: RESUMIR = ENTENDER

## 🧠 Autoexamen (tápate la respuesta)
- **¿Qué hace df['categoria'].value_counts()?** → Cuenta frecuencia de cada valor: la vía rápida de 'top categorías' sin SQL _(El one-liner favorito: en 1 llamada tienes el panorama categorial más común.)_
- **pd.merge(a, b, on='id', how='left') se comporta como...** → LEFT JOIN de SQL: todas las filas de 'a' + datos de 'b' cuando hay coincidencia en id _(merge=JOIN entre DataFrames por clave; how decide qué filas sobreviven.)_

## 🔁 Repaso espaciado sugerido
Hoy → mañana → dentro de 3 días → dentro de una semana. 5 minutos bastan.
