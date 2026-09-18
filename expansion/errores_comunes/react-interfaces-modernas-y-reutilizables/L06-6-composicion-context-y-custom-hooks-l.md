# ⚠️ Errores comunes — 6. Composición, context y custom hooks: las 3 escaleras

> React — Interfaces Modernas y Reutilizables · Lección 6 · Aprender de los errores (propios y ajenos)

- ❌ «Desde el primer día» → Frente a «¿Cuándo llegar a Context?» lo fácil es confundirse. **Verdad**: Cuando muchos componentes a mucha profundidad necesitan el mismo dato (tema, usuario, idioma). Context resuelve prop-drilling global; estado local y composición resuelven la mayoría de los casos.
- ❌ «Para todo el estado» → Frente a «¿Cuándo llegar a Context?» lo fácil es confundirse. **Verdad**: Cuando muchos componentes a mucha profundidad necesitan el mismo dato (tema, usuario, idioma). Context resuelve prop-drilling global; estado local y composición resuelven la mayoría de los casos.
- ❌ «Cualquier lugar del archivo» → Frente a «¿Qué reglas tienen los hooks (useState, useEffect, customs)?» lo fácil es confundirse. **Verdad**: Top-level del componente, sin loops/ifs, nombres use*. El orden fijo de llamadas es cómo React empareja hook con celda de estado: romperlo = caos.
- ❌ «Solo en useEffect» → Frente a «¿Qué reglas tienen los hooks (useState, useEffect, customs)?» lo fácil es confundirse. **Verdad**: Top-level del componente, sin loops/ifs, nombres use*. El orden fijo de llamadas es cómo React empareja hook con celda de estado: romperlo = caos.

## 🩹 Antídoto universal
1. Lee el mensaje de error COMPLETO antes de googlear.
2. Pon el error exacto a la IA local y pide explicación, no solución.
3. Documenta el error en tu bitácora: error → causa → fix.
