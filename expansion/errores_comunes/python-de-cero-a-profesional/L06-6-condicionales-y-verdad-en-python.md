# ⚠️ Errores comunes — 6. Condicionales y verdad en Python

> Python — De Cero a Profesional · Lección 6 · Aprender de los errores (propios y ajenos)

- ❌ «Es más corto» → Frente a «if usuario is None — ¿por qué 'is' y no '=='?» lo fácil es confundirse. **Verdad**: None es singleton: se compara identidad; además is evita métodos __eq__ raros. None/True/False → is. Valores → ==
- ❌ «== no funciona con None» → Frente a «if usuario is None — ¿por qué 'is' y no '=='?» lo fácil es confundirse. **Verdad**: None es singleton: se compara identidad; además is evita métodos __eq__ raros. None/True/False → is. Valores → ==
- ❌ «Es falsy» → Frente a «¿Qué pasa con if [0]?» lo fácil es confundirse. **Verdad**: Es truthy (lista NO vacía aunque contenga 0). La verdad está en la ESTRUCTURA (vacía vs no), no en el contenido.
- ❌ «Error» → Frente a «¿Qué pasa con if [0]?» lo fácil es confundirse. **Verdad**: Es truthy (lista NO vacía aunque contenga 0). La verdad está en la ESTRUCTURA (vacía vs no), no en el contenido.

## 🩹 Antídoto universal
1. Lee el mensaje de error COMPLETO antes de googlear.
2. Pon el error exacto a la IA local y pide explicación, no solución.
3. Documenta el error en tu bitácora: error → causa → fix.
