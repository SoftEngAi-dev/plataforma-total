# ⚡ Cheatsheet — 5. Proyecto: dockeriza tu app + publica

> Docker — 'En Mi Máquina Sí Funciona' Resuelto · Lección 5 · 18/09/2026

## 💡 Idea central
DOCKERIZA UNA APP TUYA (HOY)

## 🧠 Autoexamen (tápate la respuesta)
- **¿Por qué nunca incluir secretos DENTRO de la imagen Docker?** → Las capas de la imagen son legibles por cualquiera que la tenga/descargue: filtras las claves _(Secretos al correr (-e / compose env), nunca al build: la imagen te repite.)_
- **¿Qué combina este proyecto como cierre del curso?** → Dockerfile + build + volúmenes + compose + push al registry _(El ciclo completo real: de tu código a imagen publicada y ejecutable en cualquier máquina.)_

## 🔁 Repaso espaciado sugerido
Hoy → mañana → dentro de 3 días → dentro de una semana. 5 minutos bastan.
