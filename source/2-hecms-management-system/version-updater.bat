@echo off
set /p version="Enter the new version number: "
powershell -ExecutionPolicy Bypass -File version-updater/version-update-script.ps1 %version%