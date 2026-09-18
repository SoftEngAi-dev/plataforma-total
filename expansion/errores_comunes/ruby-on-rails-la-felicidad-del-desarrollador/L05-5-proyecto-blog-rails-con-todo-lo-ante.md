# ⚠️ Errores comunes — 5. Proyecto: blog Rails con todo lo anterior

> Ruby on Rails — La Felicidad del Desarrollador · Lección 5 · Aprender de los errores (propios y ajenos)

- ❌ «CSS» → Frente a «¿Para qué sirve un scope en el modelo Rails?» lo fácil es confundirse. **Verdad**: Guardar consultas frecuentes como métodos reutilizables: Post.publicados. Scope = query con nombre: lisible y combinables (Post.publicados.recientes).
- ❌ «Índices BD» → Frente a «¿Para qué sirve un scope en el modelo Rails?» lo fácil es confundirse. **Verdad**: Guardar consultas frecuentes como métodos reutilizables: Post.publicados. Scope = query con nombre: lisible y combinables (Post.publicados.recientes).
- ❌ «Nada» → Frente a «AddAutor a posts con autor:references en migración hace...» lo fácil es confundirse. **Verdad**: Crea la columna autor_id + índice + FK en la tabla posts (relación completa en SQL). Las migraciones versionan tu esquema en código: la BD se recrea con rails db:migrate.
- ❌ «Crea un modelo» → Frente a «AddAutor a posts con autor:references en migración hace...» lo fácil es confundirse. **Verdad**: Crea la columna autor_id + índice + FK en la tabla posts (relación completa en SQL). Las migraciones versionan tu esquema en código: la BD se recrea con rails db:migrate.

## 🩹 Antídoto universal
1. Lee el mensaje de error COMPLETO antes de googlear.
2. Pon el error exacto a la IA local y pide explicación, no solución.
3. Documenta el error en tu bitácora: error → causa → fix.
