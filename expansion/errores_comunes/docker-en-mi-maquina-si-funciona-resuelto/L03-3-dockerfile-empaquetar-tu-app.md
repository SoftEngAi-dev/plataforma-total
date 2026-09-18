# ⚠️ Errores comunes — 3. Dockerfile: empaquetar TU app

> Docker — 'En Mi Máquina Sí Funciona' Resuelto · Lección 3 · Aprender de los errores (propios y ajenos)

- ❌ «Orden alfabético» → Frente a «¿Por qué COPY requirements.txt . va ANTES de COPY . .?» lo fácil es confundirse. **Verdad**: Cache de capas: cambiar el CÓDIGO no reinstala las dependencias (build rápido). Capas inmutables cacheadas: poner lo que menos cambia arriba maximiza reuso.
- ❌ «Es más seguro» → Frente a «¿Por qué COPY requirements.txt . va ANTES de COPY . .?» lo fácil es confundirse. **Verdad**: Cache de capas: cambiar el CÓDIGO no reinstala las dependencias (build rápido). Capas inmutables cacheadas: poner lo que menos cambia arriba maximiza reuso.
- ❌ «Instala python» → Frente a «¿Qué hace CMD ["python", "app.py"]?» lo fácil es confundirse. **Verdad**: Define el comando por defecto al arrancar el contenedor. ENTRYPOINT+CMD definen el proceso principal: un contenedor sano = un proceso.
- ❌ «Abre una shell» → Frente a «¿Qué hace CMD ["python", "app.py"]?» lo fácil es confundirse. **Verdad**: Define el comando por defecto al arrancar el contenedor. ENTRYPOINT+CMD definen el proceso principal: un contenedor sano = un proceso.

## 🩹 Antídoto universal
1. Lee el mensaje de error COMPLETO antes de googlear.
2. Pon el error exacto a la IA local y pide explicación, no solución.
3. Documenta el error en tu bitácora: error → causa → fix.
