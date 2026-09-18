# ⚠️ Errores comunes — 6. Responsive design: una web para todos los tamaños

> HTML y CSS — Diseño Web Total · Lección 6 · Aprender de los errores (propios y ajenos)

- ❌ «Bloquea el zoom para siempre» → Frente a «¿Qué hace la meta etiqueta viewport?» lo fácil es confundirse. **Verdad**: Dice al móvil que use el ancho real del dispositivo y no una miniatura. Sin ella, el móvil renderiza como si fuera un desktop de 980px y escala.
- ❌ «Mejora el SEO» → Frente a «¿Qué hace la meta etiqueta viewport?» lo fácil es confundirse. **Verdad**: Dice al móvil que use el ancho real del dispositivo y no una miniatura. Sin ella, el móvil renderiza como si fuera un desktop de 980px y escala.
- ❌ «Que movil es más importante que desktop» → Frente a «¿Qué significa mobile-first?» lo fácil es confundirse. **Verdad**: Escribir el CSS base para móvil y crecer con min-width media queries. Base simple en pantalla chica; complejidad progresiva hacia pantallas grandes.
- ❌ «Testear solo en móvil» → Frente a «¿Qué significa mobile-first?» lo fácil es confundirse. **Verdad**: Escribir el CSS base para móvil y crecer con min-width media queries. Base simple en pantalla chica; complejidad progresiva hacia pantallas grandes.

## 🩹 Antídoto universal
1. Lee el mensaje de error COMPLETO antes de googlear.
2. Pon el error exacto a la IA local y pide explicación, no solución.
3. Documenta el error en tu bitácora: error → causa → fix.
