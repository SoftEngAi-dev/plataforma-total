# ⚠️ Errores comunes — 4. Flexbox: layout en una dimensión

> HTML y CSS — Diseño Web Total · Lección 4 · Aprender de los errores (propios y ajenos)

- ❌ «display:block + margin:0» → Frente a «¿Qué línea centra un elemento horizontal y verticalmente dentro de su padre?» lo fácil es confundirse. **Verdad**: display:flex; justify-content:center; align-items:center. Flexbox con ambos ejes centrados — el centramiento perfecto ya no es chiste.
- ❌ «position:center» → Frente a «¿Qué línea centra un elemento horizontal y verticalmente dentro de su padre?» lo fácil es confundirse. **Verdad**: display:flex; justify-content:center; align-items:center. Flexbox con ambos ejes centrados — el centramiento perfecto ya no es chiste.
- ❌ «Le da 1px» → Frente a «¿Qué hace flex: 1 en un hijo?» lo fácil es confundirse. **Verdad**: Lo hace crecer para repartir el espacio sobrante del contenedor. flex-grow/shrink/basis abreviado: típicamente reparte el espacio equitativamente.
- ❌ «Lo pone primero» → Frente a «¿Qué hace flex: 1 en un hijo?» lo fácil es confundirse. **Verdad**: Lo hace crecer para repartir el espacio sobrante del contenedor. flex-grow/shrink/basis abreviado: típicamente reparte el espacio equitativamente.

## 🩹 Antídoto universal
1. Lee el mensaje de error COMPLETO antes de googlear.
2. Pon el error exacto a la IA local y pide explicación, no solución.
3. Documenta el error en tu bitácora: error → causa → fix.
