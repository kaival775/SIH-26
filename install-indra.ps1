<#
.SYNOPSIS
Master Setup Wizard for INDRA

.DESCRIPTION
This script sets up the virtual environments, installs all dependencies, configures the environment securely (embedding keys), and runs the model downloader. It also creates a Desktop shortcut for easy access.
#>

$ErrorActionPreference = 'Stop'
$rootDir = $PSScriptRoot
$backendDir = "$rootDir\SIH-26\hermes-agent\backend"
$agentDir = "$rootDir\SIH-26\hermes-agent"
$envFile = "$rootDir\.env"

Write-Host "==========================================" -ForegroundColor Cyan
Write-Host "       INDRA 2.0 INSTALLATION WIZARD      " -ForegroundColor Cyan
Write-Host "==========================================" -ForegroundColor Cyan

# 1. Check Python
Write-Host "`n[1/6] Checking Python installation..." -ForegroundColor Yellow
if (!(Get-Command python -ErrorAction SilentlyContinue)) {
    Write-Host "Python is not installed or not in PATH! Please install Python 3.10+." -ForegroundColor Red
    exit 1
}

# 2. Setup Frontend Venv
Write-Host "`n[2/6] Setting up Frontend Virtual Environment..." -ForegroundColor Yellow
if (!(Test-Path "$rootDir\venv")) {
    python -m venv "$rootDir\venv"
}
& "$rootDir\venv\Scripts\python.exe" -m pip install --upgrade pip
& "$rootDir\venv\Scripts\python.exe" -m pip install -e "$agentDir"

# Ensure the indra.exe binary exists for branding
if (Test-Path "$rootDir\venv\Scripts\hermes.exe") {
    Copy-Item "$rootDir\venv\Scripts\hermes.exe" "$rootDir\venv\Scripts\indra.exe" -Force
}

# 3. Setup Backend Venv
Write-Host "`n[3/6] Setting up Backend Virtual Environment..." -ForegroundColor Yellow
if (!(Test-Path "$backendDir\venv")) {
    python -m venv "$backendDir\venv"
}
& "$backendDir\venv\Scripts\python.exe" -m pip install --upgrade pip
if (Test-Path "$backendDir\requirements.txt") {
    & "$backendDir\venv\Scripts\python.exe" -m pip install -r "$backendDir\requirements.txt"
}

# 4. Generate .env file dynamically
Write-Host "`n[4/6] Configuring Security & Environment..." -ForegroundColor Yellow
$vaultPath = "$rootDir\MyVault"
if (!(Test-Path $vaultPath)) {
    New-Item -ItemType Directory -Path $vaultPath | Out-Null
}

$envContent = @"
WORKBENCH_API_KEY=wb_live_1234567890abcdef1234567890abcdef
TERMINAL_ENV=local
OBSIDIAN_VAULT_PATH=$vaultPath
"@
Set-Content -Path $envFile -Value $envContent
Write-Host "Environment configured securely. Keys embedded." -ForegroundColor Green

# 5. Run Model Downloader
Write-Host "`n[5/6] Starting Model Downloader and SHA-256 Verifier..." -ForegroundColor Yellow
& "$rootDir\venv\Scripts\python.exe" "$rootDir\download_models.py"

# 6. Create Desktop Shortcut
Write-Host "`n[6/6] Creating Desktop Shortcut..." -ForegroundColor Yellow
$wshShell = New-Object -ComObject WScript.Shell
$desktopPath = [System.Environment]::GetFolderPath('Desktop')
$shortcut = $wshShell.CreateShortcut("$desktopPath\INDRA Dashboard.lnk")
$shortcut.TargetPath = "powershell.exe"
$shortcut.Arguments = "-ExecutionPolicy Bypass -NoExit -File `"$rootDir\start-indra.ps1`""
$shortcut.IconLocation = "$rootDir\venv\Scripts\python.exe,0" # Default python icon
$shortcut.WorkingDirectory = $rootDir
$shortcut.Save()

Write-Host "`n==========================================" -ForegroundColor Green
Write-Host " INSTALLATION COMPLETE! " -ForegroundColor Green
Write-Host "==========================================" -ForegroundColor Green
Write-Host "You can now start INDRA by double-clicking the 'INDRA Dashboard' shortcut on your Desktop." -ForegroundColor Cyan
