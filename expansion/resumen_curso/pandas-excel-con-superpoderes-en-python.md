# 📕 Resumen maestro — Pandas — Excel con Superpoderes en Python

> Todo el curso en una hoja: una idea núcleo por lección. Releer semanal.

## 1. 1. DataFrames: tablero mental de pandas
PANDAS EN UNA PÁGINA ━━━━━━━━━━━━━━━━━━━━━━━━━━━   import pandas as pd              (pip install pandas)    # Serie (una columna con índice) y DataFrame (tabla completa)   edades =…

## 2. 2. CSV, limpieza y transformación de columnas
EL FLUJO DE TRABAJO DIARIO DE PANDAS ━━━━━━━━━━━━━━━━━━━━━━━━━━━   df = pd.read_csv("ventas.csv")          (también read_excel/read_json/read_sql)   df.to_csv("salida.csv", index=F…

## 3. 3. groupby y agregaciones: análisis de negocio directo
GROUPBY: RESUMIR = ENTENDER ━━━━━━━━━━━━━━━━━━━━━━━━━━━   # ¿cómo va cada categoría?   resumen = df.groupby("categoria")["total"].sum()   # varias estadísticas a la vez:   agg = df…

## 4. 4. Fechas, strings y aplicaciones avanzadas (los .dt/.str)
SERIES CON SUPERPODERES: .dt, .str, .apply ━━━━━━━━━━━━━━━━━━━━━━━━━━━ FECHAS: convierte siempre a datetime primero   df["fecha"] = pd.to_datetime(df["fecha"])   df["anio"]  = df["…

## 5. 5. Visualización rápida y detección de historias
GRÁFICOS AL INSTANTE: LA HISTORIA EMERGE ━━━━━━━━━━━━━━━━━━━━━━━━━━━   import matplotlib.pyplot as plt            (pip install matplotlib)   df["total"].hist(bins=30); plt.show()  …

## 6. 6. Proyecto final: EDA completo de un dataset público
TU EDA PROFESSIONAL (60-90 MINUTOS, ENTREGABLE) ━━━━━━━━━━━━━━━━━━━━━━━━━━━ Dataset sugerido: Titanic (seaborn: sns.load_dataset("titanic") gratis) o un CSV de datos abiertos de tu…

---
✅ 6 lecciones · 📝 12 preguntas de repaso en quizzes_html/ · tests/