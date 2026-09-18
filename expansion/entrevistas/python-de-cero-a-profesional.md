# 🎤 Banco de entrevista — Python — De Cero a Profesional

> 32 preguntas esenciales + guía de respuestas las que ya sabes del curso

## 🔥 Fundamentales (del contenido del curso)

1. **¿Qué delimita los bloques de código en Python?**
   - La indentación (sangría) de 4 espacios  _(La sangría forzada hace el código universalmente legible — la idea nuclear de Python.)_

2. **input() devuelve siempre...**
   - str (hay que convertir con int()/float() para calcular)  _(Fuente clásica de bugs principiantes: '5' + '5' = '55'. Convierte.)_

3. **¿Qué imprime 7 % 2?**
   - 1  _(% es residuo: 7 = 2×3 + 1.)_

4. **¿Qué permite la f-string?**
   - Interpolar variables y expresiones con formato: f'{precio:.2f}'  _(Las f-strings combinadas con especificadores de formato son el estándar moderno.)_

5. **¿Qué hace numeros[1:3]?**
   - Devuelve los elementos en posiciones 1 y 2 (fin excluido)  _(Slices: [inicio:fin) — la mitad de los bugs de principiante vienen del fin excluido.)_

6. **a, b = b, a hace...**
   - Intercambiar los valores sin variable temporal (desempaquetado)  _(La derecha se evalúa como tupla completa antes de asignar: el swap pythónico.)_

7. **¿Por qué alumno.get('email') en vez de alumno['email']?**
   - Evita KeyError: devuelve None (o el default) si falta la clave  _(get = acceso defensivo sin try/except; úsalo cuando la clave puede faltar.)_

8. **¿Para qué usar set([1,1,2,3])?**
   - Eliminar duplicados: {1, 2, 3} (los sets no repiten)  _(Deduplicación instantánea + operaciones matemáticas de conjuntos.)_

9. **'a-b-c'.split('-') devuelve...**
   - ['a', 'b', 'c']  _(split corta en lista; el inverso es '-'.join(lista).)_

10. **¿Por qué debes reasignar texto = texto.strip()?**
   - Los strings son inmutables: strip devuelve uno nuevo  _(Métodos de str NUNCA modifican el original.)_

11. **if usuario is None — ¿por qué 'is' y no '=='?**
   - None es singleton: se compara identidad; además is evita métodos __eq__ raros  _(None/True/False → is. Valores → ==)_

12. **¿Qué pasa con if [0]?**
   - Es truthy (lista NO vacía aunque contenga 0)  _(La verdad está en la ESTRUCTURA (vacía vs no), no en el contenido.)_

13. **¿Qué aporta enumerate frente a range(len(lista))?**
   - Índice y elemento a la vez, legible y sin errores de off-by-one  _(enumerate es el idioma correcto; range(len()) es el acento extranjero.)_

14. **range(2, 10, 2) genera...**
   - 2, 4, 6, 8  _(range(inicio, fin, paso) — fin SIEMPRE excluido.)_

15. **def f(a, b=2): — ¿por qué el default va al final?**
   - Los posicionales deben venir primero para no ambiguar la llamada  _(f(5) debe ser claro: a=5. Con default primero sería ambiguo.)_

16. **Sin return, una función Python devuelve...**
   - None (¡cuidado al encadenar!)  _(Caso clásico: olvidas return y luego el resultado es None donde no esperas.)_

17. **¿Por qué usar with open(...)?**
   - Cierra el archivo automáticamente incluso ante errores  _(with = context manager: el recurso se libera pase lo que pase.)_

18. **¿Cómo guardar y recuperar un dict en JSON?**
   - json.dump() y json.load()  _(json es universal multiplataforma; dicts/listas pasan directo.)_

19. **¿Qué bloque corre SIEMPRE, haya o no excepción?**
   - finally  _(finally = limpieza garantizada (cerrar archivos, conexiones).)_

20. **raise ValueError('x') sirve para...**
   - Lanzar tu propio error con mensaje claro cuando detectas un estado inválido  _(Valida pronto, falla fuerte y con mensaje: debugging agradecido.)_

21. **all() y any() con generador hacen...**
   - Lógica declarativa: ¿todos/alguno cumplen? — sin bucles explícitos  _(all(x > 0 for x in nums) se lee como español: todos mayores a cero.)_

22. **¿Cuándo usar lambda?**
   - Funciones de una expresión triviales pasadas a key= y similares; en todo otro caso, def  _(Si necesita nombre para entenderse, ese nombre es su def.)_

23. **¿Qué hace self en un método?**
   - Referencia a la instancia actual: sus atributos y métodos  _(self es cómo el método sabe sobre QUÉ objeto concreto opera.)_

24. **¿Qué gana @dataclass?**
   - init, repr y eq automáticos para clases de datos  _(Modelos limpios sin boilerplate: escribes los campos y todo lo demás llega gratis.)_

25. **¿Qué protege if __name__ == '__main__'?**
   - El código solo corre al EJECUTAR el archivo, no al importarlo  _(Permite archivos que son a la vez librería (importar) y script (correr).)_

26. **¿Por qué python3 -m src.main y no python3 src/main.py?**
   - Con -m, los imports relativos del paquete funcionan; con ruta directa suelen romperse  _(-m ejecuta como módulo del paquete: los from tareas import resuelven bonito.)_

27. **¿Qué aporta Path de pathlib frente a strings de rutas?**
   - Rutas portables Windows/Linux con operadores / y métodos read_text/exists  _(p = Path.home() / 'x' funciona igual en todos los SO — el estándar moderno de Python.)_

28. **Counter('banana') devuelve...**
   - {'a': 3, 'n': 2, 'b': 1} — conteo automático  _(collections.Counter = histograma listo con una línea.)_

29. **¿Qué hace csv.DictReader?**
   - Convierte cada fila del CSV en un dict usando el encabezado como claves  _(fila['precio'] directo — parseo CSV robusto con nada instalado.)_

30. **df.groupby('producto')['total'].sum() hace...**
   - Agrupa por producto y suma el total de cada grupo  _(El GROUP BY de SQL, estilo pandas: resumir categorías en 1 línea.)_

31. **¿Por qué separar modelos.py de main.py?**
   - Separación de responsabilidades: clases/datos testeables solos, main solo orquesta  _(Cada módulo una razón de cambio; esto es arquitectura en pequeño.)_

32. **Un proyecto 'terminado' incluye además del código...**
   - README + requirements + tests básicos + .gitignore  _(Profesional = reproducible y presentable, no solo que corra en tu máquina.)_

## 🧗 Profundización (prepáralas explicando en voz alta)
- ¿Qué problema real resuelve Python y cuándo NO lo usarías?
- Explica el concepto más fuerte del curso sin usar jerga.
- Contrasta Python con una alternativa: pros/contras.
- Cuenta un error típico de novato en este tema y cómo lo evitas.

## ⭐ Método para contestarlas
1. **Responde en 60 segundos** cada una de las fundamentales, de memoria. Las que tartamudean → repásalas (flashcards/).
2. Graba tu voz en 2 y escúchate: claridad y precisión importan tanto como el contenido técnico.
3. Una respuesta buena = definición (1 línea) + ejemplo (1) + por qué importa (1).
