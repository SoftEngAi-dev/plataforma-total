#!/usr/bin/env bash
# 🚀 SUBIR PLATAFORMA TOTAL A GITHUB — guía + comandos en 1 paso
# Uso:  GITHUB_USER=tu-usuario REPO=plataforma-total ./subir_a_github.sh
# (o copia/pega los comandos de abajo a mano — mismo resultado)
set -euo pipefail

if [ -z "${GITHUB_USER:-}" ] || [ -z "${REPO:-}" ]; then
  cat <<'GUIA'
USO →  GITHUB_USER=tu-usuario REPO=plataforma-total ./subir_a_github.sh

PASO 0 — Crea el repo vacío (una vez):
  1. Ve a https://github.com/new
  2. Nombre: plataforma-total · Público o Privado al gusto
  3. NO marques "Add a README" (debe nacer vacío)
  4. Create repository

AUTENTICACIÓN — elige UNA:
  A) Token (recomendada): github.com → Settings → Developer settings
     → Personal access tokens → Tokens (classic) → Generate new token
     → marca permisos: repo + workflow → copia el token (ghp_...)
     Cuando git pida contraseña en el push, pega el TOKEN (no tu contraseña).
  B) Llave SSH ya configurada en tu máquina: cambia la URL por
     git@github.com:USUARIO/REPO.git  (este script lo detecta con USE_SSH=1)

CAMINO MANUAL (si prefieres copiar y pegar en tu terminal):
    git remote add origin https://github.com/USUARIO/REPO.git
    git push -u origin main
    # En "Run workflow": pestaña Actions en github.com → compilo Win/Mac/Linux

GUIA
  exit 1
fi

URL="https://github.com/${GITHUB_USER}/${REPO}.git"
[ "${USE_SSH:-0}" = "1" ] && URL="git@github.com:${GITHUB_USER}/${REPO}.git"

echo "📦 Repo local: $(git rev-parse --show-toplevel) · $(git ls-files | wc -l) archivos · $(git log --oneline | wc -l) commits"
echo "🚀 Configurando remote → $URL"

git remote remove origin 2>/dev/null || true
git remote add origin "$URL"

echo "⬆️ Haciendo push (te pedirá usuario y tu TOKEN como contraseña si es HTTPS)..."
git push -u origin main

cat <<OK
✅ Todo subido.
SIGUIENTE, en tu navegador:
  1. https://github.com/${GITHUB_USER}/${REPO}/actions → "🖥️ Compilar ejecutables desktop" → Run workflow
  2. En ~5 min descarga: PlataformaTotal-Windows.zip · macOS.tar.gz · Linux.tar.gz
  3. El README del repo queda como portada.
OK
