@echo off
title Fox Fuel K-Factor Optimizer
echo.
echo FoxFuel K-Factor Optimizer
echo ==========================
echo.
echo Starting K-Factor optimization...
echo.

cd /d "%~dp0"
python run_local.py

echo.
echo Process completed. Check the output files in data/outputs/
pause
