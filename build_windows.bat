@echo off
rem 🖥 Compila el ejecutable nativo Windows (PyInstaller)
cd /d "%~dp0"
python -m pip install -r requirements.txt pyinstaller
pyinstaller --noconfirm --clean --windowed --name "PlataformaTotal" --icon assets\icono.ico --add-data "assets/icono.png;assets" --collect-all customtkinter main.py
echo ✅ Listo: dist\PlataformaTotal\PlataformaTotal.exe
