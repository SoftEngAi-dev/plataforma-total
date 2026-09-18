# ⚠️ Errores comunes — 6. Proyecto: pipeline CI/CD real para tu app

> DevOps y CI/CD — De Tu PC a Producción Sin Sudor · Lección 6 · Aprender de los errores (propios y ajenos)

- ❌ «Por diversión» → Frente a «¿Por qué romper un test a propósito en el proyecto?» lo fácil es confundirse. **Verdad**: Verificar que el pipeline REALMENTE falla ante errores (red validate que CI funciona). Un CI que nunca has visto fallar no es garantía: red/verde/red lo prueba.
- ❌ «Para practicar git» → Frente a «¿Por qué romper un test a propósito en el proyecto?» lo fácil es confundirse. **Verdad**: Verificar que el pipeline REALMENTE falla ante errores (red validate que CI funciona). Un CI que nunca has visto fallar no es garantía: red/verde/red lo prueba.
- ❌ «El precio» → Frente a «¿Qué diferencia el despliegue continuo del push manual a un VPS?» lo fácil es confundirse. **Verdad**: Todo paso manual se automatiza: tras CI verde la app llega sola al usuario, sin intervención humana. La ausencia de pasos manuales es la ausencia de errores manuales.
- ❌ «Nada cambia» → Frente a «¿Qué diferencia el despliegue continuo del push manual a un VPS?» lo fácil es confundirse. **Verdad**: Todo paso manual se automatiza: tras CI verde la app llega sola al usuario, sin intervención humana. La ausencia de pasos manuales es la ausencia de errores manuales.

## 🩹 Antídoto universal
1. Lee el mensaje de error COMPLETO antes de googlear.
2. Pon el error exacto a la IA local y pide explicación, no solución.
3. Documenta el error en tu bitácora: error → causa → fix.
