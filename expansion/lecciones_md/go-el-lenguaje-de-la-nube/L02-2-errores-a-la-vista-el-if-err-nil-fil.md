# 2. Errores a la vista: el if err != nil filosófico

> 📚 Curso: **Go — El Lenguaje de la Nube** · Lección 2 de 5
> 🗓 Exportado: 18/09/2026 desde Plataforma Total
> 🍅 Sugerencia: 1-2 pomodoros para leer + practicar

---

## 📖 Contenido

```go
LA FILOSOFÍA GO: SIN EXCEPCIONES OCULTAS
━━━━━━━━━━━━━━━━━━━━━━━━━━━
Las funciones DEVUELVEN errores explícitos en vez de lanzar excepciones que te sorprenden:

  archivo, err := os.ReadFile("datos.txt")
  if err != nil {
      log.Fatal("no pude leer el archivo:", err)    // decide QUÉ hacer aquí
  }
  fmt.Println(string(archivo))

  // tu propia función con error:
  func dividir(a, b float64) (float64, error) {
      if b == 0 {
          return 0, errors.New("división por cero")
      }
      return a / b, nil
  }

  resultado, err := dividir(10, 0)
  if err != nil { fmt.Println("Error:", err) }

EL PATRÓN SE REPITE MIL VECES: resultado, err := f(); if err != nil { maneja }. Verbosidad deliberada: el camino feliz Y el de error quedan VISIBLES, no escondidos en try/catch difíciles de seguir.

errors.Is/As para comprobar tipos; fmt.Errorf("contexto: %w", err) para ENVOLVER con contexto útil arriba.
```

---

## 📝 Quiz de la lección

### 1. ¿Por qué Go no tiene excepciones para errores esperables?
- A) No pueden
- B) Diseño deliberado: errores como valores devueltos obligan a manejarlos conscientemente y flujo de control visible
- C) Son lentas
- D) Es antiguo
### 2. if err != nil es...
- A) un bug
- B) El patrón universal de Go para comprobar y manejar errores devueltos por cada operación fallible
- C) opcional
- D) un bucle

---

## 🔑 Respuestas y explicaciones

**1.** ✅ Diseño deliberado: errores como valores devueltos obligan a manejarlos conscientemente y flujo de control visible — En Go el manejo de error no se esconde en catch lejanos: está cara a cara contigo.
**2.** ✅ El patrón universal de Go para comprobar y manejar errores devueltos por cada operación fallible — Todos los libros lo bromean, todos los proyectos sanos lo escriben sin pereza.

---
✅ Al terminar, marca la lección como completada en la app (📚 Aprender → ✅ Completada)
