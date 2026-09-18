# 4. Proyecto: tu primer análisis R real

> 📚 Curso: **R y Estadística — El Idioma de los Datos** · Lección 4 de 4
> 🗓 Exportado: 18/09/2026 desde Plataforma Total
> 🍅 Sugerencia: 1-2 pomodoros para leer + practicar

---

## 📖 Contenido

```r
CONSTRUYE: ANÁLISIS DE UN CSV REAL EN R
━━━━━━━━━━━━━━━━━━━━━━━━━━━
MISIÓN (60-90 min): descarga el dataset de pinguins o tu CSV favorito y domina el ciclo EDA completo.

1. CARGA + INSPECCIÓN
   datos <- read.csv("datos.csv"); str(datos); summary(datos); head(datos)
   ¿cuántas filas/columnas? ¿qué tipo es cada columna?
2. LIMPIEZA MÍNIMA
   sum(is.na(datos))              → cuántos NAs hay en total
   limpio <- na.omit(datos)       → elimina filas con NA (o decide imputar)
   names(limpio) <- tolower(names(limpio))   → columnas en minúsculas
3. PREGUNTAS DE NEGOCIO (escríbelas antes de mirar)
   - ¿Media y mediana? ¿y el rango (varianza)?
   - ¿Mejor categoría por agregados: tapply o aggregate?
   - ¿Correlación entre las dos columnas numéricas principales?
4. VISUALIZACIÓN RÁPIDA (base R)
   hist(limpio$edad, col = "skyblue", main = "Distribución de edades")
   boxplot(edad ~ categoria, data = limpio)
   plot(limpio$x, limpio$y); abline(lm(y ~ x, data = limpio), col = "red")
5. CONCLUSIÓN escrita: 3 hallazgos con números de apoyo en un informe Rmd o un .txt

LO QUE APRENDISTE = 60% del trabajo de un analista real: inspección → limpieza → resumen → visual → historia.
```

---

## 📝 Quiz de la lección

### 1. ¿Qué hace na.omit(datos)?
- A) Rellena NAs
- B) Elimina las filas que tengan algún NA (limpieza rápida)
- C) Crea NAs
- D) Nada
### 2. ¿Cuál es el ORDEN mental correcto al analizar datos?
- A) Graficar, limpiar, decidir
- B) Inspeccionar → preguntar → limpiar → resumir → visualizar → escribir conclusiones
- C) Código primero
- D) Modelo primero

---

## 🔑 Respuestas y explicaciones

**1.** ✅ Elimina las filas que tengan algún NA (limpieza rápida) — Decisión simple de limpieza; en proyectos serios evalúa si imputar tiene más sentido.
**2.** ✅ Inspeccionar → preguntar → limpiar → resumir → visualizar → escribir conclusiones — El método importa: preguntas antes de números; conclusiones después de evidencias.

---
✅ Al terminar, marca la lección como completada en la app (📚 Aprender → ✅ Completada)
