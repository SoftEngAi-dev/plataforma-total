# 1. Flutter y Dart: el equipo del cross-platform

> 📚 Curso: **Flutter — Apps Hermosas con Una Sola Base** · Lección 1 de 5
> 🗓 Exportado: 18/09/2026 desde Plataforma Total
> 🍅 Sugerencia: 1-2 pomodoros para leer + practicar

---

## 📖 Contenido

```dart
FLUTTER: UN CÓDIGO, 6 PLATAFORMAS
━━━━━━━━━━━━━━━━━━━━━━━━━━━
Flutter de Google: Android, iOS, web, desktop — toda la UI se pinta a mano (Skia/Impeller) = pixel-perfect idéntico en todas partes. El lenguaje es Dart (imagina JavaScript + Java en cómodo).

DART A RÁPIDA VELOCIDAD
  void main() {
      var nombre = "Ada";      // var infiere
      String pais = "UY";       // o explícito
      final edad = 36;          // final = asigna UNA vez
      const pi = 3.14;          // const = en compilación
      print("Hola $nombre, ${edad + 1}");     // $var o ${expresión}
      var nums = [1, 2, 3];
      nums.where((n) => n % 2 == 0).map((n) => n * 10).toList();
  }

NULL-SAFETY igual a Kotlin/Swift: String? puede ser null; String NO.
  String? apodo; print(apodo?.length ?? 0);

INSTALAR FLUTTER: flutter.dev (SDK + Android Studio/XCode) → flutter doctor (verifica setup)
  flutter create miapp && cd miapp && flutter run    ← corre en emulador/dispositivo¡
HOT RELOAD: guardas el archivo y la app SE RECARGA AL INSTANTE (¡magia dev real!
```

---

## 📝 Quiz de la lección

### 1. ¿Qué hace Flutter único entre cross-platform?
- A) Usa web
- B) Pinta cada píxel a mano (no usa widgets nativos): UI 100% idéntica y controlada en todas las plataformas
- C) Es gratis
- D) Usa Python
### 2. ¿Para qué sirve flutter doctor?
- A) Curar código
- B) Verificar tu entorno: qué falta/configurar para que Flutter funcione (emuladores, SDKs...)
- C) Bases de datos
- D) Lint

---

## 🔑 Respuestas y explicaciones

**1.** ✅ Pinta cada píxel a mano (no usa widgets nativos): UI 100% idéntica y controlada en todas las plataformas — Render propio = diseño exacto en Android/iOS/web sin sorpresas de cada SO.
**2.** ✅ Verificar tu entorno: qué falta/configurar para que Flutter funcione (emuladores, SDKs...) — El diagnóstico automático: si doctor dice OK, todo funciona.

---
✅ Al terminar, marca la lección como completada en la app (📚 Aprender → ✅ Completada)
