# 1. DataFrames: tablero mental de pandas

> 📚 Curso: **Pandas — Excel con Superpoderes en Python** · Lección 1 de 6
> 🗓 Exportado: 18/09/2026 desde Plataforma Total
> 🍅 Sugerencia: 1-2 pomodoros para leer + practicar

---

## 📖 Contenido

```python
PANDAS EN UNA PÁGINA
━━━━━━━━━━━━━━━━━━━━━━━━━━━
  import pandas as pd              (pip install pandas)

  # Serie (una columna con índice) y DataFrame (tabla completa)
  edades = pd.Series([25, 30, 35], name="edad")
  datos = pd.DataFrame({
      "nombre": ["Ada", "Grace", "Marie"],
      "edad": [36, 85, 60],
      "pais": ["UK", "US", "FR"],
  })

  datos.head()          → primeras 5 filas     datos.tail(2)
  datos.shape           → (3, 3)                datos.columns
  datos.dtypes          → tipos por columna
  datos.info()          → resumen de tipos/nulls/memoria
  datos.describe()      → estadística descriptiva de numéricas (count/mean/std/min/quartiles/max)

SELECCIÓN (las dos grandes)
  datos["edad"]               → columna como Serie
  datos[["nombre", "edad"]]   → sub-DataFrame
  datos.iloc[0]               → primera fila POR POSICIÓN
  datos.loc[0, "nombre"]      → fila/etiqueta + columna (loc = labels, iloc = posiciones)

FILTRO (el corazón del análisis)
  datos[datos["edad"] > 40]                           → 2 filas
  datos[(datos.edad > 30) & (datos.pais == "US")]     → &/| con paréntesis obligatorios
  datos[datos.pais.isin(["UK", "FR"])]                → útil
```

---

## 📝 Quiz de la lección

### 1. ¿Qué devuelve datos[datos['edad'] > 40]?
- A) Error
- B) Filas del DataFrame donde la condición booleana es verdadera
- C) Las edades
- D) Nada
### 2. ¿Cuándo usar datos.loc vs datos.iloc?
- A) Son iguales
- B) loc: por ETIQUETA/condición; iloc: por POSICIÓN de entero
- C) loc es de lectura
- D) iloc es más nuevo

---

## 🔑 Respuestas y explicaciones

**1.** ✅ Filas del DataFrame donde la condición booleana es verdadera — Boolean indexing: la forma panda de decir 'WHERE edad > 40'.
**2.** ✅ loc: por ETIQUETA/condición; iloc: por POSICIÓN de entero — loc[[2,3], ['a']] por nombre; iloc[0:2, 0] por posición. Ambos según el índice.

---
✅ Al terminar, marca la lección como completada en la app (📚 Aprender → ✅ Completada)
