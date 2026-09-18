# ⚠️ Errores comunes — 4. Listas con fetch: conecta tu app al mundo

> Flutter — Apps Hermosas con Una Sola Base · Lección 4 · Aprender de los errores (propios y ajenos)

- ❌ «axios» → Frente a «¿Qué paquete oficial se usa para HTTP en Flutter?» lo fácil es confundirse. **Verdad**: http (pub.dev): http.get(Uri.parse(url)) devuelve Future<Response>. dart pub add http y Futures con async/await: el estándar de red en Dart.
- ❌ «requests» → Frente a «¿Qué paquete oficial se usa para HTTP en Flutter?» lo fácil es confundirse. **Verdad**: http (pub.dev): http.get(Uri.parse(url)) devuelve Future<Response>. dart pub add http y Futures con async/await: el estándar de red en Dart.
- ❌ «Todo a la vez» → Frente a «¿Qué renderiza ListView.builder con itemCount?» lo fácil es confundirse. **Verdad**: Las filas BAJO DEMANDA mientras scrolleas (ideal para listas largas). Lazy rendering nativo: miles de posts sin matar el rendimiento.
- ❌ «Una tabla» → Frente a «¿Qué renderiza ListView.builder con itemCount?» lo fácil es confundirse. **Verdad**: Las filas BAJO DEMANDA mientras scrolleas (ideal para listas largas). Lazy rendering nativo: miles de posts sin matar el rendimiento.

## 🩹 Antídoto universal
1. Lee el mensaje de error COMPLETO antes de googlear.
2. Pon el error exacto a la IA local y pide explicación, no solución.
3. Documenta el error en tu bitácora: error → causa → fix.
