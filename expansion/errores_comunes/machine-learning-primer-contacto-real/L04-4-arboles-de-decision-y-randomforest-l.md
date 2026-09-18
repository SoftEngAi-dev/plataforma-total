# ⚠️ Errores comunes — 4. Árboles de decisión y RandomForest: los caballos de batalla

> Machine Learning — Primer Contacto Real · Lección 4 · Aprender de los errores (propios y ajenos)

- ❌ «Ninguna» → Frente a «¿Qué ventaja práctica tiene max_depth=3?» lo fácil es confundirse. **Verdad**: Limita la complejidad del árbol: techo de cristal al overfit (regularización por construcción). Árbol profundo = reglas sobreajustadas de poquitas muestras; poco profundo generaliza bien.
- ❌ «Más datos» → Frente a «¿Qué ventaja práctica tiene max_depth=3?» lo fácil es confundirse. **Verdad**: Limita la complejidad del árbol: techo de cristal al overfit (regularización por construcción). Árbol profundo = reglas sobreajustadas de poquitas muestras; poco profundo generaliza bien.
- ❌ «Velocidad» → Frente a «¿Qué te dice feature_importances_?» lo fácil es confundirse. **Verdad**: QUÉ VARIABLES pesan más en las decisiones del modelo: comprensión/explicación del negocio incluida. "Los 2 mejores predictores son..." directo del bosque: insights accionables.
- ❌ «Cardiología» → Frente a «¿Qué te dice feature_importances_?» lo fácil es confundirse. **Verdad**: QUÉ VARIABLES pesan más en las decisiones del modelo: comprensión/explicación del negocio incluida. "Los 2 mejores predictores son..." directo del bosque: insights accionables.

## 🩹 Antídoto universal
1. Lee el mensaje de error COMPLETO antes de googlear.
2. Pon el error exacto a la IA local y pide explicación, no solución.
3. Documenta el error en tu bitácora: error → causa → fix.
