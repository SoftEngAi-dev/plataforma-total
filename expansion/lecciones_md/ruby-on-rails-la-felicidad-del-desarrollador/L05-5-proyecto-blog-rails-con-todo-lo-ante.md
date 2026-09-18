# 5. Proyecto: blog Rails con todo lo anterior

> 📚 Curso: **Ruby on Rails — La Felicidad del Desarrollador** · Lección 5 de 5
> 🗓 Exportado: 18/09/2026 desde Plataforma Total
> 🍅 Sugerencia: 1-2 pomodoros para leer + practicar

---

## 📖 Contenido

```ruby
CONSTRUYE: MINI-BLOG RAILS EN 45 MINUTOS
━━━━━━━━━━━━━━━━━━━━━━━━━━━
1. rails new miblog && cd miblog
2. rails generate scaffold Post titulo:string cuerpo:text publicado:boolean
3. rails db:migrate && rails server → visita localhost:3000/posts (YA funciona todo)
4. AHORA ENTIENDE (no solo copies): abre routes.rb, agrega root "posts#index". Abre el modelo, añade validates :titulo, presence: true. Recarga: sin título ya no guarda — ¿ves? validación en acción.
5. Agrega un Autor: rails g model Autor nombre:string ; rails g migration AddAutorToPosts autor:references ; rails db:migrate
6. Modelos: Autor.has_many :posts / Post.belongs_to :autor
   En la vista muestra <%= post.autor.nombre %>
7. rails console en otra terminal para experimentar: Autor.create(nombre: "Ada").posts
8. Bonus: scopes útiles — class Post; scope :publicados, -> { where(publicado: true) }; end → Post.publicados en el controller.

CHECKLIST 🎓: puedes explicar QUÉ hace cada método del controlador · dónde vive cada cosa · por qué las validaciones están en el modelo y no en la vista. Eso ES entender Rails.
```

---

## 📝 Quiz de la lección

### 1. ¿Para qué sirve un scope en el modelo Rails?
- A) CSS
- B) Guardar consultas frecuentes como métodos reutilizables: Post.publicados
- C) Índices BD
- D) Vistas
### 2. AddAutor a posts con autor:references en migración hace...
- A) Nada
- B) Crea la columna autor_id + índice + FK en la tabla posts (relación completa en SQL)
- C) Crea un modelo
- D) Borra posts

---

## 🔑 Respuestas y explicaciones

**1.** ✅ Guardar consultas frecuentes como métodos reutilizables: Post.publicados — Scope = query con nombre: lisible y combinables (Post.publicados.recientes).
**2.** ✅ Crea la columna autor_id + índice + FK en la tabla posts (relación completa en SQL) — Las migraciones versionan tu esquema en código: la BD se recrea con rails db:migrate.

---
✅ Al terminar, marca la lección como completada en la app (📚 Aprender → ✅ Completada)
