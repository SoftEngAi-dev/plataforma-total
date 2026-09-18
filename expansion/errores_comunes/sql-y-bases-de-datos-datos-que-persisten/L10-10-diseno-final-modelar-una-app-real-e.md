# ⚠️ Errores comunes — 10. Diseño final: modelar una app real en SQL

> SQL y Bases de Datos — Datos que Persisten · Lección 10 · Aprender de los errores (propios y ajenos)

- ❌ «Velocidad» → Frente a «¿Por qué CASCADE en comentarios de un post borrado?» lo fácil es confundirse. **Verdad**: No quedan comentarios huérfanos de posts inexistentes. La integridad referencial gestionada por la base: consistencia siempre.
- ❌ «Decora» → Frente a «¿Por qué CASCADE en comentarios de un post borrado?» lo fácil es confundirse. **Verdad**: No quedan comentarios huérfanos de posts inexistentes. La integridad referencial gestionada por la base: consistencia siempre.
- ❌ «Todo en una tabla» → Frente a «¿Qué patrón se repite en todo esquema serio?» lo fácil es confundirse. **Verdad**: Entidades separadas + FKs + restricciones + índices en búsquedas frecuentes. Normalización + restricciones = la base no permite corrupción de datos desde afuera.
- ❌ «Solo JSON» → Frente a «¿Qué patrón se repite en todo esquema serio?» lo fácil es confundirse. **Verdad**: Entidades separadas + FKs + restricciones + índices en búsquedas frecuentes. Normalización + restricciones = la base no permite corrupción de datos desde afuera.

## 🩹 Antídoto universal
1. Lee el mensaje de error COMPLETO antes de googlear.
2. Pon el error exacto a la IA local y pide explicación, no solución.
3. Documenta el error en tu bitácora: error → causa → fix.
