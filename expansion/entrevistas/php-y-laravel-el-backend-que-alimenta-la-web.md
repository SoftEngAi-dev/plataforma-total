# 🎤 Banco de entrevista — PHP y Laravel — El Backend Que Alimenta la Web

> 12 preguntas esenciales + guía de respuestas las que ya sabes del curso

## 🔥 Fundamentales (del contenido del curso)

1. **¿Cómo se declara una variable en PHP?**
   - $x = valor (el $ es obligatorio en cada variable)  _(El $ marca variables — parece raro y luego te acostumbras.)_

2. **¿Qué es un array asociativo en PHP?**
   - El equivalente a dict/hash: clave=>valor ['nombre'=>'Ada']  _(El tipo multiuso de PHP: lista y diccionario en uno.)_

3. **¿Qué hace htmlentities($texto) antes de un echo?**
   - Escapa <script> etc. evitando XSS: HTML inyectado queda como texto inofensivo  _(La regla de vida PHP: toda salida con datos del usuario pasa por escaping.)_

4. **$_POST["email"] ?? "" significa...**
   - Si no viene email, usa '' (null coalescing ?? en vez de undefined/index notice)  _(?? evita avisos por índices faltantes — desde PHP 7 la forma elegante.)_

5. **¿Qué protegen los prepared statements?**
   - SQL injection: los datos van apartados del SQL y nunca se interpretan como código  _(prepare() separa instrucción de datos: ' OR 1=1 -- queda como simple texto.)_

6. **¿Qué PDO::FETCH_ASSOC devuelve?**
   - Cada fila como array asociativo ['columna'=>valor]  _(Acceso por nombre de columna: código legible y resiliente.)_

7. **¿Qué es Eloquent?**
   - El ORM de Laravel: cada tabla es un Modelo y trabajas datos como objetos php (save, where, all)  _(Eloquent convierte SQL en interacción con objetos: Tarea::where('hecha', false)->get().)_

8. **¿Qué incluye la sintaxis {{ $x }} en Blade que la hace segura?**
   - Escapa HTML automáticamente (anti-XSS por defecto)  _({!! !!} imprime crudo e inseguro; {{ }} es lo normal y escapeado.)_

9. **¿Qué hace Route Model Binding en Laravel?**
   - Inyecta directo el modelo por ID (404 automático si no existe) sin hacer find manual  _(function show(Tarea $tarea) — el framework busca el id y te da el modelo o 404.)_

10. **¿Para qué sirve \$fillable en el modelo?**
   - Anti mass-assignment: lista blanca de campos rellenables vía create/update (evita inyectar campos no previstos)  _(Tarea::create($request->all()) protegido: solo pasa lo autorizado.)_

11. **¿Qué genera Route::resource()**
   - Las 7 rutas CRUD convencionales (index/create/store/show/edit/update/destroy) de golpe  _(Convención sobre configuración: Laravel asume la estructura estándar de recursos REST.)_

12. **¿Qué pone el @csrf dentro del <form> de Blade?**
   - Un token anti-CSRF oculto — todo POST sin token es rechazado por Laravel  _(CSRF protection integrada: solo formularios nacidos en tu app pueden postear.)_

## 🧗 Profundización (prepáralas explicando en voz alta)
- ¿Qué problema real resuelve PHP y Laravel y cuándo NO lo usarías?
- Explica el concepto más fuerte del curso sin usar jerga.
- Contrasta PHP y Laravel con una alternativa: pros/contras.
- Cuenta un error típico de novato en este tema y cómo lo evitas.

## ⭐ Método para contestarlas
1. **Responde en 60 segundos** cada una de las fundamentales, de memoria. Las que tartamudean → repásalas (flashcards/).
2. Graba tu voz en 2 y escúchate: claridad y precisión importan tanto como el contenido técnico.
3. Una respuesta buena = definición (1 línea) + ejemplo (1) + por qué importa (1).
