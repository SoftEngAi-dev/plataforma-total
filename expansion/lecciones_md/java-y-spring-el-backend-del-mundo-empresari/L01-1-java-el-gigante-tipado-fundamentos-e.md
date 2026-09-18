# 1. Java: el gigante tipado (fundamentos en 15 min)

> 📚 Curso: **Java y Spring — El Backend del Mundo Empresarial** · Lección 1 de 5
> 🗓 Exportado: 18/09/2026 desde Plataforma Total
> 🍅 Sugerencia: 1-2 pomodoros para leer + practicar

---

## 📖 Contenido

```java
JAVA: VERBOSO PERO SÓLIDO COMO ROCA
━━━━━━━━━━━━━━━━━━━━━━━━━━━
Instagram inicial, Netflix, bancos, Android: Java corre la economía. Lenguaje compilado, JVM, tipado ESTÁTICO.

  // Hola.java
  public class Hola {
      public static void main(String[] args) {        // entrada del programa
          String nombre = "Ada";
          int edad = 36;                              // tipos EXPLÍCITOS (pero...)
          var pi = 3.14;                              // var infiere (Java 10+)
          System.out.println("Hola, " + nombre + " tienes " + edad);

          if (edad >= 18) { System.out.println("Mayor"); }
          for (int i = 0; i < 3; i++) { System.out.println(i); }

          // colecciones:
          java.util.List<String> temas = new java.util.ArrayList<>();
          temas.add("spring"); temas.size(); temas.get(0);
      }
  }

  javac Hola.java && java Hola        ← compila y corre

CLAVE MENTAL JAVA: todo vive en clases; los tipos se verifican al compilar; la JVM lo corre en cualquier SO ("write once, run anywhere"). Maven/Gradle el gestor de paquetes+build (equivalente a npm/pip).
```

---

## 📝 Quiz de la lección

### 1. ¿Dónde empieza a ejecutar un programa Java?
- A) cualquier función
- B) El método public static void main(String[] args)
- C) En la clase
- D) En el constructor
### 2. ¿Qué es la JVM?
- A) Editor
- B) La máquina virtual que ejecuta el bytecode Java haciéndolo portable (una compilation, corre en to-do SO con JVM)
- C) Una librería
- D) Un navegador

---

## 🔑 Respuestas y explicaciones

**1.** ✅ El método public static void main(String[] args) — La firma exacta main es el punto de entrada universal de Java.
**2.** ✅ La máquina virtual que ejecuta el bytecode Java haciéndolo portable (una compilation, corre en to-do SO con JVM) — Compile once run anywhere: el bytecode .class corre en cualquier JVM.

---
✅ Al terminar, marca la lección como completada en la app (📚 Aprender → ✅ Completada)
