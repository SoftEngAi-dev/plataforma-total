# 2. Java moderno: records, streams y switch nuevo

> 📚 Curso: **Java y Spring — El Backend del Mundo Empresarial** · Lección 2 de 5
> 🗓 Exportado: 18/09/2026 desde Plataforma Total
> 🍅 Sugerencia: 1-2 pomodoros para leer + practicar

---

## 📖 Contenido

```java
JAVA DEL 2020 EN ADELANTE SE SIENTE MODERNO
━━━━━━━━━━━━━━━━━━━━━━━━━━━
RECORDS — clases de datos sin boilerplate:
  record Punto(int x, int y) {}
  var p = new Punto(1, 2);   p.x();    // accessor gratis, toString/equals gratis

STREAMS — el map/filter/reduce de Java:
  List<Integer> nums = List.of(1, 2, 3, 4, 5);
  int sumaPares = nums.stream()
      .filter(n -> n % 2 == 0)
      .mapToInt(n -> n * 10)
      .sum();
  System.out.println(sumaPares);      // 60

OPTIONAL — adiós NullPointerException por deliberación:
  Optional<Usuario> tal = repo.findById(1);
  tal.ifPresent(u -> System.out.println(u.getNombre()));
  String nombre = tal.map(Usuario::getNombre).orElse("invitado");

SWITCH EXPRESIVO (Java 14+):
  String tipo = switch (dia) {
      case SABADO, DOMINGO -> "finde";
      default -> "lectivo";
  };

TEXT BLOCKS (String json = comillas triples como delimitador): texto literal multilinea
      sin escapar comillas ni saltos — ideal para JSON/SQL embebido en Java.
```

---

## 📝 Quiz de la lección

### 1. ¿Qué resuelve Optional<T>?
- A) Nada
- B) Representa explícitamente la posible ausencia de valor: obliga a decidir (orElse, ifPresent) en vez de explotar con null
- C) Async
- D) Velocidad
### 2. streams en Java se parecen a...
- A) bucles for
- B) map/filter/reduce encadenados estilo funcional como en JS/Python
- C) clases
- D) SQL nada más

---

## 🔑 Respuestas y explicaciones

**1.** ✅ Representa explícitamente la posible ausencia de valor: obliga a decidir (orElse, ifPresent) en vez de explotar con null — Hacer visible el 'puede faltar' en el TIPO es el antídoto contra NullPointerException.
**2.** ✅ map/filter/reduce encadenados estilo funcional como en JS/Python — Operaciones declarativas sobre colecciones — Java moderno abraza lo funcional.

---
✅ Al terminar, marca la lección como completada en la app (📚 Aprender → ✅ Completada)
