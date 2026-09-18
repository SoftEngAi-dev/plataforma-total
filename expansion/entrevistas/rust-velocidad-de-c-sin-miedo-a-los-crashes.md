# 🎤 Banco de entrevista — Rust — Velocidad de C sin Miedo a los Crashes

> 10 preguntas esenciales + guía de respuestas las que ya sabes del curso

## 🔥 Fundamentales (del contenido del curso)

1. **¿Qué es diferente de los valores en Rust por defecto?**
   - Inmutables por defecto; declaras mut explícitamente para cambiar valores  _(La inmutabilidad por defecto evita enormes clases de bugs en concurrencia.)_

2. **¿Qué es cargo en el ecosistema Rust?**
   - El todo en uno: compilar, gestionar dependencias (crates), testear, documentar  _(cargo new/run/test/build: el mejor gestor de proyectos del mundo compilado.)_

3. **¿Por qué en Rust `let b = a` con Strings 'mueve' en vez de copiar?**
   - Ownership: solo un dueño por valor para liberar memoria automáticamente de forma segura  _(Si dos dueños intentaran liberar → double-free. Un dueño ya lo sabes: sin GC, sin peligro.)_

4. **¿Qué garantiza que no haya data races en concurrente Rust?**
   - Un solo &mut Sin & lectores, o muchos & pero ningún mut: exclusión mutua GARANTIZADA por el compilador  _('Fearless concurrency': el type system TAN estricto hace im-posibles los race conditions clásicos.)_

5. **¿Qué hace el operador ? tras una llamada Result?**
   - Si es Ok, desenvuelve el valor; si es Err, lo retorna inmediatamente a la función llamante (propagación elegante)  _(El equivalente Go-verboso pero sin boilerplate: error handling conciso y explícito.)_

6. **¿En qué consiste la seguridad adicional de Option<T> vs null?**
   - No hay null: la AUSENCIA es parte del TIPO y el compilador EXIGE manejar el caso None  _(Null = 'agujero invisible'; None = 'la firma te avisa y obliga'. Billion-dollar mistake corregida.)_

7. **¿Qué son los traits de Rust?**
   - Interfaces de comportamiento (comparable a interfaces Java/protocols) implementables por cualquier tipo — aún nativos predefinidos  _(derive(Debug) o impl Trait for MiStruct: comportamiento compartido sin herencia tradicional.)_

8. **¿Qué coste extra tienen los iteradores encadenados de Rust?**
   - Cero: se compilan al mismo código que un bucle for manual (zero-cost abstractions)  _('What you don't use, you don't pay for; what you do, you couldn't hand-code better' = lema.)_

9. **¿Qué hace clap con macros derive?**
   - Genera el parser de argumentos/ayuda de tu CLI desde tus structs automáticamente (--help profesional gratis)  _(Derive: Rust's compile-time code generation — CLI args tipados de regalo.)_

10. **¿Qué desafío famoso te hará 'sentir' ownership en este proyecto?**
   - Elegir entre String (dueña) y &str (prestada) en structs/funcs: la decisión de propiedad explícita  _(Las peleas con el borrow checker te enseñan el modelo: un mes después, es superpoder.)_

## 🧗 Profundización (prepáralas explicando en voz alta)
- ¿Qué problema real resuelve Rust y cuándo NO lo usarías?
- Explica el concepto más fuerte del curso sin usar jerga.
- Contrasta Rust con una alternativa: pros/contras.
- Cuenta un error típico de novato en este tema y cómo lo evitas.

## ⭐ Método para contestarlas
1. **Responde en 60 segundos** cada una de las fundamentales, de memoria. Las que tartamudean → repásalas (flashcards/).
2. Graba tu voz en 2 y escúchate: claridad y precisión importan tanto como el contenido técnico.
3. Una respuesta buena = definición (1 línea) + ejemplo (1) + por qué importa (1).
