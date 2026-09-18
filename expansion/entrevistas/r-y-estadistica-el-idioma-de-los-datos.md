# 🎤 Banco de entrevista — R y Estadística — El Idioma de los Datos

> 8 preguntas esenciales + guía de respuestas las que ya sabes del curso

## 🔥 Fundamentales (del contenido del curso)

1. **¿Qué hace edades[edades > 30]?**
   - Indexación lógica vectorizada: devuelve solo los elementos donde la condición es TRUE  _(Filtrar vectores con condiciones sin bucles: la elegancia R desde el día 1.)_

2. **¿En qué empiezan los índices de R?**
   - En 1 — viejos lenguajes científicos (R/MATLAB/Fortran) cuentan como humanos  _(Sorpresa clásica para quien viene de C/Python: edades[1] es el PRIMERO.)_

3. **¿Qué hace summary(datos)? en R?**
   - Resumen estadístico por columna (min/max/media/mediana/cuartiles): EDA gratis en una palabra  _(La primera vista a cualquier dataset: summary + str + head = inspección completa.)_

4. **datos[datos$edad > 40, ] — ¿qué hace la coma final?**
   - Selecciona filas donde edad>40 y TODAS las columnas (el espacio tras la coma = todas las columnas)  _(df[filas, columnas]: la coma vacía significa 'todas las columnas'.)_

5. **¿Qué mide sd(x)?**
   - La desviación estándar: cuánto se dispersan los datos respecto a la media  _(sd pequeña = datos agrupados; sd grande = mucha variación. Clave en cualquier resumen.)_

6. **¿Qué indica cor(edad, ingresos) = 0.8?**
   - Correlación positiva FUERTE: a más edad, más ingresos (en esa muestra)  _(Correlación NO es causalidad — pero descubrir 0.8 te dice dónde investigar.)_

7. **¿Qué hace na.omit(datos)?**
   - Elimina las filas que tengan algún NA (limpieza rápida)  _(Decisión simple de limpieza; en proyectos serios evalúa si imputar tiene más sentido.)_

8. **¿Cuál es el ORDEN mental correcto al analizar datos?**
   - Inspeccionar → preguntar → limpiar → resumir → visualizar → escribir conclusiones  _(El método importa: preguntas antes de números; conclusiones después de evidencias.)_

## 🧗 Profundización (prepáralas explicando en voz alta)
- ¿Qué problema real resuelve R y Estadística y cuándo NO lo usarías?
- Explica el concepto más fuerte del curso sin usar jerga.
- Contrasta R y Estadística con una alternativa: pros/contras.
- Cuenta un error típico de novato en este tema y cómo lo evitas.

## ⭐ Método para contestarlas
1. **Responde en 60 segundos** cada una de las fundamentales, de memoria. Las que tartamudean → repásalas (flashcards/).
2. Graba tu voz en 2 y escúchate: claridad y precisión importan tanto como el contenido técnico.
3. Una respuesta buena = definición (1 línea) + ejemplo (1) + por qué importa (1).
