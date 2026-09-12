$ErrorActionPreference = 'Stop'
$env:TERMINAL_ENV = 'local'
& "$PSScriptRoot\venv\scripts\indra.exe" dashboard
