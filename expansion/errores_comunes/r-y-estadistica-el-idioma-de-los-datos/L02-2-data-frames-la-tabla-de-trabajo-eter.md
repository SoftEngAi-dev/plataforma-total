# ⚠️ Errores comunes — 2. Data frames: la tabla de trabajo eterna

> R y Estadística — El Idioma de los Datos · Lección 2 · Aprender de los errores (propios y ajenos)

- ❌ «Imprime todo» → Frente a «¿Qué hace summary(datos)? en R?» lo fácil es confundirse. **Verdad**: Resumen estadístico por columna (min/max/media/mediana/cuartiles): EDA gratis en una palabra. La primera vista a cualquier dataset: summary + str + head = inspección completa.
- ❌ «Borra» → Frente a «¿Qué hace summary(datos)? en R?» lo fácil es confundirse. **Verdad**: Resumen estadístico por columna (min/max/media/mediana/cuartiles): EDA gratis en una palabra. La primera vista a cualquier dataset: summary + str + head = inspección completa.
- ❌ «Error» → Frente a «datos[datos$edad > 40, ] — ¿qué hace la coma final?» lo fácil es confundirse. **Verdad**: Selecciona filas donde edad>40 y TODAS las columnas (el espacio tras la coma = todas las columnas). df[filas, columnas]: la coma vacía significa 'todas las columnas'.
- ❌ «Divide» → Frente a «datos[datos$edad > 40, ] — ¿qué hace la coma final?» lo fácil es confundirse. **Verdad**: Selecciona filas donde edad>40 y TODAS las columnas (el espacio tras la coma = todas las columnas). df[filas, columnas]: la coma vacía significa 'todas las columnas'.

## 🩹 Antídoto universal
1. Lee el mensaje de error COMPLETO antes de googlear.
2. Pon el error exacto a la IA local y pide explicación, no solución.
3. Documenta el error en tu bitácora: error → causa → fix.
