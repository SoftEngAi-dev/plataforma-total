# 3. groupby y agregaciones: análisis de negocio directo

> 📚 Curso: **Pandas — Excel con Superpoderes en Python** · Lección 3 de 6
> 🗓 Exportado: 18/09/2026 desde Plataforma Total
> 🍅 Sugerencia: 1-2 pomodoros para leer + practicar

---

## 📖 Contenido

```python
GROUPBY: RESUMIR = ENTENDER
━━━━━━━━━━━━━━━━━━━━━━━━━━━
  # ¿cómo va cada categoría?
  resumen = df.groupby("categoria")["total"].sum()
  # varias estadísticas a la vez:
  agg = df.groupby("categoria").agg(
      ventas_total=("total", "sum"),
      promedio=("total", "mean"),
      operaciones=("total", "count"),
      mejor=("total", "max"),
  ).reset_index()

  df.groupby(["categoria", "mes"])["total"].sum()     # multi-grupo → MultiIndex
  .unstack()                                          # pivota: filas→columnas

  df["categoria"].value_counts()        # conteo rápido por valor (MÁS usado del mundo)

  pd.pivot_table(df, values="total", index="categoria", columns="mes", aggfunc="sum", fill_value=0)

MERGE/JOIN como SQL (combiñar tablas por clave):
  pd.merge(ventas, clientes, on="cliente_id", how="left")   # how: inner/left/right/outer
  pd.concat([df1, df2])                                      # apilar filas

MEJOR = nombre de columna + función con tupla (columñas nombradas, salida legible) — estándar moderno.
```

---

## 📝 Quiz de la lección

### 1. ¿Qué hace df['categoria'].value_counts()?
- A) Ordena
- B) Cuenta frecuencia de cada valor: la vía rápida de 'top categorías' sin SQL
- C) Exporta
- D) CSV
### 2. pd.merge(a, b, on='id', how='left') se comporta como...
- A) concatenar
- B) LEFT JOIN de SQL: todas las filas de 'a' + datos de 'b' cuando hay coincidencia en id
- C) UNION
- D) nada

---

## 🔑 Respuestas y explicaciones

**1.** ✅ Cuenta frecuencia de cada valor: la vía rápida de 'top categorías' sin SQL — El one-liner favorito: en 1 llamada tienes el panorama categorial más común.
**2.** ✅ LEFT JOIN de SQL: todas las filas de 'a' + datos de 'b' cuando hay coincidencia en id — merge=JOIN entre DataFrames por clave; how decide qué filas sobreviven.

---
✅ Al terminar, marca la lección como completada en la app (📚 Aprender → ✅ Completada)
