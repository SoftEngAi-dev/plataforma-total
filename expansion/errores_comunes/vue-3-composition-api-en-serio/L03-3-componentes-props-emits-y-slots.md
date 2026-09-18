# ⚠️ Errores comunes — 3. Componentes: props, emits y slots

> 💚 Vue 3 — Composition API en Serio · Lección 3 · Aprender de los errores (propios y ajenos)

- ❌ «Mutando la prop directamente» → Frente a «¿Cómo comunica un componente hijo a su padre en Vue?» lo fácil es confundirse. **Verdad**: Emitiendo un evento personalizado con emit(). Las props bajan, los eventos suben: el hijo emite, el padre decide qué hacer.
- ❌ «Escribiendo en localStorage» → Frente a «¿Cómo comunica un componente hijo a su padre en Vue?» lo fácil es confundirse. **Verdad**: Emitiendo un evento personalizado con emit(). Las props bajan, los eventos suben: el hijo emite, el padre decide qué hacer.
- ❌ «Hacer peticiones HTTP» → Frente a «¿Para qué sirve provide/inject?» lo fácil es confundirse. **Verdad**: Pasar datos a descendientes lejanos sin retransmitir props intermedias. provide publica un valor en el árbol; inject lo consume a cualquier profundidad.
- ❌ «Definir rutas» → Frente a «¿Para qué sirve provide/inject?» lo fácil es confundirse. **Verdad**: Pasar datos a descendientes lejanos sin retransmitir props intermedias. provide publica un valor en el árbol; inject lo consume a cualquier profundidad.

## 🩹 Antídoto universal
1. Lee el mensaje de error COMPLETO antes de googlear.
2. Pon el error exacto a la IA local y pide explicación, no solución.
3. Documenta el error en tu bitácora: error → causa → fix.
