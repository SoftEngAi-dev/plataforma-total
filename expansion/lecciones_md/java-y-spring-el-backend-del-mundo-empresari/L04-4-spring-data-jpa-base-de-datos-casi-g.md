# 4. Spring Data JPA: base de datos casi gratis

> 📚 Curso: **Java y Spring — El Backend del Mundo Empresarial** · Lección 4 de 5
> 🗓 Exportado: 18/09/2026 desde Plataforma Total
> 🍅 Sugerencia: 1-2 pomodoros para leer + practicar

---

## 📖 Contenido

```java
JPA: TU BD COMO OBJETOS JAVA
━━━━━━━━━━━━━━━━━━━━━━━━━━━
ENTIDAD (tu tabla):
  @Entity
  public class Tarea {
      @Id @GeneratedValue
      private Long id;
      private String titulo;
      private boolean hecha;
      // getters/setters/constructor
  }

REPOSITORIO (¡sin escribir SQL!):
  public interface TareaRepo extends JpaRepository<Tarea, Long> {
      List<Tarea> findByHechaFalse();                // ¡Spring genera la query del nombre!
      List<Tarea> findByTituloContaining(String texto);
  }

USO EN EL CONTROLLER
  @GetMapping("/pendientes")
  public List<Tarea> pendientes() { return repo.findByHechaFalse(); }

POR QUÉ ES IMPORTANTE: JpaRepository ya trae save/findAll/findById/deleteById... y las derivadas (findByXAndYOrderByZ) se escriben SOLAS por convención de nombre. PostgreSQL/MySQL solo agregando el driver y el application.properties:
  spring.datasource.url=jdbc:postgresql://localhost/miapp
  spring.jpa.hibernate.ddl-auto=update       (crea el esquema a partir de las entidades)

En dev; en prod controla migraciones con Flyway.
```

---

## 📝 Quiz de la lección

### 1. ¿Qué hace JpaRepository con findByHechaFalse()?
- A) Nada
- B) Spring Data genera la query automáticamente a partir del NOMBRE del método (derivada por convención)
- C) SQL manual
- D) Error
### 2. ¿Qué papel tiene @Entity?
- A) Decoración
- B) Marca la clase como tabla de BD manejada por el ORM (cada instancia = fila)
- C) Seguridad
- D) Async

---

## 🔑 Respuestas y explicaciones

**1.** ✅ Spring Data genera la query automáticamente a partir del NOMBRE del método (derivada por convención) — Query derivation: nombras bien el método, la query existe sin escribirla.
**2.** ✅ Marca la clase como tabla de BD manejada por el ORM (cada instancia = fila) — El mapeo objeto-relacional (ORM): objetos Java ↔ filas SQL.

---
✅ Al terminar, marca la lección como completada en la app (📚 Aprender → ✅ Completada)
