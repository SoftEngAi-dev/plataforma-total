# ⚠️ Errores comunes — 4. Volúmenes, redes y docker-compose: demasiado para la vida real

> Docker — 'En Mi Máquina Sí Funciona' Resuelto · Lección 4 · Aprender de los errores (propios y ajenos)

- ❌ «No puede guardar» → Frente a «¿Por qué un contenedor no debe guardar datos importantes adentro?» lo fácil es confundirse. **Verdad**: Es efímero/desmontable: los datos persistentes van en volúmenes. Contenedor descartable + volumen persistente = patrón sano.
- ❌ «Por velocidad» → Frente a «¿Por qué un contenedor no debe guardar datos importantes adentro?» lo fácil es confundirse. **Verdad**: Es efímero/desmontable: los datos persistentes van en volúmenes. Contenedor descartable + volumen persistente = patrón sano.
- ❌ «Es más rápido» → Frente a «¿Qué ventaja tiene docker compose sobre docker run largos?» lo fácil es confundirse. **Verdad**: Todo el stack (app+db+caché) versionado en un YAML: up/down con una orden. El stack completo se define, comparte y levanta reproduciblemente — adiós README de 40 pasos.
- ❌ «Menos memoria» → Frente a «¿Qué ventaja tiene docker compose sobre docker run largos?» lo fácil es confundirse. **Verdad**: Todo el stack (app+db+caché) versionado en un YAML: up/down con una orden. El stack completo se define, comparte y levanta reproduciblemente — adiós README de 40 pasos.

## 🩹 Antídoto universal
1. Lee el mensaje de error COMPLETO antes de googlear.
2. Pon el error exacto a la IA local y pide explicación, no solución.
3. Documenta el error en tu bitácora: error → causa → fix.
