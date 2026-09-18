# 5. Proyecto: API Go real + binario listo para producción

> 📚 Curso: **Go — El Lenguaje de la Nube** · Lección 5 de 5
> 🗓 Exportado: 18/09/2026 desde Plataforma Total
> 🍅 Sugerencia: 1-2 pomodoros para leer + practicar

---

## 📖 Contenido

```go
CONSTRUYE: API DE NOTAS GO
━━━━━━━━━━━━━━━━━━━━━━━━━━━
1. mkdir notasapi && cd notasapi && go mod init notas (¡el go.mod es tu package.json!)
2. main.go con:
   - struct Nota {ID, Titulo, Texto} con tags json
   - slice global []Nota con mutex sync.RWMutex (concurrencia segura)
   - handlers: GET /api/notas · GET /api/notas/{id} · POST · DELETE
     Para {id} usa r.PathValue("id") en Go 1.22+ (¡el router nativo mejoró!)
   - helpers: respondJSON(w, status, data) y valida Titulo no vacío → 400
3. Corre: go run . → localhost:8080
4. CONSTRUYE EL BINARIO y viaja:
     go build -o notasapi
     ./notasapi          ← corre SIN go instalado, en cualquier Linux igual
     GOOS=windows GOARCH=amd64 go build -o notas.exe   ← ¡compilación CRUZADA de regalo!
5. Dockeriza en 2 etapas (multi-stage): FROM golang:alpine build → FROM scratch/alpine run (imagen final ~10MB)

LO QUE APRENDISTE: tipado estático con structs y tags · errores explícitos concurrentes · API en stdlib pura · binarios autosuficientes = el stack favorito de la nube.
```

---

## 📝 Quiz de la lección

### 1. ¿Qué permite go build + cross-compilation?
- A) Nada
- B) Un único binario estático por SO/arquitectura sin dependencias: deployment es 'copiar y correr'
- C) npm
- D) Un lenguaje
### 2. ¿Por qué sync.RWMutex con la slice global en la API?
- A) Para más RAM
- B) Lecturas/escrituras concurrentes sobre memoria compartida pueden corromperse: el mutex las sincroniza
- C) Es moda
- D) No hace falta

---

## 🔑 Respuestas y explicaciones

**1.** ✅ Un único binario estático por SO/arquitectura sin dependencias: deployment es 'copiar y correr' — produce.exe final: sin JVM/python en el server — eso lo aprecian mucho en operaciones.
**2.** ✅ Lecturas/escrituras concurrentes sobre memoria compartida pueden corromperse: el mutex las sincroniza — Varios requests golpean la misma estructura a la vez: sincronización obligatoria o data race.

---
✅ Al terminar, marca la lección como completada en la app (📚 Aprender → ✅ Completada)
