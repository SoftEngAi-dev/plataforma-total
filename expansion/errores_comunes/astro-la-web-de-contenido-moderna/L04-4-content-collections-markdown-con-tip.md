# ⚠️ Errores comunes — 4. Content Collections: Markdown con tipos

> 🚀 Astro — La Web de Contenido Moderna · Lección 4 · Aprender de los errores (propios y ajenos)

- ❌ «El CSS» → Frente a «¿Qué valida el esquema zod de una Content Collection?» lo fácil es confundirse. **Verdad**: El frontmatter de cada Markdown durante el build. Si un post incumple el esquema, el build falla: contenido corrupto nunca llega a producción.
- ❌ «Las llamadas HTTP» → Frente a «¿Qué valida el esquema zod de una Content Collection?» lo fácil es confundirse. **Verdad**: El frontmatter de cada Markdown durante el build. Si un post incumple el esquema, el build falla: contenido corrupto nunca llega a producción.
- ❌ «leyendo el directorio con fs» → Frente a «¿Cómo obtienes todas las entradas de la colección blog?» lo fácil es confundirse. **Verdad**: getCollection('blog'). getCollection devuelve las entradas tipadas; con entry.render() obtienes el HTML.
- ❌ «fetch('/api/blog')» → Frente a «¿Cómo obtienes todas las entradas de la colección blog?» lo fácil es confundirse. **Verdad**: getCollection('blog'). getCollection devuelve las entradas tipadas; con entry.render() obtienes el HTML.

## 🩹 Antídoto universal
1. Lee el mensaje de error COMPLETO antes de googlear.
2. Pon el error exacto a la IA local y pide explicación, no solución.
3. Documenta el error en tu bitácora: error → causa → fix.
