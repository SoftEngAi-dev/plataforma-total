# 1. Go: simple, rápido, hecho para servidores

> 📚 Curso: **Go — El Lenguaje de la Nube** · Lección 1 de 5
> 🗓 Exportado: 18/09/2026 desde Plataforma Total
> 🍅 Sugerencia: 1-2 pomodoros para leer + practicar

---

## 📖 Contenido

```go
GO: DISEÑADO EN GOOGLE PARA LA ERA CLOUD
━━━━━━━━━━━━━━━━━━━━━━━━━━━
Go (Golang) resuelve: compilar a UN binario nativo sin dependencias (webserver completo = un archivo), concurrencia de lujo, típo simple a propósito.

  // main.go
  package main
  import "fmt"

  func main() {
      nombre := "Ada"                    // := deklara e infiere
      edad := 36
      fmt.Printf("%s tiene %d años
", nombre, edad)

      // tipos explícitos cuando hace falta:
      var total int = 5
      frutas := []string{"manzana", "pera"}       // slice (array dinámico)
      frutas = append(frutas, "uva")
      for i, f := range frutas { fmt.Println(i, f) }   // range = índice + valor

      precios := map[string]int{"café": 120}     // map (dict/hash)
      fmt.Println(precios["café"], total)
  }

  go run main.go          ← compila y corre
  go build                → BINARIO ejecutable de tu app (¡sin runtime externo!)

No tiene while: for lo es todo: for i := 0; i < 5; i++ · for cond · for range
La indentación se estandariza: gofmt lo formatea solo (¡las guerras de estilo MURIERON!)
```

---

## 📝 Quiz de la lección

### 1. ¿Qué ventaja especial tiene el build de Go?
- A) Es bonito
- B) Genera UN binario nativo sin dependencias externas: el despliegue es copiar un archivo
- C) Corre en browser
- D) Interpreta
### 2. ¿Qué hace := en Go?
- A) Asignar
- B) Declarar variable nueva con tipo INFERIDO (vs var x int explícita para el init)
- C) Comparar
- D) Importar

---

## 🔑 Respuestas y explicaciones

**1.** ✅ Genera UN binario nativo sin dependencias externas: el despliegue es copiar un archivo — Un solo ELF/EXE estático: las imágenes docker de Go pueden pesar 5MB.
**2.** ✅ Declarar variable nueva con tipo INFERIDO (vs var x int explícita para el init) — x := 5 = declarar+inicializar inferido; var para declaraciones sin valor inicial.

---
✅ Al terminar, marca la lección como completada en la app (📚 Aprender → ✅ Completada)
