# ⚠️ Errores comunes — 6. Condicionales: if, else y el operador ternario

> JavaScript — De Cero a Experto · Lección 6 · Aprender de los errores (propios y ajenos)

- ❌ «Solo false» → Frente a «¿Cuáles valores son falsy en JS?» lo fácil es confundirse. **Verdad**: false, 0, "", null, undefined, NaN. if(x) con x falsy no ejecuta el bloque — revisa esta lista cuando te sorprenda.
- ❌ «Solo null y undefined» → Frente a «¿Cuáles valores son falsy en JS?» lo fácil es confundirse. **Verdad**: false, 0, "", null, undefined, NaN. if(x) con x falsy no ejecuta el bloque — revisa esta lista cuando te sorprenda.
- ❌ «Siempre da "invitado"» → Frente a «¿Qué hace nombre ?? "invitado"?» lo fácil es confundirse. **Verdad**: Usa "invitado" SOLO si nombre es null o undefined (no si es "" o 0). ?? es el default preciso: || también rechazaría '' y 0 que podrías querer conservar.
- ❌ «Es un error de sintaxis» → Frente a «¿Qué hace nombre ?? "invitado"?» lo fácil es confundirse. **Verdad**: Usa "invitado" SOLO si nombre es null o undefined (no si es "" o 0). ?? es el default preciso: || también rechazaría '' y 0 que podrías querer conservar.

## 🩹 Antídoto universal
1. Lee el mensaje de error COMPLETO antes de googlear.
2. Pon el error exacto a la IA local y pide explicación, no solución.
3. Documenta el error en tu bitácora: error → causa → fix.
