# ⚠️ Errores comunes — 3. Instalar y gestionar paquetes (todo por terminal)

> Herramientas del Desarrollador · Lección 3 · Aprender de los errores (propios y ajenos)

- ❌ «Acelerar el código» → Frente a «¿Para qué sirve un virtualenv en Python?» lo fácil es confundirse. **Verdad**: Aislar las dependencias de cada proyecto para que no choquen. Cada proyecto tiene su propio set de paquetes/versions; nunca chocan.
- ❌ «Compilar Python más rápido» → Frente a «¿Para qué sirve un virtualenv en Python?» lo fácil es confundirse. **Verdad**: Aislar las dependencias de cada proyecto para que no choquen. Cada proyecto tiene su propio set de paquetes/versions; nunca chocan.
- ❌ «Crea el archivo de dependencias» → Frente a «¿Qué hace `pip install -r requirements.txt`?» lo fácil es confundirse. **Verdad**: Instala todas las dependencias registradas del proyecto. La forma estándar de reproducir el entorno de un proyecto en cualquier máquina.
- ❌ «Actualiza pip» → Frente a «¿Qué hace `pip install -r requirements.txt`?» lo fácil es confundirse. **Verdad**: Instala todas las dependencias registradas del proyecto. La forma estándar de reproducir el entorno de un proyecto en cualquier máquina.

## 🩹 Antídoto universal
1. Lee el mensaje de error COMPLETO antes de googlear.
2. Pon el error exacto a la IA local y pide explicación, no solución.
3. Documenta el error en tu bitácora: error → causa → fix.
