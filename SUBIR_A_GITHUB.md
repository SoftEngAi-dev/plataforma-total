# 🚀 Subir Plataforma Total a GitHub — Guía paso a paso (Windows)

> **Objetivo:** subir los 3.600+ archivos del proyecto a TU GitHub y descargar tu **PlataformaTotal.exe** compilado en la nube. Tiempo total: **~10 minutos**.

---

## 📦 Antes de empezar

1. Descarga **`plataforma-total-completo.zip`** (está en el workspace).
2. Extrae el ZIP en una carpeta nueva llamada `plataforma-total`:
   - Clic derecho sobre el ZIP → **Extraer todo...** → elige tu carpeta.
3. Instala **Git para Windows** (si no lo tienes):
   - https://git-scm.com/download/win → Descargar → Siguiente → Siguiente → Finalizar.

---

## 🔑 Paso 1 · Crea tu token (30 segundos)

1. Entra en **github.com** con tu cuenta.
2. Clic en tu avatar (arriba a la derecha) → **Settings**.
3. Abajo a la izquierda: **Developer settings**.
4. **Personal access tokens → Tokens (classic) → Generate new token (classic)**.
5. En "Note" escribe: `plataforma` · Expiration: la que quieras.
6. **Marca estas dos casillas:** ✅ `repo` y ✅ `workflow`.
7. **Generate token** → **copia el código** que empieza por `ghp_`.
   ⚠️ Solo se muestra una vez. Pégalo en un bloc de notas de momento.

---

## 🖱️ Paso 2 · Doble clic y listo

1. En la carpeta donde extrajiste el proyecto, haz **doble clic en `SUBIR_A_GITHUB.bat`**.
2. El script te pedirá 3 cosas, una por una:
   - **Tu usuario de GitHub** (el nombre de tu perfil, ej: `juanperez`).
   - **Nombre del repositorio** — pulsa Enter para usar `plataforma-total`.
   - **Tu token** — pega el `ghp_...` que copiaste.
3. El script hace TODO solo:
   - ✅ Verifica Git
   - ✅ Prepara el repositorio local (con historial incluido)
   - ✅ **Crea el repo en tu GitHub por API** (no tienes que crearlo a mano)
   - ✅ Sube los 3.600+ archivos
4. Cuando veas **"TODO SUBIDO A GITHUB"** ya está. 🎉

> Si algo falla, el propio script te dice la causa (token mal, repo existente con archivos, etc.). Lee la sección **Problemas frecuentes** abajo.

---

## 🖥️ Paso 3 · Descarga tu PlataformaTotal.exe

El push **lanzó automáticamente la compilación de Windows, macOS y Linux** en la nube de GitHub. Para descargar tu ejecutable:

1. Abre **https://github.com/TU-USUARIO/plataforma-total/actions**
2. Verás la ejecución "🖥️ Compilar ejecutables desktop". Espera al ✅ verde (5–10 min).
3. Haz clic en esa ejecución → baja hasta la sección **Artifacts**.
4. Haz clic en **`PlataformaTotal-Windows`** → se descarga un ZIP.
5. Extrae el ZIP → dentro está **`PlataformaTotal.exe`** (con todos sus archivos).
6. **Doble clic a `PlataformaTotal.exe`** → se abre la app. 🎓

> 🛡️ **Si Windows SmartScreen avisa** ("Windows protegió su PC"): es normal, el .exe no está firmado digitalmente. Clic en **"Más información" → "Ejecutar de todas formas"**. Es TU app compilada en TU GitHub.

---

## 📦 Extra · Descarga permanente con Releases (recomendado)

Los artefactos de Actions **caducan a los 30 días**. Para tener los ejecutables siempre disponibles en `github.com/TU-USUARIO/plataforma-total/releases`:

```bash
# En la carpeta del proyecto (Git Bash, PowerShell o Terminal):
git tag v3.0
git push origin v3.0
```

El workflow crea automáticamente la **Release v3.0** con los 3 ejecutables adjuntos (Windows .zip, macOS y Linux .tar.gz) que **nunca caducan**.

---

## ❓ Problemas frecuentes

| Problema | Solución |
|---|---|
| `'git' no se reconoce` | Instalaste Git después de abrir la ventana → ciérrala y vuelve a ejecutar el `.bat`. |
| **401 / 403** en el push | Token mal pegado, expirado o sin el scope `repo`. Genera uno nuevo (Paso 1). |
| El repo "ya tiene archivos" / push rechazado | Borra el repo remoto en `github.com/TU-USUARIO/REPO/settings` (Danger Zone → Delete) y vuelve a ejecutar el script, o elige otro nombre de repo. |
| PowerShell muestra caracteres raros | No afecta al funcionamiento; es solo el renderizado de emojis en la consola. |
| El `.bat` no hace nada al doble clic | Clic derecho → **Ejecutar con PowerShell** en `subir_a_github.ps1`, o abre PowerShell en la carpeta y ejecuta: `powershell -ExecutionPolicy Bypass -File .\subir_a_github.ps1` |
| No aparecen los Artifacts | La compilación aún corre (círculo amarillo). Refresca en unos minutos. |
| SmartScreen bloquea el .exe | "Más información" → "Ejecutar de todas formas". |

---

## 🔁 ¿Y si prefiero NO instalar nada? (Plan B, 100% navegador)

1. Crea el repo vacío en **https://github.com/new** (nombre `plataforma-total`, sin README).
2. Extrae el ZIP del proyecto en tu PC.
3. En la página de tu repo nuevo → **"uploading an existing file"**.
4. **Arrastra todas las carpetas y archivos** del proyecto (todo excepto la carpeta oculta `.git`).
5. **Commit changes** → la compilación de Actions arranca sola → Paso 3 de arriba.

*(Este camino sube sin el historial de commits, pero el código y la compilación funcionan igual.)*

---

**¿Mac o Linux?** Usa `./subir_a_github.sh` — hace exactamente lo mismo.
