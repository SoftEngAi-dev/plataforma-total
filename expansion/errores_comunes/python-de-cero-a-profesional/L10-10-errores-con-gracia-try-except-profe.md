# ⚠️ Errores comunes — 10. Errores con gracia: try/except profesional

> Python — De Cero a Profesional · Lección 10 · Aprender de los errores (propios y ajenos)

- ❌ «try» → Frente a «¿Qué bloque corre SIEMPRE, haya o no excepción?» lo fácil es confundirse. **Verdad**: finally. finally = limpieza garantizada (cerrar archivos, conexiones).
- ❌ «except» → Frente a «¿Qué bloque corre SIEMPRE, haya o no excepción?» lo fácil es confundirse. **Verdad**: finally. finally = limpieza garantizada (cerrar archivos, conexiones).
- ❌ «Matar el programa» → Frente a «raise ValueError('x') sirve para...» lo fácil es confundirse. **Verdad**: Lanzar tu propio error con mensaje claro cuando detectas un estado inválido. Valida pronto, falla fuerte y con mensaje: debugging agradecido.
- ❌ «Imprimir errores» → Frente a «raise ValueError('x') sirve para...» lo fácil es confundirse. **Verdad**: Lanzar tu propio error con mensaje claro cuando detectas un estado inválido. Valida pronto, falla fuerte y con mensaje: debugging agradecido.

## 🩹 Antídoto universal
1. Lee el mensaje de error COMPLETO antes de googlear.
2. Pon el error exacto a la IA local y pide explicación, no solución.
3. Documenta el error en tu bitácora: error → causa → fix.
