@echo off
setlocal enabledelayedexpansion
set FISH_HOME=%~dp0

set KEY="HKCU\Environment"
for /f "skip=2 tokens=2,*" %%A in ('reg query %KEY% /v PATH 2^>nul') do set OLD_PATH=%%B

echo %OLD_PATH% | find "%FISH_HOME%" >nul
if not errorlevel 1 goto :ALREADYINPATH

setx PATH "%OLD_PATH%;%FISH_HOME%"
echo FishScript installed! You may need to restart your terminal.
goto :END

:ALREADYINPATH
echo FishScript is already in your PATH!
:END
