# ⚠️ Errores comunes — 4. Fechas, strings y aplicaciones avanzadas (los .dt/.str)

> Pandas — Excel con Superpoderes en Python · Lección 4 · Aprender de los errores (propios y ajenos)

- ❌ «Nada» → Frente a «¿Qué permite df['fecha'].dt.month después de to_datetime?» lo fácil es confundirse. **Verdad**: Extraer partes de fecha (mes/año/día/nombre) VECTORIZADO sobre toda la columna. El accesor .dt convierte fechas en datos analizables: estacionalidad, agrupar por mes...
- ❌ «Texto» → Frente a «¿Qué permite df['fecha'].dt.month después de to_datetime?» lo fácil es confundirse. **Verdad**: Extraer partes de fecha (mes/año/día/nombre) VECTORIZADO sobre toda la columna. El accesor .dt convierte fechas en datos analizables: estacionalidad, agrupar por mes...
- ❌ «Decora» → Frente a «df['email'].str.contains('silva', na=False) — ¿por qué na=False?» lo fácil es confundirse. **Verdad**: contains con NA devuelve NA y rompe filtros booleanos: na=False lo maneja seguro. Detalle que evita un error común al filtrar strings con valores faltantes.
- ❌ «Es más rápido» → Frente a «df['email'].str.contains('silva', na=False) — ¿por qué na=False?» lo fácil es confundirse. **Verdad**: contains con NA devuelve NA y rompe filtros booleanos: na=False lo maneja seguro. Detalle que evita un error común al filtrar strings con valores faltantes.

## 🩹 Antídoto universal
1. Lee el mensaje de error COMPLETO antes de googlear.
2. Pon el error exacto a la IA local y pide explicación, no solución.
3. Documenta el error en tu bitácora: error → causa → fix.
