# ⚠️ Errores comunes — 3. Deshacer: checkout, restore, revert, reset (la tabla salvadora)

> Git y GitHub — Tu Historia Nunca Se Pierde · Lección 3 · Aprender de los errores (propios y ajenos)

- ❌ «reset --hard» → Frente a «git revert vs git reset — ¿cuál es seguro en commits compartidos?» lo fácil es confundirse. **Verdad**: revert (crea commit inverso sin reescribir la historia ya publicada). Reescribir historia compartida rompe a tus compañeros; revert es la forma polite.
- ❌ «igual» → Frente a «git revert vs git reset — ¿cuál es seguro en commits compartidos?» lo fácil es confundirse. **Verdad**: revert (crea commit inverso sin reescribir la historia ya publicada). Reescribir historia compartida rompe a tus compañeros; revert es la forma polite.
- ❌ «Borrar todo» → Frente a «git stash sirve para...» lo fácil es confundirse. **Verdad**: Apartar cambios sin commit y retomarlos luego (stash pop). El cajón rápido: limpio el área, atiendo la urgencia, recupero lo mío.
- ❌ «Subir cambios» → Frente a «git stash sirve para...» lo fácil es confundirse. **Verdad**: Apartar cambios sin commit y retomarlos luego (stash pop). El cajón rápido: limpio el área, atiendo la urgencia, recupero lo mío.

## 🩹 Antídoto universal
1. Lee el mensaje de error COMPLETO antes de googlear.
2. Pon el error exacto a la IA local y pide explicación, no solución.
3. Documenta el error en tu bitácora: error → causa → fix.
