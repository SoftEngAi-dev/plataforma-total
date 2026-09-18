# ⚠️ Errores comunes — 1. ML honesto: qué es y qué NO es

> Machine Learning — Primer Contacto Real · Lección 1 · Aprender de los errores (propios y ajenos)

- ❌ «Más datos siempre» → Frente a «¿Cuál es la REGLA SAGRADA del ML?» lo fácil es confundirse. **Verdad**: Evaluar en datos de TEST separados que el modelo nunca vio en entrenamiento. Sin test separado solo mides memoria, no capacidad de generalizar.
- ❌ «Usar más capas» → Frente a «¿Cuál es la REGLA SAGRADA del ML?» lo fácil es confundirse. **Verdad**: Evaluar en datos de TEST separados que el modelo nunca vio en entrenamiento. Sin test separado solo mides memoria, no capacidad de generalizar.
- ❌ «clasificación» → Frente a «Precio de una casa según m², zona, habitaciones es...» lo fácil es confundirse. **Verdad**: REGRESIÓN: predecir un NÚMERO (continuo), no una categoría. Regresión = número; clasificación = etiqueta/categoría. Letra chica que decide tu modelo.
- ❌ «clustering» → Frente a «Precio de una casa según m², zona, habitaciones es...» lo fácil es confundirse. **Verdad**: REGRESIÓN: predecir un NÚMERO (continuo), no una categoría. Regresión = número; clasificación = etiqueta/categoría. Letra chica que decide tu modelo.

## 🩹 Antídoto universal
1. Lee el mensaje de error COMPLETO antes de googlear.
2. Pon el error exacto a la IA local y pide explicación, no solución.
3. Documenta el error en tu bitácora: error → causa → fix.
