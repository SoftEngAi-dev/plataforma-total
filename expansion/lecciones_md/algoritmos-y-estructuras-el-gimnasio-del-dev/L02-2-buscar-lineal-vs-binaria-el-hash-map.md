# 2. Buscar: lineal vs binaria + el hash map

> 📚 Curso: **Algoritmos y Estructuras — El Gimnasio del Dev** · Lección 2 de 5
> 🗓 Exportado: 18/09/2026 desde Plataforma Total
> 🍅 Sugerencia: 1-2 pomodoros para leer + practicar

---

## 📖 Contenido

```text
EL PROBLEMA MÁS IMPORTANTE: ENCONTRAR RÁPIDO
━━━━━━━━━━━━━━━━━━━━━━━━━━━
BÚSQUEDA LINEAL (naif): recorrer todo: O(n)
  def buscar(lista, objetivo):
      for i, x in enumerate(lista):
          if x == objetivo: return i
      return -1

BÚSQUEDA BINARIA (¡solo si está ORDENADA!): divide a la mitad: O(log n) ✨
  def binaria(ordenada, objetivo):
      izq, der = 0, len(ordenada) - 1
      while izq <= der:
          medio = (izq + der) // 2
          if ordenada[medio] == objetivo: return medio
          elif ordenada[medio] < objetivo: izq = medio + 1
          else: der = medio - 1
      return -1
  # 1.000.000 de items: ~20 pasos. ESO es O(log n).

HASH MAP/dict: la herramienta que SUSTITUYE búsquedas mil veces
  por_nombre = {u["nombre"]: u for u in usuarios}     # creas el índice una vez
  por_nombre["ada"]                                    # O(1) para siempre después

REGLA PRO: ¿búsquedas repetidas? crea un dict/set ANTES. Pregunta clásica de entrevista: Two Sum (usa dict para O(n) en vez de O(n²) fuerza bruta).
```

---

## 📝 Quiz de la lección

### 1. ¿Qué requisito tiene la búsqueda binaria?
- A) Ninguno
- B) La lista DEBE estar ordenada (si no, divide mal)
- C) Ser números
- D) Ser única lista
### 2. ¿Cómo convertir múltiples búsquedas O(n) cada una en O(1) cada una?
- A) Más RAM
- B) Construir UN diccionario/hash indexado UNA vez y consultarlo en O(1) luego
- C) Bucle for
- D) SQL

---

## 🔑 Respuestas y explicaciones

**1.** ✅ La lista DEBE estar ordenada (si no, divide mal) — binaria=O(log n) pero necesita order previamente: a veces n log n+bar vale
**2.** ✅ Construir UN diccionario/hash indexado UNA vez y consultarlo en O(1) luego — Trade tiempo-por-memoria: indexar=prepagar para buscar barato.

---
✅ Al terminar, marca la lección como completada en la app (📚 Aprender → ✅ Completada)
