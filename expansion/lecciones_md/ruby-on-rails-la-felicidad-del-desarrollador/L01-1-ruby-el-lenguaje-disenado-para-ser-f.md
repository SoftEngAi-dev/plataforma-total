# 1. Ruby: el lenguaje diseñado para ser feliz

> 📚 Curso: **Ruby on Rails — La Felicidad del Desarrollador** · Lección 1 de 5
> 🗓 Exportado: 18/09/2026 desde Plataforma Total
> 🍅 Sugerencia: 1-2 pomodoros para leer + practicar

---

## 📖 Contenido

```ruby
RUBY: ELEGANCIA LEGIBLE EN TODO
━━━━━━━━━━━━━━━━━━━━━━━━━━━
Filosofía: la productividad del programador primero. Lee como inglés razonable.

  nombre = "Ada"                    # sin punto y coma, sin declarar tipo
  puts "Hola, #{nombre}"            # interpolación con #{}
  5.times { puts "¡ruby!" }          # bloques en TODO: ¿no es hermoso?

  # todo es objeto:
  "hola".upcase
  [1, 2, 3].map { |n| n * 10 }       # → [10, 20, 30]
  {nombre: "ada", edad: 36}.each { |k, v| puts k }

  def area(base, altura)             # return implícito: lo último se devuelve
    base * altura
  end

SIMBOLOS: son strings livianos para identificadores: :nombre (los verás por todos lados en Rails).
CONDICIONALES: if/elsif/else/end · unless es "if not" pythónico: puts "ok" unless errores.any?

JUGAR: ruby -v · irb (REPL interactivo: experimenta ahí) · ruby hola.rb
```

---

## 📝 Quiz de la lección

### 1. ¿Cómo interpola cadenas Ruby?
- A) ${}
- B) "#{variable}" dentro de comillas dobles
- C) f''
- D) sprintf
### 2. ¿Qué devuelve un método Ruby sin return?
- A) nil siempre
- B) La última expresión evaluada (return implícito)
- C) Error
- D) 0

---

## 🔑 Respuestas y explicaciones

**1.** ✅ "#{variable}" dentro de comillas dobles — #{} solo en comillas dobles — distinción que bugs de novato llenan.
**2.** ✅ La última expresión evaluada (return implícito) — "Lo último se devuelve" — por eso casi no verás return en Ruby idiomático.

---
✅ Al terminar, marca la lección como completada en la app (📚 Aprender → ✅ Completada)
