# ⚠️ Errores comunes — 4. Proyecto: analizador de logs con regex (uso real)

> Expresiones Regulares — El Lenguaje de Patrones · Lección 4 · Aprender de los errores (propios y ajenos)

- ❌ «CSV» → Frente a «¿Qué hace groupdict() sobre un Match?» lo fácil es confundirse. **Verdad**: Devuelve un dictando con grupos NOMBRADOS para cada campo: linea→estructura lista para pandas/procesar. La puente: texto crudo → registro estructurado con nombres del grupo = pipeline real.
- ❌ «Error» → Frente a «¿Qué hace groupdict() sobre un Match?» lo fácil es confundirse. **Verdad**: Devuelve un dictando con grupos NOMBRADOS para cada campo: linea→estructura lista para pandas/procesar. La puente: texto crudo → registro estructurado con nombres del grupo = pipeline real.
- ❌ «Es cool» → Frente a «¿Por qué probar tu regex en regex101 con muestras primero?» lo fácil es confundirse. **Verdad**: Detectas backtracking/capturas raras/escapes al instante antes de correr sobre miliones de líneas y romper produción. Iteras el patrón en segundos con explicación en vivo; es la herramienta existente.
- ❌ «Por nada» → Frente a «¿Por qué probar tu regex en regex101 con muestras primero?» lo fácil es confundirse. **Verdad**: Detectas backtracking/capturas raras/escapes al instante antes de correr sobre miliones de líneas y romper produción. Iteras el patrón en segundos con explicación en vivo; es la herramienta existente.

## 🩹 Antídoto universal
1. Lee el mensaje de error COMPLETO antes de googlear.
2. Pon el error exacto a la IA local y pide explicación, no solución.
3. Documenta el error en tu bitácora: error → causa → fix.
