# -*- coding: utf-8 -*-
"""Contenido C — Móvil, frameworks, datos, IA y carrera. Parte 3/3 (20 cursos, 88 lecciones)."""

CURSOS_MOD = {
# ═══════════════════ 23. KOTLIN (3) ═══════════════════
"Kotlin — Android y Más Allá": [
 ("1. Kotlin: el alivio que pedía Java", """KOTLIN: JAVA MODERNIZADA
━━━━━━━━━━━━━━━━━━━━━━━━━━━
Lenguaje de JetBrains, oficial para Android desde 2017. Corre sobre la JVM, interopera 100% con Java y quita el dolor: null-safety, brevedad, data classes.

  fun main() {
      val nombre = "Ada"               // val = INMUTABLE (const)
      var edad: Int = 36               // var = mutable · tipo explícito (inferencia si asignas)
      println("Hola, $nombre, $edad")  // interpolación con $
      edad = 37                        // ✅ var permite; nombre = "X" daría ERROR (val)

      val frutas = listOf("🍎", "🍌", "🥝")      // lista inmutable
      val numeros = mutableListOf(1, 2, 3)        // mutable
      numeros.add(4)

      for (f in frutas) println(f)
      for (i in 1..5) println(i)                  // rangos: 1..5 incluye ambos

      val descripcion = when {                    // when = switch elegante/expresión
          edad >= 18 -> "mayor"
          else -> "menor"
      }
  }

NULL-SAFETY NUCLEAR: String no puede ser null; String? SÍ puede y el compilador te OBLIGA a manejarlo:
  var apodo: String? = null
  println(apodo?.length)        // ?. = llama solo si no es null (devuelve null si lo es)
  println(apodo?.length ?: 0)   // ?: Elvis: valor por defecto""",
  [("¿Qué diferencia val de var en Kotlin?", ["Son iguales", "val es inmutable (referencia fija); var es reasignable", "val es para números", "var es más rápido"], 1, "Kotlin te empuja a inmutabilidad por defecto: val primero, var solo si hace falta."),
   ("¿Qué hace ?: (operador Elvis)?", ["Nada", "Si lo de la izquierda es null, devuelve lo de la derecha", "Compara strings", "Bucle"], 1, "Elvis porque parece un peinado ?:  — null coalescing con nombre rockero.")]),
 ("2. Funciones y data classes: brevedad con tipos", """FUNCIONES Y CLASES SIN CEREMONIA
━━━━━━━━━━━━━━━━━━━━━━━━━━━
  fun suma(a: Int, b: Int = 2): Int = a + b      // single-expression + default
  fun saludar(nombre: String = "mundo") = "Hola, $nombre"   // sin tipo: infiere
  saludar(nombre = "Ada")                        // ARGUMENTOS NOMBRADOS (legibilidad)

NULL HANDLING EN FUNCIONES
  fun largo(s: String?): Int = s?.length ?: 0    // acepta null, devuelve Int seguro

DATA CLASS — el record de Kotlin (toString/equals/hashCode/copy gratis):
  data class Tarea(val titulo: String, var hecha: Boolean = false)
  val t = Tarea("Estudiar Kotlin")
  val copia = t.copy(hecha = true)               // copia con cambios (inmutabilidad fácil)
  println(t)   // Tarea(titulo=Estudiar Kotlin, hecha=false)  ← toString útil auto

CLASES NORMALES + herencia (open = permite heredar, por defecto selladas):
  open class Animal(val nombre: String) { open fun sonido() = "..." }
  class Perro(nombre: String) : Animal(nombre) { override fun sonido() = "¡Guau!" }

LAMBDAS estilo funcional: listOf(1,2,3,4).filter { it % 2 == 0 }.map { it * 10 }  // 'it' implícito""",
  [("¿Qué genera automáticamente una data class?", ["Solo getters", "equals(), hashCode(), toString(), copy() y componentN() — todo el boilerplate de datos", "SQL", "Nada"], 1, "Una línea reemplaza 50 de Java: define campos y listo."),
   ("En listOf(1,2,3).map { it * 2 }, ¿qué es 'it'?", ["Un error", "El parámetro implícito de la lambda cuando hay uno solo", "Un global", "Un índice"], 1, "Lambdas de un parámetro pueden usar 'it' sin declararlo — típico estilo Kotlin.")]),
 ("3. Android con Kotlin: tu primera app", """ANDROID: ACTIVITIES, VIEWS Y GRADLE
━━━━━━━━━━━━━━━━━━━━━━━━━━━
Flujo: Android Studio (oficial, gratis) → New Project → "Empty Activity" → corre en emulador o tu celu por USB (activa Opciones de Desarrollador).

ESTRUCTURA CLAVE
  app/src/main/java/.../MainActivity.kt   ← tu código
  app/src/main/res/layout/activity_main.xml ← la UI (XML declarativo)
  app/build.gradle.kts                     ← dependencias/build

MAIN ACTIVITY CLÁSICA
  class MainActivity : AppCompatActivity() {
      override fun onCreate(savedInstanceState: Bundle?) {
          super.onCreate(savedInstanceState)
          setContentView(R.layout.activity_main)
          val boton = findViewById<Button>(R.id.miBoton)
          val texto = findViewById<TextView>(R.id.miTexto)
          boton.setOnClickListener { texto.text = "¡Clickeado!" }
      }
  }

CICLO DE VIDA: onCreate → onStart → onResume (visible) → onPause → onStop → onDestroy.
Respétalo: guarda estado en onSaveInstanceState, libera recursos al pausar.

HOY EN DÍA Jetpack Compose es la UI moderna (declarativa, estilo React):
  setContent { Button(onClick = { count++ }) { Text("Clicks: $count") } }
Empieza con Compose si vas nuevo: es el presente/futuro de Android.""",
  [("¿Qué hace findViewById<Button>(R.id.miBoton)?", ["Crea un botón", "Conecta el código Kotlin con la vista definida en el XML por su id", "Borra la vista", "Abre la cámara"], 1, "El puente código↔layout clásico; con Jetpack Compose ya no se necesita."),
   ("¿Qué es Jetpack Compose?", ["Otro lenguaje", "UI declarativa de Android: describes la interfaz con funciones Kotlin y el estado la redibuja", "Un emulador", "Una BD"], 1, "Mismo paradigma que React/Flutter: UI = f(estado) también en Android nativo.")]),
 ("4. Corrutinas: asincronía sin dolor", """CORRUTINAS: LO MÁS FINO DE KOTLIN
━━━━━━━━━━━━━━━━━━━━━━━━━━━
Problema: red, disco y timers no deben congelar la UI (si la app se congela 5s Android muestra "no responde" y la cierra).

  import kotlinx.coroutines.*

  fun main() = runBlocking {                     // puente al mundo coroutine
      launch {                                    // nueva corrutina (liviana, miles ok)
          delay(1000)                             // espera SIN bloquear el hilo
          println("¡async!")
      }
      println("esto va primero")
  }

SUSPEND: marca funciones que pueden pausarse y reanudar:
  suspend fun descargar(): String {
      delay(2000)                                 // simula red
      return "datos"
  }
Y CÓMO LLAMARLAS: desde otra suspend o un scope:
  GlobalScope.launch { val datos = descargar(); println(datos) }

async/await (paralelo de verdad):
  val a = async { descargar("usuarios") }
  val b = async { descargar("posts") }
  println(a.await() + b.await())                  // ambas corrieron a la vez

EN ANDROID: lifecycleScope.launch { ... } — la corrutina muere sola con la pantalla (sin fugas).
DIFERENCIA CON THREADS: una corrutina pesa ~1 KB; un hilo ~1 MB. Miles de corrutinas vs cientos de hilos.""",
  [("¿Qué hace suspend en una función?", ["La hace más lenta", "Puede pausar su ejecución sin bloquear el hilo y reanudar luego", "La hace pública", "La hace final"], 1, "suspend + delay = esperar sin congelar: la base de toda app Android moderna."),
   ("¿Por qué lifecycleScope en Android?", ["Porque sí", "Las corrutinas de UI se cancelan solas al destruirse la pantalla: sin fugas de memoria ni crashes", "Es más rápido", "Para SQL"], 1, "Scope atado al ciclo de vida = gestión de concurrencia automática y segura.")]),
 ("5. Proyecto: app mínima con Compose", """CONSTRUYE: CONTADOR APP CON JETPACK COMPOSE
━━━━━━━━━━━━━━━━━━━━━━━━━━━
1. Android Studio → New Project → Empty Activity (Compose)
2. En MainActivity.kt, dentro de setContent { }:

  var cuenta by remember { mutableStateOf(0) }   // estado: redibuja solo al cambiar

  Column(
      modifier = Modifier.fillMaxSize().padding(24.dp),
      verticalArrangement = Arrangement.Center,
      horizontalAlignment = Alignment.CenterHorizontally
  ) {
      Text("Clicks: $cuenta", fontSize = 32.sp)
      Spacer(Modifier.height(16.dp))
      Button(onClick = { cuenta++ }) { Text("¡Tócame!") }
      Button(onClick = { cuenta = 0 }) { Text("Reiniciar") }
  }

3. Corre en emulador o tu celu físico (USB + modo depuración)
4. Evoluciona: lista de tareas con LazyColumn { items(tareas) { } } + TextField para agregar

RECORDAR: en Compose NO llamas setText/vistas: describes UI = f(estado). Cambias 'cuenta' y Compose redibuja lo tocado. Si sabes React, ya lo entendiste.

ENTREGA: captura de la app corriendo + código en GitHub. Con Compose + Kotlin tienes el stack oficial moderno de Android lista para crecer (Room para BD, Retrofit para red).""",
  [("¿Qué hace remember { mutableStateOf(0) }?", ["Nada", "Estado que Compose observa: al cambiarlo, las funciones que lo leen se redibujan solas", "Guarda en disco", "Es un hilo"], 1, "El equivalente a useState de React pero nativo Android: UI reactiva real."),
   ("¿Qué difiere Compose de los layouts XML clásicos?", ["Nada crucial", "UI como código Kotlin declarativo (funciones + estado) en vez de XML + findViewById imperativo", "Es XML igual", "Es más lento"], 1, "Menos glue code, mismo paradigma que React/Flutter: el futuro oficial de Android.")]),
],
# ═══════════════════ 24. SWIFT (5) ═══════════════════
"Swift — El Camino de Apple": [
 ("1. Swift: elegancia tipada de Apple", """SWIFT: MODERNO, SEGURO Y VELOZ
━━━━━━━━━━━━━━━━━━━━━━━━━━━
Lenguaje de Apple desde 2014 (reemplazando Objective-C). Abierto, compilado, leéble como Python pero con tipos estrictos y safety.

  let nombre = "Ada"               // let = constante (inmutable)
  var edad = 36                    // var = variable
  print("Hola, \\(nombre)!")        // interpolación: \\(expr)
  edad += 1

  let frutas = ["🍎", "🍌"]           // Array literal, tipo inferido [String]
  var precios: [String: Int] = ["café": 120]   // Dictionary
  precios["té"] = 80
  for (fruta) in frutas { print(fruta) }
  for (producto, precio) in precios { print("\(producto): $\(precio)") }

  func area(base: Int, altura: Int) -> Int {   // -> Tipo de retorno
      base * altura                            // return implícito si es 1 expresión
  }
  print(area(base: 5, altura: 3))               // argument labels: lee claro

NUMEROS: Int, Double (decimales), Float. Bool. String.
EJECUTAR: en Xcode (Playground es mágico para aprender) o `swift hola.swift` en terminal.""",
  [("¿Qué distingue let de var en Swift?", ["Nada", "let = constante inmutable; var = reasignable — igual que val/var de Kotlin", "let es para números", "var es privado"], 1, "Swift te empuja a let por defecto: mutación solo cuando la justificas."),
   ("¿Cómo interpola strings Swift?", ["${x}", "\\(x) dentro del string", "f\"\"", "%s"], 1, "\"Hola \\(nombre)\" — la interpolación nativa de Swift.")]),
 ("2. Optionals: adiós al error del billón de dólares", """OPTIONALS: NULL-SAFETY EN EL ADN
━━━━━━━━━━━━━━━━━━━━━━━━━━━
En Swift un valor SÍ puede faltar, pero el tipo te obliga a encararlo:
  var apodo: String? = nil            // String? = "String opcional": puede ser nil
  var nombre: String = "Ada"          // String plano: NUNCA puede ser nil (¡el tipo lo garantiza!)

DESEMPAQUETAR (las 4 formas de la vida real)
1. IF LET (la más segura y común):
   if let a = apodo { print("Se llama \\(a)") } else { print("sin apodo") }
2. GUARD LET (salida temprana — el favorito en funciones):
   guard let a = apodo else { return }   // si nil, te vas ya; abajo 'a' es String real
   print(a.count)
3. NIL COALESCING ?? :
   let mostrar = apodo ?? "sin apodo"
4. OPTIONAL CHAINING ?. :
   let largo = apodo?.count            // solo si existe; largo queda Int?

⚠ EL PELIGRO: ! (force unwrap: apodo!) — crash si es nil. Úsalo solo cuando estés 100% seguro.
Esta rigurosidad es POR QUÉ las apps Swift crashean menos de pánico nil.""",
  [("¿Qué hace guard let x = y else { return }?", ["Repite", "Si y es nil, sale de la función ya; si no, x queda disponible desempaquetada para el resto", "Un bucle", "Un error"], 1, "Guard clause: los casos raros se despachan arriba y el código queda plano y claro."),
   ("¿Por qué se considera peligroso el force unwrap (!) ?", ["Es lento", "Si el valor es nil, la app CRASHEA en runtime: evitas el mecanismo que te protege", "No compila", "Es obsoleto"], 1, "El '!' es jurarle al compilador 'está ahí': cuando mientes, paga la app.")]),
 ("3. Structs, clases y protocolos", """EL TRIDENTE DEL MODELADO SWIFT
━━━━━━━━━━━━━━━━━━━━━━━━━━━
STRUCT (valor, copia — usarás ESTO por defecto)
  struct Punto { var x: Int; var y: Int }
  var p = Punto(x: 1, y: 2)
  p.x = 10                             // mutar ok (p es var)
  // init miembro a miembro es GRATIS

CLASS (referencia, herencia — para identidad/estado compartido)
  class Tarea {
      var titulo: String
      var hecha = false
      init(titulo: String) { self.titulo = titulo }   // init explícito
      func completar() { hecha = true }
  }

STRUCT vs CLASS (el SANO default Apple): struct por valor → copias seguras sin aliasing accidental.
class cuando necesites referencia compartida o herencia.

PROTOCOLOS (el interface de Swift — mucho más potente que herencia):
  protocol Describible { var descripcion: String { get } }
  extension Tarea: Describible {
      var descripcion: String { "Tarea: \\(titulo)\\(hecha ? " ✅" : "")" }
  }
  func imprimir(_ cosa: Describible) { print(cosa.descripcion) }

EXTENSIONS: agregas métodos a tipos EXISTENTES sin herencia:
  extension Int { var doble: Int { self * 2 } }   // 5.doble → 10""",
  [("¿Qué diferencia struct de class en Swift?", ["Son iguales", "struct = tipo VALOR (se copia); class = tipo REFERENCIA (se comparte) con herencia", "class es gratis", "struct es lenta"], 1, "Structs por defecto = menos bugs de aliasing; class solo para identidad compartida."),
   ("¿Qué permite una extension?", ["Herencia múltiple", "Agregar funcionalidad a tipos existentes sin subclases: incluso a Int, String nativos", "Nada especial", "Async"], 1, "Las extensiones hacen Swift extensible al infinito y súper idiomático.")]),
 ("4. SwiftUI: la UI declarativa de Apple", """SWIFTUI: UI = FUNCIÓN DEL ESTADO (¡otra vez!)
━━━━━━━━━━━━━━━━━━━━━━━━━━━
Desde 2019, la forma moderna: describís la UI y SwiftUI la redibuja al cambiar el estado.

  import SwiftUI
  struct ContadorView: View {
      @State private var cuenta = 0                 // ESTADO local (la fuente de verdad)

      var body: some View {                         // TODO view devuelve 'some View'
          VStack(spacing: 16) {                     // apila vertical (HStack horizontal)
              Text("Clicks: \\(cuenta)")
                  .font(.largeTitle)
              Button("¡Tócame!") { cuenta += 1 }    // acción con closure
              HStack {
                  Button("Reiniciar") { cuenta = 0 }
                  Button("-1") { cuenta -= 1 }
              }
          }
          .padding()
      }
  }

CONCEPTOS CLAVE
• View protocol: todo componente es una struct con 'var body'
• @State: estado local — cambia y SwiftUI redibuja automático (como useState)
• @Binding: estado que viene del padre; @StateObject/@Observable para modelos
• Modifiers encadenados: .font().padding().foregroundColor() — el estilo en cadena
• Preview gratis en Xcode mientras editás (hot reload real)

LISTAS:
  List(items) { item in Text(item.nombre) }  // como FlatList/LazyColumn/React map""",
  [("¿Qué hace @State en SwiftUI?", ["Nada especial", "Marca estado local que al cambiar provoca re-render automático del view que lo usa", "Guarda en disco", "Es async"], 1, "@State = useState de React: mutás y la UI se actualiza sola."),
   ("¿Qué es '.padding()' al final del VStack?", ["Un import", "Un modifier: transforma la vista y devuelve una nueva (estilo encadenado)", "Un error", "Un bucle"], 1, "Los modifiers se apilan de afuera hacia dentro: declarativos y componibles.")]),
 ("5. Proyecto: tu primera app iOS real", """CONSTRUYE: MINI-APP NOTAS EN SWIFTUI
━━━━━━━━━━━━━━━━━━━━━━━━━━━
1. Xcode → New Project → iOS App → SwiftUI → nombre "Notas"
2. Modelo:
  struct Nota: Identifiable {                      // Identifiable para listas
      let id = UUID(); var titulo: String; var texto: String
  }
3. Vista principal:
  struct NotasView: View {
      @State private var notas: [Nota] = []
      @State private var nueva = ""
      var body: some View {
          NavigationStack {
              VStack {
                  HStack {
                      TextField("Nueva nota...", text: $nueva)   // $ = binding doble vía
                      Button("+") {
                          guard !nueva.isEmpty else { return }
                          notas.append(Nota(titulo: nueva, texto: ""))
                          nueva = ""
                      }
                  }.padding()
                  List {
                      ForEach(notas) { n in Text(n.titulo) }
                      .onDelete { idx in notas.remove(atOffsets: idx) }  // ¡swipe to delete gratis!
                  }
              }.navigationTitle("Mis notas")
          }
      }
  }
4. Corre el simulador (Cmd+R) — swipe + borrar + agregar funcionan.

$ BINDING: text: $nueva = doble vía automática (escribes en el TextField y el estado cambia al instante).
Persistencia después: UserDefaults para cosas chicas, SwiftData/SQLite para serio.""",
  [("¿Qué significa text: $nueva en un TextField?", ["Error", "Binding bidireccional: el campo edita el estado y el estado actualiza el campo", "Es privado", "Es async"], 1, "$variable crea un Binding: ida y vuelta automática entre UI y estado."),
   ("¿Para qué sirve Identifiable en el modelo de una lista?", ["Decoración", "Cada item tiene id único para que SwiftUI rastree qué cambió en la lista (como key en React)", "Base de datos", "Nada"], 1, "List/ForEach necesitan identidad estable: id = la key del mundo Apple.")]),
],
# ═══════════════════ 25. FLUTTER (5) ═══════════════════
"Flutter — Apps Hermosas con Una Sola Base": [
 ("1. Flutter y Dart: el equipo del cross-platform", """FLUTTER: UN CÓDIGO, 6 PLATAFORMAS
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
HOT RELOAD: guardas el archivo y la app SE RECARGA AL INSTANTE (¡magia dev real!""",
  [("¿Qué hace Flutter único entre cross-platform?", ["Usa web", "Pinta cada píxel a mano (no usa widgets nativos): UI 100% idéntica y controlada en todas las plataformas", "Es gratis", "Usa Python"], 1, "Render propio = diseño exacto en Android/iOS/web sin sorpresas de cada SO."),
   ("¿Para qué sirve flutter doctor?", ["Curar código", "Verificar tu entorno: qué falta/configurar para que Flutter funcione (emuladores, SDKs...)", "Bases de datos", "Lint"], 1, "El diagnóstico automático: si doctor dice OK, todo funciona.")]),
 ("2. Widgets: TODO es un widget", """WIDGETS: LOS LEGO DE FLUTTER
━━━━━━━━━━━━━━━━━━━━━━━━━━━
En Flutterabsolutamente TODO es un widget: botones, textos, paddings, hasta la app entera.

  import 'package:flutter/material.dart';
  void main() => runApp(const MiApp());

  class MiApp extends StatelessWidget {          // Stateless: no cambia por sí mismo
      const MiApp({super.key});
      @override
      Widget build(BuildContext context) {        // build = qué dibujar
          return MaterialApp(
              home: Scaffold(                     // página base con appbar/body
                  appBar: AppBar(title: const Text("Mi app")),
                  body: const Center(child: Text("¡Hola, Flutter!")),
                  floatingActionButton: FloatingActionButton(
                      onPressed: () {}, child: const Icon(Icons.add)),
              ),
          );
      }
  }

LOS 8 QUE COMEN TODO
Text · ElevatedButton · Column/Row (apilar) · Padding · Center · Container (caja con estilo) · Icon · Image

COMPOSE-AND-NEST: no configs ocultas: anidas widgets como bloques. Column(children: [...widgets]).
stateless (inmutable) vs stateful (tiene estado y setState) — la próxima lección.""",
  [("¿Qué es un StatelessWidget?", ["Un error", "Un widget sin estado propio: se dibuja igual salvo que su PADRE le pase datos nuevos", "Un widget con tabs", "Un archivo"], 1, "La mayoría de la UI: describe, no cambia. Lo con estado es StatefulWidget."),
   ("¿Qué hace Column(children: [...])?", ["Tabla", "Apila widgets verticalmente (Row es horizontal)", "CSV", "Nada"], 1, "Layouts de una dimensión; con Expanded/flex dentro controlas el reparto.")]),
 ("3. Estado con StatefulWidget y setState", """ESTADO: QUE LA APP REACCIONE
━━━━━━━━━━━━━━━━━━━━━━━━━━━
  class Contador extends StatefulWidget {
      const Contador({super.key});
      @override State<Contador> createState() => _ContadorState();
  }
  class _ContadorState extends State<Contador> {
      int cuenta = 0;
      @override
      Widget build(BuildContext context) {
          return Column(mainAxisAlignment: MainAxisAlignment.center, children: [
              Text("Clicks: $cuenta", style: TextStyle(fontSize: 32)),
              ElevatedButton(
                  onPressed: () {
                      setState(() { cuenta++; });   // setState avisa: "redibuja"
                  },
                  child: const Text("+1")),
          ]);
      }
  }

REGLA SUPREMA: mutar el valor NUNCA redibuja; SIEMPRE dentro de setState(...).
  cuenta++;            // ❌ UI no se entera
  setState(() => cuenta++);   // ✅ redibuja el widget

LISTENERS + ASYNC: pantalla típica = StatefulWidget + initState (corre 1 vez) donde inicias fetch/timers + dispose (limpias).

HOT RELOAD con setState: guardas y ves el cambio sin perder el estado. Desarrollar en Flutter es casi mágico por esto.""",
  [("¿Por qué dentro de setState(() { cuenta++; })?", ["Por ritual", "setState marca el widget como sucio para que Flutter lo redibuje con el valor nuevo", "Evita null", "Es más rápido"], 1, "Mutación sin setState = estado cambiado pero UI vieja: el bug de todo novato."),
   ("¿Dónde inicias un fetch o timer en un StatefulWidget?", ["En build", "En initState (corre una vez al crearse); y liberas sus recursos en dispose", "En el constructor", "En main"], 1, "build se ejecuta muchas veces: inicialización va en initState, limpieza en dispose.")]),
 ("4. Listas con fetch: conecta tu app al mundo", """LISTVIEW + HTTP = EL 80% DE LAS APPS REALES
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
FutureBuilder/StreamBuilder hacen esto declarativo; empezar a mano te enseña el porqué.""",
  [("¿Qué paquete oficial se usa para HTTP en Flutter?", ["axios", "http (pub.dev): http.get(Uri.parse(url)) devuelve Future<Response>", "requests", "fetch"], 1, "dart pub add http y Futures con async/await: el estándar de red en Dart."),
   ("¿Qué renderiza ListView.builder con itemCount?", ["Todo a la vez", "Las filas BAJO DEMANDA mientras scrolleas (ideal para listas largas)", "Una tabla", "Un formulario"], 1, "Lazy rendering nativo: miles de posts sin matar el rendimiento.")]),
 ("5. Proyecto: app Flutter completa", """CONSTRUYE: APP DE CLIMA O NOTAS EN FLUTTER
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

♦F: esa última línea es LA promesa Flutter cumplida: una sola base → APK+web.""",
  [("¿Cómo se navega entre pantallas en Flutter nativo?", ["location.href", "Navigator.push con MaterialPageRoute; volver con pop (pila de rutas)", "goto", "href"], 1, "El Navigator maneja una pila: push apila pantalla, pop regresa con o sin valor."),
   ("¿Qué comando compila la app para web?", ["flutter make web", "flutter build web → estáticos en build/web desplegables en Netlify/Pages", "flutter web", "no se puede"], 1, "El mismo código Dart/Flutter corre como web estática: cross-platform real cumplida.")]),
],
# ═══════════════════ 26. REACT NATIVE (4) ═══════════════════
"React Native — Móvil con Tu Stack Web": [
 ("1. React Native: App = componentes que ya sabes", """REACT NATIVE: REACT QUE COMPILA A NATIVO
━━━━━━━━━━━━━━━━━━━━━━━━━━━
Tus componentes React renderizan a vistas NATIVAS de iOS/Android (no es un WebView: es UI real). Si sabes React, estás al 80%.

EQUIVALENCIAS (traducción directa de tu HTML)
  <div>        → <View>
  <p>/<span>   → <Text>     (¡todo texto va dentro de Text!)
  <img>        → <Image source={...}>
  <button>     → <Pressable onPress={fn}> o <Button title=... onPress={fn}>
  CSS inline   → style con StyleSheet.create (flexbox Y CSS-like, unidades sin "px")

  import { View, Text, Pressable, StyleSheet } from "react-native";
  export default function Hola() {
      return (
          <View style={estilos.pantalla}>
              <Text style={estilos.titulo}>¡Hola móvil!</Text>
              <Pressable style={estilos.boton} onPress={() => alert("¡clic!")}>
                  <Text>Soy un botón</Text>
              </Pressable>
          </View>
      );
  }
  const estilos = StyleSheet.create({
      pantalla: { flex: 1, justifyContent: "center", alignItems: "center" },
      titulo: { fontSize: 28, fontWeight: "bold" },
      boton: { backgroundColor: "#6f42c1", padding: 12, borderRadius: 8 },
  });

EXPO: la herramienta que hace el setup trivial:
  npx create-expo-app miapp && cd miapp && npx expo start
Escanneas un QR con tu celu (app Expo Go) y ves la app EN TU TELÉFONO en segundos. Magia.""",
  [("¿En qué difiere React Native de una WebView/web app empaquetada?", ["Son iguales", "RN compila tus componentes a widgets NATIVOS reales (rendimiento verdadero), no embebe una web", "Es HTML nativo", "Usa Flutter"], 1, "RN renderiza UIView/View nativas: por eso se siente app de verdad, no página."),
   ("¿Qué hace Expo en el flujo RN?", ["Otro lenguaje", "Toolchain que elimina el setup nativo: QR al teléfono, hot reload, build en la nube", "Una BD", "Un navegador"], 1, "Con Expo arrancas sin Xcode/Android Studio instalado: la puerta de entrada estándar.")]),
 ("2. listas, estilos y navegación móvil", """FLATLIST + FLEXBOX + SCREENS
━━━━━━━━━━━━━━━━━━━━━━━━━━━
LISTAR RÁPIDO (nunca map en ScrollView largo)
  import { FlatList } from "react-native";
  <FlatList
      data={notas}
      keyExtractor={(item) => item.id}
      renderItem={({ item }) => <Text style={s.item}>{item.titulo}</Text>}
  />
FlatList renderiza solo lo visible (virtualizada): miles de filas suaves.

FLEXBOX CON SABOR MÓVIL: todo es flex por defecto, mainAxisAlignment = justifyContent:
  { flex: 1 } en la pantalla raíz SIEMPRE (que ocupe todo)
  { flexDirection: "row" } para horizontal; gap: 8; padding: 16
Las unidades son números sin "px" (density-independent pixels automáticos).

NAVEGACIÓN (react-navigation, el estándar):
  npm install @react-navigation/native @react-navigation/native-stack
  const Stack = createNativeStackNavigator();
  <NavigationContainer>
    <Stack.Navigator>
      <Stack.Screen name="Inicio" component={Home} />
      <Stack.Screen name="Detalle" component={Detail} />
    </Stack.Navigator>
  </NavigationContainer>
  // navegar: navigation.navigate("Detalle", { id: item.id })""",
  [("¿Por qué FlatList y no un map dentro de ScrollView?", ["Es más corto", "FlatList virtualiza: solo dibuja filas visibles; ScrollView+map renderiza TODO (mata listas largas)", "No hay FlatList", "Es Apple"], 1, "El rendimiento de listas = virtualización. Regla: lista > ~20 items → FlatList."),
   ("¿Cómo pasas datos al navegar entre pantallas?", ["Por URL", "navigation.navigate('Detalle', { id }) y los lees con route.params en la pantalla destino", "No se puede", "Con fetch"], 1, "El segundo argumento navega parámetros: detalle recibe el id y trae/renderiza el dato.")]),
 ("3. TextInput, estado y persistencia (AsyncStorage)", """FORMS CONTROLADOS + GUARDAR EN EL DISPOSITIVO
━━━━━━━━━━━━━━━━━━━━━━━━━━━
INPUT CONTROLADO (el mismo patrón React)
  const [texto, setTexto] = useState("");
  <TextInput
      style={s.input}
      value={texto}
      onChangeText={setTexto}
      placeholder="Nueva nota..."
  />
  onChangeText da el string directo (no hay e.target.value en móvil).

PERSISTIR: AsyncStorage (el localStorage móvil)
  npm install @react-native-async-storage/async-storage
  import AsyncStorage from "@react-native-async-storage/async-storage";
  await AsyncStorage.setItem("notas", JSON.stringify(notas));
  const crudo = await AsyncStorage.getItem("notas");
  const notas = crudo ? JSON.parse(crudo) : [];

  Cargar al montar (useEffect + setState):  try/catch siempre.

DIFERENCIA CLAVE WEB: en móvil hay lifecycle de la app (va al background, la mata el SO...).
AppState de RN detecta "va al fondo" para guardar antes de que muera.

Para datos grandes: expo-sqlite (SQL nativa) o MMKV (clave-valor ultra rápida).""",
  [("¿Cómo se envía texto controlado en RN vs web?", ["e.target.value", "onChangeText recibe el string directamente: setTexto(nuevoTexto)", "No se puede", "FormData"], 1, "Mismo patrón controlado, pero el callback te da el texto límpio."),
   ("¿Qué es AsyncStorage?", ["Una BD SQL", "Almacenamiento clave-valor local (equivalente móvil de localStorage), strings+JSON", "Una nube", "Un caché HTTP"], 1, "Guarda strings; con JSON.stringify/parse persistes objetos entre sesiones de app.")]),
 ("4. Proyecto: app móvil completa con Expo", """CONSTRUYE: TU APP DE NOTAS MÓVIL EN TU CELULAR
━━━━━━━━━━━━━━━━━━━━━━━━━━━
1. npx create-expo-app notasapp && cd notasapp
2. npm install @react-native-async-storage/async-storage
3. App.js: estado notas (useState) + cargar de AsyncStorage en useEffect + guardar en cada cambio
4. UI: SafeAreaView → TextInput + botón Agregar → FlatList de notas con keyExtractor
5. Borrar: Pressable onLongPress sobre cada item (long-press = click derecho móvil) o botón 🗑 por fila
6. Estilos nítidos: flex:1 raíz · tarjetas con padding 16, borderRadius 12, marginBottom 8, elevation:2 (sombra android) / boxShadow iOS
7. npx expo start → abre Expo Go en tu celu (App Store/Play) → escanea el QR → MISMA WIFI → tu app real en tu mano
8. Bonus nivel calle: pull-to-refresh con RefreshControl en FlatList · modo oscuro con useColorScheme()

BUILD PARA DISTRIBUIR: eas build -p android (APK en la nube, gratis en tier) → lo compartes.
EAS Submit → stores, cuando seas grande. No necesitas Mac para Android ahora.

EL MOMENTO MÁGICO: la app corriendo EN TU PROPIA MANO, construida por ti. Ese es el enganche del desarrollo móvil.""",
  [("¿Qué necesitas para probar tu app RN en tu celular hoy sin Mac ni cables?", ["Un emulador", "Expo: instalar Expo Go, correr expo start, escanear el QR en la misma red WiFi", "Una Mac sí o sí", "Un AWS"], 1, "El QR de Expo convierte tu teléfono en dispositivo de desarrollo instantáneo."),
   ("¿Qué es onLongPress en un Pressable?", ["Error", "Click mantenido: el patrón móvil para acciones secundarias como borrar/editar", "Doble click", "Hover"], 1, "Móvil no tiene botón derecho: long-press = menú contextual.")]),
],
# ═══════════════════ 27. ANGULAR (4) ═══════════════════
"Angular — El Framework Empresarial Completo": [
 ("1. Angular + TypeScript: el opinioniado ganador empresa", """ANGULAR: FRAMEWORK COMPLETO, DECISIONES YA TOMADAS
━━━━━━━━━━━━━━━━━━━━━━━━━━━
Mientras React es "una librería + tú eliges", Angular trae TODO incluido: router, HTTP, formularios, DI, testing. TypeScript OBLIGATORIO. Por eso las empresas grandes lo adoran.

  npm install -g @angular/cli
  ng new miblog --standalone && cd miblog && ng serve   → localhost:4200

TU PRIMER COMPONENTE (component.ts + template inline o aparte)
  import { Component } from "@angular/core";
  @Component({
      selector: "app-saludo",
      standalone: true,
      template: `<h1>Hola, {{ nombre }}!</h1>
                 <button (click)="saludar()">Saludar</button>`,
  })
  export class SaludoComponent {
      nombre = "Ada";
      saludar() { alert("¡Hola desde Angular!"); }
  }

MEMORIA RÁPIDA
• {{ expr }} → interpolación (imprimir en template)
• (click)="fn()" → evento · [prop]="valor" → pasar dato a hijo · [(ngModel)] → doble vía
• *ngIf="cond" · *ngFor="let item of lista" (o el nuevo @if/@for moderno sintaxis v17+)

CLI TODO-PODEROSO: ng generate component usuarios → ng g c usuarios (crea los 3-4 archivos solitos).""",
  [("¿Qué distingue a Angular de React principalmente?", ["Color", "Angular es framework COMPLETO con router/http/form/DI incluidos y TypeScript obligatorio; React es librería de vista + ecosistema a elección", "Es más lento", "No hay diferencia"], 1, "Batteries-included vs composición libre: dos filosofías válidas según equipo y proyecto."),
   ("¿Qué hacen {{ }} y (click) en un template Angular?", ["JS puro", "{{ }} interpola valores al HTML; (evento)=\"fn()\" enlaza eventos a métodos del componente", "CSS", "Nada"], 1, "La sintaxis template de Angular: imprimir con {{}} y escuchar con () encadenado a la clase TS.")]),
 ("2. Servicios e inyección de dependencias: la joya oculta", """SERVICIOS + DI: DÓNDE VIVE LA LÓGICA
━━━━━━━━━━━━━━━━━━━━━━━━━━━
Regla Angular: los componentes pintan; los SERVICIOS trabajan (API, estado, lógica).

  // tareas.service.ts
  import { Injectable, inject } from "@angular/core";
  import { HttpClient } from "@angular/common/http";
  @Injectable({ providedIn: "root" })          // singleton en toda la app
  export class TareasService {
      private http = inject(HttpClient);        // DI moderna (sin constructor)
      private api = "https://jsonplaceholder.typicode.com/todos";
      todas() { return this.http.get<Tarea[]>(this.api); }   // devuelve Observable
  }

EN EL COMPONENTE
  export class ListaComponent {
      servicio = inject(TareasService);
      tareas: Tarea[] = [];
      ngOnInit() {
          this.servicio.todas().subscribe(datos => this.tareas = datos);
      }
  }

OBSERVABLES (RxJS): streams de datos que llegan en el tiempo — te SUSCRIBES para recibir.
Más potentes que promesas: se cancelan, componen (map/filter), llegan N veces (sockets, eventos).

DI = inyección de dependencias: pides lo que necesitas y Angular te lo entrega fabricado y singleton — tests con mocks triviales, arquitectura limpia de fábrica.""",
  [("¿Qué es @Injectable({ providedIn: 'root' })?", ["Decoración vacía", "Registra el servicio como singleton inyectable en toda la app (una sola instancia compartida)", "Una ruta", "Un test"], 1, "El servicio vive una vez para toda la app: estado/lógica compartida y centralizada."),
   ("¿En qué se diferencia un Observable de una Promesa?", ["Nada", "Emite N valores en el tiempo, es cancelable y componible con operadores; la promesa resuelve UNA vez", "Es solo Angular", "Es más lento siempre"], 1, "RxJS = promesas con esteroides: la columna vertebral de datos en Angular.")]),
 ("3. Signals: la nueva reactividad fina", """SIGNALS (Angular 16+): ESTADO SIMPLE, SIN ZONES
━━━━━━━━━━━━━━━━━━━━━━━━━━━
Angular moderno reacciona con signals: contenedores de valor que avisan quién los usa.

  import { signal, computed, effect } from "@angular/core";
  export class ContadorComponent {
      cuenta = signal(0);
      doble = computed(() => this.cuenta() * 2);       // derivado, se recalcula solo

      constructor() {
          effect(() => console.log("cambió:", this.cuenta()));   // efecto al cambiar
      }
      incrementar() { this.cuenta.update(v => v + 1); }  // o .set(10)
  }

EN EL TEMPLATE se leen como función:
  <p>Cuenta: {{ cuenta() }} (doble: {{ doble() }})</p>
  <button (click)="incrementar()">+1</button>

¿POR QUÉ IMPORTA? Antes Angular usaba Zone.js para detectar cambios en TODA la app (pesado).
Signals = detección quirúrgica: solo re-renderiza quien usa ese valor. Más rápido, más predecible, más simple mentalmente. Con v17+ además @if/@for reemplazan *ngIf/*ngFor:

  @if (tareas().length) { <ul>@for (t of tareas(); track t.id) { <li>{{ t.titulo }}</li> }</ul> }""",
  [("¿Qué problema resuelven los signals respecto a Zone.js?", ["Ninguno", "Detección de cambios quirúrgica: solo se actualiza lo que usa el signal, sin escanear toda la app", "Sintaxis corta", "HTTP"], 1, "Rendimiento por reacción fina: ganancia real en apps grandes y código más claro."),
   ("Un computed() es...", ["una función async", "Un valor DERIVADO de signals que se recalcula automáticamente cuando cambian sus dependencias", "Un servicio", "CSS"], 1, "Estado derivado sin lógica manual: defines la relación, Angular mantiene el valor fresco.")]),
 ("4. Proyecto: mini-app Angular con routing", """CONSTRUYE: APP DE TAREAS ANGULAR COMPLETA
━━━━━━━━━━━━━━━━━━━━━━━━━━━
1. ng new tareasapp --standalone --routing && cd tareasapp
2. MODELO + SERVICIO: interface Tarea { id: number; titulo: string; hecha: boolean }
   TareasService (root) con signal privado + métodos: todas(), agregar(t), alternar(id), borrar(id)
3. COMPONENTE LISTA (ng g c lista):
   <ul>@for (t of servicio.tareas(); track t.id) {
     <li (click)="servicio.alternar(t.id)" [class.hecha]="t.hecha">{{ t.titulo }}</li>
   }</ul>
4. COMPONENTE FORM: template-driven con [(ngModel)] o mejor ReactiveForms:
   formControl + (ngSubmit)="agregar()" → servicio.agregar(...) → reset campo
5. ROUTING (app.routes.ts):
   { path: "", component: ListaComponent }, { path: "detalle/:id", component: DetalleComponent }
   Lee el param: route = inject(ActivatedRoute); route.snapshot.params["id"]
6. ng serve → app completa. ng build → carpeta dist/ (estático desplegable en Netlify/Pages)

CHECKLIST ARQUITECTURA SAÑA
• Estado solo en el servicio (signal) · componentes tontos que lo leen · rutas por pantalla
• Test gratis: ng test corre Jasmine/Karma ya configurados""",
  [("¿Dónde debe vivir el estado compartido en Angular?", ["En cada componente", "En un servicio inyectable root: componentes lo inyectan y leen sus signals", "En el template", "En localStorage"], 1, "Single source of truth en servicio = la pantalla siempre consistente."),
   ("¿Cuál es el equivalente moderno a *ngFor en Angular 17+?", ["ng-repeat", "Bloque de control nativo: @for (item of lista(); track item.id) { ... }", "v-for", "map"], 1, "@for/@if en el template: sin imports extra, tracking explícito y más performance.")]),
],
# ═══════════════════ 28. SVELTE (3) ═══════════════════
"Svelte y SvelteKit — Menos Código, Mismo Poder": [
 ("1. Svelte: el compilador que no envía framework", """SVELTE: TU CÓDIGO SE CONVIERTE EN JS PURO VANILLA
━━━━━━━━━━━━━━━━━━━━━━━━━━━
Idea radical: React/Vue envían su runtime al navegador; Svelte COMPILA tus .svelte a JavaScript puro quirúrgico. Sin virtual DOM. Bundles minúsculos, velocidad por diseño.

  <!-- Contador.svelte — TODO vive en un archivo (script + plantilla + estilos) -->
  <script>
      let cuenta = 0;
      $: doble = cuenta * 2;                    // $: = reactivo puramente declarativo

      function incrementar() { cuenta += 1; }    // ¡asignar y listo! no setState
  </script>

  <h1>Clicks: {cuenta}</h1>
  <p>El doble es {doble}</p>
  <button on:click={incrementar}>+1</button>

  <style>
      h1 { color: purple; }                      /* estilos con SCOPE al componente */
      button { border-radius: 8px; }
  </style>

COMPARA LA MENTE:
• Estado: let x = 0 normal; modificar variable = re-render (sin setState, sin signals)
• $: etiqueta reactiva: corre de nuevo automáticamente cuando cambian sus dependencias
• on:evento · {expresión} en el markup · #if/#each/#await bloques nativos

SETUP: npm create vite@latest miblog -- --template svelte (o SvelteKit para app completa).""",
  [("¿Cuál es la gran diferencia técnica de Svelte?", ["Usa Python", "Es un compilador: no hay runtime de framework en el navegador, genera JS vanilla quirúrgico", "Es más lento", "Usa virtual DOM"], 1, "Menos código enviado + actualizaciones DOM precisas = apps veloces y bundles chicos."),
   ("¿Qué hace la etiqueta $: en el script?", ["JQuery", "Declaración reactiva: re-ejecuta la línea automáticamente cuando cambian las variables que usa", "Un import", "CSS"], 1, "$: doble = cuenta * 2 → doble siempre fresco sin lógica manual. Elegancia mínima.")]),
 ("2. Reactividad total: stores, bindings y formularios", """EL MODELO REACTIVO COMPLETO DE SVELTE
━━━━━━━━━━━━━━━━━━━━━━━━━━━
BINDINGS DOBLE VÍA (sin el rito de React)
  <input bind:value={nombre}>          <!-- escribes → variable cambia; y viceversa -->
  <input type="checkbox" bind:checked={acepta}>
  <select bind:value={color}>...</select>

  <script>
      let nombre = "";
      $: mayus = nombre.toUpperCase();  // derivado automático
  </script>
  <p>{nombre} → {mayus}</p>

STORES: estado compartido fuera del componente (equivalente a context/redux liviano)
  // stores.js
  import { writable } from "svelte/store";
  export const tema = writable("claro");
  // componente.svelte
  import { tema } from "./stores.js";
  $tema;                        // $prefijo = autosuscripción (¡magia!)
  tema.set("oscuro");  tema.update(t => t === "claro" ? "oscuro" : "claro");

BLOQUES NATIVOS (sintaxis de plantilla limpia)
  {#if cargando}<Spinner/>{:else if datos}<Lista {datos}/>{:else}<p>vacío</p>{/if}
  {#each tareas as t (t.id)}<li>{t.titulo}</li>{/each}
  {#await promesa then valor}<p>{valor}</p>{/await}""",
  [("¿Qué hace bind:value={nombre} en un input?", ["Nada", "Binding doble vía: escribir actualiza la variable y cambiar la variable actualiza el input", "Submit", "CSS"], 1, "El formulario controlado más corto que existe: una directiva y sincronía total."),
   ("¿Qué es $tema con $ delante de un store?", ["JQuery", "Autosuscripción de Svelte: lees el valor del store directo y se desuscribe solo al destruir", "Un bug", "Un import"], 1, "Los stores + $ = estado compartido sin boilerplate: context/redux incluido en el lenguaje.")]),
 ("3. SvelteKit y proyecto: app completa con rutas", """SVELTEKIT: LA APP REAL (ROUTING + SSR + FORMULARIOS)
━━━━━━━━━━━━━━━━━━━━━━━━━━━
  npm create svelte@latest miapp && cd miapp && npm install && npm run dev

ROUTING POR ARCHIVOS (como Next.js)
  src/routes/+page.svelte            → /
  src/routes/acerca/+page.svelte       → /acerca
  src/routes/tareas/[id]/+page.svelte  → /tareas/42  (parámetro dinámico)
  src/routes/tareas/[id]/+page.server.js → datos del servidor para esa ruta (¡SSR!)

LOAD FUNCTIONS: cargar datos ANTES de renderizar (con SEO feliz)
  // +page.server.js
  export async function load({ params }) {
      const post = await db.query("SELECT * FROM posts WHERE id = ?", params.id);
      if (!post) throw error(404);
      return { post };
  }
  // +page.svelte
  <script>export let data;</script>
  <h1>{data.post.titulo}</h1>

FORM ACTIONS: formularios que funcionan SIN JS (progresive enhancement)
  <form method="POST"><input name="titulo"><button>Crear</button></form>
  // +page.server.js
  export const actions = { default: async ({ request }) => {
      const datos = await request.formData();
      await crearTarea(datos.get("titulo"));    // corre en el servidor
  }};

PROYECTO: clona la app de notas: ruta / + form action para crear + load que liste desde SQLite + /nota/[id] para detalle. Deploy gratis con adapter de Vercel/Netlify/Node.""",
  [("¿Qué hace una función load en +page.server.js?", ["CSS", "Corre en el SERVIDOR antes de renderizar y pasa datos a la página (SSR + SEO + sin flicker)", "Es un test", "Sirve imágenes"], 1, "Datos en el server, HTML listo al llegar: la app rápida y el SEO contento."),
   ("¿Qué es progressive enhancement con form actions?", ["Ajax con JS", "El formulario funciona sin JavaScript (POST clásico del servidor, JS solo lo acelera cuando existe)", "No funciona sin JS", "Un alert"], 1, "Robustez por diseño: tu app no se rompe si falla/red no carga el bundle JS.")]),
],
# ═══════════════════ 29. R (4) ═══════════════════
"R y Estadística — El Idioma de los Datos": [
 ("1. R en 15 minutos: vectores, el corazón", """R: HECHO POR Y PARA ESTADÍSTICOS
━━━━━━━━━━━━━━━━━━━━━━━━━━━
R domina estadística/investigación/bioinformática. Todo son VECTORES (colecciones), las operaciones son vectorizadas.

  # hola.R — ejecuta: Rscript hola.R  (o RStudio: el IDE por excelencia)
  nombre <- "Ada"                    # <- es el operador de asignación (= también sirve)
  edades <- c(25, 30, 35, 40)        # c() = concatenate: el vector básico
  edades * 2                          # vectorizado: c(50, 60, 70, 80)
  edades + 10
  mean(edades)                        # 32.5  ← estadística de fábrica
  sum(edades); length(edades); max(edades)

  secuencias <- 1:10                  # 1..10
  seq(0, 100, by = 5)
  edades[1]                           # → 25 ¡LOS ÍNDICES EMPIEZAN EN 1!
  edades[2:4]                         # 30, 35, 40
  edades[edades > 28]                 # indexación lógica: c(30,35,40)

  edades2 <- c(27, 33)                # asignación c()
  mayores <- edades[edades >= 30]     # filtrar: el dedo es R: te acostumbras al <-

funciones: promedio <- function(x) { sum(x) / length(x) }""",
  [("¿Qué hace edades[edades > 30]?", ["Error", "Indexación lógica vectorizada: devuelve solo los elementos donde la condición es TRUE", "Borra", "Ordena"], 1, "Filtrar vectores con condiciones sin bucles: la elegancia R desde el día 1."),
   ("¿En qué empiezan los índices de R?", ["En 0", "En 1 — viejos lenguajes científicos (R/MATLAB/Fortran) cuentan como humanos", "En -1", "Depende"], 1, "Sorpresa clásica para quien viene de C/Python: edades[1] es el PRIMERO.")]),
 ("2. Data frames: la tabla de trabajo eterna", """DATA.FRAME: EL EXCEL DE R
━━━━━━━━━━━━━━━━━━━━━━━━━━━
  datos <- data.frame(
      nombre  = c("Ada", "Grace", "Marie"),
      edad    = c(36, 85, 60),
      lenguaje = c("COBOL", "COBOL", "Física")   # ejemplo libre
  )
  datos$nombre           → vector columna
  datos[1, ]             → primera FILA
  datos[, "edad"]        → columna por nombre
  datos$edad[2]          → 85
  nrow(datos); ncol(datos); names(datos)
  summary(datos)          → estadísticas por columna ¡incluido de fábrica!
  head(datos, 2)          → primeras 2 filas (tail = últimas)

AGREGAR/FILTRAR
  datos$pais <- c("UK", "US", "FR")              # columna nueva al vuelo
  adultos <- datos[datos$edad > 40, ]            # filtra filas (coma recuerda fuera)
  subset(datos, edad > 40)                       # alternativa legible

LEER CSV REAL (la base del análisis real):
  ventas <- read.csv("ventas.csv")
  str(ventas)            → tipos de cada columna (muyst útil)
  View(ventas)           → visor tipo hoja en RStudio

EXPORTAR: write.csv(datos, "salida.csv", row.names = FALSE)""",
  [("¿Qué hace summary(datos)? en R?", ["Imprime todo", "Resumen estadístico por columna (min/max/media/mediana/cuartiles): EDA gratis en una palabra", "Borra", "Ordena"], 1, "La primera vista a cualquier dataset: summary + str + head = inspección completa."),
   ("datos[datos$edad > 40, ] — ¿qué hace la coma final?", ["Error", "Selecciona filas donde edad>40 y TODAS las columnas (el espacio tras la coma = todas las columnas)", "Divide", "Nada"], 1, "df[filas, columnas]: la coma vacía significa 'todas las columnas'.")]),
 ("3. Estadística descriptiva y grupos: los números de verdad", """ESTADÍSTICA APLICADA EN 8 FUNCIONES
━━━━━━━━━━━━━━━━━━━━━━━━━━━
CENTRALIDAD Y DISPERSIÓN
  mean(x)      → media (sensible a outliers)
  median(x)    → mediana (robusta)
  sd(x)        → desviación estándar (qué tanto varía)
  var(x); range(x); quantile(x)
  IQR(x)       → rango intercuartílico (para boxplots/outliers)

  z <- (x - mean(x)) / sd(x)           → estandarizar (z-scores)
  cor(edad, ingresos)                   → correlación (-1 a 1)
  cor(x, y, method = "spearman")        → correlación por rangos (no lineal)

AGRUPAR Y RESUMIR (el group by de R)
  tapply(datos$edad, datos$pais, mean)      → media de edad por país
  aggregate(edad ~ pais, datos, mean)       → misma idea en data.frame
  # con dplyr (idyoma moderno): datos %>% group_by(pais) %>% summarise(media = mean(edad))

  table(datos$lenguaje)                 → conteo por categoría
  prop.table(table(x)) * 100            → porcentajes

PRUEBA T (comparativa básica):
  t.test(grupo_a, grupo_b) → te dice si las medias difieren significativamente (p-value)""",
  [("¿Qué mide sd(x)?", ["La media", "La desviación estándar: cuánto se dispersan los datos respecto a la media", "La correlación", "El máximo"], 1, "sd pequeña = datos agrupados; sd grande = mucha variación. Clave en cualquier resumen."),
   ("¿Qué indica cor(edad, ingresos) = 0.8?", ["Nada", "Correlación positiva FUERTE: a más edad, más ingresos (en esa muestra)", "Causalidad", "Un error"], 1, "Correlación NO es causalidad — pero descubrir 0.8 te dice dónde investigar.")]),
 ("4. Proyecto: tu primer análisis R real", """CONSTRUYE: ANÁLISIS DE UN CSV REAL EN R
━━━━━━━━━━━━━━━━━━━━━━━━━━━
MISIÓN (60-90 min): descarga el dataset de pinguins o tu CSV favorito y domina el ciclo EDA completo.

1. CARGA + INSPECCIÓN
   datos <- read.csv("datos.csv"); str(datos); summary(datos); head(datos)
   ¿cuántas filas/columnas? ¿qué tipo es cada columna?
2. LIMPIEZA MÍNIMA
   sum(is.na(datos))              → cuántos NAs hay en total
   limpio <- na.omit(datos)       → elimina filas con NA (o decide imputar)
   names(limpio) <- tolower(names(limpio))   → columnas en minúsculas
3. PREGUNTAS DE NEGOCIO (escríbelas antes de mirar)
   - ¿Media y mediana? ¿y el rango (varianza)?
   - ¿Mejor categoría por agregados: tapply o aggregate?
   - ¿Correlación entre las dos columnas numéricas principales?
4. VISUALIZACIÓN RÁPIDA (base R)
   hist(limpio$edad, col = "skyblue", main = "Distribución de edades")
   boxplot(edad ~ categoria, data = limpio)
   plot(limpio$x, limpio$y); abline(lm(y ~ x, data = limpio), col = "red")
5. CONCLUSIÓN escrita: 3 hallazgos con números de apoyo en un informe Rmd o un .txt

LO QUE APRENDISTE = 60% del trabajo de un analista real: inspección → limpieza → resumen → visual → historia.""",
  [("¿Qué hace na.omit(datos)?", ["Rellena NAs", "Elimina las filas que tengan algún NA (limpieza rápida)", "Crea NAs", "Nada"], 1, "Decisión simple de limpieza; en proyectos serios evalúa si imputar tiene más sentido."),
   ("¿Cuál es el ORDEN mental correcto al analizar datos?", ["Graficar, limpiar, decidir", "Inspeccionar → preguntar → limpiar → resumir → visualizar → escribir conclusiones", "Código primero", "Modelo primero"], 1, "El método importa: preguntas antes de números; conclusiones después de evidencias.")]),
],
# ═══════════════════ 30. PANDAS (6) ═══════════════════
"Pandas — Excel con Superpoderes en Python": [
 ("1. DataFrames: tablero mental de pandas", """PANDAS EN UNA PÁGINA
━━━━━━━━━━━━━━━━━━━━━━━━━━━
  import pandas as pd              (pip install pandas)

  # Serie (una columna con índice) y DataFrame (tabla completa)
  edades = pd.Series([25, 30, 35], name="edad")
  datos = pd.DataFrame({
      "nombre": ["Ada", "Grace", "Marie"],
      "edad": [36, 85, 60],
      "pais": ["UK", "US", "FR"],
  })

  datos.head()          → primeras 5 filas     datos.tail(2)
  datos.shape           → (3, 3)                datos.columns
  datos.dtypes          → tipos por columna
  datos.info()          → resumen de tipos/nulls/memoria
  datos.describe()      → estadística descriptiva de numéricas (count/mean/std/min/quartiles/max)

SELECCIÓN (las dos grandes)
  datos["edad"]               → columna como Serie
  datos[["nombre", "edad"]]   → sub-DataFrame
  datos.iloc[0]               → primera fila POR POSICIÓN
  datos.loc[0, "nombre"]      → fila/etiqueta + columna (loc = labels, iloc = posiciones)

FILTRO (el corazón del análisis)
  datos[datos["edad"] > 40]                           → 2 filas
  datos[(datos.edad > 30) & (datos.pais == "US")]     → &/| con paréntesis obligatorios
  datos[datos.pais.isin(["UK", "FR"])]                → útil""",
  [("¿Qué devuelve datos[datos['edad'] > 40]?", ["Error", "Filas del DataFrame donde la condición booleana es verdadera", "Las edades", "Nada"], 1, "Boolean indexing: la forma panda de decir 'WHERE edad > 40'."),
   ("¿Cuándo usar datos.loc vs datos.iloc?", ["Son iguales", "loc: por ETIQUETA/condición; iloc: por POSICIÓN de entero", "loc es de lectura", "iloc es más nuevo"], 1, "loc[[2,3], ['a']] por nombre; iloc[0:2, 0] por posición. Ambos según el índice.")]),
 ("2. CSV, limpieza y transformación de columnas", """EL FLUJO DE TRABAJO DIARIO DE PANDAS
━━━━━━━━━━━━━━━━━━━━━━━━━━━
  df = pd.read_csv("ventas.csv")          (también read_excel/read_json/read_sql)
  df.to_csv("salida.csv", index=False)    → guardar

LIMPIEZA (la realidad del 80% del trabajo)
  df.isna().sum()                 → cuántos faltan por columna (¡primero siempre!)
  limpio = df.dropna()             → eliminar filas con NA
  limpio = df.dropna(subset=["precio"])     → solo si falta en columnas críticas
  df["precio"] = df["precio"].fillna(df["precio"].median())   → imputar
  df = df.rename(columns=str.lower)         → columnas en minúsculas
  df = df.drop_duplicates()                   → quitar duplicados
  df["fecha"] = pd.to_datetime(df["fecha"])   → parsear fechas de verdad

TRANSFORMAR Y CREAR
  df["total"] = df["precio"] * df["cantidad"]
  df["Categoria2"] = df["precio"].apply(lambda p: "caro" if p > 100 else "barato")
  df["anio"] = df["fecha"].dt.year                            → acceder a partes de fecha
  df = df.sort_values("total", ascending=False)
  df.reset_index(drop=True, inplace=True)

CADENA de métodos limpia y legible (method chaining, muy común en código pro).""",
  [("¿Qué hace df.isna().sum()?", ["Suma todo", "Cuenta valores faltantes POR COLUMNA: la primera revisión de salud de un dataset", "Borra NAs", "CSV"], 1, "Antes de analizar: ¿cuántos huecos hay y dónde? Ahí decides tu estrategia de limpieza."),
   ("¿fillna con la mediana vs dropna?", ["Siempre dropna", "fillna conserva todas las filas imputando un valor neutro; dropna las elimina — depende del caso", "Ninguna diferencia", "fillna es un error"], 1, "Poquitas filas → drop; muchas → imputar. La mediana es robusta a outliers.")]),
 ("3. groupby y agregaciones: análisis de negocio directo", """GROUPBY: RESUMIR = ENTENDER
━━━━━━━━━━━━━━━━━━━━━━━━━━━
  # ¿cómo va cada categoría?
  resumen = df.groupby("categoria")["total"].sum()
  # varias estadísticas a la vez:
  agg = df.groupby("categoria").agg(
      ventas_total=("total", "sum"),
      promedio=("total", "mean"),
      operaciones=("total", "count"),
      mejor=("total", "max"),
  ).reset_index()

  df.groupby(["categoria", "mes"])["total"].sum()     # multi-grupo → MultiIndex
  .unstack()                                          # pivota: filas→columnas

  df["categoria"].value_counts()        # conteo rápido por valor (MÁS usado del mundo)

  pd.pivot_table(df, values="total", index="categoria", columns="mes", aggfunc="sum", fill_value=0)

MERGE/JOIN como SQL (combiñar tablas por clave):
  pd.merge(ventas, clientes, on="cliente_id", how="left")   # how: inner/left/right/outer
  pd.concat([df1, df2])                                      # apilar filas

MEJOR = nombre de columna + función con tupla (columñas nombradas, salida legible) — estándar moderno.""",
  [("¿Qué hace df['categoria'].value_counts()?", ["Ordena", "Cuenta frecuencia de cada valor: la vía rápida de 'top categorías' sin SQL", "Exporta", "CSV"], 1, "El one-liner favorito: en 1 llamada tienes el panorama categorial más común."),
   ("pd.merge(a, b, on='id', how='left') se comporta como...", ["concatenar", "LEFT JOIN de SQL: todas las filas de 'a' + datos de 'b' cuando hay coincidencia en id", "UNION", "nada"], 1, "merge=JOIN entre DataFrames por clave; how decide qué filas sobreviven.")]),
 ("4. Fechas, strings y aplicaciones avanzadas (los .dt/.str)", """SERIES CON SUPERPODERES: .dt, .str, .apply
━━━━━━━━━━━━━━━━━━━━━━━━━━━
FECHAS: convierte siempre a datetime primero
  df["fecha"] = pd.to_datetime(df["fecha"])
  df["anio"]  = df["fecha"].dt.year
  df["mes"]   = df["fecha"].dt.month
  df["dia_semana"] = df["fecha"].dt.day_name()
  df.groupby(df["fecha"].dt.to_period("M"))["total"].sum()   # ventas por mes elegantísimo
  rango = df[df["fecha"] >= "2026-01-01"]
  (df["entrega"] - df["compra"]).dt.days                      # duraciones calculadas as days

TEXTO (vectorizado sin loops)
  df["email"] = df["email"].str.lower().str.strip()
  df[df["nombre"].str.contains("silva", na=False)]
  df["dominio"] = df["email"].str.split("@").str[1]
  df["iniciales"] = df["nombre"].str[:2]                       # slice vectorizado

APPLY cuando no hay vector (lo justo y necesario)
  df["segmento"] = df["total"].apply(lambda t: "A" if t > 1000 else "B")
  df = df.assign(nuevo_total=lambda d: d.total * 1.22)       # encadenar sin inplace

REGLA PRO: columnas vectorizadas (.str/.dt/ops) EN VEZ de filas y loops: 10-100× más rápido.""",
  [("¿Qué permite df['fecha'].dt.month después de to_datetime?", ["Nada", "Extraer partes de fecha (mes/año/día/nombre) VECTORIZADO sobre toda la columna", "Texto", "Índices"], 1, "El accesor .dt convierte fechas en datos analizables: estacionalidad, agrupar por mes..."),
   ("df['email'].str.contains('silva', na=False) — ¿por qué na=False?", ["Decora", "contains con NA devuelve NA y rompe filtros booleanos: na=False lo maneja seguro", "Es más rápido", "Para mayúsculas"], 1, "Detalle que evita un error común al filtrar strings con valores faltantes.")]),
 ("5. Visualización rápida y detección de historias", """GRÁFICOS AL INSTANTE: LA HISTORIA EMERGE
━━━━━━━━━━━━━━━━━━━━━━━━━━━
  import matplotlib.pyplot as plt            (pip install matplotlib)
  df["total"].hist(bins=30); plt.show()     → distribución (¿normal? ¿sesgada?)
  df.plot(x="fecha", y="total"); plt.show() → líneas temporal
  df.groupby("categoria")["total"].sum().plot.bar(); plt.show()
  df.plot.scatter(x="precio", y="cantidad"); plt.show()  → relación entre variables
  df.boxplot(column="total", by="categoria"); plt.show() → comparar distribuciones

MATPLOTLIB DETALLES DE CALIDAD
  plt.title("Ventas mensuales 2026"); plt.xlabel("Mes"); plt.ylabel("Total")
  plt.tight_layout(); plt.savefig("grafico.png", dpi=150)   → exportar escala

SEABORN (estadístico bonito, cascarón sobre matplotlib) — opcional nivel up:
  import seaborn as sns
  sns.histplot(df["total"], kde=True)
  sns.scatterplot(data=df, x="precio", y="cantidad", hue="categoria")
  sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="coolwarm")   → correlaciones

REGLA DEL ANALISTA: grafica ANTES de modelar. Un boxplot revela más en un vistazo que diez resúmenes numéricos.""",
  [("¿Cuál gráfico muestra relación entre dos numéricos?", ["bar", "scatterplot: cada punto una observación - revela correlaciones, clusters y outliers de un vistazo", "histograma", "pie"], 1, "Dispersión = radiografía de relaciones: la intuición primera de cualquier análisis bivariado."),
   ("¿Qué revela un boxplot por categoría que un promedio no?", ["Nada", "Distribución completa y OUTLIERS por grupo: el promedio solo cuenta la historia central", "Solo máximo", "Solo skew"], 1, "Dos categorías con el mismo mean pueden tener varianzas y outliers mundialmente distintos.")]),
 ("6. Proyecto final: EDA completo de un dataset público", """TU EDA PROFESSIONAL (60-90 MINUTOS, ENTREGABLE)
━━━━━━━━━━━━━━━━━━━━━━━━━━━
Dataset sugerido: Titanic (seaborn: sns.load_dataset("titanic") gratis) o un CSV de datos abiertos de tu país. Jupyter/Colab recomendado (celdas=silverbullet de la narrativa de datos).

ESTRUCTURA DEL NOTEBOOK (documentable, PON POR ESCRITO LO QUE VES)
1. PREGUNTA guía (ej: "¿qué influyó en sobrevivir?") — = 50% del análisis
2. CARGA + PRIMER VISTAZO: shape · dtypes · head · describe · isna.sum
3. LIMPIEZA DOCUMENTADA: df.limpio = df.dropna(subset=[...]) → justificas en una celda Markdown
4. COLUMNAS DERIVADAS: df["familia"] = SibSp + Parch + 1 · categorías útiles
5. ANÁLISIS POR PREGUNTA:
   survival_rate_por_clase = df.groupby("Pclass")["Survived"].mean()
   El group by + value_counts para TODAS tus preguntas
6. 3-5 GRÁFICOS imprescindibles: tasa por sexo (bar) · por clase (bar) · edades (hist) · fare vs survived
7. CONCLUSIÓN: 3 bullets CON NÚMEROS DEFINITIVOS en markdown final

ENTREGABLE: notebook limpio (corre de arriba a abajo: Kernel → Restart & Run All) + README con screenshot y 3 aprendizajes clave.
Este documento es tu primera pieza de portafolio de datos.""",
  [("¿Qué verifica 'Restart Kernel & Run All'?", ["Nada", "Que tu notebook se ejecute limpio de arriba a abajo en orden — reproducibilidad real de tu análisis", "Es más rápido", "La BIOS"], 1, "Orden del código más importante: tu análisis debe reproducirse sin celdas corridas a desorden."),
   ("¿Por qué df.groupby('Pclass')['Survived'].mean() da la tasa de supervivencia?", ["Por casualidad", "El promedio de una columna 0/1 = la proporción/tasa: mean de binarios es tasa universal", "Es solo moda", "Sum()"], 1, "El truco universal de datos: promediar flags 0/1 te da porcentajes directos en una línea.")]),
],
# ═══════════════════ 31. MACHINE LEARNING (5) ═══════════════════
"Machine Learning — Primer Contacto Real": [
 ("1. ML honesto: qué es y qué NO es", """MACHINE LEARNING SIN HYPE
━━━━━━━━━━━━━━━━━━━━━━━━━━━
Definición: programas que aprenden patrones DE LOS DATOS en vez de seguir reglas escritas a mano.
Clásico: escribir "si email tiene 'gratis' → spam". ML: muéstrale 10.000 emails etiquetados y APRENDE él el patrón.

LOS 3 TIPOS GRANDES
1. SUPERVISADO (90% del mundo real): datos con respuesta conocida
   → Clasificación (spam/no spam, fraude/no fraude · respuesta = categoría)
   → Regresión (precio de casa, temperatura · respuesta = número)
2. NO SUPERVISADO: sin respuesta, encuentra estructura
   → Clustering (agrupa clientes parecidos) · Reducción dimensional
3. REFUERZO: aprender por recompensas (juegos, robots) — campo aparte

WORKFLOW REAL (aprende este mapa YA)
  datos → dividir (train/test) → entrenar en train → evaluar en test (datos que el modelo NUNCA vio) → medir → mejorar
La regla SAGRADA: nunca evalúas con datos vistos en entrenamiento (evaluarías memorización, no aprendizaje).

sklearn = tu navaja suiza  (pip install scikit-learn): el estándar para ML clásico.""",
  [("¿Cuál es la REGLA SAGRADA del ML?", ["Más datos siempre", "Evaluar en datos de TEST separados que el modelo nunca vio en entrenamiento", "Usar más capas", "GPU obligatoria"], 1, "Sin test separado solo mides memoria, no capacidad de generalizar."),
   ("Precio de una casa según m², zona, habitaciones es...", ["clasificación", "REGRESIÓN: predecir un NÚMERO (continuo), no una categoría", "clustering", "visión"], 1, "Regresión = número; clasificación = etiqueta/categoría. Letra chica que decide tu modelo.")]),
 ("2. Tu primer modelo: train/test y accuracy real", """KNN DE DÍA 1: ML EN 15 LÍNEAS CON SKLEARN
━━━━━━━━━━━━━━━━━━━━━━━━━━━
  from sklearn.model_selection import train_test_split
  from sklearn.neighbors import KNeighborsClassifier
  from sklearn.metrics import accuracy_score, confusion_matrix
  from sklearn.datasets import load_iris

  iris = load_iris()                            # dataset de juguete (flores)
  X, y = iris.data, iris.target                 # X = features (medidas) · y = etiqueta (especie)

  X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

  modelo = KNeighborsClassifier(n_neighbors=3)   # "dime con quién andas"... 3 vecinos votan
  modelo.fit(X_train, y_train)                  # ¡entrena!
  predicciones = modelo.predict(X_test)
  acc = accuracy_score(y_test, predicciones)
  print(f"Precisión: {acc:.2%}")                # ~96%+ en iris
  print(confusion_matrix(y_test, predicciones)) # dónde se equivoca

EL ENTENDIMIENTO > la métrica: pregunta por qué se equivocó (mirar la matriz de confusión).
random_state=42 = reproducible (misma división siempre): estándar de experimentos serios.
fit/predict = la API de sklearn universal: TODOS los modelos responden igual → aprendes uno, sabes todos.""",
  [("¿Qué hacen fit() y predict() en sklearn?", ["Lo contrario", "fit aprende de datos de ENTRENAMIENTO; predict va'ven predicciones sobre datos nuevos", "Son de pandas", "Miden tiempo"], 1, "API universal: instanciar modelo→fit(X_train, y)→predict(X) repite en toda sklearn."),
   ("¿Para qué sirve la matriz de confusión?", ["Confundir al usuario", "Ver no solo AL error sino QUÉ se confunde con QUÉ: errores específicos por clase", "Medir tiempo", "Gráfica"], 1, "Diagonal = aciertos; fuera de diagonal = confusiones específicas que guían mejora.")]),
 ("3. Overfitting vs underfitting y validación", """EL DILEMA CENTRAL: MEMORIZAR VS APRENDER
━━━━━━━━━━━━━━━━━━━━━━━━━━━
• UNDERFIT (falta aprender): muy simple. Fallas en train Y test. Complejidad insuficiente → agrégala.
• OVERFIT (memorizó): muy complejo. Perfecto en train, malo en test. Viene de "exámenes memorizados".

En el día a día: si train 99% pero test 70% → OVERFIT claro → el modelo memorizó tu muestra.

REMEDIOS CONTRA OVERFIT (los que usan los pros)
1. MÁS DATOS (la medicina maestra si puedes)
2. Modelo SIMPLE primero (baseline); solo complica si mejora test
3. REGULARIZACIÓN (penalizar complejidad: Ridge/Lasso en lineales, max_depth en árboles)
4. VALIDACIÓN CRUZADA:
   from sklearn.model_selection import cross_val_score
   scores = cross_val_score(modelo, X, y, cv=5)   → 5 evaluaciones rotando → media y desviación: mucho más robusto que UN solo split

CURVA de aprendizaje: ¿más datos mejoran tu test? si sí, conseguir más datos vale más que ajustar parámetros una semana (reality check útil)""",
  [("Train 99%, test 72%. ¿Diagnóstico?", ["Está perfecto", "OVERFIT: memorizó el entrenamiento, no generaliza — modelo demasiado complejo para los datos", "Underfit", "Mala métrica"], 1, "La brecha train>>test es el síntoma canónico de sobreajuste."),
   ("¿Qué aporta cross_val_score(modelo, X, y, cv=5) sobre un solo split?", ["Nada", "Evalúa 5 veces con particiones rotadas: medida mucho más estable y robusta de tu desempeño real", "Solo velocidad", "Solo pega"], 1, "Un solo split puede tener suerte/mala suerte con qué datos tocaron: la CV promedia esa lotería.")]),
 ("4. Árboles de decisión y RandomForest: los caballos de batalla", """LOS MODELOS QUE DOMINAN EL MUNDO REAL
━━━━━━━━━━━━━━━━━━━━━━━━━━━
ÁRBOL: reglas si/entonces leíbles (dile a tu jefe "ESPAÑA + saldo alto → compra")
  from sklearn.tree import DecisionTreeClassifier
  arbol = DecisionTreeClassifier(max_depth=3, random_state=42)   # ← FRENO anti-overfit
  arbol.fit(X_train, y_train)
  from sklearn.tree import export_text
  print(export_text(arbol, feature_names=iris.feature_names))  # REGLAS LEGIBLES 🎉

RANDOM FOREST (el upgrade con votación democrática, casi siempre mejorazo)
  from sklearn.ensemble import RandomForestClassifier
  bosque = RandomForestClassifier(n_estimators=100, max_depth=5, random_state=42, n_jobs=-1)
  bosque.fit(X_train, y_train)

  importancia = bosque.feature_importances_     # ← Qué FEATURES mandan en las decisiones
  for nombre, imp in sorted(zip(iris.feature_names, importancia), key=lambda x: -x[1]):
      print(f"{nombre}: {imp:.3f}")

POR QUÉ SON LOS FAVORITOS INDUSTRIALES: robustos, piden poca preparación de datos, dan importancias de features explicables. Deep Learning solo gana en imágenes/audio/texto grande; para tablas, los RandomForest/GradientBoosting (XGBoost etc) suelen seguir coronando.

En tu práctica: lineal (baseline) → luego RF → ¿mejoró test? si no, quédate con el simple: interpretabilidad y velocidad ganan.""",
  [("¿Qué ventaja práctica tiene max_depth=3?", ["Ninguna", "Limita la complejidad del árbol: techo de cristal al overfit (regularización por construcción)", "Más datos", "Más CPU"], 1, "Árbol profundo = reglas sobreajustadas de poquitas muestras; poco profundo generaliza bien."),
   ("¿Qué te dice feature_importances_?", ["Velocidad", "QUÉ VARIABLES pesan más en las decisiones del modelo: comprensión/explicación del negocio incluida", "Cardiología", "CSV"], 1, '"Los 2 mejores predictores son..." directo del bosque: insights accionables.')]),
 ("5. Proyecto: pipeline completo de ML con datos reales", """TU PRIMER PROYECTO ML COMPLETO (2 horas)
━━━━━━━━━━━━━━━━━━━━━━━━━━━
Dataset: Titanic (sns.load_dataset("titanic")) — meta: ¿viaja en esa clase con ese sexo... sobrevives?

  import seaborn as sns, pandas as pd
  from sklearn.model_selection import train_test_split, cross_val_score
  from sklearn.ensemble import RandomForestClassifier
  from sklearn.metrics import accuracy_score

  df = sns.load_dataset("titanic").dropna(subset=["age", "embarked"])
  # FEATURE ENGINEERING básico (la diferencia entre fracasar y funcionar):
  df["sol@"] = (df.sibsp + df.parch == 0).astype(int)
  df = pd.get_dummies(df, columns=["sex", "embarked"], drop_first=True)   # categorías → numérico
  features = ["pclass", "age", "fare", "sol@", "sex_male", "embarked_Q"]
  X, y = df[features], df["survived"]

  X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.2, random_state=42)
  m = RandomForestClassifier(n_estimators=100, max_depth=4, random_state=42)
  m.fit(X_tr, y_tr)
  print(f"Test: {accuracy_score(y_te, m.predict(X_te)):.2%}")        # ~80% típico
  print(f"CV 5-fold: {cross_val_score(m, X, y, cv=5).mean():.2%}")   # valida real

CHECKLIST PRO: EDA previa · NA manejados · get_dummies · baseline vs RF comparados · feature_importances_ leídas · conclusión escrita. Eso es ML honesto de nivel junior sólido.""",
  [("¿Qué hace pd.get_dummies sobre columnas categóricas?", ["Las borra", "Convierte categorías en columnas binarias 0/1 para que el algoritmo procese números", "Ordena", "CSV"], 1, "Los modelos comen números: género/embarque/categorías → one-hot encoding."),
   ("¿Qué es FEATURE ENGINEERING en este proyecto?", ["SQL", "CREAR columnas útiles desde las existentes (ej: sol@ si viajas solo): el 40% de tu mejora suele vivir aquí", "Hype", "GPU"], 1, "Pequeñas obviedades transformadas en datos = a veces más valor que elegir otro modelo.")]),
],
# ═══════════════════ 32. IA, PROMPTS Y OLLAMA (4) ═══════════════════
"IA Moderna y LLMs — Trabajar con Modelos Locales": [
 ("1. LLMs bajo el capó (en 10 frases)", """QUÉ ES REALMENTE UN LLM (SIN MAGIA)
━━━━━━━━━━━━━━━━━━━━━━━━━━━
1. Un LLM es una función estadística GIGANTE entrenada para predecir el siguiente token (pedazo de palabra) dado el contexto.
2. Esa simpleza + miles de millones de textos → emergen capacidades: resumir, escribir código, traducir...
3. NO es consciente ni "entiende": genera texto PLAUSIBLE según patrones. Alucinar = inventar con confianza estadística.
4. Contexto = tu prompt + historial (limitado: la ventana de contexto). Lo que está ahí, lo ve; lo que no, no.
5. Temperature: 0 = determinista/preciso; 1+ = más creativo/azaroso.
6. Tokens: cobranse por tokens (~0.75 palabra cada uno en general); modelos grandes = más capaces, más caros/lentos.
7. Correr LOCAL vs CLOUD: Ollama/cor en tu máquina = privado/gratis/offline pero modelos más chicos; APIs (OpenAI etc) = más capaces pero tus datos salen.
8. SYSTEM PROMPT: instrucciones permanentes que configuran al modelo por conversación (esta app lo usa: "responde corto en español").
9. Few-shot: dar 2-3 ejemplos de entrada→salida en el prompt = MUCHO mejor salida (el modelo copia tu formato).
10. La IA amplifica: un experto con IA = cohete; quien no entiende el tema no puede AUDITAR la salida. Por eso primero dominas tú.""",
  [("¿Cómo decide un LLM qué escribir?", ["Pensando", "Es una función estadística entrenada en predecir el siguiente token según el contexto dado", "Buscando en su base exacta", "Debatiendo consigo"], 1, "Estadística aplicada al lenguaje: capacidades emergen, pero no hay comprensión consciente."),
   ("¿Qué es 'alucinar' en un LLM?", ["Dormir", "Generar información INVETNADA con alta confianza aparente (porque es probabilidad, no base de datos de hechos)", "Crashear", "Traducir"], 1, "Por esto: todo dato factual importante generado por IA se VERIFICA en fuentes reales.")]),
 ("2. Prompts que funcionan: las 5 recetas", """INGENIERÍA DE PROMPTS PARA DEVS
━━━━━━━━━━━━━━━━━━━━━━━━━━━
RECETA 1 — ROL+CONTEXTO+TAREA+FORMATO
  "Eres un mentor senior de Python. Contexto: app Flask con errores 500.
   Tarea: explícame por qué este decorador rompe y dame el fix paso a paso.
   Formato: causa raíz (1 línea) + explicación + código corregido."
RECETA 2 — EJEMPLOS (few-shot)
  "Convierte a snake_case:
   MiVariable → mi_variable, OtroCoso → otro_coso,
   TuEntrada → "     → rellena perfecto aprendiendo del patrón
RECETA 3 — PENSAR EN VOZ ALTA (chain-of-thought)
  "Resuelve paso a paso y luego la respuesta final" → menos errores en lógica
RECETA 4 — RESTRICCIONES EXPLÍCITAS
  "Sin librerías externas. Máx 20 líneas. Español. Si no sabes, di que no sabes." ← clave anti-alucinación
RECETA 5 — ITERAR COMO CONVERSACIÓN (no como incantación)
  Pide → critica tú → "ese código usa eval: inseguro, reescribe con ast.literal_eval" → mejora y mejora.

PARA CÓDIGO: muestra el CÓDIGO, el ERROR completo y qué esperabas — nunca solo "no funciona" — pega el error real con contexto.""",
  [("¿Por qué el few-shot (dar ejemplos input→output) mejora tanto?", ["Gasta más", "El modelo imita el FORMATO Y EL PATRÓN de tus ejemplos en vez de adivinar", "Es solo marketing", "Nada"], 1, "2-3 ejemplos concretos enseñan estilo/estructura mejor que 10 instrucciones abstractas."),
   ("¿Cuál prompt funciona mejor para debugging?", ["'no anda, fix'", "Pegar el código + el traceback completo + qué esperabas que pasara", "Un emoji", "'mágico'"], 1, "Sin datos concretos el modelo adivina; con contexto real = respuesta de cirujano.")]),
 ("3. Ollama: tu LLM local en 3 comandos", """OLLAMA: MODELOS ABIERTOS EN TU MÁQUINA
━━━━━━━━━━━━━━━━━━━━━━━━━━━
INSTALAR Y PRIMER MODELO
  1. ollama.com → instala (Linux/Mac/Win)
  2. ollama pull llama3.1:8b          (descarga ~5GB primero vez)
  3. ollama run llama3.1:8b           → ¡chat local funcionando offline!

SERVIDOR PARA APPS (como usa esta plataforma):
  ollama serve          → API local en localhost:11434
  curl localhost:11434/api/generate -d '{"model":"llama3.1:8b","prompt":"Hola"}'
  Ollama respeta API tipo OpenAI en /v1 → tus scripts existentes suelen compatir

MODELOS RECOMENDADOS POR CASO (2026, 8GB RAM+)
• Llama 3.1 8B      → mejor general de su clase
• Qwen 2.5 7B       → multilingüe fuertísimo + razonamiento
• Codellama/Qwen-code 7B → evaluar/ayudar código
• Mistral/Gemma pequeños → si tu RAM es limitada (3B corren en laptops modestos)

VENTAJAS LOCALES REALES: privacidad 100% (nada sale de tu PC) · gratis ilimitado · sin internet · aprendes APIs de verdad.
LIMITACIÓN: menos capaces que los gigantes cloud + lentos sin GPU — para el día a día de pruebas suficiente.""",
  [("¿Qué hace ollama run llama3.1:8b?", ["Borra algo", "Descarga (si falta) y abre un chat interactivo con el modelo en tu máquina local", "Edita código", "Minar"], 1, "Tu LLM privado corriendo offline a los 30 segundos de instalarlo."),
   ("¿Qué aporta ollama serve respecto a run?", ["Nada", "Expone el modelo como API HTTP local (localhost:11434) para que TUS programas lo invoquen", "Transcription", "Un VPN"], 1, "El server convierte tu PC en un mini-OpenAI local: esta app misma le habla así.")]),
 ("4. Proyecto: integra IA local en TU app", """CONSTRUYE: ASISTENTE DE ESTUDIO CON TU OLLAMA
━━━━━━━━━━━━━━━━━━━━━━━━━━━
PYTHON PRÁCTICO (5 minutos de código útil):
  import requests
  def preguntar(pregunta, modelo="llama3.1:8b"):
      r = requests.post("http://localhost:11434/api/generate", json={
          "model": modelo,
          "prompt": f"Eres mentor de programación. Responde corto y con ejemplo.\\n\\nPregunta: {pregunta}",
          "stream": False,
      }, timeout=120)
      return r.json()["response"]
  print(preguntar("¿qué es un diccionario en Python?"))

PROYECTO COMPLETO (para tu portafolio):
1. lee un archivo de texto (tus apuntes de una materia)
2. parte el texto en trozos de ~500 palabras
3. para cada chunk: preguntar(f"Resume y genera UNA pregunta de examen sobre:\\n{chunk}")
4. junta los resúmenes + las preguntas en UN solo manual-estudio markdown
5. salida: estudio.md con resumen por sección + quiz consolidado al final

VARIANTE PODEROSA (RAG mental): pegas documentación oficial como contexto al SYSTEM prompt y el modelo responde SOLO a partir de esos textos = menos alucinación (mismo principio que RAG profesional con embeddings).

REGLA PRO: temperature 0.2 para tareas de resumen/responder datos (consistencia), 0.8 para lluvia de ideas.""",
  [("¿Qué es RAG en términos de este proyecto?", ["Un bug", "Proveer TUS documentos como contexto en el prompt para que el modelo responda sobre esa realidad, no se invente", "Un garbage collector", "Red local"], 1, "Retrieval + Generation: tu modelo responde anclado a fuentes reales que tú le das."),
   ("¿Qué temperature elegir para resumen fiel de documentos?", ["1.5", "Baja (~0.2): salida predecible y fiel; alta solo para creatividad/lluvia de ideas", "100", "Ninguna"], 1, "Temperatura baja = determinista; para hechos/resúmenes siempre frío.")]),
],
# ═══════════════════ 33. SEGURIDAD (5) ═══════════════════
"Seguridad para Desarrolladores — No Seas la Brecha": [
 ("1. Los 5 pecados capitales (OWASP real)", """SEGURIDAD SIN PARANOIA: LO QUE ROMPE EL MUNDO
━━━━━━━━━━━━━━━━━━━━━━━━━━━
OWASP Top 10 (las vulnerabilidades MÁS explotadas del mundo, estudiadas en datos reales)
TUS 5 QUE CAUSAN EL 90% DEL DAÑO:

1. 🔓 BROKEN ACCESS CONTROL — cualquiera accede a lo que no debe:
   /admin solo con @login_required NO BASTA: chequea ROL en cada endpoint.
   /api/usuarios/123/expediente → ¿verificás que soy DUEÑO del 123? (IDOR: cambiar el id en la URL y ver datos ajenos)
2. 💉 INYECCIÓN (SQL/Command): datos del usuario interpretados como código.
   "SELECT * WHERE name = '" + input + "'" → ' OR '1'='1 -- destruye login. Prepared statements SIEMPRE.
3. 🍪 FALLAS DE AUTENTICACIÓN: contraseñas en texto plano en la BD (¡!), sesiones que no expiran, sin límite de intentos.
   Contraseñas: hash con bcrypt/argon2 (NUNCA MD5/SHA1 plano).
4. ⚙️ MISCONFIG: debug=True en producción, errores con stacktrace a usuarios, headers por defecto, puertos abiertos de más.
5. 📦 DEPENDENCIAS VULNERABLES: npm install viejo con CVEs abiertas.
   pip-audit / npm audit / dependabot → actualiza lo que instalas.

PRINCIPIO RECTOR: NUNCA CONFIAR EN DATOS DEL USUARIO (entrada = potencial ataque hasta demostrar lo contrario).""",
  [("¿Qué es IDOR?", ["Un hámster", "Broken Access Control: cambiar el ID en la URL y acceder a datos de OTROS usuarios porque el servidor no verifica propiedad", "Una base de datos", "Un virus"], 1, "/perfil/1 → cambias a /perfil/2 y ves datos ajenos si el servidor no checkea dueño."),
   ("¿Cómo se guardan contraseñas correctamente?", ["Texto plano", "MD5", "Hash con bcrypt/argon2 + salt: ni siquiera tú (admin) puedes leerlas", "Base64"], 2, "El hash robusto es irreversible y lento a propósito: el que dicen los propios hashes débiles.")]),
 ("2. HTTPS, headers y sanitización: cimientos prácticos", """DEFENSA EN CAPAS (LO QUE CONFIGURAS HOY)
━━━━━━━━━━━━━━━━━━━━━━━━━━━
HTTPS OBLIGATORIO SIEMPRE
• Todo login/dato viaja cifrado. Certbot + Let's Encrypt = gratis y automático.
• Redirect 80→443, y HSTS header (instruye al navegador a usar SIEMPRE https).

HEADERS DE SEGURIDAD (configuración de 5 minutos que suman mucho)
  Content-Security-Policy: default-src 'self'    ← de dónde puede cargar recursos (anti-XSS fuerte)
  X-Frame-Options: DENY                          ← anti clickjacking (no te meten en iframe falso)
  X-Content-Type-Options: nosniff
  Referrer-Policy: no-referrer
  Strict-Transport-Security: max-age=31536000    (HSTS)
En: securityheaders.com pegas tu URL y te evalúa gratis.

SANITIZAR VS ESCAPAR (distintos y ambos necesarios)
• VALIDAR: formato, tipo, rango ("email", número 0-100) al ENTRAR
• ESCAPAR: convertir <script> a &lt;script&gt; al MOSTRAR → el XSS muere de risa
  Frameworks modernos (React {{}}, Django {{ }} escapan por defecto; cuando usas innerHTML/href dinámicos arriesgas.
• Cookies seguras: HttpOnly (JS no las lee, anti-XSS robo) + Secure (solo https) + SameSite=Lax (anti-CSRF)""",
  [("¿Qué hace el atributo HttpOnly en una cookie?", ["Oculta del JS", "El JavaScript NO puede leerla: si un atacante ejecuta XSS no te roba la sesión", "La hace lenta", "Borra cookies"], 1, "Las cookies de sesión SIEMPRE HttpOnly + Secure + SameSite."),
   ("¿Qué defensa da Content-Security-Policy?", ["Bloquea IPs", "Limita de QUÉ orígenes pueden cargarse scripts/recursos: corta de raíz muchísimos XSS", "Acelera", "Nada útil"], 1, "CSP bien puesta desactiva la ejecución de scripts inyectados inline.")]),
 ("3. Autenticación moderna: sesiones, JWT y OAuth", """LOGIN 2026: 3 FORMAS, TODAS COMPRENDIDAS
━━━━━━━━━━━━━━━━━━━━━━━━━━━
1. SESIONES CLÁSICAS (estado en el SERVIDOR, seguro y sencillo)
   Login → BD guarda session_id → cookie HttpOnly la lleva → cada request la verifica.
   Pros: revocación fácil (borras sesión); Contras: servidor mantiene estado (memoria/Redis).
2. JWT (JSON Web Token, el estado viaja FIRMADO)
   El servidor firma payload + tu secreto: cliente guarda, envía en cada request (Authorization: Bearer ...).
   Estructura: header.payload.signature (¡el payload NO es secreto! es legible base64: mete poco)
   Pros: stateless (escala fácil); Contras: mala revocación (hasta expirar), renewal complejo.
3. OAUTH2 (login con Google/GitHub)
   No implementes tu contraseña si evitas: "Sign in with Google" delega correctamente.
   Flujo: app → alcance autorizado → código → token → perfil del usuario. Úsalo con librerías probadas (NUNCA OAuth casero).

REGLAS SAGRADAS
• Expira JWTs cortos (15min) + refresh tokens seguros
• Nunca en localStorage para JWTs sensibles (XSS te lo roba): cookie HttpOnly mejor
• Rate limiting en /login (5 intentos/min): corta fuerza bruta""",
  [("¿Qué diferencia sesión-clásica de JWT?", ["Ninguna", "Sesión clásica guarda estado en el servidor con ID en cookie; JWT firma y viaja el estado EN EL TOKEN (stateless)", "JWT es más seguro", "Sesión es para APIs"], 1, "Trade: estado revocable/central vs escalabilidad sin estado ni revocación simple."),
   ("¿Por qué JWT en localStorage es riesgoso?", ["Es lento", "Cualquier XSS puede JavaScript-leerlo y robar identidad; cookie HttpOnly no es legible por JS", "No existe", "Es ilegal"], 1, "El trade de seguridad: lo que JavaScript toca, un XSS también toca.")]),
 ("4. Amenazas en el código diario: XSS, CSRF y uploads", """LOS 3 MONSTRUOS COTIDIANOS DEL LADO CLIENTE
━━━━━━━━━━━━━━━━━━━━━━━━━━━
XSS (Cross-Site Scripting): atacante mete JavaScript en tu página y se ejecuta en navegadores ajenos.
  Vector: renderizar crudo lo que escribe el usuario: <img src=x onerror=robar()>
  Defensa: escapar SIEMPRE output (framework lo hace), CSP, evitar innerHTML/v-html con datos,
           sanitizar librerías probadas (DOMPurify) si HTML permitido.

CSRF (Cross-Site Request Forgery): usas mi sesión logueada para que YO haga acciones sin saberlo.
  Vector: mi banca logueada + página maliciosa envía <img src="banca.com/transferir?a=atacante&monto=1000">
  Defensa: tokens CSRF en formularios (el servidor solo acepta posts con su token aleatorio),
           cookies SameSite=Lax/Strict (no se mandan desde sitios cruzados).

UPLOADS (riesgo subido a 11)
  Nunca confiar extensión ni Content-Type (¡los falsifican!)
  Reglas: whitelist de extensiones · limita tamaño · chequea el MAGIC BYTES real (cabecera del archivo)
  · guarda fuera del root del servidor · nombres generados por ti (no el del usuario) · antivirus
  · imágenes: re-procesar (Pillow/ImageSharp las sanitiza normalizando).

PRINCIPIO TRANSVERSAL: toda decisión de seguridad = preguntar "¿y si el usuario es mi enemigo?" antes de escribir el endpoint.""",
  [("¿En qué difiere XSS de CSRF?", ["Son iguales", "XSS roba/ejecuta en NAVEGADOR ajeno (inyectar JS); CSRF fuerza ACCIONES con tu sesión (abusa confianza del sitio)", "Mismo vector", "CSRF es más viejo"], 1, "XSS=inyección de scripts en users finales; CSRF=peticiones falsificadas usando la sesión del usuario."),
   ("¿Cuál defensa mata CSRF de forma estructural?", ["Hash", "Token CSRF único por formulario/sesión que el atacante no puede conocer + SameSite en cookies", "HTTPS solo", "CSP"], 1, "El atacante puede enviar el request PERO no el token secreto del formulario legítimo.")]),
 ("5. Proyecto: auditoría de seguridad propia", """AUDITA TU PROPÍA APP (LO QUE HACE UN BLUE TEAM JUNIOR)
━━━━━━━━━━━━━━━━━━━━━━━━━━━
CHECKLIST OPERATIVA (60 min, sobre una app tuya desplegada)
1. CABECERAS: mete tu URL en securityheaders.com → anota qué falta (CSP, HSTS, X-Frame...)
   → agrégalas en tu servidor y vuelve a pasar: meta >= A
2. INPUTS: intenta escribir <script>alert(1)</script> en cada campo/caja
   → si aparece el alert en TUS ojos: HAY XSS. Arregla con escape/sanitización y vuelve a probar SIN alert.
3. IDOR: logueado como user A, cambia la URL/recurso a otro id
   → ¿ves el contenido? Endpoint roto. Corrige: verifica dueño en el servidor, siempre.
4. CONTRASEÑAS: pon 'aaaaa' como contraseña nueva → si ADMITE, no hay política frr
   (juguete lont) Fuerza bruta: 5 intentos cortos → si no hay rate limit, debilidad anotada.
5. DEPENDENCIAS: pip-audit (o npm audit) → lista de paquetes con vulnerabilidad conocida
   → actualiza lo urgente a versiones seguras y re-corre.

BONUS NIVEL+: OWASP ZAP/Burp Suite Community hacen scanning automático gratis sobre tu app local/expuesta.

ENTREGABLE: un informe markdown "auditoría-mi-app.md" con hallazgos (severidad), evidencia y fix aplicado.
Esto = tu primera línea "seguridad práctica" en portafolio/CV — distingue muchísimo.""",
  [("¿Qué descubre pegar <script>alert(1)</script> en un campo y probar?", ["Nada", "Si ves el alert: tu app ejecuta código de usuario = XSS confirmado", "El backend", "El SEO"], 1, "La prueba ácida manual del XSS: si JS injectado corre, tu escape no es suficiente."),
   ("¿Por qué testear IDOR es tan crítico para endpoints con IDs?", ["Aburrido", "Es la vulnerabilidad web nº1 real: chequear que solo el DUEÑO accede a su recurso por cada request", "Backend only", "PCI"], 1, "La lección: no confíes en la URL escondida: cada query/id verifica ownership server-side.")]),
],
# ═══════════════════ 34. TESTING (5) ═══════════════════
"Testing — Programar con Red de Seguridad": [
 ("1. Tests: por qué son parte del código, no un extra", """EL MINDSET DE PRUEBAS DESDE EL DÍA 1
━━━━━━━━━━━━━━━━━━━━━━━━━━━
Un test es código que PRUEBA tu otro código automáticamente. Corre en segundos mil veces al día.

POR QUÉ LOS EQUIPOS SERIOS EXIGEN TESTS
• 🛡 RED DE SEGURIDAD: refactorizas sin miedo — si rompiste algo, el test grita ya
• 📐 DOCUMENTACIÓN VIVA: el test muestra cómo se USA la función (mejor que comentarios viejos)
• 🧠 DISEÑO FORZADO: código difícil de testear = código mal acoplado (avisito de diseño temprano)
• 🟢 CI/CD: sin tests no hay despliegue continuo responsable (el pipeline necesita validar solo)

EL CICLO TDD (Test-Driven Development, disciplina opcional pero poderosa)
1. 🔴 RED: escribes UN test que FALLA (la funcionalidad aún no existe)
2. 🟢 GREEN: escribes El MÍNIMO código que lo hace pasar
3. 🔵 REFACTOR: mejoras el código, tests siempre verdes

MANTRA: "No es código hecho hasta que tiene test". Y los tests NO deben depender de red/BD/reloj:
usa MOCKS para que corran sin internet siempre igual (test rápido + confiable).""",
  [("¿Qué te permite refactorizar sin miedo?", ["Suerte", "Una buena suite de tests: si rompes algo al refactor, un test grita al instante", "ORM", "TypeScript solo"], 1, "El valor práctico nº1 de una suite: cambiar código con confianza."),
   ("¿Por qué un test no debe tocar internet/reloj reales?", ["Es más rápido", "Para ser RÁPIDO, REPETIBLE y CONFIABLE: mismo resultado siempre, en cualquier máquina, sin depender de afuera", "Solo en CI", "Sin razón"], 1, "Mocks/fakes sustituyen lo externo: tu test decide el comportamiento externo, no la red.")]),
 ("2. Pytest, Jest y asserts: la gramática universal", """LA GRAMÁTICA DE LAS PRUEBAS (PYTEST COMO EJEMPLO)
━━━━━━━━━━━━━━━━━━━━━━━━━━━
  # operaciones.py
  def dividir(a, b):
      if b == 0:
          raise ValueError("división por cero")
      return a / b

  # test_operaciones.py (pytest los descubre solos por nombre)
  import pytest
  from operaciones import dividir

  def test_division_normal():
      assert dividir(10, 2) == 5

  def test_division_errores():
      with pytest.raises(ValueError):
          dividir(5, 0)

  @pytest.mark.parametrize("a,b,esperado", [(10,2,5), (9,3,3), (1,4,0.25)])   # tabla 3 casos en 1
  def test_varios(a, b, esperado):
      assert dividir(a, b) == esperado

AAA patrón sagrado de cada test: Arrange (preparar) → Act (actuar) → Assert (verificar).
Un test = UNA afirmación/pregunta específica con nombre descriptivo (test_deberia_fallar_al_reservar_duplicado).

CASOS QUE TESTEAR UN PRO: camino feliz + bordes (vacío, 0, negativos, máximo) + errores (qué pasa si dato malo).
Correr: pytest -v · pytest -k "division" · pytest --cov (cobertura)""",
  [("¿Qué patrón AAA estructura un buen test?", ["AAA", "Arrange (preparar datos) → Act (ejecutar lo probado) → Assert (verificar el resultado)", "3 tests", "Atributos"], 1, "Estructura legible y consistente: la legibilidad de los tests es deuda evitada."),
   ("¿Qué hace pytest.raises(ValueError) en with?", ["Lanza error en pytest", "Verifica que el código LANZA esa excepción concreta — test del comportamiento de error", "Mata el test", "Catch"], 1, "Probar los caminos de error es tan importante (o más) que el camino feliz.")]),
 ("3. Mocks, fixtures y el arte de aislar", """TEST DOBLE: TU LABORATORIO SIN SORPRESAS
━━━━━━━━━━━━━━━━━━━━━━━━━━━
MOCK = simular lo externo (API, email, BD, hora) para probar SOLO lo tuyo.
  from unittest.mock import patch, MagicMock
  def clima_ciudad(ciudad):
      r = requests.get(f"https://api.clima/{ciudad}")
      return r.json()["temp"]

  @patch("miapp.requests.get")                       # interceptamos la llamada a la red
  def test_clima(mock_get):
      mock_get.return_value.json.return_value = {"temp": 25}   # el "clima" del laboratorio
      assert clima_ciudad("Montevideo") == 25
Ahora el test corre sin internet, sin API real, siempre igual. ESO es el punto.

FIXTURES (pytest): preparación compartida sin repetir
  import pytest
  @pytest.fixture
  def usuario_demo():
      return {"nombre": "Ada", "edad": 36}
  def test_nombre(usuario_demo):
      assert usuario_demo["nombre"] == "Ada"
  # scope="module" si lo costoso (BD demo) se crea UNA vez por módulo

NIVELES de test doubles: stub (devuelve fijo) · mock (registra llamadas: verifica QUÉ llamaste) · fake (implementación de juguete: BD en memoria)""",
  [("¿Cuándo usar mock?", ["Siempre", "Cuando tu función llama a algo EXTERNO (red/BD/tiempo) y quieres probar solo tu lógica con respuestas controladas", "Nunca", "Solo restaurar"], 1, "El mock convierte tu entorno en laboratorio: mismos datos, siempre, instantáneo."),
   ("¿Qué reutiliza una fixture de pytest?", ["Nada", "La preparación compartida entre muchos tests (datos de prueba, conexiones, objetos complejos)", "El modal", "Docker"], 1, "Fixture = DRY aplicado a tests: un usuario demo se define una vez y todos lo usan.")]),
 ("4. Cobertura, TDD práctico y tests de integración", """MÁS ALLÁ DEL TEST UNITARIO
━━━━━━━━━━━━━━━━━━━━━━━━━━━
COBERTURA — métrica útil (pero muerte por meta)
  pip install pytest-cov; pytest --cov=miapp --cov-report=term-missing
Te muestra qué líneas/branches corrieron los tests. 80% sano > 100% fanático (puede encubrir asserts débiles).

TDD PRÁCTICO (no dogma, SÍ herramienta)
  Bug reportado → escribe el TEST que FALLA reproduciendo el bug → arréglalo → test pasa → CI verde para siempre.
  (Este flujo vuelve cada bug en un caso de test eterno: jamás devuelve por arte de magia.)

TESTS DE INTEGRACIÓN/E2E — pocos, controlados, vivos
• Integración: varios componenteścon un entorno controlado: API con BD de prueba (docker compose -f test)
• E2E: simular usuario real completo (Playwright/Selenium):
  page.goto() → escribir → click → verificar texto: navegador real automatizado
  En CI corren tras los unitarios (más lentos): estructura 'smoke tests' para lo más crítico.

REGLA DE PIPELINE SANO: unitarios rápidos SIEMPRE · integración ligeros · E2E de lo esencial. Cobertura alta pero tests ÚTILES, no relleno.""",
  [("¿Cuál es la mejor forma de evitar que un bug VUELVA?", ["Comentarios", "Escribir PRIMERO el test que reproduce el bug: queda eternamente verificado en la suite", "Code review", "Más RAM"], 1, "Bug→test rojo→fix→test verde= la regresión muere definitivamente."),
   ("¿Qué diferencia test E2E de integración?", ["Ninguna", "E2E = flujo de usuario REAL completo (browser/UI); integración = componentes juntos sin UI necesariamente", "E2E es más rápido", "Integración es frontend"], 1, "Pocos E2E (frágiles/lentos pero definitivos): el pico de la pirámide.")]),
 ("5. Proyecto: suite de tests real para tu calculadora/app", """CONSTRUYE: CALCULADORA CON TDD REAL (EN VIVO)
━━━━━━━━━━━━━━━━━━━━━━━━━━━
RETO TDD ESTRICTO (40-60 min, disciplina pura):
FUNCIONES: sumar, restar, multiplicar, dividir (con error en cero), porcentaje, memoria (M+, MR).
Por cada función: 🔴 test que falla → 🟢 código mínimo → 🔵 refactor.

# test_calculadora.py
from calculadora import Calculadora
import pytest

@pytest.fixture
def calc(): return Calculadora()

def test_suma(calc):
    assert calc.sumar(2, 3) == 5

def test_resta_negativos(calc):
    assert calc.restar(-2, -3) == 1      # ¡bordes!

def test_dividir_por_cero_lanza_error(calc):
    with pytest.raises(ValueError, match="cero"):
        calc.dividir(5, 0)

@pytest.mark.parametrize("total,pct,esperado", [(200, 10, 20), (50, 50, 25)])
def test_porcentaje(calc, total, pct, esperado):
    assert calc.porcentaje(total, pct) == esperado

# calculadora.py — escríbelo SOLO para que los tests pasen

SUITE COMPLETA: pytest -v con todos ✅ + pytest --cov 90%+.
EJERCICIO ESPIRITUAL: agrega una función NUEVA primero escribiendo SU test. Siente TDD en carne propia.""",
  [("¿Cuál secuencia TDD correcta?", ["Código-test", "🔴 test que falla → 🟢 código mínimo que pase → 🔵 refactor mejorando sin romper el verde", "Test después solo", "Código+garantizar"], 1, "Primero el contrato del comportamiento (test), después el código que lo cumple."),
   ("restar(-2, -3) == 1 es un test de...", ["feliz nomás", "CASO BORDE (números negativos): los pros testean fronteras, no solo caminos felices", "error", "mock"], 1, "Los bugs viven en los bordes: tu suite debe patrullarlos siempre.")]),
],
# ═══════════════════ 35. ALGORITMOS (5) ═══════════════════
"Algoritmos y Estructuras — El Gimnasio del Dev": [
 ("1. Big O: el idioma de la eficiencia", """BIG O: CUÁNTO CRECE EL COSTO CUANDO CRECEN LOS DATOS
━━━━━━━━━━━━━━━━━━━━━━━━━━━
No mide tiempo exacto, mide cómo ESCALA. Lo que importa en el mundo real.

LOS 5 QUE DEBES RECONOCER AL INSTANTE
  O(1)        constante      → dict[key], len(lista): mismo tiempo da igual el tamaño
  O(log n)    logarithmic    → BUSQUEDA binaria: 1 millón de datos → ~20 pasos
  O(n)        lineal         → for sobre la lista: n datos, n pasos
  O(n log n)  linealítmico   → los buenos sorts (merge, quicksort): casi lineal
  O(n²)       cuadrático     → for dentro de for (todos contra todos): 10.000 items = 100M pasos 💀
  O(2ⁿ) / O(n!)  exponencial → backtracking mal escrito (solo para problemas pequeños)

ESTIMARLO A OJO (regla mental)
• un bucle → O(n)·• bucle en bucle → O(n²)·• dividir a la mitad cada vez → O(log n)
• 1.000.000 de datos con O(n log n) = segundos; O(n²) = ¡horas!

ESPAZO (complejdad espacial): cuánta memoria EXTRA usa tu algoritmo (el trade space-time está siempre).

Pragmático real: para listas de ~10 elementos, O(n²) da igual; para un millón, eliges.""",
  [("¿Es rapidez absoluta lo que mide Big O?", ["Sí exacto", "Cómo CRECE el costo al crecer n (escalabilidad), no tiempo exacto", "Solo memoria", "Solo CPU"], 1, "Es la curva de crecimiento que decide si sirve para 10 datos o para 10 millones."),
   ("¿Qué complejidad busca/accede en un dict/hash por clave?", ["O(n)", "O(1) promedio: acces directo sin recorrer", "O(log n)", "O(n²)"], 1, "Por eso los diccionarios/hashes dominan el código real: lookups instantáneos.")]),
 ("2. Buscar: lineal vs binaria + el hash map", """EL PROBLEMA MÁS IMPORTANTE: ENCONTRAR RÁPIDO
━━━━━━━━━━━━━━━━━━━━━━━━━━━
BÚSQUEDA LINEAL (naif): recorrer todo: O(n)
  def buscar(lista, objetivo):
      for i, x in enumerate(lista):
          if x == objetivo: return i
      return -1

BÚSQUEDA BINARIA (¡solo si está ORDENADA!): divide a la mitad: O(log n) ✨
  def binaria(ordenada, objetivo):
      izq, der = 0, len(ordenada) - 1
      while izq <= der:
          medio = (izq + der) // 2
          if ordenada[medio] == objetivo: return medio
          elif ordenada[medio] < objetivo: izq = medio + 1
          else: der = medio - 1
      return -1
  # 1.000.000 de items: ~20 pasos. ESO es O(log n).

HASH MAP/dict: la herramienta que SUSTITUYE búsquedas mil veces
  por_nombre = {u["nombre"]: u for u in usuarios}     # creas el índice una vez
  por_nombre["ada"]                                    # O(1) para siempre después

REGLA PRO: ¿búsquedas repetidas? crea un dict/set ANTES. Pregunta clásica de entrevista: Two Sum (usa dict para O(n) en vez de O(n²) fuerza bruta).""",
  [("¿Qué requisito tiene la búsqueda binaria?", ["Ninguno", "La lista DEBE estar ordenada (si no, divide mal)", "Ser números", "Ser única lista"], 1, "binaria=O(log n) pero necesita order previamente: a veces n log n+bar vale"),
   ("¿Cómo convertir múltiples búsquedas O(n) cada una en O(1) cada una?", ["Más RAM", "Construir UN diccionario/hash indexado UNA vez y consultarlo en O(1) luego", "Bucle for", "SQL"], 1, "Trade tiempo-por-memoria: indexar=prepagar para buscar barato.")]),
 ("3. Ordenar eficientemente: lo que tu lenguaje hace por ti", """SORT: POR QUÉ NINGUN PRO ESCRIBE EL SUYO (PERO SABE QUÉ PASA ABAJO)
━━━━━━━━━━━━━━━━━━━━━━━━━━━
sorted(lista) / lista.sort() → Timsort (Python) / variantes: O(n log n) GARANTIZADO, adaptado, estable — siempre gana a escribir uno.

¿CÓMO FUNCIONA UNO RÁPIDO ABSTRACTO? (merge sort en espíritu)
  divide la lista a la mitad recursivamente → ordena cada mitad (listas de 1 siempre ordenadas) → MERGE de dos ordenadas en O(n)
  total: O(n log n) — el límite matemático para ordenamiento por comparación.

  def merge_sort(lista):
      if len(lista) <= 1: return lista
      medio = len(lista) // 2
      izq, der = merge_sort(lista[:medio]), merge_sort(lista[medio:])
      # merge dos listas ordenadas:
      resultado, i, j = [], 0, 0
      while i < len(izq) and j < len(der):
          if izq[i] <= der[j]: resultado.append(izq[i]); i += 1
          else: resultado.append(der[j]); j += 1
      return resultado + izq[i:] + der[j:]

ESTABLE = preserva orden original de elementos iguales (sort por edad luego nombre: estudiantes iguales conservan orden previo).
ORDENAR CON CLAVE (el truco pro): sorted(personas, key=lambda p: (-p.edad, p.nombre)) → por edad DESC luego nombre ASC.""",
  [("¿Qué complejidad garantiza un sort moderno (Timsort/Timsort-like)?", ["O(n²)", "O(n log n) en el peor caso, con adaptación en datos casi ordenados", "O(n)", "O(1)"], 1, "Por eso los algoritmos de librería estándar superan siempre al casero."),
   ("¿Cómo ordenar por edad descendente y desempatar por nombre?", ["2 sorts", "sorted(personas, key=lambda p: (-p.edad, p.nombre)) con tupla ascendente/descendente del mismo sort", "No se puede", "filter"], 1, "Tuplas en key: orden multi-nivel en UNA Llamada, elegante y estable.")]),
 ("4. Estructuras: pilas, colas y el cuándo elegirlas", """ESTRUCTURA CORRECTA = PROBLEMA MEDIO RESUELTO
━━━━━━━━━━━━━━━━━━━━━━━━━━━
STACK (pila, LIFO: último en entrar, primero en salir)
  pila = []; pila.append(x) ; pila.pop()
  CASOS: undo/redo · validar paréntesis balanceados · historial navegador · recorrido DFS

QUEUE (cola, FIFO: primero en entrar, primero en salir)
  from collections import deque
  cola = deque(); cola.append(x) ; cola.popleft()        # O(1) ambos extremos
  CASOS: procesar tareas en orden de llegada · BFS (recorrido por niveles) · colas de mensajes

  list.pop(0) es O(n) (desplaza todo) ← por qué existe deque en Python: O(1) a principios

SET: pertinencia ultra rápida O(1): if x in visitados (dedup directo: len(set(lista)))
Consejo maestro (pregunta de entrevista): N elementos donde hay duplicados en 1..N → set o frecuencia dict.

ÁRBOLES/GRAFOS (mención strategically importante): nodos con hijos (DOM, archivos, org. charts) y redes (amigos, mapas).
  DFS (profund) con pila/recursión; BFS (anchos/por niveles) con queue.""",
  [("Stack o Queue para implementar UNDO (deshacer)?", ["Queue", "Stack: reverts the last action first (LIFO), el comportamiento natural del deshacer", "Un dict", "List"], 1, "LIFO: la última acción sale primero cuando deshaces."),
   ("¿Por qué deque y no list para queue en Python?", ["Es más corto", "popleft() es O(1) en deque pero O(n) en list (remover del principio desplaza todo)", "No hay list", "Por nada"], 1, "El error rendimiento clásico: list.pop(0) en bucle = degradación invisible a O(n²).")]),
 ("5. Ejercicios prácticos: tu práctica de juicio", """ENTRENAMIENTO REAL: 4 EJERCICIOS CLÁSICOS RESUELTOS MENTALMENTE
━━━━━━━━━━━━━━━━━━━━━━━━━━━
E1 — PARÉNTESIS BALANCEADOS (stack)
  def balanceado(s):
      pila, parejas = [], {")": "(", "]": "[", "}": "{"}
      for c in s:
          if c in "([{": pila.append(c)
          elif c in ")]}":
              if not pila or pila.pop() != parejas[c]: return False
      return not pila
E2 — FRECUENCIA DE LETRA MÁXIMA (dict/contador)
  from collections import Counter
  Counter("banana").most_common(1)    → [('a', 3)]
E3 — TWO SUM (dict = evitar O(n²))
  def two_sum(nums, target):
      vistos = {}
      for i, n in enumerate(nums):
          if target - n in vistos: return [vistos[target - n], i]
          vistos[n] = i
E4 — INVERTIR LISTA O(n) SIN AYUDAS (dos punteros)
  def invertir(a):
      izq, der = 0, len(a) - 1
      while izq < der:
          a[izq], a[der] = a[der], a[izq]
          izq += 1; der -= 1

MÉTODO DE PRÁCTICA: escríbelos desde 0 sin mirar → testéalos con bordes (vacío, 1, todos iguales) → explica la complejidad en voz alta. 3 por semana = entrevistas dominadas en 3 meses.""",
  [("Two Sum con diccionario es O(n) porque...", ["más RAM", "un solo paso por datos + lookup O(1) del complemento ya visto", "es corto", "no es"], 1, "Map de vistos → cada elemento se revisa UNA vez; la fuerza bruta anidada era O(n²)."),
   ("Dos punteros (izq/der) hacia el centro resuelven elegantemente...", ["Nada", "Invertir in-place, palíndromos, búsqueda en ordenados: patrón O(n) universal", "Bases de datos", "Regex"], 1, "Pattern reconocible: dos variables convergiendo por extremos aparecen en decenas de problemas.")]),
],
# ═══════════════════ 36. ARQUITECTURA (4) ═══════════════════
"Arquitectura de Software — Diseñar para Crecer": [
 ("1. Principios universales: SOLID abreviado útil", """DISEÑO: LAS REGLAS QUE SEPARAN AL SENIOR
━━━━━━━━━━━━━━━━━━━━━━━━━━━
KISS — Keep It Simple: la solución simple gana siempre primero; overengineering = bugs duplicados de infraestructura mental.
DRY — Don't Repeat Yourself: el conocimiento vive UNA vez (función/clase); copiar-pegar = bugs replicados por todos lados.
YAGNI — You Aren't Gonna Need It: no construyas lo que quizás nunca necesites; construye cuando lo piden.
SEPARACIÓN DE RESPONSABILIDADES (el corazón): cada módulo/clase/función hace UNA cosa bien.

SOLID EN 1 FRASE CADA UNO
• S (Single Responsibility): una clase = una razón para cambiar
• O (Open/Closed): abierto a extensión, cerrado a modificación (comportamiento nuevo por código NUEVO, no tocando el viejo probado)
• L (Liskov): subclases sustituyen a sus padres sin romper nada
• I (Interface Segregation): interfaces pequeñas > interfaces gordas forzadas
• D (Dependency Inversion): depender de ABSTRACCIONES (interfaces), no de implementaciones concretas

SINTOMAS DE ARQUITECTURA ENFERMA (smells): función de 200 líneas · clase que hace de todo · import cíclicos · cambiar una cosa rompe otras cinco · tests imposibles → refactoriza.""",
  [("¿Qué propone DRY?", ["Borrar código", "El conocimiento/lógica vive UNA sola vez en el sistema; repetición = inconsistencias cuando cambies un lugar y no otro", "Más tests", "Más carpetas"], 1, "Copiar es rápido hoy; mantener copias divergentes es lento mañana."),
   ("Dependency Inversion en práctica significa...", ["No depender de nada", "Tu lógica depende de INTERFACES/contratos; la implementación concreta se inyecta y puede cambiar (prod↔test)", "Java nada más", "Inyectar SQL"], 1, "La pieza clave de testabilidad y arquitectura limpia: invierte quién controla las dependencias.")]),
 ("2. Patrones famosos en 5 minutos: Factory, Observer, Strategy, Singleton", """DECISIONES CLÁSICAS QUE CARGAN DE VIDA
━━━━━━━━━━━━━━━━━━━━━━━━━━━
FACTORY — crear objetos complejos sin新建 en el código
  def crear_tarea(tipo, datos):
      return {"urgente": TareaUrgente, "normal": Tarea}.get(tipo, Tarea)(datos["titulo"])
  # tu código pide 'una tarea urgente' y la fábrica decide cómo ensamblarla

OBSERVER — avisa a interesados sin conocerlos (eventos)
  1) Eventos que publicas / 2) Suscriptores que reaccionan
  Caso real: compra.confirmada → {email.welcome, stock.descontar, log.registrar} = acoplamiento cero

STRATEGY — algoritmo intercambiable sin ifs gigantes
  def procesar_pago(monto, estrategia): return estrategia.pagar(monto)
  class PagoT/CD/ EffectivePaypal = cambiar por inyección

SINGLETON — UNA instancia global compartida (usar con cuidado: es 'global disfrazado')
  Casos válidos: config/app logger/conexión BD por app — y preferible DI sobre singleton clásico.
DECORATOR — agregar comportamiento envolviendo sin heredar (@cache, @login_required del mundo Python)

Cuándoi REGLA: ¡patrón solo cuando el problema ya LO TIENES! (yagni aplicado a patrones)""",
  [("¿Qué resuelve Observer?", ["Visualización", "Acoplamiento: el emisor publica eventos y los interesados reaccionan sin conocerse entre sí", "Bases de datos", "Threads"], 1, "Desacopla módulos: agregar email-notification NO toca el módulo de compras."),
   ("¿Cuál antídoto a un if/elif gigante por tipo?", ["más ifs", "Strategy/Polymorphism: cada caso es su propia clase/objeto elegida de un registro y llamada uniformemente", "comentarios", "más RAM"], 1, "Eliminas el switch monster; añadir un tipo nuevo es código NUEVO, no romper el viejo.")]),
 ("3. Microservicios vs monolito: decisión de adultos", """DÓNDE VIVEN LAS APPS SERIAS
━━━━━━━━━━━━━━━━━━━━━━━━━━━
MONOLITO BIEN ESTRUCTURADO (modular monolith): un solo despliegue, llamadas internas baratas, debug fácil.
 Microservicios (múltiples apps hablando por red/API) benefician a EQUIPOS GRANDES/Idependencia de escala/prod deploy.

LA VERDAD HONESTA 2026: la mayoría de startups DEBERÍAN empezar con un monolito modular (ex: Django monolito = Instagram soportó bulto millones de usuarios).

CUÁNDO MICROSERVICIOS TIENEN SENTIDO
• equipos que necesitan desplegar sin pisarse (independencia de equipos primera razón sincera)
• escalado diferenciado: el checkout necesita x100 el email-worker
• fallos aislados: un servicio caído no tumba los demás
COSTOS MICROSERVICIOS SINCEROS: red (latencia), distributed transactions, logs entre servicios, despliegue complejo, observabilidad...

REGLA: empieza monolito MODULAR (módulos con límites claros internos); si creces, extrae módulos calientes a servicios uno a uno. Netflix fue directo a micro porque era el tamaño y el equipo, no por definición."Repítelo": microservicios no son un estado objetivo; son una resposta orgániica a la escала.""",
  [("¿Cuál es la mayor ventaja real del monolito modular para una startup?", ["Hype", "Velocidad: un despliegue, llamadas internas sin red, debug y refactors baratos mientras el equipo es pequeño", "La nube", "GraphQL"], 1, "El tiempo al mercado es el recurso: el monlito bien diseñado desperdicia menos meses iniciales."),
   ("¿Cuál costo fijo traen los microservicios que no existe en un monolito?", ["Ninguno", "Distribución: red entre servicios, transacciones complejas, logs distribuidos, deployment/orquestación", "CPU", "SQL"], 1, "Cada petición que antes era una llamada local pasa a ser una operación de red que puede fallar.")]),
 ("4. Del diagrama en servilleta a tu propia arquitectura", """ARQUITECTAR TU PROYECTO REAL (plática de servilleta a repo)
━━━━━━━━━━━━━━━━━━━━━━━━━━━
EJEMPLO REAL: "App de tareas con recordatorios por email"
PENSAMIENTO POR CAPAS/MÓDULOS (independiente del framework)
1. 🧠 DOMINIO (lógica pura testable): Tarea, Regla("si pasan 24h → vence"), sin importar web
2. 📂 APLICACIÓN (casos de uso): CrearTarea, RecordarVencidas — orquesta dominio+infra
3. 🔌 INFRAESTRUCTURA: repositorio SQLite, servidor web, adaptador email (SMTP/sendgrid)
4. 🌐 ENTREGA: API REST / UI web — llama casos de uso

REGLA DE DEPENDENCIA UNIVERSAL: capas externas dependen de las internas, NUNCA al revés (tu Tarea no sabe de HTTP ni SQL) → lo interno es testeable puro.

  src/
    dominio/tareas.py       (clases puras, sin web ni db)
    aplicacion/casos.py     (usos: CrearTarea, Recordar)
    infra/datos.py          (SQLite), infra/email.py (enviar mail)
    web/api.py              (endpoints que llaman casos)

Prueba mental: ¿puedo testear recordatorio sin servidor? sí ✅ → Buena arquitectura detectada.
Empieza a poner tu código en estas capas en tu próximo proyecto: es la misma arquitectura que en los monolitos sanos Hoy""",
  [("¿Qué ley cumple una buena separación en capas?", ["Código corto", "Las capas INTERNAS (dominio) no conocen las EXTERNAS (web/DB): lo externo se acopla HACIA el negocio, jamás al revés", "Más archivos = mejor", "ORM"], 1, "Invertir la dirección de dependencia = tu lógica de negocio es testeable pura y viva en cualquier envoltorio."),
   ("Un 'caso de uso' (application service) es...", ["Un SQL", "La orquestación de un objetivo de negocio: 'CrearTarea' coordina el dominio con la infraestructura", "Un template", "CSS"], 1, "Las APIs públicas internas de tu app: lo que el mundo puede hacer con tu sistema.")]),
],
# ═══════════════════ 37. APIS HTTP (4) ═══════════════════
"APIs REST y HTTP — El Idioma de los Servidores": [
 ("1. HTTP: el protocolo que habla el mundo", """HTTP: LA LENGUA FRANCA DE INTERNET
━━━━━━━━━━━━━━━━━━━━━━━━━━━
REQUEST (tu pedido)
  GET /api/tareas/42 HTTP/1.1
  Host: miapp.com
  Authorization: Bearer eyJ...

RESPONSE (su respuesta)
  HTTP/1.1 200 OK
  Content-Type: application/json
  {"id": 42, "titulo": "Aprender HTTP"}

MÉTODOS (verbos, el QUÉ quieres hacer)
  GET    leer (no cambia nada, idempotente y cacheable)
  POST   crear (o acción compleja) NO idempotente: dos veces = dos efectos
  PUT    reemplazar completo · PATCH modificar parcial · DELETE borrar
STATUS (códigos que DEBES conocer de memoria)
  2xx ok: 200 ok · 201 creado · 204 borrado sin contenido
  3xx: 301 movido permanentemente · 304 no cambió (caché)
  4xx TU culpa: 400 malformado · 401 no autenticado · 403 autenticado pero prohibido
         · 404 no existe · 409 conflicto · 422 validación · 429 rate limit excedido
  5xx MI culpa (servidor): 500 error genérico · 503 caído temporalmente

HEADERS vitals: Content-Type · Accept · Authorization · Cookie · User-Agent · Cache-Control""",
  [("¿Cuál es la diferencia entre 401 y 403?", ["Ninguna", "401 = falta autenticación (quién eres); 403 = ya sé quién eres pero NO tienes permiso", "404", "500 famila"], 1, "Autenticación vs autorización: la confusión más común en APIs."),
   ("¿Qué significa que GET sea idempotente?", ["Es lento", "Repetirlo N veces tiene el mismo efecto que 1: exige NO cambiar estado por definición REST", "Es seguro contra hackers", "Es corto"], 1, "GET/PUT/DELETE= idempotentes; POST no: eso decide reintentos seguros en tu cliente.")]),
 ("2. Diseñar tu API: recursos, URLs y convenciones", """DISEÑO REST QUE LOS DEMÁS ENTIENDEN AL INSTANTE
━━━━━━━━━━━━━━━━━━━━━━━━━━━
LOS RECURSOS VIVEN EN LOS NOMBRES DE LAS URLs (sustantivos PLURALES, no verbos)
  GET    /api/tareas          lista (paginada con ?pagina=2&limite=20)
  POST   /api/tareas          crear (201 + body del creado)
  GET    /api/tareas/42       detalle de una
  PATCH  /api/tareas/42       modificar campos
  DELETE /api/tareas/42       borrar (204 sin body)

ERRORES CON FORMATEADO ÚNICO (los consumidores lo agradecen)
  400 → {"error": {"codigo": "VALIDACION", "mensaje": "titulo es requerido", "campo": "titulo"}}
  Simetric: el cliente parsea un formato y listo para siempre.

FILTROS/BÚSQUEDA/ORDEN con query params:
  /api/tareas?estado=pendiente&orden=-creado&busqueda=curso
PAGINACIÓN: ?pagina=2&limite=20 con next/prev en la respuesta (links o metadata count).

VERSIONADO: /api/v1/tareas (v2 rompe cuando la v1 mantienes viva para legacy: no rompes a tus consumidores).
DOCUMENTACIÓN: OpenAPI/Swagger auto-generada (FastAPI lo trae y regs gratis /docs interactivos)""",
  [("¿Cómo es una buena URL de API?", ["/api/crearTarea", "/api/tareas (sustantivo plural; la ACCIÓN va en el método HTTP, no en la URL)", "/api/tareas.php", "con verbo"], 1, "Recursos=sustantivos; acciones=GET/POST/PATCH/DELETE: esa es la legibilidad REST."),
   ("¿Por qué responder 201 con el recurso creado en el POST?", ["Es largo", "El cliente recibe inmediato el objeto recién creado CON su id asignado; sin nueva llamada gratuita", "Hype", "Caché"], 1, "El status informa lo ocurrido + la respuesta entrega el valor resultante.")]),
 ("3. FastAPI: APIs con Python + TypeScript feel", """FASTAPI: LA MÁQUINA DE APIs MODERNAS
━━━━━━━━━━━━━━━━━━━━━━━━━━━
Ventajas: tipado nativo, validación Pydantic automática, docs Swagger gratuitos, async nativo y¡veloz!.

  from fastapi import FastAPI, HTTPException
  from pydantic import BaseModel

  app = FastAPI()

  class TareaIn(BaseModel):              # ESQUEMA = validación automática de tus datos
      titulo: str
      hecha: bool = False

  tareas = []

  @app.get("/api/tareas")
  def listar():
      return {"tareas": tareas, "total": len(tareas)}

  @app.post("/api/tareas", status_code=201)
  def crear(tarea: TareaIn):              # FastAPI valida: si falta titulo → 422 automático
      nueva = {**tarea.dict(), "id": len(tareas) + 1}
      tareas.append(nueva)
      return nueva

  @app.get("/api/tareas/{id}")
  def una(id: int):
      if not 1 <= id <= len(tareas): raise HTTPException(404, "no existe")
      return tareas[id - 1]

  uvicorn main:app --reload           → http://localhost:8000/api/tareas
                                     → http://localhost:8000/docs  🎉 SWAGGER interactivo GRATIS

🎓 /docs + /redoc con tus endpoints, esquemas y botón "Try it out" sin escribir nada: por eso es el favorito.""",
  [("¿Qué hace BaseModel de pydantic?", ["Nada", "Esquema+validación automática de tus request bodies: si el usuario envía mal, 422 sin escribir código tú", "Only types", "SQL"], 1, "TareaIn(titulo: str) garantiza str: errores de formato rechazados de fábrica (esa es la magia atrás de FastAPI)."),
   ("¿Qué dos cosas vienen GRATIS con FastAPI y ningún otro backend básico?", ["Nada", "Swagger interactivo en /docs (probar la API desde el navegador) + validación automática", "Base de datos", "Frontend"], 1, "Auto-docs + auto-valid: tu API se explica y se respeta sola.")]),
 ("4. Proyecto: API REST completa+cliente que la consume", """CONSTRUYE: API + CLIENTE (LA PAREJA REAL)
━━━━━━━━━━━━━━━━━━━━━━━━━━━
1. BACKEND: FastAPI (o tu framework del curso) con el CRUD completo de "recetas":
   recetas = [ ]  lista de {'id', 'titulo', 'ingredientes': lista, 'tiempo_min'}
   GET todos · GET /{id} · POST (validate: titulo requerido, min 3 chars) · PATCH · DELETE.
2. VALIDACIÓN Pydantic real: titulo: str; ingredientes: list[str]; tiempo_min: int = Field(gt=0).
3. MIDDLEWARE: logueo request method+path+time_ms (¡consola de verdad!)
4. CLIENTE (script separado):
     import httpx
     r = httpx.get("http://localhost:8000/api/recetas")
     for receta in r.json(): print(receta["id"], receta["titulo"])
     nueva = httpx.post(url, json={"titulo": "Tacos", ...}).json()
5. PRUEBA ACID TEST: cierras el servidor → corre el cliente → ¿EXCEPCIÓN? tu código NO está listo si no maneja errores de red (try/except + mensaje lindo).
6. ENTREGA: tu API corriendo en /docs abierta en el navegador en la captura del proyecto: el cliente consola mostrando datos vivos.

CONEXIÓN FRONTEND luego: esa MISMA api puede leerla el React/JS de tu proyecto anterior con fetch — MISMAS RECETAS EN WEB VIVA.""",
  [("¿Por qué testear el cliente CON EL API APAGADA?", ["Por castigo", "El mundo real: redes caen siempre; tu cliente debe manejar errores de conexión con gracia, no un traceback", "Sin motivo", "Por bucles"], 1, "Resiliencia honesta: probar el camino triste es parte del camino profesional."),
   ("¿Qué hace especial al acceso a /docs de FastAPI?", ["Nada especial", " Swagger generado automáticamente de tus tipos: probar tu API en vivo desde el navegador, documentación incluida", "Caché", "SQL"], 1, "Value real: es tu documentacíon VIVA sin ninguna pieza extra de código your part.")]),
],
# ═══════════════════ 38. PRODUCTIVIDAD (4) ═══════════════════
"Ecosistema del Dev — Trabajar Inteligente Todos los Días": [
 ("1. Ambiente de trabajo feliz: dotfiles, alias y costumbres", """TU MÁQUINA ACEITADA: 1 HORA SETUP, MESES DE PRODUCTIVIDAD
━━━━━━━━━━━━━━━━━━━━━━━━━━━
ALIAS BASH/ZSH (pon en ~/.bashrc o ~/.zshrc: los TUYOS valen oro)
  alias gs="git status"
  alias ga="git add -A"
  alias gc="git commit -m"
  alias ll="ls -lah"
  alias ..="cd .."; alias ...="cd ../.."

VARIABLES Y PATH: edita tu PATH sin miedo; tu shell config es tan código como tu proyecto (versiona tus dotfiles en GitHub: dotfiles repo = mejora + reproducible).

EDITOR/TMUX/shortcuts: 5 mins diarios a atajos nuevos pagan miles de horas después. Aprende: Ctrl+A/E (inicio/fin línea), Ctrl+U/K (borrar), Ctrl+R (histórico).

AUTOCORRECCIÓN FÍSICA: teclado/silla/monitor altura correcta: programar 40 años es maratón física; dolor de muñeca/espal es la lesión profesional.

CODE STANDARDS GRATIS: Prettier + ESLint (JS) · Black/Ruff (Python) · gofmt incluido → formato automático al guardar = CERO debates de estilo, reviews de lógica real.

TODO.txt o issues mínimas para tu yo del lunes; README por proyecto = tu futuro en tu propio arribol.""",
  [("¿Para qué versionar tus dotfiles en GitHub?", ["Nada", "Tu entorno personal reproducible en cualquier máquina nueva en minutos", "Para más stars", "Para backups"], 1, "~/.bashrc, config de editor, alias...: tu setup como código = ambiente portátil + aprendizaje abierto."),
   ("¿Qué problema resuelven Prettier/Black/gofmt automáticos?", ["Poca RAM", "Eliminan discusiones de estilo: el estilo lo decide el configurador, tu equipo discute lógica", "Tests", "No sirven"], 1, "El estándar a formato compartido elimina debates bikeshedding para reviews de fondo real.")]),
 ("2. Markdown + documentación que La gente lee", """DOCUMENTAR = PENSALO DOS VECES (TU CARRERA LO NOTARÁ)
━━━━━━━━━━━━━━━━━━━━━━━━━━━
MARKDOWN EN LO ESENCIAL (cubrir READMEs y notas)
  # H1 · ## H2
  **negrita** · *cursiva* · `código inline`
  ```python
  bloque_código_con_color    (¡el lenguaje tras las comillas = resaltado!)
  ```
  - lista · 1. numerada
  [texto](https://enlace) · ![alt](img.png) · > cita · --- separador

README QUE FUNCIONA (los 8 bloques mágicos)
  1. Nombre + 1 línea qué hace   2. Screenshot/demo
  3. Características (bullets)   4. Instalación en 3 comandos
  5. Uso con ejemplo de código   6. Tech stack
  7. Roadmap/estado              8. Licencia + autor
Público: tu README se lee en 40 segundos — diseñelo para el que entra con la vista en cortocircuito y cero contexto.

DOCS DE CÓDIGO: comenta el "POR QUÉ", no el "QUÉ" (el código ya dice el qué).
  # Haemos sleep porque la API cierra conexiones a los 30s
  time.sleep(30)
⚠ Comentarios que repiten el código envejecen mal y MIENTEN; la clave es actualizar o eliminar.""",
  [("¿Qué debe comentar un buen comentario en código?", ["Todo el código", "El POR QUÉ/contexto no obvio del código (el QUÉ lo dice el código mismo)", "El autor", "Fechas"], 1, "Razones, advertencias y decisiones: lo que futuras lecturas no pueden inferir."),
   ("¿Cuál es la estructura de un README que convierte?", ["Legal", "Qué hace + demo + install 3 pasos + ejemplo de uso (el lector decide en <1 minuto)", "Solo título", "Sin imágenes"], 1, "La claridad al abrir = usuarios/contribuidores que se quedan.")]),
 ("3. Atajos, flows y profundidad: libro de Deep Work dev", """PROFUNDIDAD: LA MONEDA ESCASA DE NUESTRA ERA
━━━━━━━━━━━━━━━━━━━━━━━━━━━
LA POMODORO EN PRÁCTICA PARA DEVS
1. Elige UNA sola tarea micro-definida ("test para loginService", no "trabajo en backend")
2. 🍅 25 min SIN interrupciones (chat muteado, pestañas cerradas sin-abuso). La app ayuda (sidebar ▶)?
3. Pequeña pausa real 5 min (camina, mira lejos) — tiene ciencia de la atención detrás
4. 4 pomodoros = pausa larga

ZONA DE FLUJO: el point en el que el trabajo más exigente se siente divertido. Para llegar:
• Tarea con clear feedback inmediato · dificultad al límite de tus habilidades · sin distracciones · objetivo cristalino

GESTIÓN DE CONTEXTO DEV: cambiar entre 3 proyectos = pagar cambio de contexto mental ÷ cada cambio cuesta ~15-23 min de re-preparación. Bloques temáticos: mañana=perfeccionamiento nuevo, tarde=bugs/email.

CIENCIA DEL CONOCIMIENTO QUE SE PEGA: enseñar (Feynman) — si no puedes explicar la línea a alguien, no la dominas.
Bitácora/QMD diario: "hoy encontré X → Y lo resolvió" = tu base de conocimiento personal que iniciales use en entrevistas.""",
  [("¿Qué cuestionan los cambios de contexto constantes?", ["Poco tiempo", "Cada switch cobra ~15-23 minutos de re-preparación mental: multitarea = multi-bajo-rendimiento", "RAM", "CI"], 1, "Enfoque profundo > velocidad aparente: los bloques temáticos recuperan esos minutos día a día."),
   ("La técnica Feynman consiste en...", ["Leer mucho", "EXPLICAR el tema a alguien (o a tu patito de goma): lo que no puedes explicar simple, no lo entendiste aún", "Repetir", "Audio"], 1, "Enseñar/grabar = la forma más efectiva de detectar tus propios agujeros de comprensión.")]),
 ("4. IA + automatización: trabaja menos chatos tú", """POTENCIA: AUTOMATIZAR + IA SIN PERDER TU JUICIO
━━━━━━━━━━━━━━━━━━━━━━━━━━━
AUTOMATIZACIÓN PERSONAL (las 3 horas que te ahorra cada semana)
• Scripts bash/python para tareas repetidas: backups, renames batch, JSON→CSV, limpieza de fotos...
• Aliases/bash funcs para tus tareas repetitivas del día
• Crontab para lo que sea horario (backups, reports a tu mail)
• GitHub actions/hooks para automatizar tu repo (format autocommit? CI)

IA COMO PERFIL PROFESIONAL REAL (los que trabajan más rápido lo usan así)
• Rubber ducky avanzado: pega tu código+error → te pide preguntas Socráticas que te guían SIN darte la respuesta (aprendes)
• Revisor de código antes del PR: "crítica mi diff como un senior: bugs, nombres, estandares"
• Generador de boilerplate/administrativo: docstrings, tests básicos, README estructura: TU revisas siempre
• Aprendizaje personalizado: "hazme 5 preguntas progresivas sobre Docker" — tu maestra particular 24/7

REGLA DE HIERRO 2026: la IA genera, tú ENTÍENDS, VALIDAS y ADOPTAS LA RESPONSABILIDAD. Tu valor futuro ≈ entender + desplegar + evaluar como no-ingeniero la salida de la IA.""",
  [("¿Qué perfil de dev gana con la IA actual?", ["Qué se encomienda a ella", "El que entiende y puede AUDITAR la salida: la IA amplifica expertise, no la sustituye", "El que copia rápido", "Solo seniors Cloud"], 1, "Amplificador, no sustituto: más rápido vuelas cuando TÚ eres el criterio final."),
   ("¿Cuál es el uso sano de la IA en aprendizaje?", ["Dame todo el código", "Uso Socrático: pedirle que te haga preguntas/guías y verificar tú cada afirmación", "Ninguna", "Exámenes"], 1, "La IA que te pregunta y tú razonas responde = la IA que aprende en vez de atrofiar.")]),
],
# ═══════════════════ 39. ENTREVISTAS (4) ═══════════════════
"Entrevistas Técnicas — Demostrar lo que Sabes": [
 ("1. Tipos de entrevistas y preparación estratégica", """EL JUEGO DE LAS ENTREVISTAS DEV
━━━━━━━━━━━━━━━━━━━━━━━━━━━
LOS 4 FORMATOS GRANDES
1. 💻 LIVECODING/TAKE-HOME: problema de código en vivo o en casa, puntuación sobre: CORRECTITUD → estilo → insights > llegar al final perfecto
2. 🧠 BEHAVIORAL: "cuéntame una vez que..." (aprendiste algo difícil/resolviste un conflicto/fallaste)
3. 🏗 DESIGN: "diseña un sistema de X" (junior: pequeño y concreto; senior: escala grande)
4. 📋 SCREENING TÉCNICO: charla intro con reclutador o dev sobre tu experiencia

LA CLAVE SINCERA: practicar EN VOZ ALTA pensando tus pasos es EL hábito — los entrevistadores evalúan PROCESO antes que resultado final.

3 RECETAS DE ESTRUCTURA
• Livecoding: CLARIFICAR primero (preguntas sobre inputs/rangos) → planear simple → implementar → testear → hablar todo el rato
• Behavioral (método STAR): Situación → Tarea → Acción (TU parte específica) → Resultado CON NÚMEROS (reduje 40%, verdad concreta)
• Design: ambiente de requisitos → estimaciones back-of-envelope → diagrama a grandes bloques → trade-offs sincero's

PORTAFOLIO COMO EVIDENCIA: 3 proyectos REALES con README + deploy + código limpio valen más que perfeccionismo. Cuéntalos en la entrevista con STAR.""",
  [("¿Qué evalúa PREPONDERANTEMENTE un livecoding bien dirigido?", ["Velocidad", "El PROCESO: clarificar, planificar, razonar en voz alta, testear — antes que código perfecto al final", "Teoría", "El CV"], 1, "La comunicación del razonamiento ES la skill testeada: hablar pensando todo el tiempo."),
   ("¿En qué fallan la mayoría las respuestas behavioral?", ["No saben", "Hablan ddel 'equipo'/vago sin acción propia estructurada ni resultado medible (sin STAR, sin números)", "Mentir", "Código"], 1, "Cuenta TU acción específica con un resultado cuantificado: el resto es ruido.")]),
 ("2. Problemas clásicos de código y cómo abordarlos", """PATRONES QUE CUBREN EL 70% DE ENTREVISTAS
━━━━━━━━━━━━━━━━━━━━━━━━━━━
FORMATO PARA CADA PROBLEMA (adapta uno y practías en voz alta)
  1. Repite el problema y CLARIFICA: ¿pueden ser negativos? ¿vacío? ¿unicidad?
  2. Di solución BRUTA primero ("la fuerza bruta sería O(n²): recorrer todos") ← muestra razonamiento
  3. Mejora con patrón conocido → implementa leyendo bien → testéalo con ejemplos tuyos
  4. Analiza complejidad y posibles bordes/extensión

LOS 6 PATRONES DE ORO
• TWO POINTERS: dos índices convergiendo → invertir, palíndromos, pares en ordenados
• HASH/SET: lookup O(1) → two sum, duplicates, anagramas
• SLIDING WINDOW: subcadena máxima continua → O(n) donde parecía O(n²)
• STACK: balancear paréntesis, next greater element, historial LIFO
• BFS/DFS: grafos y árboles en niveles (bfs) o caminos (dfs)
• ORDEN/GREEDY: ordenar + decisión local óptima → intervalos, reunión de llamadas

PRÁCTICA: LeetCode Easy con los 6 patrones: 5 por semana con tu patrón claro. Luego mediums.
FREECODE/Exercism NeetCode para estructura: aprender los patos, no memoriza respuestas."`""",
  [("¿Por qué decir PRIMERO la solución fuerza bruta agrea valor?", ["No lo hace", "Muestra que razonas el espacio del problema y luego optimizas: evalúan proceso, no memoria", "Más lento", "Para tests"], 1, "Demuestras técnica desde lo simple→optimizado: el entrevistador ve tu mente."),
   ("¿Qué es sliding window?", ["Nada", "Patrón O(n) que mantiene una ventana de elementos entre dos índices sin recorrer repetidamente para sumas/max de subcadena continuables',", "Un hash", "Un stack"], 1, "Substrings continuas: expansión/contracción de dos punteros sin bucles anidados.")]),
 ("3. Comunicar código por escrito: PR, take-homes y tu voice técnica", """CÓDIGO QUE TE HABLA A TI MISMO CUANDO EL ENTREVISTADOR LEE
━━━━━━━━━━━━━━━━━━━━━━━━━━━
TAKE-HOME QUE DESTACA (a menudo lo que más pesa para junior)
  1. README claro: qué, cómo correrlo (comandos exactos), decisiones tomadas (3 bullets)
  2. Código limpio y pequeño: funciones de 20 líneas, nombres que se leen como frases, cero código comentado
  3. TESTS: al menos 3-5 reales (y pasan con pytest/jest) → demuestras método
  4. COMMITS limpios con mensajes significativos (el historial ES revisado)
  5. Roadmap honesto de TODO (qué falta y por qué no lo construiste: madurez profesional)

CODE REVIEW CULTURAL (se evalúa EN las entrevistas sinceras)
  Comenta al código, no al autor: "Esta función podría simplificarse haciendo X" no "esto está mal".
  Aprende a pedir: declarar la intención, 2-3 preguntas antes de criticar.

TU NARRATIVA PERSONAL (let it prepared): ¿por qué programación? ¿qué construiste + qué aprendiste?
  90 segundos que ensayaste en espejo, sin acelerar: conecta tu trasfondo a POR QUÉ eres una inversión buena.
STAR PORTAFOLIO: 3 proyectos con sus 3 frases: reto → solución → por qué te importa.""",
  [("¿Qué elemento de un take-home pesa más que la funcionalidad extra perfecta?", ["Ninguno", "README que explica decisiones + tests reales que pasan +commits limpios: evidencia de profesionalismo", "Server propio", "Colores"], 1, "Lo entregas CÓMO lo entregas: el README y el proceso dicen el 70%."),
   ("¿Por qué los mensajes de commit importan en evaluación?", ["No importan", "El historial del repo es leído como evidencia de cómo piensas y trabajas", "Solo en GOOG", "Por orden"], 1, "'cambios x' suena a junior; 'fix: race condition on login retries' suena a colega que quiero.")]),
 ("4. Proyecto: entrevistae simulada completa", """PREPARACIÓN FINAL: SIMULACRO REAL
━━━━━━━━━━━━━━━━━━━━━━━━━━━
1. THE TAKE-HOME QUIZ (la hora verdadera):
   Crea repo "entrevista-practica".
   Elige UNO: validador de sudoku básico · URL shortener local demo · API de gastos.
   Escribe 40 min PREPARANDO: README first, luego código, luego 4 tests.
   Revisión propia: nombres legibles, funciones < 30 líneas, cero comentarios rancios, todo suite verde.
2. LIVECODING SIMULADO: abre LeetCode/Exercism fácil (FizzBuzz o reverse string o palindrome):
   1 pomodoro, hablas EN VOZ ALTA todo el tiempo mientras codificas, sin mirar respuestas: mételo encárcela si callas mucho.
3. BEHAVIORAL POR ESCRITO: 4 STAR en tu QMD personal (las 'historias' que contarás):
   • un bug difícil de resolver (STAR + qué aprendiste)
   • un conflicto/desacuerdo en equipo (casa/amigos también vale)
   • un fallo propio y cómo lo corregiste → humildad con resultado
   • una vez que superaste expectativas (con número)
4. GRABACIÓN: grábate 5 minutos respondiendo '¿preséntate y por qué quieres trabajar con nosotros?' → escúchate (duele) → mejora claridad y energy.

PANEL DE VERDAD: si completaste 🔴/🟢/writing/mirror en un día real, entrás preparado/a aunque te coman los nervios: los nervios + prep gana talent solo.""",
  [("¿Qué mejora más la entrevista: leer respuestas o simulacros grabados?", ["Leer más", "Simulacro GRABADO: escucharte te enseña claridad verbal y nervios, cosas que no se leen", "Más libros", "Nada"], 1, "El cringe de escucharte una vez supera 10 horas de prep teórico: vivido > leído."),
   ("¿Por qué escribir 4 STAR previo a la entrevista cuenta más que improvisar?", ["No cuenta", "Porque historias vagas ('ehh pues una vez...') matan el impacto que una historia concreta numérica genera en 60 seg", "Código", "Solo senior"], 1, "Estructura STAR + ejemplos ensayados = respuestas profesionales, claras, confiables.")]),
],
# ═══════════════════ 40. REGEX (4) ═══════════════════
"Expresiones Regulares — El Lenguaje de Patrones": [
 ("1. Regex en una lección: el 80% útil sin dolor", """REGEX: PATRONES PARA TEXTOS (DIFÍCIL DE LEER, FÁCIL DE APRENDER)
━━━━━━━━━━━━━━━━━━━━━━━━━━━
ESENCIA (en todos los regex modernos):
  .        cualquier carácter (excepto newline)
  \\d       un dígito (0-9) · \\w letra/número/_ · \\s espacio (y mayúsculas = negación: \\D etc.)
  [...]    clase: [aeiou] una de esas · [0-9] · [^abc] no esas · \\b límite de palabra
  ^        inicio · $ fin · | alternativa · ( ) grupo

CUANTIFICADORES
  *        0 o más · + 1 o más · ? 0 o 1 (opcional)
  {n}      exactas n · {n,} al menos n · {n,m} entre n y m

EJEMPLOS EN PYTHON (se leen igual en JS/sed/grep)
  import re
  re.findall(r"\\d+", "ventas: 3 a 120 y 45")           → ['3', '120', '45']
  re.search(r"\\w+@\\w+\\.\\w+", "mi correo es ada@test.com")  → encuentra el email
  re.sub(r"\\s+", " ", "texto   con    muchos   espacios")     → normaliza

NOTA CRUCIAL: en Python usa r"..." (raw string: el backslash no se come).
ONLINE para probar: regex101.com (¡EXPLICA tu regex en vivo!): la forma de aprender de verdad.""",
  [("¿Qué captura \\d{4}-\\d{2}-\\d{2}?", ["Cualquier cosa", "Formato fecha aproximado: 4 dígitos-guión-2 dígitos-guión-2 dígitos (2026-09-18)", "Emails", "Estampillas"], 1, "Las regex describen patrón → los números reales solo ilustran el formato esperado."),
   ("¿Qué hacen \\b y () en regex?", ["Trivia", "\\b enmarca palabra completa ('cat' en 'concatenar' NO matchea con \\bcat\\b); () crea un GRUPO capturable", "Solo negación", "Comentarios"], 1, "Límites y grupos: de patrones sueltos a coincidencias quirúrjicas.")]),
 ("2. Capturar grupos y.los casos reales: validación y extracción", """CAPTURAR SUSTANCIAS (LO QUE BUSCAS EXTRAER)
━━━━━━━━━━━━━━━━━━━━━━━━━━━
GRUPOS CON NOMBRES (legibilidad máxima)
  patron = re.compile(r"(?P<usuario>[\\w.]+)@(?P<dominio>[\\w.]+\\.\\w+)")
  m = patron.search("mi email es ada@example.com")
  m.group("usuario")   → "ada"   ·   m.group("dominio") → "example.com"

CASOS DE TRABAJO REAL (los que pedirás toda la vida)
1. VALIDAR FORMATO (no quiere decir verdad del email solo forma):
   r"^[\\w.-]+@[\\w-]+\\.[\\w.]+$"               → email razonable
   r"^\\+?\\d{1,4}[\\s.-]?\\(?\\d{2,4}\\)?[\\s\\d.-]{7,}$"  → teléfono laxo
   r"^(?=.*[A-Z])(?=.*\\d).{8,}$"              → contraseña con lookahead (mayúscula+número, 8+)
2. EXTRAER: fechas en logs, ids de URLs (r"/users/(\\d+)"), precios (r"\\$\\s?([\\d,]+)"),
   IPs (\\d{1,3}\\.\\d{1,3}\\.\\d{1,3}\\.\\d{1,3})
3. REEMPLAZAR con grupos: re.sub(r"(\\d+)/(\\d+)/(\\d+)", r"\\3-\\2-\\1", fecha)

SCRIPT REAL DIARIO: re.sub sobre un CSV/log gigante te sustituye horas de find-and-replace manual.""",
  [("¿Qué hace (?P<nombre>...) en Python regex?", ["Nada especial", "Grupo NOMBRADO: extraes por m.group('nombre') en vez de factores posición brittle", "Ordena", "Exporta"], 1, "Regex autocomentados: los nombres documentan cada parte que capturas."),
   ("¿Qué logra el lookahead (?=.*[A-Z]) en la contraseña?", ["Neutro", "VERIFICA sin consumir: exige que exista una mayúscula en lo que sigue sin avanzar el cursor", "Ordena letras", "Es bug"], 1, "Lookaheads = 'debe cumplirse X adelante': validaciones compuestas sin complicar los grupos.")]),
 ("3. Los 5 errores clásicos de regex (no sufras estos)", """ASÍ SE ROMPE EL REGEX EN PRODUCCIÓN — TUS SALVADOS AQUÍ
━━━━━━━━━━━━━━━━━━━━━━━━━━━
1. ¡GREEDY (codicioso)! .* captura TODO lo que puede.
     r"<.*>" sobre "<b>a</b><i>b</i>" matchea DESDE <b> HASTA </i> entero 💀
     Fix: lazy → <.*?> (el ? lo hace contraccible: captura lo mínimo posible)
2. sin FLAGS accesorios:
     re.IGNORECASE (r"python" matcha "PYTHON") · re.MULTILINE (^$ por línea) · re.DOTALL (. incluye newline)
3. Escapado olvidado: el PUNTO literal es \\. (sino matchea cualquier char: "2x5" matchearia "2.5" con r"2.5" errado)
   Regla: cuan desperas literales como . ? + * ( ) [ ] { } | \\ → anteponer \
4. Invalid formats en raw strings (Python): escribe r"\\d+" y no "\\\\d+" → SyntaxWarning in 3.12+
5. Catastrophic backtracking: ((a+)+$) con texto malo = tu CPU al 100% una hora (¡ataque Regex DoS real!)
   Fix: evitar anidamiento innecesario de cuantificadores + probar con strings adversos en regex101

REGLA SABÍA: si tu texto tiene estructura fija conocida (JSON, HTML, dataclasses)... mejor parsea con la librería apropiada, no regex.""",
  [("¿Qué arregla .*? frente a .*?", ["Nada", "? lo vuelve LAZY/no-greedy: captura el MÍNIMO posible en vez de todo lo posible", "Más rápido", "Al revés"], 1, "La diferencia entre 'primer cierre que encuentras' y 'último del documento': regex es codiciosa por defecto y se come todo."),
   ("¿Cuándo NO usarías regex?", ["Siempre ideal", "Para estructuras complejas anidadas como HTML/JSON reales: usa parseadores diseñados, regex se rompe en los bordes", "Para logs", "Para emails"], 1, "Zawinski: 'ahora tienes dos problemas'. Texto libre ↔ regex; formato estructurado ↔ parser real.")]),
 ("4. Proyecto: analizador de logs con regex (uso real)", """CONSTRUYE: TU ANALIZADOR DE LOGS REAL
━━━━━━━━━━━━━━━━━━━━━━━━━━━
MISIÓN (90 min): te dieron 10.000 líneas de log de un servidor:
  2026-09-18 13:42:15 ERROR usuario=ana metodo=POST ruta=/api/login ip=187.55.20.10 ms=234

TAREAS
1. PARSEAR CADA LÍNEA a dictado de campos:
   patron = re.compile(
       r"(?P<fecha>\\d{4}-\\d{2}-\\d{2}) (?P<hora>\\d{2}:\\d{2}:\\d{2}) (?P<nivel>\\w+) "
       r"usuario=(?P<usuario>\\w+) metodo=(?P<metodo>\\w+) ruta=(?P<ruta>\\S+) "
       r"ip=(?P<ip>[\\d.]+) ms=(?P<ms>\\d+)"
   )
   datos = [patron.match(linea).groupdict() for linea in log.splitlines() if patron.match(linea)]
2. MÉTRICAS: errores por usuario · p95 de ms · rutas más llamadas (Counter(rutas)) · IPs únicas
3. FILTRAR/EXPORTAR solo las líneas ERROR a un CSV
4. BONUS: valida formato email de una columna en un CSV de clientes
5. REPORTE: un pequeño "log-analisis.md" con 3 hallazgos cuantificados

ESTE SCRIPT es literalmente una herramienta de trabajo real en analistas/SREs: tu primer herramienta 'power-user' construída.
OJO: regex101.com para° probar el patrón sobre 5 líneas muestra antes de correr las 10.000.""",
  [("¿Qué hace groupdict() sobre un Match?", ["CSV", "Devuelve un dictando con grupos NOMBRADOS para cada campo: linea→estructura lista para pandas/procesar", "Error", "Orden"], 1, "La puente: texto crudo → registro estructurado con nombres del grupo = pipeline real."),
   ("¿Por qué probar tu regex en regex101 con muestras primero?", ["Es cool", "Detectas backtracking/capturas raras/escapes al instante antes de correr sobre miliones de líneas y romper produción", "Por nada", "Static"], 1, "Iteras el patrón en segundos con explicación en vivo; es la herramienta existente.")]),
],
# ═══════════════════ 41. PORTAFOLIO/CARRERA (5) ═══════════════════
"Carrera Dev — De Estudiar a Trabajar": [
 ("1. El portafolio que te consigue entrevistas", """PORTAFOLIO QUE FUNCIONA (REALIDAD HONESTA)
━━━━━━━━━━━━━━━━━━━━━━━━━━━
Un buen portafolio de JUNIOR tiene 3-4 proyectos REALES con README+deploy+código — no 10 a medias, no todo teórico.

LOS 3 NIVELES DE PROYECTOS
• Nivel 1 (aplicación aprendida): tu app de tareas/notas/documentadas (+1 si tiene tu twist personal)
• Nivel 2 (utilidad real por alguien): automatiza algo a tu mamá/trabajo actual/vecino/amigo
  👑 El proyecto que resuelve un problema REAL ajeno vale 10 tutoriales ("fue usado por familia/mi oficina")
• Nivel 3 (contribuye al mundo): un PR de open source o una librería chiquita o una herramienta CLI
  (¡un primer PR — aunque sea arreglar typo en docs — demuestra trabajo con código real y comunidad)

REPOSITORIO DISCIPLINA: cada proyecto = README (qué/demo/stack) + código limpio + screenshots + link a DEMO deployado.
GITHUB VERDE: commits regulares (incluso pequeños) cuentan consistencia real de aprendizaje.

CV/LinkedIn: bullets con VERBOS DE ACCIÓN + NÚMEROS: "Construí app de tareas con React+SQLite; usada por 5 usuarios semanales; tests 90% cobertura" — no "aprendí mucho".""",
  [("¿Qué proyecto de portafolio vale más para un junior?", ["El más grande", "El que un HUMANO real utiliza/usa (aunque sea para tu familia/trabajo actual): evidencia de valor real creado", "El de más líneas", "El copiado"], 1, "Problemas reales > tutoriales; un usuario real vale más que mil vistas de código sino utilidad."),
   ("¿Qué se mira en la presencia GitHub de un junior?", ["Avatar", "Ritmo de commits reales (consistencia) + calidad README en proyectos destacados", "Solo estrellas", "Nada"], 1, "El gráfico verde con commits de tu aprendizaje historia disciplina: lo mejor del perfil junior sincere.")]),
 ("2. Contributing a open source: tu CV universal", """TU PRIMER PR OPEN SOURCE (MÁS FÁCIL DE LO QUE CREES)
━━━━━━━━━━━━━━━━━━━━━━━━━━━
EL FLUJO PRÁCTICO (una tarde de fin de semana)
1. Encuentra proyectos acogedores: labels 'good first issue' en GitHub (docs/libraries que usas)
2. Lee CONTRIBUTING.md (estilo, ramas, tests) — la escuela del código real del proyecto
3. Fork + clone + rama fix/issue-NR-descripcion
4. Cambio chiquito pero bien hecho (corregir typo, mejorar ejemplo, test que falta)
5. PR con descripción corta: qué cambias y por qué + issue referenciado ("Fixes #1234")
6. Espera revisión con MOOD de alumno: ajusta, aprende, no tomes personal (los revisores cuidan el proyecto)

POR QUÉ ES ORO PARA TU CARRERA
• Demuestra leer código ajeno (la habilidad diaria de un dev)
• Trabajar en relacion con comunidad global
• Línea en tu CV con el nombre del proyecto (instantáneo reconocimiento si es conocido)
• Portfolio VIVO (tu contribución queda pública para siempre)

AVISO: empieza pequeño (docs/tests); código de producto llega después de entender elescos""",
  [("¿Qué representa la etiqueta 'good first issue'?", ["Spam", "Issues adecuados para primeriza contribución: acogida/simplificada por los mantenedores para nuevos", "El bug del día", "Pago"], 1, "La puerta de entrada pro a open source: empieza por docs/docs/tests de proyectos que uses."),
   ("¿Por qué un PR open source vale más que un proyecto privado extra?", ["El más popular", "Evidencia pública e verificable de: colaboración, lectura de código, responsabilidad con QA externa", "Decorativo", "SVG"], 1, "La credibilidad inmediata que genera un 'contribuidor en X-proyecto' en un CV junior es descomunal.")]),
 ("3. Networking y networking real: el 70% de los empleos", """EL TRABAJO DE CONSEGUIR TRABAJO (LA PARTE INVISIBLE)
━━━━━━━━━━━━━━━━━━━━━━━━━━━
VERDAD DEL MERCADO: hay mucho empleo de dev junior bien pagado y se cubre por REFERIDOS y reputación pública más que por aplicaciones frías.

NETWORKING QUE NO ESLIFE (práctico y sin pasar vergüenza)
1. COMUNIDAD PÚBLICA: servidores Discord/slack de tu stack (Python, React... local o emoji: hace tu pregunta, aporta también)
2. TU PÚBLICA PÚBLICA: posts curtos en LinkedIn/dev.to con lo que APRENDISTE semanalmente (Los reclutadores lean sus feeds y ven crecimiento)
3. EVENTOS: meetups locales (a menudo gratuitos), conferencias baratas/online — 30 minutos presentándano + projects = más que marchar de 10 aplicaciones
4. Outreach sincero: "Hola <nombre>, vi tu charla sobre X, estoy aprendiendo Y; ¿una pregunta 10 min?" (respuesta asombrosa del 30-50% de gente normal)

SOLICITUDES QUE CIERRAN: personalizadas, demostrastes que miraste la empresa (esto y allá/tech-stack citado), proyecto vinculado a su dominio + "acá está mi trabajo funcionando écolélink".

EL MINDSET: NO eres 'mendigu trabajo': pones tu crecimiento en público y dejas que el valor hable y las oportunidades vengan. Consistencia pública+interacción humana = los bastones del empleo.""",
  [("¿Qué es lo más efectivo para un junior buscando su primer empleo?", ["Aplicaciones masivas", "Networking real (comunidades, meetups, reputación publica) + solicitudes personalizadas mostrando trabajo real", "Ocultar portfolios", "Nada"], 1, "Los referidos/reputación deciden multitud de posiciones: consérvalo como una skill más del trabajo."),
   ("¿Qué hace publicar semanalmente tu aprendizaje en tu red?", ["Hablar solo", "Reputación publica: reclutadores ven constancia y crecimiento; los posts te PRE-VENDEN antes de la entrevista", "Nada útil", "Spam"], 1, "Documentar tu camino = marketing legitimo de la mejor versión de ti como dev emergente.")]),
 ("4. Negociación y tu primer trabajo: lo que nadie dice", """PRIMER TRABAJO: QUÉ ESPERAR Y CÓMO CRECER
━━━━━━━━━━━━━━━━━━━━━━━━━━━
TU META EN EL PRIMER EMPLEO: no es el salario máximo, es APRENDER MÁXIMO velocidad de crecimiento (mentoría, código real, feedback). Pregunta en tu entrevista: "¿cómo dan mentoría a juniors?"

AL MOMENTO DE LA OFERTA
• No la aceptes en la llamada: pide 24-48h por escrito (tiempo: decidiste en tu casa, no bajo presión)
• Investiga RANGOS de mercado (Glassdoor/encuestas locales/comunidad) → rango contado sinceramente
• Primera oferta ~aprendizaje: acepta si cumple aprendizaje+condiciones; la presión salarial vale desde el segundo salto
• Pregunta simple y poderosa: "¿hay flexibilidad en el rango?" (una vez, amable, sin justificación nerviosa)

TUS PRIMEROS 90 DÍAS (el manual práctico)
1. Semana 1: entiende cómo corre el proyecto local y PIDES ayuda rápido (tu 15 min de investigación + duda clara = imagen pro)
2. Mes 1: arregla bugs medianos y aprende el flujo PR/code review
3. Mes 2-3: tu primera feature completa + aprendes las herramientas de producción (deploy/logs/incidents)

APRENDIZAJE PARA SIEMPRE: cada día escribe en tu bitácora: 1 cosa aprendida (esquirla) — en 3 meses tienes contenido para subir posición tu próxima entrega/review.""",
  [("¿Qué debe importarte MÁS en tu primer trabajo?", ["El salario inmediato", "La velocidad de APRENDIZAJE: mentoría, feedback, código real. El salario despega tras el primer salto", "El gaming", "El título"], 1, "Tus primeros 1-2 años son capital de aprendizaje; cobras después, una vez has crecido."),
   ("¿Qué señal da pedir ayuda rápio con una buena estructura?", ["Debilidad", "Profesionalismo: investiaste 15-20 min, intentaste solo, y haces una pregunta concreta que respeta el tiempo del otro", "Inmadurez", "Nada"], 1, "Saber preguntar bien es una skill reputacional en todo equipo sano.")]),
 ("5. Proyecto final: tu paquete completo de empleabilidad", """TU CHECKOUT COMPACTO PARA EL MUNDO LABORAL
━━━━━━━━━━━━━━━━━━━━━━━━━━━
PROYECTO META (7 días, 1-2 pomodoros/día — tu propio 'shipping' personal):
1. 🐱 GITHUB PERFIL LIMP₄₀: pinned 3 proyectos con READMEs hermosos y link de demo a cada uno. Bio de 2 líneas.
2. 📝 CV REAL: 1 página donde cada bullet tiene verbo+número; quita relleno ("responsable", "dinámico") por hechos
   (Ej: "Construí app web con login JWT y base SQLite; 90% código Python/Django; mención especial por claquería en code reviews")
3. 🗨 ELEVADOR: párrafo de presentación de 90 segundos ensayado: quién eres → qué construiste → por qué te interesa la posición
4. 🏗 PORTAFOLIO WEB (gratis, estático): 1 página ultra-clara con 3 tarjetas de tus proyectos + links GitHub/demos + información de contacto real
5. 👥 PRESENCIA MINMO ACTIVA: 1 post/documentando tu aprendizaje esta semana en LinkedIn/dev.to (escribe sobre lo que acabas de aprender en este curso, benefits dobles: procesas + publicas)
6. 🎯 SOLICITUD EJEMPLO: escribe 1 carta personalizada de muestra a una empresa real, demostrando que miraste su producto y cómo tu perfil aplica a LO QUE ELLOS NECESITAN

EVALUACIÓN FINAL del curso: subes el repositorio del portafolio a tu GitHub público y compartes link con un amigo/reclutador potencial.
Si llegas aquí ejecutado todo este plan y este florilegio, ya superaste el 95% de juniors promedio que solo 'estudia'. Tú SHIPPEAS.""",
  [("¿Qué hace los pinned repos en el perfil de GitHub?", ["Nada", "Decides qué 3 proyectos destacan primero al entrar un reclutador (tu escaparate elegido según ti, no según fecha)", "Más PR", "Orden"], 1, "Tu escaparate manual: evita que el reclutador vea primero tus experimentos viejos en vez de tus mejores proyectos."),
   ("¿Por qué el portafolio web de 1 PÁGINA es mejor que el sitio complejo?", ["Es gratis", "Un reclutador con 40 segundos decide rápido: claridad + links tangibles de tus best proyectos superan complejidad innecesaria", "Menos sec", "Móvil"], 1, "El lector con cero contexto elige: claridad = entrevistas; complejidad = scroll y abandono.")]),
],
}
