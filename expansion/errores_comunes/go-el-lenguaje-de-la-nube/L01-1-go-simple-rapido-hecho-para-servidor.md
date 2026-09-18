# ⚠️ Errores comunes — 1. Go: simple, rápido, hecho para servidores

> Go — El Lenguaje de la Nube · Lección 1 · Aprender de los errores (propios y ajenos)

- ❌ «Es bonito» → Frente a «¿Qué ventaja especial tiene el build de Go?» lo fácil es confundirse. **Verdad**: Genera UN binario nativo sin dependencias externas: el despliegue es copiar un archivo. Un solo ELF/EXE estático: las imágenes docker de Go pueden pesar 5MB.
- ❌ «Corre en browser» → Frente a «¿Qué ventaja especial tiene el build de Go?» lo fácil es confundirse. **Verdad**: Genera UN binario nativo sin dependencias externas: el despliegue es copiar un archivo. Un solo ELF/EXE estático: las imágenes docker de Go pueden pesar 5MB.
- ❌ «Asignar» → Frente a «¿Qué hace := en Go?» lo fácil es confundirse. **Verdad**: Declarar variable nueva con tipo INFERIDO (vs var x int explícita para el init). x := 5 = declarar+inicializar inferido; var para declaraciones sin valor inicial.
- ❌ «Comparar» → Frente a «¿Qué hace := en Go?» lo fácil es confundirse. **Verdad**: Declarar variable nueva con tipo INFERIDO (vs var x int explícita para el init). x := 5 = declarar+inicializar inferido; var para declaraciones sin valor inicial.

## 🩹 Antídoto universal
1. Lee el mensaje de error COMPLETO antes de googlear.
2. Pon el error exacto a la IA local y pide explicación, no solución.
3. Documenta el error en tu bitácora: error → causa → fix.
