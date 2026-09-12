@echo off
rem Hermes Agent Gateway - Messaging Platform Integration
cd /d C:\Users\khatr\OneDrive\Desktop\indra\SIH-26
set "HERMES_HOME=C:\Users\khatr\OneDrive\Desktop\indra\SIH-26"
set "PYTHONIOENCODING=utf-8"
set "HERMES_GATEWAY_DETACHED=1"
set "HERMES_SUPERVISED_CHILD=1"
set "VIRTUAL_ENV=C:\Users\khatr\OneDrive\Desktop\indra\venv"
set "PYTHONPATH=C:\Users\khatr\OneDrive\Desktop\indra\SIH-26\hermes-agent;%PYTHONPATH%"
C:\Users\khatr\OneDrive\Desktop\indra\venv\Scripts\python.exe -m hermes_cli.main gateway run
exit /b 0
