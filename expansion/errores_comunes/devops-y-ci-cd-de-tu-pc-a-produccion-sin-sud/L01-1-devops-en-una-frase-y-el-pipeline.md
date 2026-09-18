# ⚠️ Errores comunes — 1. DevOps en una frase y el pipeline

> DevOps y CI/CD — De Tu PC a Producción Sin Sudor · Lección 1 · Aprender de los errores (propios y ajenos)

- ❌ «Un lenguaje» → Frente a «¿Qué es CI (Integración Continua)?» lo fácil es confundirse. **Verdad**: Automatizar build+tests en cada push para detectar roturas al instante. Commits integrados y probados constantemente: el bug se detecta cuando es pequeño.
- ❌ «Un servidor» → Frente a «¿Qué es CI (Integración Continua)?» lo fácil es confundirse. **Verdad**: Automatizar build+tests en cada push para detectar roturas al instante. Commits integrados y probados constantemente: el bug se detecta cuando es pequeño.
- ❌ «Ninguna» → Frente a «¿Qué diferencia hay entre entrega y despliegue continuos?» lo fácil es confundirse. **Verdad**: Entrega: listo para publicar con un clic; Despliegue: se publica AUTOMÁTICAMENTE al pasar CI. Delivery = siempre desplegable (decisión humana); Deployment = se hace solo.
- ❌ «Despliegue es más lento» → Frente a «¿Qué diferencia hay entre entrega y despliegue continuos?» lo fácil es confundirse. **Verdad**: Entrega: listo para publicar con un clic; Despliegue: se publica AUTOMÁTICAMENTE al pasar CI. Delivery = siempre desplegable (decisión humana); Deployment = se hace solo.

## 🩹 Antídoto universal
1. Lee el mensaje de error COMPLETO antes de googlear.
2. Pon el error exacto a la IA local y pide explicación, no solución.
3. Documenta el error en tu bitácora: error → causa → fix.
