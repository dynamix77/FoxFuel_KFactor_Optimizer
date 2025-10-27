@echo off
title FoxFuel K-Factor Analysis Tool
echo.
echo FoxFuel K-Factor Analysis Tool
echo ========================================
echo.

REM Check if Python is available
where python >nul 2>nul
if %ERRORLEVEL% NEQ 0 (
    echo Python is not installed or not in PATH
    echo Please install Python or use the standalone executable
    pause
    exit /b 1
)

echo Starting Customer Analysis GUI...
echo.

python customer_analysis_gui.py

pause
