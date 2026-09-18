# ⚠️ Errores comunes — 5. Proyecto: API Java/Spring completa

> Java y Spring — El Backend del Mundo Empresarial · Lección 5 · Aprender de los errores (propios y ajenos)

- ❌ «Un hámster» → Frente a «¿Qué es H2 en este proyecto?» lo fácil es confundirse. **Verdad**: Base de datos SQL embebida/en memoria para desarrollo rápido, reemplazable luego por PostgreSQL sin tocar el código JPA. H2 para arrancar sin instalar BD; cambia el datasource y punto: eso es abstracción ORM.
- ❌ «Un navegador» → Frente a «¿Qué es H2 en este proyecto?» lo fácil es confundirse. **Verdad**: Base de datos SQL embebida/en memoria para desarrollo rápido, reemplazable luego por PostgreSQL sin tocar el código JPA. H2 para arrancar sin instalar BD; cambia el datasource y punto: eso es abstracción ORM.
- ❌ «El código fuente» → Frente a «¿Qué genera el .jar empaquetado con spring-boot:package?» lo fácil es confundirse. **Verdad**: Un ejecutable autocontenido (app+servidor Tomcat embebido): dockerizar es trivial. El fat jar = tu app + servidor interno: corre en cualquier JVM sola.
- ❌ «JS» → Frente a «¿Qué genera el .jar empaquetado con spring-boot:package?» lo fácil es confundirse. **Verdad**: Un ejecutable autocontenido (app+servidor Tomcat embebido): dockerizar es trivial. El fat jar = tu app + servidor interno: corre en cualquier JVM sola.

## 🩹 Antídoto universal
1. Lee el mensaje de error COMPLETO antes de googlear.
2. Pon el error exacto a la IA local y pide explicación, no solución.
3. Documenta el error en tu bitácora: error → causa → fix.
