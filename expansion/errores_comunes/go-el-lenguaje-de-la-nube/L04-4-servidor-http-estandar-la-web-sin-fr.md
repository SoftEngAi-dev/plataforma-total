# ⚠️ Errores comunes — 4. Servidor HTTP estándar: la web sin frameworks

> Go — El Lenguaje de la Nube · Lección 4 · Aprender de los errores (propios y ajenos)

- ❌ «Solo clientes» → Frente a «¿Qué incluye el paquete net/http de Go?» lo fácil es confundirse. **Verdad**: Servidor HTTP completo en la stdlib: ninguna librería extra para APIs productivas. Escuchar y servir HTTP es nativo; por eso Go domina la nube sin framework pesado.
- ❌ «Solo en frameworks» → Frente a «¿Qué incluye el paquete net/http de Go?» lo fácil es confundirse. **Verdad**: Servidor HTTP completo en la stdlib: ninguna librería extra para APIs productivas. Escuchar y servir HTTP es nativo; por eso Go domina la nube sin framework pesado.
- ❌ «Comentario» → Frente a «¿Qué hace la struct tag `json:"titulo"`?» lo fácil es confundirse. **Verdad**: Mapea el campo entre Go (Titulo) y JSON (titulo) al encodear/decodear automáticamente. Las tags gobiernan la serialización: la convención de nombre se configura explícita.
- ❌ «SQL» → Frente a «¿Qué hace la struct tag `json:"titulo"`?» lo fácil es confundirse. **Verdad**: Mapea el campo entre Go (Titulo) y JSON (titulo) al encodear/decodear automáticamente. Las tags gobiernan la serialización: la convención de nombre se configura explícita.

## 🩹 Antídoto universal
1. Lee el mensaje de error COMPLETO antes de googlear.
2. Pon el error exacto a la IA local y pide explicación, no solución.
3. Documenta el error en tu bitácora: error → causa → fix.
