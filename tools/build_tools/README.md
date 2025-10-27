# Build Tools

This folder contains scripts for building standalone executables and deployment packages.

## Files:

### `build_exe.py`
- **Purpose:** Builds standalone executable for the main K-Factor optimizer
- **Usage:** `python build_exe.py`
- **Output:** `FoxFuel_KFactor.exe` in `dist/` folder
- **Features:** Console-based executable

### `build_gui_exe.py`
- **Purpose:** Builds standalone executable for the GUI version
- **Usage:** `python build_gui_exe.py`
- **Output:** `FoxFuel_KFactor_Optimizer.exe` in `dist/` folder
- **Features:** GUI-based executable (320 MB)

### `build_analysis_exe.py`
- **Purpose:** Builds standalone executable for the analysis tool
- **Usage:** `python build_analysis_exe.py`
- **Output:** `Customer_Analysis_Tool.exe` in `dist/` folder
- **Features:** GUI analysis tool executable

### `create_deployment_package.py`
- **Purpose:** Creates complete deployment package for staff installation
- **Usage:** `python create_deployment_package.py`
- **Output:** `FoxFuel_KFactor_Optimizer_Deployment_YYYYMMDD_HHMMSS.zip`
- **Contents:**
  - Main GUI executable
  - Installation scripts
  - Documentation
  - Folder structure templates

## Build Process:

1. **Install PyInstaller:** `pip install pyinstaller`
2. **Run build script:** `python build_*.py`
3. **Find executable:** Check `dist/` folder
4. **Test executable:** Run on target system

## Executable Features:

- **No Python Required:** Works on any Windows computer
- **All Dependencies Included:** Complete package
- **One-Click Operation:** Double-click to run
- **Portable:** Can be copied to any location

## File Sizes:

- **Main GUI:** ~320 MB (includes pandas, numpy, openpyxl, tkinter)
- **Analysis Tool:** ~300 MB (similar dependencies)
- **Console Version:** ~280 MB (no GUI dependencies)

## Distribution:

- **Single File:** Just copy the .exe file
- **Deployment Package:** Complete installation package with documentation
- **Network Share:** Can run from shared drives
