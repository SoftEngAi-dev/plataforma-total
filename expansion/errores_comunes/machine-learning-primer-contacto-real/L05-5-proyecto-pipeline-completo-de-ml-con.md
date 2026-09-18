# ⚠️ Errores comunes — 5. Proyecto: pipeline completo de ML con datos reales

> Machine Learning — Primer Contacto Real · Lección 5 · Aprender de los errores (propios y ajenos)

- ❌ «Las borra» → Frente a «¿Qué hace pd.get_dummies sobre columnas categóricas?» lo fácil es confundirse. **Verdad**: Convierte categorías en columnas binarias 0/1 para que el algoritmo procese números. Los modelos comen números: género/embarque/categorías → one-hot encoding.
- ❌ «Ordena» → Frente a «¿Qué hace pd.get_dummies sobre columnas categóricas?» lo fácil es confundirse. **Verdad**: Convierte categorías en columnas binarias 0/1 para que el algoritmo procese números. Los modelos comen números: género/embarque/categorías → one-hot encoding.
- ❌ «SQL» → Frente a «¿Qué es FEATURE ENGINEERING en este proyecto?» lo fácil es confundirse. **Verdad**: CREAR columnas útiles desde las existentes (ej: sol@ si viajas solo): el 40% de tu mejora suele vivir aquí. Pequeñas obviedades transformadas en datos = a veces más valor que elegir otro modelo.
- ❌ «Hype» → Frente a «¿Qué es FEATURE ENGINEERING en este proyecto?» lo fácil es confundirse. **Verdad**: CREAR columnas útiles desde las existentes (ej: sol@ si viajas solo): el 40% de tu mejora suele vivir aquí. Pequeñas obviedades transformadas en datos = a veces más valor que elegir otro modelo.

## 🩹 Antídoto universal
1. Lee el mensaje de error COMPLETO antes de googlear.
2. Pon el error exacto a la IA local y pide explicación, no solución.
3. Documenta el error en tu bitácora: error → causa → fix.
