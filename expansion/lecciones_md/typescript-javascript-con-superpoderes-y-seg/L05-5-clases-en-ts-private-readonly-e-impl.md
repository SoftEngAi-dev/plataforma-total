# 5. Clases en TS: private, readonly e implements

> 📚 Curso: **TypeScript — JavaScript con Superpoderes y Seguridad** · Lección 5 de 7
> 🗓 Exportado: 18/09/2026 desde Plataforma Total
> 🍅 Sugerencia: 1-2 pomodoros para leer + practicar

---

## 📖 Contenido

```javascript
POO SERIA CON VISIBILIDAD
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  class Cuenta {
    private saldo: number;          // solo accesible dentro
    readonly titular: string;       // no reasignable fuera del init

    constructor(titular: string) {
      this.titular = titular;
      this.saldo = 0;
    }

    depositar(monto: number): number {
      if (monto <= 0) throw new Error("Monto debe ser positivo");
      return this.saldo += monto;
    }
    getSaldo(): number { return this.saldo; }
  }

IMPLEMENTS: contratos explícitos (fundamental con DI y testing)
  interface Repositorio<T> { guardar(item: T): void; obtener(id: number): T | undefined; }
  class RepoMemoria implements Repositorio<Tarea> { ... }

ACCESO POR DEFECTO = public. Escribe private explícito: documenta.

QUÍMICA CON INTERFACES: programa contra la interface, no la clase concreta → mañana cambias RepoMemoria por RepoSQLite y NADIE más se entera. Esto es la base de la arquitectura limpia y el testing con mocks.
```

---

## 📝 Quiz de la lección

### 1. ¿Qué permite una propiedad private?
- A) Acceso desde任何地方
- B) Solo acceso dentro de la propia clase
- C) Solo lectura universal
- D) Nada, es decorativa
### 2. ¿Para qué sirve implements?
- A) Copiar código de otra clase
- B) Obligar a la clase a cumplir el contrato de una interface
- C) Importar módulos
- D) Hacer públicas las props

---

## 🔑 Respuestas y explicaciones

**1.** ✅ Solo acceso dentro de la propia clase — Encapsulación: el estado interno solo cambia por métodos controlados.
**2.** ✅ Obligar a la clase a cumplir el contrato de una interface — El compilador verifica que cumples el contrato — la base de sustituir implementaciones (mocks, DBs).

---
✅ Al terminar, marca la lección como completada en la app (📚 Aprender → ✅ Completada)
