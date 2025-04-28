@echo off
setlocal enabledelayedexpansion
set FILE=%1
set EXT=%~x1
if /i not "!EXT!"==".fish" (
    echo Please provide a .fish file to run.
    exit /b 1
)
pythonw -u "%~dp0fishscript_transpiler.py" "%FILE%" >nul 2>&1
if %errorlevel% neq 0 exit /b %errorlevel%
set PYFILE=!FILE:.fish=.py!
pythonw -u "!PYFILE!"
del /f /q "!PYFILE!" >nul 2>&1
