@echo off
REM =====================================================
REM  SUBIR PLATAFORMA TOTAL A GITHUB - lanzador Windows
REM  Doble clic aqui. Ejecuta subir_a_github.ps1 sin
REM  problemas de politicas de ejecucion de PowerShell.
REM =====================================================
powershell -NoProfile -ExecutionPolicy Bypass -File "%~dp0subir_a_github.ps1"
pause
