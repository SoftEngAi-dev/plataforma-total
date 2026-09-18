# ⚠️ Errores comunes — 3. Autenticación moderna: sesiones, JWT y OAuth

> Seguridad para Desarrolladores — No Seas la Brecha · Lección 3 · Aprender de los errores (propios y ajenos)

- ❌ «Ninguna» → Frente a «¿Qué diferencia sesión-clásica de JWT?» lo fácil es confundirse. **Verdad**: Sesión clásica guarda estado en el servidor con ID en cookie; JWT firma y viaja el estado EN EL TOKEN (stateless). Trade: estado revocable/central vs escalabilidad sin estado ni revocación simple.
- ❌ «JWT es más seguro» → Frente a «¿Qué diferencia sesión-clásica de JWT?» lo fácil es confundirse. **Verdad**: Sesión clásica guarda estado en el servidor con ID en cookie; JWT firma y viaja el estado EN EL TOKEN (stateless). Trade: estado revocable/central vs escalabilidad sin estado ni revocación simple.
- ❌ «Es lento» → Frente a «¿Por qué JWT en localStorage es riesgoso?» lo fácil es confundirse. **Verdad**: Cualquier XSS puede JavaScript-leerlo y robar identidad; cookie HttpOnly no es legible por JS. El trade de seguridad: lo que JavaScript toca, un XSS también toca.
- ❌ «No existe» → Frente a «¿Por qué JWT en localStorage es riesgoso?» lo fácil es confundirse. **Verdad**: Cualquier XSS puede JavaScript-leerlo y robar identidad; cookie HttpOnly no es legible por JS. El trade de seguridad: lo que JavaScript toca, un XSS también toca.

## 🩹 Antídoto universal
1. Lee el mensaje de error COMPLETO antes de googlear.
2. Pon el error exacto a la IA local y pide explicación, no solución.
3. Documenta el error en tu bitácora: error → causa → fix.
