# ⚠️ Errores comunes — 2. Tipos básicos y anotaciones

> TypeScript — JavaScript con Superpoderes y Seguridad · Lección 2 · Aprender de los errores (propios y ajenos)

- ❌ «En TODAS las variables» → Frente a «¿Cuándo anotar tipos explícitamente?» lo fácil es confundirse. **Verdad**: Cuando la inferencia no es obvia (y siempre en firmas de funciones públicas). TS infiere en la asignación; anota donde el contrato importa.
- ❌ «Nunca» → Frente a «¿Cuándo anotar tipos explícitamente?» lo fácil es confundirse. **Verdad**: Cuando la inferencia no es obvia (y siempre en firmas de funciones públicas). TS infiere en la asignación; anota donde el contrato importa.
- ❌ «Ninguna» → Frente a «¿Qué diferencia hay entre any y unknown?» lo fácil es confundirse. **Verdad**: any desactiva toda verificación; unknown exige comprobar el tipo antes de usarlo. unknown = 'no sé aún, pero TS me protege'; any = 'ríndete, compilador'.
- ❌ «unknown es más corto» → Frente a «¿Qué diferencia hay entre any y unknown?» lo fácil es confundirse. **Verdad**: any desactiva toda verificación; unknown exige comprobar el tipo antes de usarlo. unknown = 'no sé aún, pero TS me protege'; any = 'ríndete, compilador'.

## 🩹 Antídoto universal
1. Lee el mensaje de error COMPLETO antes de googlear.
2. Pon el error exacto a la IA local y pide explicación, no solución.
3. Documenta el error en tu bitácora: error → causa → fix.
