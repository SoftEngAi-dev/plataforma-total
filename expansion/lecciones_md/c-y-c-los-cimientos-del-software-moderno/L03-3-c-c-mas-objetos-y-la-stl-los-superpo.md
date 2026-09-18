# 3. C++: C más objetos y la STL (los superpoderes)

> 📚 Curso: **C y C++ — Los Cimientos del Software Moderno** · Lección 3 de 5
> 🗓 Exportado: 18/09/2026 desde Plataforma Total
> 🍅 Sugerencia: 1-2 pomodoros para leer + practicar

---

## 📖 Contenido

```cpp
C++: C CON SUPERPOBLACIÓN (ENORME Y POTENTE)
━━━━━━━━━━━━━━━━━━━━━━━━━━━
C++ = C 98% válido + clases, templates, excepciones y la Standard Template Library (STL). Juegos (Unreal), Chrome, MySQL, Tesla, trading: el software rápido de verdad.

  #include <iostream>
  #include <vector>
  #include <string>
  using namespace std;
  int main() {
      string nombre = "Ada";                    // string de verdad (no char*)
      vector<int> nums = {1, 2, 3, 4, 5};       // array dinámico seguro
      nums.push_back(6);
      for (int n : nums) cout << n << " ";      // for-range moderno
      cout << endl;

      auto doble = [](int x) { return x * 2; }; // lambdas (C++11)
      sort(nums.begin(), nums.end());            // algoritmos STL
  }

CLASES (POO verdadera)
  class Tarea {
      string titulo; bool hecha = false;
  public:
      Tarea(const string& t) : titulo(t) {}    // constructor
      void completar() { hecha = true; }
  };

RAII (la GRAN IDEA de C++): los recursos (memoria, archivos, locks) se liberan solos cuando el objeto sale de scope → es el origen del design de Rust. new/delete (o mejor: punteros inteligentes unique_ptr/shared_ptr).
```

---

## 📝 Quiz de la lección

### 1. ¿Qué aporta vector<T> de la STL respecto a arrays C?
- A) Nada
- B) Array dinámico gestionado: crece solo, sabe su tamaño, sin malloc/free manual
- C) Es de Java
- D) Es lento por obligación
### 2. ¿Qué es RAII en C++?
- A) Un error
- B) Adquisición/liberación de recursos ligada al ciclo de vida de objetos: scope-ended = recurso liberado (origen del modelo que perfecciona Rust)
- C) Una clase
- D) Excepción

---

## 🔑 Respuestas y explicaciones

**1.** ✅ Array dinámico gestionado: crece solo, sabe su tamaño, sin malloc/free manual — vector + string + sort + map = la STL: productividad C++, sin pelear malloc manual.
**2.** ✅ Adquisición/liberación de recursos ligada al ciclo de vida de objetos: scope-ended = recurso liberado (origen del modelo que perfecciona Rust) — Destructor al salir del bloque: no olvidas liberar; es la contra a los leaks/locks olvidados.

---
✅ Al terminar, marca la lección como completada en la app (📚 Aprender → ✅ Completada)
