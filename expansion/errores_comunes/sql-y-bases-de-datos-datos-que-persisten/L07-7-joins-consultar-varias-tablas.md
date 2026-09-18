# ⚠️ Errores comunes — 7. JOINs: consultar varias tablas

> SQL y Bases de Datos — Datos que Persisten · Lección 7 · Aprender de los errores (propios y ajenos)

- ❌ «Todos los de la derecha» → Frente a «¿Qué registros incluye LEFT JOIN que INNER no?» lo fácil es confundirse. **Verdad**: Los de la tabla izquierda sin coincidencia (con NULLs en la derecha). LEFT preserva el lado izquierdo completo: ideal para 'X con o sin Y'.
- ❌ «Duplicados» → Frente a «¿Qué registros incluye LEFT JOIN que INNER no?» lo fácil es confundirse. **Verdad**: Los de la tabla izquierda sin coincidencia (con NULLs en la derecha). LEFT preserva el lado izquierdo completo: ideal para 'X con o sin Y'.
- ❌ «Error» → Frente a «SELECT COUNT(l.id) con LEFT JOIN + GROUP BY autor da 0 cuando...» lo fácil es confundirse. **Verdad**: El autor no tiene libros (las NULL no se cuentan en COUNT). COUNT(columna) no cuenta NULLs: encaja perfecto con LEFT JOIN para conteos con cero.
- ❌ «El join falló» → Frente a «SELECT COUNT(l.id) con LEFT JOIN + GROUP BY autor da 0 cuando...» lo fácil es confundirse. **Verdad**: El autor no tiene libros (las NULL no se cuentan en COUNT). COUNT(columna) no cuenta NULLs: encaja perfecto con LEFT JOIN para conteos con cero.

## 🩹 Antídoto universal
1. Lee el mensaje de error COMPLETO antes de googlear.
2. Pon el error exacto a la IA local y pide explicación, no solución.
3. Documenta el error en tu bitácora: error → causa → fix.
