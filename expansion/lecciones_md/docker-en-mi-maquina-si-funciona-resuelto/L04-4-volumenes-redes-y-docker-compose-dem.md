# 4. Volúmenes, redes y docker-compose: demasiado para la vida real

> 📚 Curso: **Docker — 'En Mi Máquina Sí Funciona' Resuelto** · Lección 4 de 5
> 🗓 Exportado: 18/09/2026 desde Plataforma Total
> 🍅 Sugerencia: 1-2 pomodoros para leer + practicar

---

## 📖 Contenido

```dockerfile
MÁS ALLÁ DEL CONTENEDOR EFÍMERO
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
DATOS QUE SOBREVIVEN: un contenedor es descartable; una BD que borra datos al reiniciarse no sirve.
  docker run -v $(pwd)/datos:/app/datos mi-app     # volumen: carpeta de tu máquina montada adentro

REDES: contenedores que hablan entre ellos por NOMBRE:
  docker network create mired
  docker run --network mired --name db postgres:16
  docker run --network mired mi-app                # la app llega a db con host "db"

DOCKER-COMPOSE: TODO EL STACK EN UN ARCHIVO (el estándar rey)
  # docker-compose.yml
  services:
    web:
      build: .
      ports: ["8000:8000"]
      environment: ["DB_URL=postgres://db/notas"]
      depends_on: [db]
    db:
      image: postgres:16
      volumes: ["pgdata:/var/lib/postgresql/data"]
      environment: ["POSTGRES_PASSWORD=dev"]
  volumes: { pgdata: {} }

  docker compose up -d      ← todo el sistema con UNA orden
  docker compose down       ← limpiar todo

Dev local con DB real, cero instalación local: por eso compose ganó.
```

---

## 📝 Quiz de la lección

### 1. ¿Por qué un contenedor no debe guardar datos importantes adentro?
- A) No puede guardar
- B) Es efímero/desmontable: los datos persistentes van en volúmenes
- C) Por velocidad
- D) Solo en producción
### 2. ¿Qué ventaja tiene docker compose sobre docker run largos?
- A) Es más rápido
- B) Todo el stack (app+db+caché) versionado en un YAML: up/down con una orden
- C) Menos memoria
- D) Solo para Windows

---

## 🔑 Respuestas y explicaciones

**1.** ✅ Es efímero/desmontable: los datos persistentes van en volúmenes — Contenedor descartable + volumen persistente = patrón sano.
**2.** ✅ Todo el stack (app+db+caché) versionado en un YAML: up/down con una orden — El stack completo se define, comparte y levanta reproduciblemente — adiós README de 40 pasos.

---
✅ Al terminar, marca la lección como completada en la app (📚 Aprender → ✅ Completada)
