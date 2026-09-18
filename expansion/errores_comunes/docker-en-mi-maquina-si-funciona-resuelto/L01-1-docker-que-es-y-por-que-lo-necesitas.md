# ⚠️ Errores comunes — 1. Docker: qué es y por qué lo necesitas

> Docker — 'En Mi Máquina Sí Funciona' Resuelto · Lección 1 · Aprender de los errores (propios y ajenos)

- ❌ «Son lo mismo» → Frente a «¿Diferencia imagen vs contenedor?» lo fácil es confundirse. **Verdad**: Imagen = plantilla inmutable; contenedor = instancia(s) ejecutándose de ella. Como clase vs objeto: defines la imagen una vez, lanzas contenedores a voluntad.
- ❌ «El contenedor es la plantilla» → Frente a «¿Diferencia imagen vs contenedor?» lo fácil es confundirse. **Verdad**: Imagen = plantilla inmutable; contenedor = instancia(s) ejecutándose de ella. Como clase vs objeto: defines la imagen una vez, lanzas contenedores a voluntad.
- ❌ «Usa la nube» → Frente a «¿Por qué un contenedor es más liviano que una VM?» lo fácil es confundirse. **Verdad**: Comparte el kernel del SO anfitrión en vez de emular hardware y llevar SO completo. El aislamiento es por namespaces del kernel: sin hipervisor ni boot de SO.
- ❌ «No tiene SO» → Frente a «¿Por qué un contenedor es más liviano que una VM?» lo fácil es confundirse. **Verdad**: Comparte el kernel del SO anfitrión en vez de emular hardware y llevar SO completo. El aislamiento es por namespaces del kernel: sin hipervisor ni boot de SO.

## 🩹 Antídoto universal
1. Lee el mensaje de error COMPLETO antes de googlear.
2. Pon el error exacto a la IA local y pide explicación, no solución.
3. Documenta el error en tu bitácora: error → causa → fix.
