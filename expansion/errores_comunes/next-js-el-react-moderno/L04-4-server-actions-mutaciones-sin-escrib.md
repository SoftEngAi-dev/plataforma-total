# ⚠️ Errores comunes — 4. Server Actions: mutaciones sin escribir APIs

> ▲ Next.js — El React Moderno · Lección 4 · Aprender de los errores (propios y ajenos)

- ❌ «Un Service Worker» → Frente a «¿Qué es una Server Action?» lo fácil es confundirse. **Verdad**: Una función que corre en el servidor invocable desde la UI sin escribir un endpoint. Con 'use server' declaras funciones backend llamables: Next genera el canal seguro automáticamente.
- ❌ «Un middleware de Express» → Frente a «¿Qué es una Server Action?» lo fácil es confundirse. **Verdad**: Una función que corre en el servidor invocable desde la UI sin escribir un endpoint. Con 'use server' declaras funciones backend llamables: Next genera el canal seguro automáticamente.
- ❌ «Confiar en los datos del formulario» → Frente a «¿Qué debes hacer SIEMPRE dentro de una Server Action?» lo fácil es confundirse. **Verdad**: Validar entradas y comprobar permisos. El cliente puede enviar cualquier cosa: la action es tu última línea de defensa (zod + auth).
- ❌ «Guardar en localStorage» → Frente a «¿Qué debes hacer SIEMPRE dentro de una Server Action?» lo fácil es confundirse. **Verdad**: Validar entradas y comprobar permisos. El cliente puede enviar cualquier cosa: la action es tu última línea de defensa (zod + auth).

## 🩹 Antídoto universal
1. Lee el mensaje de error COMPLETO antes de googlear.
2. Pon el error exacto a la IA local y pide explicación, no solución.
3. Documenta el error en tu bitácora: error → causa → fix.
