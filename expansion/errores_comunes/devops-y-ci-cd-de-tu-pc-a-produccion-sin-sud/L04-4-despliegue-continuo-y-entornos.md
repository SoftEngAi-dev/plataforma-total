# ⚠️ Errores comunes — 4. Despliegue continuo y entornos

> DevOps y CI/CD — De Tu PC a Producción Sin Sudor · Lección 4 · Aprender de los errores (propios y ajenos)

- ❌ «Cuestión litúrgica» → Frente a «¿Para qué existe staging?» lo fácil es confundirse. **Verdad**: Ambiente IDÉNTICO a producción donde validar antes del deploy real. Los bugs 'solo-pasan-en-prod' se atrapan en staging.
- ❌ «Para guardar código» → Frente a «¿Para qué existe staging?» lo fácil es confundirse. **Verdad**: Ambiente IDÉNTICO a producción donde validar antes del deploy real. Los bugs 'solo-pasan-en-prod' se atrapan en staging.
- ❌ «Nada» → Frente a «¿Qué regala Docker al momento de rollback?» lo fácil es confundirse. **Verdad**: La versión anterior sigue como imagen: vuelves a correr esa y listo, sin reinstalar. Inmutabilidad de imágenes = tiempo de restauración en segundos.
- ❌ «Más CPU» → Frente a «¿Qué regala Docker al momento de rollback?» lo fácil es confundirse. **Verdad**: La versión anterior sigue como imagen: vuelves a correr esa y listo, sin reinstalar. Inmutabilidad de imágenes = tiempo de restauración en segundos.

## 🩹 Antídoto universal
1. Lee el mensaje de error COMPLETO antes de googlear.
2. Pon el error exacto a la IA local y pide explicación, no solución.
3. Documenta el error en tu bitácora: error → causa → fix.
