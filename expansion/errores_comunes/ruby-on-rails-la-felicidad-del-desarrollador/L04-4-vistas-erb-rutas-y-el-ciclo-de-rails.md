# ⚠️ Errores comunes — 4. Vistas ERB, rutas y el ciclo de Rails

> Ruby on Rails — La Felicidad del Desarrollador · Lección 4 · Aprender de los errores (propios y ajenos)

- ❌ «Ninguna» → Frente a «¿Diferencia entre <% %> y <%= %> en ERB?» lo fácil es confundirse. **Verdad**: <% ejecuta sin imprimir (loops/ifs); <%= ejecuta E IMPRIME escapando HTML. El clásico bug: poner <%= en un @each y ver la lista entera impresa.
- ❌ «<%= es comentario» → Frente a «¿Diferencia entre <% %> y <%= %> en ERB?» lo fácil es confundirse. **Verdad**: <% ejecuta sin imprimir (loops/ifs); <%= ejecuta E IMPRIME escapando HTML. El clásico bug: poner <%= en un @each y ver la lista entera impresa.
- ❌ «CSS» → Frente a «¿Qué hace form_with model: @post?» lo fácil es confundirse. **Verdad**: Formulario automático ligado al modelo: crea o edita según el objeto, con token CSRF incluido. Los helpers sienten la convención: si @post es nuevo → POST /posts; si existe → PATCH.
- ❌ «Valida» → Frente a «¿Qué hace form_with model: @post?» lo fácil es confundirse. **Verdad**: Formulario automático ligado al modelo: crea o edita según el objeto, con token CSRF incluido. Los helpers sienten la convención: si @post es nuevo → POST /posts; si existe → PATCH.

## 🩹 Antídoto universal
1. Lee el mensaje de error COMPLETO antes de googlear.
2. Pon el error exacto a la IA local y pide explicación, no solución.
3. Documenta el error en tu bitácora: error → causa → fix.
