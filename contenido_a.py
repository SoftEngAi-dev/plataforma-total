# -*- coding: utf-8 -*-
"""Contenido A — Fundamentos y Web Core. Parte 1/3 del contenido (9 cursos, 86 lecciones).
Formato: (titulo, contenido, [(pregunta, [4 opciones], indice_correcta, explicacion), ×2])"""

CURSOS_MOD = {
# ═══════════════════ 1. RUTA MAESTRA (6) ═══════════════════
"Ruta Maestra — Cómo Usar Esta Plataforma": [
 ("1. El mapa completo: 41 cursos, un objetivo", """BIENVENIDO A TU ESCUELA LOCAL
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Esto es Plataforma Total: una escuela de programación completa que vive en TU máquina.
Sin internet, sin cuentas, sin suscripciones. Solo tú, contenido curado y una IA local opcional.

🎯 EL OBJETIVO
Convertirte en desarrollador/a capaz de construir software real, a tu ritmo.

🗺 EL MAPA (orden sugerido)
1. Ruta Maestra (estás aquí)     → cómo estudiar
2. Herramientas del Desarrollador → tu kit básico
3. HTML/CSS + JavaScript          → la web por dentro
4. Python o el lenguaje que elijas
5. Git, Linux, Docker             → trabajar como pro
6. Un framework (React, etc.)     → construir en serio
7. Portafolio, entrevistas        → conseguir trabajo

📌 REGLA N.º 1
La consistencia diaria vence a los maratones dominicales: 25 minutos todos los días (un 🍅) transforman más que 8 horas una vez al mes.""",
  [("¿Cuál es la regla n.º 1 de la plataforma?", ["Estudiar 8 horas los fines de semana", "Consistencia diaria: 25 minutos al día mínimo", "Terminar un curso por semana", "Aprenderse la documentación de memoria"], 1, "La racha diaria (🔥) es la palanca que hace funcionar todo lo demás."),
   ("¿Qué necesita Plataforma Total para funcionar?", ["Internet permanente", "Una cuenta de usuario", "Nada más que tu máquina — es 100% local", "Una GPU potente"], 2, "Todo el contenido y la base de datos viven en tu máquina; la IA externa es 100% opcional.")]),
 ("2. Cómo estudiar una lección (método comprobado)", """EL PROTOCOLO DE 25 MINUTOS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1. 🍅 Inicia un Pomodoro (panel lateral ▶)
2. 📖 Lee la lección COMPLETA una vez, sin ejecutar nada
3. 🧠 Ciérrala y di en voz alta lo que recuerdas (explica en voz alta)
4. 🛠 Abre el editor y reproduce el ejemplo sin mirar
5. ✅ Marca la lección como completada
6. 📝 Haz el quiz. Si no es 100%, repasa y reintenta

POR QUÉ FUNCIONA
• Recordar activamente (paso 3) graba 2-3× más que releer
• Escribir el código tú mismo (paso 4) es donde ocurre el aprendizaje real
• El quiz detecta huecos que la lectura disimula

⛔ TRAMPA CLÁSICA: ver el código y pensar "ya lo entendí". Entender ≠ saber. Solo sabes lo que puedes reproducir.""",
  [("¿Qué es la recordación activa?", ["Releer la lección varias veces", "Cerrar el material e intentar recordar/explicar sin mirar", "Subrayar con marcador", "Copiar el contenido a mano"], 1, "Recuperar de memoria (aunque cueste) es el ejercicio que más graba en el cerebro."),
   ("Al terminar una lección, ¿cuál es la señal de dominio?", ["Haberla leído con calma", "Entender el ejemplo al verlo", "Quiz aprobado al 100% 🏆", "Marcarla como completada"], 2, "El quiz al 100% es la evidencia; el resto son intenciones.")]),
 ("3. Tus herramientas: progreso, racha y certificados", """EL SISTEMA DE PROGRESO
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
• ✅ Lección completada — se guarda en SQLite para siempre
• 📝 Quiz por lección — tu mejor puntaje se recuerda
• 🏆 Quiz al 100% — marca de maestría, meta de cada lección
• 🔥 Racha — días seguidos con actividad (lección, quiz o pomodoro)
• 🍅 Pomodoros — contador diario de bloques de enfoque
• 🎓 Certificado — se desbloquea con TODAS las lecciones + TODOS los quizzes al 100% de un curso

DÓNDE VIVEN TUS DATOS
~/PlataformaTotal/datos/plataforma.db — es tuyo. Respáldalo si quieres.

EL JUEGO LARGO
Los certificados 🎓 se regulan solos: no puedes hacer trampa porque el requisito es dominio real (100% en todo). Cuando digas "terminé React", lo demostrarás con el certificado y sus quizzes 🏆.""",
  [("¿Qué desbloquea el certificado de un curso?", ["Leer todas las lecciones", "Todas las lecciones + todos los quizzes al 100%", "Pagar la capstone", "Hacer 50 pomodoros"], 1, "Lecciones ✅ + quizzes 🏆 en cada lección del curso."),
   ("¿Dónde se guarda tu progreso?", ["En la nube", "En el navegador", "En SQLite local: ~/PlataformaTotal/datos/plataforma.db", "No se guarda"], 2, "Todo tu progreso es local y tuyo — portable y respaldable.")]),
 ("4. Aprender construyendo: proyectos desde el día 1", """PROYECTOS: DONDE OCURRE LA MAGIA
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Las lecciones te dan vocabulario. Los proyectos te dan JUICIO.

LA FÓRMULA
1 lección nueva + experimentar 10 min = aprendizaje
1 proyecto pequeño terminado = conocimiento que se queda

TIPOS DE PROYECTO (escala)
• Mini (30-60 min): una idea, un archivo, hoy mismo
• Semana: algo con 2-3 conceptos juntos (Python + archivos + JSON)
• Mes: una app que enseñes con orgullo (incluye README)

CÓMO NO FRACASAR EN PROYECTOS
1. Escópalo TAN pequeño que no pueda fallar (¿"app de tareas"? empieza: "guardar UNA tarea en un archivo")
2. Termina antes de mejorar: versión fea funcionando > bonita sin funcionar
3. README siempre — explicar tu código es la mitad del aprendizaje

🚀 La pestaña Proyectos te crea esqueletos listos para arrancar.""",
  [("¿Cuál es el error más común al empezar un proyecto?", ["Usar un lenguaje nuevo", "Ámbito demasiado grande desde el inicio", "Escribir un README", "Terminar antes de mejorar"], 1, "Haz el ámbito tan pequeño que no pueda fallar; luego creces."),
   ("¿Por qué escribir un README en cada proyecto?", ["Para que GitHub lo muestre bonito", "Porque explicar tu código consolida el aprendizaje y es evidencia de tu trabajo", "Es requisito del sistema", "Para ganar puntos"], 1, "Documentar = enseñar = consolidar. Y tu portafolio lo agradece.")]),
 ("5. IA como copiloto (no como piloto)", """USAR LA IA SIN ATROFIARTE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
La IA es un multiplicador: multiplica por 10 lo que ya entiendes y por 0 lo que no.

✅ BUENOS USOS (te hacen mejor)
• "Explícame este error y su causa raíz"
• "¿Por qué funciona X y no Y?" (entender, no copiar)
• "Dame 3 iteraciones de mejora de MI código"
• "Hazme preguntas de entrevista sobre este tema"
• Quiz con IA sobre lecciones ya estudiadas

⛔ MALOS USOS (te mantienen atascado)
• Ver un error → pegarlo a la IA → copiar la solución sin leer
• Generar el proyecto entero y no entenderlo
• Usar IA en tu primera pasada de cada lección

LOS 10 MINUTOS DE ORO
Antes de pedir ayuda a la IA: 10 minutos tú solo intentando. La frustración productiva es el gimnasio del cerebro; la IA no levanta las pesas por ti.""",
  [("¿Cuál es un uso saludable de la IA al aprender?", ["Generar el proyecto completo", "Copiar soluciones sin leerlas", "Pedir que te haga preguntas y explique causas raíz", "Usarla en tu primera pasada por cada lección"], 2, "La IA que te pregunta y explica causas te educa; la que solo responde te sustituye."),
   ("¿Qué son los '10 minutos de oro'?", ["Aspecto premium de la app", "Intentar resolver solo 10 min antes de pedir ayuda", "Descanso de 10 minutos", "Leer 10 minutos antes de codificar"], 1, "La lucha productiva es donde se construye la capacidad de resolver.")]),
 ("6. Tu primer día (empieza en 25 minutos)", """DÍA 1 — PROTOCOLO DE ARRANQUE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
⏱ 0-2 min: 🍅 Inicia un pomodoro (panel lateral)
📖 2-12 min: ve a Herramientas del Desarrollador, lección 1 — sigue el protocolo de 25 min
🛠 12-20 min: reproduce el ejemplo de la lección con tus manos
✅ 20-22 min: marca completada, haz el 📝 quiz
🧭 22-25 min: mira tu Inicio: ya tienes racha 🔥 = 1

MAÑANA (día 2)
1 lección más. Solo una. La racha vale más que la velocidad.

SEÑALES DE QUE VAS BIEN
• Vuelves a abrir la app sin que nadie te empuje
• A veces el pomodoro se te queda corto (zona dorada: flujo)
• Empiezas a explicar lo aprendido a alguien más

🎯 RECORDATORIO FINAL
Esto no es una carrera. 243 lecciones a 1/día ≈ 8 meses transformadores. El de hoy ya lo tienes entre manos — empieza ahora.""",
  [("¿Cuánto debe durar tu primera sesión?", ["2-3 horas para arrancar bien", "Un pomodoro de 25 minutos", "Lo que aguantes", "15 minutos"], 1, "Pequeño y terminado > grande y abandonado. El pomodoro enmarca la victoria del día."),
   ("¿Qué es más importante la primera semana?", ["Terminar un curso", "Construir la racha diaria 🔥", "Instalar todo lo posible", "Leer mucha teoría"], 1, "El hábito precede al conocimiento: sin racha, el plan muere; con racha, es inevitable.")]),
],
# ═══════════════════ 2. HERRAMIENTAS (6) ═══════════════════
"Herramientas del Desarrollador": [
 ("1. El editor de código: tu casa de trabajo", """EL EDITOR: ACÁ VIVIRÁS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Opciones reales 2026:
• VS Code — estándar de facto. Extensions, todo el mundo lo usa
• Zed / Sublime / Neon — rápidos y modernos
• Vim/Neovim/Helix — si quieres la vida en el teclado (fase avanzada)
• VSCodium — VS Code sin telemetría

MÍNIMO QUE DEBES DOMINAR
• Abrir carpeta completa (no archivos sueltos): el proyecto es la unidad
• Ctrl+P → saltar a cualquier archivo por nombre
• Ctrl+Mayús+F → buscar en todo el proyecto
• Ctrl+` → terminal integrada
• Split editor: ver dos archivos a la vez

EXTENSIONES CLAVE (VS Code)
• Python/Pylance si vas a Python
• Prettier (formato automático)
• GitLens (quién escribió qué línea)
• Error Lens (errores en línea, en vez de escondidos)

Regla: el editor se aprende con el uso, no leyendo manuales. Acostúmbrate a UNA cosa nueva por semana.""",
  [("¿Qué hace Ctrl+P en VS Code?", ["Imprimir", "Abrir cualquier archivo del proyecto escribiendo parte de su nombre", "Formatear el documento", "Abrir la terminal"], 1, "Quick Open: navegación veloz por archivos — la uso cientos de veces al día."),
   ("¿Cuál es la ética del proyecto en el editor?", ["Abrir archivo por archivo desde el explorador", "Abrir el explorador de internet", "Abrir la CARPETA del proyecto completa", "Un editor por archivo"], 2, "El proyecto es la unidad: la búsqueda global, la terminal y la IA contextual dependen de ello.")]),
 ("2. La terminal: miedo fuera", """LA LÍNEA DE COMANDOS SIN DRAMA
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
La terminal asusta porque parece "de hackers". Solo es hablar con el SO por texto en vez de clics — y es MÁS rápido.

SUPERVIVENCIA (Linux/Mac; en Windows usa Git Bash o WSL)
  pwd             → dónde estoy
  ls              (dir) → qué hay aquí
  cd carpeta      → entrar;  cd .. → subir
  mkdir nombre    → crear carpeta
  touch archivo   (New-Item) → crear archivo vacío
  cp a b          → copiar;   mv a b → mover/renombrar
  rm archivo      → borrar (¡sin papelera!)
  cat archivo     → ver contenido
  Ctrl+C          → cancelar lo que sea
  Ctrl+R          → buscar en tu historial

AUTOCOMPLETAR = TAB. Siempre. Escribes `cd Pro+<TAB>` y lo completa.

⚠ rm -rf borra TODO sin preguntar: piénsala dos veces. Esta app te enseña — un rm mal puesto borró un workspace entero de verdad (historia real).""",
  [("¿Qué comando muestra en qué carpeta estás?", ["ls", "cd", "pwd", "where"], 2, "pwd (print working directory)."),
   ("¿Qué hace la tecla TAB en la terminal?", ["Inserta un tabulador", "Autocompleta rutas, archivos y comandos", "Borra la línea", "Cambia de ventana"], 1, "TAB es tu superpoder: menos typos, más velocidad.")]),
 ("3. Instalar y gestionar paquetes (todo por terminal)", """GESTORES DE PAQUETES: LA TIENDA DE TU STACK
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Cada lenguaje tiene el suyo:
• Python → pip    : pip install requests
• Node   → npm    : npm install express
• Sistema(Ubuntu) → apt    : sudo apt install git
• Mac    → brew   : brew install python

PYENV/VIRTUALENV — ¿aislamiento?
pip instala global por defecto y los proyectos chocan entre sí. Solución: un virtualenv por proyecto:
  python3 -m venv .venv
  source .venv/bin/activate    # Windows: .venv\\Scripts\\activate
  pip install requests
  pip freeze > requirements.txt

El requirements.txt registra tus dependencias → cualquiera puede reproducir tu proyecto:
  pip install -r requirements.txt

Esta app mismo tiene el suyo: es así de universal.""",
  [("¿Para qué sirve un virtualenv en Python?", ["Acelerar el código", "Aislar las dependencias de cada proyecto para que no choquen", "Compilar Python más rápido", "Ejecutar código remoto"], 1, "Cada proyecto tiene su propio set de paquetes/versions; nunca chocan."),
   ("¿Qué hace `pip install -r requirements.txt`?", ["Crea el archivo de dependencias", "Instala todas las dependencias registradas del proyecto", "Actualiza pip", "Desinstala paquetes"], 1, "La forma estándar de reproducir el entorno de un proyecto en cualquier máquina.")]),
 ("4. Git: la memoria eterna de tu código (básico)", """GIT EN 10 COMANDOS (flujo mínimo)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Git es la máquina del tiempo de tu proyecto. Puntos clave:  lo guardas TÚ con commits; sin commit no hay historia.

  git init                     → nace el repositorio aquí
  git status                   → qué cambió (lo usarás mil veces)
  git add archivo / git add -A  → preparar cambios
  git commit -m "mensaje"       → guardar punto de restauración
  git log --oneline             → ver historia
  git diff                      → qué cambió exactamente
  git checkout -- archivo       → OOPS, deshacer cambios no commiteados
  git branch nombre             → crear rama
  git switch nombre             → cambiar a rama
  git merge otra_rama           → fusionar

LA BUENA COSTUMBRE: commit pequeño y frecuente, mensaje que diga QUÉ cambiaste ("feat: quiz de python", no "cambios").

Cada commit es un punto de restauración. «No se borra nada, todo se adiciona»: con git es literalmente cierto.""",
  [("¿Qué hace git add antes del commit?", ["Publica en el servidor", "Prepara (stage) los cambios que irán en el próximo commit", "Borra cambios", "Crea una rama"], 1, "Add prepara; commit guarda el punto en la historia."),
   ("¿Cómo debe ser un buen mensaje de commit?", ["Largo y detallado siempre", "Corto y describe QUÉ cambió y por qué", "'asdf'", "Con emojis únicamente"], 1, "Tú futuro (y tu equipo) lo leerán: comunica el cambio.")]),
 ("5. GitHub: publica y colabora", """DE TU MÁQUINA AL MUNDO
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
GitHub = git + colaboración + portafolio público.

SETUP (una vez)
  1. Cuenta en github.com
  2. Configura tu identidad: git config --global user.name "Tu Nombre" / user.email tu@correo
  3. Autenticación: token (https) o llave SSH (recomendada, permanente)

SUBIR UN PROYECTO NUEVO
  1. Crea el repo en github.com (vacío, sin README)
  2. git remote add origin git@github.com:usuario/repo.git
  3. git push -u origin main        ← primera vez
  (luego solo: git push)

CICLO DIARIO DE COLABORACIÓN
  git pull        → traer cambios del equipo
  ...trabajas, commiteas...
  git push        → subir tus cambios

También: Issues = tareas; Pull Request = proponer cambios revisables; Actions = CI/CD gratis (esta app lo usa para compilar ejecutables Win/Mac/Linux automáticamente).

🎓 Tu GitHub verde (contribuciones diarias) es hoy casi un CV por sí solo.""",
  [("¿Qué hace `git push -u origin main`?", ["Descarga el repo", "Sube tus commits y enlaza la rama local con la remota para futuros pushes", "Borra el repo remoto", "Crea el repositorio en GitHub"], 1, "El -u solo hace falta la primera vez; después, `git push` a secas."),
   ("¿Qué es un Pull Request?", ["Un ticket de soporte", "Proponer cambios de una rama para que otros los revisen antes de fusionar", "Un virus", "Una forma de borrar ramas"], 1, "PR = cambio propuesto + revisión + discusión + fusión: la base del trabajo en equipo.")]),
 ("6. Debugging: el arte de encontrar lo que rompiste", """EL DEPURADOR Y LA CIENCIA DE LOS ERRORES
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
El debugging es 50% del trabajo real de un programador. Profesionalízate aquí y te separas del 90%.

NIVEL 1 — print/tutela científica
  print("LLEGUÉ AQUÍ", variable)   → y antes de eso: ¿CUÁL era mi hipótesis?
Método: hipótesis → experimento mínimo → resultado → nueva hipótesis.

NIVEL 2 — leer tracebacks DE ABAJO HACIA ARRIBA
  Traceback (most recent call last):
    File "x", line 10, in main ...   ← la ruta
  ZeroDivisionError: division by zero ← TIPO y MENSAJE: empezar aquí
El último frame tuyo suele ser tu código; el mensaje de error ES la pista.

NIVEL 3 — el debugger de verdad
  breakpoint()  (Python)  /  debugger;  (JS)
Controles: siguiente línea, entrar a función, inspeccionar variables, continuar.

REGLA: reproduce el error de forma CONFIABLE antes de intentar arreglarlo. Si no lo puedes reproducir, no entiendes el bug aún.""",
  [("¿Cómo se lee un traceback?", ["De arriba hacia abajo", "De abajo hacia arriba: tipo de error y mensaje primero", "Ignorando el mensaje", "Solo la primera línea"], 1, "Tipo + mensaje (abajo) te dicen el qué; los frames (arriba) te dicen el dónde."),
   ("¿Qué debe pasar ANTES de intentar arreglar un bug?", ["Borrar el código", "Reproducir el error de forma confiable", "Pedir ayuda en foros", "Reescribir todo"], 1, "Sin reproducción confiable solo estás adivinando.")]),
],
# ═══════════════════ 3. HTML Y CSS (10) ═══════════════════
"HTML y CSS — Diseño Web Total": [
 ("1. HTML: el esqueleto de toda la web", """HTML: ESTRUCTURA, NO DECORACIÓN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
HTML (HyperText Markup Language) define QUÉ ES cada cosa: un título, un párrafo, un botón. La decoración es tarea de CSS.

ANATOMÍA DE UNA ETIQUETA
  <etiqueta atributo="valor">contenido</etiqueta>
  <p class="nota">Hola</p>          ← p es etiqueta, class es atributo

DOCUMENTO MÍNIMO
  <!DOCTYPE html>
  <html lang="es">
    <head><meta charset="utf-8"><title>Mi página</title></head>
    <body><h1>¡Hola mundo web!</h1></body>
  </html>

LAS 12 QUE USARÁS SIEMPRE
h1-h6 (títulos) · p · a href · img src alt · ul/ol/li · div (caja genérica) · span · button · input · form · br · hr

PRÁCTICA: abre tu editor, crea index.html, escribe el documento mínimo, ábrelo con doble clic. Eso ES una web.""",
  [("¿Qué define HTML en una página web?", ["Los colores y tipografías", "La estructura y el significado del contenido", "La lógica interactiva", "La base de datos"], 1, "HTML = estructura/semántica; CSS = presentación; JS = comportamiento."),
   ("¿Para qué sirve <head> en un documento HTML?", ["Mostrar el encabezado visible", "Metadatos: title, charset, enlaces a CSS/JS — no se muestra en la página", "El menú de navegación", "Nada, es opcional"], 1, "Todo lo de <head> configura la página; lo visible vive en <body>.")]),
 ("2. Formularios e inputs: la web habla contigo", """FORMULARIOS: RECOGER DATOS DEL USUARIO
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  <form action="/registro" method="POST">
    <label for="email">Email:</label>
    <input id="email" name="email" type="email" required>
    <input type="password" name="clave" minlength="8">
    <input type="number" name="edad" min="13" max="99">
    <select name="pais"><option value="UY">Uruguay</option></select>
    <textarea name="bio"></textarea>
    <button type="submit">Enviar</button>
  </form>

CLAVES
• name es lo que viaja al servidor (sin name no llega nada)
• label + for/id: accesibilidad Y clic más grande
• type valida gratis: email, number, date, url...
• required/min/max/minlength: validación HTML5 sin código

VALIDACIÓN EN DOS CAPAS
La validación HTML es para UX rápida; el servidor SIEMPRE valida de nuevo (el cliente es falsificable).""",
  [("¿Qué atributo hace que el dato de un input llegue al servidor?", ["id", "class", "name", "type"], 2, "Sin name, el input no viaja con el formulario."),
   ("¿Por qué validar también en el servidor si el HTML ya valida?", ["Porque el HTML5 bugs mucho", "Porque la validación del cliente se puede saltar/falsificar", "No hace falta", "Para SEO"], 1, "Toda entrada del cliente es hostil hasta que el servidor la valida.")]),
 ("3. CSS: selectores, cascada y el modelo de caja", """CSS: CÓMO SE DECIDE QUÉ GANA
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  selector { propiedad: valor; }
  p { color: navy; }            /* todas las <p> */
  .nota { font-size: 20px; }    /* class= (reutilizable) */
  #principal { width: 90%; }    /* id= (único en la página) */
  div p { ... }                 /* p DENTRO de div */
  a:hover { color: red; }       /* estado */

LA CASCADA (quién gana si hay choque)
1. Especificidad: inline > #id > .clase > etiqueta
2. A igual especificidad: gana la última escrita

EL MODELO DE CAJA (¡ESTO ES CSS!)
Todo elemento es una caja:
  contenido → padding (aire INTERNO) → border → margin (aire EXTERNO)
  box-sizing: border-box;   ← ponlo SIEMPRE: width incluye padding y border

  * { box-sizing: border-box; }

PRUEBA: background-color es la linterna del layout — pinta las cajas para ver qué pasa.""",
  [("¿Qué selector tiene más especificidad?", ["etiqueta (p)", "clase (.nota)", "id (#principal)", "universal (*)"], 2, "id gana sobre clase y etiqueta. Inline style gana sobre todos."),
   ("¿Qué hace box-sizing: border-box?", ["Elimina los bordes", "width/height incluyen padding y border (lo intuitivo)", "Añade sombras", "Redondea esquinas"], 1, "Sin él, width:100px + padding te da una caja de más de 100px; con él, es exacto.")]),
 ("4. Flexbox: layout en una dimensión", """FLEXBOX: ALINEAR COSAS FÁCIL
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  .contenedor {
    display: flex;
    justify-content: center;   /* eje principal (horizontal por defecto) */
    align-items: center;       /* eje cruzado (vertical) */
    gap: 12px;                 /* espacio entre hijos */
  }

PROPIEDADES DEL PADRE (flex container)
• justify-content: flex-start | center | space-between | space-around
• align-items: stretch | center | flex-start | flex-end
• flex-direction: row | column        ← invierte los ejes
• flex-wrap: wrap                      ← permite varias líneas

PROPIEDADES DEL HIJO
• flex: 1            → "crece y reparte el espacio sobrante"
• align-self: ...    → excepción individual

LOS 3 CASOS DE LA VIDA REAL
1. Barra de navegación: space-between + align center
2. Centrar algo perfecto (vertical y horizontal): ambas a center
3. Cards uniformes: wrap + flex:1 en cada una

PRÁCTICA: centra un div con flexbox. Hoy. Es EL examen de CSS doméstico.""",
  [("¿Qué línea centra un elemento horizontal y verticalmente dentro de su padre?", ["display:block + margin:0", "display:flex; justify-content:center; align-items:center", "position:center", "float:center"], 1, "Flexbox con ambos ejes centrados — el centramiento perfecto ya no es chiste."),
   ("¿Qué hace flex: 1 en un hijo?", ["Le da 1px", "Lo hace crecer para repartir el espacio sobrante del contenedor", "Lo pone primero", "Lo oculta"], 1, "flex-grow/shrink/basis abreviado: típicamente reparte el espacio equitativamente.")]),
 ("5. CSS Grid: diseño en dos dimensiones", """GRID: EL LAYOUT PROFESIONAL
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Cuando hay filas Y columnas (galerías, dashboards, páginas enteras): Grid.

  .galeria {
    display: grid;
    grid-template-columns: repeat(3, 1fr);   /* 3 columnas iguales */
    gap: 15px;
  }

  /* El clásico responsive sin media queries: */
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));

LAYOUT DE PÁGINA COMPLETA
  .app { display: grid; grid-template-areas:
    "header header"
    "sidebar main"
    "footer footer"; }
  header  { grid-area: header; }

FLEX vs GRID (regla de bolsillo)
• Una fila/columna de cosas → Flexbox (navbar, botones, centrado)
• Retícula de ambas dimensiones → Grid (galerías, páginas)
Conviven: Grid para la página, Flex dentro de cada card.""",
  [("¿Qué hace repeat(auto-fit, minmax(250px, 1fr))?", ["3 columnas fijas", "Columnas dinámicas: entran las quepan con mínimo 250px y rellenan el espacio", "250px de alto", "Nada sin media queries"], 1, "El patrón responsive por excelencia: se adapta solo al ancho disponible."),
   ("¿Cuándo elegir Grid sobre Flexbox?", ["Siempre", "Nunca", "Cuando el diseño es bidimensional (filas y columnas)", "Solo para tablas"], 2, "Flex = una dimensión; Grid = dos. Conviven felices.")]),
 ("6. Responsive design: una web para todos los tamaños", """RESPONSIVE: MOBILE-FIRST
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
El 60% del tráfico web es móvil. Diseña desde la pantalla chica y escala hacia arriba.

LA LÍNEA OBLIGADA (sin ella el móvil muestra miniatura)
  <meta name="viewport" content="width=device-width, initial-scale=1">

MEDIA QUERIES
  /* Base: escrito para móvil (mobile-first) */
  @media (min-width: 768px) {       /* tablet+ */
    .contenedor { display: flex; }
  }
  @media (min-width: 1024px) {      /* desktop */ }

UNIDADES
• px → solo para bordes/detalle fino
• rem → tipografía/espacios (respeta configuración del usuario: accesibilidad)
• % / fr / vw → layout fluido
• max-width: 1100px + margin:auto → columna de lectura cómoda en pantallas gigantes

IMG responsive gratis: img { max-width: 100%; height: auto; }

TEST: herramientas de desarrollo del navegador (F12) → modo dispositivo. Prueba en 360px de ancho primero.""",
  [("¿Qué hace la meta etiqueta viewport?", ["Bloquea el zoom para siempre", "Dice al móvil que use el ancho real del dispositivo y no una miniatura", "Mejora el SEO", "Nada en móviles modernos"], 1, "Sin ella, el móvil renderiza como si fuera un desktop de 980px y escala."),
   ("¿Qué significa mobile-first?", ["Que movil es más importante que desktop", "Escribir el CSS base para móvil y crecer con min-width media queries", "Testear solo en móvil", "Apps nativas primero"], 1, "Base simple en pantalla chica; complejidad progresiva hacia pantallas grandes.")]),
 ("7. Variables CSS y tipografía: sistemas de diseño mínimos", """DISEÑA CON SISTEMA, NO CON ADIVINANZAS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
VARIABLES CSS (custom properties)
  :root {
    --color-principal: #6f42c1;
    --espacio: 8px;
    --radio: 12px;
  }
  .boton { background: var(--color-principal); border-radius: var(--radio); }
Cambiar un valor en :root → rebranding completo en 1 línea.

ESCALA TIPOGRÁFICA (consistencia visual)
  --texto-sm: 0.875rem; --texto-base: 1rem; --texto-lg: 1.25rem; --texto-xl: 1.75rem;
Fundamentos: máximo 2-3 tamaños por página al empezar.

FONT
  font-family: system-ui, sans-serif;   ← fuente nativa del SO: carga 0 ms
  line-height: 1.6;                      ← lectura cómoda
  max-width: 65ch en párrafos;           ← líneas legibles

REGLA DEL DISEÑADOR NO-DISEÑADOR: elige UNA paleta (60-30-10: fondo/dominante/acento) y no improvises colores. El 80% del diseño bonito es consistencia.""",
  [("¿Qué ventaja da definir colores como variables en :root?", ["Cargan más rápido", "Cambias una línea y actualizas toda la web (sistema de diseño)", "Es la única forma válida", "Ahorra memoria del navegador"], 1, "Las variables convierten estilos sueltos en un sistema coherente y mantenible."),
   ("¿Cuál es el largo de línea recomendado para texto legible?", ["Sin límite", "~45-75 caracteres (65ch) por línea", "Exactamente 200px", "El ancho de la pantalla"], 1, "Líneas demasiado largas cansan la vista: limita el ancho del texto.")]),
 ("8. Transiciones y micro-interacciones", """MOVIMIENTO CON SENTIDO
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
TRANSICIONES — la base de todo movimiento suave:
  .tarjeta {
    transition: transform 0.2s ease, box-shadow 0.2s ease;
  }
  .tarjeta:hover {
    transform: translateY(-4px);
    box-shadow: 0 8px 20px rgba(0,0,0,0.15);
  }
Sin transition el cambio es brusco; con ella, se interpola.

ANIMACIONES (keyframes) para ciclos:
  @keyframes pulso { 50% { transform: scale(1.05); } }
  .logo { animation: pulso 2s infinite; }

REGLAS DEL MOVIMIENTO PROFESIONAL
1. Anima SOLO transform y opacity (no width/margin: provocan reflow lento)
2. Duraciones 150-300ms para UI — más lento se siente torpe
3. Movimiento = comunicación (hover, feedback, atención), no decoración
4. Respeta prefers-reduced-motion para accesibilidad:
   @media (prefers-reduced-motion: reduce) { * { animation: none; transition: none; } }""",
  [("¿Qué propiedades se deben animar para rendimiento fluido?", ["width y height", "top y left", "transform y opacity", "margin y padding"], 2, "Solo esas dos no provocan reflow/repaint del layout: la GPU las acelera."),
   ("¿Qué duración se siente natural en micro-interacciones de UI?", ["2-3 segundos", "150-300ms", "Lo máximo posible", "10 segundos"], 1, "Suficiente para percibirse, corto para no frenar.")]),
 ("9. Proyecto guiado: tu página personal completa", """CONSTRUYE: TU PORTAFOLIO V1 (este pomodoro)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Requisitos (todo lo aprendido en el curso):
1. index.html con: header/nav, sección sobre-mí, lista de proyectos, footer
2. style.css con: variables de color, tipografía system-ui, max-width 1100px
3. Nav con flexbox space-between; proyectos como grid auto-fit minmax
4. Hover en links y tarjetas con transition en transform
5. Meta viewport + comprobación en modo móvil (F12)
6. Imágenes con max-width:100%

ESTRUCTURA SUGERIDA
  mi-portafolio/
    index.html
    style.css
    img/ (tu foto, si quieres)

ÉXITO MÍNIMO: se ve bien en móvil Y en desktop. Nosotros no pedimos bonito de concurso; pedimos SÓLIDO y responsivo.

SIGUIENTE NIVEL: súbelo a GitHub; en el curso de Despliegue lo pondrás gratis en internet con GitHub Pages.""",
  [("¿Cuál es el éxito mínimo del proyecto?", ["Que gane un premio de diseño", "Que se vea bien tanto en móvil como en desktop", "Que use 10 fuentes distintas", "Que tenga animaciones complejas"], 1, "Responsive sólido es la meta; el gusto se entrena después."),
   ("¿Qué combinación cubre los layouts del proyecto?", ["Solo floats", "Flexbox para el nav + Grid para las tarjetas", "Tablas HTML", "Solo posición absoluta"], 1, "Flex para 1 dimensión (nav), Grid para 2 (cards): la receta moderna.")]),
 ("10. Accesibilidad básica: la web es para todas las personas", """A11Y: ACCESIBILIDAD (EL 15% DE PERSONAS LO NECESITA)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
No es opción ni caridad: es ingeniería correcta, y mejora la UX de TODOS.

CHECKLIST FUNDAMENTAL
1. HTML semántico: usa <nav>, <main>, <button> reales (no <div onclick>)
2. alt en TODAS las imágenes con información: alt="gráfico de ventas 2025"
3. Contraste: texto vs fondo mínimo 4.5:1 (WebAIM Contrast Checker)
4. Todo operable con teclado (tab, enter) — pruébalo sin ratón
5. Labels en formularios (for/id)
6. lang="es" en <html> — los lectores de pantalla pronuncian bien
7. No comuniques solo con color ("los campos rojos"): icono + texto también

PRUEBA 30 SEGUNDOS: aprieta TAB en tu web. ¿Ves el foco? ¿Tiene sentido el orden?
Nivel pro: Lighthouse (F12) → auditoría de accesibilidad automática.""",
  [("¿Qué elemento es correcto para acción clickeable accesible?", ["<div onclick=...>", "<span onclick=...>", "<button>", "cualquiera"], 2, "<button> trae gratis: foco de teclado, Enter/Espacio, y semántica para lectores de pantalla."),
   ("¿Cuál es el contraste mínimo texto/fondo recomendado?", ["2:1", "3:1", "4.5:1", "10:1"], 2, "WCAG AA: 4.5:1 para texto normal (3:1 para texto grande).")]),
],
# ═══════════════════ 4. JAVASCRIPT (18) ═══════════════════
"JavaScript — De Cero a Experto": [
 ("1. JavaScript: el lenguaje que está en todas partes", """JS: DE NAVEGADOR A TODAS PARTES
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Nació en 10 días en 1995. Hoy corre en: navegadores, servidores (Node), móviles, desktops, satélites.

TU PRIMER CÓDIGO (consola del navegador: F12)
  console.log("Hola JS");          // imprimir
  alert("¡Hola!");                 // popup (solo navegador)

DÓNDE EJECUTAR HOY
• F12 → Consola: experimenta YA
• archivo .js dentro de <script src="app.js"></script>
• Node.js: node app.js (si lo tienes instalado)

COMENTARIOS
  // una línea
  /* varias
     líneas */

JS es de tipado DINÁMICO: las variables cambian de tipo (a veces para mal; TypeScript lo arregla).
  let x = 5; x = "cinco";   // legal (aunque discutible)

ESTÁNDAR ACTUAL: aprende ES6+ (2015+), el JS moderno que enseña este curso.""",
  [("¿Dónde corre JavaScript hoy día?", ["Solo en navegadores", "Solo en servidores", "Navegadores, servidores, móviles, desktops y más", "Solo dentro de HTML"], 2, "Con Node y sus derivados, JS es verdaderamente universal."),
   ("¿Qué imprime en la consola del navegador?", ["print()", "echo()", "console.log()", "System.out.println()"], 2, "console.log es el print de JavaScript — tu aliado n.º 1.")]),
 ("2. Variables: let, const y por qué var quedó atrás", """LET Y CONST (y olvida var por ahora)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  const nombre = "Ada";       // NO se puede reasignar. EL POR DEFECTO.
  let edad = 36;              // reasignable. Cuándo necesitas cambiarla.
  var  vieja = "evítala";     // scope confuso; existe solo en código legado

  edad = 37;                  // ✅ let permite
  nombre = "Otra";            // ❌ TypeError

🚨 const no significa inmutable por dentro:
  const lista = [1, 2, 3];
  lista.push(4);              // ✅ permitido (muta el contenido)
  lista = [];                 // ❌ prohibido (reasignar)

ÁMBITO (scope)
  { let x = 1; }              // x solo vive entre llaves (bloque)
Funciones también crean su propio ámbito.

REGLA PROFESIONAL: const por defecto; let solo si vas a reasignar; var nunca (código nuevo). Hace tu intención legible y previene bugs.""",
  [("¿Cuál es la regla moderna para declarar variables?", ["var siempre", "let siempre", "const por defecto; let solo si reasignas; var nunca", "No declarar, usar globales"], 2, "const comunica 'esto no cambia': menos sorpresas, bugs más difíciles."),
   ("¿Qué pasa con const arr = [1]; arr.push(2)?", ["Error: const es inmutable", "Funciona: const prohíbe reasignar, no mutar el contenido", "Duplica el array", "Lo convierte en string"], 1, "const congela la REFERENCIA, no el objeto: puedes mutar por dentro.")]),
 ("3. Tipos de datos y operadores", """LOS 8 TIPOS QUE IMPORTAN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PRIMITIVOS: string, number, boolean, undefined, null, bigint, symbol
  "hola" · 42 · 3.14 · true · undefined (no asignado) · null (ausencia intencional)
OBJETO (todo lo demás): { }, [ ], funciones...

OPERADORES
  + - * / % **        % = resto (12 % 5 → 2), ** = potencia (2**3 → 8)
  === vs ==  → ESTRICTA compara valor Y tipo (úsala siempre):
    5 === "5"   → false   (tipo distinto)
    5 ==  "5"   → true    (¡convierte! fuente infinita de bugs)
  !==, >, <, >=, <=
  && (y) || (o) ! (no)

DETECCIÓN DE TIPO
  typeof "hola"   → "string"
  typeof undefined → "undefined"

TRAMPA CLÁSICA
  null == undefined  → true ;   null === undefined → false
  NaN === NaN        → false  (usa Number.isNaN(x))""",
  [("¿Por qué usar === y no ==?", ["Es más rápido", "== convierte tipos automáticamente y genera bugs sutiles; === compara valor y tipo", "Por estilo", "== está obsoleto"], 1, '"5" == 5 da true; con === da false. Predicibilidad > comodidad.'),
   ("¿Qué valor representa la ausencia intencional?", ["0", "''", "null", "NaN"], 2, "null = 'vacío a propósito'; undefined = 'aún no se le asignó nada'.")]),
 ("4. Strings: la caja de herramientas del texto", """TEXTO COMO DATO
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  const nombre = "Ada Lovelace";

PLANTILLAS LITERALES (backticks): las usarás siempre
  `Hola ${nombre}, tienes ${2026 - 1815} años.`   // interpolación

MÉTODOS ESENCIALES
  nombre.length             → 12
  nombre.toUpperCase()      → "ADA LOVELACE"
  nombre.toLowerCase()      → "ada lovelace"
  nombre.includes("Love")   → true
  nombre.startsWith("Ad")   → true
  nombre.slice(0, 3)        → "Ada"
  nombre.split(" ")         → ["Ada", "Lovelace"]
  "  sobrante  ".trim()     → "sobrante"
  nombre.replace("Ada", "Grace")  → "Grace Lovelace"

INMUTABILIDAD: los métodos devuelven NUEVO string; el original nunca cambia.
  let s = "hola";  let t = s.toUpperCase();  // s sigue siendo "hola"

Acceso por índice: nombre[0] → "A". Último: nombre[nombre.length-1].""",
  [("¿Qué es una plantilla literal?", ["Un string común", "Backticks con ${} para interpolar variables/expresiones", "Una función", "Un comentario"], 1, "`Hola ${nombre}` — la forma moderna de construir texto dinámico."),
   ('Tras let s="hola"; s.toUpperCase(); ¿qué vale s?', ['"HOLA"', '"hola" — los strings son inmutables', "Error", "undefined"], 1, "toUpperCase devuelve un NUEVO string; s no cambia salvo que lo reasignes.")]),
 ("5. Números, mate y errores clásicos", """NÚMEROS Y SUS TRAMPAS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Un solo tipo number para enteros y decimales (punto flotante de 64 bits).

  const precio = 19.99;
  Math.round(precio)     → 20
  Math.floor(precio)     → 19
  Math.ceil(precio)      → 20
  Math.random()          → decimal [0, 1)
  Math.floor(Math.random() * 6) + 1   → dado de 1 a 6
  Math.max(3, 9, 4)      → 9

FORMATEAR
  precio.toFixed(2)      → "19.99" (string, ojo)

LA TRAMPA DEL FLOTANTE (universal en programación)
  0.1 + 0.2 === 0.3      → false  (!)
  (0.1 + 0.2).toFixed(2) → "0.30"
Dinero real: trabaja en CENTAVOS enteros (1999) y divide al mostrar.

CONVERSIONES
  Number("42") → 42 ·  parseInt("42px") → 42 ·  String(42) → "42"
  Number("hola") → NaN ·  Number.isNaN(x) para comprobar""",
  [("¿Por qué 0.1 + 0.2 !== 0.3 en JS (y casi todo lenguaje)?", ["Bug de JavaScript", "Representación binaria de punto flotante: 0.1 y 0.2 no son exactos en base 2", "La consola miente", "Falta de redondeo"], 1, "Como 1/3 en decimal, algunos decimales son infinitos en binario. Solución: enteros (centavos) o toFixed."),
   ("¿Cómo generar un entero aleatorio entre 1 y 6?", ["Math.random(1,6)", "Math.floor(Math.random() * 6) + 1", "random(6)", "Math.ceil(Math.random()*6)+1"], 1, "random()*6 ∈ [0,6); floor → 0-5; +1 → dado de 1 a 6.")]),
 ("6. Condicionales: if, else y el operador ternario", """DECISIONES
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  if (edad >= 18) {
    acceso = "permitido";
  } else if (edad >= 13) {
    acceso = "con tutor";
  } else {
    acceso = "denegado";
  }

TERNARIO (asignación corta y elegante)
  const mensaje = edad >= 18 ? "mayor" : "menor";
Solo para casos simples; si anidas ternarios, vuelve a if.

SWITCH (varias opciones del mismo valor)
  switch (dia) {
    case "lunes":  actividad(); break;
    case "viernes": fiesta(); break;
    default: descansar();
  }
⚠ Sin break, CASCADA engañosa ("fall-through").

FALSY (valores que if trata como falso): false, 0, "", null, undefined, NaN
  if (nombre) { ... }   // pasa solo si nombre tiene contenido
?? (nullish): valor ?? "por defecto"  → solo captura null/undefined (¡más preciso que ||!).""",
  [("¿Cuáles valores son falsy en JS?", ["Solo false", "false, 0, \"\", null, undefined, NaN", "Solo null y undefined", "Cualquier número"], 1, "if(x) con x falsy no ejecuta el bloque — revisa esta lista cuando te sorprenda."),
   ('¿Qué hace nombre ?? "invitado"?', ['Siempre da "invitado"', 'Usa "invitado" SOLO si nombre es null o undefined (no si es "" o 0)', "Es un error de sintaxis", "Compara nombre con invitado"], 1, "?? es el default preciso: || también rechazaría '' y 0 que podrías querer conservar.")]),
 ("7. Bucles: for, while y recorrer colecciones", """REPETICIÓN CONTROLADA
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
FOR clásico (control total):
  for (let i = 0; i < 5; i++) { console.log(i); }

FOR...OF (elementos de un array, EL RECOMENDADO):
  for (const fruta of ["🍎", "🍌", "🥝"]) { console.log(fruta); }

FOR...IN (claves de un objeto):
  for (const clave in persona) { console.log(clave, persona[clave]); }

WHILE (no sabes cuántas vueltas):
  let n = 100;
  while (n > 1) { n = n / 2; }

DO...WHILE (ejecuta AL MENOS una vez).

CONTROL
  break;      → sale del bucle
  continue;   → salta a la siguiente vuelta

⚠ BUCLE INFINITO: condición que nunca cambia. while(true) + break apropiable; i olvidado en for = clásico.
REGLA: confirma que la condición de salida LLEGARÁ a cumplirse.""",
  [("¿Cuál es la forma moderna recomendada de recorrer un array?", ["for clásico con índice", "for...of", "for...in", "while con contador"], 1, "for...of es directo y seguro; for...in es para CLAVES de objetos, no arrays."),
   ("¿Qué hace continue?", ["Rompe el bucle", "Salta a la siguiente iteración", "Termina la función", "Pausa 1 segundo"], 1, "Omite el resto del bloque en esta vuelta y sigue con la próxima.")]),
 ("8. Funciones y arrow functions: el corazón de JS", """FUNCIONES: HAY 3 SABORES
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1. Declarada (con hoisting: puedes llamarla antes de definirla)
  function sumar(a, b) { return a + b; }

2. Expresada
  const sumar = function(a, b) { return a + b; };

3. ARROW (la moderna, más corta, hereda `this`)
  const sumar = (a, b) => { return a + b; };
  const doble = n => n * 2;                   // 1 parámetro + 1 línea: súper corta
  const saludar = () => "¡Hola!";             // sin parámetros

PARÁMETROS POR DEFECTO Y RESTO
  const precioConIva = (precio, iva = 0.22) => precio * (1 + iva);
  const maximo = (...numeros) => Math.max(...numeros);

RETURN: toda función devuelve undefined salvo que digas return.

REGLA: funciones CORTAS que hacen UNA cosa bien con nombre verbo+qué (calcularTotal, validarEmail).""",
  [("¿Qué devuelve una función sin return?", ["null", "0", "undefined", "Error"], 2, "Sin return explícito, toda función JS devuelve undefined."),
   ("¿Qué diferencia clave tiene una arrow function?", ["Es más lenta", "No tiene su propio this: usa el del contexto que la rodea", "No acepta parámetros", "No puede devolver valores"], 1, "Crucial en callbacks y objetos: la arrow no 'secuestra' el this como hace function.")]),
 ("9. Arrays: la colección reina", """ARRAYS: LISTAS ORDENADAS DE CUALQUIER COSA
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  const numeros = [10, 20, 30];
  numeros[0]         → 10
  numeros.length     → 3

AGREGAR/QUITAR extremos
  numeros.push(40)   → agrega al final
  numeros.pop()      → quita el último
  numeros.shift()    → quita el primero
  numeros.unshift(5) → agrega al inicio

BUSCAR/CORTAR
  numeros.indexOf(20)     → 1
  numeros.includes(99)    → false
  numeros.slice(0, 2)     → [10, 20] (copia, no toca al original)
  numeros.splice(1, 1)    → quita (MUTA al original)

UNIR Y CONVERTIR
  [1,2].join("-")    → "1-2"
  [...a, ...b]       → fusionar arrays con spread
  [...numeros]       → copia superficial

TRAMPA: const a = [1]; const b = a; b.push(2) → a TIENE el 2 (¡misma referencia!). Copia con [...a].""",
  [("¿Qué métodos agregan/quitan AL FINAL de un array?", ["shift/unshift", "push/pop", "slice/splice", "join/split"], 1, "push y pop operan en el extremo final; shift/unshift al inicio."),
   ("const b = a (arrays) — ¿qué relación tienen?", ["Copia total", "Apuntan AL MISMO array: mutar uno muta el otro", "b es de solo lectura", "Ninguna"], 1, "Los arrays son referencias. Copia real: [...a] o a.slice().")]),
 ("10. map, filter, reduce: programar sin bucles", """EL TRÍO FUNCIONAL (ÚSALOS SIEMPRE QUE PUEDAS)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  const nums = [1, 2, 3, 4, 5];

MAP — transformar cada elemento (mismo largo):
  nums.map(n => n * 10)            → [10, 20, 30, 40, 50]

FILTER — quedarse con los que cumplen:
  nums.filter(n => n % 2 === 0)    → [2, 4]

REDUCE — condensar todo a un valor:
  nums.reduce((total, n) => total + n, 0)   → 15
                             ↑ acumulador   ↑ valor inicial

ENCADENAR (lo verás en código real todo el tiempo):
  nums.filter(n => n > 2).map(n => n * 10).reduce((t, n) => t + n, 0)   → 120

FIND y SOME/EVERY (prima-hermanas útiles)
  nums.find(n => n > 3)     → 4 (el primero)
  nums.some(n => n > 4)     → true
  nums.every(n => n > 0)    → true

⚠ Ninguno muta el original. for muta silenciosamente; estos son declarativos y seguros.""",
  [("¿Qué devuelve [2,4,6].filter(n => n > 3)?", ["6", "[4, 6]", "2", "3"], 1, "filter conserva los que cumplen la condición."),
   ("¿Qué hace el segundo argumento de reduce?", ["Nada, decorativo", "Es el valor inicial del acumulador", "Es el límite de iteraciones", "Es una función de fallback"], 1, "Sin valor inicial, reduce usa el primer elemento — que a veces es sorpresa. Escribe siempre el inicial.")]),
 ("11. Objetos: diccionarios con superpoderes", """OBJETOS: CLAVE → VALOR
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  const alumno = {
    nombre: "Ada",
    edad: 36,
    cursos: ["JS", "Python"],
    saludar() { return `Hola, soy ${this.nombre}`; }
  };

ACCEDER
  alumno.nombre              → "Ada"   (punto: lo más cómodo)
  alumno["edad"]             → 36      (corchete: claves dinámicas)
  const campo = "nombre"; alumno[campo] → "Ada"   ← por qué existe

  alumno.ciudad = "Londres";           // agregar
  delete alumno.edad;                  // borrar

ATALHOS MODERNOS
  const { nombre, edad = 18 } = alumno;      // DESTRUCTURING (¡úsalo!)
  const copia = { ...alumno, edad: 37 };     // spread: copia + sobreescribe

UTILIDADES
  Object.keys(alumno)      → ["nombre", "edad", "cursos", "saludar"]
  Object.values(alumno)    → lista de valores
  Object.entries(alumno)   → [["nombre","Ada"], ...]

THIS: dentro de métodos apunta al objeto. Las arrow functions NO lo capturan bien (usar function/método).""",
  [("¿Qué hace const { nombre } = alumno?", ["Borra nombre del objeto", "Extrae alumno.nombre en una variable llamada nombre (destructuring)", "Crea un objeto", "Convierte a JSON"], 1, "Destructuring: la forma idiomática de extraer propiedades en JS moderno."),
   ('¿Cuándo usar alumno["nombre"] en vez de alumno.nombre?', ["Nunca, es obsoleto", "Cuando la clave viene de una variable o tiene espacios", "Es más rápido", "Para métodos solamente"], 1, "Los corchetes aceptan expresiones: alumno[variable] resuelve la clave dinámicamente.")]),
 ("12. JSON: el idioma universal de los datos", """JSON: DE TEXTO A DATOS Y VUELTA
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
JSON (JavaScript Object Notation) es EL formato para mover datos entre sistemas: APIs, archivos, bases de datos.

SE PARECE a un objeto JS pero: claves SIEMPRE con comillas dobles, sin funciones, sin comentarios.
  '{"nombre":"Ada","edad":36,"activa":true}'

LAS DOS FUNCIONES
我们可以JSON
  const texto = JSON.stringify(alumno);      // objeto → TEXTO (para enviar/guardar)
  const obj   = JSON.parse(texto);           // TEXTO → objeto (al recibir/leer)

USO REAL
  // Guardar en localStorage del navegador:
  localStorage.setItem("alumno", JSON.stringify(alumno));
  const recuperado = JSON.parse(localStorage.getItem("alumno"));

  // Enviar a una API (lo veremos con fetch):
  fetch("/api", { method: "POST", body: JSON.stringify(datos) })

TRAPPER ERROR COMÚN
JSON.parse(texto inválido) → SyntaxError. En producción: try/catch y valida.

INDENTADO para humanos: JSON.stringify(obj, null, 2).""",
  [("¿Qué hace JSON.stringify(datos)?", ["Lee un archivo", "Convierte datos JS en texto JSON para guardar/enviar", "Valida el JSON", "Imprime bonito"], 1, "stringify serializa; parse deserializa. Juntas son el puente de datos."),
   ("¿Qué pasa si JSON.parse recibe texto mal formado?", ["Devuelve null", "Devuelve el texto igual", "Lanza SyntaxError", "Lo repara solo"], 2, "parse es estricto — envuélvelo en try/catch en código serio.")]),
 ("13. El DOM: convertir HTML en objeto vivo", """DOM: EL HTML COMO OBJETOS MANIPULABLES
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
El navegador convierte tu HTML en un árbol de objetos: el DOM. JS lo lee y lo MODIFICA en vivo.

SELECCIONAR
  document.querySelector(".tarjeta")       ← el primero que coincide (selector CSS)
  document.querySelectorAll("p")           ← todos (NodeList iterable)
  document.getElementById("titulo")        ← por id (viejo pero válido)

LEER Y CAMBIAR
  el.textContent = "Nuevo texto";          // texto plano
  el.innerHTML = "<b>Marcado</b>";          // HTML (⚠ riesgo de inyección con input de usuario)
  el.style.color = "red";                   // CSS inline
  el.classList.add("activa");   el.classList.toggle("activa");   // clases ✅ mejor práctica

CREAR Y ANEXAR
  const p = document.createElement("p");
  p.textContent = "Hola, DOM";
  document.body.appendChild(p);

REGLA: evita innerHTML con datos de usuario (XSS); textContent es seguro por defecto.""",
  [("¿Qué método es seguro para insertar TEXTO de usuario en la página?", ["innerHTML", "textContent", "eval()", "document.write()"], 1, "textContent no interpreta HTML: protege contra inyección XSS básica."),
   ("¿Qué hace el.classList.toggle('activa')?", ["Siempre la añade", "Siempre la quita", "La añade si no está, la quita si está", "La renombra"], 2, "Toggle = interruptor: perfecto para menús, modos oscuro/claro, etc.")]),
 ("14. Eventos: la web reacciona", """EVENTOS: LISTENERS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  const boton = document.querySelector("#agregar");
  boton.addEventListener("click", () => {
    console.log("¡Clickeaste!");
  });

EVENTOS COMUNES
  click · dblclick · submit (formularios) · input/keydown/change (campos)
  mouseenter/mouseleave · scroll · DOMContentLoaded

EL OBJETO EVENT
  input.addEventListener("input", (evento) => {
    console.log(evento.target.value);      // lo que hay en el campo
  });

FORMULARIOS: el default es RECARGAR la página — evítalo:
  form.addEventListener("submit", (e) => {
    e.preventDefault();                    // ¡siempres!
    // procesar datos aquí
  });

DELEGACIÓN (para listas dinámicas): un listener en el padre que filtra por e.target
  lista.addEventListener("click", e => {
    if (e.target.matches(".borrar")) e.target.parentElement.remove();
  });""",
  [("¿Por qué e.preventDefault() en el submit de un formulario?", ["Acelera el envío", "Evita que el navegador recargue la página para procesarlo con JS", "Valida los campos", "Es opcional sin efecto"], 1, "Sin preventDefault, el formulario navega/recarga y tu lógica JS no corre."),
   ("¿Qué es delegación de eventos?", ["Un listener por cada hijo", "Un solo listener en el padre que reacciona según e.target", "Eventos automáticos", "Eventos de red"], 1, "Clave para contenido dinámico: los hijos futuros también funcionan.")]),
 ("15. Asincronía: setTimeout, promesas y async/await", """ASINCRONÍA: NO BLOQUEAR LA FIESTA
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
JS corre en un solo hilo. Las operaciones lentas (red, disco, timers) NO deben congelar la página. Solución: asincronía.

TIMER
  setTimeout(() => console.log("pasaron 2s"), 2000);   // no bloquea

PROMESAS (un valor que llegará: pending → fulfilled/rejected)
  fetch(url)
    .then(respuesta => respuesta.json())
    .then(datos => console.log(datos))
    .catch(error => console.error(error));

ASYNC/AWAIT — la sintaxis moderna (ES azúcar sobre promesas, se lee de arriba hacia abajo)
  async function traerUsuarios() {
    try {
      const resp = await fetch("/api/usuarios");
      const datos = await resp.json();
      console.log(datos);
    } catch (e) { console.error("Falló:", e); }
  }

REGLAS
1. await SOLO dentro de async
2. Siempre maneja errores (try/catch o .catch)
3. Promise.all([p1, p2]) → varias en paralelo""",
  [("¿Qué devuelve inmediatamente una función async?", ["El resultado final", "Una promesa", "undefined", "El error"], 1, "async significa 'esto devolverá una promesa'; await desenvuelve su valor."),
   ("¿Para qué sirve Promise.all?", ["Cancelar promesas", "Esperar varias promesas EN PARALELO y continuar cuando todas terminan", "Convertir promesas a callbacks", "Una por una"], 1, "Paralelismo de verdad: si son independientes, esperar juntas = mitad del tiempo.")]),
 ("16. fetch: hablar con APIs del mundo", """FETCH: CLIENTE DE APIS EN 10 LÍNEAS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
GET (leer):
  const resp = await fetch("https://api.github.com/users/octocat");
  if (!resp.ok) throw new Error("HTTP " + resp.status);   // ¡fetch NO falla en 404/500!
  const datos = await resp.json();

POST (enviar):
  const resp = await fetch("/api/tareas", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ titulo: "Aprender fetch" })
  });

LAYOUT COMPLETO PROFESIONAL
  async function api(url, opciones = {}) {
    const resp = await fetch(url, opciones);
    if (!resp.ok) throw new Error(`${resp.status} ${resp.statusText}`);
    return resp.json();
  }

RECUERDOS VITALES
1. resp.ok es tu responsabilidad: fetch solo rechaza en error de RED
2. JSON requiere el header Content-Type al enviar
3. Las APIs públicas gratis para practicar: JSONPlaceholder, PokéAPI, GitHub API""",
  [("¿Cuándo rechaza fetch (lanza error) SIN ayuda tuya?", ["En cualquier error HTTP 4xx/5xx", "Solo en errores de red (sin conexión, CORS, DNS)", "Siempre que resp.ok es false", "Nunca"], 1, "Por eso el patrón: chequear resp.ok y lanzar tu propio error en 4xx/5xx."),
   ("¿Qué header obliga al enviar JSON con POST?", ["Accept", "Content-Type: application/json", "Authorization", "User-Agent"], 1, "Sin ese header, muchos servidores no interpretan el body como JSON.")]),
 ("17. Clases y módulos: código a escala", """ESTRUCTURA CUANDO CRECE EL PROYECTO
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
CLASES (plantillas de objetos con comportamiento)
  class Tarea {
    constructor(titulo) {
      this.titulo = titulo;
      this.completada = false;
    }
    completar() { this.completada = true; }
    static desdeJSON(obj) { return Object.assign(new Tarea(obj.titulo), obj); }
  }
  const t = new Tarea("Estudiar clases");
  t.completar();

  class TareaUrgente extends Tarea {     // herencia
    completar() { super.completar(); this.prioridad = "alta"; }
  }

MÓDULOS ES (1 responsabilidad = 1 archivo)
  // utilidades.js
  export const sumar = (a, b) => a + b;
  export default class Calculadora { }

  // app.js
  import Calculadora, { sumar } from "./utilidades.js";

  En el navegador: <script type="module" src="app.js"></script>

REGLA: archivos como cajones etiquetados. Cuando uno pasa de ~300 líneas, pregúntate si son dos.""",
  [("¿Qué hace export default frente a export nombrado?", ["Es más rápido", "Un solo default por archivo, se importa sin llaves; los nombrados van con llaves exactas", "Default es privado", "No hay diferencia"], 1, "import X from... (default) vs import { x } from... (nombrados)."),
   ("¿Qué hace super.completar() en una subclase?", ["Borra el método del padre", "Invoca la versión del método en la clase padre", "Copia el objeto", "Nada"], 1, "super = acceso a la clase padre: reutilizas y extiendes en vez de reescribir.")]),
 ("18. Proyecto final: aplicación completa de tareas (DOM + eventos + JSON)", """CONSTRUYE: GESTOR DE TAREAS COMPLETO
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Todo el curso condensado en UNA app. Sin frameworks. Para tu portafolio.

MVP (versión mínima, 2 pomodoros)
1. index.html: input + botón + lista <ul>
2. app.js:
   const tareas = JSON.parse(localStorage.getItem("tareas") || "[]");
3. Agregar tarea (submit + preventDefault + push + render + save)
4. render(): limpiar ul, crear li por cada tarea (createElement + textContent ¡no innerHTML!)
5. Marcar completada (toggle class tachado; delegación de eventos)
6. Borrar (botón 🗑 por li; delegación)
7. Filtro: todas/pendientes/hechas (array.filter + render)
8. save(): localStorage.setItem("tareas", JSON.stringify(tareas))

CHECKLIST DE CALIDAD
• [ ] Funciona al recargar (persistencia JSON)
• [ ] Sin bugs con nombres raros (<script> como título → prueba el XSS)
• [ ] Código en: funciones puras tarea-objeto + render + listeners separados

🎓 Si pasaste TODOS los quizzes 🏆 del curso: genera tu certificado en 📚 Aprender.""",
  [("¿Qué dos llamadas sincronizan la app con localStorage?", ["parse y stringify de JSON", "fetch GET y POST", "push y pop", "querySelector y createElement"], 0, "stringify al guardar, parse al cargar: JSON es el puente."),
   ("¿Por qué delegación de eventos en la lista en vez de listener por li?", ["Es más corto", "Los li se recrean en cada render; un solo listener en el ul sigue funcionando siempre", "Es requisito del DOM", "No hay razón"], 1, "Contenido dinámico = listener en el padre estable, acción según e.target.")]),
],
# ═══════════════════ 5. TYPESCRIPT (7) ═══════════════════
"TypeScript — JavaScript con Superpoderes y Seguridad": [
 ("1. TypeScript en 10 minutos: por qué existe", """TS: JS + CHEQUEO DE TIPOS ANTES DE EJECUTAR
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
TypeScript es JavaScript con anotaciones que el compilador verifica ANTES de que corras nada. Detecta 40% de bugs típicos sin ejecutar.

  let edad: number = 36;
  edad = "treinta y seis";     // ❌ Error EN EDICIÓN, no en producción

LA MAGIA: todo JS válido es TS válido. Acoges gradualmente.

HERRAMIENTAS
  npm install -g typescript   → tsc archivo.ts → archivo.js
  tsc --init                   → tsconfig.json (configuración del proyecto)

EL TS NUNCA CORRE; el tsc lo CONVIERTE a JS limpio y eso es lo que se ejecuta.
Por eso los builds: TS → compilar → JS → navegador/Node.

ADOPCIÓN: hoy es la norma industrial. React/Angular/Node serio = TypeScript.
Empezar un proyecto nuevo 2026 sin TS es autoinfringirse sufrimiento a mediano plazo.""",
  [("¿Qué es TypeScript exactamente?", ["Un lenguaje distinto a JS", "JavaScript + chequeo estático de tipos que se compila a JS puro", "Una librería de JS", "Un navegador"], 1, "Superconjunto tipado: corre como JS tras compilar — el navegador jamás ve tipos."),
   ("¿Cuándo detecta TypeScript los errores de tipo?", ["En producción", "Al editar/compilar, antes de ejecutar", "Nunca", "Solo con tests"], 1, "Shift-left: el error aparece cuando lo escribes, no cuando el usuario lo encuentra.")]),
 ("2. Tipos básicos y anotaciones", """EL VOCABULARIO DE TIPOS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  const nombre: string = "Ada";
  const edad: number = 36;
  const activa: boolean = true;
  const temas: string[] = ["js", "ts"];
  const punto: [number, number] = [10, 20];        // tupla: posición y tipo fijos
  let cualquier: any = ...;                        // ⚠ desactiva la seguridad: evítalo
  let desconocido: unknown = ...;                  // any seguro: obliga a verificar antes de usar

INFERENCIA: TS adivina; SÓLO anota cuando no es obvio
  let total = 0;              // TS sabe que es number (no anotes de más)

FUNCIONES — lo más valioso está aquí:
  function sumar(a: number, b: number): number { return a + b; }
  const log = (m: string): void => { console.log(m); };    // void: no devuelve

OBJETOS
  type Alumno = { nombre: string; edad: number; email?: string };   // ? = opcional
  const ada: Alumno = { nombre: "Ada", edad: 36 };

LITERALES: type Rol = "admin" | "editor" | "lector";   ← solo esos valores""",
  [("¿Cuándo anotar tipos explícitamente?", ["En TODAS las variables", "Cuando la inferencia no es obvia (y siempre en firmas de funciones públicas)", "Nunca", "Solo en clases"], 1, "TS infiere en la asignación; anota donde el contrato importa."),
   ("¿Qué diferencia hay entre any y unknown?", ["Ninguna", "any desactiva toda verificación; unknown exige comprobar el tipo antes de usarlo", "unknown es más corto", "any es para números"], 1, "unknown = 'no sé aún, pero TS me protege'; any = 'ríndete, compilador'.")]),
 ("3. Interfaces vs Types: modelar el mundo", """MODELAR DATOS CON ESTILO
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
INTERFACE — el contrato de forma de un objeto:
  interface Usuario {
    id: number;
    nombre: string;
    email?: string;          // opcional
    readonly creado: Date;   // solo lectura tras crear
  }
  function guardar(u: Usuario) { ... }

TYPE — el comodín: uniones, intersecciones, alias, todo:
  type Resultado = "ok" | "error";
  type Admin = Usuario & { permisos: string[] };        // intersección

EXTENDER
  interface ConEmail extends Usuario { email: string; }  // requerido aquí

¿CUÁL USAR? Convención 2026:
• Formas de objetos/clases/domínio → interface (mensajes de error más claros, se fusionan)
• Uniones, tuplas, funciones, composiciones → type

UTILITY TYPES (los usarás con React y APIs):
  Partial<Usuario>  (todo opcional) ·  Required  ·  Pick<Usuario,"nombre">  ·  Omit""",
  [("¿Cuándo elegir interface sobre type?", ["Siempre", "Para formas de objetos: más legible, mensajes de error claros y extensión natural", "Nunca", "Solo en Angular"], 1, "Interface para modelos de dominio; type para uniones y composiciones."),
   ('¿Qué expresa type Estado = "cargando" | "ok" | "error"?', ["Un objeto", "Una unión de literales: la variable solo vale uno de esos strings", "Un enum numérico", "Un error"], 1, "Uniones de literales = estados exhaustivos que TS puede verificar (sin strings sueltos).")]),
 ("4. Genéricos: reusabilidad con seguridad", """GENÉRICOS: <T> = TIPO PARÁMETRO
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Sin genérico pierdes tipos o repites código:
  function identidad<T>(valor: T): T { return valor; }
  identidad("hola")      → T = string
  identidad(42)          → T = number      (TS lo infiere)

CASOS REALES (los verás en TODAS las librerías)
  Array<string>          ≡ string[]
  Promise<Usuario>       → el await te da Usuario
  Map<string, number>    → diccionario con clave/valor tipados

RESTRINGIR (constraints): el genérico con requisitos mínimos:
  function largo<T extends { length: number }>(x: T): number { return x.length; }
  largo("hola")    ✅ (string tiene length)
  largo(42)        ❌

GENÉRICOS EN FUNCIONES DE API (el patrón favorito del mundo real):
  async function api<T>(url: string): Promise<T> { ... }
  const user = await api<Usuario>("/me");   // user: Usuario, autocomplete total

REGLA: cuando la firma de una función depende del tipo de OTRA parte de sí misma → genérico.""",
  [("¿Qué gana identidad<T>(v: T): T respecto a misto?: any?", ["Nada", "Recuerda el tipo exacto de entrada y lo devuelve: autocomplete y chequeo completos", "Es más rápido", "Evita compilar"], 1, "Los genéricos modelan RELACIONES entre tipos — any solo las borra."),
   ("¿Qué hace <T extends { length: number }>?", ["Crea una clase T", "Restringe T a tipos que tengan la propiedad length", "Hace T opcional", "Borra el tipo"], 1, "Constraint: puedo usar .length sabiendo que el compilador lo garantiza.")]),
 ("5. Clases en TS: private, readonly e implements", """POO SERIA CON VISIBILIDAD
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  class Cuenta {
    private saldo: number;          // solo accesible dentro
    readonly titular: string;       // no reasignable fuera del init

    constructor(titular: string) {
      this.titular = titular;
      this.saldo = 0;
    }

    depositar(monto: number): number {
      if (monto <= 0) throw new Error("Monto debe ser positivo");
      return this.saldo += monto;
    }
    getSaldo(): number { return this.saldo; }
  }

IMPLEMENTS: contratos explícitos (fundamental con DI y testing)
  interface Repositorio<T> { guardar(item: T): void; obtener(id: number): T | undefined; }
  class RepoMemoria implements Repositorio<Tarea> { ... }

ACCESO POR DEFECTO = public. Escribe private explícito: documenta.

QUÍMICA CON INTERFACES: programa contra la interface, no la clase concreta → mañana cambias RepoMemoria por RepoSQLite y NADIE más se entera. Esto es la base de la arquitectura limpia y el testing con mocks.""",
  [("¿Qué permite una propiedad private?", ["Acceso desde任何地方", "Solo acceso dentro de la propia clase", "Solo lectura universal", "Nada, es decorativa"], 1, "Encapsulación: el estado interno solo cambia por métodos controlados."),
   ("¿Para qué sirve implements?", ["Copiar código de otra clase", "Obligar a la clase a cumplir el contrato de una interface", "Importar módulos", "Hacer públicas las props"], 1, "El compilador verifica que cumples el contrato — la base de sustituir implementaciones (mocks, DBs).")]),
 ("6. Narrowing y utilidades: escribir lógica segura", """NARROWING: DESECHAR CASOS Y GANAR CERTEZA
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
TS VIGILA tu código y afina el tipo dentro de condicionales:

  function procesar(x: string | number) {
    if (typeof x === "string") { x.toUpperCase(); }   // aquí x ES string ✅
    else                       { x.toFixed(2); }       // aquí x ES number ✅
  }

OPERADORES DE NARROWING
  typeof · instanceof · "prop" in obj · truthiness (if (user))
  Discriminated unions — el PATTERN estrella para estados:
  type Estado =
    | { kind: "cargando" }
    | { kind: "ok"; datos: string[] }
    | { kind: "error"; mensaje: string };
  if (estado.kind === "ok") estado.datos;              // ✅ TS lo sabe
  else if (estado.kind === "error") estado.mensaje;    // ✅

TYPE GUARDS (función que certifica):
  function esString(x: unknown): x is string { return typeof x === "string"; }

⚠ CASTING (as) → último recurso; "tú sabes más que el compilador" suele envejecer mal:
  (valor as Usuario).nombre""",
  [("¿Qué es una discriminated union?", ["Unir objetos con &", "Una unión donde cada variante tiene una clave literal común (kind) que permite narrowing", "Una clase abstracta", "Un enum"], 1, "El patrón de modelado de estados favorito en TS: cada rama decide la forma disponible."),
   ("¿Qué significa x is string en un type guard?", ["Una comparación", "Le dice a TS: si esta función devuelve true, trata x como string de ahí en adelante", "Convierte el tipo", "Un error de sintaxis"], 1, "Los guards personalizados enseñan al compilador a razonar sobre tus datos.")]),
 ("7. TS en proyectos reales: configuración y flujo", """DE LOS TIPOS A LA PRODUCCIÓN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SETUP
  npm init -y
  npm install --save-dev typescript
  npx tsc --init      → tsconfig.json

TSCONFIG (los 5 que importan)
  "strict": true           ← SIEMPRE; activa todas las protecciones
  "target": "ES2022"       ← JS de salida moderno
  "outDir": "./dist"       ← compilado separado de src
  "rootDir": "./src"
  "noEmitOnError": true    ← si hay errores, no publica

FLUJO
  src/*.ts → npx tsc (watch: npx tsc --watch) → dist/*.js → node dist/app.js
  (y en frontend: Vite/esbuild lo hacen transparente)

CON LIBRERÍAS JS: instala sus tipos
  npm i express && npm i -D @types/express   ← la comunidad tipa casi todo

DISCIPLINA REAL
1. strict desde el día 1 (aflojar después es dolor)
2. Errores de tipo se ARREGLAN; los `as any` se cuentan como deuda técnica
3. Tipos en los límites (APIs, archivos, props) y deja inferir en el interior""",
  [("¿Qué activa \"strict\": true en tsconfig?", ["Solo chequeo básico", "Una familia de protecciones: null checks, noImplicitAny, etc. — el modo serio de TS", "Rápida ejecución", "Nada"], 1, "Strict atrapa el grueso de los bugs de tipo. Proyecto profesional sin strict = medio TS."),
   ("¿Cómo usar tipos con una librería JS como express?", ["No se puede", "npm i -D @types/express (definiciones de tipos de la comunidad)", "Reescribirla en TS", "Con un plugin"], 1, "@types/* cubre todo el ecosistema popular: tu editor la entiende como si fuera TS nativa.")]),
],
# ═══════════════════ 6. REACT (8) ═══════════════════
"React — Interfaces Modernas y Reutilizables": [
 ("1. React: pensar en componentes", """REACT EN UNA IDEA: UI = f(estado)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
React es una librería para construir UIs con COMPONENTES: funciones que reciben datos (props) y devuelven descripciones de qué mostrar (JSX). Cuando el estado cambia, React re-renderiza lo necesario. Tú no tocas el DOM a mano.

SETUP MODERNO (Vite)
  npm create vite@latest mi-app -- --template react
  cd mi-app && npm install && npm run dev

TU PRIMER COMPONENTE
  // App.jsx
  function Saludo({ nombre }) {
    return <h1>¡Hola, {nombre}!</h1>;
  }
  export default Saludo;

JSX = mezcla HTML con JS (entre llaves):
  <p>2 + 2 = {2 + 2}</p>
  <img src={url} alt={texto} />
⚠ className (no class) · todas las etiquetas se cierran · un solo padre raíz (o <>fragment</>)

EL CICLO: escribes componentes → compones → React se encarga del DOM.""",
  [("¿Qué es JSX?", ["Un lenguaje aparte", "Sintaxis que escribe HTML dentro de JS y llama funciones de React para construir el DOM", "CSS en JS", "Un compilador"], 1, "JSX describe la UI; Babel/Vite lo convierte en llamadas a funciones."),
   ("¿Qué son las props?", ["Variables globales", "Los datos que un componente recibe de su padre (parámetros del componente)", "Estilos del componente", "Funciones internas"], 1, "Componente = función; props = sus argumentos. Comunicación de padre a hijo.")]),
 ("2. Estado con useState: que la UI reaccione", """ESTADO: LA MEMORIA DEL COMPONENTE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Los datos LOCALES que cambian con el tiempo viven en estado:
  import { useState } from "react";

  function Contador() {
    const [cuenta, setCuenta] = useState(0);

    return (
      <button onClick={() => setCuenta(cuenta + 1)}>
        Clicks: {cuenta}
      </button>
    );
  }

REGLAS DE ORO
1. NUNCA mutar estado directamente: usa el setter (setCuenta(...))
2. Con estado previo: setCuenta(c => c + 1) (forma funcional, la segura)
3. Estado = inmutable mentalmente: arrays se reemplazan, no se les hace push:
     setTareas([...tareas, nueva])/ setTareas(tareas.filter(t => t.id !== id))

ESTADO vs VARIABLE: reasignar una variable NO re-renderiza. El estado SÍ.

SUBIR ESTADO: si dos componentes lo necesitan, vive en el padre COMÚN y baja por props.""",
  [("¿Por qué setTareas([...tareas, nueva]) y no tareas.push(nueva)?", ["push está prohibido", "React detecta cambios por REFERENCIA: hay que pasarle un array NUEVO o no re-renderiza", "Es más corto", "Ambas funcionan igual"], 1, "Inmutabilidad: nueva referencia = señal de re-render. push muta en silencio."),
   ("¿Qué forma de actualización de estado es segura con valores previos?", ["setCuenta(cuenta + 1)", "setCuenta(c => c + 1)", "cuenta++", "las dos primeras igual"], 1, "La forma funcional garantiza trabajar sobre el estado más reciente (clicks encolados).")]),
 ("3. Renderizar listas y condicionales", """LISTAS: MAP + KEY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  {tareas.map(t => (
    <li key={t.id} className={t.hecha ? "tachada" : ""}>
      {t.texto}
    </li>
  ))}

KEY: identifica cada elemento entre re-renders
• Debe ser estable y único: ID real, NO el índice del map (salvo lista estática inmutable)
• Sin key: React confunde elementos → bugs visuales y de formulario

CONDICIONALES (dentro del JSX siempre expresiones)
  {cargando && <Spinner />}                 // renderizar o no
  {usuario ? <Panel/> : <Login/>}            // una u otra
  {estado === "error" && <Alerta msg={error}/>}

⚠ VERDAD DEL if: no escribes if dentro del JSX; escribes expresiones boolean/ternarias.
Para ifs complejos: extrae a una función o variable ANTES del return:
  let contenido = estado === "ok" ? <Datos/> : <Vacio/>;
  return <div>{contenido}</div>;""",
  [("¿Qué prop requiere React al mapear elementos y por qué?", ["id, por CSS", "key: identidad estable entre renders para emparejar el DOM correctamente", "className, por estilos", "index, por orden"], 1, "La key es DNI, no apellido: el índice del map cambia y traiciona con listas dinámicas."),
   ("¿Cómo renderizar condicionalmente en JSX?", ["Con if/else dentro de llaves", "Operador &&, ternario, o variable calculada ANTES del return", "Con v-if", "No se puede"], 1, "JSX admite expresiones, no sentencias: la lógica va en expresiones o antes del return.")]),
 ("4. Eventos, formularios y estado controlado", """FORMULARIOS CONTROLADOS (EL PATRÓN REACT)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
El ESTADO manda, el input solo lo refleja:
  const [texto, setTexto] = useState("");
  <input
    value={texto}
    onChange={e => setTexto(e.target.value)}
    placeholder="Nueva tarea..."
  />
Cada tecla → setState → re-render → input muestra el nuevo valor. Simple y predecible.

FORMULARIO COMPLETO
  const manejarSubmit = (e) => {
    e.preventDefault();                        // siempre
    if (!texto.trim()) return;
    onAgregar(texto.trim());                   // avisa al padre
    setTexto("");                              // reset controlado
  };
  <form onSubmit={manejarSubmit}>...</form>

EVENTOS SYNTHETICS: React envuelve eventos nativos. Los usas igual; onClic se escribe onClick (camelCase).

UNIDIRECCIONAL = la paz mental: estado arriba; eventos abajo; nunca al revés. Cuando sientas que "empujamos datos hacia arriba", llamas a una función que el padre te pasó por props.""",
  [("¿Qué significa input 'controlado'?", ["readonly", "Su value viene del estado y onChange lo actualiza: el estado es la fuente de verdad", "Que valida solo", "Que usa refs"], 1, "Estado ↔ input en bucle controlado. React manda; el DOM obedece."),
   ("¿Cómo sabe el hijo que debe agregar una tarea si el estado está arriba?", ["Accede al estado del padre directamente", "Llama a una función que el padre le pasó por props (onAgregar)", "Modifica el DOM del padre", "No puede"], 1, "Datos bajan por props; cambios suben ejecutando callbacks que bajaron por props.")]),
 ("5. useEffect: sincronizar con el mundo exterior", """EFECTOS: DESPUÉS DEL RENDER
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
useEffect corre código DESPUÉS de que React pinta: fetch, timers, suscripciones, localStorage.

  useEffect(() => {
    // efecto
    return () => { /* limpieza opcional (cancela fetch, limpia timer) */ };
  }, [dependencias]);

EL ARRAY LO CAMBIA TODO
  useEffect(fn)           → tras CADA render (casi nunca lo quieres)
  useEffect(fn, [])       → UNA vez al montar (fetch inicial límpio)
  useEffect(fn, [id])     → cada vez que CAMBIA id

EJEMPLO REAL (con guardia para doble montaje en StrictMode):
  useEffect(() => {
    let cancelado = false;
    fetch(`/api/tareas/${id}`).then(r => r.json()).then(d => {
      if (!cancelado) setTarea(d);
    });
    return () => { cancelado = true; };
  }, [id]);

REGLAS: no sincronices React consigo mismo con effects (calcula en render); efectos = ir AFUERA (API, temporalización, DOM externo).""",
  [("¿Cuándo se ejecuta useEffect(fn, [])?", ["Cada render", "Una vez al montar el componente", "Al desmontar", "Nunca"], 1, "Array vacío = sin dependencias: solo el montaje. La limpieza corre al desmontar."),
   ("¿Para qué sirve la función de limpieza del efecto?", ["Borrar el estado", "Cancelar trabajo pendiente (fetch, timers, subscripciones) antes de re-ejecutar o desmontar", "Limpiar el JSX", "Es teórica"], 1, "Evita race conditions y fugas: la respuesta tardía de un fetch viejo no pisa la nueva.")]),
 ("6. Composición, context y custom hooks: las 3 escaleras", """CRECER SIN COLAPSAR
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1. COMPOSICIÓN — children:
  function Card({ titulo, children }) {
    return <section className="card"><h2>{titulo}</h2>{children}</section>;
  }
  <Card titulo="Tareas"><ListaTareas/></Card>
Antes de context/estado global, llega lejos con children.

2. CONTEXT — datos que necesita mucha profundidad sin prop-drilling:
  const TemaContext = createContext("claro");
  <TemaContext.Provider value="oscuro">{app}</TemaContext.Provider>
  const tema = useContext(TemaContext);   // en cualquier nieto
Úsalo para: tema, usuario logueado, idioma. No para TODO (vuelve lento al re-render).

3. CUSTOM HOOKS — lógica reutilizable con estado:
  function useLocalStorage(clave, inicial) {
    const [valor, setValor] = useState(() =>
      JSON.parse(localStorage.getItem(clave)) ?? inicial);
    useEffect(() => localStorage.setItem(clave, JSON.stringify(valor)), [clave, valor]);
    return [valor, setValor];
  }
  // uso: const [tema, setTema] = useLocalStorage("tema", "claro");

Los hooks empiezan con "use" y solo se llaman en el nivel SUPERIOR (ni loops ni condicionales).""",
  [("¿Cuándo llegar a Context?", ["Desde el primer día", "Cuando muchos componentes a mucha profundidad necesitan el mismo dato (tema, usuario, idioma)", "Para todo el estado", "Nunca"], 1, "Context resuelve prop-drilling global; estado local y composición resuelven la mayoría de los casos."),
   ("¿Qué reglas tienen los hooks (useState, useEffect, customs)?", ["Top-level del componente, sin loops/ifs, nombres use*", "Cualquier lugar del archivo", "Solo en useEffect", "Dentro de condicionales"], 0, "El orden fijo de llamadas es cómo React empareja hook con celda de estado: romperlo = caos.")]),
 ("7. Patrones reales: fetch con estados y manejo de errores", """ FETCH EN REACT NIVEL PRODUCCIÓN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  const [datos, setDatos] = useState(null);
  const [cargando, setCargando] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    let cancelado = false;
    (async () => {
      try {
        setCargando(true); setError(null);
        const resp = await fetch("/api/tareas");
        if (!resp.ok) throw new Error(`HTTP ${resp.status}`);
        if (!cancelado) setDatos(await resp.json());
      } catch (e) {
        if (!cancelado) setError(e.message);
      } finally {
        if (!cancelado) setCargando(false);
      }
    })();
    return () => { cancelado = true; };
  }, []);

RENDERIZAR POR ESTADOS (discrimina siempre)
  if (cargando) return <Spinner/>;
  if (error)    return <Alerta texto={error} reintentar={refetch}/>;
  if (!datos?.length) return <Vacio texto="Sin tareas todavía 🌱"/>;
  return <Lista items={datos}/>;

MEJORA MADURA (proyectos grandes): React Query/SWR cachean, reintentan y sincronizan solos — pero primero domina esto a mano para entenderlos.""",
  [("¿Qué 3 estados mínimos modelan cualquier fetch en UI?", ["vacio, ok, no", "cargando, error, datos", "init, run, end", "get, post, delete"], 1, "Con esos tres discriminas exáctamente qué pintar: spinner, mensaje de error o contenido."),
   ("¿Por qué la bandera 'cancelado' en el efecto de fetch?", ["Cancela la red", "Evita que una respuesta tardía actualice estado de un componente desmontado (warning + race)", "Acelera fetch", "No es necesaria"], 1, "En StrictMode y navegación rápida los componentes se montan/desmontan: la guardia lo hace robusto.")]),
 ("8. Proyecto: app de notas con todo el curso", """CONSTRUYE: NOTAS REACT COMPLETAS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Requisitos (todo lo aprendido):
1. Estado: notas (array de {id, titulo, texto}) con useState
2. Persistencia: custom hook useLocalStorage("notas", [])
3. UI: formulario controlado (submit + validar trim) · lista con map+key · borrar por nota
4. Filtro de búsqueda: notas.filter(n => n.texto.toLowerCase().includes(busqueda))
5. Edición: estado editando; reemplazar con map(n => n.id === id ? {...n, texto} : n)
6. UI por estados: vacío / lista / editando (ternarios antes del return o componentes)
7. CSS: una clase .nota:hover con transition; responsive mínimo
8. Opcional subidón: useEffect que sincronice al cerrar la pestaña con beforeunload

ENTREGA (para portafolio)
• npm run build → carpeta dist estática
• Despliegue gratis: GitHub Pages / Vercel / Netlify (curso Despliegue)
• README con screenshot y lista de patrones usados

Dales las gracias después: si la terminaste SIN mirar soluciones, ya piensas en React.""",
  [("¿Cómo editar una nota inmutablemente en un array de estado?", ["notas[idx].texto = x", "map que devuelve objeto nuevo {...n, texto: x} solo para el id coincidente", "splice y setState", "push y pop"], 1, "map con spread: reemplazas el objeto con uno NUEVO; referencias nuevas → React entiende y la UI se actualiza."),
   ("¿Qué dos APIs persisten las notas en esta app?", ["fetch + axios", "useState + useEffect dentro de un custom hook useLocalStorage", "Redux + thunk", "Context + reducer"], 1, "Estado + efecto que escribe a localStorage: patrón simple, potente y reutilizable.")]),
],
# ═══════════════════ 7. NODE.JS (6) ═══════════════════
"Node.js — JavaScript en el Servidor": [
 ("1. Node: sacar JS del navegador", """NODE: V8 EN LA TERMINAL
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Node.js corre JavaScript fuera del navegador: servidores, CLIs, scripts. Mismo lenguaje, otro hogar.

SETUP + PRIMER SCRIPT
  # instalar: nodejs.org o nvm (gestor de versiones, recomendado)
  node --version
  node app.js                  # ejecutar archivos

MÓDULOS NATIVOS CLAVE (sin instalar nada)
  const fs = require("fs");            // sistema de archivos (CommonJS clásico)
  import fs from "node:fs/promises";   // ES Modules moderno (package.json: "type": "module")
  const path = require("path");        // rutas portables
  const http = require("http");        // servidor crudo

HOLA SERVIDOR (el famoso):
  import http from "node:http";
  http.createServer((req, res) => {
    res.writeHead(200, { "Content-Type": "text/plain; charset=utf-8" });
    res.end("Hola desde Node 🚀");
  }).listen(3000, () => console.log("http://localhost:3000"));

ARCHIVOS
  await fs.writeFile("nota.txt", "hola");
  const txt = await fs.readFile("nota.txt", "utf-8");""",
  [("¿Qué es Node.js?", ["Un framework", "Un runtime que ejecuta JS fuera del navegador (motor V8)", "Un editor", "Una base de datos"], 1, "Mismo motor V8 de Chrome, liberado para servidores y scripts."),
   ('¿Cómo activar ES Modules (import/export) en Node?', ["npm i esm", '"type": "module" en package.json (o usar .mjs)', "No se puede", "Con require"], 1, "Con esa flag, import from 'node:fs/promises' y top-level await funcionan nativamente.")]),
 ("2. npm: el universo de paquetes", """NPM: DEPENDENCIAS Y SCRIPTS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
INICIALIZAR PROYECTO
  npm init -y                    → package.json (el manifiesto)

INSTALAR
  npm install express            → dependencia de producción (dependencies)
  npm install -D jest            → solo desarrollo (devDependencies: tests, builds)
  npm install                    → restaura TODO desde package.json (node_modules NO se sube a git)

  .gitignore OBLIGADO: node_modules/   (¡pesa cientos de MB!)

SCRIPTS (automatiza tu flujo)
  "scripts": {
    "dev": "node --watch src/index.js",
    "start": "node src/index.js",
    "test": "node --test"
  }
  npm run dev          (npm test va sin 'run')

VERSIONES (semver): "express": "^4.19.2"
  ^4.19.2 = 4.x.x compatible · package-lock.json fija la instalación EXACTA (súbelo a git sí).

SEGURIDAD: revisa paquetes antes de instalar; npm audit reporta vulnerabilidades.""",
  [("¿Por qué node_modules NUNCA va a git?", ["Porque es secreto", "Es enorme y reproducible: package.json + package-lock permiten recrearlo con npm install", "Por licencias", "Porque git no lo soporta"], 1, "El manifiesto viaja; el contenido se instala. Así mantienen repos livianos TODOS los equipos."),
   ('¿Qué significa "express": "^4.19.2"?', ["Exactamente 4.19.2", "Cualquier versión 4.x.x compatible desde 4.19.2", "Mayor a 5", "Versión aleatoria"], 1, "^ permite parches y menores compatibles; el lock file congela la realidad exacta.")]),
 ("3. Express: el servidor web minimalista", """EXPRESS EN 20 LÍNEAS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  import express from "express";
  const app = express();
  app.use(express.json());                 // parsea JSON del body (middleware)

  const tareas = [];

  app.get("/api/tareas", (req, res) => res.json(tareas));

  app.post("/api/tareas", (req, res) => {
    const { titulo } = req.body;
    if (!titulo) return res.status(400).json({ error: "titulo requerido" });
    const tarea = { id: Date.now(), titulo, hecha: false };
    tareas.push(tarea);
    res.status(201).json(tarea);
  });

  app.delete("/api/tareas/:id", (req, res) => {
    const i = tareas.findIndex(t => t.id === Number(req.params.id));
    if (i === -1) return res.status(404).json({ error: "no existe" });
    res.json(tareas.splice(i, 1)[0]);
  });

  app.listen(3000, () => console.log("API en http://localhost:3000"));

CONCEPTOS: rutas (método+path → función) · params (:id) · status HTTP (200 ok, 201 creado, 400 mal pedido, 404 no hay) · middleware (código que se ejecuta ANTES: json, auth, logs).""",
  [("¿Qué es un middleware en Express?", ["Una base de datos", "Función que se ejecuta entre la petición y la ruta (JSON, auth, logs...)", "Un tipo de error", "Un plugin de VS Code"], 1, "app.use(express.json()) transforma req.body en datos listos — ejemplo clásico."),
   ("¿Qué código HTTP corresponde a 'recurso creado'?", ["200", "201", "400", "404"], 1, "201 Created: convención para POST exitoso de recursos nuevos.")]),
 ("4. Asincronía en Node: no congeles el servidor", """EL EVENT LOOP: EL MOTOR DE NODE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Node corre TODO en un hilo. Una operación lenta sincrónica CONGELA a todos los usuarios a la vez. Solución: async SIEMPRE en I/O.

  // ❌ bloqueante
  const datos = fs.readFileSync("grande.txt", "utf-8");

  // ✅ no bloqueante (promesas)
  const datos = await fs.readFile("grande.txt", "utf-8");

EN RUTAS EXPRESS: async handlers
  app.get("/api/datos", async (req, res, next) => {
    try {
      const datos = await db.query("SELECT * FROM tareas");
      res.json(datos);
    } catch (e) { next(e); }              // pásalo al middleware de errores
  });

MIDDLEWARE DE ERRORES (al final, con 4 parámetros — así lo reconoce Express)
  app.use((err, req, res, next) => {
    console.error(err);
    res.status(500).json({ error: "Error interno" });
  });

IMAGINA: camarero único (Node). Si se queda limpiando una mesa, toda la fila espera. I/O async = toma el pedido y sigue; la cocina avisa cuando está listo.""",
  [("¿Por qué prohibir readFileSync en un servidor (salvo arranque)?", ["Es más lento", "Bloquea el único hilo de Node: TODOS los usuarios esperan", "Está deprecado", "Usa mucha RAM"], 1, "El event loop único detenido = servidor congelado para todos."),
   ("¿Cómo reconoce Express un middleware de errores?", ["Por su nombre", "Tiene exactamente 4 parámetros (err, req, res, next)", "Está primero", "Lleva try/catch"], 1, "La firma de 4 argumentos es el contrato; se registra DESPUÉS de las rutas.")]),
 ("5. Express + estructura real + variables de entorno", """DE EJEMPLO A PROYECTO REAL
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ESTRUCTURA PROFESIONAL
  src/
    index.js          ← arranque (escucha puerto)
    app.js            ← configura express (testeable sin listen)
    rutas/tareas.js   ← router por recurso: express.Router()
    datos/db.js       ← acceso a datos
    middleware/auth.js
  tests/

ROUTER MODULAR
  // rutas/tareas.js
  import { Router } from "express";
  const r = Router();
  r.get("/", (req, res) => res.json(tareas));
  export default r;
  // app.js:  app.use("/api/tareas", rutasTareas);

VARIABLES DE ENTORNO — secretos FUERA del código
  .env:   DB_URL=postgres://...   JWT_SECRET=secreto
  npm i dotenv →  import "dotenv/config";  →  process.env.DB_URL
  .gitignore: .env   (NUNCA subas secretos)
  En producción: las variables reales las pone el servidor (Railway, VPS...).

CORS si tu frontend está en otro puerto:
  npm i cors → app.use(cors());""",
  [("¿Por qué los secretos van en variables de entorno y no en el código?", ["Por velocidad", "Para no publicarlos en git y poder variarlos por entorno (dev/prod)", "Porque .env es más rápido", "No hay diferencia"], 1, "Código público + secretos = filtración. .env + .gitignore es la norma; nunca commitees el .env."),
   ("¿Qué aporta separar app.js de index.js (listen)?", ["Nada útil", "Puedes importar y TESTEAR la app sin abrir puerto; separa configuración de ejecución", "Es solo estética", "Usa menos memoria"], 1, "La app testeable se exporta sin listen; en tests corren peticiones contra ella con supertest.")]),
 ("6. Proyecto: API REST real con Express", """CONSTRUYE: API DE NOTAS COMPLETA
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
MVP (3 pomodoros)
1. npm init -y; "type": "module"; npm i express dotenv
2. Rutas: GET /api/notas · GET /api/notas/:id · POST /api/notas · PATCH /api/notas/:id · DELETE /api/notas/:id
3. Datos: array en memoria primero; LUEGO archivito JSON con fs (persistencia real)
4. Validación: titulo obligatorio → 400; no existe → 404
5. status correctos: 200/201/400/404/500
6. Middleware: json + logger (console.log(req.method, req.url))
7. Probar: curl o Postman:
     curl -X POST localhost:3000/api/notas -H "Content-Type: application/json" -d '{"titulo":"hola"}'

BONUS NIVEL PRO
• Router modular en rutas/notas.js
• Middleware de errores 4-parámetros centralizado
• Paginación en GET: ?pagina=1&limite=10
• Tests con node --test + supertest

✅ Cuando: hiciste 5 endpoints funcionando con persistencia y status correctos, ya sabes construir backends. El curso de SQL le da memoria de verdad.""",
  [("¿Qué códigos HTTP usan POST-crear y 'recurso no encontrado' respectivamente?", ["200 y 400", "201 y 404", "204 y 500", "200 y 404"], 1, "201 = creado; 404 = not found. La semántica HTTP es el idioma de las APIs."),
   ("¿Cómo probar un POST sin frontend?", ["Solo desde el navegador", "curl / Postman / thunder client: cliente HTTP para probar endpoints", "Con console.log", "No se puede"], 1, "curl/demand-tester cliente es tu amigo backend: probar sin UI es el standard.")]),
],
# ═══════════════════ 8. PYTHON (16) ═══════════════════
"Python — De Cero a Profesional": [
 ("1. Python: instalación y primer programa", """PYTHON: LEGIBLE > TODO
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Instalación: python.org (marca "Add to PATH" en Windows) o sudo apt install python3.

  python3 --version
  python3 hola.py      # ejecutar
  python3              # modo interactivo (REPL) — experimenta aquí

HOLA MUNDO COMPLETO
  nombre = input("¿Tu nombre? ")       # input siempre devuelve str
  print(f"¡Hola, {nombre}!")           # f-strings: interpolación moderna

  edad = int(input("¿Edad? "))         # convertir antes de operar
  print(f"En 10 años: {edad + 10}")

FILOSOFÍA (aparece en todo): indentación = bloques de código (4 espacios, no llaves)
  if edad >= 18:
      print("mayor")          # el sangrado ES la estructura

  print() salida · input() entrada · # comentario · f"" interpolación moderna ❤

REPL para probar ideas al instante; archivos .py para guardar historias.""",
  [("¿Qué delimita los bloques de código en Python?", ["Llaves { }", "La indentación (sangría) de 4 espacios", "begin/end", "Punto y coma"], 1, "La sangría forzada hace el código universalmente legible — la idea nuclear de Python."),
   ("input() devuelve siempre...", ["int", "float", "str (hay que convertir con int()/float() para calcular)", "bool"], 2, "Fuente clásica de bugs principiantes: '5' + '5' = '55'. Convierte.")]),
 ("2. Tipos, variables y f-strings", """LOS TIPOS DE BASE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  edad = 36                  # int
  precio = 19.99             # float
  nombre = "Ada"             # str
  activo = True              # bool (¡mayúscula!)
  nada = None                # NoneType: ausencia (el null de Python)
  type(edad)                 → <class 'int'>   (pregunta su tipo)

CONVERTIR
  int("42") → 42 · float("3.14") · str(42) · bool(0) → False
  FALSY: 0, 0.0, "", [], {}, None, False

F-STRINGS: LA FORMA (desde Python 3.6)
  print(f"Me llamo {nombre} y tengo {edad} años")
  print(f"{precio:.2f}")          → 19.99 (formatos!)
  print(f"{edad * 2}")            → incluso expresiones dentro

OPERADORES: + - * / //  %  **   
  7 // 2 → 3 (entero) · 7 % 2 → 1 (residuo) · 2 ** 10 → 1024

PIP para librerías externas; para TODO lo demás, la standard library trae: math, random, datetime, json, re, os...""",
  [("¿Qué imprime 7 % 2?", ["3", "0", "1", "3.5"], 2, "% es residuo: 7 = 2×3 + 1."),
   ("¿Qué permite la f-string?", ["Solo texto", "Interpolar variables y expresiones con formato: f'{precio:.2f}'", "Solo variables", "Solo sumas"], 1, "Las f-strings combinadas con especificadores de formato son el estándar moderno.")]),
 ("3. Listas y tuplas: colecciones ordenadas", """LISTAS: EL CABALLITO DE BATALLA
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  numeros = [10, 20, 30, 40]
  numeros[0]     → 10
  numeros[-1]    → 40        (índices negativos: desde el final)
  numeros[1:3]   → [20, 30]  (slice: [inicio:fin), fin excluido)
  numeros[::-1]  → invertida

MUTAR (las listas SÍ cambian en el sitio)
  numeros.append(50) · insert(0, 5) · remove(20) (por valor) · pop() · sort()
  len(numeros) · sum(numeros) · max/min

COMPREHENSIONS — la estrella:
  cuadrados = [n ** 2 for n in range(10)]
  pares     = [n for n in numeros if n % 2 == 0]     # con filtro
Equivalente a map+filter en una línea readable.

TUPLAS: listas INMUTABLES entre paréntesis — para datos que no deben cambiar
  coordenada = (-34.9, -56.2)
  lat, lon = coordenada     # desempaquetado
  a, b = b, a               # swap elegante sin variable temporal

¿LISTA O TUPLA? Dinámicas → lista. Fijas/heterogéneas (registros) → tupla.""",
  [("¿Qué hace numeros[1:3]?", ["Devuelve 3 elementos", "Devuelve los elementos en posiciones 1 y 2 (fin excluido)", "Devuelve del 1 al 3 inclusive", "Error"], 1, "Slices: [inicio:fin) — la mitad de los bugs de principiante vienen del fin excluido."),
   ("a, b = b, a hace...", ["Comparar", "Intercambiar los valores sin variable temporal (desempaquetado)", "Error", "Crear una tupla rota"], 1, "La derecha se evalúa como tupla completa antes de asignar: el swap pythónico.")]),
 ("4. Diccionarios y sets: clave-valor y unicidad", """DICTS: LA ESTRUCTURA MÁS USADA DE PYTHON
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  alumno = {"nombre": "Ada", "edad": 36, "temas": ["py", "js"]}
  alumno["nombre"]        → "Ada"
  alumno.get("email")     → None     (¡sin explotar!)
  alumno.get("email", "sin email")   → valor por defecto
  alumno["ciudad"] = "Londres"       # agregar/actualizar
  del alumno["edad"]
  "nombre" in alumno      → True     (chequea CLAVES)

RECORRER
  for clave, valor in alumno.items(): print(clave, "=", valor)
  .keys() · .values() · .items()

DICT COMPREHENSION
  cuadrados = {n: n**2 for n in range(5)}     → {0:0, 1:1, 2:4, 3:9, 4:16}

SETS: colección SIN duplicados y sin orden — operaciones de conjunto
  set([1,1,2,3])          → {1, 2, 3}         (deduplicar al vuelo)
  {1,2,3} & {2,3,4} → {2, 3}  (intersección) · | unión · - diferencia

JSON ↔ DICT: prácticamente lo mismo → apis y archivos (lo veremos con json).""",
  [("¿Por qué alumno.get('email') en vez de alumno['email']?", ["Es más rápido", "Evita KeyError: devuelve None (o el default) si falta la clave", "Es más corto", "No hay diferencia"], 1, "get = acceso defensivo sin try/except; úsalo cuando la clave puede faltar."),
   ("¿Para qué usar set([1,1,2,3])?", ["Ordenar", "Eliminar duplicados: {1, 2, 3} (los sets no repiten)", "Sumar", "Nada útil"], 1, "Deduplicación instantánea + operaciones matemáticas de conjuntos.")]),
 ("5. Strings: métodos que usarás a diario", """STRINGS: INMUTABLES Y POTENTES
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  texto = "Hola Mundo Python"
  texto.lower() · .upper() · .title()         # casos
  texto.strip()                               # "  hola  ".strip() → limpiar edges
  texto.replace("Mundo", "Universo")
  texto.split(" ")       → ["Hola", "Mundo", "Python"]
  "-".join(["a", "b"])   → "a-b"              # une con separador
  texto.startswith("Hola") · .endswith("Python")
  "num" in texto         → False              # contiene
  texto.find("Mundo")    → 5 (-1 si no está)

INMUTABLES: cada método devuelve uno NUEVO:
  texto = texto.lower()      # reasignar si quieres el cambio

FORMATO DE FECHAS Y MILES (f-strings con poder):
  f"{precio:,.2f}"       → 1,234.56
  f"{fraccion:.1%}"      → 22.0%

SLICES también aplican: texto[::-1] invierte; texto[:4] primeros 4.""",
  [("'a-b-c'.split('-') devuelve...", ['"a-b-c"', "['a', 'b', 'c']", "('a','b','c')", "Error"], 1, "split corta en lista; el inverso es '-'.join(lista)."),
   ("¿Por qué debes reasignar texto = texto.strip()?", ["Porque strip falla sin ella", "Los strings son inmutables: strip devuelve uno nuevo", "Por velocidad", "No hace falta"], 1, "Métodos de str NUNCA modifican el original.")]),
 ("6. Condicionales y verdad en Python", """IF/ELIF/ELSE — LA SINTAXIS LIMPIA
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  if edad >= 18:
      print("mayor")
  elif edad >= 13:
      print("adolescente")
  else:
      print("menor")

EXPRESIÓN CONDICIONAL (ternario pythónico):
  mensaje = "mayor" if edad >= 18 else "menor"

VERDAD PYTHONICA (qué vale como True/False)
  Falsy: 0, 0.0, "", [], {}, set(), None, False
  Todo lo demás es truthy → aprovecha:
  if nombre:          # existe y no está vacío
  if not lista:       # lista vacía
  while numero:       # hasta que valga 0

COMPARADORES: == != < > <= >=
CADENADOS (pythónico): 18 <= edad < 65     (rango natural)

LÓGICOS: and · or · not
  if edad >= 18 and tiene_cedula:

⚠ is vs ==: `is` compara IDENTIDAD (mismo objeto); `==` compara VALOR. Con None siempre: if x is None.""",
  [("if usuario is None — ¿por qué 'is' y no '=='?", ["Es más corto", "None es singleton: se compara identidad; además is evita métodos __eq__ raros", "== no funciona con None", "Convención sin razón"], 1, "None/True/False → is. Valores → =="),
   ("¿Qué pasa con if [0]?", ["Es truthy (lista NO vacía aunque contenga 0)", "Es falsy", "Error", "Depende"], 0, "La verdad está en la ESTRUCTURA (vacía vs no), no en el contenido.")]),
 ("7. Bucles: for, range, enumerate, while", """FOR: PRECIOSO EN PYTHON
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  for fruta in ["🍎", "🍌", "🥝"]:          # itera directo sobre elementos
      print(fruta)

RANGE (cuentas)
  range(5)         → 0,1,2,3,4
  range(1, 6)      → 1..5
  range(10, 0, -1) → cuenta regresival

ENUMERATE (índice + elemento, EL PYTHONICO)
  for i, nombre in enumerate(nombres): print(i, nombre)

WHILE (condición, no conteo)
  n = 100
  while n > 1:
      n //= 2

CONTROL: break (salir) · continue (siguiente vuelta) · else en bucles (rara útil: si NO hubo break)

COMPREHENSIONS = bucle + transformación + filtro en 1 línea:
  [len(p) for p in palabras if len(p) > 3]

REGLA: si puedes leerlo como frase en español, es pythónico. 'for numero in numeros si es par' → comprehension de ham.""",
  [("¿Qué aporta enumerate frente a range(len(lista))?", ["Nada", "Índice y elemento a la vez, legible y sin errores de off-by-one", "Más velocidad", "Desempaqueta tuplas"], 1, "enumerate es el idioma correcto; range(len()) es el acento extranjero."),
   ("range(2, 10, 2) genera...", ["2..9", "2, 4, 6, 8", "2, 4, 6, 8, 10", "Pares hasta 10 inclusive"], 1, "range(inicio, fin, paso) — fin SIEMPRE excluido.")]),
 ("8. Funciones: parámetros, return y scope", """FUNCIONES: CONTRATOS DE UNA LÍNEA
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  def area_rectangulo(base, altura):
      '''Devuelve el area.'''        # docstring: tu API documentada
      return base * altura

PARÁMETROS CON PODER
  def precio_con_iva(precio, iva=0.22):          # por defecto al FINAL
      return precio * (1 + iva)
  precio_con_iva(100)        → 122.0
  precio_con_iva(100, 0.10)  → 110.0
  precio_con_iva(iva=0.10, precio=100)   # kwargs: por nombre, orden libre

  def maximo(*numeros):                            # *args: tupla de sobrantes
      return max(numeros)
  def config(**opciones):                          # **kwargs: dict de nombrados
      print(opciones)

RETURN MULTIPLE (devuelve tupla):
  def punto(): return 10, 20
  x, y = punto()                  # desempaquetado

SCOPE: lo asignado dentro es LOCAL; leer globales funciona pero asignarlas requiere `global` (evítala; devuelve valores en su lugar).

Sin return → la función devuelve None.""",
  [("def f(a, b=2): — ¿por qué el default va al final?", ["Le gusta a Python", "Los posicionales deben venir primero para no ambiguar la llamada", "Velocidad", "No hay regla"], 1, "f(5) debe ser claro: a=5. Con default primero sería ambiguo."),
   ("Sin return, una función Python devuelve...", ["0", "cadena vacía", "None (¡cuidado al encadenar!)", "Error"], 2, "Caso clásico: olvidas return y luego el resultado es None donde no esperas.")]),
 ("9. Archivos: leer, escribir y JSON", """ARCHIVOS: PERSISTENCIA BÁSICA (Y BONITA)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
LA FRASE DE LOS PROFESIONALES: with
  with open("notas.txt", "w", encoding="utf-8") as f:
      f.write("línea 1\\nlínea 2\\n")
  with open("notas.txt", encoding="utf-8") as f:
      texto = f.read()
  with OPEN CIERRA AUTOMÁTICAMENTE aunque explote algo. SIEMPRE úsalo.

MODOS: "r" leer · "w" escribir (BORRA el anterior) · "a" agregar · "r+" ambos · "rb"/"wb" binarios
  encoding="utf-8" EXPLÍCITO siempre (evita acentos rotos entre sistemas)

JSON — el caso de uso n.º 1 real de los archivos:
  import json
  datos = {"nombre": "Ada", "temas": ["py", "js"]}
  with open("datos.json", "w", encoding="utf-8") as f:
      json.dump(datos, f),  # guardar
  with open("datos.json", encoding="utf-8") as f:
      recuperado = json.load(f)      # cargar (dict/listas)

Errores esperables: try/except FileNotFoundError alrededor del open.""",
  [("¿Por qué usar with open(...)?", ["Es más corto", "Cierra el archivo automáticamente incluso ante errores", "Acelera la lectura", "Permite binarios"], 1, "with = context manager: el recurso se libera pase lo que pase."),
   ("¿Cómo guardar y recuperar un dict en JSON?", ["write con str()", "json.dump() y json.load()", "pikcle y unpack", "print a archivo"], 1, "json es universal multiplataforma; dicts/listas pasan directo.")]),
 ("10. Errores con gracia: try/except profesional", """EXCEPCIONES: FALLAR ES NORMAL, CAPTÚRALAS CON ESTILO
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  try:
      edad = int(input("Edad: "))
      print(100 / edad)
  except ValueError:
      print("Eso no era un número")
  except ZeroDivisionError:
      print("No puedo dividir por cero")
  except FileNotFoundError as e:
      print(f"Archivo no hallado: {e}")
  except Exception as e:            # red de última instancia
      print(f"Error inesperado: {e}")
  else:
      print("Todo OK")              # corre solo si NO hubo excepción
  finally:
      conexion.close()              # SIEMPRE corre (limpieza)

REGLAS PROFESIONALES
1. Captura EXCEPCIONES ESPECÍFICAS (ValueError, no except: desnudo)
2. Fail fast en el límite (input/archivo/red); propaga hacia quién puede decidir
3. Los errores esperados (archivo perdido) → comportamiento previsible: default, reintento, mensaje
4. LANZA tú también: raise ValueError("monto debe ser positivo")

Un crash con buen mensaje > silencio con datos corruptos.""",
  [("¿Qué bloque corre SIEMPRE, haya o no excepción?", ["try", "except", "else", "finally"], 3, "finally = limpieza garantizada (cerrar archivos, conexiones)."),
   ("raise ValueError('x') sirve para...", ["Matar el programa", "Lanzar tu propio error con mensaje claro cuando detectas un estado inválido", "Imprimir errores", "Ignorar errores"], 1, "Valida pronto, falla fuerte y con mensaje: debugging agradecido.")]),
 ("11. Comprensiones avanzadas y lambda: código que se lee", """AZÚCAR PITÓNICO DE VERDAD
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
COMPREHENSIONS CON FILTRO DOBLE Y DICCIONARIOS
  resultado = {n: "par" if n % 2 == 0 else "impar" for n in range(6)}
  listas  = [[1,2],[3,4]]
  plana   = [x for sub in listas for x in sub]     → [1,2,3,4]

LAMBDA (funciones mini de UNA expresión: solo cuando claramente hace más legible)
  doble = lambda x: x * 2
  sorted(palabras, key=lambda p: len(p))           # ordenar por largo
  max(alumnos, key=lambda a: a["edad"])             # el mayor

FUNCS QUE SUSTITUYEN lambdas (stdlib siempre gana)
  from operator import itemgetter
  sorted(alumnos, key=itemgetter("edad"))           # mejor
  sum() · any() · all() · zip() · map()/filter() (pero las comprehensions ganan)

ANY/ALL — lógica declarativa:
  all(u["activo"] for u in usuarios)     # ¿todos activos?
  any("@" in e for e in emails)          # ¿alguno tiene @?

ZIP — recorrer en paralelo:
  for nombre, nota in zip(nombres, notas): ...""",
  [("all() y any() con generador hacen...", ["Loops normales", "Lógica declarativa: ¿todos/alguno cumplen? — sin bucles explícitos", "Suma de listas", "Nada útil"], 1, "all(x > 0 for x in nums) se lee como español: todos mayores a cero."),
   ("¿Cuándo usar lambda?", ["Siempre", "Funciones de una expresión triviales pasadas a key= y similares; en todo otro caso, def", "Nunca", "En clases"], 1, "Si necesita nombre para entenderse, ese nombre es su def.")]),
 ("12. Clases y objectos: modelar el mundo", """POO PITÓNICA: CLASES SENCILLAS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  class Tarea:
      def __init__(self, titulo):          # constructor
          self.titulo = titulo
          self.completada = False

      def completar(self):
          self.completada = True

      def __repr__(self):                   # print bonito
          return f"Tarea({self.titulo!r}, hecha={self.completada})"

  t = Tarea("Estudiar POO")
  t.completar()

HERENCIA (usa con moderación)
  class TareaUrgente(Tarea):
      def __init__(self, titulo, dias):
          super().__init__(titulo)          # llama al padre
          self.dias = dias

DUNDER (métodos especiales): __init__ · __repr__ · __len__ · __eq__ → tu clase se comporta como las nativas.

DATACLASS — clases que solo guardan datos (elimina boilerplate):
  from dataclasses import dataclass
  @dataclass
  class Punto:
      x: float
      y: float
  Punto(1, 2) + __repr__ + __eq__ gratis.""",
  [("¿Qué hace self en un método?", ["Decoración", "Referencia a la instancia actual: sus atributos y métodos", "Importar la clase", "Nada"], 1, "self es cómo el método sabe sobre QUÉ objeto concreto opera."),
   ("¿Qué gana @dataclass?", ["Más velocidad", "init, repr y eq automáticos para clases de datos", "Herencia", "Async"], 1, "Modelos limpios sin boilerplate: escribes los campos y todo lo demás llega gratis.")]),
 ("13. Módulos, paquetes y entornos virtuales", """ORGANIZA TU CÓDIGO COMO LOS PROFESIONALES
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
MÓDULO = un archivo .py. IMPORTA lo que necesitas:
  import math; math.sqrt(2)                    # namespace claro
  from math import sqrt; sqrt(2)               # directo
  import mis_utilidades                         # ¡tus archivos también son módulos!

PAQUETE = carpeta con __init__.py (puede estar vacío):
  proyecto/
    src/
      __init__.py
      tareas.py  (clase Tarea)
      main.py    (from tareas import Tarea — si lo corre como módulo)
  python3 -m src.main        # -m = ejecutar como módulo (los imports funcionan)

if __name__ == "__main__":   ← código que corre SOLO si ejecutas el archivo directo (no al importarlo)

ENTORNOS VIRTUALES (¡obligatorios!)
  python3 -m venv .venv && source .venv/bin/activate
  pip install requests
  pip freeze > requirements.txt

ESTRUCTURA REAL (mínima profesional): src/ + tests/ + README + requirements + .gitignore""",
  [("¿Qué protege if __name__ == '__main__'?", ["Al socket", "El código solo corre al EJECUTAR el archivo, no al importarlo", "Los tipos", "La memoria"], 1, "Permite archivos que son a la vez librería (importar) y script (correr)."),
   ("¿Por qué python3 -m src.main y no python3 src/main.py?", ["Es más corto", "Con -m, los imports relativos del paquete funcionan; con ruta directa suelen romperse", "Es lo mismo", "Es más rápido"], 1, "-m ejecuta como módulo del paquete: los from tareas import resuelven bonito.")]),
 ("14. Librería estándar: 10 joyas incluidas", """LA STDLIB: BATERÍAS INCLUIDAS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  import datetime
  hoy = datetime.date.today() · datetime.datetime.now() · (fecha - otra).days

  import random
  random.choice(lista) · random.randint(1, 6) · random.shuffle(lista) · random.sample(lista, 3)

  import json     ·  import re (regex)   ·  import os (sistema)   ·  sys (argumentos: sys.argv)

  from pathlib import Path                    # rutas MODERNAS (reemplaza os.path)
  Path.home() / "proyectos" / "notas.txt"; p.read_text(); p.exists(); p.glob("*.py")

  import requests? (externa la única: pip install requests) — http GET en una línea.

  from collections import Counter, defaultdict
  Counter("banana")                      → cuenta letras automáticamente
  defaultdict(list)                      → dict con default lista (sin KeyError)

  import statistics; statistics.mean(numeros)
  import subprocess; subprocess.run(["ls"])

REGLA DEL PROFESIONAL: antes de escribir código, busca si stdlib ya lo hace. 9 de cada 10 veces sí.""",
  [("¿Qué aporta Path de pathlib frente a strings de rutas?", ["Solo estética", "Rutas portables Windows/Linux con operadores / y métodos read_text/exists", "Velocidad", "Compresión"], 1, "p = Path.home() / 'x' funciona igual en todos los SO — el estándar moderno de Python."),
   ("Counter('banana') devuelve...", ["Una lista", "{'a': 3, 'n': 2, 'b': 1} — conteo automático", "'bn'", "Error"], 1, "collections.Counter = histograma listo con una línea.")]),
 ("15. Python para datos: tu primer análisis real", """PYTHON + DATOS: EL SUPERPODER LABORAL
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Escenario real: tienes ventas.csv:
  producto,precio,cantidad
  Café,120,3
  Pan,45,10

SIN PANDAS (stdlib pura, ENTIENDE primero esto):
  import csv
  with open("ventas.csv", encoding="utf-8") as f:
      for fila in csv.DictReader(f):                    # dicts: fila["producto"]
          print(fila["producto"], int(fila["cantidad"]))

CON PANDAS (el estándar):
  pip install pandas
  import pandas as pd
  df = pd.read_csv("ventas.csv")
  df.head()                      # primeras filas
  df["total"] = df["precio"] * df["cantidad"]      # columna calculada
  df.groupby("producto")["total"].sum()            # agrupar y sumar
  df.describe()                  # estadísticas automaticas

pandas = tablas (DataFrame) con operaciones vectorizadas: mucho más rápido y corto que loops.

MINI PROYECTO HOY: descarga cualquier CSV público (datos abiertos de tu país) y pregunta: ¿máximo, promedio, top 5?""",
  [("¿Qué hace csv.DictReader?", ["Lee JSON", "Convierte cada fila del CSV en un dict usando el encabezado como claves", "Escribe CSV", "Ordena filas"], 1, "fila['precio'] directo — parseo CSV robusto con nada instalado."),
   ("df.groupby('producto')['total'].sum() hace...", ["Filtra filas", "Agrupa por producto y suma el total de cada grupo", "Ordena por producto", "Crea tabla nueva"], 1, "El GROUP BY de SQL, estilo pandas: resumir categorías en 1 línea.")]),
 ("16. Proyecto final: tu asistente CLI personal", """CONSTRUYE: ASISTENTE CLI COMPLETO
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Requisitos (todo el curso aplicado):
1. Comandos: nota agregar/lista · tarea agregar/hecha · dado · fecha · exportar
   usando sys.argv o menú
2. Datos en notas.json y tareas.json (json.dump/load) — persistencia real
3. Clases: Nota, Tarea con dataclasses + métodos
4. Errores con try/except específicos (JSON corrupto, input inválido)
5. Fechas con datetime (mostrar "creado hace X días")
6. Formato profesional: f-strings, emojis, líneas guía
7. Módulos: main.py + modelos.py + almacenamiento.py
8. Empaquetado: venv + requirements.txt + README.md

ESTRUCTURA SUGERIDA
  mi-asistente/
    src/main.py        (menú/argparse)
    src/modelos.py     (dataclasses)
    src/datos.py       (load/save JSON)
    notas.json tareas.json (datos del usuario: en .gitignore)
    requirements.txt README.md

GRANDES IDEAS BONUS: conectar a una API (requests al clima) · exportar CSV · tabulate para tablas bonitas.

🏆 Al terminar esto SIN copiar código externo, ya piensas como desarrollador Python.""",
  [("¿Por qué separar modelos.py de main.py?", ["Obligación", "Separación de responsabilidades: clases/datos testeables solos, main solo orquesta", "Velocidad", "Estética"], 1, "Cada módulo una razón de cambio; esto es arquitectura en pequeño."),
   ("Un proyecto 'terminado' incluye además del código...", ["Un PDF", "README + requirements + tests básicos + .gitignore", "Un servidor", "Logo"], 1, "Profesional = reproducible y presentable, no solo que corra en tu máquina.")]),
],
# ═══════════════════ 9. SQL (10) ═══════════════════
"SQL y Bases de Datos — Datos que Persisten": [
 ("1. Bases de datos y SQL: el lenguaje de los datos", """SQL: HABLARLE A LOS DATOS DESDE 1974
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Base de datos = tablas relacionadas con estructura estricta. SQL = el lenguaje para consultarlas. Misma sintaxis en PostgreSQL, MySQL, SQLite...

TU PRIMERA CONSULTA
  SELECT nombre, precio FROM productos;

CONCEPTOS
• Tabla (relación): filas y columnas
• Fila = registro · Columna = atributo (con tipo: INTEGER, TEXT, NUMERIC, DATE, BOOLEAN...)
• EN VERDAD: SQLITE incluida en tu sistema: no hay nada que instalar. Esta app misma la usa.
  sqlite3 datos.db  → abre la consola sqlite (o en Python: import sqlite3)

PK (primary key): identificador único de cada fila — casi siempre id autoincremental.

SQL ES DECLARATIVO: dices QUÉ quieres ("productos caros"), no CÓMO recorrerlos. El motor se encarga de la eficiencia.""",
  [("¿Qué hace SELECT nombre, precio FROM productos?", ["Crea la tabla", "Devuelve solo esas dos columnas de la tabla productos", "Inserta datos", "Borra filas"], 1, "SELECT = leer columnas elegidas de una tabla: la consulta más básica."),
   ("¿Por qué SQLite es ideal para aprender/apps locales?", ["Es para datos simples nada más", "Zero-config: la base ES un archivo; sin servidor, incluida en Python y en todos los SO", "No soporta SQL real", "Solo Mac"], 1, "Sin instalar servidor, pero con SQL completo: perfecta para apps desktop/móvil y aprender.")]),
 ("2. SELECT con WHERE: filtrar con precisión", """FILTRAR ADULTOS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  SELECT nombre, precio
  FROM productos
  WHERE precio > 100;               -- comentario con dos guiones

OPERADORES
  = · != · > · < · >= · <=
  BETWEEN 5 AND 10          (inclusive)
  IN ('a', 'b')
  LIKE 'Ana%'               (empieza por) · '%ana' · '%ana%'
  IS NULL / IS NOT NULL     (⚠ NULL = NULL es falso; usa IS)
  AND · OR · NOT

CUIDADO CON NULL: null significa DESCONOCIDO — no es igual a nada, ni siquiera a otro null:
  WHERE edad = NULL     → siempre vacío
  WHERE edad IS NULL    → correcto

COMBINAR CON PARÉNTESIS (la precedencia anda traicionera):
  WHERE (precio > 100 OR oferta = 1) AND activo = 1;

PRÁCTICA: pon datos juguete en una tabla en tu SQLite y escribe 5 WHERE distintos. 10 minutos.""",
  [("¿Cómo verificar si un campo es NULL?", ["campo = NULL", "campo IS NULL", "campo == NULL", "NULL(campo)"], 1, "NULL no es un valor; solo IS NULL funciona — bug clásico en todo el mundo."),
   ("SELECT * FROM empleados WHERE nombre LIKE 'Ana%' busca...", ["Nombres que terminan en Ana", "Nombres que EMPIEZAN por Ana ( % = comodín de caracteres)", "Exactamente 'Ana%'", "Todo lo que no sea Ana"], 1, "% sustituye cualquier secuencia; Ana% = empieza por.")]),
 ("3. Ordenar, limitar y funciones agregadas", """SUMARIZAR Y ORDENAR
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ORDENAR
  SELECT nombre, precio FROM productos ORDER BY precio DESC;      -- ASC es defecto
  ORDER BY categoria ASC, precio DESC;                             -- varias columnas

LIMITAR (paginación)
  ORDER BY precio DESC LIMIT 5 OFFSET 10;                         -- página 3 de 5 en 5

AGREGADAS (resumen de todo el grupo)
  COUNT(*)      → cuántas filas
  COUNT(email)  → cuántas no NULAS
  SUM · AVG · MIN · MAX
  SELECT COUNT(*), AVG(precio) FROM productos;

DISTINCT (únicos)
  SELECT DISTINCT categoria FROM productos;

ALIAS (legibilidad)
  SELECT AVG(precio) AS precio_promedio FROM productos;

ARITMÉTICA EN SELECT: SELECT nombre, precio * 1.22 AS con_iva FROM productos;""",
  [("¿Qué devuelve COUNT(*)?", ["Columnas", "Número TOTAL de filas (incluyendo nulos)", "Promedio", "Suma"], 1, "COUNT(*) cuenta filas; COUNT(columna) omite las NULL."),
   ("ORDER BY precio DESC LIMIT 5 OFFSET 10 devuelve...", ["Los 5 más baratos", "Del puesto 11 al 15 en precio descendente", "Todo menos 10", "Error"], 1, "OFFSET salta las primeras N: base de la paginación de APIs y webs.")]),
 ("4. GROUP BY y HAVING: resúmenes por grupos", """GROUP BY: ANALÍTICA EN UNA LÍNEA
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Pregunta de negocio: ¿cuánto vendí por categoría?
  SELECT categoria,
         COUNT(*) AS productos,
         SUM(precio) AS total,
         AVG(precio) AS promedio
  FROM productos
  GROUP BY categoria;

LA CASCADA LÓGICA (apréndelas de memoria — confunden a todos):
  FROM → WHERE (filtra FILAS) → GROUP BY (agrupa) → HAVING (filtra GRUPOS) → SELECT → ORDER BY

HAVING: filtra tras agrupar
  GROUP BY categoria
  HAVING SUM(precio) > 1000;       -- solo categorías que venden > 1000
  HAVING COUNT(*) >= 5;

WHERE ≠ HAVING:
  WHERE descarta filas ANTES de agrupar (usa columnas crudas)
  HAVING filtra DESPUÉS (usa resultados de agregadas)

JUGADA REAL: ¿qué clientes han hecho más de 3 pedidos?
  SELECT cliente_id, COUNT(*) AS pedidos FROM pedidos
  GROUP BY cliente_id HAVING COUNT(*) > 3 ORDER BY pedidos DESC;""",
  [("¿Diferencia entre WHERE y HAVING?", ["Ninguna", "WHERE filtra filas antes de agrupar; HAVING filtra grupos después de la agregación", "HAVING es más rápido", "WHERE es para números"], 1, "Orden lógico: WHERE → GROUP BY → HAVING. El clásico de entrevistas."),
   ("¿Qué agregada debe estar en HAVING COUNT(*) >= 5?", ["Ninguna permitida", "Las agregadas (COUNT, SUM...) se vetican en HAVING tras agrupar", "Solo AVG", "Solo SUM"], 1, "HAVING vive en el mundo de los grupos; las funciones agregadas habitan ahí.")]),
 ("5. CREATE, INSERT, UPDATE, DELETE: escribir datos", """CRUD COMPLETO
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
CREAR TABLA
  CREATE TABLE productos (
      id INTEGER PRIMARY KEY AUTOINCREMENT,   -- SQLite
      nombre TEXT NOT NULL,
      precio NUMERIC CHECK (precio >= 0),
      categoria TEXT DEFAULT 'general',
      creado TEXT DEFAULT CURRENT_TIMESTAMP
  );

INSERT
  INSERT INTO productos (nombre, precio) VALUES ('Café', 120);
  INSERT INTO productos (nombre, precio) VALUES ('Pan', 45), ('Té', 80);

UPDATE — siempre con WHERE
  UPDATE productos SET precio = 110 WHERE id = 1;
⚠ UPDATE sin WHERE cambia TODA la tabla — regla 1 de un DBA.

DELETE — siempre con WHERE
  DELETE FROM productos WHERE id = 3;
⚠ DELETE sin WHERE vacía la tabla.

RESTRICCIONES (integrity gratis): NOT NULL · UNIQUE · DEFAULT · CHECK · PRIMARY KEY
La base rechaza datos inválidos aunque tu código se equivoque. Ponlas siempre: la integridad vive en la BD, no en tu app.""",
  [("¿Por qué UPDATE sin WHERE es un desastre clásico?", ["Es error de sintaxis", "Actualiza TODAS las filas de la tabla", "Es más lento", "Solo en MySQL"], 1, "Sin filtro = global: regla para la vida: escribe primero el WHERE... y después UPDATE/DELETE junto."),
   ("¿Qué gana poner NOT NULL y CHECK en CREATE TABLE?", ["Decora", "La base de datos rechaza datos inválidos aunque bugs de la app los intenten insertar", "Nada", "Velocidad de index"], 1, "La última línea de defensa de la calidad de datos está en el esquema.")]),
 ("6. Relaciones: FOREIGN KEY y primer diseño", """MODELO RELACIONAL: NORMALIZAR BIEN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Los datos se separan en entidades y se conectan por claves:

  CREATE TABLE autores (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      nombre TEXT NOT NULL UNIQUE
  );
  CREATE TABLE libros (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      titulo TEXT NOT NULL,
      autor_id INTEGER NOT NULL REFERENCES autores(id)   -- FOREIGN KEY
  );

REGLA: NO repitas datos en varias filas (nombre del autor mil veces); ponlo una vez y enlaza.

TIPOS DE RELACIÓN
• 1 a muchos: autor → libros (FK en el lado "muchos": libros.autor_id)
• muchos a muchos: estudiantes ↔ cursos → tabla intermedia:
  inscripciones(estudiante_id, curso_id, fecha, PRIMARY KEY(estudiante_id, curso_id))
• 1 a 1: user ↔ perfil (FK UNIQUE)

ON DELETE: qué pasa con los libros si borro el autor
  REFERENCES autores(id) ON DELETE CASCADE    (borrar hijos) / SET NULL / RESTRICT""",
  [("¿Dónde va la FK en una relación 1 a muchos (autor-libros)?", ["En autores", "En libros (el lado 'muchos')", "En ambos", "En una tabla aparte"], 1, "Cada libro apunta a su autor: FK en la tabla del lado N."),
   ("¿Cómo se modela muchos-a-muchos?", ["Con arrays", "Tabla intermedia con ambas FK y PK compuesta", "Duplicando datos", "No se puede"], 1, "La tabla puente (inscripciones) convierte M:N en dos relaciones 1:N.")]),
 ("7. JOINs: consultar varias tablas", """JOINS: PEGAR TABLAS POR SUS CLAVES
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
INNER JOIN (intersección): solo lo que coincide en ambas
  SELECT l.titulo, a.nombre
  FROM libros l
  JOIN autores a ON l.autor_id = a.id;

LEFT JOIN (todo el lado izquierdo, aunque falte el derecho: NULLs)
  SELECT a.nombre, COUNT(l.id) AS libros
  FROM autores a
  LEFT JOIN libros l ON l.autor_id = a.id
  GROUP BY a.nombre;
  → autores sin libros aparecen con 0 (INNER los habría escondido)

VISUALIZACIÓN RÁPIDA
• INNER: intersección (solo los emparejados)
• LEFT: todo A + lo emparejable de B (resto NULLs)
• RIGHT: al revés · FULL: todos de ambos (pocos motores)

ALIAS CORTOS (l/a): estándar profesional para legibilidad cuando hay varias tablas.

PRÁCTICA: ejecuta ambos INNERS y LEFT sobre datos de juguete y mira la diferencia. Ahí vive el 80% del entendimiento de JOINs.""",
  [("¿Qué registros incluye LEFT JOIN que INNER no?", ["Todos los de la derecha", "Los de la tabla izquierda sin coincidencia (con NULLs en la derecha)", "Duplicados", "Ninguno"], 1, "LEFT preserva el lado izquierdo completo: ideal para 'X con o sin Y'."),
   ("SELECT COUNT(l.id) con LEFT JOIN + GROUP BY autor da 0 cuando...", ["Error", "El autor no tiene libros (las NULL no se cuentan en COUNT)", "El join falló", "La tabla está vacía"], 1, "COUNT(columna) no cuenta NULLs: encaja perfecto con LEFT JOIN para conteos con cero.")]),
 ("8. Índices y transacciones: velocidad y seguridad", """ÍNDICES: DEL O(n) AL O(log n)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Sin índice, buscar email es leer TODA la tabla. Con índice, es un árbol: rapidísimo.
  CREATE INDEX idx_email ON usuarios(email);       -- UNIQUE INDEX si corresponde
  Regla práctica: indexa columnas de WHERE frecuente/JOIN. Demasiados índices frenan los INSERT.

EXPLAIN QUERY PLAN SELECT ...    ← descubre si tu consulta usa índice

TRANSACCIONES: TODO O NADA
  BEGIN;
  UPDATE cuentas SET saldo = saldo - 100 WHERE id = 1;
  UPDATE cuentas SET saldo = saldo + 100 WHERE id = 2;
  COMMIT;        -- guardar; ROLLBACK; deshacer todo

Si algo falla en el medio, ROLLBACK: la plata no aparece ni desaparece en el aire.

ACID (lo que una transacción garantiza): Atomicidad (todo/nada), Consistencia, Aislamiento (otras sesiones no ven datos a medio camino), Durabilidad (commit = disco).

EN PYTHON: con sqlite3: con = sqlite3.connect(...); con.commit() o rollback();  with con: hace commit/rollback automáticamente.""",
  [("¿Cuándo crear un índice?", ["En todas las columnas siempre", "En columnas usadas frecuentemente en WHERE/JOIN (con costo de escritura)", "Nunca", "Solo en PK"], 1, "Índices aceleran lecturas pero encarecen escrituras: sobredimensionarlos es deuda."),
   ("¿Qué garantiza una transacción bancaria (BEGIN...COMMIT)?", ["Velocidad", "Las dos actualizaciones suceden juntas o ninguna (atomicidad)", "Orden alfabético", "Backup"], 1, "Si falla a mitad, ROLLBACK: nunca hay dinero perdido en el aire.")]),
 ("9. SQL con Python: sqlite3 práctico", """PYTHON + SQLITE: DATOS REALES DESDE TU CÓDIGO
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  import sqlite3

  con = sqlite3.connect("plataforma.db")
  cur = con.cursor()

  # CRUD CON PARÁMETROS (¡la regla de oro del SQL!)
  cur.execute("INSERT INTO usuarios(nombre, edad) VALUES (?, ?)", ("Ada", 36))
  con.commit()

  cur.execute("SELECT * FROM usuarios WHERE edad > ?", (18,))
  for fila in cur.fetchall():      # fetchall → lista de tuplas
      print(fila)

  # Transacción segura con with (auto commit/rollback):
  with sqlite3.connect("plataforma.db") as con:
      con.execute("UPDATE ...")

⚠ SEGURIDAD CRÍTICA (SQL Injection):
  cur.execute(f"... WHERE nombre = '{nombre}'")     → MORTAL: el usuario escribe SQL
  cur.execute("... WHERE nombre = ?", (nombre,))    → SEGURO: la librería lo escapa

row_factory para dicts:
  con.row_factory = sqlite3.Row      → fila["nombre"] en vez de fila[1]""",
  [("¿Por qué usar ? (parámetros) y nunca f-strings en SQL?", ["Las f-strings son lentas", "Los parámetros previenen SQL injection: los datos jamás se interpretan como código", "Son más cortos", "Solo funciona con ?"], 1, "Con f-strings, un usuario malicioso escribe SQL dentro de tu consulta: el primer ataque web de la historia."),
   ("¿Qué aporta con.row_factory = sqlite3.Row?", ["Autocommit", "Acceder a las columnas POR NOMBRE (fila['nombre']) en vez de índices", "Async", "Nada"], 1, "Código legible y resistente a cambios de orden de columnas.")]),
 ("10. Diseño final: modelar una app real en SQL", """DISEÑA: BLOG COMPLETO EN SQL
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Ejercicio sombrero: esquema real con todo el curso (ejecútalo en sqlite3):

  CREATE TABLE usuarios (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      username TEXT UNIQUE NOT NULL,
      email TEXT UNIQUE NOT NULL,
      creado TEXT DEFAULT CURRENT_TIMESTAMP
  );
  CREATE TABLE posts (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      usuario_id INTEGER NOT NULL REFERENCES usuarios(id) ON DELETE CASCADE,
      titulo TEXT NOT NULL,
      cuerpo TEXT NOT NULL,
      publicado INTEGER DEFAULT 0 CHECK(publicado IN (0,1)),
      creado TEXT DEFAULT CURRENT_TIMESTAMP
  );
  CREATE TABLE comentarios (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      post_id INTEGER NOT NULL REFERENCES posts(id) ON DELETE CASCADE,
      usuario_id INTEGER NOT NULL REFERENCES usuarios(id),
      texto TEXT NOT NULL
  );
  CREATE INDEX idx_posts_usuario ON posts(usuario_id);

CONSULTA FINAL: los 5 posts con más comentarios
  SELECT p.titulo, COUNT(c.id) AS comentarios
  FROM posts p LEFT JOIN comentarios c ON c.post_id = p.id
  GROUP BY p.id ORDER BY comentarios DESC LIMIT 5;

✅ CHECKLIST DEL ESQUEMA BUENO: PKs · FKs con comportamiento ON DELETE · UNIQUE donde sea verdad · CHECKs · índices en columnas de búsqueda · nombres plural y snake_case.""",
  [("¿Por qué CASCADE en comentarios de un post borrado?", ["Velocidad", "No quedan comentarios huérfanos de posts inexistentes", "Decora", "Sumar"], 1, "La integridad referencial gestionada por la base: consistencia siempre."),
   ("¿Qué patrón se repite en todo esquema serio?", ["Todo en una tabla", "Entidades separadas + FKs + restricciones + índices en búsquedas frecuentes", "Solo JSON", "Sin PKs"], 1, "Normalización + restricciones = la base no permite corrupción de datos desde afuera.")]),
],
}
