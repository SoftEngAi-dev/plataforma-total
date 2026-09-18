# 6. Proyecto: CRUD completo en Laravel

> 📚 Curso: **PHP y Laravel — El Backend Que Alimenta la Web** · Lección 6 de 6
> 🗓 Exportado: 18/09/2026 desde Plataforma Total
> 🍅 Sugerencia: 1-2 pomodoros para leer + practicar

---

## 📖 Contenido

```php
CONSTRUYE: MINI-BLOG LARAVEL EN ~1 HORA
━━━━━━━━━━━━━━━━━━━━━━━━━━━
1. composer create-project laravel/laravel miniblog && cd miniblog
2. Configura .env (usa SQLite: DB_CONNECTION=sqlite, crea database/database.sqlite)
3. php artisan make:model Post -mcr        (modelo + migración + controller resource)
4. En la migración: $table->string("titulo"); $table->text("cuerpo"); $table->boolean("publicado")->default(false);
   php artisan migrate
5. En routes/web.php: Route::resource("posts", PostController::class);
   (Esto genera index/create/show/edit/store/update/destroy de regalo)
6. En el modelo: protected $fillable = ["titulo", "cuerpo", "publicado"];
7. En el controller: validación en store() y update():
   $request->validate(["titulo"=>"required|max:120", "cuerpo"=>"required"]);
8. Las vistas Blade (resources/views/posts/): formulario + tabla de lista con @foreach + @csrf en el form
9. php artisan serve → http://localhost:8000/posts → ¡CRUD comppleto!

ENTENDIMIENTO CLAVE: si recorriste ruta→controller→migración→modelo→vista y EXPLICAS cada pieza, entendiste Laravel más que la mitad de los que lo usan por inercia.
```

---

## 📝 Quiz de la lección

### 1. ¿Qué genera Route::resource()
- A) Nada
- B) Las 7 rutas CRUD convencionales (index/create/store/show/edit/update/destroy) de golpe
- C) Vistas
- D) Un servidor
### 2. ¿Qué pone el @csrf dentro del <form> de Blade?
- A) CSS
- B) Un token anti-CSRF oculto — todo POST sin token es rechazado por Laravel
- C) JavaScript
- D) SQL

---

## 🔑 Respuestas y explicaciones

**1.** ✅ Las 7 rutas CRUD convencionales (index/create/store/show/edit/update/destroy) de golpe — Convención sobre configuración: Laravel asume la estructura estándar de recursos REST.
**2.** ✅ Un token anti-CSRF oculto — todo POST sin token es rechazado por Laravel — CSRF protection integrada: solo formularios nacidos en tu app pueden postear.

---
✅ Al terminar, marca la lección como completada en la app (📚 Aprender → ✅ Completada)
