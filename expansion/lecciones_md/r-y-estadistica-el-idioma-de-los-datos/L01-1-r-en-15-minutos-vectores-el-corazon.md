# 1. R en 15 minutos: vectores, el corazón

> 📚 Curso: **R y Estadística — El Idioma de los Datos** · Lección 1 de 4
> 🗓 Exportado: 18/09/2026 desde Plataforma Total
> 🍅 Sugerencia: 1-2 pomodoros para leer + practicar

---

## 📖 Contenido

```r
R: HECHO POR Y PARA ESTADÍSTICOS
━━━━━━━━━━━━━━━━━━━━━━━━━━━
R domina estadística/investigación/bioinformática. Todo son VECTORES (colecciones), las operaciones son vectorizadas.

  # hola.R — ejecuta: Rscript hola.R  (o RStudio: el IDE por excelencia)
  nombre <- "Ada"                    # <- es el operador de asignación (= también sirve)
  edades <- c(25, 30, 35, 40)        # c() = concatenate: el vector básico
  edades * 2                          # vectorizado: c(50, 60, 70, 80)
  edades + 10
  mean(edades)                        # 32.5  ← estadística de fábrica
  sum(edades); length(edades); max(edades)

  secuencias <- 1:10                  # 1..10
  seq(0, 100, by = 5)
  edades[1]                           # → 25 ¡LOS ÍNDICES EMPIEZAN EN 1!
  edades[2:4]                         # 30, 35, 40
  edades[edades > 28]                 # indexación lógica: c(30,35,40)

  edades2 <- c(27, 33)                # asignación c()
  mayores <- edades[edades >= 30]     # filtrar: el dedo es R: te acostumbras al <-

funciones: promedio <- function(x) { sum(x) / length(x) }
```

---

## 📝 Quiz de la lección

### 1. ¿Qué hace edades[edades > 30]?
- A) Error
- B) Indexación lógica vectorizada: devuelve solo los elementos donde la condición es TRUE
- C) Borra
- D) Ordena
### 2. ¿En qué empiezan los índices de R?
- A) En 0
- B) En 1 — viejos lenguajes científicos (R/MATLAB/Fortran) cuentan como humanos
- C) En -1
- D) Depende

---

## 🔑 Respuestas y explicaciones

**1.** ✅ Indexación lógica vectorizada: devuelve solo los elementos donde la condición es TRUE — Filtrar vectores con condiciones sin bucles: la elegancia R desde el día 1.
**2.** ✅ En 1 — viejos lenguajes científicos (R/MATLAB/Fortran) cuentan como humanos — Sorpresa clásica para quien viene de C/Python: edades[1] es el PRIMERO.

---
✅ Al terminar, marca la lección como completada en la app (📚 Aprender → ✅ Completada)
