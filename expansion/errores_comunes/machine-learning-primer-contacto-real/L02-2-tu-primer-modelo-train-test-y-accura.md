# ⚠️ Errores comunes — 2. Tu primer modelo: train/test y accuracy real

> Machine Learning — Primer Contacto Real · Lección 2 · Aprender de los errores (propios y ajenos)

- ❌ «Lo contrario» → Frente a «¿Qué hacen fit() y predict() en sklearn?» lo fácil es confundirse. **Verdad**: fit aprende de datos de ENTRENAMIENTO; predict va'ven predicciones sobre datos nuevos. API universal: instanciar modelo→fit(X_train, y)→predict(X) repite en toda sklearn.
- ❌ «Son de pandas» → Frente a «¿Qué hacen fit() y predict() en sklearn?» lo fácil es confundirse. **Verdad**: fit aprende de datos de ENTRENAMIENTO; predict va'ven predicciones sobre datos nuevos. API universal: instanciar modelo→fit(X_train, y)→predict(X) repite en toda sklearn.
- ❌ «Confundir al usuario» → Frente a «¿Para qué sirve la matriz de confusión?» lo fácil es confundirse. **Verdad**: Ver no solo AL error sino QUÉ se confunde con QUÉ: errores específicos por clase. Diagonal = aciertos; fuera de diagonal = confusiones específicas que guían mejora.
- ❌ «Medir tiempo» → Frente a «¿Para qué sirve la matriz de confusión?» lo fácil es confundirse. **Verdad**: Ver no solo AL error sino QUÉ se confunde con QUÉ: errores específicos por clase. Diagonal = aciertos; fuera de diagonal = confusiones específicas que guían mejora.

## 🩹 Antídoto universal
1. Lee el mensaje de error COMPLETO antes de googlear.
2. Pon el error exacto a la IA local y pide explicación, no solución.
3. Documenta el error en tu bitácora: error → causa → fix.
