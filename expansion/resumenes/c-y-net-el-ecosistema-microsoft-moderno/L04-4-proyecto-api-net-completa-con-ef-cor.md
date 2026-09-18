# ⚡ Cheatsheet — 4. Proyecto: API .NET completa con EF Core

> C# y .NET — El Ecosistema Microsoft Moderno · Lección 4 · 18/09/2026

## 💡 Idea central
CONSTRUYE: API DE TAREAS .NET SERIA

## 🧠 Autoexamen (tápate la respuesta)
- **¿Cómo recibe el endpoint la instancia AppDb?** → Inyección de dependencias automática: declaras (AppDb db) en la firma y .NET la entrega _(DI integrada en Minimal APIs: efímero por petición, manejo del ciclo por ti.)_
- **¿Qué hace FindAsync(id)?** → Busca por clave primaria devolviendo el objeto o null si no existe _(La operación básica de lectura-por-id en EF Core — el orElse NotFound a continuación es el patrón.)_

## 🔁 Repaso espaciado sugerido
Hoy → mañana → dentro de 3 días → dentro de una semana. 5 minutos bastan.
