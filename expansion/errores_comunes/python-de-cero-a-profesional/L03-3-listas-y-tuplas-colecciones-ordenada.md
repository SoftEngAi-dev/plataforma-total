# ⚠️ Errores comunes — 3. Listas y tuplas: colecciones ordenadas

> Python — De Cero a Profesional · Lección 3 · Aprender de los errores (propios y ajenos)

- ❌ «Devuelve 3 elementos» → Frente a «¿Qué hace numeros[1:3]?» lo fácil es confundirse. **Verdad**: Devuelve los elementos en posiciones 1 y 2 (fin excluido). Slices: [inicio:fin) — la mitad de los bugs de principiante vienen del fin excluido.
- ❌ «Devuelve del 1 al 3 inclusive» → Frente a «¿Qué hace numeros[1:3]?» lo fácil es confundirse. **Verdad**: Devuelve los elementos en posiciones 1 y 2 (fin excluido). Slices: [inicio:fin) — la mitad de los bugs de principiante vienen del fin excluido.
- ❌ «Comparar» → Frente a «a, b = b, a hace...» lo fácil es confundirse. **Verdad**: Intercambiar los valores sin variable temporal (desempaquetado). La derecha se evalúa como tupla completa antes de asignar: el swap pythónico.
- ❌ «Error» → Frente a «a, b = b, a hace...» lo fácil es confundirse. **Verdad**: Intercambiar los valores sin variable temporal (desempaquetado). La derecha se evalúa como tupla completa antes de asignar: el swap pythónico.

## 🩹 Antídoto universal
1. Lee el mensaje de error COMPLETO antes de googlear.
2. Pon el error exacto a la IA local y pide explicación, no solución.
3. Documenta el error en tu bitácora: error → causa → fix.
