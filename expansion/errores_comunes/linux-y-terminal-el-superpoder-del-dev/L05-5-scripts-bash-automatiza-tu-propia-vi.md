# ⚠️ Errores comunes — 5. Scripts Bash: automatiza tu propia vida

> Linux y Terminal — El Superpoder del Dev · Lección 5 · Aprender de los errores (propios y ajenos)

- ❌ «Son bonitas» → Frente a «¿Por qué siempre "comillas dobles" en variables de bash?» lo fácil es confundirse. **Verdad**: Sin ellas, valores con espacios se rompen en múltiples argumentos (bugs y desastres). rm $f → rm dos cosas si f="mi archivo.txt"; rm "$f" → correcto.
- ❌ «Van más rápido» → Frente a «¿Por qué siempre "comillas dobles" en variables de bash?» lo fácil es confundirse. **Verdad**: Sin ellas, valores con espacios se rompen en múltiples argumentos (bugs y desastres). rm $f → rm dos cosas si f="mi archivo.txt"; rm "$f" → correcto.
- ❌ «Depurar» → Frente a «set -euo pipefail permite...» lo fácil es confundirse. **Verdad**: Fallar rápido y claramente: el script se detiene ante errores en vez de continuar roto. Script que sigue tras error suele causar más daño que uno que para.
- ❌ «Logs bonitos» → Frente a «set -euo pipefail permite...» lo fácil es confundirse. **Verdad**: Fallar rápido y claramente: el script se detiene ante errores en vez de continuar roto. Script que sigue tras error suele causar más daño que uno que para.

## 🩹 Antídoto universal
1. Lee el mensaje de error COMPLETO antes de googlear.
2. Pon el error exacto a la IA local y pide explicación, no solución.
3. Documenta el error en tu bitácora: error → causa → fix.
