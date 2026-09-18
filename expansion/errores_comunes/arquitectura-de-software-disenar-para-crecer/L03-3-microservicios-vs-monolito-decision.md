# ⚠️ Errores comunes — 3. Microservicios vs monolito: decisión de adultos

> Arquitectura de Software — Diseñar para Crecer · Lección 3 · Aprender de los errores (propios y ajenos)

- ❌ «Hype» → Frente a «¿Cuál es la mayor ventaja real del monolito modular para una startup?» lo fácil es confundirse. **Verdad**: Velocidad: un despliegue, llamadas internas sin red, debug y refactors baratos mientras el equipo es pequeño. El tiempo al mercado es el recurso: el monlito bien diseñado desperdicia menos meses iniciales.
- ❌ «La nube» → Frente a «¿Cuál es la mayor ventaja real del monolito modular para una startup?» lo fácil es confundirse. **Verdad**: Velocidad: un despliegue, llamadas internas sin red, debug y refactors baratos mientras el equipo es pequeño. El tiempo al mercado es el recurso: el monlito bien diseñado desperdicia menos meses iniciales.
- ❌ «Ninguno» → Frente a «¿Cuál costo fijo traen los microservicios que no existe en un monolito?» lo fácil es confundirse. **Verdad**: Distribución: red entre servicios, transacciones complejas, logs distribuidos, deployment/orquestación. Cada petición que antes era una llamada local pasa a ser una operación de red que puede fallar.
- ❌ «CPU» → Frente a «¿Cuál costo fijo traen los microservicios que no existe en un monolito?» lo fácil es confundirse. **Verdad**: Distribución: red entre servicios, transacciones complejas, logs distribuidos, deployment/orquestación. Cada petición que antes era una llamada local pasa a ser una operación de red que puede fallar.

## 🩹 Antídoto universal
1. Lee el mensaje de error COMPLETO antes de googlear.
2. Pon el error exacto a la IA local y pide explicación, no solución.
3. Documenta el error en tu bitácora: error → causa → fix.
