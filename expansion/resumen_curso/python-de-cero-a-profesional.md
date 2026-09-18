# 📕 Resumen maestro — Python — De Cero a Profesional

> Todo el curso en una hoja: una idea núcleo por lección. Releer semanal.

## 1. 1. Python: instalación y primer programa
PYTHON: LEGIBLE > TODO ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ Instalación: python.org (marca "Add to PATH" en Windows) o sudo apt install python3.    python3 --version   python3 hola.py  …

## 2. 2. Tipos, variables y f-strings
LOS TIPOS DE BASE ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━   edad = 36                  # int   precio = 19.99             # float   nombre = "Ada"             # str   activo = True        …

## 3. 3. Listas y tuplas: colecciones ordenadas
LISTAS: EL CABALLITO DE BATALLA ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━   numeros = [10, 20, 30, 40]   numeros[0]     → 10   numeros[-1]    → 40        (índices negativos: desde el final) …

## 4. 4. Diccionarios y sets: clave-valor y unicidad
DICTS: LA ESTRUCTURA MÁS USADA DE PYTHON ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━   alumno = {"nombre": "Ada", "edad": 36, "temas": ["py", "js"]}   alumno["nombre"]        → "Ada"   alumno.…

## 5. 5. Strings: métodos que usarás a diario
STRINGS: INMUTABLES Y POTENTES ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━   texto = "Hola Mundo Python"   texto.lower() · .upper() · .title()         # casos   texto.strip()                  …

## 6. 6. Condicionales y verdad en Python
IF/ELIF/ELSE — LA SINTAXIS LIMPIA ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━   if edad >= 18:       print("mayor")   elif edad >= 13:       print("adolescente")   else:       print("menor")  …

## 7. 7. Bucles: for, range, enumerate, while
FOR: PRECIOSO EN PYTHON ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━   for fruta in ["🍎", "🍌", "🥝"]:          # itera directo sobre elementos       print(fruta)  RANGE (cuentas)   range(5)     …

## 8. 8. Funciones: parámetros, return y scope
FUNCIONES: CONTRATOS DE UNA LÍNEA ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━   def area_rectangulo(base, altura):       '''Devuelve el area.'''        # docstring: tu API documentada       re…

## 9. 9. Archivos: leer, escribir y JSON
ARCHIVOS: PERSISTENCIA BÁSICA (Y BONITA) ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ LA FRASE DE LOS PROFESIONALES: with   with open("notas.txt", "w", encoding="utf-8") as f:       f.write("lí…

## 10. 10. Errores con gracia: try/except profesional
EXCEPCIONES: FALLAR ES NORMAL, CAPTÚRALAS CON ESTILO ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━   try:       edad = int(input("Edad: "))       print(100 / edad)   except ValueError:       pri…

## 11. 11. Comprensiones avanzadas y lambda: código que se lee
AZÚCAR PITÓNICO DE VERDAD ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ COMPREHENSIONS CON FILTRO DOBLE Y DICCIONARIOS   resultado = {n: "par" if n % 2 == 0 else "impar" for n in range(6)}   lis…

## 12. 12. Clases y objectos: modelar el mundo
POO PITÓNICA: CLASES SENCILLAS ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━   class Tarea:       def __init__(self, titulo):          # constructor           self.titulo = titulo           self…

## 13. 13. Módulos, paquetes y entornos virtuales
ORGANIZA TU CÓDIGO COMO LOS PROFESIONALES ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ MÓDULO = un archivo .py. IMPORTA lo que necesitas:   import math; math.sqrt(2)                    # namesp…

## 14. 14. Librería estándar: 10 joyas incluidas
LA STDLIB: BATERÍAS INCLUIDAS ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━   import datetime   hoy = datetime.date.today() · datetime.datetime.now() · (fecha - otra).days    import random   ran…

## 15. 15. Python para datos: tu primer análisis real
PYTHON + DATOS: EL SUPERPODER LABORAL ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ Escenario real: tienes ventas.csv:   producto,precio,cantidad   Café,120,3   Pan,45,10  SIN PANDAS (stdlib pur…

## 16. 16. Proyecto final: tu asistente CLI personal
CONSTRUYE: ASISTENTE CLI COMPLETO ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ Requisitos (todo el curso aplicado): 1. Comandos: nota agregar/lista · tarea agregar/hecha · dado · fecha · export…

---
✅ 16 lecciones · 📝 32 preguntas de repaso en quizzes_html/ · tests/