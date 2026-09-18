# ⚠️ Errores comunes — 2. CSV, limpieza y transformación de columnas

> Pandas — Excel con Superpoderes en Python · Lección 2 · Aprender de los errores (propios y ajenos)

- ❌ «Suma todo» → Frente a «¿Qué hace df.isna().sum()?» lo fácil es confundirse. **Verdad**: Cuenta valores faltantes POR COLUMNA: la primera revisión de salud de un dataset. Antes de analizar: ¿cuántos huecos hay y dónde? Ahí decides tu estrategia de limpieza.
- ❌ «Borra NAs» → Frente a «¿Qué hace df.isna().sum()?» lo fácil es confundirse. **Verdad**: Cuenta valores faltantes POR COLUMNA: la primera revisión de salud de un dataset. Antes de analizar: ¿cuántos huecos hay y dónde? Ahí decides tu estrategia de limpieza.
- ❌ «Siempre dropna» → Frente a «¿fillna con la mediana vs dropna?» lo fácil es confundirse. **Verdad**: fillna conserva todas las filas imputando un valor neutro; dropna las elimina — depende del caso. Poquitas filas → drop; muchas → imputar. La mediana es robusta a outliers.
- ❌ «Ninguna diferencia» → Frente a «¿fillna con la mediana vs dropna?» lo fácil es confundirse. **Verdad**: fillna conserva todas las filas imputando un valor neutro; dropna las elimina — depende del caso. Poquitas filas → drop; muchas → imputar. La mediana es robusta a outliers.

## 🩹 Antídoto universal
1. Lee el mensaje de error COMPLETO antes de googlear.
2. Pon el error exacto a la IA local y pide explicación, no solución.
3. Documenta el error en tu bitácora: error → causa → fix.
