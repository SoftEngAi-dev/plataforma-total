# 15. Python para datos: tu primer análisis real

> 📚 Curso: **Python — De Cero a Profesional** · Lección 15 de 16
> 🗓 Exportado: 18/09/2026 desde Plataforma Total
> 🍅 Sugerencia: 1-2 pomodoros para leer + practicar

---

## 📖 Contenido

```python
PYTHON + DATOS: EL SUPERPODER LABORAL
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Escenario real: tienes ventas.csv:
  producto,precio,cantidad
  Café,120,3
  Pan,45,10

SIN PANDAS (stdlib pura, ENTIENDE primero esto):
  import csv
  with open("ventas.csv", encoding="utf-8") as f:
      for fila in csv.DictReader(f):                    # dicts: fila["producto"]
          print(fila["producto"], int(fila["cantidad"]))

CON PANDAS (el estándar):
  pip install pandas
  import pandas as pd
  df = pd.read_csv("ventas.csv")
  df.head()                      # primeras filas
  df["total"] = df["precio"] * df["cantidad"]      # columna calculada
  df.groupby("producto")["total"].sum()            # agrupar y sumar
  df.describe()                  # estadísticas automaticas

pandas = tablas (DataFrame) con operaciones vectorizadas: mucho más rápido y corto que loops.

MINI PROYECTO HOY: descarga cualquier CSV público (datos abiertos de tu país) y pregunta: ¿máximo, promedio, top 5?
```

---

## 📝 Quiz de la lección

### 1. ¿Qué hace csv.DictReader?
- A) Lee JSON
- B) Convierte cada fila del CSV en un dict usando el encabezado como claves
- C) Escribe CSV
- D) Ordena filas
### 2. df.groupby('producto')['total'].sum() hace...
- A) Filtra filas
- B) Agrupa por producto y suma el total de cada grupo
- C) Ordena por producto
- D) Crea tabla nueva

---

## 🔑 Respuestas y explicaciones

**1.** ✅ Convierte cada fila del CSV en un dict usando el encabezado como claves — fila['precio'] directo — parseo CSV robusto con nada instalado.
**2.** ✅ Agrupa por producto y suma el total de cada grupo — El GROUP BY de SQL, estilo pandas: resumir categorías en 1 línea.

---
✅ Al terminar, marca la lección como completada en la app (📚 Aprender → ✅ Completada)
