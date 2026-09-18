# ⚠️ Errores comunes — 10. map, filter, reduce: programar sin bucles

> JavaScript — De Cero a Experto · Lección 10 · Aprender de los errores (propios y ajenos)

- ❌ «6» → Frente a «¿Qué devuelve [2,4,6].filter(n => n > 3)?» lo fácil es confundirse. **Verdad**: [4, 6]. filter conserva los que cumplen la condición.
- ❌ «2» → Frente a «¿Qué devuelve [2,4,6].filter(n => n > 3)?» lo fácil es confundirse. **Verdad**: [4, 6]. filter conserva los que cumplen la condición.
- ❌ «Nada, decorativo» → Frente a «¿Qué hace el segundo argumento de reduce?» lo fácil es confundirse. **Verdad**: Es el valor inicial del acumulador. Sin valor inicial, reduce usa el primer elemento — que a veces es sorpresa. Escribe siempre el inicial.
- ❌ «Es el límite de iteraciones» → Frente a «¿Qué hace el segundo argumento de reduce?» lo fácil es confundirse. **Verdad**: Es el valor inicial del acumulador. Sin valor inicial, reduce usa el primer elemento — que a veces es sorpresa. Escribe siempre el inicial.

## 🩹 Antídoto universal
1. Lee el mensaje de error COMPLETO antes de googlear.
2. Pon el error exacto a la IA local y pide explicación, no solución.
3. Documenta el error en tu bitácora: error → causa → fix.
