# ⚠️ Errores comunes — 2. Buscar: lineal vs binaria + el hash map

> Algoritmos y Estructuras — El Gimnasio del Dev · Lección 2 · Aprender de los errores (propios y ajenos)

- ❌ «Ninguno» → Frente a «¿Qué requisito tiene la búsqueda binaria?» lo fácil es confundirse. **Verdad**: La lista DEBE estar ordenada (si no, divide mal). binaria=O(log n) pero necesita order previamente: a veces n log n+bar vale
- ❌ «Ser números» → Frente a «¿Qué requisito tiene la búsqueda binaria?» lo fácil es confundirse. **Verdad**: La lista DEBE estar ordenada (si no, divide mal). binaria=O(log n) pero necesita order previamente: a veces n log n+bar vale
- ❌ «Más RAM» → Frente a «¿Cómo convertir múltiples búsquedas O(n) cada una en O(1) cada una?» lo fácil es confundirse. **Verdad**: Construir UN diccionario/hash indexado UNA vez y consultarlo en O(1) luego. Trade tiempo-por-memoria: indexar=prepagar para buscar barato.
- ❌ «Bucle for» → Frente a «¿Cómo convertir múltiples búsquedas O(n) cada una en O(1) cada una?» lo fácil es confundirse. **Verdad**: Construir UN diccionario/hash indexado UNA vez y consultarlo en O(1) luego. Trade tiempo-por-memoria: indexar=prepagar para buscar barato.

## 🩹 Antídoto universal
1. Lee el mensaje de error COMPLETO antes de googlear.
2. Pon el error exacto a la IA local y pide explicación, no solución.
3. Documenta el error en tu bitácora: error → causa → fix.
