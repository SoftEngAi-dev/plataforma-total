#!/usr/bin/env python3
"""🧪 Tests de integridad de Plataforma Total (sin dependencias GUI).

Valida que los 41 cursos tengan estructura correcta: lecciones con
título/contenido/quiz, opciones válidas y explicaciones; que el código
compile; y que el material de expansion/ esté completo.

Uso:  python tests/test_integridad.py
"""
import os
import sys
import glob
import py_compile

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(RAIZ)
sys.path.insert(0, RAIZ)


def main():
    # 1) Cargar los 3 módulos de contenido
    cursos = {}
    for nombre in ("contenido_a", "contenido_b", "contenido_c", "contenido_d", "contenido_e"):
        mod = __import__(nombre)
        cursos.update(mod.CURSOS_MOD)

    assert len(cursos) == 47, f"❌ se esperaban 47 cursos, hay {len(cursos)}"

    # 2) Validar lecciones y quizzes
    n_lecciones = n_preguntas = 0
    for curso in sorted(cursos):
        lecciones = cursos[curso]
        assert isinstance(lecciones, (list, tuple)) and lecciones, f"❌ {curso}: sin lecciones"
        for i, lec in enumerate(lecciones, 1):
            titulo, contenido, quiz = lec
            assert titulo and contenido, f"❌ {curso} L{i}: título o contenido vacío"
            assert len(contenido) > 80, f"❌ {curso} L{i}: contenido demasiado corto"
            assert isinstance(quiz, (list, tuple)) and quiz, f"❌ {curso} L{i}: sin quiz"
            for j, (pregunta, opciones, correcta, explicacion) in enumerate(quiz, 1):
                assert pregunta, f"❌ {curso} L{i} Q{j}: pregunta vacía"
                assert len(opciones) == 4, f"❌ {curso} L{i} Q{j}: {len(opciones)} opciones"
                assert isinstance(correcta, int) and 0 <= correcta < 4, \
                    f"❌ {curso} L{i} Q{j}: índice correcta={correcta}"
                assert explicacion, f"❌ {curso} L{i} Q{j}: sin explicación"
            n_preguntas += len(quiz)
        n_lecciones += len(lecciones)

    assert n_lecciones == 269, f"❌ se esperaban 269 lecciones, hay {n_lecciones}"
    assert n_preguntas == 2 * n_lecciones, "❌ cobertura de quiz ≠ 2 por lección"
    print(f"✅ 41 cursos · {n_lecciones} lecciones · {n_preguntas} preguntas — íntegro")

    # 3) Todo el código compila
    for f in ("main.py", "contenido_a.py", "contenido_b.py", "contenido_c.py", "expandir_contenido.py"):
        py_compile.compile(f, doraise=True)
    print("✅ los 5 módulos Python compilan sin errores")

    # 4) Material de expansión completo
    n_archivos = len([p for p in glob.glob("expansion/**/*.*", recursive=True) if os.path.isfile(p)])
    assert n_archivos >= 3600, f"❌ expansion/ incompleta: {n_archivos} archivos"
    print(f"✅ expansion/ completa: {n_archivos} archivos de material de estudio")

    print("\n🎓 TODOS LOS TESTS PASARON")


if __name__ == "__main__":
    main()
