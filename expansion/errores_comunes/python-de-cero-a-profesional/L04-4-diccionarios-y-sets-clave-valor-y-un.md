# ⚠️ Errores comunes — 4. Diccionarios y sets: clave-valor y unicidad

> Python — De Cero a Profesional · Lección 4 · Aprender de los errores (propios y ajenos)

- ❌ «Es más rápido» → Frente a «¿Por qué alumno.get('email') en vez de alumno['email']?» lo fácil es confundirse. **Verdad**: Evita KeyError: devuelve None (o el default) si falta la clave. get = acceso defensivo sin try/except; úsalo cuando la clave puede faltar.
- ❌ «Es más corto» → Frente a «¿Por qué alumno.get('email') en vez de alumno['email']?» lo fácil es confundirse. **Verdad**: Evita KeyError: devuelve None (o el default) si falta la clave. get = acceso defensivo sin try/except; úsalo cuando la clave puede faltar.
- ❌ «Ordenar» → Frente a «¿Para qué usar set([1,1,2,3])?» lo fácil es confundirse. **Verdad**: Eliminar duplicados: {1, 2, 3} (los sets no repiten). Deduplicación instantánea + operaciones matemáticas de conjuntos.
- ❌ «Sumar» → Frente a «¿Para qué usar set([1,1,2,3])?» lo fácil es confundirse. **Verdad**: Eliminar duplicados: {1, 2, 3} (los sets no repiten). Deduplicación instantánea + operaciones matemáticas de conjuntos.

## 🩹 Antídoto universal
1. Lee el mensaje de error COMPLETO antes de googlear.
2. Pon el error exacto a la IA local y pide explicación, no solución.
3. Documenta el error en tu bitácora: error → causa → fix.
