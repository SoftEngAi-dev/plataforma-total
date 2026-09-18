# 2. Punteros y memoria manual: la estrella de C

> 📚 Curso: **C y C++ — Los Cimientos del Software Moderno** · Lección 2 de 5
> 🗓 Exportado: 18/09/2026 desde Plataforma Total
> 🍅 Sugerencia: 1-2 pomodoros para leer + practicar

---

## 📖 Contenido

```cpp
PUNTEROS: LA DIRECCIÓN DE LA MEMORIA (EL CONCEPTO CLAVE)
━━━━━━━━━━━━━━━━━━━━━━━━━━━
Un puntero ES una variable que guarda una DIRECCIÓN de memoria. Simple y profundo.

  int edad = 36;
  int *p = &edad;         // p guarda la DIRECCIÓN de edad (& = 'dirección de')
  printf("%d", *p);       // * = seguir el puntero (desreferenciar): imprime 36
  *p = 40;                // ¡modifica edad a través del puntero!

  // scanf con punteros (por eso tanto &):
  scanf("%d", &edad);     // scanf necesita DÓNDE escribir

MEMORIA MANUAL: malloc pide, free devuelve (¡olvidares = fugas/leaks!)
  int *arr = malloc(5 * sizeof(int));     // bloque de 5 enteros
  arr[0] = 99;
  free(arr);                              // devolver la memoria: obligatorio
  arr = NULL;                             // evita usar colgante

ERRORES ILEGALES FAMOSOS (que Rust previene en compilación):
• usar memoria tras free (use-after-free)
• liberar dos veces (double-free)
• salirte del array (buffer overflow: apocalipsis de seguridad)
```

---

## 📝 Quiz de la lección

### 1. ¿Qué significa *p cuando p es puntero?
- A) Multiplicar
- B) Seguir el puntero: LEER/ESCRIBIR el valor en esa dirección
- C) Reservar memoria
- D) Liberar
### 2. ¿Qué es una fuga de memoria (memory leak)?
- A) Un virus
- B) malloc sin free: la memoria reservada nunca se devuelve y el programa crece hasta morir
- C) Un print raro
- D) Puntero NULL

---

## 🔑 Respuestas y explicaciones

**1.** ✅ Seguir el puntero: LEER/ESCRIBIR el valor en esa dirección — * = dereferenciar; & = sacar dirección. Las dos caras de la memoria manual.
**2.** ✅ malloc sin free: la memoria reservada nunca se devuelve y el programa crece hasta morir — En C/GestiónManual: cada malloc necesita su free — por eso los lenguajes modernos tienen GC/ownership.

---
✅ Al terminar, marca la lección como completada en la app (📚 Aprender → ✅ Completada)
