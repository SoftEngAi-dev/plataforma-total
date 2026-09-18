# ⚡ Cheatsheet — 2. CSV, limpieza y transformación de columnas

> Pandas — Excel con Superpoderes en Python · Lección 2 · 18/09/2026

## 💡 Idea central
EL FLUJO DE TRABAJO DIARIO DE PANDAS

## 🧠 Autoexamen (tápate la respuesta)
- **¿Qué hace df.isna().sum()?** → Cuenta valores faltantes POR COLUMNA: la primera revisión de salud de un dataset _(Antes de analizar: ¿cuántos huecos hay y dónde? Ahí decides tu estrategia de limpieza.)_
- **¿fillna con la mediana vs dropna?** → fillna conserva todas las filas imputando un valor neutro; dropna las elimina — depende del caso _(Poquitas filas → drop; muchas → imputar. La mediana es robusta a outliers.)_

## 🔁 Repaso espaciado sugerido
Hoy → mañana → dentro de 3 días → dentro de una semana. 5 minutos bastan.
