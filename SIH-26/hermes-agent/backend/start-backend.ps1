$ErrorActionPreference = 'Stop'
$backendRoot = $PSScriptRoot
function Test-BackendPort([int]$port) {
    $client = [System.Net.Sockets.TcpClient]::new()
    try { $client.Connect('127.0.0.1', $port); return $true }
    catch { return $false }
    finally { $client.Dispose() }
}
function Start-BackendPart($name, $port, $executable, $arguments) {
    if (Test-BackendPort $port) { return }
    # Start-Process fails when a parent process carries both PATH and Path.
    # Build a case-insensitive, de-duplicated environment for Windows instead.
    $info = [System.Diagnostics.ProcessStartInfo]::new()
    $info.FileName = $executable
    $info.Arguments = $arguments
    $info.WorkingDirectory = $backendRoot
    $info.UseShellExecute = $false
    $info.CreateNoWindow = $true
    $info.RedirectStandardOutput = $true
    $info.RedirectStandardError = $true
    $seen = [System.Collections.Generic.HashSet[string]]::new([System.StringComparer]::OrdinalIgnoreCase)
    foreach ($entry in [System.Environment]::GetEnvironmentVariables().GetEnumerator()) {
        if ($seen.Add([string]$entry.Key)) { $info.Environment[[string]$entry.Key] = [string]$entry.Value }
    }
    $process = [System.Diagnostics.Process]::new()
    $process.StartInfo = $info
    $process.Start()
    $stdoutPath = "$backendRoot\data\$name-start.log"
    $stderrPath = "$backendRoot\data\$name-start-error.log"
    $process.BeginOutputReadLine()
    $process.BeginErrorReadLine()
    Register-ObjectEvent -InputObject $process -EventName OutputDataReceived -Action { if ($EventArgs.Data) { Add-Content -LiteralPath $using:stdoutPath -Value $EventArgs.Data } } | Out-Null
    Register-ObjectEvent -InputObject $process -EventName ErrorDataReceived -Action { if ($EventArgs.Data) { Add-Content -LiteralPath $using:stderrPath -Value $EventArgs.Data } } | Out-Null
    $deadline = (Get-Date).AddSeconds(45)
    while (-not (Test-BackendPort $port)) {
        if ((Get-Date) -gt $deadline) { throw "$name did not start; check backend/data/$name-start-error.log" }
        Start-Sleep -Milliseconds 400
    }
}
# Qdrant is intentionally omitted for the offline skills-based demo.
Start-BackendPart 'llamaswap' 8100 "$backendRoot\bin\llama-swap.exe" '--config config/llama-swap.yaml --listen 127.0.0.1:8100 --watch-config'
Start-BackendPart 'workbench' 8000 "$backendRoot\venv\Scripts\python.exe" '-m uvicorn server.app:app --host 0.0.0.0 --port 8000'
