# 3. Spring Boot: API REST en 15 líneas de verdad

> 📚 Curso: **Java y Spring — El Backend del Mundo Empresarial** · Lección 3 de 5
> 🗓 Exportado: 18/09/2026 desde Plataforma Total
> 🍅 Sugerencia: 1-2 pomodoros para leer + practicar

---

## 📖 Contenido

```java
SPRING BOOT: JAVA QUE CORRE COMO EXPRESS
━━━━━━━━━━━━━━━━━━━━━━━━━━━
  // build (maven) → spring-boot-starter-web. start.spring.io genera el proyecto listo.

  @RestController
  @RequestMapping("/api/tareas")
  public class TareaController {
      private final List<Tarea> tareas = new ArrayList<>();

      @GetMapping
      public List<Tarea> todas() { return tareas; }

      @PostMapping
      @ResponseStatus(HttpStatus.CREATED)
      public Tarea crear(@RequestBody Tarea t) { tareas.add(t); return t; }

      @GetMapping("/{id}")
      public Tarea una(@PathVariable int id) {
          return tareas.stream().filter(t -> t.id() == id).findFirst()
              .orElseThrow(() -> new ResponseStatusException(HttpStatus.NOT_FOUND));
      }
  }

INIECCIÓN DE DEPENDENCIAS (la magia Spring): tú diseñes interfaces y recibes implementaciones por constructor — testing y cambio de implementación gratis.

Spring Boot corere con su servidor incluido: mvn spring-boot:run → localhost:8080/api/tareas.
Auto-configuración: detecta qué hay en el classpath (maven deps) y configura solo: JSON, BD, seguridad.
```

---

## 📝 Quiz de la lección

### 1. ¿Qué hace @RestController?
- A) Decora
- B) Declara la clase como controlador web: los métodos responden HTTP y devuelven datos serializados (JSON)
- C) Conecta BD
- D) Corre tests
### 2. ¿Qué es inyección de dependencias en Spring?
- A) SQL
- B) El framework crea y entrega los objetos que necesita tu clase por el constructor: cambiar implementación sin tocar tu código
- C) Npm install
- D) Herencia

---

## 🔑 Respuestas y explicaciones

**1.** ✅ Declara la clase como controlador web: los métodos responden HTTP y devuelven datos serializados (JSON) — @RestController = @Controller + @ResponseBody: todo método = respuesta JSON directa.
**2.** ✅ El framework crea y entrega los objetos que necesita tu clase por el constructor: cambiar implementación sin tocar tu código — Recibes lo que necesitas; no lo construyes: testeo con mocks y evolución sin drama.

---
✅ Al terminar, marca la lección como completada en la app (📚 Aprender → ✅ Completada)
