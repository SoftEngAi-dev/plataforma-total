# 3. ActiveRecord: tu base de datos con sabor Ruby

> 📚 Curso: **Ruby on Rails — La Felicidad del Desarrollador** · Lección 3 de 5
> 🗓 Exportado: 18/09/2026 desde Plataforma Total
> 🍅 Sugerencia: 1-2 pomodoros para leer + practicar

---

## 📖 Contenido

```ruby
ACTIVERECORD: LA GRAMÁTICA DE DATOS DE RAILS
━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Post.create(titulo: "Hola Rails", cuerpo: "...")   # INSERT
  Post.all                                            # SELECT *
  Post.find(1)                                        # por id o lanza error
  Post.find_by(publicado: true)                       # el primero
  Post.where("creado > ?", 1.week.ago)               # filtrado con params seguros
  Post.where(publicado: true).order(titulo: :asc).limit(10)
  p = Post.find(1); p.update(publicado: true)         # UPDATE
  p.destroy                                           # DELETE

VALIDACIONES EN EL MODELO (la madre de la integridad):
  class Post < ApplicationRecord
    validates :titulo, presence: true, length: { maximum: 120 }, uniqueness: true
    validates :cuerpo, presence: true
  end
  Post.new(cuerpo: "x").valid?   # false y te dice por qué: .errors.full_messages

RELACIONES (1línea declara ORM completa):
  class Autor; has_many :posts; end                   # un autor, muchos posts
  class Post;  belongs_to :autor; end                 # FK autor_id en posts
  autor.posts → todos; post.autor → el autor suyo.
```

---

## 📝 Quiz de la lección

### 1. ¿Qué hace validates :titulo, presence: true?
- A) Decora
- B) Rechaza guardar si falta el título; el objeto retorna valid? false con errores
- C) Borra
- D) Imprime
### 2. has_many :posts presupone...
- A) Nada
- B) Que la tabla posts tiene columna autor_id (convención Rails que la FK sigue el modelo singular+_id)
- C) Que tiene un índice
- D) Que son amigos

---

## 🔑 Respuestas y explicaciones

**1.** ✅ Rechaza guardar si falta el título; el objeto retorna valid? false con errores — Validaciones a nivel MODELO = defensa total (formulario, API, consola).
**2.** ✅ Que la tabla posts tiene columna autor_id (convención Rails que la FK sigue el modelo singular+_id) — Por convención no tienes que decírselo: la FK es visible: autor_id.

---
✅ Al terminar, marca la lección como completada en la app (📚 Aprender → ✅ Completada)
