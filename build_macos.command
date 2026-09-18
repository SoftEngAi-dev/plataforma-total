#!/bin/bash
# 🖥 Compila la app nativa macOS (PyInstaller)
cd "$(dirname "$0")"
python3 -m pip install -r requirements.txt pyinstaller
pyinstaller --noconfirm --clean --windowed --name "PlataformaTotal" --collect-all customtkinter main.py
echo "✅ Listo: dist/PlataformaTotal.app"
