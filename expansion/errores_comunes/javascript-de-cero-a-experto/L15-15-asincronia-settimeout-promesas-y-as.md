# ⚠️ Errores comunes — 15. Asincronía: setTimeout, promesas y async/await

> JavaScript — De Cero a Experto · Lección 15 · Aprender de los errores (propios y ajenos)

- ❌ «El resultado final» → Frente a «¿Qué devuelve inmediatamente una función async?» lo fácil es confundirse. **Verdad**: Una promesa. async significa 'esto devolverá una promesa'; await desenvuelve su valor.
- ❌ «undefined» → Frente a «¿Qué devuelve inmediatamente una función async?» lo fácil es confundirse. **Verdad**: Una promesa. async significa 'esto devolverá una promesa'; await desenvuelve su valor.
- ❌ «Cancelar promesas» → Frente a «¿Para qué sirve Promise.all?» lo fácil es confundirse. **Verdad**: Esperar varias promesas EN PARALELO y continuar cuando todas terminan. Paralelismo de verdad: si son independientes, esperar juntas = mitad del tiempo.
- ❌ «Convertir promesas a callbacks» → Frente a «¿Para qué sirve Promise.all?» lo fácil es confundirse. **Verdad**: Esperar varias promesas EN PARALELO y continuar cuando todas terminan. Paralelismo de verdad: si son independientes, esperar juntas = mitad del tiempo.

## 🩹 Antídoto universal
1. Lee el mensaje de error COMPLETO antes de googlear.
2. Pon el error exacto a la IA local y pide explicación, no solución.
3. Documenta el error en tu bitácora: error → causa → fix.
