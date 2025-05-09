@echo off
if "%1"=="" (
    echo Uso: %0 [rango_de_red]
    echo Ejemplo: %0 192.168.1
    exit /b
)

set "network=%~1"
if "%network:~-1%" neq "." set "network=%network%."

echo Script hecho por Esdichi
echo Suscribete al canal
echo si no eres mala gente

echo Escaneando IPs en %network%1-254...

for /l %%i in (1,1,254) do (
    ping -n 1 -w 100 %network%%%i >nul
    if not errorlevel 1 echo %network%%%i responde
)

echo Escaneo completado.
