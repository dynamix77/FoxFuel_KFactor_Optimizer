# Releases

This folder contains generated executables and deployment packages for the FoxFuel K-Factor Optimizer.

## 🚫 **Note: Large Files Not in Git**

Due to GitHub's 100MB file size limit, the following large files are **NOT** tracked in Git:

- `FoxFuel_KFactor_Optimizer.exe` (~320 MB) - Main GUI executable
- `FoxFuel_KFactor_Optimizer_Deployment_*.zip` (~320 MB) - Complete deployment packages

## 📦 **How to Get Executables:**

### **Option 1: Build Your Own**
1. Go to `tools/build_tools/` folder
2. Run `python build_gui_exe.py` to create the GUI executable
3. Run `python create_deployment_package.py` to create deployment package

### **Option 2: Download from Releases**
1. Go to the [GitHub Releases page](https://github.com/dynamix77/FoxFuel_KFactor_Optimizer/releases)
2. Download the latest release assets
3. Extract and use the executables

### **Option 3: Use Python Version**
1. Install Python dependencies: `pip install -r requirements.txt`
2. Run from `tools/main_app/` folder:
   - `python gui_runner.py` (GUI version)
   - `python run_local.py` (command-line version)

## 📁 **What's Included:**

### **Deployment Package Contents:**
- `FoxFuel_KFactor_Optimizer.exe` - Main GUI application
- `INSTALL.bat` - Automated installer
- `RUN_GUI.bat` - Simple launcher
- `FoxFuel_KFactor_User_Guide.md` - Complete user manual
- `INSTALLATION_GUIDE.md` - Setup instructions
- `data/` folder structure for inputs/outputs

### **Installation Process:**
1. Extract the deployment package
2. Run `INSTALL.bat` as administrator
3. Place CSV files in `data/inputs/` folder
4. Double-click the executable to run

## 🔧 **Build Requirements:**

- Python 3.8+
- PyInstaller: `pip install pyinstaller`
- All dependencies from `requirements.txt`

## 📋 **File Sizes:**

| File | Size | Purpose |
|------|------|---------|
| `FoxFuel_KFactor_Optimizer.exe` | ~320 MB | Main GUI executable |
| `Deployment Package.zip` | ~320 MB | Complete installer |
| `Customer_Analysis_Tool.exe` | ~300 MB | Analysis tool executable |

## 🚀 **Quick Start:**

1. **For End Users:** Use the deployment package
2. **For Developers:** Build your own executables
3. **For Analysis:** Use the customer analysis tool

The executables are standalone and don't require Python installation on target computers!
