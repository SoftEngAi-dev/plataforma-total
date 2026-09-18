# 🎤 Banco de entrevista — DevOps y CI/CD — De Tu PC a Producción Sin Sudor

> 12 preguntas esenciales + guía de respuestas las que ya sabes del curso

## 🔥 Fundamentales (del contenido del curso)

1. **¿Qué es CI (Integración Continua)?**
   - Automatizar build+tests en cada push para detectar roturas al instante  _(Commits integrados y probados constantemente: el bug se detecta cuando es pequeño.)_

2. **¿Qué diferencia hay entre entrega y despliegue continuos?**
   - Entrega: listo para publicar con un clic; Despliegue: se publica AUTOMÁTICAMENTE al pasar CI  _(Delivery = siempre desplegable (decisión humana); Deployment = se hace solo.)_

3. **¿Qué hace runs-on: ubuntu-latest?**
   - Define la imagen de máquina virtual limpia de GitHub que ejecutará el job  _(Cada job arranca en una VM limpia; por eso hay que instalar dependencias en los steps.)_

4. **¿Dónde debe vivir el archivo del workflow?**
   - .github/workflows/*.yml  _(GitHub solo reconoce los workflows en esa ruta exacta.)_

5. **¿Por qué la pirámide tiene más tests unitarios que E2E?**
   - Unitarios = rápidos, estables y baratos; E2E = lentos, frágiles y caros (manténlos pocos)  _(La base ancha de unit tests cubre lógica; los pocos E2E verifican el cableado.)_

6. **¿Qué debe evitar un test unitario?**
   - Tocar red/BD/reloj reales (úsese mocks/fakes) para ser rápido, repetible y confiable  _(Un test que depende del internet es un test que fallará a las 3am cuando menos lo esperas.)_

7. **¿Para qué existe staging?**
   - Ambiente IDÉNTICO a producción donde validar antes del deploy real  _(Los bugs 'solo-pasan-en-prod' se atrapan en staging.)_

8. **¿Qué regala Docker al momento de rollback?**
   - La versión anterior sigue como imagen: vuelves a correr esa y listo, sin reinstalar  _(Inmutabilidad de imágenes = tiempo de restauración en segundos.)_

9. **¿Qué niveles correctos de logs distinguen?**
   - DEBUG/INFO/WARNING/ERROR — filtras según la gravedad y el ambiente  _(En prod corre INFO+; en dev activas DEBUG. El ruido bien dosificado vale oro.)_

10. **¿Qué verifica un endpoint /health?**
   - Que la aplicación responde (200) — monitores externos lo sondean periódicamente  _(Healthcheck es el '¿sigues viva?' de toda app desplegada: bases de alertas.)_

11. **¿Por qué romper un test a propósito en el proyecto?**
   - Verificar que el pipeline REALMENTE falla ante errores (red validate que CI funciona)  _(Un CI que nunca has visto fallar no es garantía: red/verde/red lo prueba.)_

12. **¿Qué diferencia el despliegue continuo del push manual a un VPS?**
   - Todo paso manual se automatiza: tras CI verde la app llega sola al usuario, sin intervención humana  _(La ausencia de pasos manuales es la ausencia de errores manuales.)_

## 🧗 Profundización (prepáralas explicando en voz alta)
- ¿Qué problema real resuelve DevOps y CI/CD y cuándo NO lo usarías?
- Explica el concepto más fuerte del curso sin usar jerga.
- Contrasta DevOps y CI/CD con una alternativa: pros/contras.
- Cuenta un error típico de novato en este tema y cómo lo evitas.

## ⭐ Método para contestarlas
1. **Responde en 60 segundos** cada una de las fundamentales, de memoria. Las que tartamudean → repásalas (flashcards/).
2. Graba tu voz en 2 y escúchate: claridad y precisión importan tanto como el contenido técnico.
3. Una respuesta buena = definición (1 línea) + ejemplo (1) + por qué importa (1).
