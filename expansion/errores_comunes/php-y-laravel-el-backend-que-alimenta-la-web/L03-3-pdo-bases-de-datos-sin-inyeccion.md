# ⚠️ Errores comunes — 3. PDO: bases de datos sin inyección

> PHP y Laravel — El Backend Que Alimenta la Web · Lección 3 · Aprender de los errores (propios y ajenos)

- ❌ «La velocidad» → Frente a «¿Qué protegen los prepared statements?» lo fácil es confundirse. **Verdad**: SQL injection: los datos van apartados del SQL y nunca se interpretan como código. prepare() separa instrucción de datos: ' OR 1=1 -- queda como simple texto.
- ❌ «El código PHP» → Frente a «¿Qué protegen los prepared statements?» lo fácil es confundirse. **Verdad**: SQL injection: los datos van apartados del SQL y nunca se interpretan como código. prepare() separa instrucción de datos: ' OR 1=1 -- queda como simple texto.
- ❌ «XML» → Frente a «¿Qué PDO::FETCH_ASSOC devuelve?» lo fácil es confundirse. **Verdad**: Cada fila como array asociativo ['columna'=>valor]. Acceso por nombre de columna: código legible y resiliente.
- ❌ «Objetos siempre» → Frente a «¿Qué PDO::FETCH_ASSOC devuelve?» lo fácil es confundirse. **Verdad**: Cada fila como array asociativo ['columna'=>valor]. Acceso por nombre de columna: código legible y resiliente.

## 🩹 Antídoto universal
1. Lee el mensaje de error COMPLETO antes de googlear.
2. Pon el error exacto a la IA local y pide explicación, no solución.
3. Documenta el error en tu bitácora: error → causa → fix.
