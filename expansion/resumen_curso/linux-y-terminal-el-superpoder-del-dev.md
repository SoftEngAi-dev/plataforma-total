# 📕 Resumen maestro — Linux y Terminal — El Superpoder del Dev

> Todo el curso en una hoja: una idea núcleo por lección. Releer semanal.

## 1. 1. El sistema de archivos y navegación
EL ÁRBOL DE LINUX HACIA ADENTRO ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ TODO es un archivo a partir de /   /home/tu_usuario      ← tu casa (~)  ·  /etc configs  ·  /var logs  ·  /usr progr…

## 2. 2. Leer, buscar y tuberías: la filosofía Unix
COMANDOS PEQUEÑOS, CADENAS POTENTES (|) ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ LEER   cat archivo        (todo) · less archivo (paginado, / busca, q sale) · head -20 (principio) · tail -f…

## 3. 3. Permisos y procesos: controlar el sistema
QUIÉN PUEDE QUÉ + QUÉ ESTÁ CORRIENDO ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ PERMISOS: -rwxr-xr--   r(4) leer · w(2) escribir · x(1) ejecutar | dueño / grupo / otros   chmod +x script.sh  …

## 4. 4. SSH: tu llave a cualquier servidor
SSH: CONTROL REMOTO CIFRADO, LA HERRAMIENTA ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━   ssh usuario@IP_DEL_SERVIDOR      → entras a otra máquina por terminal (así se administran TODOS los se…

## 5. 5. Scripts Bash: automatiza tu propia vida
BASH: TU PRIMER LENGUAJE REAL DE SERVIDOR ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━   #!/bin/bash            ← shebang: qué lo ejecuta (primera línea)   nombre="Mundo"   echo "Hola, $nombre"…

## 6. 6. Proyecto: pone tu PC a trabajar sola
AUTOMATIZA: 3 SCRIPTS DE TU VIDA DIARIA ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ SCRIPT 1 — respaldo.sh (el indispensable)   #!/bin/bash   set -euo pipefail   fecha=$(date +%F)   tar -czf "…

---
✅ 6 lecciones · 📝 12 preguntas de repaso en quizzes_html/ · tests/