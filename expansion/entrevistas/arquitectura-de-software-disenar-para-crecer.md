# 🎤 Banco de entrevista — Arquitectura de Software — Diseñar para Crecer

> 8 preguntas esenciales + guía de respuestas las que ya sabes del curso

## 🔥 Fundamentales (del contenido del curso)

1. **¿Qué propone DRY?**
   - El conocimiento/lógica vive UNA sola vez en el sistema; repetición = inconsistencias cuando cambies un lugar y no otro  _(Copiar es rápido hoy; mantener copias divergentes es lento mañana.)_

2. **Dependency Inversion en práctica significa...**
   - Tu lógica depende de INTERFACES/contratos; la implementación concreta se inyecta y puede cambiar (prod↔test)  _(La pieza clave de testabilidad y arquitectura limpia: invierte quién controla las dependencias.)_

3. **¿Qué resuelve Observer?**
   - Acoplamiento: el emisor publica eventos y los interesados reaccionan sin conocerse entre sí  _(Desacopla módulos: agregar email-notification NO toca el módulo de compras.)_

4. **¿Cuál antídoto a un if/elif gigante por tipo?**
   - Strategy/Polymorphism: cada caso es su propia clase/objeto elegida de un registro y llamada uniformemente  _(Eliminas el switch monster; añadir un tipo nuevo es código NUEVO, no romper el viejo.)_

5. **¿Cuál es la mayor ventaja real del monolito modular para una startup?**
   - Velocidad: un despliegue, llamadas internas sin red, debug y refactors baratos mientras el equipo es pequeño  _(El tiempo al mercado es el recurso: el monlito bien diseñado desperdicia menos meses iniciales.)_

6. **¿Cuál costo fijo traen los microservicios que no existe en un monolito?**
   - Distribución: red entre servicios, transacciones complejas, logs distribuidos, deployment/orquestación  _(Cada petición que antes era una llamada local pasa a ser una operación de red que puede fallar.)_

7. **¿Qué ley cumple una buena separación en capas?**
   - Las capas INTERNAS (dominio) no conocen las EXTERNAS (web/DB): lo externo se acopla HACIA el negocio, jamás al revés  _(Invertir la dirección de dependencia = tu lógica de negocio es testeable pura y viva en cualquier envoltorio.)_

8. **Un 'caso de uso' (application service) es...**
   - La orquestación de un objetivo de negocio: 'CrearTarea' coordina el dominio con la infraestructura  _(Las APIs públicas internas de tu app: lo que el mundo puede hacer con tu sistema.)_

## 🧗 Profundización (prepáralas explicando en voz alta)
- ¿Qué problema real resuelve Arquitectura de Software y cuándo NO lo usarías?
- Explica el concepto más fuerte del curso sin usar jerga.
- Contrasta Arquitectura de Software con una alternativa: pros/contras.
- Cuenta un error típico de novato en este tema y cómo lo evitas.

## ⭐ Método para contestarlas
1. **Responde en 60 segundos** cada una de las fundamentales, de memoria. Las que tartamudean → repásalas (flashcards/).
2. Graba tu voz en 2 y escúchate: claridad y precisión importan tanto como el contenido técnico.
3. Una respuesta buena = definición (1 línea) + ejemplo (1) + por qué importa (1).
