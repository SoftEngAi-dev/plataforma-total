# ⚠️ Errores comunes — 2. GitHub Actions desde cero: tu primer workflow

> DevOps y CI/CD — De Tu PC a Producción Sin Sudor · Lección 2 · Aprender de los errores (propios y ajenos)

- ❌ «Es tu PC» → Frente a «¿Qué hace runs-on: ubuntu-latest?» lo fácil es confundirse. **Verdad**: Define la imagen de máquina virtual limpia de GitHub que ejecutará el job. Cada job arranca en una VM limpia; por eso hay que instalar dependencias en los steps.
- ❌ «El sistema del repo» → Frente a «¿Qué hace runs-on: ubuntu-latest?» lo fácil es confundirse. **Verdad**: Define la imagen de máquina virtual limpia de GitHub que ejecutará el job. Cada job arranca en una VM limpia; por eso hay que instalar dependencias en los steps.
- ❌ «en src/» → Frente a «¿Dónde debe vivir el archivo del workflow?» lo fácil es confundirse. **Verdad**: .github/workflows/*.yml. GitHub solo reconoce los workflows en esa ruta exacta.
- ❌ «en la raíz» → Frente a «¿Dónde debe vivir el archivo del workflow?» lo fácil es confundirse. **Verdad**: .github/workflows/*.yml. GitHub solo reconoce los workflows en esa ruta exacta.

## 🩹 Antídoto universal
1. Lee el mensaje de error COMPLETO antes de googlear.
2. Pon el error exacto a la IA local y pide explicación, no solución.
3. Documenta el error en tu bitácora: error → causa → fix.
