# ⚠️ Errores comunes — 3. groupby y agregaciones: análisis de negocio directo

> Pandas — Excel con Superpoderes en Python · Lección 3 · Aprender de los errores (propios y ajenos)

- ❌ «Ordena» → Frente a «¿Qué hace df['categoria'].value_counts()?» lo fácil es confundirse. **Verdad**: Cuenta frecuencia de cada valor: la vía rápida de 'top categorías' sin SQL. El one-liner favorito: en 1 llamada tienes el panorama categorial más común.
- ❌ «Exporta» → Frente a «¿Qué hace df['categoria'].value_counts()?» lo fácil es confundirse. **Verdad**: Cuenta frecuencia de cada valor: la vía rápida de 'top categorías' sin SQL. El one-liner favorito: en 1 llamada tienes el panorama categorial más común.
- ❌ «concatenar» → Frente a «pd.merge(a, b, on='id', how='left') se comporta como...» lo fácil es confundirse. **Verdad**: LEFT JOIN de SQL: todas las filas de 'a' + datos de 'b' cuando hay coincidencia en id. merge=JOIN entre DataFrames por clave; how decide qué filas sobreviven.
- ❌ «UNION» → Frente a «pd.merge(a, b, on='id', how='left') se comporta como...» lo fácil es confundirse. **Verdad**: LEFT JOIN de SQL: todas las filas de 'a' + datos de 'b' cuando hay coincidencia en id. merge=JOIN entre DataFrames por clave; how decide qué filas sobreviven.

## 🩹 Antídoto universal
1. Lee el mensaje de error COMPLETO antes de googlear.
2. Pon el error exacto a la IA local y pide explicación, no solución.
3. Documenta el error en tu bitácora: error → causa → fix.
