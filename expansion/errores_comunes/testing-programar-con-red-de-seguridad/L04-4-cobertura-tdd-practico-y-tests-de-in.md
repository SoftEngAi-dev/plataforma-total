# ⚠️ Errores comunes — 4. Cobertura, TDD práctico y tests de integración

> Testing — Programar con Red de Seguridad · Lección 4 · Aprender de los errores (propios y ajenos)

- ❌ «Comentarios» → Frente a «¿Cuál es la mejor forma de evitar que un bug VUELVA?» lo fácil es confundirse. **Verdad**: Escribir PRIMERO el test que reproduce el bug: queda eternamente verificado en la suite. Bug→test rojo→fix→test verde= la regresión muere definitivamente.
- ❌ «Code review» → Frente a «¿Cuál es la mejor forma de evitar que un bug VUELVA?» lo fácil es confundirse. **Verdad**: Escribir PRIMERO el test que reproduce el bug: queda eternamente verificado en la suite. Bug→test rojo→fix→test verde= la regresión muere definitivamente.
- ❌ «Ninguna» → Frente a «¿Qué diferencia test E2E de integración?» lo fácil es confundirse. **Verdad**: E2E = flujo de usuario REAL completo (browser/UI); integración = componentes juntos sin UI necesariamente. Pocos E2E (frágiles/lentos pero definitivos): el pico de la pirámide.
- ❌ «E2E es más rápido» → Frente a «¿Qué diferencia test E2E de integración?» lo fácil es confundirse. **Verdad**: E2E = flujo de usuario REAL completo (browser/UI); integración = componentes juntos sin UI necesariamente. Pocos E2E (frágiles/lentos pero definitivos): el pico de la pirámide.

## 🩹 Antídoto universal
1. Lee el mensaje de error COMPLETO antes de googlear.
2. Pon el error exacto a la IA local y pide explicación, no solución.
3. Documenta el error en tu bitácora: error → causa → fix.
