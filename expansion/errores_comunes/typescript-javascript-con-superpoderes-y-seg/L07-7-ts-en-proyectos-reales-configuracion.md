# ⚠️ Errores comunes — 7. TS en proyectos reales: configuración y flujo

> TypeScript — JavaScript con Superpoderes y Seguridad · Lección 7 · Aprender de los errores (propios y ajenos)

- ❌ «Solo chequeo básico» → Frente a «¿Qué activa "strict": true en tsconfig?» lo fácil es confundirse. **Verdad**: Una familia de protecciones: null checks, noImplicitAny, etc. — el modo serio de TS. Strict atrapa el grueso de los bugs de tipo. Proyecto profesional sin strict = medio TS.
- ❌ «Rápida ejecución» → Frente a «¿Qué activa "strict": true en tsconfig?» lo fácil es confundirse. **Verdad**: Una familia de protecciones: null checks, noImplicitAny, etc. — el modo serio de TS. Strict atrapa el grueso de los bugs de tipo. Proyecto profesional sin strict = medio TS.
- ❌ «No se puede» → Frente a «¿Cómo usar tipos con una librería JS como express?» lo fácil es confundirse. **Verdad**: npm i -D @types/express (definiciones de tipos de la comunidad). @types/* cubre todo el ecosistema popular: tu editor la entiende como si fuera TS nativa.
- ❌ «Reescribirla en TS» → Frente a «¿Cómo usar tipos con una librería JS como express?» lo fácil es confundirse. **Verdad**: npm i -D @types/express (definiciones de tipos de la comunidad). @types/* cubre todo el ecosistema popular: tu editor la entiende como si fuera TS nativa.

## 🩹 Antídoto universal
1. Lee el mensaje de error COMPLETO antes de googlear.
2. Pon el error exacto a la IA local y pide explicación, no solución.
3. Documenta el error en tu bitácora: error → causa → fix.
