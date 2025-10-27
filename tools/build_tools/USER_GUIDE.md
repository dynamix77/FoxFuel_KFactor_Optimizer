# User Guide: Build Tools

## Overview

Build Tools are used to create standalone executables and deployment packages for the FoxFuel K-Factor Optimizer. These tools package Python applications into self-contained executables that don't require Python installation.

## 🎯 **Quick Start**

### **Build Main GUI Executable**
1. **Navigate to:** `tools/build_tools/` folder
2. **Run:** `python build_gui_exe.py`
3. **Wait for completion** (may take several minutes)
4. **Find executable** in `dist/` folder

### **Build Customer Analysis Tool**
1. **Navigate to:** `tools/build_tools/` folder
2. **Run:** `python build_analysis_exe.py`
3. **Wait for completion**
4. **Find executable** in `dist/` folder

### **Create Deployment Package**
1. **Navigate to:** `tools/build_tools/` folder
2. **Run:** `python create_deployment_package.py`
3. **Wait for completion**
4. **Find package** in the main directory

## 📋 **Prerequisites**

### **Required Software:**
- **Python 3.8+** installed
- **PyInstaller:** `pip install pyinstaller`
- **All dependencies:** `pip install -r requirements.txt`

### **Disk Space:**
- At least 2 GB free space (for build process)
- Executable files are ~300-320 MB each

## 🔧 **Build Process**

### **Main GUI Executable (`build_gui_exe.py`)**

**Purpose:** Creates standalone GUI application

**Output:**
- `dist/FoxFuel_KFactor_Optimizer.exe` (~320 MB)
- Self-contained, no Python required
- Includes all dependencies (pandas, openpyxl, tkinter, etc.)

**Features:**
- Windowed application (no console)
- Full GUI functionality
- File browsing and management
- Progress feedback
- Error handling

**Usage:**
```bash
python build_gui_exe.py
```

### **Customer Analysis Tool (`build_analysis_exe.py`)**

**Purpose:** Creates standalone analysis tool

**Output:**
- `dist/FoxFuel_KFactor_Analysis_Tool.exe` (~300 MB)
- Self-contained analysis GUI
- Customer investigation tool

**Features:**
- Customer lookup interface
- Detailed calculation trace
- Summary and detailed views
- Governance rule display

**Usage:**
```bash
python build_analysis_exe.py
```

### **Deployment Package Creator (`create_deployment_package.py`)**

**Purpose:** Creates complete installation package

**Output:**
- `FoxFuel_KFactor_Optimizer_Deployment_YYYYMMDD_HHMMSS.zip`
- Contains executable, documentation, installer
- Ready for staff deployment

**Contents:**
- `FoxFuel_KFactor_Optimizer.exe` - Main application
- `INSTALL.bat` - Automated installer
- `RUN_GUI.bat` - Simple launcher
- `FoxFuel_KFactor_User_Guide.md` - User manual
- `INSTALLATION_GUIDE.md` - Setup instructions
- `data/` - Folder structure template

**Usage:**
```bash
python create_deployment_package.py
```

## 📦 **Deployment Package Contents**

```
FoxFuel_KFactor_Optimizer_Deployment/
├── FoxFuel_KFactor_Optimizer.exe    (Main application)
├── INSTALL.bat                       (Automated installer)
├── RUN_GUI.bat                      (Quick launcher)
├── FoxFuel_KFactor_User_Guide.md    (User manual)
├── INSTALLATION_GUIDE.md            (Setup guide)
├── README.md                        (Quick start)
├── PACKAGE_INFO.txt                 (Package info)
└── data/                            (Folder structure)
    ├── inputs/                      (Place CSV files here)
    │   └── README.txt
    └── outputs/                     (Results appear here)
        └── README.txt
```

## 🚀 **Distributing Executables**

### **For Internal Use:**
1. **Copy executable** to network share
2. **Staff download** and run
3. **Create desktop shortcut** (optional)

### **For Remote Staff:**
1. **Upload deployment package** to file sharing service
2. **Provide download link** to staff
3. **Include installation instructions**

### **For Individual PCs:**
1. **Use deployment package**
2. **Run INSTALL.bat** as administrator
3. **Desktop shortcut created** automatically

## 🔍 **Understanding Build Output**

### **Build Messages:**
```
✓ PyInstaller version: 5.0
✓ Building executable...
✓ Collecting dependencies...
✓ Generating executable...
✓ Build completed successfully!
```

### **Common Messages:**
- **"WARN: Hidden import"** - Normal, PyInstaller is including dependencies
- **"WARN: Binary replacement"** - Normal, file optimization
- **"INFO: Analyzing"** - PyInstaller is analyzing dependencies

### **Build Time:**
- **Main GUI:** 2-5 minutes (depending on computer speed)
- **Analysis Tool:** 2-4 minutes
- **Deployment Package:** 5-10 minutes

## 🐛 **Troubleshooting**

### **"PyInstaller not found"**
- **Problem:** PyInstaller not installed
- **Solution:** `pip install pyinstaller`

### **"Module not found" during build**
- **Problem:** Missing dependency
- **Solution:** `pip install -r requirements.txt`

### **Build fails with "Permission denied"**
- **Problem:** Output directory locked
- **Solution:** Close any programs using the directory

### **Executable is too large**
- **Problem:** Normal behavior
- **Solution:** Files are large because they include all dependencies
- **Note:** This is expected for standalone executables

### **Executable doesn't run on other computers**
- **Problem:** Missing Windows updates or antivirus blocking
- **Solution:**
  - Ensure Windows is up to date
  - Add antivirus exception
  - Run as administrator

## 💡 **Tips**

1. **Test Before Distribution:** Run executable on clean system
2. **Check File Size:** Executables should be ~300-320 MB
3. **Include Documentation:** Always provide user guide
4. **Update Regularly:** Rebuild when updating code
5. **Version Control:** Keep track of which version is deployed

## 📈 **Best Practices**

### **Building:**
1. **Clean Build:** Delete `build/` and `dist/` folders before rebuilding
2. **Test Thoroughly:** Test executable before distribution
3. **Include Documentation:** Always include user guides
4. **Version Info:** Update version numbers in code
5. **Backup:** Keep previous versions

### **Distribution:**
1. **Use Deployment Package:** Easiest for end users
2. **Provide Instructions:** Always include installation guide
3. **Support Contact:** Include contact information
4. **Update Mechanism:** Plan for future updates
5. **Documentation:** Make user guides accessible

## 🔗 **Related Tools**

- **Main Application:** `tools/main_app/` - Run the optimizer
- **Analysis Tools:** `tools/analysis_tools/` - Customer investigation
- **Deployment Tools:** `tools/deployment/` - Installation scripts
- **Documentation:** `tools/documentation/` - User guides

## 📞 **Support**

For build issues:
1. Check Python version (3.8+ required)
2. Verify all dependencies installed
3. Check disk space (2+ GB required)
4. Review build output for specific errors
5. Contact developer for assistance

---

**Last Updated:** October 2025  
**Version:** 1.0
