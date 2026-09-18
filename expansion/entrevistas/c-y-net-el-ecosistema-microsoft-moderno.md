# 🎤 Banco de entrevista — C# y .NET — El Ecosistema Microsoft Moderno

> 8 preguntas esenciales + guía de respuestas las que ya sabes del curso

## 🔥 Fundamentales (del contenido del curso)

1. **¿Qué hace el $ antes de una cadena en C#?**
   - Habilita interpolación: $"{variable}" inserta valores  _($"{nombre}" es la f-string/template literal de C#.)_

2. **LINQ Where(...).Select(...) equivale a...**
   - filter + map encadenados sobre colecciones, tipo JS/Python  _(LINQ es funcional sobre colecciones: es una de las mayores comodidades de C#.)_

3. **¿Qué es una Minimal API en .NET?**
   - El estilo conciso de ASP.NET Core: rutas con lambdas en Program.cs sin controladores pesados  _(Equivalente .NET a Express/Flask: ideal para APIs y microservicios.)_

4. **¿Qué tipo es record Tarea(...)?**
   - Tipo de datos inmutable con constructor/equals/desconstruct generados — el DTO perfecto  _(Records = POJOs cómodas: modelos limpios en una línea, igualdad por VALOR.)_

5. **¿Qué es DbContext en EF Core?**
   - La sesión/unidad de trabajo con la BD: DbSets por tabla y SaveChanges como transacción  _(DbContext coordina tracked changes y los persiste con SaveChanges: el corazón del ORM.)_

6. **¿Qué hacen las 'migraciones' de EF Core?**
   - Generan/aplican el esquema SQL desde tus clases C# y mantienen su historial versionado  _(El esquema de la BD vive en tu código: cambiar clase → migración → BD nueva consistente.)_

7. **¿Cómo recibe el endpoint la instancia AppDb?**
   - Inyección de dependencias automática: declaras (AppDb db) en la firma y .NET la entrega  _(DI integrada en Minimal APIs: efímero por petición, manejo del ciclo por ti.)_

8. **¿Qué hace FindAsync(id)?**
   - Busca por clave primaria devolviendo el objeto o null si no existe  _(La operación básica de lectura-por-id en EF Core — el orElse NotFound a continuación es el patrón.)_

## 🧗 Profundización (prepáralas explicando en voz alta)
- ¿Qué problema real resuelve C# y .NET y cuándo NO lo usarías?
- Explica el concepto más fuerte del curso sin usar jerga.
- Contrasta C# y .NET con una alternativa: pros/contras.
- Cuenta un error típico de novato en este tema y cómo lo evitas.

## ⭐ Método para contestarlas
1. **Responde en 60 segundos** cada una de las fundamentales, de memoria. Las que tartamudean → repásalas (flashcards/).
2. Graba tu voz en 2 y escúchate: claridad y precisión importan tanto como el contenido técnico.
3. Una respuesta buena = definición (1 línea) + ejemplo (1) + por qué importa (1).
