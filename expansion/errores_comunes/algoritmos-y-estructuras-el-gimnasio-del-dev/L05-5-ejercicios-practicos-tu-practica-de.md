# ⚠️ Errores comunes — 5. Ejercicios prácticos: tu práctica de juicio

> Algoritmos y Estructuras — El Gimnasio del Dev · Lección 5 · Aprender de los errores (propios y ajenos)

- ❌ «más RAM» → Frente a «Two Sum con diccionario es O(n) porque...» lo fácil es confundirse. **Verdad**: un solo paso por datos + lookup O(1) del complemento ya visto. Map de vistos → cada elemento se revisa UNA vez; la fuerza bruta anidada era O(n²).
- ❌ «es corto» → Frente a «Two Sum con diccionario es O(n) porque...» lo fácil es confundirse. **Verdad**: un solo paso por datos + lookup O(1) del complemento ya visto. Map de vistos → cada elemento se revisa UNA vez; la fuerza bruta anidada era O(n²).
- ❌ «Nada» → Frente a «Dos punteros (izq/der) hacia el centro resuelven elegantemente...» lo fácil es confundirse. **Verdad**: Invertir in-place, palíndromos, búsqueda en ordenados: patrón O(n) universal. Pattern reconocible: dos variables convergiendo por extremos aparecen en decenas de problemas.
- ❌ «Bases de datos» → Frente a «Dos punteros (izq/der) hacia el centro resuelven elegantemente...» lo fácil es confundirse. **Verdad**: Invertir in-place, palíndromos, búsqueda en ordenados: patrón O(n) universal. Pattern reconocible: dos variables convergiendo por extremos aparecen en decenas de problemas.

## 🩹 Antídoto universal
1. Lee el mensaje de error COMPLETO antes de googlear.
2. Pon el error exacto a la IA local y pide explicación, no solución.
3. Documenta el error en tu bitácora: error → causa → fix.
