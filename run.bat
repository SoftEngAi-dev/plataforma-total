@echo off
rem 🚀 Ejecuta Plataforma Total en Windows (crea el entorno virtual si hace falta)
cd /d "%~dp0"

if not exist .venv (
  echo 📦 Primera ejecución: creando entorno virtual (.venv^)...
  python -m venv .venv
  call .venv\Scripts\activate.bat
  pip install --quiet --upgrade pip
  pip install --quiet -r requirements.txt
  echo ✅ Entorno listo
) else (
  call .venv\Scripts\activate.bat
)

python main.py
