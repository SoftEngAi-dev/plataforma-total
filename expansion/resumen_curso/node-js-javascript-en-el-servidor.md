# 📕 Resumen maestro — Node.js — JavaScript en el Servidor

> Todo el curso en una hoja: una idea núcleo por lección. Releer semanal.

## 1. 1. Node: sacar JS del navegador
NODE: V8 EN LA TERMINAL ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ Node.js corre JavaScript fuera del navegador: servidores, CLIs, scripts. Mismo lenguaje, otro hogar.  SETUP + PRIMER SCRIPT …

## 2. 2. npm: el universo de paquetes
NPM: DEPENDENCIAS Y SCRIPTS ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ INICIALIZAR PROYECTO   npm init -y                    → package.json (el manifiesto)  INSTALAR   npm install express    …

## 3. 3. Express: el servidor web minimalista
EXPRESS EN 20 LÍNEAS ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━   import express from "express";   const app = express();   app.use(express.json());                 // parsea JSON del body (m…

## 4. 4. Asincronía en Node: no congeles el servidor
EL EVENT LOOP: EL MOTOR DE NODE ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ Node corre TODO en un hilo. Una operación lenta sincrónica CONGELA a todos los usuarios a la vez. Solución: async SI…

## 5. 5. Express + estructura real + variables de entorno
DE EJEMPLO A PROYECTO REAL ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ ESTRUCTURA PROFESIONAL   src/     index.js          ← arranque (escucha puerto)     app.js            ← configura express…

## 6. 6. Proyecto: API REST real con Express
CONSTRUYE: API DE NOTAS COMPLETA ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ MVP (3 pomodoros) 1. npm init -y; "type": "module"; npm i express dotenv 2. Rutas: GET /api/notas · GET /api/notas/…

---
✅ 6 lecciones · 📝 12 preguntas de repaso en quizzes_html/ · tests/