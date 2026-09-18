# 2. Formularios y superglobales: PHP recibe datos

> 📚 Curso: **PHP y Laravel — El Backend Que Alimenta la Web** · Lección 2 de 6
> 🗓 Exportado: 18/09/2026 desde Plataforma Total
> 🍅 Sugerencia: 1-2 pomodoros para leer + practicar

---

## 📖 Contenido

```php
$_GET, $_POST, $_FILES: EL PAN DE CADA DÍA
━━━━━━━━━━━━━━━━━━━━━━━━━━━
FORMULARIO QUE SE PROCESA SOLO
  <form method="POST" action="registro.php">
    <input name="email" type="email" required>
    <button>Enviar</button>
  </form>

  <?php // registro.php
  $email = $_POST["email"] ?? "";          // ?? = null coalescing (si no existe)
  $email = trim($email);
  if (empty($email)) { die("Email requerido"); }
  if (!filter_var($email, FILTER_VALIDATE_EMAIL)) { die("Email inválido"); }

SUPERGLOBALS: $_GET (URL: registro.php?busqueda=gato → $_GET["busqueda"])
  $_POST (form POST) · $_SESSION (entre páginas, tras session_start()) · $_COOKIE · $_SERVER

SEGURIDAD OBLIGATORIA
• NUNCA imprimas $_POST/$_GET crudo en HTML: htmlentities($valor) (previene XSS)
• NUNCA concatenes en SQL: prepared statements (PDO, siguiente lección)
• Valida TODO lo del usuario (filter_var es tu kit)

SESIONES: session_start(); $_SESSION["usuario_id"]=42; → recordar sesión entre páginas.
```

---

## 📝 Quiz de la lección

### 1. ¿Qué hace htmlentities($texto) antes de un echo?
- A) Nada útil
- B) Escapa <script> etc. evitando XSS: HTML inyectado queda como texto inofensivo
- C) Formatea bonito
- D) Valida email
### 2. $_POST["email"] ?? "" significa...
- A) Error
- B) Si no viene email, usa '' (null coalescing ?? en vez de undefined/index notice)
- C) Comparar
- D) Sumar

---

## 🔑 Respuestas y explicaciones

**1.** ✅ Escapa <script> etc. evitando XSS: HTML inyectado queda como texto inofensivo — La regla de vida PHP: toda salida con datos del usuario pasa por escaping.
**2.** ✅ Si no viene email, usa '' (null coalescing ?? en vez de undefined/index notice) — ?? evita avisos por índices faltantes — desde PHP 7 la forma elegante.

---
✅ Al terminar, marca la lección como completada en la app (📚 Aprender → ✅ Completada)
