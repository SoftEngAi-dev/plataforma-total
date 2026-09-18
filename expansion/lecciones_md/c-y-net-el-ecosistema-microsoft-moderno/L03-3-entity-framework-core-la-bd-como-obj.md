# 3. Entity Framework Core: la BD como objetos C#

> 📚 Curso: **C# y .NET — El Ecosistema Microsoft Moderno** · Lección 3 de 4
> 🗓 Exportado: 18/09/2026 desde Plataforma Total
> 🍅 Sugerencia: 1-2 pomodoros para leer + practicar

---

## 📖 Contenido

```csharp
EF CORE: EL ORM DE .NET
━━━━━━━━━━━━━━━━━━━━━━━━━━━
  dotnet add package Microsoft.EntityFrameworkCore.Sqlite

  // El modelo y la 'sesión' con la BD:
  class Tarea { public int Id { get; set; } public string Titulo { get; set; } = ""; public bool Hecha { get; set; } }
  class AppDb : DbContext {
      public DbSet<Tarea> Tareas => Set<Tarea>();
      protected override void OnConfiguring(DbContextOptionsBuilder o) => o.UseSqlite("Data Source=tareas.db");
  }

  // Usar:
  using var db = new AppDb();
  db.Database.EnsureCreated();                          // crea la BD del esquema C#
  db.Tareas.Add(new Tarea { Titulo = "Estudiar EF" });
  db.SaveChanges();
  var pendientes = db.Tareas.Where(t => !t.Hecha).ToList();

MIGRACIONES (código → esquema versionado como en Laravel/Rails):
  dotnet ef migrations add Inicial
  dotnet ef database update

LINQ → SQL automático: tu .Where(t => !t.Hecha) se CONVIERTE en la query SQL: objetos afuera, SQL adentro optimizado.
Lo interesante: con DependencyInjection en el Program.cs lo inyectas: builder.Services.AddDbContext<AppDb>();
```

---

## 📝 Quiz de la lección

### 1. ¿Qué es DbContext en EF Core?
- A) Un controller
- B) La sesión/unidad de trabajo con la BD: DbSets por tabla y SaveChanges como transacción
- C) Un navegador
- D) JSON
### 2. ¿Qué hacen las 'migraciones' de EF Core?
- A) Nada en especial
- B) Generan/aplican el esquema SQL desde tus clases C# y mantienen su historial versionado
- C) Solo JSON
- D) Test

---

## 🔑 Respuestas y explicaciones

**1.** ✅ La sesión/unidad de trabajo con la BD: DbSets por tabla y SaveChanges como transacción — DbContext coordina tracked changes y los persiste con SaveChanges: el corazón del ORM.
**2.** ✅ Generan/aplican el esquema SQL desde tus clases C# y mantienen su historial versionado — El esquema de la BD vive en tu código: cambiar clase → migración → BD nueva consistente.

---
✅ Al terminar, marca la lección como completada en la app (📚 Aprender → ✅ Completada)
