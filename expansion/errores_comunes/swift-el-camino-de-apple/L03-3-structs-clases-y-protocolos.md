# ⚠️ Errores comunes — 3. Structs, clases y protocolos

> Swift — El Camino de Apple · Lección 3 · Aprender de los errores (propios y ajenos)

- ❌ «Son iguales» → Frente a «¿Qué diferencia struct de class en Swift?» lo fácil es confundirse. **Verdad**: struct = tipo VALOR (se copia); class = tipo REFERENCIA (se comparte) con herencia. Structs por defecto = menos bugs de aliasing; class solo para identidad compartida.
- ❌ «class es gratis» → Frente a «¿Qué diferencia struct de class en Swift?» lo fácil es confundirse. **Verdad**: struct = tipo VALOR (se copia); class = tipo REFERENCIA (se comparte) con herencia. Structs por defecto = menos bugs de aliasing; class solo para identidad compartida.
- ❌ «Herencia múltiple» → Frente a «¿Qué permite una extension?» lo fácil es confundirse. **Verdad**: Agregar funcionalidad a tipos existentes sin subclases: incluso a Int, String nativos. Las extensiones hacen Swift extensible al infinito y súper idiomático.
- ❌ «Nada especial» → Frente a «¿Qué permite una extension?» lo fácil es confundirse. **Verdad**: Agregar funcionalidad a tipos existentes sin subclases: incluso a Int, String nativos. Las extensiones hacen Swift extensible al infinito y súper idiomático.

## 🩹 Antídoto universal
1. Lee el mensaje de error COMPLETO antes de googlear.
2. Pon el error exacto a la IA local y pide explicación, no solución.
3. Documenta el error en tu bitácora: error → causa → fix.
