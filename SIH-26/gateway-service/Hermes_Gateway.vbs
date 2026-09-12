' Hermes Agent Gateway - Messaging Platform Integration
Option Explicit
Dim sh, env, existing_pp
Set sh = CreateObject("WScript.Shell")
Set env = sh.Environment("PROCESS")
env.Item("HERMES_HOME") = "C:\Users\khatr\OneDrive\Desktop\indra\SIH-26"
env.Item("PYTHONIOENCODING") = "utf-8"
env.Item("HERMES_GATEWAY_DETACHED") = "1"
env.Item("HERMES_SUPERVISED_CHILD") = "1"
env.Item("VIRTUAL_ENV") = "C:\Users\khatr\OneDrive\Desktop\indra\venv"
existing_pp = env.Item("PYTHONPATH")
If Len(existing_pp) > 0 Then
  env.Item("PYTHONPATH") = "C:\Users\khatr\OneDrive\Desktop\indra\SIH-26\hermes-agent;" & existing_pp
Else
  env.Item("PYTHONPATH") = "C:\Users\khatr\OneDrive\Desktop\indra\SIH-26\hermes-agent"
End If
sh.CurrentDirectory = "C:\Users\khatr\OneDrive\Desktop\indra\SIH-26"
sh.Run "C:\Users\khatr\OneDrive\Desktop\indra\venv\Scripts\python.exe -m hermes_cli.main gateway run", 0, False
