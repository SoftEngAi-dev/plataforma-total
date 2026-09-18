# ⚠️ Errores comunes — 3. Renderizar listas y condicionales

> React — Interfaces Modernas y Reutilizables · Lección 3 · Aprender de los errores (propios y ajenos)

- ❌ «id, por CSS» → Frente a «¿Qué prop requiere React al mapear elementos y por qué?» lo fácil es confundirse. **Verdad**: key: identidad estable entre renders para emparejar el DOM correctamente. La key es DNI, no apellido: el índice del map cambia y traiciona con listas dinámicas.
- ❌ «className, por estilos» → Frente a «¿Qué prop requiere React al mapear elementos y por qué?» lo fácil es confundirse. **Verdad**: key: identidad estable entre renders para emparejar el DOM correctamente. La key es DNI, no apellido: el índice del map cambia y traiciona con listas dinámicas.
- ❌ «Con if/else dentro de llaves» → Frente a «¿Cómo renderizar condicionalmente en JSX?» lo fácil es confundirse. **Verdad**: Operador &&, ternario, o variable calculada ANTES del return. JSX admite expresiones, no sentencias: la lógica va en expresiones o antes del return.
- ❌ «Con v-if» → Frente a «¿Cómo renderizar condicionalmente en JSX?» lo fácil es confundirse. **Verdad**: Operador &&, ternario, o variable calculada ANTES del return. JSX admite expresiones, no sentencias: la lógica va en expresiones o antes del return.

## 🩹 Antídoto universal
1. Lee el mensaje de error COMPLETO antes de googlear.
2. Pon el error exacto a la IA local y pide explicación, no solución.
3. Documenta el error en tu bitácora: error → causa → fix.
