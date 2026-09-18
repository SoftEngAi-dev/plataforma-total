# ⚠️ Errores comunes — 2. Pytest, Jest y asserts: la gramática universal

> Testing — Programar con Red de Seguridad · Lección 2 · Aprender de los errores (propios y ajenos)

- ❌ «AAA» → Frente a «¿Qué patrón AAA estructura un buen test?» lo fácil es confundirse. **Verdad**: Arrange (preparar datos) → Act (ejecutar lo probado) → Assert (verificar el resultado). Estructura legible y consistente: la legibilidad de los tests es deuda evitada.
- ❌ «3 tests» → Frente a «¿Qué patrón AAA estructura un buen test?» lo fácil es confundirse. **Verdad**: Arrange (preparar datos) → Act (ejecutar lo probado) → Assert (verificar el resultado). Estructura legible y consistente: la legibilidad de los tests es deuda evitada.
- ❌ «Lanza error en pytest» → Frente a «¿Qué hace pytest.raises(ValueError) en with?» lo fácil es confundirse. **Verdad**: Verifica que el código LANZA esa excepción concreta — test del comportamiento de error. Probar los caminos de error es tan importante (o más) que el camino feliz.
- ❌ «Mata el test» → Frente a «¿Qué hace pytest.raises(ValueError) en with?» lo fácil es confundirse. **Verdad**: Verifica que el código LANZA esa excepción concreta — test del comportamiento de error. Probar los caminos de error es tan importante (o más) que el camino feliz.

## 🩹 Antídoto universal
1. Lee el mensaje de error COMPLETO antes de googlear.
2. Pon el error exacto a la IA local y pide explicación, no solución.
3. Documenta el error en tu bitácora: error → causa → fix.
