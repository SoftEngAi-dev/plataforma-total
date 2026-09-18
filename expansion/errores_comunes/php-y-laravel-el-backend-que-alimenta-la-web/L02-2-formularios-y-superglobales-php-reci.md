# ⚠️ Errores comunes — 2. Formularios y superglobales: PHP recibe datos

> PHP y Laravel — El Backend Que Alimenta la Web · Lección 2 · Aprender de los errores (propios y ajenos)

- ❌ «Nada útil» → Frente a «¿Qué hace htmlentities($texto) antes de un echo?» lo fácil es confundirse. **Verdad**: Escapa <script> etc. evitando XSS: HTML inyectado queda como texto inofensivo. La regla de vida PHP: toda salida con datos del usuario pasa por escaping.
- ❌ «Formatea bonito» → Frente a «¿Qué hace htmlentities($texto) antes de un echo?» lo fácil es confundirse. **Verdad**: Escapa <script> etc. evitando XSS: HTML inyectado queda como texto inofensivo. La regla de vida PHP: toda salida con datos del usuario pasa por escaping.
- ❌ «Error» → Frente a «$_POST["email"] ?? "" significa...» lo fácil es confundirse. **Verdad**: Si no viene email, usa '' (null coalescing ?? en vez de undefined/index notice). ?? evita avisos por índices faltantes — desde PHP 7 la forma elegante.
- ❌ «Comparar» → Frente a «$_POST["email"] ?? "" significa...» lo fácil es confundirse. **Verdad**: Si no viene email, usa '' (null coalescing ?? en vez de undefined/index notice). ?? evita avisos por índices faltantes — desde PHP 7 la forma elegante.

## 🩹 Antídoto universal
1. Lee el mensaje de error COMPLETO antes de googlear.
2. Pon el error exacto a la IA local y pide explicación, no solución.
3. Documenta el error en tu bitácora: error → causa → fix.
