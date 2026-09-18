# ⚠️ Errores comunes — 3. Concurrencia: goroutines y canales (el superpoder)

> Go — El Lenguaje de la Nube · Lección 3 · Aprender de los errores (propios y ajenos)

- ❌ «Un error» → Frente a «¿Qué crea la palabra go delante de una llamada?» lo fácil es confundirse. **Verdad**: Una goroutine: la función corre concurrentemente sin bloquear. go f() = paralelo livianísimo: miles concurrentes con MB de RAM, no GB.
- ❌ «Un bucle» → Frente a «¿Qué crea la palabra go delante de una llamada?» lo fácil es confundirse. **Verdad**: Una goroutine: la función corre concurrentemente sin bloquear. go f() = paralelo livianísimo: miles concurrentes con MB de RAM, no GB.
- ❌ «Imprimir» → Frente a «¿Para qué sirve un channel en Go?» lo fácil es confundirse. **Verdad**: Comunicación tipada y segura entre goroutines: enviar/recibir datos sin locks manuales. channels = tubería sincronizada entre tareas concurrentes: el camino GOnativo.
- ❌ «Red TCP» → Frente a «¿Para qué sirve un channel en Go?» lo fácil es confundirse. **Verdad**: Comunicación tipada y segura entre goroutines: enviar/recibir datos sin locks manuales. channels = tubería sincronizada entre tareas concurrentes: el camino GOnativo.

## 🩹 Antídoto universal
1. Lee el mensaje de error COMPLETO antes de googlear.
2. Pon el error exacto a la IA local y pide explicación, no solución.
3. Documenta el error en tu bitácora: error → causa → fix.
