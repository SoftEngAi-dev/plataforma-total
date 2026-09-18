# ⚠️ Errores comunes — 3. Ordenar, limitar y funciones agregadas

> SQL y Bases de Datos — Datos que Persisten · Lección 3 · Aprender de los errores (propios y ajenos)

- ❌ «Columnas» → Frente a «¿Qué devuelve COUNT(*)?» lo fácil es confundirse. **Verdad**: Número TOTAL de filas (incluyendo nulos). COUNT(*) cuenta filas; COUNT(columna) omite las NULL.
- ❌ «Promedio» → Frente a «¿Qué devuelve COUNT(*)?» lo fácil es confundirse. **Verdad**: Número TOTAL de filas (incluyendo nulos). COUNT(*) cuenta filas; COUNT(columna) omite las NULL.
- ❌ «Los 5 más baratos» → Frente a «ORDER BY precio DESC LIMIT 5 OFFSET 10 devuelve...» lo fácil es confundirse. **Verdad**: Del puesto 11 al 15 en precio descendente. OFFSET salta las primeras N: base de la paginación de APIs y webs.
- ❌ «Todo menos 10» → Frente a «ORDER BY precio DESC LIMIT 5 OFFSET 10 devuelve...» lo fácil es confundirse. **Verdad**: Del puesto 11 al 15 en precio descendente. OFFSET salta las primeras N: base de la paginación de APIs y webs.

## 🩹 Antídoto universal
1. Lee el mensaje de error COMPLETO antes de googlear.
2. Pon el error exacto a la IA local y pide explicación, no solución.
3. Documenta el error en tu bitácora: error → causa → fix.
