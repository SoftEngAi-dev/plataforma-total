# ⚠️ Errores comunes — 1. Kotlin: el alivio que pedía Java

> Kotlin — Android y Más Allá · Lección 1 · Aprender de los errores (propios y ajenos)

- ❌ «Son iguales» → Frente a «¿Qué diferencia val de var en Kotlin?» lo fácil es confundirse. **Verdad**: val es inmutable (referencia fija); var es reasignable. Kotlin te empuja a inmutabilidad por defecto: val primero, var solo si hace falta.
- ❌ «val es para números» → Frente a «¿Qué diferencia val de var en Kotlin?» lo fácil es confundirse. **Verdad**: val es inmutable (referencia fija); var es reasignable. Kotlin te empuja a inmutabilidad por defecto: val primero, var solo si hace falta.
- ❌ «Nada» → Frente a «¿Qué hace ?: (operador Elvis)?» lo fácil es confundirse. **Verdad**: Si lo de la izquierda es null, devuelve lo de la derecha. Elvis porque parece un peinado ?:  — null coalescing con nombre rockero.
- ❌ «Compara strings» → Frente a «¿Qué hace ?: (operador Elvis)?» lo fácil es confundirse. **Verdad**: Si lo de la izquierda es null, devuelve lo de la derecha. Elvis porque parece un peinado ?:  — null coalescing con nombre rockero.

## 🩹 Antídoto universal
1. Lee el mensaje de error COMPLETO antes de googlear.
2. Pon el error exacto a la IA local y pide explicación, no solución.
3. Documenta el error en tu bitácora: error → causa → fix.
