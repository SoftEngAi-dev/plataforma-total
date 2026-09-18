# 🎤 Banco de entrevista — Docker — 'En Mi Máquina Sí Funciona' Resuelto

> 10 preguntas esenciales + guía de respuestas las que ya sabes del curso

## 🔥 Fundamentales (del contenido del curso)

1. **¿Diferencia imagen vs contenedor?**
   - Imagen = plantilla inmutable; contenedor = instancia(s) ejecutándose de ella  _(Como clase vs objeto: defines la imagen una vez, lanzas contenedores a voluntad.)_

2. **¿Por qué un contenedor es más liviano que una VM?**
   - Comparte el kernel del SO anfitrión en vez de emular hardware y llevar SO completo  _(El aislamiento es por namespaces del kernel: sin hipervisor ni boot de SO.)_

3. **En -p 8080:80, ¿qué es cada número?**
   - Puerto DE TU MÁQUINA : puerto DEL CONTENEDOR  _(Mapeo de puertos: localhost:8080 → entra al contenedor en su puerto 80.)_

4. **¿Por qué preferir python:3.12-slim sobre python:latest?**
   - Tamaño pequeño Y versión fijada (reproducible); latest es caja sorpresa y pesa GB  _(Imágenes mínimas + tag exacto = builds rápidos, seguros y deterministas.)_

5. **¿Por qué COPY requirements.txt . va ANTES de COPY . .?**
   - Cache de capas: cambiar el CÓDIGO no reinstala las dependencias (build rápido)  _(Capas inmutables cacheadas: poner lo que menos cambia arriba maximiza reuso.)_

6. **¿Qué hace CMD ["python", "app.py"]?**
   - Define el comando por defecto al arrancar el contenedor  _(ENTRYPOINT+CMD definen el proceso principal: un contenedor sano = un proceso.)_

7. **¿Por qué un contenedor no debe guardar datos importantes adentro?**
   - Es efímero/desmontable: los datos persistentes van en volúmenes  _(Contenedor descartable + volumen persistente = patrón sano.)_

8. **¿Qué ventaja tiene docker compose sobre docker run largos?**
   - Todo el stack (app+db+caché) versionado en un YAML: up/down con una orden  _(El stack completo se define, comparte y levanta reproduciblemente — adiós README de 40 pasos.)_

9. **¿Por qué nunca incluir secretos DENTRO de la imagen Docker?**
   - Las capas de la imagen son legibles por cualquiera que la tenga/descargue: filtras las claves  _(Secretos al correr (-e / compose env), nunca al build: la imagen te repite.)_

10. **¿Qué combina este proyecto como cierre del curso?**
   - Dockerfile + build + volúmenes + compose + push al registry  _(El ciclo completo real: de tu código a imagen publicada y ejecutable en cualquier máquina.)_

## 🧗 Profundización (prepáralas explicando en voz alta)
- ¿Qué problema real resuelve Docker y cuándo NO lo usarías?
- Explica el concepto más fuerte del curso sin usar jerga.
- Contrasta Docker con una alternativa: pros/contras.
- Cuenta un error típico de novato en este tema y cómo lo evitas.

## ⭐ Método para contestarlas
1. **Responde en 60 segundos** cada una de las fundamentales, de memoria. Las que tartamudean → repásalas (flashcards/).
2. Graba tu voz en 2 y escúchate: claridad y precisión importan tanto como el contenido técnico.
3. Una respuesta buena = definición (1 línea) + ejemplo (1) + por qué importa (1).
