# 1. PHP: el gigante subestimado

> 📚 Curso: **PHP y Laravel — El Backend Que Alimenta la Web** · Lección 1 de 6
> 🗓 Exportado: 18/09/2026 desde Plataforma Total
> 🍅 Sugerencia: 1-2 pomodoros para leer + practicar

---

## 📖 Contenido

```php
PHP: 25 AÑOS ALIMENTANDO LA WEB REAL
━━━━━━━━━━━━━━━━━━━━━━━━━━━
¿Sabías? ~wordPress (43% de la web), Facebook nació en PHP, Laravel es uno de los frameworks más amados del mundo. PHP moderno (8.x) es rápido y elegante.

CORRER SIN INSTALAR NADA PESADO
  php -S localhost:8000 hola.php     ← servidor de desarrollo incorporado

SINTAXIS ESENCIAL (mezclable con HTML — su origen)
  <?php
  $nombre = "Ada";                     // $ variables SIEMPRE con $
  $edad = 36;
  echo "Hola, $nombre<br>";            // interpolación con comillas DOBLES
  $frutas = ["manzana", "pera"];      // array moderno ([])
  $frutas[] = "uva";                   // agregar
  foreach ($frutas as $fruta) { echo $fruta; }
  $alumno = ["nombre" => "Ada", "edad" => 36];  // array asociativo = dict/hash
  echo $alumno["nombre"];
  function saludar(string $nombre): string { return "Hola, $nombre"; }

PHP 8 MODERNO: tipos : string / int en params y returns (zig: eh, mejor que nada), nullsafe ?->, JIT. La broma "PHP es malo" quedó congelada en 2010.
```

---

## 📝 Quiz de la lección

### 1. ¿Cómo se declara una variable en PHP?
- A) let x
- B) $x = valor (el $ es obligatorio en cada variable)
- C) var x
- D) def x
### 2. ¿Qué es un array asociativo en PHP?
- A) Un número
- B) El equivalente a dict/hash: clave=>valor ['nombre'=>'Ada']
- C) Una clase
- D) SQL

---

## 🔑 Respuestas y explicaciones

**1.** ✅ $x = valor (el $ es obligatorio en cada variable) — El $ marca variables — parece raro y luego te acostumbras.
**2.** ✅ El equivalente a dict/hash: clave=>valor ['nombre'=>'Ada'] — El tipo multiuso de PHP: lista y diccionario en uno.

---
✅ Al terminar, marca la lección como completada en la app (📚 Aprender → ✅ Completada)
