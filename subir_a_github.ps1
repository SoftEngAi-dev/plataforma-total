# =================================================================
#  SUBIR PLATAFORMA TOTAL A GITHUB — Windows (PowerShell)
#  Ejecútalo con doble clic en SUBIR_A_GITHUB.bat
#  Te pide: tu usuario de GitHub, el nombre del repo y tu token.
#  Crea el repo en GitHub por API y sube TODO automáticamente.
# =================================================================
$ErrorActionPreference = "Stop"
[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12
try { [Console]::OutputEncoding = [Text.Encoding]::UTF8 } catch {}
Set-Location -Path $PSScriptRoot

Write-Host ""
Write-Host "============================================" -ForegroundColor Cyan
Write-Host "   PLATAFORMA TOTAL  →  GITHUB" -ForegroundColor Cyan
Write-Host "============================================" -ForegroundColor Cyan

# ---------- Paso 1: comprobar Git ----------
Write-Host "`n[1/5] Comprobando Git..." -ForegroundColor Yellow
$git = Get-Command git -ErrorAction SilentlyContinue
if (-not $git) {
    Write-Host "`n   Git no está instalado en este equipo." -ForegroundColor Red
    Write-Host "   1. Abre  https://git-scm.com/download/win"
    Write-Host "   2. Instálalo: Siguiente → Siguiente → ... → Finalizar"
    Write-Host "   3. Vuelve a ejecutar este script."
    Read-Host "`nPulsa Enter para cerrar"
    exit 1
}
$gv = git --version
Write-Host "   OK: $gv" -ForegroundColor Green

# ---------- Paso 2: credenciales ----------
Write-Host "`n[2/5] Tus datos de GitHub" -ForegroundColor Yellow
$User = Read-Host "   Tu usuario de GitHub (como aparece en tu perfil)"
$Repo = Read-Host "   Nombre del repositorio [plataforma-total]"
if ([string]::IsNullOrWhiteSpace($Repo)) { $Repo = "plataforma-total" }
Write-Host "" 
Write-Host "   Si no tienes token, créalo así (30 segundos):" -ForegroundColor DarkGray
Write-Host "   github.com → tu avatar → Settings → Developer settings" -ForegroundColor DarkGray
Write-Host "   → Personal access tokens → Tokens (classic) → Generate new token (classic)" -ForegroundColor DarkGray
Write-Host "   → marca las casillas 'repo' y 'workflow' → Generate → copia el ghp_..." -ForegroundColor DarkGray
Write-Host ""
$Token = Read-Host "   Pega tu token (empieza por ghp_)"
if ([string]::IsNullOrWhiteSpace($User) -or [string]::IsNullOrWhiteSpace($Token)) {
    Write-Host "`n   ERROR: usuario y token son obligatorios." -ForegroundColor Red
    Read-Host "Pulsa Enter para cerrar"; exit 1
}
$User = $User.Trim(); $Repo = $Repo.Trim(); $Token = $Token.Trim()

# ---------- Paso 3: preparar repo local ----------
Write-Host "`n[3/5] Preparando el proyecto local..." -ForegroundColor Yellow
if (-not (Test-Path ".git")) {
    git init | Out-Null
    git symbolic-ref HEAD refs/heads/main
    git add -A
    git -c user.name="$User" -c user.email="$User@users.noreply.github.com" commit -m "feat: Plataforma Total v3.0" | Out-Null
    Write-Host "   Repositorio git creado con el primer commit." -ForegroundColor Green
} else {
    $ncommits = (git log --oneline | Measure-Object -Line).Lines
    $nfiles   = (git ls-files | Measure-Object -Line).Lines
    Write-Host "   Repositorio git ya existente: $nfiles archivos, $ncommits commits." -ForegroundColor Green
}

# ---------- Paso 4: crear el repo en GitHub por API ----------
Write-Host "`n[4/5] Creando el repositorio en GitHub..." -ForegroundColor Yellow
$headers = @{
    Authorization = "Bearer $Token"
    "User-Agent"  = "plataforma-total"
    Accept        = "application/vnd.github+json"
}
$body = @{
    name        = $Repo
    private     = $false
    description = "Plataforma Total — 41 cursos, 241 lecciones, 482 quizzes + app desktop (Python / customtkinter)"
} | ConvertTo-Json
try {
    Invoke-RestMethod -Uri "https://api.github.com/user/repos" -Method Post -Headers $headers -Body $body -ContentType "application/json" | Out-Null
    Write-Host "   Repositorio '$Repo' creado (público)." -ForegroundColor Green
} catch {
    $code = 0
    if ($_.Exception.Response) { $code = [int]$_.Exception.Response.StatusCode }
    if ($code -eq 422) {
        Write-Host "   El repo ya existía en tu cuenta — continuamos con el push." -ForegroundColor DarkYellow
    } elseif ($code -eq 401) {
        Write-Host "`n   ERROR 401: token inválido o sin permisos." -ForegroundColor Red
        Write-Host "   Asegúrate de usar un token (classic) con los scopes 'repo' y 'workflow'."
        Read-Host "Pulsa Enter para cerrar"; exit 1
    } else {
        Write-Host "   Aviso: la API respondió HTTP $code. Si el repo ya lo creaste a mano en github.com/new, sigo adelante..." -ForegroundColor DarkYellow
    }
}

# ---------- Paso 5: push ----------
Write-Host "`n[5/5] Subiendo los archivos a GitHub (puede tardar unos minutos)..." -ForegroundColor Yellow
git remote remove origin 2>$null | Out-Null
$pushUrl = "https://x-access-token:$Token@github.com/$User/$Repo.git"
git push $pushUrl "main:main" 2>&1 | ForEach-Object { Write-Host "   $_" -ForegroundColor DarkGray }
if ($LASTEXITCODE -ne 0) {
    Write-Host "`n   El push falló. Causas más comunes:" -ForegroundColor Red
    Write-Host "   · 401/403  → token mal pegado, expirado o sin scope 'repo'"
    Write-Host "   · 404      → usuario o nombre de repo mal escritos (respeta mayúsculas)"
    Write-Host "   · rejected → el repo remoto NO está vacío: bórralo en"
    Write-Host "                github.com/$User/$Repo/settings (Danger Zone) o usa otro nombre"
    Read-Host "`nPulsa Enter para cerrar"; exit 1
}
git remote add origin "https://github.com/$User/$Repo.git" 2>$null | Out-Null

# ---------- Éxito ----------
Write-Host ""
Write-Host "============================================" -ForegroundColor Green
Write-Host "        TODO SUBIDO A GITHUB" -ForegroundColor Green
Write-Host "============================================" -ForegroundColor Green
Write-Host ""
Write-Host "Tu repo:      https://github.com/$User/$Repo"
Write-Host "Compilación:  https://github.com/$User/$Repo/actions"
Write-Host ""
Write-Host "DESCARGAR TU EJECUTABLE DE WINDOWS (en 5-10 min):" -ForegroundColor Yellow
Write-Host "  1. El push ya lanzó la compilación automática (pestaña Actions)"
Write-Host "  2. Cuando aparezca el tick verde, haz clic en la ejecución"
Write-Host "  3. Baja hasta 'Artifacts' y haz clic en:  PlataformaTotal-Windows"
Write-Host "  4. Se descarga un .zip → extráelo → dentro está PlataformaTotal.exe"
Write-Host "  5. Doble clic al .exe. Si SmartScreen avisa:"
Write-Host "     'Más información' → 'Ejecutar de todas formas'"
Write-Host ""
Write-Host "Descarga PERMANENTE (los artefactos caducan a los 30 días):" -ForegroundColor Yellow
Write-Host "  git tag v3.0 ; git push origin v3.0"
Write-Host "  → los 3 ejecutables quedan en https://github.com/$User/$Repo/releases"
Write-Host ""
Read-Host "Pulsa Enter para cerrar"
