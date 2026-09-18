# ⚠️ Errores comunes — 9. SQL con Python: sqlite3 práctico

> SQL y Bases de Datos — Datos que Persisten · Lección 9 · Aprender de los errores (propios y ajenos)

- ❌ «Las f-strings son lentas» → Frente a «¿Por qué usar ? (parámetros) y nunca f-strings en SQL?» lo fácil es confundirse. **Verdad**: Los parámetros previenen SQL injection: los datos jamás se interpretan como código. Con f-strings, un usuario malicioso escribe SQL dentro de tu consulta: el primer ataque web de la historia.
- ❌ «Son más cortos» → Frente a «¿Por qué usar ? (parámetros) y nunca f-strings en SQL?» lo fácil es confundirse. **Verdad**: Los parámetros previenen SQL injection: los datos jamás se interpretan como código. Con f-strings, un usuario malicioso escribe SQL dentro de tu consulta: el primer ataque web de la historia.
- ❌ «Autocommit» → Frente a «¿Qué aporta con.row_factory = sqlite3.Row?» lo fácil es confundirse. **Verdad**: Acceder a las columnas POR NOMBRE (fila['nombre']) en vez de índices. Código legible y resistente a cambios de orden de columnas.
- ❌ «Async» → Frente a «¿Qué aporta con.row_factory = sqlite3.Row?» lo fácil es confundirse. **Verdad**: Acceder a las columnas POR NOMBRE (fila['nombre']) en vez de índices. Código legible y resistente a cambios de orden de columnas.

## 🩹 Antídoto universal
1. Lee el mensaje de error COMPLETO antes de googlear.
2. Pon el error exacto a la IA local y pide explicación, no solución.
3. Documenta el error en tu bitácora: error → causa → fix.
