# 4. Listas con fetch: conecta tu app al mundo

> 📚 Curso: **Flutter — Apps Hermosas con Una Sola Base** · Lección 4 de 5
> 🗓 Exportado: 18/09/2026 desde Plataforma Total
> 🍅 Sugerencia: 1-2 pomodoros para leer + practicar

---

## 📖 Contenido

```dart
LISTVIEW + HTTP = EL 80% DE LAS APPS REALES
━━━━━━━━━━━━━━━━━━━━━━━━━━━
  // pubspec.yaml: http: ^1.2.0 ; dart pub add http
  import 'package:http/http.dart' as http;
  import 'dart:convert';

  class ApiScreen extends StatefulWidget { const ApiScreen({super.key});
      @override State<ApiScreen> createState() => _ApiState(); }

  class _ApiState extends State<ApiScreen> {
      List<dynamic> items = [];
      bool cargando = true;
      String? error;

      @override void initState() { super.initState(); cargar(); }

      Future<void> cargar() async {
          try {
              final resp = await http.get(Uri.parse("https://jsonplaceholder.typicode.com/posts"));
              if (resp.statusCode == 200) {
                  setState(() { items = jsonDecode(resp.body); cargando = false; });
              } else { throw Exception("HTTP ${resp.statusCode}"); }
      Future<void> cargar() async {
          try {
              final resp = await http.get(Uri.parse("https://jsonplaceholder.typicode.com/posts"));
              if (resp.statusCode == 200) {
                  setState(() { items = jsonDecode(resp.body); cargando = false; });
              } else { throw Exception("HTTP ${resp.statusCode}"); }
          } catch (e) {
              setState(() { error = "$e"; cargando = false; });
          }
      }

      @override
      Widget build(BuildContext context) {
          if (cargando) return const Center(child: CircularProgressIndicator());
          if (error != null) return Center(child: Text("Error: $error"));
          return ListView.builder(
              itemCount: items.length,
              itemBuilder: (context, i) => ListTile(
                  title: Text("${items[i]['title']}"),
                  subtitle: Text("Post #${items[i]['id']}"),
              ),
          );
      }
  }

LOS 3 ESTADOS DEL UI (siempre los mismos): cargando (spinner) → error (mensaje) → datos (lista).
FutureBuilder/StreamBuilder hacen esto declarativo; empezar a mano te enseña el porqué.
```

---

## 📝 Quiz de la lección

### 1. ¿Qué paquete oficial se usa para HTTP en Flutter?
- A) axios
- B) http (pub.dev): http.get(Uri.parse(url)) devuelve Future<Response>
- C) requests
- D) fetch
### 2. ¿Qué renderiza ListView.builder con itemCount?
- A) Todo a la vez
- B) Las filas BAJO DEMANDA mientras scrolleas (ideal para listas largas)
- C) Una tabla
- D) Un formulario

---

## 🔑 Respuestas y explicaciones

**1.** ✅ http (pub.dev): http.get(Uri.parse(url)) devuelve Future<Response> — dart pub add http y Futures con async/await: el estándar de red en Dart.
**2.** ✅ Las filas BAJO DEMANDA mientras scrolleas (ideal para listas largas) — Lazy rendering nativo: miles de posts sin matar el rendimiento.

---
✅ Al terminar, marca la lección como completada en la app (📚 Aprender → ✅ Completada)
