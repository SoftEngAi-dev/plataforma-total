# 📕 Resumen maestro — Go — El Lenguaje de la Nube

> Todo el curso en una hoja: una idea núcleo por lección. Releer semanal.

## 1. 1. Go: simple, rápido, hecho para servidores
GO: DISEÑADO EN GOOGLE PARA LA ERA CLOUD ━━━━━━━━━━━━━━━━━━━━━━━━━━━ Go (Golang) resuelve: compilar a UN binario nativo sin dependencias (webserver completo = un archivo), concurre…

## 2. 2. Errores a la vista: el if err != nil filosófico
LA FILOSOFÍA GO: SIN EXCEPCIONES OCULTAS ━━━━━━━━━━━━━━━━━━━━━━━━━━━ Las funciones DEVUELVEN errores explícitos en vez de lanzar excepciones que te sorprenden:    archivo, err := o…

## 3. 3. Concurrencia: goroutines y canales (el superpoder)
GOROUTINES: 10.000 TAREAS A LA VEZ ━━━━━━━━━━━━━━━━━━━━━━━━━━━ Concurrencia = el ADN de Go. Una goroutine es un hilo livianísimo (KB de memoria, no MB):    func descargar(url strin…

## 4. 4. Servidor HTTP estándar: la web sin frameworks
NET/HTTP: FRAMEWORK INCLUIDO DE FÁBRICA ━━━━━━━━━━━━━━━━━━━━━━━━━━━   package main   import ("encoding/json"; "net/http")    func tareas(w http.ResponseWriter, r *http.Request) {  …

## 5. 5. Proyecto: API Go real + binario listo para producción
CONSTRUYE: API DE NOTAS GO ━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1. mkdir notasapi && cd notasapi && go mod init notas (¡el go.mod es tu package.json!) 2. main.go con:    - struct Nota {ID, …

---
✅ 5 lecciones · 📝 10 preguntas de repaso en quizzes_html/ · tests/