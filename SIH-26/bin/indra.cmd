@echo off
setlocal
set "ROOT=%~dp0.."
set "HERMES_HOME=%ROOT%"
set "DOCKER_CONFIG=%ROOT%\docker-config"
if exist "%ROOT%\..\venv\Scripts\activate.bat" (
    call "%ROOT%\..\venv\Scripts\activate.bat"
)
python -m hermes_cli.main %*
endlocal
