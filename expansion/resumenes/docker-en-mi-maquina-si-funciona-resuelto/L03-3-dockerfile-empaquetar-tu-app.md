# ⚡ Cheatsheet — 3. Dockerfile: empaquetar TU app

> Docker — 'En Mi Máquina Sí Funciona' Resuelto · Lección 3 · 18/09/2026

## 💡 Idea central
TU PROPIA IMAGEN: DOCKERFILE

## 🧠 Autoexamen (tápate la respuesta)
- **¿Por qué COPY requirements.txt . va ANTES de COPY . .?** → Cache de capas: cambiar el CÓDIGO no reinstala las dependencias (build rápido) _(Capas inmutables cacheadas: poner lo que menos cambia arriba maximiza reuso.)_
- **¿Qué hace CMD ["python", "app.py"]?** → Define el comando por defecto al arrancar el contenedor _(ENTRYPOINT+CMD definen el proceso principal: un contenedor sano = un proceso.)_

## 🔁 Repaso espaciado sugerido
Hoy → mañana → dentro de 3 días → dentro de una semana. 5 minutos bastan.
