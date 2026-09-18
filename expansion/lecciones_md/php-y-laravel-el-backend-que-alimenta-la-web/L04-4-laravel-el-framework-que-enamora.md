# 4. Laravel: el framework que enamora

> 📚 Curso: **PHP y Laravel — El Backend Que Alimenta la Web** · Lección 4 de 6
> 🗓 Exportado: 18/09/2026 desde Plataforma Total
> 🍅 Sugerencia: 1-2 pomodoros para leer + practicar

---

## 📖 Contenido

```php
LARAVEL: PHP PREMIUM
━━━━━━━━━━━━━━━━━━━━━━━━━━━
El framework más amado de PHP. Elegancia + convenciones. Instalación con Composer (el npm de PHP):
  composer create-project laravel/laravel miapp
  cd miapp && php artisan serve          → en localhost:8000 tu app viva

LA ESTRUCTURA (rutas → controladores → modelos → vistas Blade)
  routes/web.php:
  Route::get("/hola", fn() => "¡Hola desde Laravel!");
  Route::get("/tareas", [TareaController::class, "index"]);

ELOQUENT ORM — datos que se sienten como objetos:
  $tareas = Tarea::all();                          // SELECT *
  $tarea = Tarea::where("hecha", false)->get();    // filtrado
  $t = new Tarea(["titulo" => "Estudiar"]); $t->save();
  Tarea::find($id)->update(["hecha" => true]);

  Migraciones (esquema versionado en código): php artisan make:migration crear_tabla_tareas

BLADE (vistas con superpoderes):
  @foreach ($tareas as $t) <li>{{ $t->titulo }}</li> @endforeach
  {{ $titulo }} imprime ESCAPADO autop (XSS defendida de fábrica)

artisan = tu varita: php artisan make:model Tarea -mcr (modelo+migración+controller de golpe)
```

---

## 📝 Quiz de la lección

### 1. ¿Qué es Eloquent?
- A) Un lenguaje
- B) El ORM de Laravel: cada tabla es un Modelo y trabajas datos como objetos php (save, where, all)
- C) Un motor de vistas
- D) Una BD
### 2. ¿Qué incluye la sintaxis {{ $x }} en Blade que la hace segura?
- A) Nada
- B) Escapa HTML automáticamente (anti-XSS por defecto)
- C) Español
- D) SQL

---

## 🔑 Respuestas y explicaciones

**1.** ✅ El ORM de Laravel: cada tabla es un Modelo y trabajas datos como objetos php (save, where, all) — Eloquent convierte SQL en interacción con objetos: Tarea::where('hecha', false)->get().
**2.** ✅ Escapa HTML automáticamente (anti-XSS por defecto) — {!! !!} imprime crudo e inseguro; {{ }} es lo normal y escapeado.

---
✅ Al terminar, marca la lección como completada en la app (📚 Aprender → ✅ Completada)
