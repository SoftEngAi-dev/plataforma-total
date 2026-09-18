# 2. CSV, limpieza y transformación de columnas

> 📚 Curso: **Pandas — Excel con Superpoderes en Python** · Lección 2 de 6
> 🗓 Exportado: 18/09/2026 desde Plataforma Total
> 🍅 Sugerencia: 1-2 pomodoros para leer + practicar

---

## 📖 Contenido

```python
EL FLUJO DE TRABAJO DIARIO DE PANDAS
━━━━━━━━━━━━━━━━━━━━━━━━━━━
  df = pd.read_csv("ventas.csv")          (también read_excel/read_json/read_sql)
  df.to_csv("salida.csv", index=False)    → guardar

LIMPIEZA (la realidad del 80% del trabajo)
  df.isna().sum()                 → cuántos faltan por columna (¡primero siempre!)
  limpio = df.dropna()             → eliminar filas con NA
  limpio = df.dropna(subset=["precio"])     → solo si falta en columnas críticas
  df["precio"] = df["precio"].fillna(df["precio"].median())   → imputar
  df = df.rename(columns=str.lower)         → columnas en minúsculas
  df = df.drop_duplicates()                   → quitar duplicados
  df["fecha"] = pd.to_datetime(df["fecha"])   → parsear fechas de verdad

TRANSFORMAR Y CREAR
  df["total"] = df["precio"] * df["cantidad"]
  df["Categoria2"] = df["precio"].apply(lambda p: "caro" if p > 100 else "barato")
  df["anio"] = df["fecha"].dt.year                            → acceder a partes de fecha
  df = df.sort_values("total", ascending=False)
  df.reset_index(drop=True, inplace=True)

CADENA de métodos limpia y legible (method chaining, muy común en código pro).
```

---

## 📝 Quiz de la lección

### 1. ¿Qué hace df.isna().sum()?
- A) Suma todo
- B) Cuenta valores faltantes POR COLUMNA: la primera revisión de salud de un dataset
- C) Borra NAs
- D) CSV
### 2. ¿fillna con la mediana vs dropna?
- A) Siempre dropna
- B) fillna conserva todas las filas imputando un valor neutro; dropna las elimina — depende del caso
- C) Ninguna diferencia
- D) fillna es un error

---

## 🔑 Respuestas y explicaciones

**1.** ✅ Cuenta valores faltantes POR COLUMNA: la primera revisión de salud de un dataset — Antes de analizar: ¿cuántos huecos hay y dónde? Ahí decides tu estrategia de limpieza.
**2.** ✅ fillna conserva todas las filas imputando un valor neutro; dropna las elimina — depende del caso — Poquitas filas → drop; muchas → imputar. La mediana es robusta a outliers.

---
✅ Al terminar, marca la lección como completada en la app (📚 Aprender → ✅ Completada)
