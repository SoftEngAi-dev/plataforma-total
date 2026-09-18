# ⚠️ Errores comunes — 3. Overfitting vs underfitting y validación

> Machine Learning — Primer Contacto Real · Lección 3 · Aprender de los errores (propios y ajenos)

- ❌ «Está perfecto» → Frente a «Train 99%, test 72%. ¿Diagnóstico?» lo fácil es confundirse. **Verdad**: OVERFIT: memorizó el entrenamiento, no generaliza — modelo demasiado complejo para los datos. La brecha train>>test es el síntoma canónico de sobreajuste.
- ❌ «Underfit» → Frente a «Train 99%, test 72%. ¿Diagnóstico?» lo fácil es confundirse. **Verdad**: OVERFIT: memorizó el entrenamiento, no generaliza — modelo demasiado complejo para los datos. La brecha train>>test es el síntoma canónico de sobreajuste.
- ❌ «Nada» → Frente a «¿Qué aporta cross_val_score(modelo, X, y, cv=5) sobre un solo split?» lo fácil es confundirse. **Verdad**: Evalúa 5 veces con particiones rotadas: medida mucho más estable y robusta de tu desempeño real. Un solo split puede tener suerte/mala suerte con qué datos tocaron: la CV promedia esa lotería.
- ❌ «Solo velocidad» → Frente a «¿Qué aporta cross_val_score(modelo, X, y, cv=5) sobre un solo split?» lo fácil es confundirse. **Verdad**: Evalúa 5 veces con particiones rotadas: medida mucho más estable y robusta de tu desempeño real. Un solo split puede tener suerte/mala suerte con qué datos tocaron: la CV promedia esa lotería.

## 🩹 Antídoto universal
1. Lee el mensaje de error COMPLETO antes de googlear.
2. Pon el error exacto a la IA local y pide explicación, no solución.
3. Documenta el error en tu bitácora: error → causa → fix.
