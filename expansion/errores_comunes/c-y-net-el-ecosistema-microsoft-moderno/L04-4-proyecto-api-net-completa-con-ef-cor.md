# ⚠️ Errores comunes — 4. Proyecto: API .NET completa con EF Core

> C# y .NET — El Ecosistema Microsoft Moderno · Lección 4 · Aprender de los errores (propios y ajenos)

- ❌ «new global» → Frente a «¿Cómo recibe el endpoint la instancia AppDb?» lo fácil es confundirse. **Verdad**: Inyección de dependencias automática: declaras (AppDb db) en la firma y .NET la entrega. DI integrada en Minimal APIs: efímero por petición, manejo del ciclo por ti.
- ❌ «Static» → Frente a «¿Cómo recibe el endpoint la instancia AppDb?» lo fácil es confundirse. **Verdad**: Inyección de dependencias automática: declaras (AppDb db) en la firma y .NET la entrega. DI integrada en Minimal APIs: efímero por petición, manejo del ciclo por ti.
- ❌ «SQL crudo» → Frente a «¿Qué hace FindAsync(id)?» lo fácil es confundirse. **Verdad**: Busca por clave primaria devolviendo el objeto o null si no existe. La operación básica de lectura-por-id en EF Core — el orElse NotFound a continuación es el patrón.
- ❌ «Borra» → Frente a «¿Qué hace FindAsync(id)?» lo fácil es confundirse. **Verdad**: Busca por clave primaria devolviendo el objeto o null si no existe. La operación básica de lectura-por-id en EF Core — el orElse NotFound a continuación es el patrón.

## 🩹 Antídoto universal
1. Lee el mensaje de error COMPLETO antes de googlear.
2. Pon el error exacto a la IA local y pide explicación, no solución.
3. Documenta el error en tu bitácora: error → causa → fix.
