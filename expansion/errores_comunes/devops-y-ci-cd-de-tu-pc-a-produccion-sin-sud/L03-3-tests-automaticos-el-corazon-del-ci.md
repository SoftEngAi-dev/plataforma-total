# ⚠️ Errores comunes — 3. Tests automáticos: el corazón del CI

> DevOps y CI/CD — De Tu PC a Producción Sin Sudor · Lección 3 · Aprender de los errores (propios y ajenos)

- ❌ «Es bonita» → Frente a «¿Por qué la pirámide tiene más tests unitarios que E2E?» lo fácil es confundirse. **Verdad**: Unitarios = rápidos, estables y baratos; E2E = lentos, frágiles y caros (manténlos pocos). La base ancha de unit tests cubre lógica; los pocos E2E verifican el cableado.
- ❌ «Unitarios son nuevos» → Frente a «¿Por qué la pirámide tiene más tests unitarios que E2E?» lo fácil es confundirse. **Verdad**: Unitarios = rápidos, estables y baratos; E2E = lentos, frágiles y caros (manténlos pocos). La base ancha de unit tests cubre lógica; los pocos E2E verifican el cableado.
- ❌ «assert» → Frente a «¿Qué debe evitar un test unitario?» lo fácil es confundirse. **Verdad**: Tocar red/BD/reloj reales (úsese mocks/fakes) para ser rápido, repetible y confiable. Un test que depende del internet es un test que fallará a las 3am cuando menos lo esperas.
- ❌ «Ejecutarse en CI» → Frente a «¿Qué debe evitar un test unitario?» lo fácil es confundirse. **Verdad**: Tocar red/BD/reloj reales (úsese mocks/fakes) para ser rápido, repetible y confiable. Un test que depende del internet es un test que fallará a las 3am cuando menos lo esperas.

## 🩹 Antídoto universal
1. Lee el mensaje de error COMPLETO antes de googlear.
2. Pon el error exacto a la IA local y pide explicación, no solución.
3. Documenta el error en tu bitácora: error → causa → fix.
