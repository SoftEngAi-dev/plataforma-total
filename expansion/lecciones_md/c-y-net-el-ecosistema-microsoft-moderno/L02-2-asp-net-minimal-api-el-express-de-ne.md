# 2. ASP.NET Minimal API: el Express de .NET

> 📚 Curso: **C# y .NET — El Ecosistema Microsoft Moderno** · Lección 2 de 4
> 🗓 Exportado: 18/09/2026 desde Plataforma Total
> 🍅 Sugerencia: 1-2 pomodoros para leer + practicar

---

## 📖 Contenido

```csharp
API REST EN 15 LÍNEAS CON .NET
━━━━━━━━━━━━━━━━━━━━━━━━━━━
  dotnet new web -o Api && cd Api

  // Program.cs COMPLETO:
  var builder = WebApplication.CreateBuilder(args);
  var app = builder.Build();

  var tareas = new List<Tarea>();

  app.MapGet("/api/tareas", () => tareas);
  app.MapPost("/api/tareas", (Tarea t) => { tareas.Add(t); return Results.Created($"/tareas/{t.Id}", t); });
  app.MapGet("/api/tareas/{id}", (int id) =>
      tareas.FirstOrDefault(t => t.Id == id) is { } t ? Results.Ok(t) : Results.NotFound());

  app.Run();
  record Tarea(int Id, string Titulo, bool Hecha);

  dotnet run → API en localhost:5000 ¡Y SWAGGER AUTOEN/DOC gratis en /swagger si agregas AddSwaggerGen!

RECORDS (¡los modelos más cortos que existen!): tipos inmutables de datos de una línea.
Results.Ok/Created/NotFound/BadRequest = status HTTP semánticos.
JSON: serialización automática de sus records/POCOs.
```

---

## 📝 Quiz de la lección

### 1. ¿Qué es una Minimal API en .NET?
- A) Lento
- B) El estilo conciso de ASP.NET Core: rutas con lambdas en Program.cs sin controladores pesados
- C) Una BD
- D) algo mínimo sin poder
### 2. ¿Qué tipo es record Tarea(...)?
- A) Clase estándar
- B) Tipo de datos inmutable con constructor/equals/desconstruct generados — el DTO perfecto
- C) Un struct
- D) Un enum

---

## 🔑 Respuestas y explicaciones

**1.** ✅ El estilo conciso de ASP.NET Core: rutas con lambdas en Program.cs sin controladores pesados — Equivalente .NET a Express/Flask: ideal para APIs y microservicios.
**2.** ✅ Tipo de datos inmutable con constructor/equals/desconstruct generados — el DTO perfecto — Records = POJOs cómodas: modelos limpios en una línea, igualdad por VALOR.

---
✅ Al terminar, marca la lección como completada en la app (📚 Aprender → ✅ Completada)
