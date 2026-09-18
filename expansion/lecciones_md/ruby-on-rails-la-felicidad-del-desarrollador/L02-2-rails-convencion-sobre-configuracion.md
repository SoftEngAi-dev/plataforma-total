# 2. Rails: convención sobre configuración

> 📚 Curso: **Ruby on Rails — La Felicidad del Desarrollador** · Lección 2 de 5
> 🗓 Exportado: 18/09/2026 desde Plataforma Total
> 🍅 Sugerencia: 1-2 pomodoros para leer + practicar

---

## 📖 Contenido

```ruby
RAILS EN 5 COMANDOS (LA MAGIA)
━━━━━━━━━━━━━━━━━━━━━━━━━━━
  rails new miblog --database=sqlite3
  cd miblog
  rails generate scaffold Post titulo:string cuerpo:text publicado:boolean
  rails db:migrate
  rails server                       ← localhost:3000/posts YA funciona CRUD completo

Scaffold generó: modelo + migración + controlador + rutas + vistas HTML para todo el CRUD. Minutos.

CONVENTION OVER CONFIGURATION — la idea nuclear
Rails decide por ti el 90%: tabla posts = modelo Post; controlador PostsController; /posts → index...
Tú solo defines lo ORIGINAL de tu app. Menos decisiones, más producto.

RAILS CONSOLE: rails console → Post.create(titulo: "Hola") → Post.count → juegas con la BD real.
ActiveRecord (ORM) = primo de Eloquent: Post.where(publicado: true).order(created_at: :desc)

FLUJO MVC: rutas (config/routes.rb) → controlador (app/controllers) → modelo (app/models) → vista ERB (app/views).
resources :posts en routes = las 7 rutas REST de regalo (como en Laravel).
```

---

## 📝 Quiz de la lección

### 1. ¿Qué es el 'scaffold' de Rails?
- A) Una gema
- B) Generador del CRUD completo (modelo, migración, controller, vistas, rutas) desde una consola
- C) Un servidor
- D) Testing
### 2. ¿Qué significa Convention over Configuration?
- A) Ignora convenciones
- B) El framework asume estándares sensatos (Post↔posts, id PK...) y tú solo configuras lo distinto
- C) No hay convenciones
- D) Toca YAML

---

## 🔑 Respuestas y explicaciones

**1.** ✅ Generador del CRUD completo (modelo, migración, controller, vistas, rutas) desde una consola — Ideal para aprender el MVC viendo todas las piezas en acción y de una vez.
**2.** ✅ El framework asume estándares sensatos (Post↔posts, id PK...) y tú solo configuras lo distinto — CoC = menos decisiones triviales = velocidad de desarrollo enorme.

---
✅ Al terminar, marca la lección como completada en la app (📚 Aprender → ✅ Completada)
