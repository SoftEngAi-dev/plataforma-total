# 📕 Resumen maestro — Testing — Programar con Red de Seguridad

> Todo el curso en una hoja: una idea núcleo por lección. Releer semanal.

## 1. 1. Tests: por qué son parte del código, no un extra
EL MINDSET DE PRUEBAS DESDE EL DÍA 1 ━━━━━━━━━━━━━━━━━━━━━━━━━━━ Un test es código que PRUEBA tu otro código automáticamente. Corre en segundos mil veces al día.  POR QUÉ LOS EQUIP…

## 2. 2. Pytest, Jest y asserts: la gramática universal
LA GRAMÁTICA DE LAS PRUEBAS (PYTEST COMO EJEMPLO) ━━━━━━━━━━━━━━━━━━━━━━━━━━━   # operaciones.py   def dividir(a, b):       if b == 0:           raise ValueError("división por cero…

## 3. 3. Mocks, fixtures y el arte de aislar
TEST DOBLE: TU LABORATORIO SIN SORPRESAS ━━━━━━━━━━━━━━━━━━━━━━━━━━━ MOCK = simular lo externo (API, email, BD, hora) para probar SOLO lo tuyo.   from unittest.mock import patch, M…

## 4. 4. Cobertura, TDD práctico y tests de integración
MÁS ALLÁ DEL TEST UNITARIO ━━━━━━━━━━━━━━━━━━━━━━━━━━━ COBERTURA — métrica útil (pero muerte por meta)   pip install pytest-cov; pytest --cov=miapp --cov-report=term-missing Te mue…

## 5. 5. Proyecto: suite de tests real para tu calculadora/app
CONSTRUYE: CALCULADORA CON TDD REAL (EN VIVO) ━━━━━━━━━━━━━━━━━━━━━━━━━━━ RETO TDD ESTRICTO (40-60 min, disciplina pura): FUNCIONES: sumar, restar, multiplicar, dividir (con error …

---
✅ 5 lecciones · 📝 10 preguntas de repaso en quizzes_html/ · tests/