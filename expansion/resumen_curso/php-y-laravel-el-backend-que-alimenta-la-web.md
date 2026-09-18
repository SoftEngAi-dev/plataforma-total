# 📕 Resumen maestro — PHP y Laravel — El Backend Que Alimenta la Web

> Todo el curso en una hoja: una idea núcleo por lección. Releer semanal.

## 1. 1. PHP: el gigante subestimado
PHP: 25 AÑOS ALIMENTANDO LA WEB REAL ━━━━━━━━━━━━━━━━━━━━━━━━━━━ ¿Sabías? ~wordPress (43% de la web), Facebook nació en PHP, Laravel es uno de los frameworks más amados del mundo. …

## 2. 2. Formularios y superglobales: PHP recibe datos
$_GET, $_POST, $_FILES: EL PAN DE CADA DÍA ━━━━━━━━━━━━━━━━━━━━━━━━━━━ FORMULARIO QUE SE PROCESA SOLO   <form method="POST" action="registro.php">     <input name="email" type="ema…

## 3. 3. PDO: bases de datos sin inyección
PDO: SQL SEGURO EN PHP ━━━━━━━━━━━━━━━━━━━━━━━━━━━   $pdo = new PDO("sqlite:".__DIR__."/datos.db");   $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);  CREAR Y ESCRIB…

## 4. 4. Laravel: el framework que enamora
LARAVEL: PHP PREMIUM ━━━━━━━━━━━━━━━━━━━━━━━━━━━ El framework más amado de PHP. Elegancia + convenciones. Instalación con Composer (el npm de PHP):   composer create-project larave…

## 5. 5. MVC en Laravel: flujo completo de una petición
DE URL A RESPUESTA: EL CAMINO LARAVEL ━━━━━━━━━━━━━━━━━━━━━━━━━━━   Route::get("/tareas/{id}", [TareaController::class, "show"]);    // app/Http/Controllers/TareaController.php   c…

## 6. 6. Proyecto: CRUD completo en Laravel
CONSTRUYE: MINI-BLOG LARAVEL EN ~1 HORA ━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1. composer create-project laravel/laravel miniblog && cd miniblog 2. Configura .env (usa SQLite: DB_CONNECTION=…

---
✅ 6 lecciones · 📝 12 preguntas de repaso en quizzes_html/ · tests/