@echo off
title FoxFuel K-Factor Optimizer - GUI Launcher
echo.
echo ========================================
echo   FoxFuel K-Factor Optimizer - GUI
echo ========================================
echo.
echo Starting the GUI application...
echo.

REM Check if the executable exists
if not exist "FoxFuel_KFactor_Optimizer.exe" (
    echo ERROR: FoxFuel_KFactor_Optimizer.exe not found!
    echo Please ensure the executable is in the same folder as this batch file.
    echo.
    pause
    exit /b 1
)

REM Run the GUI executable
start "" "FoxFuel_KFactor_Optimizer.exe"

echo GUI application started successfully!
echo.
echo The application window should open shortly.
echo If it doesn't appear, check your taskbar.
echo.
pause
