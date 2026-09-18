# 8. Índices y transacciones: velocidad y seguridad

> 📚 Curso: **SQL y Bases de Datos — Datos que Persisten** · Lección 8 de 10
> 🗓 Exportado: 18/09/2026 desde Plataforma Total
> 🍅 Sugerencia: 1-2 pomodoros para leer + practicar

---

## 📖 Contenido

```sql
ÍNDICES: DEL O(n) AL O(log n)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Sin índice, buscar email es leer TODA la tabla. Con índice, es un árbol: rapidísimo.
  CREATE INDEX idx_email ON usuarios(email);       -- UNIQUE INDEX si corresponde
  Regla práctica: indexa columnas de WHERE frecuente/JOIN. Demasiados índices frenan los INSERT.

EXPLAIN QUERY PLAN SELECT ...    ← descubre si tu consulta usa índice

TRANSACCIONES: TODO O NADA
  BEGIN;
  UPDATE cuentas SET saldo = saldo - 100 WHERE id = 1;
  UPDATE cuentas SET saldo = saldo + 100 WHERE id = 2;
  COMMIT;        -- guardar; ROLLBACK; deshacer todo

Si algo falla en el medio, ROLLBACK: la plata no aparece ni desaparece en el aire.

ACID (lo que una transacción garantiza): Atomicidad (todo/nada), Consistencia, Aislamiento (otras sesiones no ven datos a medio camino), Durabilidad (commit = disco).

EN PYTHON: con sqlite3: con = sqlite3.connect(...); con.commit() o rollback();  with con: hace commit/rollback automáticamente.
```

---

## 📝 Quiz de la lección

### 1. ¿Cuándo crear un índice?
- A) En todas las columnas siempre
- B) En columnas usadas frecuentemente en WHERE/JOIN (con costo de escritura)
- C) Nunca
- D) Solo en PK
### 2. ¿Qué garantiza una transacción bancaria (BEGIN...COMMIT)?
- A) Velocidad
- B) Las dos actualizaciones suceden juntas o ninguna (atomicidad)
- C) Orden alfabético
- D) Backup

---

## 🔑 Respuestas y explicaciones

**1.** ✅ En columnas usadas frecuentemente en WHERE/JOIN (con costo de escritura) — Índices aceleran lecturas pero encarecen escrituras: sobredimensionarlos es deuda.
**2.** ✅ Las dos actualizaciones suceden juntas o ninguna (atomicidad) — Si falla a mitad, ROLLBACK: nunca hay dinero perdido en el aire.

---
✅ Al terminar, marca la lección como completada en la app (📚 Aprender → ✅ Completada)
