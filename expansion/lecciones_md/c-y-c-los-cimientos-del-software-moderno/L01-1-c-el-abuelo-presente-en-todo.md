# 1. C: el abuelo presente en TODO

> 📚 Curso: **C y C++ — Los Cimientos del Software Moderno** · Lección 1 de 5
> 🗓 Exportado: 18/09/2026 desde Plataforma Total
> 🍅 Sugerencia: 1-2 pomodoros para leer + practicar

---

## 📖 Contenido

```cpp
C: 1972 Y SIGUE CORRIENDO EL MUNDO
━━━━━━━━━━━━━━━━━━━━━━━━━━━
Linux, Git, PostgreSQL, Python (¡está escrito en C!), el kernel de tu celu: TODO corre sobre C.
Aprender C = entender cómo funcionan TODOS los demás lenguajes por debajo.

  // hola.c
  #include <stdio.h>                 // stdio: print/scan
  int main(void) {
      char nombre[] = "Ada";         // string = array de char (¡Rust/Go lo heredan!)
      int edad = 36;
      printf("Hola %s, tienes %d años
", nombre, edad);   // placeholders %s %d %.2f

      int nums[5] = {10, 20, 30};    // array fijo
      for (int i = 0; i < 5; i++) printf("%d ", nums[i]);

      // funciones (declaradas antes de usarse o con prototipo arriba):
      // int area(int base, int altura);
      return 0;
  }

  gcc hola.c -o hola && ./hola      ← compilar + correr

DECLARACIONES EXPLÍCITAS siempre (int edad;); sin bool nativo antes de C99 (int 0/1); memoria manual (malloc/free, próxima lección). Verás cadenas de formato: %d=int,%f=float,%s=string,%c=char.
```

---

## 📝 Quiz de la lección

### 1. ¿Por qué aprender C hoy si 'no lo usaré directo'?
- A) Nostalgia
- B) Es el substrato real: memoria, punteros y bajo nivel explican el comportamiento de TODOS los demás lenguajes actuales
- C) Es gratis
- D) Es fácil
### 2. ¿Qué hace printf("%d", x)?
- A) Imprime 5
- B) Imprime valores donde %d es el placeholder de un entero (y %s string, %f float...)
- C) Lee input
- D) Error

---

## 🔑 Respuestas y explicaciones

**1.** ✅ Es el substrato real: memoria, punteros y bajo nivel explican el comportamiento de TODOS los demás lenguajes actuales — 'Entender realmente' qué hace tu lenguaje favorito = haber pasado por C.
**2.** ✅ Imprime valores donde %d es el placeholder de un entero (y %s string, %f float...) — String de formato con marcadores posicionales: el printf-family clásico.

---
✅ Al terminar, marca la lección como completada en la app (📚 Aprender → ✅ Completada)
