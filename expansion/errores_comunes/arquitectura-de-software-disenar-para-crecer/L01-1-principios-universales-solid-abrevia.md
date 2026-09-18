# ⚠️ Errores comunes — 1. Principios universales: SOLID abreviado útil

> Arquitectura de Software — Diseñar para Crecer · Lección 1 · Aprender de los errores (propios y ajenos)

- ❌ «Borrar código» → Frente a «¿Qué propone DRY?» lo fácil es confundirse. **Verdad**: El conocimiento/lógica vive UNA sola vez en el sistema; repetición = inconsistencias cuando cambies un lugar y no otro. Copiar es rápido hoy; mantener copias divergentes es lento mañana.
- ❌ «Más tests» → Frente a «¿Qué propone DRY?» lo fácil es confundirse. **Verdad**: El conocimiento/lógica vive UNA sola vez en el sistema; repetición = inconsistencias cuando cambies un lugar y no otro. Copiar es rápido hoy; mantener copias divergentes es lento mañana.
- ❌ «No depender de nada» → Frente a «Dependency Inversion en práctica significa...» lo fácil es confundirse. **Verdad**: Tu lógica depende de INTERFACES/contratos; la implementación concreta se inyecta y puede cambiar (prod↔test). La pieza clave de testabilidad y arquitectura limpia: invierte quién controla las dependencias.
- ❌ «Java nada más» → Frente a «Dependency Inversion en práctica significa...» lo fácil es confundirse. **Verdad**: Tu lógica depende de INTERFACES/contratos; la implementación concreta se inyecta y puede cambiar (prod↔test). La pieza clave de testabilidad y arquitectura limpia: invierte quién controla las dependencias.

## 🩹 Antídoto universal
1. Lee el mensaje de error COMPLETO antes de googlear.
2. Pon el error exacto a la IA local y pide explicación, no solución.
3. Documenta el error en tu bitácora: error → causa → fix.
