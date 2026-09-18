# 12. Clases y objectos: modelar el mundo

> 📚 Curso: **Python — De Cero a Profesional** · Lección 12 de 16
> 🗓 Exportado: 18/09/2026 desde Plataforma Total
> 🍅 Sugerencia: 1-2 pomodoros para leer + practicar

---

## 📖 Contenido

```python
POO PITÓNICA: CLASES SENCILLAS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  class Tarea:
      def __init__(self, titulo):          # constructor
          self.titulo = titulo
          self.completada = False

      def completar(self):
          self.completada = True

      def __repr__(self):                   # print bonito
          return f"Tarea({self.titulo!r}, hecha={self.completada})"

  t = Tarea("Estudiar POO")
  t.completar()

HERENCIA (usa con moderación)
  class TareaUrgente(Tarea):
      def __init__(self, titulo, dias):
          super().__init__(titulo)          # llama al padre
          self.dias = dias

DUNDER (métodos especiales): __init__ · __repr__ · __len__ · __eq__ → tu clase se comporta como las nativas.

DATACLASS — clases que solo guardan datos (elimina boilerplate):
  from dataclasses import dataclass
  @dataclass
  class Punto:
      x: float
      y: float
  Punto(1, 2) + __repr__ + __eq__ gratis.
```

---

## 📝 Quiz de la lección

### 1. ¿Qué hace self en un método?
- A) Decoración
- B) Referencia a la instancia actual: sus atributos y métodos
- C) Importar la clase
- D) Nada
### 2. ¿Qué gana @dataclass?
- A) Más velocidad
- B) init, repr y eq automáticos para clases de datos
- C) Herencia
- D) Async

---

## 🔑 Respuestas y explicaciones

**1.** ✅ Referencia a la instancia actual: sus atributos y métodos — self es cómo el método sabe sobre QUÉ objeto concreto opera.
**2.** ✅ init, repr y eq automáticos para clases de datos — Modelos limpios sin boilerplate: escribes los campos y todo lo demás llega gratis.

---
✅ Al terminar, marca la lección como completada en la app (📚 Aprender → ✅ Completada)
