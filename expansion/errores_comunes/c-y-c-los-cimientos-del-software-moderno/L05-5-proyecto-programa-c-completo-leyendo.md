# ⚠️ Errores comunes — 5. Proyecto: programa C completo leyendo archivos

> C y C++ — Los Cimientos del Software Moderno · Lección 5 · Aprender de los errores (propios y ajenos)

- ❌ «Cualquiera» → Frente a «¿Qué return values significan en main C?» lo fácil es confundirse. **Verdad**: 0 = éxito; ≠0 = falló (la shell lo lee con $? — parte del protocolo Unix). El exit code es como los programas 'hablan' entre sí en batch/pipes: vital en scripts.
- ❌ «Nada» → Frente a «¿Qué return values significan en main C?» lo fácil es confundirse. **Verdad**: 0 = éxito; ≠0 = falló (la shell lo lee con $? — parte del protocolo Unix). El exit code es como los programas 'hablan' entre sí en batch/pipes: vital en scripts.
- ❌ «No importa» → Frente a «¿Por qué fclose(f) explícito importa en C?» lo fácil es confundirse. **Verdad**: Sin cerrar, fopen queda abiertoy puede agotar file descriptors / corrupt data si escribías. C no tiene with/auto-cleanup: cada recurso abierto necesita su cierre deliberado.
- ❌ «Por estética» → Frente a «¿Por qué fclose(f) explícito importa en C?» lo fácil es confundirse. **Verdad**: Sin cerrar, fopen queda abiertoy puede agotar file descriptors / corrupt data si escribías. C no tiene with/auto-cleanup: cada recurso abierto necesita su cierre deliberado.

## 🩹 Antídoto universal
1. Lee el mensaje de error COMPLETO antes de googlear.
2. Pon el error exacto a la IA local y pide explicación, no solución.
3. Documenta el error en tu bitácora: error → causa → fix.
