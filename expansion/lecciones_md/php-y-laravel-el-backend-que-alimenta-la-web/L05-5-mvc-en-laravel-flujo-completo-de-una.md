# 5. MVC en Laravel: flujo completo de una petición

> 📚 Curso: **PHP y Laravel — El Backend Que Alimenta la Web** · Lección 5 de 6
> 🗓 Exportado: 18/09/2026 desde Plataforma Total
> 🍅 Sugerencia: 1-2 pomodoros para leer + practicar

---

## 📖 Contenido

```php
DE URL A RESPUESTA: EL CAMINO LARAVEL
━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Route::get("/tareas/{id}", [TareaController::class, "show"]);

  // app/Http/Controllers/TareaController.php
  class TareaController extends Controller {
      public function show(Tarea $tarea) {        // Model Binding: si no existe id → 404 auto
          return view("tareas.show", ["tarea" => $tarea]);
      }
      public function store(Request $request) {
          $datos = $request->validate([            // validación de una línea, robusta
              "titulo" => "required|string|max:140"
          ]);
          Tarea::create($datos);                   // (requiere fillable en el modelo)
          return redirect("/tareas")->with("ok", "¡Creada!");
      }
  }

  // resources/views/tareas/show.blade.php
  <h1>{{ $tarea->titulo }}</h1>

PROTECCIÓN MASS ASSIGNMENT: en el modelo declara qué campos se pueden llenar masivamente:
  protected $fillable = ["titulo"];      // evita que un POST malicioso te pase "es_admin"

VALIDATION EN ESPAÑOL MENTAL: required|email|min:8|max:255|unique:tareas,titulo|numeric...

EL FLUJO VISUAL: petición → Route → (optional middleware auth) → Controller (valida) → Model (datos) → View (presenta) → respuesta. Una separación clara = mantenimiento feliz.
```

---

## 📝 Quiz de la lección

### 1. ¿Qué hace Route Model Binding en Laravel?
- A) Nada especial
- B) Inyecta directo el modelo por ID (404 automático si no existe) sin hacer find manual
- C) Valida forms
- D) Sirve estáticos
### 2. ¿Para qué sirve \$fillable en el modelo?
- A) Indexar
- B) Anti mass-assignment: lista blanca de campos rellenables vía create/update (evita inyectar campos no previstos)
- C) Migraciones
- D) Nada

---

## 🔑 Respuestas y explicaciones

**1.** ✅ Inyecta directo el modelo por ID (404 automático si no existe) sin hacer find manual — function show(Tarea $tarea) — el framework busca el id y te da el modelo o 404.
**2.** ✅ Anti mass-assignment: lista blanca de campos rellenables vía create/update (evita inyectar campos no previstos) — Tarea::create($request->all()) protegido: solo pasa lo autorizado.

---
✅ Al terminar, marca la lección como completada en la app (📚 Aprender → ✅ Completada)
