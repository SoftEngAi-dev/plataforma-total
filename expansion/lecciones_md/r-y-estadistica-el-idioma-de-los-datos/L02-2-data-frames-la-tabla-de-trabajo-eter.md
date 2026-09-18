# 2. Data frames: la tabla de trabajo eterna

> 📚 Curso: **R y Estadística — El Idioma de los Datos** · Lección 2 de 4
> 🗓 Exportado: 18/09/2026 desde Plataforma Total
> 🍅 Sugerencia: 1-2 pomodoros para leer + practicar

---

## 📖 Contenido

```r
DATA.FRAME: EL EXCEL DE R
━━━━━━━━━━━━━━━━━━━━━━━━━━━
  datos <- data.frame(
      nombre  = c("Ada", "Grace", "Marie"),
      edad    = c(36, 85, 60),
      lenguaje = c("COBOL", "COBOL", "Física")   # ejemplo libre
  )
  datos$nombre           → vector columna
  datos[1, ]             → primera FILA
  datos[, "edad"]        → columna por nombre
  datos$edad[2]          → 85
  nrow(datos); ncol(datos); names(datos)
  summary(datos)          → estadísticas por columna ¡incluido de fábrica!
  head(datos, 2)          → primeras 2 filas (tail = últimas)

AGREGAR/FILTRAR
  datos$pais <- c("UK", "US", "FR")              # columna nueva al vuelo
  adultos <- datos[datos$edad > 40, ]            # filtra filas (coma recuerda fuera)
  subset(datos, edad > 40)                       # alternativa legible

LEER CSV REAL (la base del análisis real):
  ventas <- read.csv("ventas.csv")
  str(ventas)            → tipos de cada columna (muyst útil)
  View(ventas)           → visor tipo hoja en RStudio

EXPORTAR: write.csv(datos, "salida.csv", row.names = FALSE)
```

---

## 📝 Quiz de la lección

### 1. ¿Qué hace summary(datos)? en R?
- A) Imprime todo
- B) Resumen estadístico por columna (min/max/media/mediana/cuartiles): EDA gratis en una palabra
- C) Borra
- D) Ordena
### 2. datos[datos$edad > 40, ] — ¿qué hace la coma final?
- A) Error
- B) Selecciona filas donde edad>40 y TODAS las columnas (el espacio tras la coma = todas las columnas)
- C) Divide
- D) Nada

---

## 🔑 Respuestas y explicaciones

**1.** ✅ Resumen estadístico por columna (min/max/media/mediana/cuartiles): EDA gratis en una palabra — La primera vista a cualquier dataset: summary + str + head = inspección completa.
**2.** ✅ Selecciona filas donde edad>40 y TODAS las columnas (el espacio tras la coma = todas las columnas) — df[filas, columnas]: la coma vacía significa 'todas las columnas'.

---
✅ Al terminar, marca la lección como completada en la app (📚 Aprender → ✅ Completada)
