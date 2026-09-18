# ⚠️ Errores comunes — 6. Relaciones: FOREIGN KEY y primer diseño

> SQL y Bases de Datos — Datos que Persisten · Lección 6 · Aprender de los errores (propios y ajenos)

- ❌ «En autores» → Frente a «¿Dónde va la FK en una relación 1 a muchos (autor-libros)?» lo fácil es confundirse. **Verdad**: En libros (el lado 'muchos'). Cada libro apunta a su autor: FK en la tabla del lado N.
- ❌ «En ambos» → Frente a «¿Dónde va la FK en una relación 1 a muchos (autor-libros)?» lo fácil es confundirse. **Verdad**: En libros (el lado 'muchos'). Cada libro apunta a su autor: FK en la tabla del lado N.
- ❌ «Con arrays» → Frente a «¿Cómo se modela muchos-a-muchos?» lo fácil es confundirse. **Verdad**: Tabla intermedia con ambas FK y PK compuesta. La tabla puente (inscripciones) convierte M:N en dos relaciones 1:N.
- ❌ «Duplicando datos» → Frente a «¿Cómo se modela muchos-a-muchos?» lo fácil es confundirse. **Verdad**: Tabla intermedia con ambas FK y PK compuesta. La tabla puente (inscripciones) convierte M:N en dos relaciones 1:N.

## 🩹 Antídoto universal
1. Lee el mensaje de error COMPLETO antes de googlear.
2. Pon el error exacto a la IA local y pide explicación, no solución.
3. Documenta el error en tu bitácora: error → causa → fix.
