# FoxFuel K-Factor Optimizer - Tools

This folder contains all the tools and utilities for the FoxFuel K-Factor Optimizer system, organized by function.

## 📁 Folder Structure:

### `main_app/` - Core Applications
- **GUI Runner** (`gui_runner.py`) - Main graphical interface
- **Command Line** (`run_local.py`) - Console version
- **Batch Launcher** (`RUN_KFACTOR.bat`) - One-click execution

### `analysis_tools/` - Customer Analysis
- **Customer Analysis GUI** (`customer_analysis_gui.py`) - Trace K-factor calculations
- **Analysis Launcher** (`RUN_ANALYSIS.bat`) - Quick launcher

### `build_tools/` - Executable Builders
- **GUI Executable Builder** (`build_gui_exe.py`) - Creates standalone GUI
- **Analysis Tool Builder** (`build_analysis_exe.py`) - Creates analysis executable
- **Deployment Package Creator** (`create_deployment_package.py`) - Complete installer

### `deployment/` - Installation Tools
- **Automated Installer** (`INSTALL.bat`) - Staff computer setup
- **GUI Launcher** (`RUN_GUI.bat`) - Simple launcher
- **Installation Guide** (`INSTALLATION_GUIDE.md`) - Complete setup instructions

### `documentation/` - User Guides
- **User Manual** (`FoxFuel_KFactor_User_Guide.md`) - Complete usage guide
- **GitHub Setup** (`GitHub_Setup_Guide.md`) - Repository management

## 🚀 Quick Start:

### For End Users:
1. **Use Main App:** Go to `main_app/` folder
2. **Run GUI:** Double-click `RUN_KFACTOR.bat`
3. **Place CSV files** in `data/inputs/` folder
4. **Review results** in `data/outputs/` folder

### For Analysis:
1. **Use Analysis Tools:** Go to `analysis_tools/` folder
2. **Run Analysis:** Double-click `RUN_ANALYSIS.bat`
3. **Enter customer number** and analyze

### For IT Deployment:
1. **Use Build Tools:** Go to `build_tools/` folder
2. **Create Executable:** Run `build_gui_exe.py`
3. **Create Package:** Run `create_deployment_package.py`
4. **Deploy:** Use `deployment/` tools

## 📋 Tool Categories:

| Category | Purpose | Target User |
|----------|---------|-------------|
| **Main App** | Daily K-factor optimization | Staff members |
| **Analysis** | Troubleshooting & validation | Supervisors, IT |
| **Build** | Creating executables | Developers, IT |
| **Deployment** | Installing on computers | IT staff |
| **Documentation** | User guides & manuals | Everyone |

## 🔧 Prerequisites:

- **Python 3.8+** (for development)
- **Required packages:** `pip install -r requirements.txt`
- **Windows 10+** (for executables)
- **CSV files** in `data/inputs/` folder

## 📖 Documentation:

Each folder contains its own README with detailed instructions. Start with:
- **`main_app/README.md`** - For daily usage
- **`documentation/FoxFuel_KFactor_User_Guide.md`** - Complete manual
- **`deployment/INSTALLATION_GUIDE.md`** - For installation

## 🆘 Support:

- **User Guide:** `documentation/FoxFuel_KFactor_User_Guide.md`
- **Troubleshooting:** Check individual folder READMEs
- **Analysis Tool:** Use `analysis_tools/` for debugging
