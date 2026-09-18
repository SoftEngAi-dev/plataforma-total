# ⚠️ Errores comunes — 1. Tests: por qué son parte del código, no un extra

> Testing — Programar con Red de Seguridad · Lección 1 · Aprender de los errores (propios y ajenos)

- ❌ «Suerte» → Frente a «¿Qué te permite refactorizar sin miedo?» lo fácil es confundirse. **Verdad**: Una buena suite de tests: si rompes algo al refactor, un test grita al instante. El valor práctico nº1 de una suite: cambiar código con confianza.
- ❌ «ORM» → Frente a «¿Qué te permite refactorizar sin miedo?» lo fácil es confundirse. **Verdad**: Una buena suite de tests: si rompes algo al refactor, un test grita al instante. El valor práctico nº1 de una suite: cambiar código con confianza.
- ❌ «Es más rápido» → Frente a «¿Por qué un test no debe tocar internet/reloj reales?» lo fácil es confundirse. **Verdad**: Para ser RÁPIDO, REPETIBLE y CONFIABLE: mismo resultado siempre, en cualquier máquina, sin depender de afuera. Mocks/fakes sustituyen lo externo: tu test decide el comportamiento externo, no la red.
- ❌ «Solo en CI» → Frente a «¿Por qué un test no debe tocar internet/reloj reales?» lo fácil es confundirse. **Verdad**: Para ser RÁPIDO, REPETIBLE y CONFIABLE: mismo resultado siempre, en cualquier máquina, sin depender de afuera. Mocks/fakes sustituyen lo externo: tu test decide el comportamiento externo, no la red.

## 🩹 Antídoto universal
1. Lee el mensaje de error COMPLETO antes de googlear.
2. Pon el error exacto a la IA local y pide explicación, no solución.
3. Documenta el error en tu bitácora: error → causa → fix.
