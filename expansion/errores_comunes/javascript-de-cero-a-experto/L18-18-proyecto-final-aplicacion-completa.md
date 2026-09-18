# ⚠️ Errores comunes — 18. Proyecto final: aplicación completa de tareas (DOM + eventos + JSON)

> JavaScript — De Cero a Experto · Lección 18 · Aprender de los errores (propios y ajenos)

- ❌ «fetch GET y POST» → Frente a «¿Qué dos llamadas sincronizan la app con localStorage?» lo fácil es confundirse. **Verdad**: parse y stringify de JSON. stringify al guardar, parse al cargar: JSON es el puente.
- ❌ «push y pop» → Frente a «¿Qué dos llamadas sincronizan la app con localStorage?» lo fácil es confundirse. **Verdad**: parse y stringify de JSON. stringify al guardar, parse al cargar: JSON es el puente.
- ❌ «Es más corto» → Frente a «¿Por qué delegación de eventos en la lista en vez de listener por li?» lo fácil es confundirse. **Verdad**: Los li se recrean en cada render; un solo listener en el ul sigue funcionando siempre. Contenido dinámico = listener en el padre estable, acción según e.target.
- ❌ «Es requisito del DOM» → Frente a «¿Por qué delegación de eventos en la lista en vez de listener por li?» lo fácil es confundirse. **Verdad**: Los li se recrean en cada render; un solo listener en el ul sigue funcionando siempre. Contenido dinámico = listener en el padre estable, acción según e.target.

## 🩹 Antídoto universal
1. Lee el mensaje de error COMPLETO antes de googlear.
2. Pon el error exacto a la IA local y pide explicación, no solución.
3. Documenta el error en tu bitácora: error → causa → fix.
