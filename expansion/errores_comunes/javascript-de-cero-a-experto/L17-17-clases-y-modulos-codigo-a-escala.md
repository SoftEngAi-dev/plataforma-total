# ⚠️ Errores comunes — 17. Clases y módulos: código a escala

> JavaScript — De Cero a Experto · Lección 17 · Aprender de los errores (propios y ajenos)

- ❌ «Es más rápido» → Frente a «¿Qué hace export default frente a export nombrado?» lo fácil es confundirse. **Verdad**: Un solo default por archivo, se importa sin llaves; los nombrados van con llaves exactas. import X from... (default) vs import { x } from... (nombrados).
- ❌ «Default es privado» → Frente a «¿Qué hace export default frente a export nombrado?» lo fácil es confundirse. **Verdad**: Un solo default por archivo, se importa sin llaves; los nombrados van con llaves exactas. import X from... (default) vs import { x } from... (nombrados).
- ❌ «Borra el método del padre» → Frente a «¿Qué hace super.completar() en una subclase?» lo fácil es confundirse. **Verdad**: Invoca la versión del método en la clase padre. super = acceso a la clase padre: reutilizas y extiendes en vez de reescribir.
- ❌ «Copia el objeto» → Frente a «¿Qué hace super.completar() en una subclase?» lo fácil es confundirse. **Verdad**: Invoca la versión del método en la clase padre. super = acceso a la clase padre: reutilizas y extiendes en vez de reescribir.

## 🩹 Antídoto universal
1. Lee el mensaje de error COMPLETO antes de googlear.
2. Pon el error exacto a la IA local y pide explicación, no solución.
3. Documenta el error en tu bitácora: error → causa → fix.
