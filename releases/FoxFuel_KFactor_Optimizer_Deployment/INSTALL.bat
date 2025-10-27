@echo off
title FoxFuel K-Factor Optimizer - Installation Script
echo.
echo ========================================
echo   FoxFuel K-Factor Optimizer
echo   Installation Script
echo ========================================
echo.
echo This script will set up the K-Factor Optimizer on this computer.
echo.
echo Requirements:
echo - Windows 10 or later
echo - No Python installation needed
echo - Administrator privileges (for folder creation)
echo.
pause

echo.
echo Creating folder structure...
echo.

REM Create main application directory
if not exist "FoxFuel_KFactor_Optimizer" mkdir "FoxFuel_KFactor_Optimizer"
cd "FoxFuel_KFactor_Optimizer"

REM Create data directories
if not exist "data" mkdir "data"
if not exist "data\inputs" mkdir "data\inputs"
if not exist "data\outputs" mkdir "data\outputs"

echo ✓ Folder structure created successfully!
echo.
echo Created directories:
echo   FoxFuel_KFactor_Optimizer\
echo   ├── data\
echo   │   ├── inputs\     (place CSV files here)
echo   │   └── outputs\    (results will appear here)
echo.

REM Copy the executable if it exists in the same directory
if exist "..\FoxFuel_KFactor_Optimizer.exe" (
    copy "..\FoxFuel_KFactor_Optimizer.exe" "FoxFuel_KFactor_Optimizer.exe"
    echo ✓ Executable copied successfully!
) else (
    echo ⚠ Warning: FoxFuel_KFactor_Optimizer.exe not found in parent directory
    echo   Please ensure the .exe file is in the same folder as this installer
)

REM Create desktop shortcut
echo.
echo Creating desktop shortcut...
set "desktop=%USERPROFILE%\Desktop"
set "currentDir=%CD%"

echo [InternetShortcut] > "%desktop%\FoxFuel K-Factor Optimizer.url"
echo URL=file:///%currentDir%/FoxFuel_KFactor_Optimizer.exe >> "%desktop%\FoxFuel K-Factor Optimizer.url"
echo IconFile=%currentDir%/FoxFuel_KFactor_Optimizer.exe >> "%desktop%\FoxFuel K-Factor Optimizer.url"
echo IconIndex=0 >> "%desktop%\FoxFuel K-Factor Optimizer.url"

echo ✓ Desktop shortcut created!

REM Create start menu shortcut
echo.
echo Creating start menu shortcut...
set "startMenu=%APPDATA%\Microsoft\Windows\Start Menu\Programs"

echo [InternetShortcut] > "%startMenu%\FoxFuel K-Factor Optimizer.url"
echo URL=file:///%currentDir%/FoxFuel_KFactor_Optimizer.exe >> "%startMenu%\FoxFuel K-Factor Optimizer.url"
echo IconFile=%currentDir%/FoxFuel_KFactor_Optimizer.exe >> "%startMenu%\FoxFuel K-Factor Optimizer.url"
echo IconIndex=0 >> "%startMenu%\FoxFuel K-Factor Optimizer.url"

echo ✓ Start menu shortcut created!

echo.
echo ========================================
echo   INSTALLATION COMPLETE!
echo ========================================
echo.
echo The FoxFuel K-Factor Optimizer has been installed successfully!
echo.
echo Next steps:
echo 1. Place your CSV files in: %currentDir%\data\inputs\
echo    - 03_CustomerFuel.csv
echo    - 04_DeliveryTickets.csv
echo    - 06_DegreeDayValues.csv
echo.
echo 2. Run the application by:
echo    - Double-clicking the desktop shortcut, OR
echo    - Double-clicking FoxFuel_KFactor_Optimizer.exe
echo.
echo 3. In the application:
echo    - Click "Auto-Detect Files"
echo    - Click "Run K-Factor Optimizer"
echo    - Review results in the GUI
echo.
echo Installation location: %currentDir%
echo.
echo For support, refer to the user guide included with the application.
echo.
pause
