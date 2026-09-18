# ⚠️ Errores comunes — 4. Compilar y depurar: gcc, make y headers

> C y C++ — Los Cimientos del Software Moderno · Lección 4 · Aprender de los errores (propios y ajenos)

- ❌ «Ninguna» → Frente a «¿Cuál es la diferencia .h vs .c en C?» lo fácil es confundirse. **Verdad**: .h declara (interfaz pública) y .c define (implementación): separación contrato/código. El header es la 'API' del módulo; main lo incluye sin ver su implementación.
- ❌ «.h es más rápido» → Frente a «¿Cuál es la diferencia .h vs .c en C?» lo fácil es confundirse. **Verdad**: .h declara (interfaz pública) y .c define (implementación): separación contrato/código. El header es la 'API' del módulo; main lo incluye sin ver su implementación.
- ❌ «Todo de nuevo» → Frente a «¿Qué hace make con un Makefile bien escrito?» lo fácil es confundirse. **Verdad**: Recompila SOLO los archivos cuyos fuentes cambiaron (build incremental con dependencias). Dependencias+reglas: el build incremental nació aquí (todo build system actual lo hereda).
- ❌ «Instala paquetes» → Frente a «¿Qué hace make con un Makefile bien escrito?» lo fácil es confundirse. **Verdad**: Recompila SOLO los archivos cuyos fuentes cambiaron (build incremental con dependencias). Dependencias+reglas: el build incremental nació aquí (todo build system actual lo hereda).

## 🩹 Antídoto universal
1. Lee el mensaje de error COMPLETO antes de googlear.
2. Pon el error exacto a la IA local y pide explicación, no solución.
3. Documenta el error en tu bitácora: error → causa → fix.
