# ⚠️ Errores comunes — 6. Debugging: el arte de encontrar lo que rompiste

> Herramientas del Desarrollador · Lección 6 · Aprender de los errores (propios y ajenos)

- ❌ «De arriba hacia abajo» → Frente a «¿Cómo se lee un traceback?» lo fácil es confundirse. **Verdad**: De abajo hacia arriba: tipo de error y mensaje primero. Tipo + mensaje (abajo) te dicen el qué; los frames (arriba) te dicen el dónde.
- ❌ «Ignorando el mensaje» → Frente a «¿Cómo se lee un traceback?» lo fácil es confundirse. **Verdad**: De abajo hacia arriba: tipo de error y mensaje primero. Tipo + mensaje (abajo) te dicen el qué; los frames (arriba) te dicen el dónde.
- ❌ «Borrar el código» → Frente a «¿Qué debe pasar ANTES de intentar arreglar un bug?» lo fácil es confundirse. **Verdad**: Reproducir el error de forma confiable. Sin reproducción confiable solo estás adivinando.
- ❌ «Pedir ayuda en foros» → Frente a «¿Qué debe pasar ANTES de intentar arreglar un bug?» lo fácil es confundirse. **Verdad**: Reproducir el error de forma confiable. Sin reproducción confiable solo estás adivinando.

## 🩹 Antídoto universal
1. Lee el mensaje de error COMPLETO antes de googlear.
2. Pon el error exacto a la IA local y pide explicación, no solución.
3. Documenta el error en tu bitácora: error → causa → fix.
