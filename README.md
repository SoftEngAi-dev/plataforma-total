<p align="center">
  <img src="assets/icono-256.png" width="140" alt="Plataforma Total 🎓">
</p>

# 🎓 Plataforma Total — Tu Escuela Local de Programación

[![🏷️ v3.1.0](https://img.shields.io/github/v/release/SoftEngAi-dev/plataforma-total?display_name=tag&label=versi%C3%B3n&color=7c3aed)](https://github.com/SoftEngAi-dev/plataforma-total/releases)
[![🖥️ Build](https://github.com/SoftEngAi-dev/plataforma-total/actions/workflows/build.yml/badge.svg)](https://github.com/SoftEngAi-dev/plataforma-total/actions)
[![📜 Licencia MIT](https://img.shields.io/badge/licencia-MIT-22c55e)](LICENSE)
[![🌐 Web](https://img.shields.io/badge/web-del%20proyecto-f59e0b)](https://softengai-dev.github.io/plataforma-total/)

**Escuela completa de software que vive 100% en tu máquina. Sin internet, sin cuentas, sin suscripciones — justo tú, 47 cursos y (opcional) tu IA local.**

```
47 cursos · 269 lecciones · 538 quizzes (100% cobertura) · 3.941 archivos de material
Buscador 🔍 · Quizzes 📝 · Pomodoro 🍅 · Racha 🔥 · Certificados 🎓 · Chat IA con memoria 🤖
Linux · Windows · macOS · 100% offline · Ejecutables con icono oficial 🖼️
```

---

## ⬇️ Descarga directa (sin compilar nada)

| SO | Archivo | Instrucciones |
|----|---------|---------------|
| 🪟 **Windows** | [PlataformaTotal-Windows.zip](https://github.com/SoftEngAi-dev/plataforma-total/releases/latest/download/PlataformaTotal-Windows.zip) | Descomprimir → doble clic en `PlataformaTotal.exe` *(SmartScreen: "Más información" → "Ejecutar de todas formas")* |
| 🐧 **Linux** | [PlataformaTotal-Linux.tar.gz](https://github.com/SoftEngAi-dev/plataforma-total/releases/latest/download/PlataformaTotal-Linux.tar.gz) | `tar -xzf` → ejecutar `PlataformaTotal/PlataformaTotal` |
| 🍎 **macOS** | [PlataformaTotal-macOS.tar.gz](https://github.com/SoftEngAi-dev/plataforma-total/releases/latest/download/PlataformaTotal-macOS.tar.gz) | `tar -xzf` → abrir la app |

> 🏷️ Enlaces permanentes siempre a la **última versión**. Historial completo: [Releases](https://github.com/SoftEngAi-dev/plataforma-total/releases) · Cambios: [CHANGELOG](CHANGELOG.md)

---

## 🚀 Arranque en 60 segundos (desde código)

| SO | Opción A: código | Opción B: ejecutable |
|----|------------------|----------------------|
| **Linux** | `./run.sh` | `./PlataformaTotal` (descomprimido de `.tar.gz`) |
| **Windows** | `run.bat` | `PlataformaTotal.exe` (vía Actions ⌨ abajo) |
| **macOS** | `./run.command` | `PlataformaTotal.app` (vía Actions ⌨ abajo) |

**Código fuente** (necesitas Python 3.10+): los scripts instalan todo solos la primera vez.

```bash
git clone https://github.com/SoftEngAi-dev/plataforma-total.git && cd plataforma-total
./run.sh        # Linux (o run.bat / run.command)
```

## ⬇️ Ejecutable ya compilado (Linux)

En `ejecutable/PlataformaTotal-Linux-x86_64.tar.gz`:

```bash
tar -xzf ejecutable/PlataformaTotal-Linux-x86_64.tar.gz
./PlataformaTotal/PlataformaTotal     # doble clic también funciona
```

Funciona en Linux x86_64 reciente **sin instalar Python ni dependencias** (GLibc; simplemente corre).

## ☁️ Ejecutables de Windows y macOS (gratis, automáticos)

El workflow `.github/workflows/build.yml` compila los **3 ejecutables en la nube de GitHub** en cada push a `main`:

1. Sube/uplift este proyecto a tu GitHub
2. Pestaña **Actions** → "🖥️ Compilar ejecutables desktop" → descarga los artefactos
3. Tienes: **Windows.zip (con .exe)**, **macOS.tar.gz (con .app)** y **Linux.tar.gz**

## 📤 Subir a GitHub (guía completa: [`SUBIR_A_GITHUB.md`](SUBIR_A_GITHUB.md))

**🪟 Windows (recomendado):** descarga `plataforma-total-completo.zip`, extráelo y haz **doble clic en `SUBIR_A_GITHUB.bat`** — te pide usuario, repo y token, **crea el repo en tu GitHub por API** y sube los 3.600+ archivos solo.

**🍎 macOS / 🐧 Linux:** `./subir_a_github.sh` (interactivo) o manual:

```bash
# github.com/new → crea el repo VACÍO, luego:
git remote add origin https://github.com/TU-USUARIO/plataforma-total.git
git push -u origin main        # contraseña = tu Personal Access Token
```

> 🔐 Token: github.com → **Settings → Developer settings → Tokens (classic)** → scopes `repo` + `workflow`.

**🖥️ Descargar tu `.exe` tras el push:** pestaña **Actions** → run ✅ → **Artifacts** → `PlataformaTotal-Windows` (ZIP con `PlataformaTotal.exe` dentro). Para descargas **permanentes**: `git tag v3.0 && git push origin v3.0` → los 3 ejecutables quedan en **Releases** sin caducidad.

## 🖥️ Icono de escritorio (Linux)

Tras descomprimir el ejecutable:

```bash
tar -xzf ejecutable/PlataformaTotal-Linux-x86_64.tar.gz -C /opt  # o cualquier carpeta
sed -i "s|/opt/PlataformaTotal|$(pwd)/PlataformaTotal|" PlataformaTotal.desktop
cp PlataformaTotal.desktop ~/.local/share/applications/
```

La app aparece en tu menú de aplicaciones como 🎓 **Plataforma Total**.

---

## 📚 El curriculum (47 cursos)

**Ruta y herramientas:** Ruta Maestra · Herramientas del Dev · Git/GitHub · Linux/Terminal · Docker · DevOps/CI-CD · Despliegue/Servidores
**Web core:** HTML/CSS · JavaScript (18 lecciones) · TypeScript · React · Node.js
**Backend:** Python (16) · SQL/PostgreSQL · PHP/Laravel · Ruby/Rails · Java/Spring · C#/.NET · Go · Rust · C/C++
**Móvil:** Kotlin · Swift · Flutter · React Native
**Frameworks:** Angular · Svelte/SvelteKit
**Datos/IA:** R · Pandas · Machine Learning · IA y LLMs (Ollama incluido)
**Profesional:** Seguridad Web · Testing · Algoritmos · Arquitectura · APIs REST · Productividad Dev · Entrevistas · Regex · Carrera/Portafolio

## 🧠 Cómo se estudia aquí (método comprobado)

1. 🍅 panel lateral → pulsa ▶ (pomodoro 25 min)
2. 📚 Aprender → elige curso/lección, lee el protocolo 25 minutos
3. 🛠 Reproduce el ejemplo con tus propias manos
4. ✅ marca completada → 📝 juega el quiz → **meta: 🏆 100%**
5. 🔥 repite mañana — la racha es la palanca de todo

Domina un curso entero (lecciones + quizzes al 100%) y la app te **emisía tu certificado 🎓 imprimible** con código de verificación SHA-256.

## 🗂 ¿Qué hay en este repo?

| Ruta | Qué es |
|------|--------|
| `main.py` | La aplicación completa (customtkinter, SQLite, Ollama) |
| `contenido_a/b/c.py` | El contenido curricular: 47 cursos × lecciones × quizzes |
| `expandir_contenido.py` | Generador del ecosistema de estudio (`expansion/`) |
| `expansion/` | **3.478 archivos de material**: lecciones MD, quizzes HTML offline, 482 flashcards, ejercicios, glosarios, prompts IA, 246 guías de proyecto, plan anual de estudio... |
| `expansion/plan_diario/` | Plan día a día para un año de estudio (364 días) |
| `expansion/quizzes_html/` | Quizzes interactivos offline por lección (se abren en el navegador) |
| `ejecutable/` | Binario Linux empaquetado y verificado |
| `.github/workflows/build.yml` | CI que compila los ejecutables Win/Mac/Linux en cada push |
| `run.*` / `build_*` | Scripts de ejecución y compilación local por SO |
| `expansion/entrevistas/` | Banco de preguntas de entrevista por tecnología |
| `expansion/resumen_curso/` | Cheatsheet consolidado por curso |

## 🩺 Datos y privacidad

Todo lo que haces vive en **SQLite local**: `~/PlataformaTotal/datos/plataforma.db` — lecciones, racha, quizzes, pomodoros, historial de chat, certificados. Es tuyo: respáldalo, inspecciónalo, bórralo.

**IA**: el chat usa tu propio **[Ollama](https://ollama.com)** local (gratis, privado). Sin Ollama activo, un cerebro offline responde las FAQs. Nada sale de tu máquina en ningún caso.

## 🤝 Contribuir

¿Bug, mejora de lección, quiz nuevo? Revisa `CONTRIBUTING.md` y abre un PR. El contenido curricular vive en `contenido_*.py` con un formato fácil de leer.

## 📜 Licencia

MIT — úsala, cámbiala, enséñala. Ver `LICENSE`.

---

> 💡 **Empieza hoy la lección 1 de la Ruta Maestra.** Un 🍅 = una lección. En 8 meses, una transformación. ¡Vamos!