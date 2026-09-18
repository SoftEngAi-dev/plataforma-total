# ⚠️ Errores comunes — 2. Variables: let, const y por qué var quedó atrás

> JavaScript — De Cero a Experto · Lección 2 · Aprender de los errores (propios y ajenos)

- ❌ «var siempre» → Frente a «¿Cuál es la regla moderna para declarar variables?» lo fácil es confundirse. **Verdad**: const por defecto; let solo si reasignas; var nunca. const comunica 'esto no cambia': menos sorpresas, bugs más difíciles.
- ❌ «let siempre» → Frente a «¿Cuál es la regla moderna para declarar variables?» lo fácil es confundirse. **Verdad**: const por defecto; let solo si reasignas; var nunca. const comunica 'esto no cambia': menos sorpresas, bugs más difíciles.
- ❌ «Error: const es inmutable» → Frente a «¿Qué pasa con const arr = [1]; arr.push(2)?» lo fácil es confundirse. **Verdad**: Funciona: const prohíbe reasignar, no mutar el contenido. const congela la REFERENCIA, no el objeto: puedes mutar por dentro.
- ❌ «Duplica el array» → Frente a «¿Qué pasa con const arr = [1]; arr.push(2)?» lo fácil es confundirse. **Verdad**: Funciona: const prohíbe reasignar, no mutar el contenido. const congela la REFERENCIA, no el objeto: puedes mutar por dentro.

## 🩹 Antídoto universal
1. Lee el mensaje de error COMPLETO antes de googlear.
2. Pon el error exacto a la IA local y pide explicación, no solución.
3. Documenta el error en tu bitácora: error → causa → fix.
