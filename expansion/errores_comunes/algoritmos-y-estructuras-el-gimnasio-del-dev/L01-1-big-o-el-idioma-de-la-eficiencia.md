# ⚠️ Errores comunes — 1. Big O: el idioma de la eficiencia

> Algoritmos y Estructuras — El Gimnasio del Dev · Lección 1 · Aprender de los errores (propios y ajenos)

- ❌ «Sí exacto» → Frente a «¿Es rapidez absoluta lo que mide Big O?» lo fácil es confundirse. **Verdad**: Cómo CRECE el costo al crecer n (escalabilidad), no tiempo exacto. Es la curva de crecimiento que decide si sirve para 10 datos o para 10 millones.
- ❌ «Solo memoria» → Frente a «¿Es rapidez absoluta lo que mide Big O?» lo fácil es confundirse. **Verdad**: Cómo CRECE el costo al crecer n (escalabilidad), no tiempo exacto. Es la curva de crecimiento que decide si sirve para 10 datos o para 10 millones.
- ❌ «O(n)» → Frente a «¿Qué complejidad busca/accede en un dict/hash por clave?» lo fácil es confundirse. **Verdad**: O(1) promedio: acces directo sin recorrer. Por eso los diccionarios/hashes dominan el código real: lookups instantáneos.
- ❌ «O(log n)» → Frente a «¿Qué complejidad busca/accede en un dict/hash por clave?» lo fácil es confundirse. **Verdad**: O(1) promedio: acces directo sin recorrer. Por eso los diccionarios/hashes dominan el código real: lookups instantáneos.

## 🩹 Antídoto universal
1. Lee el mensaje de error COMPLETO antes de googlear.
2. Pon el error exacto a la IA local y pide explicación, no solución.
3. Documenta el error en tu bitácora: error → causa → fix.
