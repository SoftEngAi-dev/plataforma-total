# ⚠️ Errores comunes — 4. GROUP BY y HAVING: resúmenes por grupos

> SQL y Bases de Datos — Datos que Persisten · Lección 4 · Aprender de los errores (propios y ajenos)

- ❌ «Ninguna» → Frente a «¿Diferencia entre WHERE y HAVING?» lo fácil es confundirse. **Verdad**: WHERE filtra filas antes de agrupar; HAVING filtra grupos después de la agregación. Orden lógico: WHERE → GROUP BY → HAVING. El clásico de entrevistas.
- ❌ «HAVING es más rápido» → Frente a «¿Diferencia entre WHERE y HAVING?» lo fácil es confundirse. **Verdad**: WHERE filtra filas antes de agrupar; HAVING filtra grupos después de la agregación. Orden lógico: WHERE → GROUP BY → HAVING. El clásico de entrevistas.
- ❌ «Ninguna permitida» → Frente a «¿Qué agregada debe estar en HAVING COUNT(*) >= 5?» lo fácil es confundirse. **Verdad**: Las agregadas (COUNT, SUM...) se vetican en HAVING tras agrupar. HAVING vive en el mundo de los grupos; las funciones agregadas habitan ahí.
- ❌ «Solo AVG» → Frente a «¿Qué agregada debe estar en HAVING COUNT(*) >= 5?» lo fácil es confundirse. **Verdad**: Las agregadas (COUNT, SUM...) se vetican en HAVING tras agrupar. HAVING vive en el mundo de los grupos; las funciones agregadas habitan ahí.

## 🩹 Antídoto universal
1. Lee el mensaje de error COMPLETO antes de googlear.
2. Pon el error exacto a la IA local y pide explicación, no solución.
3. Documenta el error en tu bitácora: error → causa → fix.
