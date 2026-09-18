# ⚡ Cheatsheet — 3. Entity Framework Core: la BD como objetos C#

> C# y .NET — El Ecosistema Microsoft Moderno · Lección 3 · 18/09/2026

## 💡 Idea central
EF CORE: EL ORM DE .NET

## 🧠 Autoexamen (tápate la respuesta)
- **¿Qué es DbContext en EF Core?** → La sesión/unidad de trabajo con la BD: DbSets por tabla y SaveChanges como transacción _(DbContext coordina tracked changes y los persiste con SaveChanges: el corazón del ORM.)_
- **¿Qué hacen las 'migraciones' de EF Core?** → Generan/aplican el esquema SQL desde tus clases C# y mantienen su historial versionado _(El esquema de la BD vive en tu código: cambiar clase → migración → BD nueva consistente.)_

## 🔁 Repaso espaciado sugerido
Hoy → mañana → dentro de 3 días → dentro de una semana. 5 minutos bastan.
