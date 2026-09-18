# ⚠️ Errores comunes — 5. Proyecto: dockeriza tu app + publica

> Docker — 'En Mi Máquina Sí Funciona' Resuelto · Lección 5 · Aprender de los errores (propios y ajenos)

- ❌ «La hace más lenta» → Frente a «¿Por qué nunca incluir secretos DENTRO de la imagen Docker?» lo fácil es confundirse. **Verdad**: Las capas de la imagen son legibles por cualquiera que la tenga/descargue: filtras las claves. Secretos al correr (-e / compose env), nunca al build: la imagen te repite.
- ❌ «Docker lo prohíbe» → Frente a «¿Por qué nunca incluir secretos DENTRO de la imagen Docker?» lo fácil es confundirse. **Verdad**: Las capas de la imagen son legibles por cualquiera que la tenga/descargue: filtras las claves. Secretos al correr (-e / compose env), nunca al build: la imagen te repite.
- ❌ «Solo docker run» → Frente a «¿Qué combina este proyecto como cierre del curso?» lo fácil es confundirse. **Verdad**: Dockerfile + build + volúmenes + compose + push al registry. El ciclo completo real: de tu código a imagen publicada y ejecutable en cualquier máquina.
- ❌ «Solo Kubernetes» → Frente a «¿Qué combina este proyecto como cierre del curso?» lo fácil es confundirse. **Verdad**: Dockerfile + build + volúmenes + compose + push al registry. El ciclo completo real: de tu código a imagen publicada y ejecutable en cualquier máquina.

## 🩹 Antídoto universal
1. Lee el mensaje de error COMPLETO antes de googlear.
2. Pon el error exacto a la IA local y pide explicación, no solución.
3. Documenta el error en tu bitácora: error → causa → fix.
