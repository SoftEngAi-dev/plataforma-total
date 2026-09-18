# 10. Errores con gracia: try/except profesional

> 📚 Curso: **Python — De Cero a Profesional** · Lección 10 de 16
> 🗓 Exportado: 18/09/2026 desde Plataforma Total
> 🍅 Sugerencia: 1-2 pomodoros para leer + practicar

---

## 📖 Contenido

```python
EXCEPCIONES: FALLAR ES NORMAL, CAPTÚRALAS CON ESTILO
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  try:
      edad = int(input("Edad: "))
      print(100 / edad)
  except ValueError:
      print("Eso no era un número")
  except ZeroDivisionError:
      print("No puedo dividir por cero")
  except FileNotFoundError as e:
      print(f"Archivo no hallado: {e}")
  except Exception as e:            # red de última instancia
      print(f"Error inesperado: {e}")
  else:
      print("Todo OK")              # corre solo si NO hubo excepción
  finally:
      conexion.close()              # SIEMPRE corre (limpieza)

REGLAS PROFESIONALES
1. Captura EXCEPCIONES ESPECÍFICAS (ValueError, no except: desnudo)
2. Fail fast en el límite (input/archivo/red); propaga hacia quién puede decidir
3. Los errores esperados (archivo perdido) → comportamiento previsible: default, reintento, mensaje
4. LANZA tú también: raise ValueError("monto debe ser positivo")

Un crash con buen mensaje > silencio con datos corruptos.
```

---

## 📝 Quiz de la lección

### 1. ¿Qué bloque corre SIEMPRE, haya o no excepción?
- A) try
- B) except
- C) else
- D) finally
### 2. raise ValueError('x') sirve para...
- A) Matar el programa
- B) Lanzar tu propio error con mensaje claro cuando detectas un estado inválido
- C) Imprimir errores
- D) Ignorar errores

---

## 🔑 Respuestas y explicaciones

**1.** ✅ finally — finally = limpieza garantizada (cerrar archivos, conexiones).
**2.** ✅ Lanzar tu propio error con mensaje claro cuando detectas un estado inválido — Valida pronto, falla fuerte y con mensaje: debugging agradecido.

---
✅ Al terminar, marca la lección como completada en la app (📚 Aprender → ✅ Completada)
