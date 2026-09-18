# ⚡ Cheatsheet — 4. Compilar y depurar: gcc, make y headers

> C y C++ — Los Cimientos del Software Moderno · Lección 4 · 18/09/2026

## 💡 Idea central
DE .C A EJECUTABLE REAL (EL FLUJO COMPLETO)

## 🧠 Autoexamen (tápate la respuesta)
- **¿Cuál es la diferencia .h vs .c en C?** → .h declara (interfaz pública) y .c define (implementación): separación contrato/código _(El header es la 'API' del módulo; main lo incluye sin ver su implementación.)_
- **¿Qué hace make con un Makefile bien escrito?** → Recompila SOLO los archivos cuyos fuentes cambiaron (build incremental con dependencias) _(Dependencias+reglas: el build incremental nació aquí (todo build system actual lo hereda).)_

## 🔁 Repaso espaciado sugerido
Hoy → mañana → dentro de 3 días → dentro de una semana. 5 minutos bastan.
