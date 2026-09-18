# ⚠️ Errores comunes — 3. Result y Option: errores como parte del tipo

> Rust — Velocidad de C sin Miedo a los Crashes · Lección 3 · Aprender de los errores (propios y ajenos)

- ❌ «Nada» → Frente a «¿Qué hace el operador ? tras una llamada Result?» lo fácil es confundirse. **Verdad**: Si es Ok, desenvuelve el valor; si es Err, lo retorna inmediatamente a la función llamante (propagación elegante). El equivalente Go-verboso pero sin boilerplate: error handling conciso y explícito.
- ❌ «Borra» → Frente a «¿Qué hace el operador ? tras una llamada Result?» lo fácil es confundirse. **Verdad**: Si es Ok, desenvuelve el valor; si es Err, lo retorna inmediatamente a la función llamante (propagación elegante). El equivalente Go-verboso pero sin boilerplate: error handling conciso y explícito.
- ❌ «Es un puntero» → Frente a «¿En qué consiste la seguridad adicional de Option<T> vs null?» lo fácil es confundirse. **Verdad**: No hay null: la AUSENCIA es parte del TIPO y el compilador EXIGE manejar el caso None. Null = 'agujero invisible'; None = 'la firma te avisa y obliga'. Billion-dollar mistake corregida.
- ❌ «Es más rápido» → Frente a «¿En qué consiste la seguridad adicional de Option<T> vs null?» lo fácil es confundirse. **Verdad**: No hay null: la AUSENCIA es parte del TIPO y el compilador EXIGE manejar el caso None. Null = 'agujero invisible'; None = 'la firma te avisa y obliga'. Billion-dollar mistake corregida.

## 🩹 Antídoto universal
1. Lee el mensaje de error COMPLETO antes de googlear.
2. Pon el error exacto a la IA local y pide explicación, no solución.
3. Documenta el error en tu bitácora: error → causa → fix.
