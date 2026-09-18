# ⚠️ Errores comunes — 5. Proyecto: app Flutter completa

> Flutter — Apps Hermosas con Una Sola Base · Lección 5 · Aprender de los errores (propios y ajenos)

- ❌ «location.href» → Frente a «¿Cómo se navega entre pantallas en Flutter nativo?» lo fácil es confundirse. **Verdad**: Navigator.push con MaterialPageRoute; volver con pop (pila de rutas). El Navigator maneja una pila: push apila pantalla, pop regresa con o sin valor.
- ❌ «goto» → Frente a «¿Cómo se navega entre pantallas en Flutter nativo?» lo fácil es confundirse. **Verdad**: Navigator.push con MaterialPageRoute; volver con pop (pila de rutas). El Navigator maneja una pila: push apila pantalla, pop regresa con o sin valor.
- ❌ «flutter make web» → Frente a «¿Qué comando compila la app para web?» lo fácil es confundirse. **Verdad**: flutter build web → estáticos en build/web desplegables en Netlify/Pages. El mismo código Dart/Flutter corre como web estática: cross-platform real cumplida.
- ❌ «flutter web» → Frente a «¿Qué comando compila la app para web?» lo fácil es confundirse. **Verdad**: flutter build web → estáticos en build/web desplegables en Netlify/Pages. El mismo código Dart/Flutter corre como web estática: cross-platform real cumplida.

## 🩹 Antídoto universal
1. Lee el mensaje de error COMPLETO antes de googlear.
2. Pon el error exacto a la IA local y pide explicación, no solución.
3. Documenta el error en tu bitácora: error → causa → fix.
