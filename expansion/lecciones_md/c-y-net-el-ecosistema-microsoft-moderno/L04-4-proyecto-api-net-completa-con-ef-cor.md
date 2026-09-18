# 4. Proyecto: API .NET completa con EF Core

> 📚 Curso: **C# y .NET — El Ecosistema Microsoft Moderno** · Lección 4 de 4
> 🗓 Exportado: 18/09/2026 desde Plataforma Total
> 🍅 Sugerencia: 1-2 pomodoros para leer + practicar

---

## 📖 Contenido

```csharp
CONSTRUYE: API DE TAREAS .NET SERIA
━━━━━━━━━━━━━━━━━━━━━━━━━━━
1. dotnet new web -o Tareas.Api && cd Tareas.Api
2. dotnet add package Microsoft.EntityFrameworkCore.Sqlite
3. Crea Tarea.cs (clase normal) + AppDb.cs (DbContext con DbSet<Tarea>)
4. En Program.cs:
   builder.Services.AddDbContext<AppDb>();
   var app = builder.Build();
   using (var s = app.Services.CreateScope()) { s.ServiceProvider.GetRequiredService<AppDb>().Database.EnsureCreated(); }
   app.MapGet("/api/tareas", async (AppDb db) => await db.Tareas.ToListAsync());
   app.MapPost("/api/tareas", async (AppDb db, Tarea t) => { db.Tareas.Add(t); await db.SaveChangesAsync(); return Results.Created($"/{t.Id}", t); });
   app.MapPatch("/api/tareas/{id}/toggle", async (AppDb db, int id) => {
       var t = await db.Tareas.FindAsync(id); if (t is null) return Results.NotFound();
       t.Hecha = !t.Hecha; await db.SaveChangesAsync(); return Results.Ok(t);
   });
   app.MapDelete("/api/tareas/{id}", ...Results.NoContent);
   app.Run();
5. dotnet run y prueba con curl: GET/POST/toggle.

BONUS: AddDbContext + parámetro (AppDb db) = DI automática por endpoint = el Spring-fácil de .NET.
Next: MVC completo, Blazor (frontend C# puro!) o publicar con docker.
```

---

## 📝 Quiz de la lección

### 1. ¿Cómo recibe el endpoint la instancia AppDb?
- A) new global
- B) Inyección de dependencias automática: declaras (AppDb db) en la firma y .NET la entrega
- C) Static
- D) No la recibe
### 2. ¿Qué hace FindAsync(id)?
- A) SQL crudo
- B) Busca por clave primaria devolviendo el objeto o null si no existe
- C) Borra
- D) Actualiza

---

## 🔑 Respuestas y explicaciones

**1.** ✅ Inyección de dependencias automática: declaras (AppDb db) en la firma y .NET la entrega — DI integrada en Minimal APIs: efímero por petición, manejo del ciclo por ti.
**2.** ✅ Busca por clave primaria devolviendo el objeto o null si no existe — La operación básica de lectura-por-id en EF Core — el orElse NotFound a continuación es el patrón.

---
✅ Al terminar, marca la lección como completada en la app (📚 Aprender → ✅ Completada)
