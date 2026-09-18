# 1. Docker: qué es y por qué lo necesitas

> 📚 Curso: **Docker — 'En Mi Máquina Sí Funciona' Resuelto** · Lección 1 de 5
> 🗓 Exportado: 18/09/2026 desde Plataforma Total
> 🍅 Sugerencia: 1-2 pomodoros para leer + practicar

---

## 📖 Contenido

```dockerfile
CONTENEDORES: EMBALAJE ESTÁNDAR DE SOFTWARE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PROBLEMA: "en mi máquina sí funciona" — Python 3.11 vs 3.9, librerías distintas, configs distintas.
SOLUCIÓN: contenedor = tu app + todo su entorno exacto empaquetados en una caja estándar que corre IDÉNTICA en cualquier Linux/Windows/Mac/Servidor.

VM vs CONTENEDOR
• VM: emula hardware completo + SO completo (GB, minutos de arranque)
• Contenedor: comparte el kernel del anfitrión (MB, milisegundos, aislado así mismo)

IMAGEN vs CONTENEDOR (la confusión de todos)
• Imagen = la plantilla inmutable (la clase)
• Contenedor = instancia corriendo de la imagen (el objeto)
Una imagen, mil contenedores iguales en segundos.

INSTALAR: docker.com (Docker Desktop Win/Mac, Engine Linux). Verifica:
  docker run hello-world

LOS 5 COMANDOS DIARIOS: docker build (crear imagen) · run (ejecutar) · ps (ver corriendo) · stop · logs (qué pasó adentro)
```

---

## 📝 Quiz de la lección

### 1. ¿Diferencia imagen vs contenedor?
- A) Son lo mismo
- B) Imagen = plantilla inmutable; contenedor = instancia(s) ejecutándose de ella
- C) El contenedor es la plantilla
- D) Imagen es solo para web
### 2. ¿Por qué un contenedor es más liviano que una VM?
- A) Usa la nube
- B) Comparte el kernel del SO anfitrión en vez de emular hardware y llevar SO completo
- C) No tiene SO
- D) Solo para Linux

---

## 🔑 Respuestas y explicaciones

**1.** ✅ Imagen = plantilla inmutable; contenedor = instancia(s) ejecutándose de ella — Como clase vs objeto: defines la imagen una vez, lanzas contenedores a voluntad.
**2.** ✅ Comparte el kernel del SO anfitrión en vez de emular hardware y llevar SO completo — El aislamiento es por namespaces del kernel: sin hipervisor ni boot de SO.

---
✅ Al terminar, marca la lección como completada en la app (📚 Aprender → ✅ Completada)
