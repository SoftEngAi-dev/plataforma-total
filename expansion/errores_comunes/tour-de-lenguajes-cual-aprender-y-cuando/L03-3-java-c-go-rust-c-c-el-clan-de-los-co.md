# ⚠️ Errores comunes — 3. Java, C#, Go, Rust, C/C++: el clan de los compilados

> Tour de Lenguajes — Cuál Aprender y Cuándo · Lección 3 · Aprender de los errores (propios y ajenos)

- ❌ «Python» → Frente a «Si quieres trabajar en infraestructura/cloud (k8s, Terraform, etc.), el lenguaje estrella es...» lo fácil es confundirse. **Verdad**: Go: la nube moderna está escrita en él (Docker, Kubernetes, Terraform). Go = lenguaje icu de la nube: binarios únicos + concurrencia nativa.
- ❌ «Java» → Frente a «Si quieres trabajar en infraestructura/cloud (k8s, Terraform, etc.), el lenguaje estrella es...» lo fácil es confundirse. **Verdad**: Go: la nube moderna está escrita en él (Docker, Kubernetes, Terraform). Go = lenguaje icu de la nube: binarios únicos + concurrencia nativa.
- ❌ «Siempre» → Frente a «¿Cuándo C/C++ es la OPCIÓN y no una elección?» lo fácil es confundirse. **Verdad**: Sistemas operativos, drivers, motores gráficos, embebidos, latencia extrema — donde el control hardware es la feature. Cuando nanosegundos/bytes importan como requisito: C/C++ no es viejo, es el cimiento obligado.
- ❌ «Para web APIs» → Frente a «¿Cuándo C/C++ es la OPCIÓN y no una elección?» lo fácil es confundirse. **Verdad**: Sistemas operativos, drivers, motores gráficos, embebidos, latencia extrema — donde el control hardware es la feature. Cuando nanosegundos/bytes importan como requisito: C/C++ no es viejo, es el cimiento obligado.

## 🩹 Antídoto universal
1. Lee el mensaje de error COMPLETO antes de googlear.
2. Pon el error exacto a la IA local y pide explicación, no solución.
3. Documenta el error en tu bitácora: error → causa → fix.
