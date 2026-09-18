# ⚠️ Errores comunes — 2. Imágenes: descargar y listar

> Docker — 'En Mi Máquina Sí Funciona' Resuelto · Lección 2 · Aprender de los errores (propios y ajenos)

- ❌ «Dos contenedores» → Frente a «En -p 8080:80, ¿qué es cada número?» lo fácil es confundirse. **Verdad**: Puerto DE TU MÁQUINA : puerto DEL CONTENEDOR. Mapeo de puertos: localhost:8080 → entra al contenedor en su puerto 80.
- ❌ «CPU y memoria» → Frente a «En -p 8080:80, ¿qué es cada número?» lo fácil es confundirse. **Verdad**: Puerto DE TU MÁQUINA : puerto DEL CONTENEDOR. Mapeo de puertos: localhost:8080 → entra al contenedor en su puerto 80.
- ❌ «Es más nueva» → Frente a «¿Por qué preferir python:3.12-slim sobre python:latest?» lo fácil es confundirse. **Verdad**: Tamaño pequeño Y versión fijada (reproducible); latest es caja sorpresa y pesa GB. Imágenes mínimas + tag exacto = builds rápidos, seguros y deterministas.
- ❌ «Solo por moda» → Frente a «¿Por qué preferir python:3.12-slim sobre python:latest?» lo fácil es confundirse. **Verdad**: Tamaño pequeño Y versión fijada (reproducible); latest es caja sorpresa y pesa GB. Imágenes mínimas + tag exacto = builds rápidos, seguros y deterministas.

## 🩹 Antídoto universal
1. Lee el mensaje de error COMPLETO antes de googlear.
2. Pon el error exacto a la IA local y pide explicación, no solución.
3. Documenta el error en tu bitácora: error → causa → fix.
