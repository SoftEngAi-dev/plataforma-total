# ⚠️ Errores comunes — 2. Punteros y memoria manual: la estrella de C

> C y C++ — Los Cimientos del Software Moderno · Lección 2 · Aprender de los errores (propios y ajenos)

- ❌ «Multiplicar» → Frente a «¿Qué significa *p cuando p es puntero?» lo fácil es confundirse. **Verdad**: Seguir el puntero: LEER/ESCRIBIR el valor en esa dirección. * = dereferenciar; & = sacar dirección. Las dos caras de la memoria manual.
- ❌ «Reservar memoria» → Frente a «¿Qué significa *p cuando p es puntero?» lo fácil es confundirse. **Verdad**: Seguir el puntero: LEER/ESCRIBIR el valor en esa dirección. * = dereferenciar; & = sacar dirección. Las dos caras de la memoria manual.
- ❌ «Un virus» → Frente a «¿Qué es una fuga de memoria (memory leak)?» lo fácil es confundirse. **Verdad**: malloc sin free: la memoria reservada nunca se devuelve y el programa crece hasta morir. En C/GestiónManual: cada malloc necesita su free — por eso los lenguajes modernos tienen GC/ownership.
- ❌ «Un print raro» → Frente a «¿Qué es una fuga de memoria (memory leak)?» lo fácil es confundirse. **Verdad**: malloc sin free: la memoria reservada nunca se devuelve y el programa crece hasta morir. En C/GestiónManual: cada malloc necesita su free — por eso los lenguajes modernos tienen GC/ownership.

## 🩹 Antídoto universal
1. Lee el mensaje de error COMPLETO antes de googlear.
2. Pon el error exacto a la IA local y pide explicación, no solución.
3. Documenta el error en tu bitácora: error → causa → fix.
