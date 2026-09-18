# 3. Estadística descriptiva y grupos: los números de verdad

> 📚 Curso: **R y Estadística — El Idioma de los Datos** · Lección 3 de 4
> 🗓 Exportado: 18/09/2026 desde Plataforma Total
> 🍅 Sugerencia: 1-2 pomodoros para leer + practicar

---

## 📖 Contenido

```r
ESTADÍSTICA APLICADA EN 8 FUNCIONES
━━━━━━━━━━━━━━━━━━━━━━━━━━━
CENTRALIDAD Y DISPERSIÓN
  mean(x)      → media (sensible a outliers)
  median(x)    → mediana (robusta)
  sd(x)        → desviación estándar (qué tanto varía)
  var(x); range(x); quantile(x)
  IQR(x)       → rango intercuartílico (para boxplots/outliers)

  z <- (x - mean(x)) / sd(x)           → estandarizar (z-scores)
  cor(edad, ingresos)                   → correlación (-1 a 1)
  cor(x, y, method = "spearman")        → correlación por rangos (no lineal)

AGRUPAR Y RESUMIR (el group by de R)
  tapply(datos$edad, datos$pais, mean)      → media de edad por país
  aggregate(edad ~ pais, datos, mean)       → misma idea en data.frame
  # con dplyr (idyoma moderno): datos %>% group_by(pais) %>% summarise(media = mean(edad))

  table(datos$lenguaje)                 → conteo por categoría
  prop.table(table(x)) * 100            → porcentajes

PRUEBA T (comparativa básica):
  t.test(grupo_a, grupo_b) → te dice si las medias difieren significativamente (p-value)
```

---

## 📝 Quiz de la lección

### 1. ¿Qué mide sd(x)?
- A) La media
- B) La desviación estándar: cuánto se dispersan los datos respecto a la media
- C) La correlación
- D) El máximo
### 2. ¿Qué indica cor(edad, ingresos) = 0.8?
- A) Nada
- B) Correlación positiva FUERTE: a más edad, más ingresos (en esa muestra)
- C) Causalidad
- D) Un error

---

## 🔑 Respuestas y explicaciones

**1.** ✅ La desviación estándar: cuánto se dispersan los datos respecto a la media — sd pequeña = datos agrupados; sd grande = mucha variación. Clave en cualquier resumen.
**2.** ✅ Correlación positiva FUERTE: a más edad, más ingresos (en esa muestra) — Correlación NO es causalidad — pero descubrir 0.8 te dice dónde investigar.

---
✅ Al terminar, marca la lección como completada en la app (📚 Aprender → ✅ Completada)
