# -*- coding: utf-8 -*-
"""Contenido B — DevOps, sistemas y lenguajes backend. Parte 2/3 (12 cursos, 68 lecciones)."""

CURSOS_MOD = {
# ═══════════════════ 10. GIT (6) ═══════════════════
"Git y GitHub — Tu Historia Nunca Se Pierde": [
 ("1. Git mental: qué es un commit", """GIT DE VERDAD: 4 IDEAS, NO 50 COMANDOS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1. SNAPSHOT: cada commit es una foto COMPLETA del proyecto (no diferencias). Cada foto apunta a su padre → línea de tiempo.
2. 3 ESTADOS: working (editas) → staging (git add: preparas el paquete) → repository (git commit: foto guardada).
3. BRANCH: un branch es solo un PUNTERO móvil a un commit. Head = dónde está parado tu "tú".
4. GUIAT BÁSICO DIARIO
  git status         → dónde estás (lo-las de cada sesión)
  git add -A         → preparar todo
  git commit -m "feat: sistema de quizzes"   → foto con mensaje
  git log --oneline --graph                  → ver la historia

MENSAJES: imperativo y corto ("agrega login", no "agregado/cambios/x"). Tu yo del martes lo agradece.

SETUP INICIAL (una vez): git config --global user.name "Tu" / user.email. Sin esto git no sabe quién eres.""",
  [("¿Qué es un commit en git?", ["Un diff de cambios", "Un snapshot completo del proyecto con puntero al commit padre", "Un archivo zip", "Un mensaje"], 1, "Cada commit = foto completa; git las deduplica internamente (objetos)."),
   ("¿Cuál es el orden del flujo básico?", ["commit → add", "editar → git add → git commit", "push → commit", "add → status"], 1, "Working → staging (add) → repo (commit). push va aparte al remoto.")]),
 ("2. Ramas: el multiverso de tu proyecto", """BRANCHES: EXPERIMENTA SIN MIEDO
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  git switch -c feature/login      # crear rama y saltar (equivale: checkout -b)
  git switch main                  # volver
  git branch                       # listar locales
  git merge feature/login          # desde main: integrar la rama
  git branch -d feature/login      # borrar rama ya integrada

MERGE sin conflicto: git avanza el puntero (fast-forward) o crea commit de merge.
CONFLICTO (mismo lugar editado en ambas ramas):
  <<<<<<< HEAD
  tu versión
  =======
  la versión de la rama
  >>>>>>> feature/login
Editas a mano, dejas lo correcto, git add, git commit. NO ES UN ERROR: es git pidiéndote decidir.

FLUJO DE TRABAJO DIARIO
1. main limpio y estable
2. rama por cada cosa nueva (feature/quiz-python, fix/bug-login)
3. trabajas, commiteas, merge, borras la rama

DISCIPLINA: ramas CORTAS (1-3 días); ramas largas = merges de terror.""",
  [("¿Qué es un merge conflict?", ["Git roto", "Dos ramas editaron las mismas líneas: git te pide elegir manualmente entre marcadores <<<<", "Un virus", "Pérdida de datos"], 1, "Los conflictos son decisiones pendientes, no errores: resuelves, add, commit."),
   ("¿Por qué ramas cortas de 1-3 días?", ["Por estética", "Cambios pequeños = conflictos raros y merges simples; la rama eterna deviene imposible de integrar", "Git tiene límite", "Es solo sugerencia"], 1, "La integración continua empieza por ramas efímeras.")]),
 ("3. Deshacer: checkout, restore, revert, reset (la tabla salvadora)", """LA MÁQUINA DEL TIEMPO — NIVEL POR NIVEL
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
¿QUÉ ROMPÍ?                  → SOLUCIÓN
Edité archivo y lo quiero original (sin commitear):
  git restore archivo.py
Preparé con add y no va:
  git restore --staged archivo.py    (saca del stage)
Un commit YA hecho es malo pero quiero conservar historia:
  git revert <hash>                   → commit nuevo que DESHACE (seguro en compartido)
Commits locales NO subidos aún, quiero borrar el último manteniendo cambios en working:
  git reset --soft HEAD~1             → vuelve, cambios siguen preparados
Borrar TODO incluido cambios (peligro):
  git restore . + git reset --hard HEAD   (¡irrecuperable!)

git stash: guarda trabajo a medias y deja limpio el stage
  git stash → trabajas en otra cosa → git stash pop

TABLA DE ORO: seguro compartido = revert · local privado = reset.
Nunca hagas reset --hard ni rebase de ramas YA SUBIDAS que otros usan.""",
  [("git revert vs git reset — ¿cuál es seguro en commits compartidos?", ["reset --hard", "revert (crea commit inverso sin reescribir la historia ya publicada)", "igual", "ninguno"], 1, "Reescribir historia compartida rompe a tus compañeros; revert es la forma polite."),
   ("git stash sirve para...", ["Borrar todo", "Apartar cambios sin commit y retomarlos luego (stash pop)", "Subir cambios", "Crear rama"], 1, "El cajón rápido: limpio el área, atiendo la urgencia, recupero lo mío.")]),
 ("4. GitHub colaboración real: PRs y forks", """TRABAJAR CON OTROS SIN PISARSE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
EL CICLO DEL PR (Pull Request)
1. git switch -c feature/quiz-IA
2. trabajas + commits
3. git push -u origin feature/quiz-IA
4. En GitHub: New Pull Request → describes QUÉ y PARA QUÉ
5. Revisión (comentarios línea por línea) → ajustas con nuevos commits (se agregan al PR)
6. Aprobado → Merge (squash suele dejar historia limpia) → borrar rama

FORK (repos ajenos/open source): tu copia en TU cuenta → clonas, trabajas, PR al original.
Ignorar repo ajeno + clone = no puedes empujar; fork primero.

REGLAS DE ETIQUETA PRO
• PR pequeño (<400 líneas revisables) · título que dice qué · descripción que dice por qué
• Revisa el PR de otros como le gustaría que revisen el tuyo: al código, no al autor
• main protegida: nadie empuja directo, todo pasa por PR con CI verde

ISSUES = discusión/trabajo pendiente; cierra con "Closes #12" en el PR.""",
  [("¿Cuál es el ciclo correcto de contribución?", ["push directo a main", "rama → commits → push → PR → revisión → merge", "fork del compañero", "mail con el código"], 1, "El PR con revisión es el corazón del trabajo en equipo moderno."),
   ("¿Cuándo necesitas hacer fork?", ["Siempre", "Cuando el repo no es tuyo/no tienes permiso de push (open source)", "Para clonar local", "Para borrar"], 1, "Fork = tu copia en tu cuenta, que permite proponer PR al original.")]),
 ("5. .gitignore, tags y limpieza: buen ciudadano del repo", """LIMPIEZA DE REPO NIVEL PRO
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
.gitignore — cosas que NUNCA van a git:
  node_modules/          # dependencias instalables
  .venv/ __pycache__/    # Python
  .env                   # SECRETOS (la regla de vida)
  dist/ build/           # compilados
  *.log .DS_Store ejecutable/

⚠ Si ya subiste un secreto: eliminarlo en un nuevo commit NO basta (queda en historia) → rota la credencial y usa git filter-repo o BFG.

TAGS (versiones)
  git tag -a v1.0 -m "primera versión estable"
  git push origin --tags
  GitHub los presenta como "Releases" con binarios adjuntos.

README.md: el escaparate. Qué hace + cómo instalar + cómo usar + screenshot. Sin README casi nadie mira tu repo.

LICENCIA: MIT (permisiva) / GPL (copyleft). Sin licencia, legalmente nadie puede usar tu código.

GitHub Actions (CI): .github/workflows/*.yml — corre tests/build en cada push automáticamente, gratis.""",
  [("¿Por qué .env va al .gitignore SIEMPRE?", ["Es pequeño", "Contiene secretos (claves, tokens) que jamás deben quedar en la historia pública", "Porque git no los soporta", "Por estilo"], 1, "Un secreto subido = filtrado para siempre, aunque lo borres después: hay que rotar la credencial."),
   ("¿Qué es un tag v1.0 en git?", ["Un archivo", "Una marca permanente sobre un commit: la forma de publicar releases/versiones", "Una rama", "Un issue"], 1, "Los tags señalan hitos estables; son referencia para despliegues.")]),
 ("6. Proyecto final: flujo completo de punta a punta", """SIMULA UN EQUIPO REAL EN 4 PASOS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PRÁCTICA INTEGRAL (30 min, hazlo desde cero)
1. Nace el repo: mkdir miniapp && cd miniapp && git init
   → app.py con una función → git add . && git commit -m "feat: hola mundo"
2. Crea repo vacío en github.com → git remote add origin ... → git push -u origin main
3. Flujo rama completa:
   git switch -c feature/despedida → añade función despedir() → commit
   git push -u origin feature/despedida → abre PR en GitHub → léetelo tú mismo como revisor
   → merge por la web → local: git switch main && git pull
4. Libera v0.1: git tag -a v0.1 -m "primera versión" && git push origin v0.1

BONUS REALISMO: vuelve a la rama, cambia la MISMA línea en main y en la rama en dos commits distintos, merge... y resuelve el conflicto a mano. Los conflictos solo se dominan viviéndolos.

SIGUIENTE: este mismo proyecto (plataforma-total) es repo git real con Actions que compilan los 3 ejecutables solos. Míralo: es un ejemplo vivo del curso.""",
  [("¿Qué hace `git pull` tras hacer merge del PR en la web?", ["Sube cambios", "Trae e integra los cambios del remoto a tu rama local", "Borra ramas", "Crea un tag"], 1, "La web integró tu PR; tu main local está vieja hasta que pullas."),
   ("¿Por qué practicar un conflicto a posta?", ["Por sufrimiento", "Ver los marcadores <<< y resolverlo a mano desmistifica el conflicto real futuro", "No hace falta", "Para romperlo"], 1, "El conflicto es mero texto a decidir: el miedo se cura con práctica.")]),
],
# ═══════════════════ 11. DOCKER (5) ═══════════════════
"Docker — 'En Mi Máquina Sí Funciona' Resuelto": [
 ("1. Docker: qué es y por qué lo necesitas", """CONTENEDORES: EMBALAJE ESTÁNDAR DE SOFTWARE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PROBLEMA: "en mi máquina sí funciona" — Python 3.11 vs 3.9, librerías distintas, configs distintas.
SOLUCIÓN: contenedor = tu app + todo su entorno exacto empaquetados en una caja estándar que corre IDÉNTICA en cualquier Linux/Windows/Mac/Servidor.

VM vs CONTENEDOR
• VM: emula hardware completo + SO completo (GB, minutos de arranque)
• Contenedor: comparte el kernel del anfitrión (MB, milisegundos, aislado así mismo)

IMAGEN vs CONTENEDOR (la confusión de todos)
• Imagen = la plantilla inmutable (la clase)
• Contenedor = instancia corriendo de la imagen (el objeto)
Una imagen, mil contenedores iguales en segundos.

INSTALAR: docker.com (Docker Desktop Win/Mac, Engine Linux). Verifica:
  docker run hello-world

LOS 5 COMANDOS DIARIOS: docker build (crear imagen) · run (ejecutar) · ps (ver corriendo) · stop · logs (qué pasó adentro)""",
  [("¿Diferencia imagen vs contenedor?", ["Son lo mismo", "Imagen = plantilla inmutable; contenedor = instancia(s) ejecutándose de ella", "El contenedor es la plantilla", "Imagen es solo para web"], 1, "Como clase vs objeto: defines la imagen una vez, lanzas contenedores a voluntad."),
   ("¿Por qué un contenedor es más liviano que una VM?", ["Usa la nube", "Comparte el kernel del SO anfitrión en vez de emular hardware y llevar SO completo", "No tiene SO", "Solo para Linux"], 1, "El aislamiento es por namespaces del kernel: sin hipervisor ni boot de SO.")]),
 ("2. Imágenes: descargar y listar", """DOCKER HUB: LA TIENDA DE CONTENEDORES
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  docker pull python:3.12-slim        # bajar imagen del registro público
  docker images                        # listar imágenes locales
  docker run -it python:3.12-slim      # correr interactiva (entra a su shell!)
  docker run -it python:3.12-slim python  # ejecuta python adentro

ETIQUETAS (:tag): python:3.12-slim · python:3.12-alpine (mínima) · latest (default, evítala en prod: no es determinista).
slim/alpine = mismos binarios, MUCHO menos MB: tu imagen de 1GB puede pesar 50MB.

CORRER UN SERVIDOR REAL (nginx) y verlo:
  docker run -d -p 8080:80 --name web nginx
  # -d = segundo plano · -p 8080:80 = tu puerto 8080 → puerto 80 del contenedor
  # abre http://localhost:8080 → ¡web servida sin instalar nginx!

  docker ps            # corriendo
  docker stop web      # parar
  docker rm web        # borrar el contenedor (la imagen queda)""",
  [("En -p 8080:80, ¿qué es cada número?", ["Dos contenedores", "Puerto DE TU MÁQUINA : puerto DEL CONTENEDOR", "CPU y memoria", "Versiones"], 1, "Mapeo de puertos: localhost:8080 → entra al contenedor en su puerto 80."),
   ("¿Por qué preferir python:3.12-slim sobre python:latest?", ["Es más nueva", "Tamaño pequeño Y versión fijada (reproducible); latest es caja sorpresa y pesa GB", "Solo por moda", "latest no funciona"], 1, "Imágenes mínimas + tag exacto = builds rápidos, seguros y deterministas.")]),
 ("3. Dockerfile: empaquetar TU app", """TU PROPIA IMAGEN: DOCKERFILE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  # Dockerfile (app Python)
  FROM python:3.12-slim
  WORKDIR /app
  COPY requirements.txt .
  RUN pip install --no-cache-dir -r requirements.txt
  COPY . .
  CMD ["python", "app.py"]

CONSTRUIR Y CORRER
  docker build -t mi-app:1.0 .
  docker run -p 8000:8000 mi-app:1.0

LAYER CACHING (por qué ese orden): cada línea crea una capa cacheada. requirements PRIMERO (cambia poco), el código al FINAL (cambia siempre) → rebuilds en segundos.

.dockerignore (igual que .gitignore): evita copiar al contexto .git, .venv, node_modules → builds rápidos.

BUENAS PRÁCTICAS ESTRELLA
1. Imagen base slim/alpine · 2. Un proceso por contenedor · 3. No metas secretos (env al correr, no en la imagen) · 4. Multi-stage si compilas (golang/node): el binario final salta a una imagen vacía de compilador.""",
  [("¿Por qué COPY requirements.txt . va ANTES de COPY . .?", ["Orden alfabético", "Cache de capas: cambiar el CÓDIGO no reinstala las dependencias (build rápido)", "Es más seguro", "Docker lo obliga"], 1, "Capas inmutables cacheadas: poner lo que menos cambia arriba maximiza reuso."),
   ("¿Qué hace CMD [\"python\", \"app.py\"]?", ["Instala python", "Define el comando por defecto al arrancar el contenedor", "Abre una shell", "Nada (comentario)"], 1, "ENTRYPOINT+CMD definen el proceso principal: un contenedor sano = un proceso.")]),
 ("4. Volúmenes, redes y docker-compose: demasiado para la vida real", """MÁS ALLÁ DEL CONTENEDOR EFÍMERO
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
DATOS QUE SOBREVIVEN: un contenedor es descartable; una BD que borra datos al reiniciarse no sirve.
  docker run -v $(pwd)/datos:/app/datos mi-app     # volumen: carpeta de tu máquina montada adentro

REDES: contenedores que hablan entre ellos por NOMBRE:
  docker network create mired
  docker run --network mired --name db postgres:16
  docker run --network mired mi-app                # la app llega a db con host "db"

DOCKER-COMPOSE: TODO EL STACK EN UN ARCHIVO (el estándar rey)
  # docker-compose.yml
  services:
    web:
      build: .
      ports: ["8000:8000"]
      environment: ["DB_URL=postgres://db/notas"]
      depends_on: [db]
    db:
      image: postgres:16
      volumes: ["pgdata:/var/lib/postgresql/data"]
      environment: ["POSTGRES_PASSWORD=dev"]
  volumes: { pgdata: {} }

  docker compose up -d      ← todo el sistema con UNA orden
  docker compose down       ← limpiar todo

Dev local con DB real, cero instalación local: por eso compose ganó.""",
  [("¿Por qué un contenedor no debe guardar datos importantes adentro?", ["No puede guardar", "Es efímero/desmontable: los datos persistentes van en volúmenes", "Por velocidad", "Solo en producción"], 1, "Contenedor descartable + volumen persistente = patrón sano."),
   ("¿Qué ventaja tiene docker compose sobre docker run largos?", ["Es más rápido", "Todo el stack (app+db+caché) versionado en un YAML: up/down con una orden", "Menos memoria", "Solo para Windows"], 1, "El stack completo se define, comparte y levanta reproduciblemente — adiós README de 40 pasos.")]),
 ("5. Proyecto: dockeriza tu app + publica", """DOCKERIZA UNA APP TUYA (HOY)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PASOS (con tu proyecto Python o Node real)
1. Dockeriza: Dockerfile base slim + WORKDIR + requirements + COPY + CMD
2. docker build -t miusuario/miapp:1.0 .
3. Corre y verifica: docker run -p 8000:8000 miusuario/miapp:1.0 → abre localhost:8000
4. Datos: si usa SQLite o archivos, monta -v para persistirlos
5. Compose: agrega app + postgres/redis de juguete aunque no lo uses → practica up -d
6. Publica en Docker Hub: docker login && docker push miusuario/miapp:1.0
   → desde OTRO ordenador/servidor: docker pull y RUN: el momento "wow" entero.

CHECKLIST DE PRODUCCIÓN
• tag con versión exacta (no latest)
• imagen <200MB si se puede (multi-stage/alpine)
• secretos por -e / .env al correr: NUNCA en la imagen (está en las capas: pública)
• healthcheck o logs claros

🎯 Con esto, el curso de Despliegue se te hace fácil: un VPS moderno corre tu app con las mismas 2 órdenes.""",
  [("¿Por qué nunca incluir secretos DENTRO de la imagen Docker?", ["La hace más lenta", "Las capas de la imagen son legibles por cualquiera que la tenga/descargue: filtras las claves", "Docker lo prohíbe", "No se puede"], 1, "Secretos al correr (-e / compose env), nunca al build: la imagen te repite."),
   ("¿Qué combina este proyecto como cierre del curso?", ["Solo docker run", "Dockerfile + build + volúmenes + compose + push al registry", "Solo Kubernetes", "Edición de imágenes"], 1, "El ciclo completo real: de tu código a imagen publicada y ejecutable en cualquier máquina.")]),
],
# ═══════════════════ 12. LINUX (6) ═══════════════════
"Linux y Terminal — El Superpoder del Dev": [
 ("1. El sistema de archivos y navegación", """EL ÁRBOL DE LINUX HACIA ADENTRO
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
TODO es un archivo a partir de /
  /home/tu_usuario      ← tu casa (~)  ·  /etc configs  ·  /var logs  ·  /usr programas

NAVEGAR
  pwd · ls -lah  (larga+ocultos+humanos) · cd ruta/relativa o /absoluta
  cd ~  ·  cd -  (anterior)  ·  cd ..
  tree            (ver estructura en árbol — instálalo)
  find . -name "*.py"        → buscar archivos por nombre
  locate archivo / which python3  → dónde está un comando

CREAR/MOVER/COPIAR/BORRAR
  mkdir -p a/b/c    (cree todo el camino)
  cp -r origen destino (-r copia carpetas) · mv (mover/renombrar) · rm -i (pregunta)

COMODINES: *.py · archivo?.txt · [abc].txt
HISTORIAL: history · Ctrl+R búsqueda · !! repetir último

TAB TAB TAB: el autocompletar es la mitad de la velocidad de un pro de terminal.""",
  [("¿Qué hace mkdir -p a/b/c?", ["Borra a/b/c", "Crea la ruta completa incluidos padres intermedios sin error", "Cambia permisos", "Mueve archivos"], 1, "Sin -p falla si 'a' no existe; con -p crea todo el camino."),
   ("rm -r lo que hace peligroso es que...", ["existe", "Linux NO tiene papelera: lo borrado por rm se fue (por eso rm -i o trash tools)", "es root", "es lento"], 1, "Cuidado con rm: la ruta / o comodines mal puestos borran todo sin preguntar.")]),
 ("2. Leer, buscar y tuberías: la filosofía Unix", """COMANDOS PEQUEÑOS, CADENAS POTENTES (|)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
LEER
  cat archivo        (todo) · less archivo (paginado, / busca, q sale) · head -20 (principio) · tail -f log (seguir EN VIVO — el que usarás en servidores)

BUSCAR EN CONTENIDO
  grep -rn "TODO" .        (recursivo con números de línea)
  grep -i error log.txt    (ignora mayúsculas)

TUBERÍAS |: la salida de uno es la entrada del siguiente — ¡ESTA ES la magia Unix!
  cat log.txt | grep ERROR | wc -l            → cuántos errores hay
  history | grep docker                       → cuándo usé docker
  ls -lh | sort -k5 -h -r                     → ordenar por tamaño

REDIRECCIÓN
  comando > salida.txt    (guardar, BORRA el archivo)
  comando >> log.txt      (AGREGAR al final: es vital distinguir)
  comando 2>&1            (mandar errores al mismo flujo)

SU Y PERMISOS
  sudo comando     → ejecutar como admin (con respeto: puede romper el sistema)""",
  [("cat log | grep ERROR | wc -l hace...", ["Muestra todo", "Cuenta las líneas del log que contienen ERROR (tuberías encadenadas)", "Borra errores", "Nada si hay error"], 1, "Filtro → contador: las tuberías componen herramientas con texto crudo."),
   ("¿Diferencia entre > y >>?", ["Ninguna", "> SOBRESCRIBE el archivo; >> AGREGA al final", ">> es para errores", "Es más rápido >>"], 1, "Confundirlos = perder archivos (factor real de incidentes).")]),
 ("3. Permisos y procesos: controlar el sistema", """QUIÉN PUEDE QUÉ + QUÉ ESTÁ CORRIENDO
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PERMISOS: -rwxr-xr--
  r(4) leer · w(2) escribir · x(1) ejecutar | dueño / grupo / otros
  chmod +x script.sh        → hacerlo ejecutable
  chmod 644 archivo         → típico para archivos (dueño rw, resto r)
  chmod 755 carpeta/script
  chown usuario:grupo archivo   → cambiar dueño (con sudo)

PROCESOS
  ps aux | grep python          → buscar procesos
  top / htop                    → monitor en vivo (q sale)
  kill <PID>                    → terminar amable (SIGTERM)
  kill -9 <PID>                 → matar a la fuerza (plan B)
  comando &                     → correr en segundo plano
  jobs · fg %1                  → traer al frente

SERVICIOS (systemd, en la mayoría de distros)
  sudo systemctl status/start/stop/enable miapp   → correr apps permanentes (musculo de servidores)""",
  [("chmod +x script.sh permite...", ["Leerlo", "Ejecutarlo directamente (bit de ejecución)", "Comprimirlo", "Imprimirlo"], 1, "Sin +x lo corres como ./script.sh solo con bash script.sh; con +x directo."),
   ("¿Cuándo usar kill -9?", ["Siempre primero", "Solo cuando kill normal (SIGTERM) falla: -9 no deja limpiar al proceso", "Para todo", "Jamás"], 1, "SIGTERM pide cortésmente cerrarse (guardar estado); SIGKILL lo aniquila sin aviso.")]),
 ("4. SSH: tu llave a cualquier servidor", """SSH: CONTROL REMOTO CIFRADO, LA HERRAMIENTA
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  ssh usuario@IP_DEL_SERVIDOR      → entras a otra máquina por terminal (así se administran TODOS los servidores linux del mundo)

LLAVES (adiós contraseñas, más seguro)
  ssh-keygen -t ed25519            → genera par: privada (~/.ssh/id_ed25519, SECRETA) pública (.pub)
  ssh-copy-id usuario@IP           → instala tu pública en el servidor
  # o manual: copia la .pub a ~/.ssh/authorized_keys del server

  Después: ssh usuario@IP entra sin contraseña. Y scp/rsync copian archivos.

COPIAR ARCHIVOS
  scp archivo.zip usuario@IP:/home/usuario/      → subir
  rsync -avz carpeta/ usuario@IP:~/destino/       → sincronizar (solo diferencias, reanudable)

CONFIGS PARA TIPOGRAFÍA CÓMODA (~/.ssh/config)
  Host miserver
      HostName 192.0.2.10
      User ubuntu
  → ssh miserver   (así de corto)

PUERTOS/CHECKS: ssh -p 2222 (puerto no estándar) · el firewall/ufw decide qué entra.""",
  [("¿Por qué llaves SSH en vez de contraseña?", ["Son más cortas", "Criptografía asimétrica: la privada nunca viaja; contraseñas por red son atacables con fuerza bruta", "Es obligatorio", "No hay diferencia"], 1, "La pública en el server + privada en tu máquina: imposible de robar por sniffing."),
   ("rsync -avz a/ usuario@IP:~/b/ se usa para...", ["Imprimir", "Sincronizar carpetas remotas eficientemente (solo cambios, comprime, reanuda)", "Chat remoto", "Ejecutar SQL"], 1, "El caballo de batalla de backups y despliegues artesanales.")]),
 ("5. Scripts Bash: automatiza tu propia vida", """BASH: TU PRIMER LENGUAJE REAL DE SERVIDOR
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  #!/bin/bash            ← shebang: qué lo ejecuta (primera línea)
  nombre="Mundo"
  echo "Hola, $nombre"   ← $ para expandir variables

  for f in *.txt; do
      echo "Procesando $f"
  done

  if [ -f config.txt ]; then
      echo "existe"
  else
      echo "no existe"
  fi

  # argumentos: $1 $ or $2 ... · "$@" todos · $# cuántos
  echo "Hola $1"

GUARDA COMO backup.sh, chmod +x, ./backup.sh

CHECKS ÚTILES: -f archivo existe·-d directorio·-z vacío·"$a" == "$b"
COMILLA DOBLA SIEMPRE en variables: echo "$f" (si tiene espacios, sin comillas EXPLOTA)

set -euo pipefail    ← al inicio: que falle el script si algo falla (scripts sanos)

EJEMPLO REAL: backup diario con fecha en el nombre:
  fecha=$(date +%F)
  tar -czf "backup-$fecha.tar.gz" ~/proyectos/
  cron: 0 3 * * * /ruta/backup.sh   (crontab -e → lo corre solo a las 3am)""",
  [("¿Por qué siempre \"comillas dobles\" en variables de bash?", ["Son bonitas", "Sin ellas, valores con espacios se rompen en múltiples argumentos (bugs y desastres)", "Van más rápido", "Solo en if"], 1, 'rm $f → rm dos cosas si f="mi archivo.txt"; rm "$f" → correcto.'),
   ("set -euo pipefail permite...", ["Depurar", "Fallar rápido y claramente: el script se detiene ante errores en vez de continuar roto", "Logs bonitos", "Correr en paralelo"], 1, "Script que sigue tras error suele causar más daño que uno que para.")]),
 ("6. Proyecto: pone tu PC a trabajar sola", """AUTOMATIZA: 3 SCRIPTS DE TU VIDA DIARIA
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SCRIPT 1 — respaldo.sh (el indispensable)
  #!/bin/bash
  set -euo pipefail
  fecha=$(date +%F)
  tar -czf "$HOME/backups/proyectos-$fecha.tar.gz" "$HOME/PlataformaTotal" ~/proyectos 2>/dev/null || true
  echo "✅ Respaldo $fecha listo"

SCRIPT 2 — limpieza.sh (espacio en disco)
  #!/bin/bash
  echo "Temporales grandes:"
  find /tmp -type f -size +50M -exec ls -lh {} \\; 2>/dev/null
  read -p "¿Borrar? (s/n) " sn
  [[ "$sn" == s ]] && find /tmp -type f -size +50M -delete && echo "🧹 limpio"

SCRIPT 3 — mi-sistema.sh (tablero rápido)
  #!/bin/bash
  echo "💾 Disco:"; df -h /
  echo "🧠 RAM:"; free -h
  echo "🔥 Top 3 procesos:"; ps aux --sort=-%mem | head -4

AUTOMÁTICO con cron (crontab -e):
  0 21 * * * $HOME/scripts/respaldo.sh >> $HOME/backups/log.txt 2>&1

🎯 La regla del dev senior: si lo haces 3 veces a mano, la 4.ª es un script.""",
  [("¿Qué ventaja tiene $fecha=$(date +%F) en el nombre del backup?", ["Ninguna", "Cada respaldo es distinto: nunca sobreescribes el de ayer", "Es obligación del sistema", "Comprime más"], 1, "Backups fechados = historia de restauración; sin fecha solo tienes una copia."),
   ("crontab -e + '0 21 * * * ./respaldo.sh' hace...", ["Nada", "Corre el respaldo automáticamente todos los días a las 21:00", "Borra cron", "Abre editor solo"], 1, "cron = programador de tareas de Unix: tu computador trabaja mientras duermes.")]),
],
# ═══════════════════ 13. DEVOPS (6) ═══════════════════
"DevOps y CI/CD — De Tu PC a Producción Sin Sudor": [
 ("1. DevOps en una frase y el pipeline", """DEVOPS: CULTURA + AUTOMATIZACIÓN DE ENTREGAR VALOR
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
En 2008 los devs escupían código y "ops" sufría en servidores. DevOps unificó: TU construyes, TU lo corres, TU lo mejoras — con tanta AUTOMATIZACIÓN en medio que el humano no interviene.

EL PIPELINE (tubería por la que pasa todo commit)
  código → BUILD (compilar) → TEST (pruebas automáticas) → DEPLOY (al servidor/usuario)
  Si algo rompe: el pipeline se detiene y te avisa. Nadie se entera del bug salvo tú.

CI (Integración Continua): cada push corre build+tests en un runner limpio (GitHub Actions, GitLab CI...)
CD (Entrega/Despliegue Continuo): si CI está verde, se publica solo (o con un botón) a staging/producción.

POR QUÉ IMPORTA A UN DEV SOLO: aunque trabajes solo, mover tu "push → producción" de 30 pasos manuales a 1 pipeline verde es el salto de amateur a profesional. Menos errores, más velocidad, menos miedo a desplegar los viernes.

「Si duele, hazlo más seguido」→ la frecuencia hace pequeños a los problemas.""",
  [("¿Qué es CI (Integración Continua)?", ["Un lenguaje", "Automatizar build+tests en cada push para detectar roturas al instante", "Un servidor", "Integración con bases de datos"], 1, "Commits integrados y probados constantemente: el bug se detecta cuando es pequeño."),
   ("¿Qué diferencia hay entre entrega y despliegue continuos?", ["Ninguna", "Entrega: listo para publicar con un clic; Despliegue: se publica AUTOMÁTICAMENTE al pasar CI", "Despliegue es más lento", "Son sinónimos legales"], 1, "Delivery = siempre desplegable (decisión humana); Deployment = se hace solo.")]),
 ("2. GitHub Actions desde cero: tu primer workflow", """ACTIONS: CI/CD GRATIS EN TU REPO
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
La estructura: .github/workflows/ci.yml

  name: CI
  on: [push, pull_request]            ← cuándo corre
  jobs:
    test:                             ← un trabajo (varios en paralelo posibles)
      runs-on: ubuntu-latest          ← runner (máquina de GitHub)
      steps:
        - uses: actions/checkout@v4            ← baja tu código
        - uses: actions/setup-python@v5
          with: { python-version: "3.12" }
        - run: pip install -r requirements.txt
        - run: python -m pytest               ← tu suite de tests

CONCEPTOS
• Workflow = el archivo; Job = paralelo aislado; Step = cada comando
• on: eventos (push, PR, cron "0 6 * * *", workflow_dispatch manual...)
• Artefactos: subir resultados (builds, binarios) descargables: actions/upload-artifact@v4

LA MAGIA: este MISMO proyecto incluye workflow que compila los ejecutables de Windows/Mac/Linux en la nube — míralo: es tu ejemplo de la vida real, no teoría.""",
  [("¿Qué hace runs-on: ubuntu-latest?", ["Es tu PC", "Define la imagen de máquina virtual limpia de GitHub que ejecutará el job", "El sistema del repo", "Nada"], 1, "Cada job arranca en una VM limpia; por eso hay que instalar dependencias en los steps."),
   ("¿Dónde debe vivir el archivo del workflow?", ["en src/", ".github/workflows/*.yml", "en la raíz", "en cualquier lado"], 1, "GitHub solo reconoce los workflows en esa ruta exacta.")]),
 ("3. Tests automáticos: el corazón del CI", """SIN TESTS NO HAY CI REAL
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
El trabajo del pipeline es responder: ¿esto sigue funcionando? Solo los tests lo responden sin humanos.

PIRÁMIDE DE TESTS
       ↑ pocos, lentos
    E2E (end-to-end: la app entera real: navegador/HTTP)
   Integración (varios módulos juntos: API + BD)
  Unitarias (muchísimas, rapidísimas: funciones aisladas)
       ↓ muchas, rápidas, baratas

PYTEST MÍNIMO (Python)
  # test_math.py
  def sumar(a, b): return a + b
  def test_sumar(): assert sumar(2, 3) == 5
  pip install pytest ; pytest    → busca test_*.py y corre solo

NODE: node --test nativo o vitest/jest
  test("suma", () => expect(sumar(2,3)).toBe(5));

REGLAS DE ORO
1. Los tests NO tocan servicios externos (usa mocks) → rápidos y confiables
2. Test que a veces falla = peor que ningún test (se ignora)
3. En CI: si un test falla ✗, el pipeline corta y NO se despliega""",
  [("¿Por qué la pirámide tiene más tests unitarios que E2E?", ["Es bonita", "Unitarios = rápidos, estables y baratos; E2E = lentos, frágiles y caros (manténlos pocos)", "Unitarios son nuevos", "Es convenio"], 1, "La base ancha de unit tests cubre lógica; los pocos E2E verifican el cableado."),
   ("¿Qué debe evitar un test unitario?", ["assert", "Tocar red/BD/reloj reales (úsese mocks/fakes) para ser rápido, repetible y confiable", "Ejecutarse en CI", "Tener nombre test_"], 1, "Un test que depende del internet es un test que fallará a las 3am cuando menos lo esperas.")]),
 ("4. Despliegue continuo y entornos", """ENTORNOS: DEV → STAGING → PROD
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Nunca tejes en prod directo. La cadena:
• DEV: tu máquina, rompe sin culpa
• STAGING: réplica de producción para validar (¡misma rama de Docker!)
• PROD: donde vive el usuario real

ESTRATEGIAS DE DESPLIEGUE (de simple a pro)
1. Push directo (hobby): git push → VPS corre git pull + restart
2. Docker compose up en el VPS (simple y sanito)
3. Rolling/Railway/Fly/Render: plataforma que agarra tu Dockerfile y se encarga
4. Blue-Green/Canary (empresas): nueva versión recibe 5% del tráfico primero

VARIABLES DE ENTORNO POR AMBIENTE: misma app/imagen, distinta config (DB dev vs prod) — por eso nunca hardcodeas config: la 12-factor app.

ROLLBACK: cuana algo falla, vuelves rápido. Docker hace esto trivial: la imagen anterior SIGUE ahí: corre la versión vieja otra vez y listo.

CHECKLIST DEPLOY PM: healthcheck endpoint · logs accesibles · rollback practicado · variables de prod seteadas · alertas básicas""",
  [("¿Para qué existe staging?", ["Cuestión litúrgica", "Ambiente IDÉNTICO a producción donde validar antes del deploy real", "Para guardar código", "Para tests unitarios"], 1, "Los bugs 'solo-pasan-en-prod' se atrapan en staging."),
   ("¿Qué regala Docker al momento de rollback?", ["Nada", "La versión anterior sigue como imagen: vuelves a correr esa y listo, sin reinstalar", "Más CPU", "Backups de BD"], 1, "Inmutabilidad de imágenes = tiempo de restauración en segundos.")]),
 ("5. Monitoreo y logs: saber cuando tu app llora", """OBSERVABILIDAD: DEL 'SÍ FUNCIONA' AL 'SÉ CÓMO VA'
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Los 3 pilares:
1. LOGS: qué pasó. Escribe logs estructurados (nivel, timestamp, mensaje).
   docker logs -f contenedor · journalctl -u miapp -f (systemd)
2. MÉTRICAS: cuántas requests/seg, errores %, latencia p95, RAM/CPU.
3. TRACES: recorrido de una petición a través de tu sistema (en micro-servicios).

LOGGING BIEN HECHO (reglas)
• Niveles: DEBUG (desarrollo) → INFO (eventos normales) → WARNING (rarito) → ERROR (fallo)
• JSON structured logs: máquinas los filtran (jq), humanos los leen
• NO loguees secretos ni datos personales (GDPR/sentido común)
• Con timestamp siempre: "ERROR 2026-09-18T13:44 disc-quota"

HERAMIENTAS pro gratuitas para practicar (ojo pesar): Grafana + Prometheus (métricas), Loki (logs), Uptime Kuma (¿sigue arriba?).

Empieza por lo simple: logs claros + un /health endpoint + Uptime Kuma revisando que responde 200 cada minuto. Ya duermes mejor.""",
  [("¿Qué niveles correctos de logs distinguen?", ["Solo print", "DEBUG/INFO/WARNING/ERROR — filtras según la gravedad y el ambiente", "Rojo/verde", "único nivel"], 1, "En prod corre INFO+; en dev activas DEBUG. El ruido bien dosificado vale oro."),
   ("¿Qué verifica un endpoint /health?", ["La base de datos sola", "Que la aplicación responde (200) — monitores externos lo sondean periódicamente", "Los tests", "La red"], 1, "Healthcheck es el '¿sigues viva?' de toda app desplegada: bases de alertas.")]),
 ("6. Proyecto: pipeline CI/CD real para tu app", """TU PIPELINE DE VERDAD (HOY, en ~5 pasos)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
CONTEXTO: ya tienes app + Dockerfile + tests básicos.

1. CREA .github/workflows/ci.yml:
   - trigger: en push y PR
   - job test: checkout → setup-python → pip install -r requirements.txt → pytest
2. Agrega aunque sea 3 tests unitarios reales a tu app
3. Push: abre repo → pestaña Actions → mira tu CI correr verde. ROMPE un test a propósito → push → rojo. Arréglalo → verde otra vez (esa sensación ES DevOps)
4. Job BUILD: pyinstaller o docker build → upload-artifact → tienes binarios descargables en la pestaña Actions
5. DESPLIEGUE (elije uno):
   a. Tu IRL: Railway/Fly.io/Render: conecta el repo → ellos corren tu Dockerfile tras cada push (despliegue continuo gratis/tier free)
   b. Tu VPS: workflow ssh/rsync + docker compose up -d tras CI verde

LOGRO TOTAL: push a main → tests → imagen → tu app actualizada sola en internet.
Con eso VIVISTE el ciclo que usan los equipos profesionales a diario. Bienvenido.""",
  [("¿Por qué romper un test a propósito en el proyecto?", ["Por diversión", "Verificar que el pipeline REALMENTE falla ante errores (red validate que CI funciona)", "Para practicar git", "No tiene sentido"], 1, "Un CI que nunca has visto fallar no es garantía: red/verde/red lo prueba."),
   ("¿Qué diferencia el despliegue continuo del push manual a un VPS?", ["El precio", "Todo paso manual se automatiza: tras CI verde la app llega sola al usuario, sin intervención humana", "Nada cambia", "Es solo para grandes empresas"], 1, "La ausencia de pasos manuales es la ausencia de errores manuales.")]),
],
# ═══════════════════ 14. DESPLIEGUE (6) ═══════════════════
"Despliegue y Servidores — Tu App al Mundo": [
 ("1. Dónde puede vivir tu app: el menú de opciones", """OPCIONES DE HOSPEDAJE 2026
━━━━━━━━━━━━━━━━━━━━━━━━━━━
ESTÁTICO (HTML/CSS/JS, SPAs compiladas — gratis y global):
• GitHub Pages (directo de tu repo) · Netlify · Vercel (arrastras la carpeta, dominio + HTTPS gratis)
FULL-STACK (backend/APIs):
• PaaS (Railway, Fly.io, Render, Heroku): das tu repo/Dockerfile, ellos todo lo demás (free tier para practicar)
• VPS (Hetzner, DigitalOcean ~$5/mes): TU máquina Linux, aprendes "de verdad"
• Cloud pro (AWS/GCP/Azure): para cuando seas grande

DOMINIO PROPIO (~$12/año en Namecheap/Porkbun):
  app.tudominio.com → CNAME o A la IP del servidor
HTTPS gratis: Let's Encrypt (Caddy/certbot lo automatiza) — obligatorio en 2026.

PARA APRENDER, EL ORDEN IDEAL
1. Estático con GitHub Pages/Netlify (5 minutos, emociona)
2. Full-stack en Railway/Render (10 minutos, tu primera API viva)
3. Un VPS propio (fin de semana: aprenderás más que un curso entero)""",
  [("¿Cuál es la forma MÁS rápida de publicar una web estática hoy?", ["Comprar un VPS", "GitHub Pages / Netlify: arrastrar la carpeta o conectar el repo, gratis con HTTPS", "AWS", "IIS"], 1, "El hoy: no necesitas ni servidor: tu carpeta ya es una web mundial."),
   ("¿Qué diferencia un VPS de un PaaS?", ["Precio solamente", "VPS = tú administras todo (más control y aprendizaje); PaaS = ellos administran, tú solo das el código (menos fricción)", "El VPS es la nube", "Son iguales"], 1, "Elige VPS para APRENDER sistemas; PaaS para enfocarte en producto.")]),
 ("2. Nginx y reverse proxy: el portero de tu servidor", """NGINX: LA PUERTA DE ENTRADA
━━━━━━━━━━━━━━━━━━━━━━━━━━━
  /etc/nginx/sites-available/miapp:
  server {
      listen 80;
      server_name tudominio.com;
      location / {
          proxy_pass http://localhost:8000;        ← tu app Node/Python interna
          proxy_set_header Host $host;
      }
  }
  sudo nginx -t && sudo systemctl reload nginx

¿POR QUÉ NO EXPONER LA APP DIRECTO?
• Nginx sirve archivos estáticos (css/js/imágenes) SIN tocar tu app: veloz
• Un punto para HTTPS, límites de rate, cabeceras de seguridad
• Varios apps en un servidor: app1.dominio.com → :8000, app2 → :8001 (un solo 80/443 público)

HTTPS AUTOMÁTICO
  sudo certbot --nginx -d tudominio.com   (Let's Encrypt: certificado gratis, se renueva solo)

CADDY es alternativa moderna: HTTPS automático de salida, config de 3 líneas.""",
  [("¿Qué hace proxy_pass http://localhost:8000?", ["Borra peticiones", "Nginx recibe en el 80 público y reenvía internamente a tu app en :8000", "Sube archivos", "Cierra el puerto"], 1, "Reverse proxy: un solo punto público, muchas apps atrás."),
   ("¿Por qué es estándar que la app corra en 127.0.0.1:8000 y no exponga su puerto?", ["Es más rápido", "Control y seguridad: solo Nginx habla con el mundo; aplica HTTPS, límites y cabeceras en un solo sitio", "Porque sí", "Legal"], 1, "El perímetro en un punto único de control es higiene de seguridad básica.")]),
 ("3. Mantener tu app viva: systemd, pm2 y reinicios", """PROCESOS QUE NO MUEREN (TRANQUILAMENTE)
━━━━━━━━━━━━━━━━━━━━━━━━━━━
Cerrar la terminal no mataba tu app? Ahí entra el gestor de procesos.

SYSTEMD (nativo, universal en Linux — recomendado)
  /etc/systemd/system/miapp.service:
  [Unit]
  Description=Mi app
  After=network.target
  [Service]
  ExecStart=/usr/bin/node /home/ubuntu/app/index.js
  WorkingDirectory=/home/ubuntu/app
  Restart=always                      ← si muere, resucita solo
  RestartSec=3
  Environment=NODE_ENV=production
  [Install]
  WantedBy=multi-user.target

  sudo systemctl enable --now miapp   ← inicia ahora y en cada boot
  journalctl -u miapp -f              ← sus logs en vivo

PM2 (alternativa node, con dashboard bonito): pm2 start index.js --name app && pm2 save && pm2 startup
DOCKERers: docker run --restart unless-stopped (el mismo concepto, modo contenedor)

CHECKLIST REANIMACIÓN: reinicio ante caída ✓ reinicio al boot ✓ logs persistentes ✓""",
  [("¿Qué hace Restart=always en systemd?", ["Arranca lento", "Si el proceso muere, systemd lo vuelve a levantar automáticamente", "Recarga config", "Nada importante"], 1, "Con enable (boot) + Restart, tu app sobrevive cuelgues Y reboots sin tocarte el dedo."),
   ("¿Por qué un proceso 'detached' no basta para producción?", ["Sí basta", "Un pipeline nohup se pierde en reboots y caídas no planificadas; systemd/pm2 vigilan y resucitan", "Es igual", "Financiero"], 1, "La supervisor de procesos es la diferencia entre hobby y servicio confiable.")]),
 ("4. Bases de datos en producción: presupuesto mínimo de seriedad", """DATOS EN PROD: ALGUNOS PRECEPTOS DUROS
━━━━━━━━━━━━━━━━━━━━━━━━━━━
DONDE PONER LA BD
• Hobby/practicar: SQLite en volumen persistente funciona PERFECTO (miles de apps reales la usan)
• Apps mayores: PostgreSQL (administrada si prefieres no sudarte: Neon/AWS RDS/Supabase; o en tu VPS en Docker con volumen)

REGLAS NO NEGOCIABLES
1. BACKUPS AUTOMÁTICOS, PROBADOS (un backup no restaurado no es backup)
     pg_dump miapp | gzip > backup-$(date +%F).sql.gz    (cron diario)
2. La BD NO se expone al internet público: bind a localhost o red privada, siempre
3. Usuarios con privilegios MÍNIMOS: tu app no usa el usuario root/postgres
4. Contraseña fuerte y EN VARIABLES DE ENTORNO (nunca en el código)
5. SSL/TLS si atraviesa redes (proveedores gestionados lo incluyen)

FIREWALL — la ley del mínimo:
  sudo ufw allow OpenSSH && sudo ufw allow 'Nginx Full' && sudo ufw enable
  (solo 22 y 80/443 abiertos. La BD queda inaccesible desde fuera. Así debe ser.)""",
  [("¿Por qué la base de datos NUNCA se expone directamente a internet?", ["Por costo", "Ataques automáticos la encontrarían en horas; debe escuchar solo localhost/red interna", "Por latencia", "Está bien exponerla"], 1, "Postgres/MySQL abiertos al mundo topan scanners a los minutos: firewall + bind local o red privada."),
   ("¿Qué es un backup 'probado'?", ["Está comprimido", "Que REALMENTE restauraste alguna vez y verificaste que funciona", "Automático", "Está en la nube"], 1, "Sin undrill de restauración periodic, el backup puede estar corrupto sin que lo sepas.")]),
 ("5. GitHub Pages y Netlify: tu estática en 5 minutos", """PUBLICA TU PRIMERA WEB HOY MISMO
━━━━━━━━━━━━━━━━━━━━━━━━━━━
A) GITHUB PAGES (desde tu repo)
1. Repo con index.html en la raíz
2. Settings → Pages → Source: "Deploy from a branch" → main / root
3. 1-2 minutos: https://tuusuario.github.io/turepo/
   Dominio propio: pestaña Pages → Custom domain + CNAME en tu registrador.

B) NETLIFY (aún más magia)
   Arrastra tu carpeta al panel de netlify.com → URL instantánea con HTTPS.
   O conecta GitHub: cada git push republica solo (¡CI/CD de regalo!).
   Formularios gratis sin backend; build command si usas Vite/React: npm run build, publish: dist.

REACT/VITE EN PÁGINA ESTÁTICA
  npm run build → genera carpeta dist de puro estático → esa sube (no el código fuente).
  En GitHub Pages con pakage.json puedes usar workflow para build automático.

DOMINIO propio entre todas: CNAME para www/dominio secundario; A/ALIAS a la IP para el raíz. Propagación: minutos a horas (paciencia).""",
  [("¿Qué se sube al hosting estático cuando usas React con Vite?", ["src/", "La carpeta dist/ generada por npm run build (HTMl/CSS/JS puro)", "node_modules/", "package.json"], 1, "El navegador no entiende JSX/TS: el build los compila a estático; eso es lo que se publica."),
   ("¿Qué añade Netlify sobre un hosting de archivos normal?", ["Java", "Deploy por git push automático + vistas previas por PR + formularios y HTTPS incluidos", "Base de datos", "SSH"], 1, "Joncy: conectas el repo una vez; cada push redeploya — de hecho tu ya tubiste CD.")]),
 ("6. Proyecto final: tu app COMPLETA en internet con dominio", """LA GRAN FINAL: DE CERO A URL PÚBLICA
━━━━━━━━━━━━━━━━━━━━━━━━━━━
LISTA DE MISIÓN (operativa, ~90 min, vale 1 curso entero)
1. App lista (backend con Dockerfile o web estática dist/)
2. ELIGE CAMINO:
   A) Estática → Netlify/GitHub Pages (ya la tienes en 5 min)
   B) Backend → Railway/Render (conecta repo → detecta Dockerfile → URL pública automática)
   C) VPS (el épico): Hetzner/DO ~$5 → ssh → docker compose up → nginx + certbot
3. DOMINIO: compra uno barato → registro A/CNAME a tu hosting → espera propagación
4. HTTPS: Caddy o certbot --nginx (confirmar candado verde en el navegador)
5. VARIABLES de producción seteadas (DB url, secrets) en el panel de tu proveedor
6. MONITOREO: Uptime Kuma propio o servicio simple que pida tu /health

EJERCICIO CLAVE: mándale el link a un amigo. "https://miapp.midominio.com funciona" = ya eres DevOps practicante en formación.

DOCUMENTA en el README: screenshot + URL + stack usado. Tu portafolio quedó completo: código (GitHub) + app viva (dominio) + pipeline (Actions verde).""",
  [("¿Qué verifica que realmente desplegaste bien?", ["Que corre local", "URL pública + HTTPS (candado) + datos persistiendo + se mantiene tras reinicios", "Compilar", "1 test verde"], 1, "Accesibilidad real desde afuera, seguridad básica y persistencia: la trifecta del deploy."),
   ("¿Por qué documentar el despliegue en el README del proyecto?", ["Es bonito", "URL viva en tu portafolio es la prueba '#1 para recruiters: cualquiera entra y ve tu trabajo andando", "Google lo pide", "SEO del repo"], 1, "El link que demuestra es infinitamente más persuasivo que la descripción.")]),
],
# ═══════════════════ 15. PHP Y LARAVEL (6) ═══════════════════
"PHP y Laravel — El Backend Que Alimenta la Web": [
 ("1. PHP: el gigante subestimado", """PHP: 25 AÑOS ALIMENTANDO LA WEB REAL
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

PHP 8 MODERNO: tipos : string / int en params y returns (zig: eh, mejor que nada), nullsafe ?->, JIT. La broma "PHP es malo" quedó congelada en 2010.""",
  [("¿Cómo se declara una variable en PHP?", ["let x", "$x = valor (el $ es obligatorio en cada variable)", "var x", "def x"], 1, "El $ marca variables — parece raro y luego te acostumbras."),
   ("¿Qué es un array asociativo en PHP?", ["Un número", "El equivalente a dict/hash: clave=>valor ['nombre'=>'Ada']", "Una clase", "SQL"], 1, "El tipo multiuso de PHP: lista y diccionario en uno.")]),
 ("2. Formularios y superglobales: PHP recibe datos", """$_GET, $_POST, $_FILES: EL PAN DE CADA DÍA
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

SESIONES: session_start(); $_SESSION["usuario_id"]=42; → recordar sesión entre páginas.""",
  [("¿Qué hace htmlentities($texto) antes de un echo?", ["Nada útil", "Escapa <script> etc. evitando XSS: HTML inyectado queda como texto inofensivo", "Formatea bonito", "Valida email"], 1, "La regla de vida PHP: toda salida con datos del usuario pasa por escaping."),
   ('$_POST["email"] ?? "" significa...', ["Error", "Si no viene email, usa '' (null coalescing ?? en vez de undefined/index notice)", "Comparar", "Sumar"], 1, "?? evita avisos por índices faltantes — desde PHP 7 la forma elegante.")]),
 ("3. PDO: bases de datos sin inyección", """PDO: SQL SEGURO EN PHP
━━━━━━━━━━━━━━━━━━━━━━━━━━━
  $pdo = new PDO("sqlite:".__DIR__."/datos.db");
  $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

CREAR Y ESCRIBIR (prepared: USA SIEMPRE)
  $pdo->exec("CREATE TABLE IF NOT EXISTS tareas(id INTEGER PRIMARY KEY, titulo TEXT)");
  $stmt = $pdo->prepare("INSERT INTO tareas(titulo) VALUES (?)");
  $stmt->execute([$_POST["titulo"]]);           // los datos VAN SEPARADOS del SQL

LEER (fetch asociativo, EL dict php)
  $stmt = $pdo->prepare("SELECT * FROM tareas WHERE id = ?");
  $stmt->execute([$id]);
  $tarea = $stmt->fetch(PDO::FETCH_ASSOC);     // ['id'=>1,'titulo'=>'x']
  $todas = $pdo->query("SELECT * FROM tareas")->fetchAll(PDO::FETCH_ASSOC);

REGLA DE ORO DE NUEVO:
  "... VALUES ('".$_POST['x']."')"     → ☠ SQL INJECTION (¡el clásico de los clásicos!)
  prepare + execute                  → seguro por diseño

PDO misma API para SQLite/MySQL/PostgreSQL — cambias una línea al crecer.""",
  [("¿Qué protegen los prepared statements?", ["La velocidad", "SQL injection: los datos van apartados del SQL y nunca se interpretan como código", "El código PHP", "La memoria"], 1, "prepare() separa instrucción de datos: ' OR 1=1 -- queda como simple texto."),
   ("¿Qué PDO::FETCH_ASSOC devuelve?", ["XML", "Cada fila como array asociativo ['columna'=>valor]", "Objetos siempre", "CSV"], 1, "Acceso por nombre de columna: código legible y resiliente.")]),
 ("4. Laravel: el framework que enamora", """LARAVEL: PHP PREMIUM
━━━━━━━━━━━━━━━━━━━━━━━━━━━
El framework más amado de PHP. Elegancia + convenciones. Instalación con Composer (el npm de PHP):
  composer create-project laravel/laravel miapp
  cd miapp && php artisan serve          → en localhost:8000 tu app viva

LA ESTRUCTURA (rutas → controladores → modelos → vistas Blade)
  routes/web.php:
  Route::get("/hola", fn() => "¡Hola desde Laravel!");
  Route::get("/tareas", [TareaController::class, "index"]);

ELOQUENT ORM — datos que se sienten como objetos:
  $tareas = Tarea::all();                          // SELECT *
  $tarea = Tarea::where("hecha", false)->get();    // filtrado
  $t = new Tarea(["titulo" => "Estudiar"]); $t->save();
  Tarea::find($id)->update(["hecha" => true]);

  Migraciones (esquema versionado en código): php artisan make:migration crear_tabla_tareas

BLADE (vistas con superpoderes):
  @foreach ($tareas as $t) <li>{{ $t->titulo }}</li> @endforeach
  {{ $titulo }} imprime ESCAPADO autop (XSS defendida de fábrica)

artisan = tu varita: php artisan make:model Tarea -mcr (modelo+migración+controller de golpe)""",
  [("¿Qué es Eloquent?", ["Un lenguaje", "El ORM de Laravel: cada tabla es un Modelo y trabajas datos como objetos php (save, where, all)", "Un motor de vistas", "Una BD"], 1, "Eloquent convierte SQL en interacción con objetos: Tarea::where('hecha', false)->get()."),
   ("¿Qué incluye la sintaxis {{ $x }} en Blade que la hace segura?", ["Nada", "Escapa HTML automáticamente (anti-XSS por defecto)", "Español", "SQL"], 1, "{!! !!} imprime crudo e inseguro; {{ }} es lo normal y escapeado.")]),
 ("5. MVC en Laravel: flujo completo de una petición", """DE URL A RESPUESTA: EL CAMINO LARAVEL
━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Route::get("/tareas/{id}", [TareaController::class, "show"]);

  // app/Http/Controllers/TareaController.php
  class TareaController extends Controller {
      public function show(Tarea $tarea) {        // Model Binding: si no existe id → 404 auto
          return view("tareas.show", ["tarea" => $tarea]);
      }
      public function store(Request $request) {
          $datos = $request->validate([            // validación de una línea, robusta
              "titulo" => "required|string|max:140"
          ]);
          Tarea::create($datos);                   // (requiere fillable en el modelo)
          return redirect("/tareas")->with("ok", "¡Creada!");
      }
  }

  // resources/views/tareas/show.blade.php
  <h1>{{ $tarea->titulo }}</h1>

PROTECCIÓN MASS ASSIGNMENT: en el modelo declara qué campos se pueden llenar masivamente:
  protected $fillable = ["titulo"];      // evita que un POST malicioso te pase "es_admin"

VALIDATION EN ESPAÑOL MENTAL: required|email|min:8|max:255|unique:tareas,titulo|numeric...

EL FLUJO VISUAL: petición → Route → (optional middleware auth) → Controller (valida) → Model (datos) → View (presenta) → respuesta. Una separación clara = mantenimiento feliz.""",
  [("¿Qué hace Route Model Binding en Laravel?", ["Nada especial", "Inyecta directo el modelo por ID (404 automático si no existe) sin hacer find manual", "Valida forms", "Sirve estáticos"], 1, 'function show(Tarea $tarea) — el framework busca el id y te da el modelo o 404.'),
   ("¿Para qué sirve \\$fillable en el modelo?", ["Indexar", "Anti mass-assignment: lista blanca de campos rellenables vía create/update (evita inyectar campos no previstos)", "Migraciones", "Nada"], 1, "Tarea::create($request->all()) protegido: solo pasa lo autorizado.")]),
 ("6. Proyecto: CRUD completo en Laravel", """CONSTRUYE: MINI-BLOG LARAVEL EN ~1 HORA
━━━━━━━━━━━━━━━━━━━━━━━━━━━
1. composer create-project laravel/laravel miniblog && cd miniblog
2. Configura .env (usa SQLite: DB_CONNECTION=sqlite, crea database/database.sqlite)
3. php artisan make:model Post -mcr        (modelo + migración + controller resource)
4. En la migración: $table->string("titulo"); $table->text("cuerpo"); $table->boolean("publicado")->default(false);
   php artisan migrate
5. En routes/web.php: Route::resource("posts", PostController::class);
   (Esto genera index/create/show/edit/store/update/destroy de regalo)
6. En el modelo: protected $fillable = ["titulo", "cuerpo", "publicado"];
7. En el controller: validación en store() y update():
   $request->validate(["titulo"=>"required|max:120", "cuerpo"=>"required"]);
8. Las vistas Blade (resources/views/posts/): formulario + tabla de lista con @foreach + @csrf en el form
9. php artisan serve → http://localhost:8000/posts → ¡CRUD comppleto!

ENTENDIMIENTO CLAVE: si recorriste ruta→controller→migración→modelo→vista y EXPLICAS cada pieza, entendiste Laravel más que la mitad de los que lo usan por inercia.""",
  [("¿Qué genera Route::resource()", ["Nada", "Las 7 rutas CRUD convencionales (index/create/store/show/edit/update/destroy) de golpe", "Vistas", "Un servidor"], 1, "Convención sobre configuración: Laravel asume la estructura estándar de recursos REST."),
   ("¿Qué pone el @csrf dentro del <form> de Blade?", ["CSS", "Un token anti-CSRF oculto — todo POST sin token es rechazado por Laravel", "JavaScript", "SQL"], 1, "CSRF protection integrada: solo formularios nacidos en tu app pueden postear.")]),
],
# ═══════════════════ 16. RUBY ON RAILS (5) ═══════════════════
"Ruby on Rails — La Felicidad del Desarrollador": [
 ("1. Ruby: el lenguaje diseñado para ser feliz", """RUBY: ELEGANCIA LEGIBLE EN TODO
━━━━━━━━━━━━━━━━━━━━━━━━━━━
Filosofía: la productividad del programador primero. Lee como inglés razonable.

  nombre = "Ada"                    # sin punto y coma, sin declarar tipo
  puts "Hola, #{nombre}"            # interpolación con #{}
  5.times { puts "¡ruby!" }          # bloques en TODO: ¿no es hermoso?

  # todo es objeto:
  "hola".upcase
  [1, 2, 3].map { |n| n * 10 }       # → [10, 20, 30]
  {nombre: "ada", edad: 36}.each { |k, v| puts k }

  def area(base, altura)             # return implícito: lo último se devuelve
    base * altura
  end

SIMBOLOS: son strings livianos para identificadores: :nombre (los verás por todos lados en Rails).
CONDICIONALES: if/elsif/else/end · unless es "if not" pythónico: puts "ok" unless errores.any?

JUGAR: ruby -v · irb (REPL interactivo: experimenta ahí) · ruby hola.rb""",
  [("¿Cómo interpola cadenas Ruby?", ["${}", '"#{variable}" dentro de comillas dobles', "f''", "sprintf"], 1, "#{} solo en comillas dobles — distinción que bugs de novato llenan."),
   ("¿Qué devuelve un método Ruby sin return?", ["nil siempre", "La última expresión evaluada (return implícito)", "Error", "0"], 1, '"Lo último se devuelve" — por eso casi no verás return en Ruby idiomático.')]),
 ("2. Rails: convención sobre configuración", """RAILS EN 5 COMANDOS (LA MAGIA)
━━━━━━━━━━━━━━━━━━━━━━━━━━━
  rails new miblog --database=sqlite3
  cd miblog
  rails generate scaffold Post titulo:string cuerpo:text publicado:boolean
  rails db:migrate
  rails server                       ← localhost:3000/posts YA funciona CRUD completo

Scaffold generó: modelo + migración + controlador + rutas + vistas HTML para todo el CRUD. Minutos.

CONVENTION OVER CONFIGURATION — la idea nuclear
Rails decide por ti el 90%: tabla posts = modelo Post; controlador PostsController; /posts → index...
Tú solo defines lo ORIGINAL de tu app. Menos decisiones, más producto.

RAILS CONSOLE: rails console → Post.create(titulo: "Hola") → Post.count → juegas con la BD real.
ActiveRecord (ORM) = primo de Eloquent: Post.where(publicado: true).order(created_at: :desc)

FLUJO MVC: rutas (config/routes.rb) → controlador (app/controllers) → modelo (app/models) → vista ERB (app/views).
resources :posts en routes = las 7 rutas REST de regalo (como en Laravel).""",
  [("¿Qué es el 'scaffold' de Rails?", ["Una gema", "Generador del CRUD completo (modelo, migración, controller, vistas, rutas) desde una consola", "Un servidor", "Testing"], 1, "Ideal para aprender el MVC viendo todas las piezas en acción y de una vez."),
   ("¿Qué significa Convention over Configuration?", ["Ignora convenciones", "El framework asume estándares sensatos (Post↔posts, id PK...) y tú solo configuras lo distinto", "No hay convenciones", "Toca YAML"], 1, "CoC = menos decisiones triviales = velocidad de desarrollo enorme.")]),
 ("3. ActiveRecord: tu base de datos con sabor Ruby", """ACTIVERECORD: LA GRAMÁTICA DE DATOS DE RAILS
━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Post.create(titulo: "Hola Rails", cuerpo: "...")   # INSERT
  Post.all                                            # SELECT *
  Post.find(1)                                        # por id o lanza error
  Post.find_by(publicado: true)                       # el primero
  Post.where("creado > ?", 1.week.ago)               # filtrado con params seguros
  Post.where(publicado: true).order(titulo: :asc).limit(10)
  p = Post.find(1); p.update(publicado: true)         # UPDATE
  p.destroy                                           # DELETE

VALIDACIONES EN EL MODELO (la madre de la integridad):
  class Post < ApplicationRecord
    validates :titulo, presence: true, length: { maximum: 120 }, uniqueness: true
    validates :cuerpo, presence: true
  end
  Post.new(cuerpo: "x").valid?   # false y te dice por qué: .errors.full_messages

RELACIONES (1línea declara ORM completa):
  class Autor; has_many :posts; end                   # un autor, muchos posts
  class Post;  belongs_to :autor; end                 # FK autor_id en posts
  autor.posts → todos; post.autor → el autor suyo.""",
  [("¿Qué hace validates :titulo, presence: true?", ["Decora", "Rechaza guardar si falta el título; el objeto retorna valid? false con errores", "Borra", "Imprime"], 1, "Validaciones a nivel MODELO = defensa total (formulario, API, consola)."),
   ("has_many :posts presupone...", ["Nada", "Que la tabla posts tiene columna autor_id (convención Rails que la FK sigue el modelo singular+_id)", "Que tiene un índice", "Que son amigos"], 1, "Por convención no tienes que decírselo: la FK es visible: autor_id.")]),
 ("4. Vistas ERB, rutas y el ciclo de Rails", """DE URL A PANTALLA (VISTAS + RUTAS)
━━━━━━━━━━━━━━━━━━━━━━━━━━━
RUTAS (config/routes.rb)
  resources :posts                      # las 7 REST GET/POST/PATCH/DELETE
  root "posts#index"                    # la home
  get "acerca", to: "pages#about"       # una estática

EL CONTROLADOR prepara @variables (con @ llegan a la vista):
  def index
    @posts = Post.order(created_at: :desc)     # los más nuevos primero
  end

LA VISTA (app/views/posts/index.html.erb))
  <h1>Mi blog</h1>
  <% @posts.each do |post| %>            ← <% %> ejecuta SIN imprimir
    <h2><%= link_to post.titulo, post %></h2>    ← <%= %> imprime ESCAPADO (anti-XSS)
    <p><%= truncate(post.cuerpo, length: 100) %></p>
  <% end %>

HELPERS que enamoran: link_to · truncate · time_ago_in_words · number_to_currency
FORM autogenerado:
  <%= form_with model: @post do |f| %>
    <%= f.text_field :titulo %> <%= f.text_area :cuerpo %> <%= f.submit %>
  <% end %>
  (form_with incluye el token CSRF gratis y detecta si es crear/update)""",
  [("¿Diferencia entre <% %> y <%= %> en ERB?", ["Ninguna", "<% ejecuta sin imprimir (loops/ifs); <%= ejecuta E IMPRIME escapando HTML", "<%= es comentario", "Lo contrario"], 1, "El clásico bug: poner <%= en un @each y ver la lista entera impresa."),
   ("¿Qué hace form_with model: @post?", ["CSS", "Formulario automático ligado al modelo: crea o edita según el objeto, con token CSRF incluido", "Valida", "Nada en especial"], 1, "Los helpers sienten la convención: si @post es nuevo → POST /posts; si existe → PATCH.")]),
 ("5. Proyecto: blog Rails con todo lo anterior", """CONSTRUYE: MINI-BLOG RAILS EN 45 MINUTOS
━━━━━━━━━━━━━━━━━━━━━━━━━━━
1. rails new miblog && cd miblog
2. rails generate scaffold Post titulo:string cuerpo:text publicado:boolean
3. rails db:migrate && rails server → visita localhost:3000/posts (YA funciona todo)
4. AHORA ENTIENDE (no solo copies): abre routes.rb, agrega root "posts#index". Abre el modelo, añade validates :titulo, presence: true. Recarga: sin título ya no guarda — ¿ves? validación en acción.
5. Agrega un Autor: rails g model Autor nombre:string ; rails g migration AddAutorToPosts autor:references ; rails db:migrate
6. Modelos: Autor.has_many :posts / Post.belongs_to :autor
   En la vista muestra <%= post.autor.nombre %>
7. rails console en otra terminal para experimentar: Autor.create(nombre: "Ada").posts
8. Bonus: scopes útiles — class Post; scope :publicados, -> { where(publicado: true) }; end → Post.publicados en el controller.

CHECKLIST 🎓: puedes explicar QUÉ hace cada método del controlador · dónde vive cada cosa · por qué las validaciones están en el modelo y no en la vista. Eso ES entender Rails.""",
  [("¿Para qué sirve un scope en el modelo Rails?", ["CSS", "Guardar consultas frecuentes como métodos reutilizables: Post.publicados", "Índices BD", "Vistas"], 1, "Scope = query con nombre: lisible y combinables (Post.publicados.recientes)."),
   ("AddAutor a posts con autor:references en migración hace...", ["Nada", "Crea la columna autor_id + índice + FK en la tabla posts (relación completa en SQL)", "Crea un modelo", "Borra posts"], 1, "Las migraciones versionan tu esquema en código: la BD se recrea con rails db:migrate.")]),
],
# ═══════════════════ 17. JAVA Y SPRING (5) ═══════════════════
"Java y Spring — El Backend del Mundo Empresarial": [
 ("1. Java: el gigante tipado (fundamentos en 15 min)", """JAVA: VERBOSO PERO SÓLIDO COMO ROCA
━━━━━━━━━━━━━━━━━━━━━━━━━━━
Instagram inicial, Netflix, bancos, Android: Java corre la economía. Lenguaje compilado, JVM, tipado ESTÁTICO.

  // Hola.java
  public class Hola {
      public static void main(String[] args) {        // entrada del programa
          String nombre = "Ada";
          int edad = 36;                              // tipos EXPLÍCITOS (pero...)
          var pi = 3.14;                              // var infiere (Java 10+)
          System.out.println("Hola, " + nombre + " tienes " + edad);

          if (edad >= 18) { System.out.println("Mayor"); }
          for (int i = 0; i < 3; i++) { System.out.println(i); }

          // colecciones:
          java.util.List<String> temas = new java.util.ArrayList<>();
          temas.add("spring"); temas.size(); temas.get(0);
      }
  }

  javac Hola.java && java Hola        ← compila y corre

CLAVE MENTAL JAVA: todo vive en clases; los tipos se verifican al compilar; la JVM lo corre en cualquier SO ("write once, run anywhere"). Maven/Gradle el gestor de paquetes+build (equivalente a npm/pip).""",
  [("¿Dónde empieza a ejecutar un programa Java?", ["cualquier función", "El método public static void main(String[] args)", "En la clase", "En el constructor"], 1, "La firma exacta main es el punto de entrada universal de Java."),
   ("¿Qué es la JVM?", ["Editor", "La máquina virtual que ejecuta el bytecode Java haciéndolo portable (una compilation, corre en to-do SO con JVM)", "Una librería", "Un navegador"], 1, "Compile once run anywhere: el bytecode .class corre en cualquier JVM.")]),
 ("2. Java moderno: records, streams y switch nuevo", """JAVA DEL 2020 EN ADELANTE SE SIENTE MODERNO
━━━━━━━━━━━━━━━━━━━━━━━━━━━
RECORDS — clases de datos sin boilerplate:
  record Punto(int x, int y) {}
  var p = new Punto(1, 2);   p.x();    // accessor gratis, toString/equals gratis

STREAMS — el map/filter/reduce de Java:
  List<Integer> nums = List.of(1, 2, 3, 4, 5);
  int sumaPares = nums.stream()
      .filter(n -> n % 2 == 0)
      .mapToInt(n -> n * 10)
      .sum();
  System.out.println(sumaPares);      // 60

OPTIONAL — adiós NullPointerException por deliberación:
  Optional<Usuario> tal = repo.findById(1);
  tal.ifPresent(u -> System.out.println(u.getNombre()));
  String nombre = tal.map(Usuario::getNombre).orElse("invitado");

SWITCH EXPRESIVO (Java 14+):
  String tipo = switch (dia) {
      case SABADO, DOMINGO -> "finde";
      default -> "lectivo";
  };

TEXT BLOCKS (String json = comillas triples como delimitador): texto literal multilinea
      sin escapar comillas ni saltos — ideal para JSON/SQL embebido en Java.""",
  [("¿Qué resuelve Optional<T>?", ["Nada", "Representa explícitamente la posible ausencia de valor: obliga a decidir (orElse, ifPresent) en vez de explotar con null", "Async", "Velocidad"], 1, "Hacer visible el 'puede faltar' en el TIPO es el antídoto contra NullPointerException."),
   ("streams en Java se parecen a...", ["bucles for", "map/filter/reduce encadenados estilo funcional como en JS/Python", "clases", "SQL nada más"], 1, "Operaciones declarativas sobre colecciones — Java moderno abraza lo funcional.")]),
 ("3. Spring Boot: API REST en 15 líneas de verdad", """SPRING BOOT: JAVA QUE CORRE COMO EXPRESS
━━━━━━━━━━━━━━━━━━━━━━━━━━━
  // build (maven) → spring-boot-starter-web. start.spring.io genera el proyecto listo.

  @RestController
  @RequestMapping("/api/tareas")
  public class TareaController {
      private final List<Tarea> tareas = new ArrayList<>();

      @GetMapping
      public List<Tarea> todas() { return tareas; }

      @PostMapping
      @ResponseStatus(HttpStatus.CREATED)
      public Tarea crear(@RequestBody Tarea t) { tareas.add(t); return t; }

      @GetMapping("/{id}")
      public Tarea una(@PathVariable int id) {
          return tareas.stream().filter(t -> t.id() == id).findFirst()
              .orElseThrow(() -> new ResponseStatusException(HttpStatus.NOT_FOUND));
      }
  }

INIECCIÓN DE DEPENDENCIAS (la magia Spring): tú diseñes interfaces y recibes implementaciones por constructor — testing y cambio de implementación gratis.

Spring Boot corere con su servidor incluido: mvn spring-boot:run → localhost:8080/api/tareas.
Auto-configuración: detecta qué hay en el classpath (maven deps) y configura solo: JSON, BD, seguridad.""",
  [("¿Qué hace @RestController?", ["Decora", "Declara la clase como controlador web: los métodos responden HTTP y devuelven datos serializados (JSON)", "Conecta BD", "Corre tests"], 1, "@RestController = @Controller + @ResponseBody: todo método = respuesta JSON directa."),
   ("¿Qué es inyección de dependencias en Spring?", ["SQL", "El framework crea y entrega los objetos que necesita tu clase por el constructor: cambiar implementación sin tocar tu código", "Npm install", "Herencia"], 1, "Recibes lo que necesitas; no lo construyes: testeo con mocks y evolución sin drama.")]),
 ("4. Spring Data JPA: base de datos casi gratis", """JPA: TU BD COMO OBJETOS JAVA
━━━━━━━━━━━━━━━━━━━━━━━━━━━
ENTIDAD (tu tabla):
  @Entity
  public class Tarea {
      @Id @GeneratedValue
      private Long id;
      private String titulo;
      private boolean hecha;
      // getters/setters/constructor
  }

REPOSITORIO (¡sin escribir SQL!):
  public interface TareaRepo extends JpaRepository<Tarea, Long> {
      List<Tarea> findByHechaFalse();                // ¡Spring genera la query del nombre!
      List<Tarea> findByTituloContaining(String texto);
  }

USO EN EL CONTROLLER
  @GetMapping("/pendientes")
  public List<Tarea> pendientes() { return repo.findByHechaFalse(); }

POR QUÉ ES IMPORTANTE: JpaRepository ya trae save/findAll/findById/deleteById... y las derivadas (findByXAndYOrderByZ) se escriben SOLAS por convención de nombre. PostgreSQL/MySQL solo agregando el driver y el application.properties:
  spring.datasource.url=jdbc:postgresql://localhost/miapp
  spring.jpa.hibernate.ddl-auto=update       (crea el esquema a partir de las entidades)

En dev; en prod controla migraciones con Flyway.""",
  [("¿Qué hace JpaRepository con findByHechaFalse()?", ["Nada", "Spring Data genera la query automáticamente a partir del NOMBRE del método (derivada por convención)", "SQL manual", "Error"], 1, "Query derivation: nombras bien el método, la query existe sin escribirla."),
   ("¿Qué papel tiene @Entity?", ["Decoración", "Marca la clase como tabla de BD manejada por el ORM (cada instancia = fila)", "Seguridad", "Async"], 1, "El mapeo objeto-relacional (ORM): objetos Java ↔ filas SQL.")]),
 ("5. Proyecto: API Java/Spring completa", """CONSTRUYE: API DE TAREAS SPRING SERIO
━━━━━━━━━━━━━━━━━━━━━━━━━━━
SETUP (10 min)
1. start.spring.io → Project Maven, Java 17+, dependencias: Spring Web + Spring Data JPA + H2 (BD embebida para dev)
2. Descomprime e importa a tu IDE (IntelliJ Community gratis)

CÓDIGO (lo aprendido en orden)
1. record Tarea(Long id, String titulo, Boolean hecha) {}  → record para el DTO
2. @Entity clase Tarea para JPA (o usa el record como DTO y entidad aparte)
3. TareaRepo extends JpaRepository<Tarea, Long> con findByHechaFalse()
4. @RestController /api/tareas: GET todas + pendientes · POST crear · PATCH {id} alternar · DELETE {id}
5. application.properties:
   spring.datasource.url=jdbc:h2:mem:tareas · spring.h2.console.enabled=true
   → consola web H2 en localhost:8080/h2-console para ver tus datos en vivo
6. Ejecuta: mvn spring-boot:run
7. Prueba: curl localhost:8080/api/tareas

BONUS (siguiente nivel realista):
• Validación: spring-boot-starter-validation + @Valid + @NotBlank en los DTOs
• Tests: @SpringBootTest o @DataJpaTest
• Dockeriza tu jar: FROM eclipse-temurin:17-jre + COPY target/*.jar + CMD java -jar

Con eso ya tienes un backend Java real: el idiom del 30% de las empresas.""",
  [("¿Qué es H2 en este proyecto?", ["Un hámster", "Base de datos SQL embebida/en memoria para desarrollo rápido, reemplazable luego por PostgreSQL sin tocar el código JPA", "Un navegador", "Un test"], 1, "H2 para arrancar sin instalar BD; cambia el datasource y punto: eso es abstracción ORM."),
   ("¿Qué genera el .jar empaquetado con spring-boot:package?", ["El código fuente", "Un ejecutable autocontenido (app+servidor Tomcat embebido): dockerizar es trivial", "JS", "Los tests"], 1, "El fat jar = tu app + servidor interno: corre en cualquier JVM sola.")]),
],
# ═══════════════════ 18. C#/.NET (4) ═══════════════════
"C# y .NET — El Ecosistema Microsoft Moderno": [
 ("1. C#: lenguaje que ya no es 'de Windows'", """C#/.NET: MULTIPLATAFORMA Y RÁPIDO
━━━━━━━━━━━━━━━━━━━━━━━━━━━
.NET moderno (6+) corre Linux/Mac/Windows, es de los backends más rápidos del mundo (benchmarks top), y C# es un TypeScript con esteroides de arquitectura.

PRIMER APP (con el SDK de dotnet)
  dotnet new console -o MiApp && cd MiApp
  dotnet run

  // Program.cs (top-level: ¡sin boilerplate clase+Main!)
  Console.WriteLine("¡Hola desde C#!");
  string nombre = "Ada";
  int edad = 36;
  var pi = 3.14;                         // var = infiere tipo
  Console.WriteLine($"{nombre} tiene {edad}");   // interpolación $""

  // LINQ: map/filter/reduce estilo C#
  var nums = new List<int> { 1, 2, 3, 4, 5 };
  var paresX10 = nums.Where(n => n % 2 == 0).Select(n => n * 10).ToList();
  nums.Sum(); nums.Max();

FUERTEMENTE TIPADO con inferencia cómoda: te protege como TS pero el compilador lo ve todo.
NuGet = el npm: dotnet add package Newtonsoft.Json""",
  [("¿Qué hace el $ antes de una cadena en C#?", ["Nada", "Habilita interpolación: $\"{variable}\" inserta valores", "Es regex", "Dinero"], 1, "$\"{nombre}\" es la f-string/template literal de C#."),
   ("LINQ Where(...).Select(...) equivale a...", ["SQL puro", "filter + map encadenados sobre colecciones, tipo JS/Python", "loops for", "bucles while"], 1, "LINQ es funcional sobre colecciones: es una de las mayores comodidades de C#.")]),
 ("2. ASP.NET Minimal API: el Express de .NET", """API REST EN 15 LÍNEAS CON .NET
━━━━━━━━━━━━━━━━━━━━━━━━━━━
  dotnet new web -o Api && cd Api

  // Program.cs COMPLETO:
  var builder = WebApplication.CreateBuilder(args);
  var app = builder.Build();

  var tareas = new List<Tarea>();

  app.MapGet("/api/tareas", () => tareas);
  app.MapPost("/api/tareas", (Tarea t) => { tareas.Add(t); return Results.Created($"/tareas/{t.Id}", t); });
  app.MapGet("/api/tareas/{id}", (int id) =>
      tareas.FirstOrDefault(t => t.Id == id) is { } t ? Results.Ok(t) : Results.NotFound());

  app.Run();
  record Tarea(int Id, string Titulo, bool Hecha);

  dotnet run → API en localhost:5000 ¡Y SWAGGER AUTOEN/DOC gratis en /swagger si agregas AddSwaggerGen!

RECORDS (¡los modelos más cortos que existen!): tipos inmutables de datos de una línea.
Results.Ok/Created/NotFound/BadRequest = status HTTP semánticos.
JSON: serialización automática de sus records/POCOs.""",
  [("¿Qué es una Minimal API en .NET?", ["Lento", "El estilo conciso de ASP.NET Core: rutas con lambdas en Program.cs sin controladores pesados", "Una BD", "algo mínimo sin poder"], 1, "Equivalente .NET a Express/Flask: ideal para APIs y microservicios."),
   ("¿Qué tipo es record Tarea(...)?", ["Clase estándar", "Tipo de datos inmutable con constructor/equals/desconstruct generados — el DTO perfecto", "Un struct", "Un enum"], 1, "Records = POJOs cómodas: modelos limpios en una línea, igualdad por VALOR.")]),
 ("3. Entity Framework Core: la BD como objetos C#", """EF CORE: EL ORM DE .NET
━━━━━━━━━━━━━━━━━━━━━━━━━━━
  dotnet add package Microsoft.EntityFrameworkCore.Sqlite

  // El modelo y la 'sesión' con la BD:
  class Tarea { public int Id { get; set; } public string Titulo { get; set; } = ""; public bool Hecha { get; set; } }
  class AppDb : DbContext {
      public DbSet<Tarea> Tareas => Set<Tarea>();
      protected override void OnConfiguring(DbContextOptionsBuilder o) => o.UseSqlite("Data Source=tareas.db");
  }

  // Usar:
  using var db = new AppDb();
  db.Database.EnsureCreated();                          // crea la BD del esquema C#
  db.Tareas.Add(new Tarea { Titulo = "Estudiar EF" });
  db.SaveChanges();
  var pendientes = db.Tareas.Where(t => !t.Hecha).ToList();

MIGRACIONES (código → esquema versionado como en Laravel/Rails):
  dotnet ef migrations add Inicial
  dotnet ef database update

LINQ → SQL automático: tu .Where(t => !t.Hecha) se CONVIERTE en la query SQL: objetos afuera, SQL adentro optimizado.
Lo interesante: con DependencyInjection en el Program.cs lo inyectas: builder.Services.AddDbContext<AppDb>();""",
  [("¿Qué es DbContext en EF Core?", ["Un controller", "La sesión/unidad de trabajo con la BD: DbSets por tabla y SaveChanges como transacción", "Un navegador", "JSON"], 1, "DbContext coordina tracked changes y los persiste con SaveChanges: el corazón del ORM."),
   ("¿Qué hacen las 'migraciones' de EF Core?", ["Nada en especial", "Generan/aplican el esquema SQL desde tus clases C# y mantienen su historial versionado", "Solo JSON", "Test"], 1, "El esquema de la BD vive en tu código: cambiar clase → migración → BD nueva consistente.")]),
 ("4. Proyecto: API .NET completa con EF Core", """CONSTRUYE: API DE TAREAS .NET SERIA
━━━━━━━━━━━━━━━━━━━━━━━━━━━
1. dotnet new web -o Tareas.Api && cd Tareas.Api
2. dotnet add package Microsoft.EntityFrameworkCore.Sqlite
3. Crea Tarea.cs (clase normal) + AppDb.cs (DbContext con DbSet<Tarea>)
4. En Program.cs:
   builder.Services.AddDbContext<AppDb>();
   var app = builder.Build();
   using (var s = app.Services.CreateScope()) { s.ServiceProvider.GetRequiredService<AppDb>().Database.EnsureCreated(); }
   app.MapGet("/api/tareas", async (AppDb db) => await db.Tareas.ToListAsync());
   app.MapPost("/api/tareas", async (AppDb db, Tarea t) => { db.Tareas.Add(t); await db.SaveChangesAsync(); return Results.Created($"/{t.Id}", t); });
   app.MapPatch("/api/tareas/{id}/toggle", async (AppDb db, int id) => {
       var t = await db.Tareas.FindAsync(id); if (t is null) return Results.NotFound();
       t.Hecha = !t.Hecha; await db.SaveChangesAsync(); return Results.Ok(t);
   });
   app.MapDelete("/api/tareas/{id}", ...Results.NoContent);
   app.Run();
5. dotnet run y prueba con curl: GET/POST/toggle.

BONUS: AddDbContext + parámetro (AppDb db) = DI automática por endpoint = el Spring-fácil de .NET.
Next: MVC completo, Blazor (frontend C# puro!) o publicar con docker.""",
  [("¿Cómo recibe el endpoint la instancia AppDb?", ["new global", "Inyección de dependencias automática: declaras (AppDb db) en la firma y .NET la entrega", "Static", "No la recibe"], 1, "DI integrada en Minimal APIs: efímero por petición, manejo del ciclo por ti."),
   ("¿Qué hace FindAsync(id)?", ["SQL crudo", "Busca por clave primaria devolviendo el objeto o null si no existe", "Borra", "Actualiza"], 1, "La operación básica de lectura-por-id en EF Core — el orElse NotFound a continuación es el patrón.")]),
],
# ═══════════════════ 19. GO (5) ═══════════════════
"Go — El Lenguaje de la Nube": [
 ("1. Go: simple, rápido, hecho para servidores", """GO: DISEÑADO EN GOOGLE PARA LA ERA CLOUD
━━━━━━━━━━━━━━━━━━━━━━━━━━━
Go (Golang) resuelve: compilar a UN binario nativo sin dependencias (webserver completo = un archivo), concurrencia de lujo, típo simple a propósito.

  // main.go
  package main
  import "fmt"

  func main() {
      nombre := "Ada"                    // := deklara e infiere
      edad := 36
      fmt.Printf("%s tiene %d años\n", nombre, edad)

      // tipos explícitos cuando hace falta:
      var total int = 5
      frutas := []string{"manzana", "pera"}       // slice (array dinámico)
      frutas = append(frutas, "uva")
      for i, f := range frutas { fmt.Println(i, f) }   // range = índice + valor

      precios := map[string]int{"café": 120}     // map (dict/hash)
      fmt.Println(precios["café"], total)
  }

  go run main.go          ← compila y corre
  go build                → BINARIO ejecutable de tu app (¡sin runtime externo!)

No tiene while: for lo es todo: for i := 0; i < 5; i++ · for cond · for range
La indentación se estandariza: gofmt lo formatea solo (¡las guerras de estilo MURIERON!)""",
  [("¿Qué ventaja especial tiene el build de Go?", ["Es bonito", "Genera UN binario nativo sin dependencias externas: el despliegue es copiar un archivo", "Corre en browser", "Interpreta"], 1, "Un solo ELF/EXE estático: las imágenes docker de Go pueden pesar 5MB."),
   ("¿Qué hace := en Go?", ["Asignar", "Declarar variable nueva con tipo INFERIDO (vs var x int explícita para el init)", "Comparar", "Importar"], 1, "x := 5 = declarar+inicializar inferido; var para declaraciones sin valor inicial.")]),
 ("2. Errores a la vista: el if err != nil filosófico", """LA FILOSOFÍA GO: SIN EXCEPCIONES OCULTAS
━━━━━━━━━━━━━━━━━━━━━━━━━━━
Las funciones DEVUELVEN errores explícitos en vez de lanzar excepciones que te sorprenden:

  archivo, err := os.ReadFile("datos.txt")
  if err != nil {
      log.Fatal("no pude leer el archivo:", err)    // decide QUÉ hacer aquí
  }
  fmt.Println(string(archivo))

  // tu propia función con error:
  func dividir(a, b float64) (float64, error) {
      if b == 0 {
          return 0, errors.New("división por cero")
      }
      return a / b, nil
  }

  resultado, err := dividir(10, 0)
  if err != nil { fmt.Println("Error:", err) }

EL PATRÓN SE REPITE MIL VECES: resultado, err := f(); if err != nil { maneja }. Verbosidad deliberada: el camino feliz Y el de error quedan VISIBLES, no escondidos en try/catch difíciles de seguir.

errors.Is/As para comprobar tipos; fmt.Errorf("contexto: %w", err) para ENVOLVER con contexto útil arriba.""",
  [("¿Por qué Go no tiene excepciones para errores esperables?", ["No pueden", "Diseño deliberado: errores como valores devueltos obligan a manejarlos conscientemente y flujo de control visible", "Son lentas", "Es antiguo"], 1, "En Go el manejo de error no se esconde en catch lejanos: está cara a cara contigo."),
   ("if err != nil es...", ["un bug", "El patrón universal de Go para comprobar y manejar errores devueltos por cada operación fallible", "opcional", "un bucle"], 1, "Todos los libros lo bromean, todos los proyectos sanos lo escriben sin pereza.")]),
 ("3. Concurrencia: goroutines y canales (el superpoder)", """GOROUTINES: 10.000 TAREAS A LA VEZ
━━━━━━━━━━━━━━━━━━━━━━━━━━━
Concurrencia = el ADN de Go. Una goroutine es un hilo livianísimo (KB de memoria, no MB):

  func descargar(url string, canal chan string) {
      // simulando trabajo lento...
      canal <- "listo: " + url                     // enviar al canal
  }

  func main() {
      canal := make(chan string)
      urls := []string{"a.com", "b.com", "c.com"}

      for _, u := range urls {
          go descargar(u, canal)                   // ¡la palabra 'go' y sigue!
      }
      for range urls {
          fmt.Println(<-canal)                      // recibir: bloquea hasta que hay dato
      }
  }

GOROUTINE: go funcion() y corre en paralelo (miles a la vez sin problema).
CANAL: tubo seguro para que las goroutines se comuniquen SIN locks compartidos:
  "Dont communicate by sharing memory; share memory by communicating" — el lema de Go.

sync.WaitGroup para esperar a todas las goroutines; context.Context para cancelar/timeouts reales.""",
  [("¿Qué crea la palabra go delante de una llamada?", ["Un error", "Una goroutine: la función corre concurrentemente sin bloquear", "Un bucle", "Otro proceso peado"], 1, "go f() = paralelo livianísimo: miles concurrentes con MB de RAM, no GB."),
   ("¿Para qué sirve un channel en Go?", ["Imprimir", "Comunicación tipada y segura entre goroutines: enviar/recibir datos sin locks manuales", "Red TCP", "SQL"], 1, "channels = tubería sincronizada entre tareas concurrentes: el camino GOnativo.")]),
 ("4. Servidor HTTP estándar: la web sin frameworks", """NET/HTTP: FRAMEWORK INCLUIDO DE FÁBRICA
━━━━━━━━━━━━━━━━━━━━━━━━━━━
  package main
  import ("encoding/json"; "net/http")

  func tareas(w http.ResponseWriter, r *http.Request) {
      w.Header().Set("Content-Type", "application/json")
      switch r.Method {
      case "GET":
          lista := []map[string]any{{"id": 1, "titulo": "Aprender Go"}}
          json.NewEncoder(w).Encode(lista)
      case "POST":
          var t struct{ Titulo string `json:"titulo"` }
          json.NewDecoder(r.Body).Decode(&t)
          w.WriteHeader(http.StatusCreated)
          json.NewEncoder(w).Encode(t)
      default:
          http.Error(w, "método no soportado", 405)
      }
  }

  func main() {
      http.HandleFunc("/api/tareas", tareas)
      http.ListenAndServe(":8080", nil)      // servidor listo en localhost:8080
  }

`json:"titulo"` (struct tag) mapea JSON <-> struct automático.
MUCHOs proyectos serios usan SOLO la stdlib o Gin/Echo livianos (porque la stdlib YA es buena).

JSON EN structs:
  type Tarea struct {
      ID     int    `json:"id"`
      Titulo string `json:"titulo"`
      Hecha  bool   `json:"hecha"`
  }""",
  [("¿Qué incluye el paquete net/http de Go?", ["Solo clientes", "Servidor HTTP completo en la stdlib: ninguna librería extra para APIs productivas", "Solo en frameworks", "SMTP"], 1, "Escuchar y servir HTTP es nativo; por eso Go domina la nube sin framework pesado."),
   ("¿Qué hace la struct tag `json:\"titulo\"`?", ["Comentario", "Mapea el campo entre Go (Titulo) y JSON (titulo) al encodear/decodear automáticamente", "SQL", "Un indice"], 1, "Las tags gobiernan la serialización: la convención de nombre se configura explícita.")]),
 ("5. Proyecto: API Go real + binario listo para producción", """CONSTRUYE: API DE NOTAS GO
━━━━━━━━━━━━━━━━━━━━━━━━━━━
1. mkdir notasapi && cd notasapi && go mod init notas (¡el go.mod es tu package.json!)
2. main.go con:
   - struct Nota {ID, Titulo, Texto} con tags json
   - slice global []Nota con mutex sync.RWMutex (concurrencia segura)
   - handlers: GET /api/notas · GET /api/notas/{id} · POST · DELETE
     Para {id} usa r.PathValue("id") en Go 1.22+ (¡el router nativo mejoró!)
   - helpers: respondJSON(w, status, data) y valida Titulo no vacío → 400
3. Corre: go run . → localhost:8080
4. CONSTRUYE EL BINARIO y viaja:
     go build -o notasapi
     ./notasapi          ← corre SIN go instalado, en cualquier Linux igual
     GOOS=windows GOARCH=amd64 go build -o notas.exe   ← ¡compilación CRUZADA de regalo!
5. Dockeriza en 2 etapas (multi-stage): FROM golang:alpine build → FROM scratch/alpine run (imagen final ~10MB)

LO QUE APRENDISTE: tipado estático con structs y tags · errores explícitos concurrentes · API en stdlib pura · binarios autosuficientes = el stack favorito de la nube.""",
  [("¿Qué permite go build + cross-compilation?", ["Nada", "Un único binario estático por SO/arquitectura sin dependencias: deployment es 'copiar y correr'", "npm", "Un lenguaje"], 1, "produce.exe final: sin JVM/python en el server — eso lo aprecian mucho en operaciones."),
   ("¿Por qué sync.RWMutex con la slice global en la API?", ["Para más RAM", "Lecturas/escrituras concurrentes sobre memoria compartida pueden corromperse: el mutex las sincroniza", "Es moda", "No hace falta"], 1, "Varios requests golpean la misma estructura a la vez: sincronización obligatoria o data race.")]),
],
# ═══════════════════ 20. RUST (5) ═══════════════════
"Rust — Velocidad de C sin Miedo a los Crashes": [
 ("1. Rust: el lenguaje querido 9 años seguidos", """RUST: SIN GC, SIN SEGFAULTS, SEGURO DE MEMORIA EN COMPILACIÓN
━━━━━━━━━━━━━━━━━━━━━━━━━━━
Rust compila tan rápido como C++ pero el COMPILADOR garantiza que no cuelgas punteros ni rompes memoria (sin garbage collector encima). Por eso: #1 'most loved' de StackOverflow 8+ años.

  // main.rs
  fn main() {
      let nombre = "Ada";                        // inmutable POR DEFECTO (inmutabilidad manda)
      let mut edad = 36;                         // mutable requiere mut explícito
      edad += 1;
      println!("{} tiene {} años", nombre, edad);

      let frutas = vec!["manzana", "pera"];       // Vec<T>: array dinámico
      for f in &frutas { println!("{}", f); }     // & = BY REFERENCIA (¡el corazón!)

      fn area(b: i32, h: i32) -> i32 { b * h }    // -> tipo de retorno, return implícito sin ;
  }

INSTALACIÓN: rustup (rustup.rs) → cargo (el gestor TODO: build+deps+test)
  cargo new miapp && cd miapp && cargo run    ← el flujo feliz

cargotest integrado; docs automáticas: cargo doc --open""",
  [("¿Qué es diferente de los valores en Rust por defecto?", ["Todos mutables", "Inmutables por defecto; declaras mut explícitamente para cambiar valores", "Todos globales", "Todos públicos"], 1, "La inmutabilidad por defecto evita enormes clases de bugs en concurrencia."),
   ("¿Qué es cargo en el ecosistema Rust?", ["Puerto mar", "El todo en uno: compilar, gestionar dependencias (crates), testear, documentar", "Un VC", "Solo build"], 1, "cargo new/run/test/build: el mejor gestor de proyectos del mundo compilado.")]),
 ("2. Ownership: el sistema que cambia tu cabeza", """OWNERSHIP: LA REGLA DE ORO DE RUST
━━━━━━━━━━━━━━━━━━━━━━━━━━━
Tres reglas (de las que TODO se deriva):
1. Cada valor tiene UN dueño (una variable)
2. Solo puede haber UN dueño a la vez (al moverse, el anterior lo pierde)
3. Cuando el dueño sale de scope → valor liberado automáticamente (¡sin GC!)

  let a = String::from("hola");
  let b = a;              // MOVIDO: 'a' YA NO VALE (¡se 'movió' la propiedad!)
  // println!("{}", a);  // ❌ error de compilación: 'value used after move'
  println!("{}", b);      // ✅

  let r = &b;             // & = pedir prestado (lea, no mueve): puedo tener mil & lectores
  let w = &mut b_mut;     // &mut = prestar PARA ESCRIBIR: solo UNO a la vez (y sin lectores activos)

POR QUÉ IMPORTA: el compilador rechaza data races, use-after-free y double-free en COMPILACIÓN, no en producción. La memoria se libera sin garbage collector ni free manual.

.clone() copia de verdad cuando necesitas dos dueños. Strings con String (mutable en heap), &str vista/prestada (lo eficiente).""",
  [("¿Por qué en Rust `let b = a` con Strings \x27mueve\x27 en vez de copiar?", ["Es bug", "Ownership: solo un dueño por valor para liberar memoria automáticamente de forma segura", "Es C puro", "Para velocidad del IDE"], 1, "Si dos dueños intentaran liberar → double-free. Un dueño ya lo sabes: sin GC, sin peligro."),
   ("¿Qué garantiza que no haya data races en concurrente Rust?", ["Suerte", "Un solo &mut Sin & lectores, o muchos & pero ningún mut: exclusión mutua GARANTIZADA por el compilador", "Threads especiales", "Locks manuales"], 1, "'Fearless concurrency': el type system TAN estricto hace im-posibles los race conditions clásicos.")]),
 ("3. Result y Option: errores como parte del tipo", """RESULT/OPTION: NULL Y EXCEPCIONES, PERO TIPADOS
━━━━━━━━━━━━━━━━━━━━━━━━━━━
  // Result<T, E> en vez de excepciones; Option<T> en vez de null:
  use std::fs;
  fn leer() -> Result<String, std::io::Error> {
      let texto = fs::read_to_string("notas.txt")?;      // ? = si error, devuélvelo ya
      Ok(texto)
  }

  // en main:
  match leer() {
      Ok(texto)   => println!("Contenido: {}", texto),
      Err(error)  => eprintln!("Falló: {}", error),
  }

  // Option para ausencia de valor (su Some/None):
  let tal = vec![1,2,3].first();      // Some(1) o None si vacío
  match tal {
      Some(n) => println!("primero: {}", n),
      None    => println!("lista vacía"),
  }
  // atajos: .unwrap_or(0) · .unwrap_or_else(...) (¡.unwrap() explota: avoid!)

EL PUNTO GENIAL: el COMPILADOR te obliga a manejar ambos casos. No hay "ops, me olvidé del null".

El operador ? propaga el error hacia arriba automáticamente = código delgado y seguro a la vez.""",
  [("¿Qué hace el operador ? tras una llamada Result?", ["Nada", "Si es Ok, desenvuelve el valor; si es Err, lo retorna inmediatamente a la función llamante (propagación elegante)", "Borra", "Bucle"], 1, "El equivalente Go-verboso pero sin boilerplate: error handling conciso y explícito."),
   ("¿En qué consiste la seguridad adicional de Option<T> vs null?", ["Es un puntero", "No hay null: la AUSENCIA es parte del TIPO y el compilador EXIGE manejar el caso None", "Es más rápido", "Sin diferencia"], 1, "Null = 'agujero invisible'; None = 'la firma te avisa y obliga'. Billion-dollar mistake corregida.")]),
 ("4. Structs, traits e iteradores: Rust en su salsa", """MODELADO RÚSTICO
━━━━━━━━━━━━━━━━━━━━━━━━━━━
STRUCTS (tus datos)
  #[derive(Debug, Clone)]                    // rasgos generados automagicamente
  struct Tarea { titulo: String, hecha: bool }

IMPL (los métodos del struct)
  impl Tarea {
      fn nueva(titulo: &str) -> Self {                 // constructor convencional
          Tarea { titulo: titulo.to_string(), hecha: false }
      }
      fn completar(&mut self) { self.hecha = true; }   // muta: requiere instancia mut
  }

TRAITS (interfaces compartidas: el polimorfismo de Rust)
  trait Saludable { fn saludar(&self) -> String; }
  impl Saludable for Tarea { fn saludar(&self) -> String { format!("Soy {}!", self.titulo) } }
  // genéricos con trait bounds: fn imprimir<T: Saludable>(x: &T) → cero overhead

ITERADORES puros: encadena sin loops manuales, cero coste:
  let numeros = vec![1, 2, 3, 4, 5];
  let resultado: Vec<i32> = numeros.iter().filter(|n| *n % 2 == 0).map(|n| n * 10).collect();
  let suma: i32 = numeros.iter().sum();""",
  [("¿Qué son los traits de Rust?", ["Clases normales", "Interfaces de comportamiento (comparable a interfaces Java/protocols) implementables por cualquier tipo — aún nativos predefinidos", "Macros", "Bases de datos"], 1, "derive(Debug) o impl Trait for MiStruct: comportamiento compartido sin herencia tradicional."),
   ("¿Qué coste extra tienen los iteradores encadenados de Rust?", ["Mucho (boxed)", "Cero: se compilan al mismo código que un bucle for manual (zero-cost abstractions)", "Algo en runtime", "Lentísimos"], 1, "'What you don't use, you don't pay for; what you do, you couldn't hand-code better' = lema.")]),
 ("5. Proyecto: CLI real en Rust con clap", """CONSTRUYE: CLI DE NOTAS EN RUST
━━━━━━━━━━━━━━━━━━━━━━━━━━━
1. cargo new notas && cd notas
2. Cargo.toml → [dependencies]: clap = { version = "4", features = ["derive"] } · serde/serde_json (parse/serializa JSON)
   cargo add clap --features derive serde serde_json
3. Estructura: main.rs CLI con clap:
   #[derive(clap::Parser)] struct Args { #[command(subcommand)] cmd: Cmd }
   #[derive(clap::Subcommand)] enum Cmd { Agregar { titulo: String }, Lista, Borrar { id: usize } }
4. notas.rs: struct Nota + Vec<Nota> guardado en notas.json (serde_json + fs write/read)
   → practicarás: Result, ? , Option, ownership con Strings
5. Matching el comando, cargas, mutas, guardas. fuzz con clap: notas agregar "Estudiar Rust" → agrega
6. cargo test para funciones internas (tests al lado del código: #[test] fn ...{})
7. cargo build --release → target/release/notas → ¡tu binario final nativo para portar/entregar!

CON LO QUE ENFRENTÁS de verdad: lifetimes básicos (peleas del novato: hence String vs &str decisiones), Result serializable, CLI parse profesional. Próximo área: async con tokio, tu primer servicio web rápido.""",
  [("¿Qué hace clap con macros derive?", ["Nada", "Genera el parser de argumentos/ayuda de tu CLI desde tus structs automáticamente (--help profesional gratis)", "Compila Rust", "Instala crates"], 1, "Derive: Rust's compile-time code generation — CLI args tipados de regalo."),
   ("¿Qué desafío famoso te hará 'sentir' ownership en este proyecto?", ["Null", "Elegir entre String (dueña) y &str (prestada) en structs/funcs: la decisión de propiedad explícita", "Threads", "Red"], 1, "Las peleas con el borrow checker te enseñan el modelo: un mes después, es superpoder.")]),
],
# ═══════════════════ 21. C Y C++ (5) ═══════════════════
"C y C++ — Los Cimientos del Software Moderno": [
 ("1. C: el abuelo presente en TODO", """C: 1972 Y SIGUE CORRIENDO EL MUNDO
━━━━━━━━━━━━━━━━━━━━━━━━━━━
Linux, Git, PostgreSQL, Python (¡está escrito en C!), el kernel de tu celu: TODO corre sobre C.
Aprender C = entender cómo funcionan TODOS los demás lenguajes por debajo.

  // hola.c
  #include <stdio.h>                 // stdio: print/scan
  int main(void) {
      char nombre[] = "Ada";         // string = array de char (¡Rust/Go lo heredan!)
      int edad = 36;
      printf("Hola %s, tienes %d años\n", nombre, edad);   // placeholders %s %d %.2f

      int nums[5] = {10, 20, 30};    // array fijo
      for (int i = 0; i < 5; i++) printf("%d ", nums[i]);

      // funciones (declaradas antes de usarse o con prototipo arriba):
      // int area(int base, int altura);
      return 0;
  }

  gcc hola.c -o hola && ./hola      ← compilar + correr

DECLARACIONES EXPLÍCITAS siempre (int edad;); sin bool nativo antes de C99 (int 0/1); memoria manual (malloc/free, próxima lección). Verás cadenas de formato: %d=int,%f=float,%s=string,%c=char.""",
  [("¿Por qué aprender C hoy si 'no lo usaré directo'?", ["Nostalgia", "Es el substrato real: memoria, punteros y bajo nivel explican el comportamiento de TODOS los demás lenguajes actuales", "Es gratis", "Es fácil"], 1, "'Entender realmente' qué hace tu lenguaje favorito = haber pasado por C."),
   ("¿Qué hace printf(\"%d\", x)?", ["Imprime 5", "Imprime valores donde %d es el placeholder de un entero (y %s string, %f float...)", "Lee input", "Error"], 1, "String de formato con marcadores posicionales: el printf-family clásico.")]),
 ("2. Punteros y memoria manual: la estrella de C", """PUNTEROS: LA DIRECCIÓN DE LA MEMORIA (EL CONCEPTO CLAVE)
━━━━━━━━━━━━━━━━━━━━━━━━━━━
Un puntero ES una variable que guarda una DIRECCIÓN de memoria. Simple y profundo.

  int edad = 36;
  int *p = &edad;         // p guarda la DIRECCIÓN de edad (& = 'dirección de')
  printf("%d", *p);       // * = seguir el puntero (desreferenciar): imprime 36
  *p = 40;                // ¡modifica edad a través del puntero!

  // scanf con punteros (por eso tanto &):
  scanf("%d", &edad);     // scanf necesita DÓNDE escribir

MEMORIA MANUAL: malloc pide, free devuelve (¡olvidares = fugas/leaks!)
  int *arr = malloc(5 * sizeof(int));     // bloque de 5 enteros
  arr[0] = 99;
  free(arr);                              // devolver la memoria: obligatorio
  arr = NULL;                             // evita usar colgante

ERRORES ILEGALES FAMOSOS (que Rust previene en compilación):
• usar memoria tras free (use-after-free)
• liberar dos veces (double-free)
• salirte del array (buffer overflow: apocalipsis de seguridad)""",
  [("¿Qué significa *p cuando p es puntero?", ["Multiplicar", "Seguir el puntero: LEER/ESCRIBIR el valor en esa dirección", "Reservar memoria", "Liberar"], 1, "* = dereferenciar; & = sacar dirección. Las dos caras de la memoria manual."),
   ("¿Qué es una fuga de memoria (memory leak)?", ["Un virus", "malloc sin free: la memoria reservada nunca se devuelve y el programa crece hasta morir", "Un print raro", "Puntero NULL"], 1, "En C/GestiónManual: cada malloc necesita su free — por eso los lenguajes modernos tienen GC/ownership.")]),
 ("3. C++: C más objetos y la STL (los superpoderes)", """C++: C CON SUPERPOBLACIÓN (ENORME Y POTENTE)
━━━━━━━━━━━━━━━━━━━━━━━━━━━
C++ = C 98% válido + clases, templates, excepciones y la Standard Template Library (STL). Juegos (Unreal), Chrome, MySQL, Tesla, trading: el software rápido de verdad.

  #include <iostream>
  #include <vector>
  #include <string>
  using namespace std;
  int main() {
      string nombre = "Ada";                    // string de verdad (no char*)
      vector<int> nums = {1, 2, 3, 4, 5};       // array dinámico seguro
      nums.push_back(6);
      for (int n : nums) cout << n << " ";      // for-range moderno
      cout << endl;

      auto doble = [](int x) { return x * 2; }; // lambdas (C++11)
      sort(nums.begin(), nums.end());            // algoritmos STL
  }

CLASES (POO verdadera)
  class Tarea {
      string titulo; bool hecha = false;
  public:
      Tarea(const string& t) : titulo(t) {}    // constructor
      void completar() { hecha = true; }
  };

RAII (la GRAN IDEA de C++): los recursos (memoria, archivos, locks) se liberan solos cuando el objeto sale de scope → es el origen del design de Rust. new/delete (o mejor: punteros inteligentes unique_ptr/shared_ptr).""",
  [("¿Qué aporta vector<T> de la STL respecto a arrays C?", ["Nada", "Array dinámico gestionado: crece solo, sabe su tamaño, sin malloc/free manual", "Es de Java", "Es lento por obligación"], 1, "vector + string + sort + map = la STL: productividad C++, sin pelear malloc manual."),
   ("¿Qué es RAII en C++?", ["Un error", "Adquisición/liberación de recursos ligada al ciclo de vida de objetos: scope-ended = recurso liberado (origen del modelo que perfecciona Rust)", "Una clase", "Excepción"], 1, "Destructor al salir del bloque: no olvidas liberar; es la contra a los leaks/locks olvidados.")]),
 ("4. Compilar y depurar: gcc, make y headers", """DE .C A EJECUTABLE REAL (EL FLUJO COMPLETO)
━━━━━━━━━━━━━━━━━━━━━━━━━━━
COMPILACIÓN PASOS (lo que hace gcc por dentro)
  gcc -c hola.c          → compila a hola.o (código objeto por archivo)
  gcc hola.o util.o -o app   → LINKEA objetos+bibliotecas → ejecutable final

DIVIDIR EN ARCHIVOS (la costumbre de C serio)
  util.h  → DECLARACIONES (qué existe: int area(int,int);  )
  util.c  → DEFINICIONES (cómo se hace: int area(...){...}  )
  main.c  → #include "util.h" → usa sin saber los detalles

MAKEFILE: automatizar builds multi-archivo
  app: main.o util.o
<TAB>gcc main.o util.o -o app
  main.o: main.c util.h
<TAB>gcc -c main.c
  clean:
<TAB>rm -f *.o app
  → make   (compila solo lo que cambió) · make clean

FLAGS PROFESIONALES
  gcc -Wall -Wextra -g hola.c -o hola    ← todos los warnings + símbolos debug
  gdb ./hola                              ← depurador: break main, run, print, next

⚠ Los warnings de -Wall son tus mejores amigos C: trátalos como errores.""",
  [("¿Cuál es la diferencia .h vs .c en C?", ["Ninguna", ".h declara (interfaz pública) y .c define (implementación): separación contrato/código", ".h es más rápido", ".h es para header HTTP"], 1, "El header es la 'API' del módulo; main lo incluye sin ver su implementación."),
   ("¿Qué hace make con un Makefile bien escrito?", ["Todo de nuevo", "Recompila SOLO los archivos cuyos fuentes cambiaron (build incremental con dependencias)", "Instala paquetes", "Ejecuta tests"], 1, "Dependencias+reglas: el build incremental nació aquí (todo build system actual lo hereda).")]),
 ("5. Proyecto: programa C completo leyendo archivos", """CONSTRUYE: CONTADOR DE PALABRAS EN C puro
━━━━━━━━━━━━━━━━━━━━━━━━━━━
SPEC: programa que recibe un .txt y reporta líneas, palabras y caracteres (el clásico wc).

  #include <stdio.h>
  int main(int argc, char *argv[]) {           // argc = cuántos args; argv = la lista
      if (argc < 2) {
          printf("Uso: %s archivo.txt\n", argv[0]);
          return 1;                            // código de error ≠ 0 = convención de fallo
      }
      FILE *f = fopen(argv[1], "r");
      if (f == NULL) { perror("No pude abrir"); return 1; }        // chequeo de error siempre

      int c, lineas = 0, palabras = 0, caracteres = 0, enPalabra = 0;
      while ((c = fgetc(f)) != EOF) {          // lee caracter a caracter
          caracteres++;
          if (c == '\n') lineas++;
          if (c == ' ' || c == '\n' || c == '\t') enPalabra = 0;
          else if (!enPalabra) { palabras++; enPalabra = 1; }
      }
      fclose(f);                                // LIBERAR el recurso: RAII mental en C
      printf("%d líneas, %d palabras, %d caracteres\n", lineas, palabras, caracteres);
      return 0;
  }

  gcc -Wall -o wc wc.c && ./wc nota.txt

EJERCICIO STRETCH: argc>2 soportar varios archivos y sumar; -l flag para solo líneas.
LO QUE REALMENTE APRENDISTE: argc/argv · fopen/fclose · fgetc/EOF · return codes. El ABC de Unix puro.""",
  [("¿Qué return values significan en main C?", ["Cualquiera", "0 = éxito; ≠0 = falló (la shell lo lee con $? — parte del protocolo Unix)", "Nada", "255 siempre"], 1, "El exit code es como los programas 'hablan' entre sí en batch/pipes: vital en scripts."),
   ("¿Por qué fclose(f) explícito importa en C?", ["No importa", "Sin cerrar, fopen queda abiertoy puede agotar file descriptors / corrupt data si escribías", "Por estética", "Por velocidad"], 1, "C no tiene with/auto-cleanup: cada recurso abierto necesita su cierre deliberado.")]),
],
# ═══════════════════ 22. TOUR DE LENGUAJES (5) ═══════════════════
"Tour de Lenguajes — Cuál Aprender y Cuándo": [
 ("1. El mapa completo: paradigmas que se repiten", """LENGUAJES = HERRAMIENTAS, NO RELIGIONES
━━━━━━━━━━━━━━━━━━━━━━━━━━━
PARADIGMAS (famlías mentales — aprendes UNO de cada y el resto son dialectos)
• Imperativo/Procedural: dícese los pasos — C, Go
• POO-clásica: objetos con estado y mensajes — Java, C#, Ruby, C++
• Funcional: datos fluyen, inmutabilidad, funciones puras — Haskell, Elixir (y rasgos en JS/Python/Rust)
• Dinámico/criptivo: iteración rápida — Python, JS, Ruby
• Estático + memoria: control total y velocidad — C, C++, Rust, Go
• Web-específico: PHP (backend HTML-native), Dart (Flutter), Swift/Kotlin (móvil)

LAS DIMENSIONES QUE IMPORTAN AL ELEGIR
• Tipo: estático (compilador verifica) vs dinámico (flexible, corre y ve)
• Velocidad: interpretado (py) < VM (java/cs/node) < compilado nativo (c/go/rust)
• Ecosistema: librerías/empleos/comunidad (factor ignorado a tu costa)
• Modelo de memoria: manual (C) < ownership (Rust) < GC (todo lo demás)

VERDAD DURA ÚTIL: el segundo lenguaje es el que más te cuesta. El tercero, dos semanas. El 15.º, días.""",
  [("¿Qué es lo MÁS ignorado pero importante al elegir lenguaje?", ["La sintaxis", "El ecosistema: librerías disponibles, mercado laboral y comunidad viva", "El nombre", "La moda"], 1, "Un lenguaje perfecto sin librerías ni ofertas es un callejón: mira el ecosistema antes."),
   ("¿Por qué el segundo lenguaje cuesta más que el quinto?", ["Es universal", "El primero te enseña conceptos universales: luego solo aprendes dialectos de lo mismo", "Porque sí", "No es cierto"], 1, "if/for/funciones/estado/estructuras se repiten con disfraz distinto: aprendes mapas, no zonas.")]),
 ("2. Python vs JavaScript: los dos gigantes y cuándo cada uno", """LA PREGUNTA MÁS HECHA: PYTHON O JAVASCRIPT
━━━━━━━━━━━━━━━━━━━━━━━━━━━
COMPARATIVA HONESTA
criterio | PYTHON | JAVASCRIPT
Donde manda | Datos/IA/backend/scripting/automatización | La web frontend PER SE + backend con Node
Sintaxis | Limpia, legible, para enseñar | Más símbolos, ES6 la salvó
Ecosistema | pandas/TF/Django... insustituible en datos | npm: la librería más grande de la historia
Tipado | Dinámico + type hints opcionales | Dinámico + TypeScript como salvavidas ya estándar
Velocidad cruda | lento (pero C de bajo nivel a 1 lib) | V8 rápido para su clase
Primer empleo | junior data/backend/qa | junior web (mercado mayor pero más competido)

RESPUESTA DIRECTA EN 2 REGLAS
• Quieres la WEB → JavaScript inevitable (ningún otro corre en navegadores: es monopolio legal js)
• Quieres DATOS/IA/bitácoras/scripts → Python (el default global de la industria de datos)

(NO elijas por "velocidad": para el 95% de proyectos, tu I/O manda antes que el lenguaje.)

Y SI SOLO APRENDES UNO POR AHORA: ambos son 'primer lenguaje seguro'. Lo que te pone a trabajar es completar UNO con proyectos, no cuestionar el otro.""",
  [("¿Por qué JS es literalmente inevitable para frontend web?", ["Es más bonito", "Es el ÚNICO lenguaje que corren los navegadores (WebAssembly emergiendo pero JS sigue en los browsers como lingua franca)", "Por estándar europeo", "Por Google"], 1, "Si fabricas UI en navegador, JS está en tu fatora — no es opinión, es el mercado."),
   ("¿Cuál es la trampa al decidir 'conqué el mejor lenguaje' y esperar?", ["Ninguna", "Deciditis: la elección vale menos que terminar UNO con 5 proyectos reales; la emeployabilidad premia a quien CONSTRUYE", "Python", "JS"], 1, "El time-box de decisión: 1 día máximo; luego, carril elegido y acelerar.")]),
 ("3. Java, C#, Go, Rust, C/C++: el clan de los compilados", """JI CERRA EL CÍRCULO: GUÍA DE ESTÁTICOS EN 5 LÍNEAS C/U
━━━━━━━━━━━━━━━━━━━━━━━━━━━
JAVA — el rey del enterprise (banca, ERP, Android nativo). Estable, verborragico mejorado, mercado ENORME y paga. Si quieres empleo grande y estable: Java + Spring.

C#/.NET — el Java de Microsoft pero ¡mejoró muchísimo! Multiplataforma post-.NET Core, LINQ elegante, Unity (videojuegos), Azure. Gran equilibrio productividad/potencia.

GO — el lenguaje DE LA NUBE: Kubernetes, Docker, Terraform, microservicios everywhere. Concurrency nativa, binario único, sintaxis mínima. DevOps/SRE/backend-cloud TIENEN que saber Go.

RUST — velocidad C sin UB: navegadores, cripto, sistemas embebidos, herramientas CLI velocísimas. Curva dura (ownership te duele 1 mes) pero te cambia a mejor como programador para siempre.

C/C++ — donde NO PUEDES elegir: kernels, drivers, juegos AAA, motores físicos, aviónica, trading nanosegundos. Control absoluto a precio de peligro absoluto.

REGLA ELEGIDA SINCERA: infraestructura/cloud → Go · empresa corporativa → Java/C# · performance real → Rust primero, C++ si tu industria lo exige (juegos, hardware).""",
  [("Si quieres trabajar en infraestructura/cloud (k8s, Terraform, etc.), el lenguaje estrella es...", ["Python", "Go: la nube moderna está escrita en él (Docker, Kubernetes, Terraform)", "Java", "Ruby"], 1, "Go = lenguaje icu de la nube: binarios únicos + concurrencia nativa."),
   ("¿Cuándo C/C++ es la OPCIÓN y no una elección?", ["Siempre", "Sistemas operativos, drivers, motores gráficos, embebidos, latencia extrema — donde el control hardware es la feature", "Para web APIs", "Nunca"], 1, "Cuando nanosegundos/bytes importan como requisito: C/C++ no es viejo, es el cimiento obligado.")]),
 ("4. Kotlin, Swift, Dart/Flutter, React Native: el mapa móvil", """MÓVIL: UNA DECISIÓN ESTRATÉGICA
━━━━━━━━━━━━━━━━━━━━━━━━━━━
NATIVO (rendimiento/máxima integración con el SO, DOS código bases)
• KOTLIN → Android (Google lo hizo oficial; Java mejorado y moderno, null-safety)
• SWIFT → Apple (iOS/Mac; lenguaje precioso, sintaxis moderna; la Store paga bien)

CROSS-PLATFORM (UNA base, ambas tiendas)
• FLUTTER (Dart): compila a nativo ARM, pixel-perfect propio render → UI idéntica, popularísimo en startups
• REACT NATIVE: tu JavaScript/React renderizando componentes NATIVOS (Meta lo usa: Instagram)
  → si YA sabes React/JS, RN es tu puerta sin curva

COMPARATIVA ESTRATÉGICA
• ¿Startup que necesita ambas tiendas YA? → Flutter o RN (una persona, dos apps)
• ¿Trabajo estable en empresa móvil grande? → nativo por plataforma
• ¿Solo iOS / solo Android? → nativo (integración 100%)
• ¿Frontend web que busca móvil? → React Native

EXPO para React Native hace el setup trivialexpo start: menos nativo-debug hell, más producto.""",
  [("¿Qué es lo MÁS estratégico a decidir en móvil?", ["El color del icono", "Nativo vs cross-platform: dos citas tienen curvas de coste totalmente distintas por equ, equipo y objetivo", "El IDE", "Nada"], 1, "Decisión de arquitectura de negocio: tiempo de mercado vs acceso total a la plataforma."),
   ("¿Por qué React Native le convenía tan rápido a equipos web?", ["Es Apple", "Reutiliza tu stack React/JS: un equipo web rinde en móvil en semanas, sin aprender dos nuevos mundos", "Sin curva", "JSON"], 1, "Plataformas distintas but conocimientos trasladables: de ahi su explosión.")]),
 ("5. Elegir con propósito + tu plan de aprendizaje", """EL FRAMEWORK DE DECISIÓN DEL LENGUAJE (EN 4 PREGUNTAS)
━━━━━━━━━━━━━━━━━━━━━━━━━━━
P1. ¿QUÉ QUIERO CONSTRUIR (ahora, específico)?
   web frontend = JS · web backend = py/js/go/java · datos/IA = Python · móvil = flutter/kotlin/swift · juegos = C#(Unity)/C++ · sistemas = rust/go · empresa = java/c#
P2. ¿QUÉ LENGUAJE ME ABRE MÁS PUERTAS?
   python+js son llaves maestras universales: aprendes uno de estos PRIMERO siempre
P3. ¿CUÁNTO MERCADO HAY EN MI PAÍS/NICHO?
   (búscalo real: LinkedIn empleos + los 3 stacks competitivos) — Nottingham del diálogo
P4. ¿CUÁL ME MANTIENE EN JUEGO 6 MESES?
   el mejor lenguaje es el que practicas cada día: elige el que combina respuestas 1-3 × tu persistencia

PLAN DE 12 MESES AHORRADO EN PAÍNELES
mes 1-3: UN lenguaje + proyectos pequeños (python o js)
mes 4-6: agrega el segundo del otro campo (js si empezaste py, al revés)
mes 7-9: git+linux+docker+sql (el trasversal que todo empleo pide)
mes 10-12: un framework (React o Django/Spring) + portafolio + primeras entrevistas

🎯 MANTRA FINAL: lenguajes NUEVOS son features de sintaxis de las ideas que YA sabes; construir PROYECTOS es la MISMA habilidad en cualquiera. Elige ya; ajusta caminando.""",
  [("¿Cuál es la M1 regla para no quedarte eligiendo para siempre?", ["Basear 10", "Elegir 1 de python/js, comprometerte 90 días y construir proyectos: después, agregar desde la experiencia, no desde el FOMO", "Todos a la vez", "Solo el de moda"], 1, "Decisión+momentum > análisis. Ajustas rumbo con apps REALES bajo el brazo."),
   ("¿Qué último criterio completa una buena elección de lenguaje?", ["El logo", "Cuánto te mantiene volviendo colza día (persistencia real) × mercado × qué quieres construir", "Ser el más rápido", "Ser gratis"], 1, "La disciplina es tu moss importante tecnología: sin ella ningún stack importa.")]),
],
}
