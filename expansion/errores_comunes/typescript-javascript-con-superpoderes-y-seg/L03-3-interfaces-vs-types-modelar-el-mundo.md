# ⚠️ Errores comunes — 3. Interfaces vs Types: modelar el mundo

> TypeScript — JavaScript con Superpoderes y Seguridad · Lección 3 · Aprender de los errores (propios y ajenos)

- ❌ «Siempre» → Frente a «¿Cuándo elegir interface sobre type?» lo fácil es confundirse. **Verdad**: Para formas de objetos: más legible, mensajes de error claros y extensión natural. Interface para modelos de dominio; type para uniones y composiciones.
- ❌ «Nunca» → Frente a «¿Cuándo elegir interface sobre type?» lo fácil es confundirse. **Verdad**: Para formas de objetos: más legible, mensajes de error claros y extensión natural. Interface para modelos de dominio; type para uniones y composiciones.
- ❌ «Un objeto» → Frente a «¿Qué expresa type Estado = "cargando" | "ok" | "error"?» lo fácil es confundirse. **Verdad**: Una unión de literales: la variable solo vale uno de esos strings. Uniones de literales = estados exhaustivos que TS puede verificar (sin strings sueltos).
- ❌ «Un enum numérico» → Frente a «¿Qué expresa type Estado = "cargando" | "ok" | "error"?» lo fácil es confundirse. **Verdad**: Una unión de literales: la variable solo vale uno de esos strings. Uniones de literales = estados exhaustivos que TS puede verificar (sin strings sueltos).

## 🩹 Antídoto universal
1. Lee el mensaje de error COMPLETO antes de googlear.
2. Pon el error exacto a la IA local y pide explicación, no solución.
3. Documenta el error en tu bitácora: error → causa → fix.
