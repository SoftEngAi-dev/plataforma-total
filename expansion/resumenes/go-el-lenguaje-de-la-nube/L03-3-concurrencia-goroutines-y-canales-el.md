# ⚡ Cheatsheet — 3. Concurrencia: goroutines y canales (el superpoder)

> Go — El Lenguaje de la Nube · Lección 3 · 18/09/2026

## 💡 Idea central
GOROUTINES: 10.000 TAREAS A LA VEZ

## 🧠 Autoexamen (tápate la respuesta)
- **¿Qué crea la palabra go delante de una llamada?** → Una goroutine: la función corre concurrentemente sin bloquear _(go f() = paralelo livianísimo: miles concurrentes con MB de RAM, no GB.)_
- **¿Para qué sirve un channel en Go?** → Comunicación tipada y segura entre goroutines: enviar/recibir datos sin locks manuales _(channels = tubería sincronizada entre tareas concurrentes: el camino GOnativo.)_

## 🔁 Repaso espaciado sugerido
Hoy → mañana → dentro de 3 días → dentro de una semana. 5 minutos bastan.
