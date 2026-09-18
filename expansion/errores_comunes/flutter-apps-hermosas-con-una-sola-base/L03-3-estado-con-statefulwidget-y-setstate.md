# ⚠️ Errores comunes — 3. Estado con StatefulWidget y setState

> Flutter — Apps Hermosas con Una Sola Base · Lección 3 · Aprender de los errores (propios y ajenos)

- ❌ «Por ritual» → Frente a «¿Por qué dentro de setState(() { cuenta++; })?» lo fácil es confundirse. **Verdad**: setState marca el widget como sucio para que Flutter lo redibuje con el valor nuevo. Mutación sin setState = estado cambiado pero UI vieja: el bug de todo novato.
- ❌ «Evita null» → Frente a «¿Por qué dentro de setState(() { cuenta++; })?» lo fácil es confundirse. **Verdad**: setState marca el widget como sucio para que Flutter lo redibuje con el valor nuevo. Mutación sin setState = estado cambiado pero UI vieja: el bug de todo novato.
- ❌ «En build» → Frente a «¿Dónde inicias un fetch o timer en un StatefulWidget?» lo fácil es confundirse. **Verdad**: En initState (corre una vez al crearse); y liberas sus recursos en dispose. build se ejecuta muchas veces: inicialización va en initState, limpieza en dispose.
- ❌ «En el constructor» → Frente a «¿Dónde inicias un fetch o timer en un StatefulWidget?» lo fácil es confundirse. **Verdad**: En initState (corre una vez al crearse); y liberas sus recursos en dispose. build se ejecuta muchas veces: inicialización va en initState, limpieza en dispose.

## 🩹 Antídoto universal
1. Lee el mensaje de error COMPLETO antes de googlear.
2. Pon el error exacto a la IA local y pide explicación, no solución.
3. Documenta el error en tu bitácora: error → causa → fix.
