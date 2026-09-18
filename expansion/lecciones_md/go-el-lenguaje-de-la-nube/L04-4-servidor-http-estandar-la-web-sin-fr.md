# 4. Servidor HTTP estándar: la web sin frameworks

> 📚 Curso: **Go — El Lenguaje de la Nube** · Lección 4 de 5
> 🗓 Exportado: 18/09/2026 desde Plataforma Total
> 🍅 Sugerencia: 1-2 pomodoros para leer + practicar

---

## 📖 Contenido

```go
NET/HTTP: FRAMEWORK INCLUIDO DE FÁBRICA
━━━━━━━━━━━━━━━━━━━━━━━━━━━
  package main
  import ("encoding/json"; "net/http")

  func tareas(w http.ResponseWriter, r *http.Request) {
      w.Header().Set("Content-Type", "application/json")
      switch r.Method {
      case "GET":
          lista := []map[string]any{{"id": 1, "titulo": "Aprender Go"}}
          json.NewEncoder(w).Encode(lista)
      case "POST":
          var t struct{ Titulo string `json:"titulo"` }
          json.NewDecoder(r.Body).Decode(&t)
          w.WriteHeader(http.StatusCreated)
          json.NewEncoder(w).Encode(t)
      default:
          http.Error(w, "método no soportado", 405)
      }
  }

  func main() {
      http.HandleFunc("/api/tareas", tareas)
      http.ListenAndServe(":8080", nil)      // servidor listo en localhost:8080
  }

`json:"titulo"` (struct tag) mapea JSON <-> struct automático.
MUCHOs proyectos serios usan SOLO la stdlib o Gin/Echo livianos (porque la stdlib YA es buena).

JSON EN structs:
  type Tarea struct {
      ID     int    `json:"id"`
      Titulo string `json:"titulo"`
      Hecha  bool   `json:"hecha"`
  }
```

---

## 📝 Quiz de la lección

### 1. ¿Qué incluye el paquete net/http de Go?
- A) Solo clientes
- B) Servidor HTTP completo en la stdlib: ninguna librería extra para APIs productivas
- C) Solo en frameworks
- D) SMTP
### 2. ¿Qué hace la struct tag `json:"titulo"`?
- A) Comentario
- B) Mapea el campo entre Go (Titulo) y JSON (titulo) al encodear/decodear automáticamente
- C) SQL
- D) Un indice

---

## 🔑 Respuestas y explicaciones

**1.** ✅ Servidor HTTP completo en la stdlib: ninguna librería extra para APIs productivas — Escuchar y servir HTTP es nativo; por eso Go domina la nube sin framework pesado.
**2.** ✅ Mapea el campo entre Go (Titulo) y JSON (titulo) al encodear/decodear automáticamente — Las tags gobiernan la serialización: la convención de nombre se configura explícita.

---
✅ Al terminar, marca la lección como completada en la app (📚 Aprender → ✅ Completada)
