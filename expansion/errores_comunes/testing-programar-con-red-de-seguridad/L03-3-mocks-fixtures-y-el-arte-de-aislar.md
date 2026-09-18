# ⚠️ Errores comunes — 3. Mocks, fixtures y el arte de aislar

> Testing — Programar con Red de Seguridad · Lección 3 · Aprender de los errores (propios y ajenos)

- ❌ «Siempre» → Frente a «¿Cuándo usar mock?» lo fácil es confundirse. **Verdad**: Cuando tu función llama a algo EXTERNO (red/BD/tiempo) y quieres probar solo tu lógica con respuestas controladas. El mock convierte tu entorno en laboratorio: mismos datos, siempre, instantáneo.
- ❌ «Nunca» → Frente a «¿Cuándo usar mock?» lo fácil es confundirse. **Verdad**: Cuando tu función llama a algo EXTERNO (red/BD/tiempo) y quieres probar solo tu lógica con respuestas controladas. El mock convierte tu entorno en laboratorio: mismos datos, siempre, instantáneo.
- ❌ «Nada» → Frente a «¿Qué reutiliza una fixture de pytest?» lo fácil es confundirse. **Verdad**: La preparación compartida entre muchos tests (datos de prueba, conexiones, objetos complejos). Fixture = DRY aplicado a tests: un usuario demo se define una vez y todos lo usan.
- ❌ «El modal» → Frente a «¿Qué reutiliza una fixture de pytest?» lo fácil es confundirse. **Verdad**: La preparación compartida entre muchos tests (datos de prueba, conexiones, objetos complejos). Fixture = DRY aplicado a tests: un usuario demo se define una vez y todos lo usan.

## 🩹 Antídoto universal
1. Lee el mensaje de error COMPLETO antes de googlear.
2. Pon el error exacto a la IA local y pide explicación, no solución.
3. Documenta el error en tu bitácora: error → causa → fix.
