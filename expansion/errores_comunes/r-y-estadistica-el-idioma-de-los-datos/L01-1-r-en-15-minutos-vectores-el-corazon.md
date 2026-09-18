# ⚠️ Errores comunes — 1. R en 15 minutos: vectores, el corazón

> R y Estadística — El Idioma de los Datos · Lección 1 · Aprender de los errores (propios y ajenos)

- ❌ «Error» → Frente a «¿Qué hace edades[edades > 30]?» lo fácil es confundirse. **Verdad**: Indexación lógica vectorizada: devuelve solo los elementos donde la condición es TRUE. Filtrar vectores con condiciones sin bucles: la elegancia R desde el día 1.
- ❌ «Borra» → Frente a «¿Qué hace edades[edades > 30]?» lo fácil es confundirse. **Verdad**: Indexación lógica vectorizada: devuelve solo los elementos donde la condición es TRUE. Filtrar vectores con condiciones sin bucles: la elegancia R desde el día 1.
- ❌ «En 0» → Frente a «¿En qué empiezan los índices de R?» lo fácil es confundirse. **Verdad**: En 1 — viejos lenguajes científicos (R/MATLAB/Fortran) cuentan como humanos. Sorpresa clásica para quien viene de C/Python: edades[1] es el PRIMERO.
- ❌ «En -1» → Frente a «¿En qué empiezan los índices de R?» lo fácil es confundirse. **Verdad**: En 1 — viejos lenguajes científicos (R/MATLAB/Fortran) cuentan como humanos. Sorpresa clásica para quien viene de C/Python: edades[1] es el PRIMERO.

## 🩹 Antídoto universal
1. Lee el mensaje de error COMPLETO antes de googlear.
2. Pon el error exacto a la IA local y pide explicación, no solución.
3. Documenta el error en tu bitácora: error → causa → fix.
