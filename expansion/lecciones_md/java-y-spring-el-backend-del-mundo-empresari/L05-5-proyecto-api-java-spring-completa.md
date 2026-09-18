# 5. Proyecto: API Java/Spring completa

> 📚 Curso: **Java y Spring — El Backend del Mundo Empresarial** · Lección 5 de 5
> 🗓 Exportado: 18/09/2026 desde Plataforma Total
> 🍅 Sugerencia: 1-2 pomodoros para leer + practicar

---

## 📖 Contenido

```java
CONSTRUYE: API DE TAREAS SPRING SERIO
━━━━━━━━━━━━━━━━━━━━━━━━━━━
SETUP (10 min)
1. start.spring.io → Project Maven, Java 17+, dependencias: Spring Web + Spring Data JPA + H2 (BD embebida para dev)
2. Descomprime e importa a tu IDE (IntelliJ Community gratis)

CÓDIGO (lo aprendido en orden)
1. record Tarea(Long id, String titulo, Boolean hecha) {}  → record para el DTO
2. @Entity clase Tarea para JPA (o usa el record como DTO y entidad aparte)
3. TareaRepo extends JpaRepository<Tarea, Long> con findByHechaFalse()
4. @RestController /api/tareas: GET todas + pendientes · POST crear · PATCH {id} alternar · DELETE {id}
5. application.properties:
   spring.datasource.url=jdbc:h2:mem:tareas · spring.h2.console.enabled=true
   → consola web H2 en localhost:8080/h2-console para ver tus datos en vivo
6. Ejecuta: mvn spring-boot:run
7. Prueba: curl localhost:8080/api/tareas

BONUS (siguiente nivel realista):
• Validación: spring-boot-starter-validation + @Valid + @NotBlank en los DTOs
• Tests: @SpringBootTest o @DataJpaTest
• Dockeriza tu jar: FROM eclipse-temurin:17-jre + COPY target/*.jar + CMD java -jar

Con eso ya tienes un backend Java real: el idiom del 30% de las empresas.
```

---

## 📝 Quiz de la lección

### 1. ¿Qué es H2 en este proyecto?
- A) Un hámster
- B) Base de datos SQL embebida/en memoria para desarrollo rápido, reemplazable luego por PostgreSQL sin tocar el código JPA
- C) Un navegador
- D) Un test
### 2. ¿Qué genera el .jar empaquetado con spring-boot:package?
- A) El código fuente
- B) Un ejecutable autocontenido (app+servidor Tomcat embebido): dockerizar es trivial
- C) JS
- D) Los tests

---

## 🔑 Respuestas y explicaciones

**1.** ✅ Base de datos SQL embebida/en memoria para desarrollo rápido, reemplazable luego por PostgreSQL sin tocar el código JPA — H2 para arrancar sin instalar BD; cambia el datasource y punto: eso es abstracción ORM.
**2.** ✅ Un ejecutable autocontenido (app+servidor Tomcat embebido): dockerizar es trivial — El fat jar = tu app + servidor interno: corre en cualquier JVM sola.

---
✅ Al terminar, marca la lección como completada en la app (📚 Aprender → ✅ Completada)
