# Deployment Tools

This folder contains tools for deploying the K-Factor Optimizer to staff computers.

## Files:

### `INSTALL.bat`
- **Purpose:** Automated installation script for staff computers
- **Usage:** Right-click → "Run as administrator"
- **Features:**
  - Creates installation directory
  - Copies all necessary files
  - Creates desktop shortcut
  - Sets up folder structure

### `RUN_GUI.bat`
- **Purpose:** Simple launcher for the GUI application
- **Usage:** Double-click to run
- **Features:**
  - No command line knowledge required
  - Works after installation

### `INSTALLATION_GUIDE.md`
- **Purpose:** Complete installation instructions for staff
- **Contents:**
  - System requirements
  - Step-by-step installation
  - Troubleshooting guide
  - Usage instructions

## Installation Process:

### For IT Staff:
1. **Extract deployment package** to a folder
2. **Run `INSTALL.bat` as administrator**
3. **Verify installation** works correctly
4. **Distribute to staff** via network share or USB

### For End Users:
1. **Double-click desktop shortcut**
2. **Place CSV files** in `data/inputs/` folder
3. **Run the application**
4. **Review results** in `data/outputs/` folder

## Installation Directory Structure:
```
C:\FoxFuel_KFactor_Optimizer\
├── FoxFuel_KFactor_Optimizer.exe
├── RUN_GUI.bat
├── FoxFuel_KFactor_User_Guide.md
├── README.md
├── INSTALLATION_GUIDE.md
└── data\
    ├── inputs\          (place CSV files here)
    └── outputs\         (results appear here)
```

## System Requirements:

- **OS:** Windows 10 or later (64-bit recommended)
- **RAM:** 4 GB minimum
- **Disk Space:** 500 MB free space
- **No Python Required:** Standalone executable

## Troubleshooting:

- **Permission Errors:** Run installer as administrator
- **Antivirus Issues:** Add exception for the executable
- **Missing Files:** Ensure complete deployment package
- **Excel Locked:** Close Excel before running optimizer

## Support:

- **User Guide:** `FoxFuel_KFactor_User_Guide.md`
- **Installation Guide:** `INSTALLATION_GUIDE.md`
- **Quick Start:** `README.md`
