# ⚠️ Errores comunes — 3. Entity Framework Core: la BD como objetos C#

> C# y .NET — El Ecosistema Microsoft Moderno · Lección 3 · Aprender de los errores (propios y ajenos)

- ❌ «Un controller» → Frente a «¿Qué es DbContext en EF Core?» lo fácil es confundirse. **Verdad**: La sesión/unidad de trabajo con la BD: DbSets por tabla y SaveChanges como transacción. DbContext coordina tracked changes y los persiste con SaveChanges: el corazón del ORM.
- ❌ «Un navegador» → Frente a «¿Qué es DbContext en EF Core?» lo fácil es confundirse. **Verdad**: La sesión/unidad de trabajo con la BD: DbSets por tabla y SaveChanges como transacción. DbContext coordina tracked changes y los persiste con SaveChanges: el corazón del ORM.
- ❌ «Nada en especial» → Frente a «¿Qué hacen las 'migraciones' de EF Core?» lo fácil es confundirse. **Verdad**: Generan/aplican el esquema SQL desde tus clases C# y mantienen su historial versionado. El esquema de la BD vive en tu código: cambiar clase → migración → BD nueva consistente.
- ❌ «Solo JSON» → Frente a «¿Qué hacen las 'migraciones' de EF Core?» lo fácil es confundirse. **Verdad**: Generan/aplican el esquema SQL desde tus clases C# y mantienen su historial versionado. El esquema de la BD vive en tu código: cambiar clase → migración → BD nueva consistente.

## 🩹 Antídoto universal
1. Lee el mensaje de error COMPLETO antes de googlear.
2. Pon el error exacto a la IA local y pide explicación, no solución.
3. Documenta el error en tu bitácora: error → causa → fix.
