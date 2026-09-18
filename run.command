#!/bin/bash
# 🚀 Ejecuta Plataforma Total en macOS (doble clic, crea .venv si hace falta)
cd "$(dirname "$0")"

if [ ! -d .venv ]; then
  echo "📦 Primera ejecución: creando entorno virtual (.venv)..."
  python3 -m venv .venv
  source .venv/bin/activate
  pip install --quiet --upgrade pip
  pip install --quiet -r requirements.txt
  echo "✅ Entorno listo"
else
  source .venv/bin/activate
fi

python3 main.py
