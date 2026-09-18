# ⚠️ Errores comunes — 13. Módulos, paquetes y entornos virtuales

> Python — De Cero a Profesional · Lección 13 · Aprender de los errores (propios y ajenos)

- ❌ «Al socket» → Frente a «¿Qué protege if __name__ == '__main__'?» lo fácil es confundirse. **Verdad**: El código solo corre al EJECUTAR el archivo, no al importarlo. Permite archivos que son a la vez librería (importar) y script (correr).
- ❌ «Los tipos» → Frente a «¿Qué protege if __name__ == '__main__'?» lo fácil es confundirse. **Verdad**: El código solo corre al EJECUTAR el archivo, no al importarlo. Permite archivos que son a la vez librería (importar) y script (correr).
- ❌ «Es más corto» → Frente a «¿Por qué python3 -m src.main y no python3 src/main.py?» lo fácil es confundirse. **Verdad**: Con -m, los imports relativos del paquete funcionan; con ruta directa suelen romperse. -m ejecuta como módulo del paquete: los from tareas import resuelven bonito.
- ❌ «Es lo mismo» → Frente a «¿Por qué python3 -m src.main y no python3 src/main.py?» lo fácil es confundirse. **Verdad**: Con -m, los imports relativos del paquete funcionan; con ruta directa suelen romperse. -m ejecuta como módulo del paquete: los from tareas import resuelven bonito.

## 🩹 Antídoto universal
1. Lee el mensaje de error COMPLETO antes de googlear.
2. Pon el error exacto a la IA local y pide explicación, no solución.
3. Documenta el error en tu bitácora: error → causa → fix.
