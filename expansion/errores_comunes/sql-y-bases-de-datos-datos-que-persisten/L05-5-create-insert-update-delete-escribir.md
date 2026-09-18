# ⚠️ Errores comunes — 5. CREATE, INSERT, UPDATE, DELETE: escribir datos

> SQL y Bases de Datos — Datos que Persisten · Lección 5 · Aprender de los errores (propios y ajenos)

- ❌ «Es error de sintaxis» → Frente a «¿Por qué UPDATE sin WHERE es un desastre clásico?» lo fácil es confundirse. **Verdad**: Actualiza TODAS las filas de la tabla. Sin filtro = global: regla para la vida: escribe primero el WHERE... y después UPDATE/DELETE junto.
- ❌ «Es más lento» → Frente a «¿Por qué UPDATE sin WHERE es un desastre clásico?» lo fácil es confundirse. **Verdad**: Actualiza TODAS las filas de la tabla. Sin filtro = global: regla para la vida: escribe primero el WHERE... y después UPDATE/DELETE junto.
- ❌ «Decora» → Frente a «¿Qué gana poner NOT NULL y CHECK en CREATE TABLE?» lo fácil es confundirse. **Verdad**: La base de datos rechaza datos inválidos aunque bugs de la app los intenten insertar. La última línea de defensa de la calidad de datos está en el esquema.
- ❌ «Nada» → Frente a «¿Qué gana poner NOT NULL y CHECK en CREATE TABLE?» lo fácil es confundirse. **Verdad**: La base de datos rechaza datos inválidos aunque bugs de la app los intenten insertar. La última línea de defensa de la calidad de datos está en el esquema.

## 🩹 Antídoto universal
1. Lee el mensaje de error COMPLETO antes de googlear.
2. Pon el error exacto a la IA local y pide explicación, no solución.
3. Documenta el error en tu bitácora: error → causa → fix.
