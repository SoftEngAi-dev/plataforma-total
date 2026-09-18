# 2. Leer, buscar y tuberías: la filosofía Unix

> 📚 Curso: **Linux y Terminal — El Superpoder del Dev** · Lección 2 de 6
> 🗓 Exportado: 18/09/2026 desde Plataforma Total
> 🍅 Sugerencia: 1-2 pomodoros para leer + practicar

---

## 📖 Contenido

```bash
COMANDOS PEQUEÑOS, CADENAS POTENTES (|)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
LEER
  cat archivo        (todo) · less archivo (paginado, / busca, q sale) · head -20 (principio) · tail -f log (seguir EN VIVO — el que usarás en servidores)

BUSCAR EN CONTENIDO
  grep -rn "TODO" .        (recursivo con números de línea)
  grep -i error log.txt    (ignora mayúsculas)

TUBERÍAS |: la salida de uno es la entrada del siguiente — ¡ESTA ES la magia Unix!
  cat log.txt | grep ERROR | wc -l            → cuántos errores hay
  history | grep docker                       → cuándo usé docker
  ls -lh | sort -k5 -h -r                     → ordenar por tamaño

REDIRECCIÓN
  comando > salida.txt    (guardar, BORRA el archivo)
  comando >> log.txt      (AGREGAR al final: es vital distinguir)
  comando 2>&1            (mandar errores al mismo flujo)

SU Y PERMISOS
  sudo comando     → ejecutar como admin (con respeto: puede romper el sistema)
```

---

## 📝 Quiz de la lección

### 1. cat log | grep ERROR | wc -l hace...
- A) Muestra todo
- B) Cuenta las líneas del log que contienen ERROR (tuberías encadenadas)
- C) Borra errores
- D) Nada si hay error
### 2. ¿Diferencia entre > y >>?
- A) Ninguna
- B) > SOBRESCRIBE el archivo; >> AGREGA al final
- C) >> es para errores
- D) Es más rápido >>

---

## 🔑 Respuestas y explicaciones

**1.** ✅ Cuenta las líneas del log que contienen ERROR (tuberías encadenadas) — Filtro → contador: las tuberías componen herramientas con texto crudo.
**2.** ✅ > SOBRESCRIBE el archivo; >> AGREGA al final — Confundirlos = perder archivos (factor real de incidentes).

---
✅ Al terminar, marca la lección como completada en la app (📚 Aprender → ✅ Completada)
