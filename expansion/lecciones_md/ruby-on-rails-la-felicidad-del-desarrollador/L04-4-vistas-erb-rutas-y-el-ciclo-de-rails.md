# 4. Vistas ERB, rutas y el ciclo de Rails

> 📚 Curso: **Ruby on Rails — La Felicidad del Desarrollador** · Lección 4 de 5
> 🗓 Exportado: 18/09/2026 desde Plataforma Total
> 🍅 Sugerencia: 1-2 pomodoros para leer + practicar

---

## 📖 Contenido

```ruby
DE URL A PANTALLA (VISTAS + RUTAS)
━━━━━━━━━━━━━━━━━━━━━━━━━━━
RUTAS (config/routes.rb)
  resources :posts                      # las 7 REST GET/POST/PATCH/DELETE
  root "posts#index"                    # la home
  get "acerca", to: "pages#about"       # una estática

EL CONTROLADOR prepara @variables (con @ llegan a la vista):
  def index
    @posts = Post.order(created_at: :desc)     # los más nuevos primero
  end

LA VISTA (app/views/posts/index.html.erb))
  <h1>Mi blog</h1>
  <% @posts.each do |post| %>            ← <% %> ejecuta SIN imprimir
    <h2><%= link_to post.titulo, post %></h2>    ← <%= %> imprime ESCAPADO (anti-XSS)
    <p><%= truncate(post.cuerpo, length: 100) %></p>
  <% end %>

HELPERS que enamoran: link_to · truncate · time_ago_in_words · number_to_currency
FORM autogenerado:
  <%= form_with model: @post do |f| %>
    <%= f.text_field :titulo %> <%= f.text_area :cuerpo %> <%= f.submit %>
  <% end %>
  (form_with incluye el token CSRF gratis y detecta si es crear/update)
```

---

## 📝 Quiz de la lección

### 1. ¿Diferencia entre <% %> y <%= %> en ERB?
- A) Ninguna
- B) <% ejecuta sin imprimir (loops/ifs); <%= ejecuta E IMPRIME escapando HTML
- C) <%= es comentario
- D) Lo contrario
### 2. ¿Qué hace form_with model: @post?
- A) CSS
- B) Formulario automático ligado al modelo: crea o edita según el objeto, con token CSRF incluido
- C) Valida
- D) Nada en especial

---

## 🔑 Respuestas y explicaciones

**1.** ✅ <% ejecuta sin imprimir (loops/ifs); <%= ejecuta E IMPRIME escapando HTML — El clásico bug: poner <%= en un @each y ver la lista entera impresa.
**2.** ✅ Formulario automático ligado al modelo: crea o edita según el objeto, con token CSRF incluido — Los helpers sienten la convención: si @post es nuevo → POST /posts; si existe → PATCH.

---
✅ Al terminar, marca la lección como completada en la app (📚 Aprender → ✅ Completada)
