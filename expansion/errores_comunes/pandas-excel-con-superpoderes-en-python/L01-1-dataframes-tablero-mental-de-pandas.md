# ⚠️ Errores comunes — 1. DataFrames: tablero mental de pandas

> Pandas — Excel con Superpoderes en Python · Lección 1 · Aprender de los errores (propios y ajenos)

- ❌ «Error» → Frente a «¿Qué devuelve datos[datos['edad'] > 40]?» lo fácil es confundirse. **Verdad**: Filas del DataFrame donde la condición booleana es verdadera. Boolean indexing: la forma panda de decir 'WHERE edad > 40'.
- ❌ «Las edades» → Frente a «¿Qué devuelve datos[datos['edad'] > 40]?» lo fácil es confundirse. **Verdad**: Filas del DataFrame donde la condición booleana es verdadera. Boolean indexing: la forma panda de decir 'WHERE edad > 40'.
- ❌ «Son iguales» → Frente a «¿Cuándo usar datos.loc vs datos.iloc?» lo fácil es confundirse. **Verdad**: loc: por ETIQUETA/condición; iloc: por POSICIÓN de entero. loc[[2,3], ['a']] por nombre; iloc[0:2, 0] por posición. Ambos según el índice.
- ❌ «loc es de lectura» → Frente a «¿Cuándo usar datos.loc vs datos.iloc?» lo fácil es confundirse. **Verdad**: loc: por ETIQUETA/condición; iloc: por POSICIÓN de entero. loc[[2,3], ['a']] por nombre; iloc[0:2, 0] por posición. Ambos según el índice.

## 🩹 Antídoto universal
1. Lee el mensaje de error COMPLETO antes de googlear.
2. Pon el error exacto a la IA local y pide explicación, no solución.
3. Documenta el error en tu bitácora: error → causa → fix.
