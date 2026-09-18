# ⚠️ Errores comunes — 1. Git mental: qué es un commit

> Git y GitHub — Tu Historia Nunca Se Pierde · Lección 1 · Aprender de los errores (propios y ajenos)

- ❌ «Un diff de cambios» → Frente a «¿Qué es un commit en git?» lo fácil es confundirse. **Verdad**: Un snapshot completo del proyecto con puntero al commit padre. Cada commit = foto completa; git las deduplica internamente (objetos).
- ❌ «Un archivo zip» → Frente a «¿Qué es un commit en git?» lo fácil es confundirse. **Verdad**: Un snapshot completo del proyecto con puntero al commit padre. Cada commit = foto completa; git las deduplica internamente (objetos).
- ❌ «commit → add» → Frente a «¿Cuál es el orden del flujo básico?» lo fácil es confundirse. **Verdad**: editar → git add → git commit. Working → staging (add) → repo (commit). push va aparte al remoto.
- ❌ «push → commit» → Frente a «¿Cuál es el orden del flujo básico?» lo fácil es confundirse. **Verdad**: editar → git add → git commit. Working → staging (add) → repo (commit). push va aparte al remoto.

## 🩹 Antídoto universal
1. Lee el mensaje de error COMPLETO antes de googlear.
2. Pon el error exacto a la IA local y pide explicación, no solución.
3. Documenta el error en tu bitácora: error → causa → fix.
