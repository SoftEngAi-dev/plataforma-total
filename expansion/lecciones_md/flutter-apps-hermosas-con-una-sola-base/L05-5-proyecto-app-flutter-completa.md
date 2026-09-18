# 5. Proyecto: app Flutter completa

> 📚 Curso: **Flutter — Apps Hermosas con Una Sola Base** · Lección 5 de 5
> 🗓 Exportado: 18/09/2026 desde Plataforma Total
> 🍅 Sugerencia: 1-2 pomodoros para leer + practicar

---

## 📖 Contenido

```dart
CONSTRUYE: APP DE CLIMA O NOTAS EN FLUTTER
━━━━━━━━━━━━━━━━━━━━━━━━━━━
MVP GUIADO (elige y construye—2-3 pomodoros)
1. flutter create misnotas && cd misnotas
2. Pantalla principal: Scaffold + AppBar + ListView de notas guardadas en una List<Nota> en estado (modelo class Nota {String titulo; String texto;})
3. Pantalla agregar: Navigator.push al presionar + (rutas: Navigator.push(context, MaterialPageRoute(builder: (_) => AgregarScreen()))), TextField + botón Guardar → Navigator.pop(context, nota) devuelve el dato
4. Persistencia: shared_preferences con jsonEncode/Decode de la lista (flutter pub add shared_preferences) — guardas en setState tras cambios
5. Estados de UI: lista vacía con imagen/mensaje bonito (error/cargando no aplica aquí)
6. Pulido: dismissible para borrar con swipe: Dismissible(key: ..., onDismissed: ...)

COMPILAR PARA ENTREGAR
  flutter build apk --release   (Android)   flutter build ios (necesita Mac)
  flutter build web             (¡la misma app como web estática en build/web!)

♦F: esa última línea es LA promesa Flutter cumplida: una sola base → APK+web.
```

---

## 📝 Quiz de la lección

### 1. ¿Cómo se navega entre pantallas en Flutter nativo?
- A) location.href
- B) Navigator.push con MaterialPageRoute; volver con pop (pila de rutas)
- C) goto
- D) href
### 2. ¿Qué comando compila la app para web?
- A) flutter make web
- B) flutter build web → estáticos en build/web desplegables en Netlify/Pages
- C) flutter web
- D) no se puede

---

## 🔑 Respuestas y explicaciones

**1.** ✅ Navigator.push con MaterialPageRoute; volver con pop (pila de rutas) — El Navigator maneja una pila: push apila pantalla, pop regresa con o sin valor.
**2.** ✅ flutter build web → estáticos en build/web desplegables en Netlify/Pages — El mismo código Dart/Flutter corre como web estática: cross-platform real cumplida.

---
✅ Al terminar, marca la lección como completada en la app (📚 Aprender → ✅ Completada)
