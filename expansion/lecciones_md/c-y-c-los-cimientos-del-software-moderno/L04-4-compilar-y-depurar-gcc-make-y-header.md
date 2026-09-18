# 4. Compilar y depurar: gcc, make y headers

> 📚 Curso: **C y C++ — Los Cimientos del Software Moderno** · Lección 4 de 5
> 🗓 Exportado: 18/09/2026 desde Plataforma Total
> 🍅 Sugerencia: 1-2 pomodoros para leer + practicar

---

## 📖 Contenido

```cpp
DE .C A EJECUTABLE REAL (EL FLUJO COMPLETO)
━━━━━━━━━━━━━━━━━━━━━━━━━━━
COMPILACIÓN PASOS (lo que hace gcc por dentro)
  gcc -c hola.c          → compila a hola.o (código objeto por archivo)
  gcc hola.o util.o -o app   → LINKEA objetos+bibliotecas → ejecutable final

DIVIDIR EN ARCHIVOS (la costumbre de C serio)
  util.h  → DECLARACIONES (qué existe: int area(int,int);  )
  util.c  → DEFINICIONES (cómo se hace: int area(...){...}  )
  main.c  → #include "util.h" → usa sin saber los detalles

MAKEFILE: automatizar builds multi-archivo
  app: main.o util.o
<TAB>gcc main.o util.o -o app
  main.o: main.c util.h
<TAB>gcc -c main.c
  clean:
<TAB>rm -f *.o app
  → make   (compila solo lo que cambió) · make clean

FLAGS PROFESIONALES
  gcc -Wall -Wextra -g hola.c -o hola    ← todos los warnings + símbolos debug
  gdb ./hola                              ← depurador: break main, run, print, next

⚠ Los warnings de -Wall son tus mejores amigos C: trátalos como errores.
```

---

## 📝 Quiz de la lección

### 1. ¿Cuál es la diferencia .h vs .c en C?
- A) Ninguna
- B) .h declara (interfaz pública) y .c define (implementación): separación contrato/código
- C) .h es más rápido
- D) .h es para header HTTP
### 2. ¿Qué hace make con un Makefile bien escrito?
- A) Todo de nuevo
- B) Recompila SOLO los archivos cuyos fuentes cambiaron (build incremental con dependencias)
- C) Instala paquetes
- D) Ejecuta tests

---

## 🔑 Respuestas y explicaciones

**1.** ✅ .h declara (interfaz pública) y .c define (implementación): separación contrato/código — El header es la 'API' del módulo; main lo incluye sin ver su implementación.
**2.** ✅ Recompila SOLO los archivos cuyos fuentes cambiaron (build incremental con dependencias) — Dependencias+reglas: el build incremental nació aquí (todo build system actual lo hereda).

---
✅ Al terminar, marca la lección como completada en la app (📚 Aprender → ✅ Completada)
