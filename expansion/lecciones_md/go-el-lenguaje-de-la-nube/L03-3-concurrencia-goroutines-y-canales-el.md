# 3. Concurrencia: goroutines y canales (el superpoder)

> 📚 Curso: **Go — El Lenguaje de la Nube** · Lección 3 de 5
> 🗓 Exportado: 18/09/2026 desde Plataforma Total
> 🍅 Sugerencia: 1-2 pomodoros para leer + practicar

---

## 📖 Contenido

```go
GOROUTINES: 10.000 TAREAS A LA VEZ
━━━━━━━━━━━━━━━━━━━━━━━━━━━
Concurrencia = el ADN de Go. Una goroutine es un hilo livianísimo (KB de memoria, no MB):

  func descargar(url string, canal chan string) {
      // simulando trabajo lento...
      canal <- "listo: " + url                     // enviar al canal
  }

  func main() {
      canal := make(chan string)
      urls := []string{"a.com", "b.com", "c.com"}

      for _, u := range urls {
          go descargar(u, canal)                   // ¡la palabra 'go' y sigue!
      }
      for range urls {
          fmt.Println(<-canal)                      // recibir: bloquea hasta que hay dato
      }
  }

GOROUTINE: go funcion() y corre en paralelo (miles a la vez sin problema).
CANAL: tubo seguro para que las goroutines se comuniquen SIN locks compartidos:
  "Dont communicate by sharing memory; share memory by communicating" — el lema de Go.

sync.WaitGroup para esperar a todas las goroutines; context.Context para cancelar/timeouts reales.
```

---

## 📝 Quiz de la lección

### 1. ¿Qué crea la palabra go delante de una llamada?
- A) Un error
- B) Una goroutine: la función corre concurrentemente sin bloquear
- C) Un bucle
- D) Otro proceso peado
### 2. ¿Para qué sirve un channel en Go?
- A) Imprimir
- B) Comunicación tipada y segura entre goroutines: enviar/recibir datos sin locks manuales
- C) Red TCP
- D) SQL

---

## 🔑 Respuestas y explicaciones

**1.** ✅ Una goroutine: la función corre concurrentemente sin bloquear — go f() = paralelo livianísimo: miles concurrentes con MB de RAM, no GB.
**2.** ✅ Comunicación tipada y segura entre goroutines: enviar/recibir datos sin locks manuales — channels = tubería sincronizada entre tareas concurrentes: el camino GOnativo.

---
✅ Al terminar, marca la lección como completada en la app (📚 Aprender → ✅ Completada)
