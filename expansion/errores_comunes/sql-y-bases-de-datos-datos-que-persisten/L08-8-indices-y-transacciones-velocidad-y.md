# ⚠️ Errores comunes — 8. Índices y transacciones: velocidad y seguridad

> SQL y Bases de Datos — Datos que Persisten · Lección 8 · Aprender de los errores (propios y ajenos)

- ❌ «En todas las columnas siempre» → Frente a «¿Cuándo crear un índice?» lo fácil es confundirse. **Verdad**: En columnas usadas frecuentemente en WHERE/JOIN (con costo de escritura). Índices aceleran lecturas pero encarecen escrituras: sobredimensionarlos es deuda.
- ❌ «Nunca» → Frente a «¿Cuándo crear un índice?» lo fácil es confundirse. **Verdad**: En columnas usadas frecuentemente en WHERE/JOIN (con costo de escritura). Índices aceleran lecturas pero encarecen escrituras: sobredimensionarlos es deuda.
- ❌ «Velocidad» → Frente a «¿Qué garantiza una transacción bancaria (BEGIN...COMMIT)?» lo fácil es confundirse. **Verdad**: Las dos actualizaciones suceden juntas o ninguna (atomicidad). Si falla a mitad, ROLLBACK: nunca hay dinero perdido en el aire.
- ❌ «Orden alfabético» → Frente a «¿Qué garantiza una transacción bancaria (BEGIN...COMMIT)?» lo fácil es confundirse. **Verdad**: Las dos actualizaciones suceden juntas o ninguna (atomicidad). Si falla a mitad, ROLLBACK: nunca hay dinero perdido en el aire.

## 🩹 Antídoto universal
1. Lee el mensaje de error COMPLETO antes de googlear.
2. Pon el error exacto a la IA local y pide explicación, no solución.
3. Documenta el error en tu bitácora: error → causa → fix.
