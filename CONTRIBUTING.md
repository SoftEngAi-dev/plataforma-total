# 🤝 Guía de contribución

¡Gracias por mejorar Plataforma Total! Es poco rígida y fácil de tocar:

## Estructura del contenido

El curriculum vive en `contenido_a.py`, `contenido_b.py`, `contenido_c.py`:

```python
CURSOS_MOD = {
    "Nombre del curso": [
        ("N. Título de la lección",
         """CONTENIDO EN MAYÚSCULAS TÍTULO
         explicado en markdown ligero con ejemplos de código""",
         [("¿Pregunta del quiz?", ["Op A", "Op B", "Op C", "Op D"], índice_correcta, "Explicación de una línea"),
          ("¿Segunda pregunta?", [...], 2, "Otra explicación")]),
        ...
    ]
}
```

- Siempre **exactamente 4 opciones** y el índice de la correcta (0-3).
- Cobertura 100%: toda lección lleva quiz. Nada de lecciones huérfanas.
- Español claro, tono mentor, ejemplos ejecutables.

## Verificación antes del PR

```bash
python3 -m py_compile main.py contenido_a.py contenido_b.py contenido_c.py
python3 -c "import contenido_a, contenido_b, contenido_c as c; print('OK')"
```

Y en 📚 Aprender de la app: revisar que la lección nueva carga y el quiz corre.

## Flujo

1. Fork → rama `feat/mi-mejora` → commit con mensaje claro
2. PR con descripción: qué cambia y por qué (1 pantalla basta)
3. ¡Listo! Revisión amable garantizada 🙂

## Estilo

- Código de app en `main.py`: una clase App, funciones db_* fuera (historia: creció orgánico, pero funciona).
- Markdown ligero en contenido, nada de HTML crudo en lecciones.
