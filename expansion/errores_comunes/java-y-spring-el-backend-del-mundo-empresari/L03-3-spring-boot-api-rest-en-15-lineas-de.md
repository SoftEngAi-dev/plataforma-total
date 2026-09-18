# ⚠️ Errores comunes — 3. Spring Boot: API REST en 15 líneas de verdad

> Java y Spring — El Backend del Mundo Empresarial · Lección 3 · Aprender de los errores (propios y ajenos)

- ❌ «Decora» → Frente a «¿Qué hace @RestController?» lo fácil es confundirse. **Verdad**: Declara la clase como controlador web: los métodos responden HTTP y devuelven datos serializados (JSON). @RestController = @Controller + @ResponseBody: todo método = respuesta JSON directa.
- ❌ «Conecta BD» → Frente a «¿Qué hace @RestController?» lo fácil es confundirse. **Verdad**: Declara la clase como controlador web: los métodos responden HTTP y devuelven datos serializados (JSON). @RestController = @Controller + @ResponseBody: todo método = respuesta JSON directa.
- ❌ «SQL» → Frente a «¿Qué es inyección de dependencias en Spring?» lo fácil es confundirse. **Verdad**: El framework crea y entrega los objetos que necesita tu clase por el constructor: cambiar implementación sin tocar tu código. Recibes lo que necesitas; no lo construyes: testeo con mocks y evolución sin drama.
- ❌ «Npm install» → Frente a «¿Qué es inyección de dependencias en Spring?» lo fácil es confundirse. **Verdad**: El framework crea y entrega los objetos que necesita tu clase por el constructor: cambiar implementación sin tocar tu código. Recibes lo que necesitas; no lo construyes: testeo con mocks y evolución sin drama.

## 🩹 Antídoto universal
1. Lee el mensaje de error COMPLETO antes de googlear.
2. Pon el error exacto a la IA local y pide explicación, no solución.
3. Documenta el error en tu bitácora: error → causa → fix.
