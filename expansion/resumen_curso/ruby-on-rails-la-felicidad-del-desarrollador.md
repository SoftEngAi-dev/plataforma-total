# 📕 Resumen maestro — Ruby on Rails — La Felicidad del Desarrollador

> Todo el curso en una hoja: una idea núcleo por lección. Releer semanal.

## 1. 1. Ruby: el lenguaje diseñado para ser feliz
RUBY: ELEGANCIA LEGIBLE EN TODO ━━━━━━━━━━━━━━━━━━━━━━━━━━━ Filosofía: la productividad del programador primero. Lee como inglés razonable.    nombre = "Ada"                    # s…

## 2. 2. Rails: convención sobre configuración
RAILS EN 5 COMANDOS (LA MAGIA) ━━━━━━━━━━━━━━━━━━━━━━━━━━━   rails new miblog --database=sqlite3   cd miblog   rails generate scaffold Post titulo:string cuerpo:text publicado:bool…

## 3. 3. ActiveRecord: tu base de datos con sabor Ruby
ACTIVERECORD: LA GRAMÁTICA DE DATOS DE RAILS ━━━━━━━━━━━━━━━━━━━━━━━━━━━   Post.create(titulo: "Hola Rails", cuerpo: "...")   # INSERT   Post.all                                   …

## 4. 4. Vistas ERB, rutas y el ciclo de Rails
DE URL A PANTALLA (VISTAS + RUTAS) ━━━━━━━━━━━━━━━━━━━━━━━━━━━ RUTAS (config/routes.rb)   resources :posts                      # las 7 REST GET/POST/PATCH/DELETE   root "posts#ind…

## 5. 5. Proyecto: blog Rails con todo lo anterior
CONSTRUYE: MINI-BLOG RAILS EN 45 MINUTOS ━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1. rails new miblog && cd miblog 2. rails generate scaffold Post titulo:string cuerpo:text publicado:boolean 3.…

---
✅ 5 lecciones · 📝 10 preguntas de repaso en quizzes_html/ · tests/