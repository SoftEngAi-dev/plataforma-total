# ⚠️ Errores comunes — 1. El SFC y la reactividad con ref()

> 💚 Vue 3 — Composition API en Serio · Lección 1 · Aprender de los errores (propios y ajenos)

- ❌ «contador++» → Frente a «¿Cómo incrementas un ref dentro del <script setup>?» lo fácil es confundirse. **Verdad**: contador.value++. En el script los refs se manipulan con .value; en el template Vue lo desenvuelve automáticamente.
- ❌ «setContador(contador + 1)» → Frente a «¿Cómo incrementas un ref dentro del <script setup>?» lo fácil es confundirse. **Verdad**: contador.value++. En el script los refs se manipulan con .value; en el template Vue lo desenvuelve automáticamente.
- ❌ «html, css y js» → Frente a «¿Qué tres bloques suele tener un Single File Component?» lo fácil es confundirse. **Verdad**: script, template y style. El SFC agrupa lógica (script), vista (template) y estilos (style) en un solo archivo .vue.
- ❌ «setup, render y mount» → Frente a «¿Qué tres bloques suele tener un Single File Component?» lo fácil es confundirse. **Verdad**: script, template y style. El SFC agrupa lógica (script), vista (template) y estilos (style) en un solo archivo .vue.

## 🩹 Antídoto universal
1. Lee el mensaje de error COMPLETO antes de googlear.
2. Pon el error exacto a la IA local y pide explicación, no solución.
3. Documenta el error en tu bitácora: error → causa → fix.
