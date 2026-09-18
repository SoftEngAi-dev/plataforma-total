# 1. El sistema de archivos y navegación

> 📚 Curso: **Linux y Terminal — El Superpoder del Dev** · Lección 1 de 6
> 🗓 Exportado: 18/09/2026 desde Plataforma Total
> 🍅 Sugerencia: 1-2 pomodoros para leer + practicar

---

## 📖 Contenido

```bash
EL ÁRBOL DE LINUX HACIA ADENTRO
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
TODO es un archivo a partir de /
  /home/tu_usuario      ← tu casa (~)  ·  /etc configs  ·  /var logs  ·  /usr programas

NAVEGAR
  pwd · ls -lah  (larga+ocultos+humanos) · cd ruta/relativa o /absoluta
  cd ~  ·  cd -  (anterior)  ·  cd ..
  tree            (ver estructura en árbol — instálalo)
  find . -name "*.py"        → buscar archivos por nombre
  locate archivo / which python3  → dónde está un comando

CREAR/MOVER/COPIAR/BORRAR
  mkdir -p a/b/c    (cree todo el camino)
  cp -r origen destino (-r copia carpetas) · mv (mover/renombrar) · rm -i (pregunta)

COMODINES: *.py · archivo?.txt · [abc].txt
HISTORIAL: history · Ctrl+R búsqueda · !! repetir último

TAB TAB TAB: el autocompletar es la mitad de la velocidad de un pro de terminal.
```

---

## 📝 Quiz de la lección

### 1. ¿Qué hace mkdir -p a/b/c?
- A) Borra a/b/c
- B) Crea la ruta completa incluidos padres intermedios sin error
- C) Cambia permisos
- D) Mueve archivos
### 2. rm -r lo que hace peligroso es que...
- A) existe
- B) Linux NO tiene papelera: lo borrado por rm se fue (por eso rm -i o trash tools)
- C) es root
- D) es lento

---

## 🔑 Respuestas y explicaciones

**1.** ✅ Crea la ruta completa incluidos padres intermedios sin error — Sin -p falla si 'a' no existe; con -p crea todo el camino.
**2.** ✅ Linux NO tiene papelera: lo borrado por rm se fue (por eso rm -i o trash tools) — Cuidado con rm: la ruta / o comodines mal puestos borran todo sin preguntar.

---
✅ Al terminar, marca la lección como completada en la app (📚 Aprender → ✅ Completada)
