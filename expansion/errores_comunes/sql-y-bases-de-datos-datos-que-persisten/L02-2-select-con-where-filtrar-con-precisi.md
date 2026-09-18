# ⚠️ Errores comunes — 2. SELECT con WHERE: filtrar con precisión

> SQL y Bases de Datos — Datos que Persisten · Lección 2 · Aprender de los errores (propios y ajenos)

- ❌ «campo = NULL» → Frente a «¿Cómo verificar si un campo es NULL?» lo fácil es confundirse. **Verdad**: campo IS NULL. NULL no es un valor; solo IS NULL funciona — bug clásico en todo el mundo.
- ❌ «campo == NULL» → Frente a «¿Cómo verificar si un campo es NULL?» lo fácil es confundirse. **Verdad**: campo IS NULL. NULL no es un valor; solo IS NULL funciona — bug clásico en todo el mundo.
- ❌ «Nombres que terminan en Ana» → Frente a «SELECT * FROM empleados WHERE nombre LIKE 'Ana%' busca...» lo fácil es confundirse. **Verdad**: Nombres que EMPIEZAN por Ana ( % = comodín de caracteres). % sustituye cualquier secuencia; Ana% = empieza por.
- ❌ «Exactamente 'Ana%'» → Frente a «SELECT * FROM empleados WHERE nombre LIKE 'Ana%' busca...» lo fácil es confundirse. **Verdad**: Nombres que EMPIEZAN por Ana ( % = comodín de caracteres). % sustituye cualquier secuencia; Ana% = empieza por.

## 🩹 Antídoto universal
1. Lee el mensaje de error COMPLETO antes de googlear.
2. Pon el error exacto a la IA local y pide explicación, no solución.
3. Documenta el error en tu bitácora: error → causa → fix.
