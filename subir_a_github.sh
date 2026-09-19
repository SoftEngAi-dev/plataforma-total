#!/usr/bin/env bash
# =================================================================
#  SUBIR PLATAFORMA TOTAL A GITHUB — macOS / Linux / Git Bash
#  Uso interactivo:  ./subir_a_github.sh
#  Uso directo:      GITHUB_USER=tu-usuario REPO=plataforma-total \
#                    GITHUB_TOKEN=ghp_xxx ./subir_a_github.sh
# =================================================================
set -euo pipefail
cd "$(dirname "$0")"

echo "🚀 Plataforma Total → GitHub"
echo "============================"
command -v git >/dev/null || { echo "❌ Instala git primero (sudo apt install git / brew install git)"; exit 1; }

if [ -z "${GITHUB_USER:-}" ]; then read -rp "👉 Tu usuario de GitHub: " GITHUB_USER; fi
if [ -z "${REPO:-}" ]; then read -rp "👉 Nombre del repo [plataforma-total]: " REPO; fi
REPO="${REPO:-plataforma-total}"

if [ -z "${GITHUB_TOKEN:-}" ]; then
  echo "ℹ️  Sin token, créalo en: github.com → Settings → Developer settings"
  echo "   → Personal access tokens → Tokens (classic) → permisos: repo + workflow"
  read -rp "👉 Token (ghp_...) [Enter = login interactivo de git]: " GITHUB_TOKEN || true
fi
GITHUB_TOKEN="${GITHUB_TOKEN:-}"

# Repo local
if [ ! -d .git ]; then
  git init -q && git symbolic-ref HEAD refs/heads/main
  git add -A
  git -c user.name="$GITHUB_USER" -c user.email="$GITHUB_USER@users.noreply.github.com" commit -qm "feat: Plataforma Total v3.0"
fi
echo "📦 Repo local: $(git ls-files | wc -l | tr -d ' ') archivos · $(git log --oneline | wc -l | tr -d ' ') commits"

git remote remove origin 2>/dev/null || true

if [ -n "$GITHUB_TOKEN" ] && command -v curl >/dev/null; then
  echo "🌐 Creando el repo en GitHub vía API..."
  code=$(curl -s -o /tmp/pt_gh_resp.json -w "%{http_code}" -X POST https://api.github.com/user/repos \
    -H "Authorization: Bearer $GITHUB_TOKEN" -H "Accept: application/vnd.github+json" \
    -d "{\"name\":\"$REPO\",\"private\":false,\"description\":\"Plataforma Total — 41 cursos, 241 lecciones, 482 quizzes + app desktop\"}")
  case "$code" in
    201) echo "✔ Repo '$REPO' creado (público)";;
    422) echo "ℹ️  Ya existía — seguimos con el push";;
    401) echo "❌ Token inválido o sin scope 'repo' (HTTP 401)"; exit 1;;
    *)   echo "⚠️  API respondió HTTP $code — si creaste el repo a mano en github.com/new, continúo";;
  esac
  echo "⬆️  Subiendo archivos (push)..."
  git push "https://x-access-token:${GITHUB_TOKEN}@github.com/${GITHUB_USER}/${REPO}.git" main:main
  git remote add origin "https://github.com/${GITHUB_USER}/${REPO}.git" 2>/dev/null \
    || git remote set-url origin "https://github.com/${GITHUB_USER}/${REPO}.git"
else
  echo "ℹ️  Sin token: asegúrate de haber creado el repo VACÍO en https://github.com/new"
  git remote add origin "https://github.com/${GITHUB_USER}/${REPO}.git"
  echo "⬆️  Push (git pedirá usuario y, como contraseña, tu TOKEN)..."
  git push -u origin main
fi

cat <<OK

============================================
✅ ¡TODO SUBIDO!  →  https://github.com/$GITHUB_USER/$REPO
============================================
🖥️  Descargar ejecutables (5-10 min): pestaña Actions → run ✅ → Artifacts:
    PlataformaTotal-Windows (.zip) · PlataformaTotal-macOS (.tar.gz) · PlataformaTotal-Linux (.tar.gz)
📦 Release permanente (no caduca):  git tag v3.0 && git push origin v3.0
    → https://github.com/$GITHUB_USER/$REPO/releases
OK
