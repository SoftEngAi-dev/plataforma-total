# ⚠️ Errores comunes — 2. Capturar grupos y.los casos reales: validación y extracción

> Expresiones Regulares — El Lenguaje de Patrones · Lección 2 · Aprender de los errores (propios y ajenos)

- ❌ «Nada especial» → Frente a «¿Qué hace (?P<nombre>...) en Python regex?» lo fácil es confundirse. **Verdad**: Grupo NOMBRADO: extraes por m.group('nombre') en vez de factores posición brittle. Regex autocomentados: los nombres documentan cada parte que capturas.
- ❌ «Ordena» → Frente a «¿Qué hace (?P<nombre>...) en Python regex?» lo fácil es confundirse. **Verdad**: Grupo NOMBRADO: extraes por m.group('nombre') en vez de factores posición brittle. Regex autocomentados: los nombres documentan cada parte que capturas.
- ❌ «Neutro» → Frente a «¿Qué logra el lookahead (?=.*[A-Z]) en la contraseña?» lo fácil es confundirse. **Verdad**: VERIFICA sin consumir: exige que exista una mayúscula en lo que sigue sin avanzar el cursor. Lookaheads = 'debe cumplirse X adelante': validaciones compuestas sin complicar los grupos.
- ❌ «Ordena letras» → Frente a «¿Qué logra el lookahead (?=.*[A-Z]) en la contraseña?» lo fácil es confundirse. **Verdad**: VERIFICA sin consumir: exige que exista una mayúscula en lo que sigue sin avanzar el cursor. Lookaheads = 'debe cumplirse X adelante': validaciones compuestas sin complicar los grupos.

## 🩹 Antídoto universal
1. Lee el mensaje de error COMPLETO antes de googlear.
2. Pon el error exacto a la IA local y pide explicación, no solución.
3. Documenta el error en tu bitácora: error → causa → fix.
