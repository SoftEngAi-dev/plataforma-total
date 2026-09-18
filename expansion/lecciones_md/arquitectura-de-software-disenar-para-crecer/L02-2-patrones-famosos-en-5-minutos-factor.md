# 2. Patrones famosos en 5 minutos: Factory, Observer, Strategy, Singleton

> 📚 Curso: **Arquitectura de Software — Diseñar para Crecer** · Lección 2 de 4
> 🗓 Exportado: 18/09/2026 desde Plataforma Total
> 🍅 Sugerencia: 1-2 pomodoros para leer + practicar

---

## 📖 Contenido

```text
DECISIONES CLÁSICAS QUE CARGAN DE VIDA
━━━━━━━━━━━━━━━━━━━━━━━━━━━
FACTORY — crear objetos complejos sin新建 en el código
  def crear_tarea(tipo, datos):
      return {"urgente": TareaUrgente, "normal": Tarea}.get(tipo, Tarea)(datos["titulo"])
  # tu código pide 'una tarea urgente' y la fábrica decide cómo ensamblarla

OBSERVER — avisa a interesados sin conocerlos (eventos)
  1) Eventos que publicas / 2) Suscriptores que reaccionan
  Caso real: compra.confirmada → {email.welcome, stock.descontar, log.registrar} = acoplamiento cero

STRATEGY — algoritmo intercambiable sin ifs gigantes
  def procesar_pago(monto, estrategia): return estrategia.pagar(monto)
  class PagoT/CD/ EffectivePaypal = cambiar por inyección

SINGLETON — UNA instancia global compartida (usar con cuidado: es 'global disfrazado')
  Casos válidos: config/app logger/conexión BD por app — y preferible DI sobre singleton clásico.
DECORATOR — agregar comportamiento envolviendo sin heredar (@cache, @login_required del mundo Python)

Cuándoi REGLA: ¡patrón solo cuando el problema ya LO TIENES! (yagni aplicado a patrones)
```

---

## 📝 Quiz de la lección

### 1. ¿Qué resuelve Observer?
- A) Visualización
- B) Acoplamiento: el emisor publica eventos y los interesados reaccionan sin conocerse entre sí
- C) Bases de datos
- D) Threads
### 2. ¿Cuál antídoto a un if/elif gigante por tipo?
- A) más ifs
- B) Strategy/Polymorphism: cada caso es su propia clase/objeto elegida de un registro y llamada uniformemente
- C) comentarios
- D) más RAM

---

## 🔑 Respuestas y explicaciones

**1.** ✅ Acoplamiento: el emisor publica eventos y los interesados reaccionan sin conocerse entre sí — Desacopla módulos: agregar email-notification NO toca el módulo de compras.
**2.** ✅ Strategy/Polymorphism: cada caso es su propia clase/objeto elegida de un registro y llamada uniformemente — Eliminas el switch monster; añadir un tipo nuevo es código NUEVO, no romper el viejo.

---
✅ Al terminar, marca la lección como completada en la app (📚 Aprender → ✅ Completada)
