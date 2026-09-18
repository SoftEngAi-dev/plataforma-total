#!/usr/bin/env bash
# 🖥 Compila el ejecutable nativo Linux (PyInstaller)
set -euo pipefail
cd "$(dirname "$0")"
python3 -m pip install -r requirements.txt pyinstaller
pyinstaller --noconfirm --clean --windowed --name "PlataformaTotal" --icon assets/icono.png --add-data "assets/icono.png:assets" --collect-all customtkinter main.py
echo "✅ Listo: dist/PlataformaTotal/PlataformaTotal"
