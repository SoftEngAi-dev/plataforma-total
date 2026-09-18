# ⚡ Cheatsheet — 5. Proyecto: API Go real + binario listo para producción

> Go — El Lenguaje de la Nube · Lección 5 · 18/09/2026

## 💡 Idea central
CONSTRUYE: API DE NOTAS GO

## 🧠 Autoexamen (tápate la respuesta)
- **¿Qué permite go build + cross-compilation?** → Un único binario estático por SO/arquitectura sin dependencias: deployment es 'copiar y correr' _(produce.exe final: sin JVM/python en el server — eso lo aprecian mucho en operaciones.)_
- **¿Por qué sync.RWMutex con la slice global en la API?** → Lecturas/escrituras concurrentes sobre memoria compartida pueden corromperse: el mutex las sincroniza _(Varios requests golpean la misma estructura a la vez: sincronización obligatoria o data race.)_

## 🔁 Repaso espaciado sugerido
Hoy → mañana → dentro de 3 días → dentro de una semana. 5 minutos bastan.
