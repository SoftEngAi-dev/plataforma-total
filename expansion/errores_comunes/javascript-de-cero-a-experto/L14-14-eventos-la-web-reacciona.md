# ⚠️ Errores comunes — 14. Eventos: la web reacciona

> JavaScript — De Cero a Experto · Lección 14 · Aprender de los errores (propios y ajenos)

- ❌ «Acelera el envío» → Frente a «¿Por qué e.preventDefault() en el submit de un formulario?» lo fácil es confundirse. **Verdad**: Evita que el navegador recargue la página para procesarlo con JS. Sin preventDefault, el formulario navega/recarga y tu lógica JS no corre.
- ❌ «Valida los campos» → Frente a «¿Por qué e.preventDefault() en el submit de un formulario?» lo fácil es confundirse. **Verdad**: Evita que el navegador recargue la página para procesarlo con JS. Sin preventDefault, el formulario navega/recarga y tu lógica JS no corre.
- ❌ «Un listener por cada hijo» → Frente a «¿Qué es delegación de eventos?» lo fácil es confundirse. **Verdad**: Un solo listener en el padre que reacciona según e.target. Clave para contenido dinámico: los hijos futuros también funcionan.
- ❌ «Eventos automáticos» → Frente a «¿Qué es delegación de eventos?» lo fácil es confundirse. **Verdad**: Un solo listener en el padre que reacciona según e.target. Clave para contenido dinámico: los hijos futuros también funcionan.

## 🩹 Antídoto universal
1. Lee el mensaje de error COMPLETO antes de googlear.
2. Pon el error exacto a la IA local y pide explicación, no solución.
3. Documenta el error en tu bitácora: error → causa → fix.
