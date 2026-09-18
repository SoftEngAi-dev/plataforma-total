# 5. Proyecto: programa C completo leyendo archivos

> 📚 Curso: **C y C++ — Los Cimientos del Software Moderno** · Lección 5 de 5
> 🗓 Exportado: 18/09/2026 desde Plataforma Total
> 🍅 Sugerencia: 1-2 pomodoros para leer + practicar

---

## 📖 Contenido

```cpp
CONSTRUYE: CONTADOR DE PALABRAS EN C puro
━━━━━━━━━━━━━━━━━━━━━━━━━━━
SPEC: programa que recibe un .txt y reporta líneas, palabras y caracteres (el clásico wc).

  #include <stdio.h>
  int main(int argc, char *argv[]) {           // argc = cuántos args; argv = la lista
      if (argc < 2) {
          printf("Uso: %s archivo.txt
", argv[0]);
          return 1;                            // código de error ≠ 0 = convención de fallo
      }
      FILE *f = fopen(argv[1], "r");
      if (f == NULL) { perror("No pude abrir"); return 1; }        // chequeo de error siempre

      int c, lineas = 0, palabras = 0, caracteres = 0, enPalabra = 0;
      while ((c = fgetc(f)) != EOF) {          // lee caracter a caracter
          caracteres++;
          if (c == '
') lineas++;
          if (c == ' ' || c == '
' || c == '	') enPalabra = 0;
          else if (!enPalabra) { palabras++; enPalabra = 1; }
      }
      fclose(f);                                // LIBERAR el recurso: RAII mental en C
      printf("%d líneas, %d palabras, %d caracteres
", lineas, palabras, caracteres);
      return 0;
  }

  gcc -Wall -o wc wc.c && ./wc nota.txt

EJERCICIO STRETCH: argc>2 soportar varios archivos y sumar; -l flag para solo líneas.
LO QUE REALMENTE APRENDISTE: argc/argv · fopen/fclose · fgetc/EOF · return codes. El ABC de Unix puro.
```

---

## 📝 Quiz de la lección

### 1. ¿Qué return values significan en main C?
- A) Cualquiera
- B) 0 = éxito; ≠0 = falló (la shell lo lee con $? — parte del protocolo Unix)
- C) Nada
- D) 255 siempre
### 2. ¿Por qué fclose(f) explícito importa en C?
- A) No importa
- B) Sin cerrar, fopen queda abiertoy puede agotar file descriptors / corrupt data si escribías
- C) Por estética
- D) Por velocidad

---

## 🔑 Respuestas y explicaciones

**1.** ✅ 0 = éxito; ≠0 = falló (la shell lo lee con $? — parte del protocolo Unix) — El exit code es como los programas 'hablan' entre sí en batch/pipes: vital en scripts.
**2.** ✅ Sin cerrar, fopen queda abiertoy puede agotar file descriptors / corrupt data si escribías — C no tiene with/auto-cleanup: cada recurso abierto necesita su cierre deliberado.

---
✅ Al terminar, marca la lección como completada en la app (📚 Aprender → ✅ Completada)
