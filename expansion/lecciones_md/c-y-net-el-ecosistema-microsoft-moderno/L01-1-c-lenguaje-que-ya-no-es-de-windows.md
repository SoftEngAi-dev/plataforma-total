# 1. C#: lenguaje que ya no es 'de Windows'

> 📚 Curso: **C# y .NET — El Ecosistema Microsoft Moderno** · Lección 1 de 4
> 🗓 Exportado: 18/09/2026 desde Plataforma Total
> 🍅 Sugerencia: 1-2 pomodoros para leer + practicar

---

## 📖 Contenido

```csharp
C#/.NET: MULTIPLATAFORMA Y RÁPIDO
━━━━━━━━━━━━━━━━━━━━━━━━━━━
.NET moderno (6+) corre Linux/Mac/Windows, es de los backends más rápidos del mundo (benchmarks top), y C# es un TypeScript con esteroides de arquitectura.

PRIMER APP (con el SDK de dotnet)
  dotnet new console -o MiApp && cd MiApp
  dotnet run

  // Program.cs (top-level: ¡sin boilerplate clase+Main!)
  Console.WriteLine("¡Hola desde C#!");
  string nombre = "Ada";
  int edad = 36;
  var pi = 3.14;                         // var = infiere tipo
  Console.WriteLine($"{nombre} tiene {edad}");   // interpolación $""

  // LINQ: map/filter/reduce estilo C#
  var nums = new List<int> { 1, 2, 3, 4, 5 };
  var paresX10 = nums.Where(n => n % 2 == 0).Select(n => n * 10).ToList();
  nums.Sum(); nums.Max();

FUERTEMENTE TIPADO con inferencia cómoda: te protege como TS pero el compilador lo ve todo.
NuGet = el npm: dotnet add package Newtonsoft.Json
```

---

## 📝 Quiz de la lección

### 1. ¿Qué hace el $ antes de una cadena en C#?
- A) Nada
- B) Habilita interpolación: $"{variable}" inserta valores
- C) Es regex
- D) Dinero
### 2. LINQ Where(...).Select(...) equivale a...
- A) SQL puro
- B) filter + map encadenados sobre colecciones, tipo JS/Python
- C) loops for
- D) bucles while

---

## 🔑 Respuestas y explicaciones

**1.** ✅ Habilita interpolación: $"{variable}" inserta valores — $"{nombre}" es la f-string/template literal de C#.
**2.** ✅ filter + map encadenados sobre colecciones, tipo JS/Python — LINQ es funcional sobre colecciones: es una de las mayores comodidades de C#.

---
✅ Al terminar, marca la lección como completada en la app (📚 Aprender → ✅ Completada)
