# 4. Fechas, strings y aplicaciones avanzadas (los .dt/.str)

> 📚 Curso: **Pandas — Excel con Superpoderes en Python** · Lección 4 de 6
> 🗓 Exportado: 18/09/2026 desde Plataforma Total
> 🍅 Sugerencia: 1-2 pomodoros para leer + practicar

---

## 📖 Contenido

```python
SERIES CON SUPERPODERES: .dt, .str, .apply
━━━━━━━━━━━━━━━━━━━━━━━━━━━
FECHAS: convierte siempre a datetime primero
  df["fecha"] = pd.to_datetime(df["fecha"])
  df["anio"]  = df["fecha"].dt.year
  df["mes"]   = df["fecha"].dt.month
  df["dia_semana"] = df["fecha"].dt.day_name()
  df.groupby(df["fecha"].dt.to_period("M"))["total"].sum()   # ventas por mes elegantísimo
  rango = df[df["fecha"] >= "2026-01-01"]
  (df["entrega"] - df["compra"]).dt.days                      # duraciones calculadas as days

TEXTO (vectorizado sin loops)
  df["email"] = df["email"].str.lower().str.strip()
  df[df["nombre"].str.contains("silva", na=False)]
  df["dominio"] = df["email"].str.split("@").str[1]
  df["iniciales"] = df["nombre"].str[:2]                       # slice vectorizado

APPLY cuando no hay vector (lo justo y necesario)
  df["segmento"] = df["total"].apply(lambda t: "A" if t > 1000 else "B")
  df = df.assign(nuevo_total=lambda d: d.total * 1.22)       # encadenar sin inplace

REGLA PRO: columnas vectorizadas (.str/.dt/ops) EN VEZ de filas y loops: 10-100× más rápido.
```

---

## 📝 Quiz de la lección

### 1. ¿Qué permite df['fecha'].dt.month después de to_datetime?
- A) Nada
- B) Extraer partes de fecha (mes/año/día/nombre) VECTORIZADO sobre toda la columna
- C) Texto
- D) Índices
### 2. df['email'].str.contains('silva', na=False) — ¿por qué na=False?
- A) Decora
- B) contains con NA devuelve NA y rompe filtros booleanos: na=False lo maneja seguro
- C) Es más rápido
- D) Para mayúsculas

---

## 🔑 Respuestas y explicaciones

**1.** ✅ Extraer partes de fecha (mes/año/día/nombre) VECTORIZADO sobre toda la columna — El accesor .dt convierte fechas en datos analizables: estacionalidad, agrupar por mes...
**2.** ✅ contains con NA devuelve NA y rompe filtros booleanos: na=False lo maneja seguro — Detalle que evita un error común al filtrar strings con valores faltantes.

---
✅ Al terminar, marca la lección como completada en la app (📚 Aprender → ✅ Completada)
