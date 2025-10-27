# User Guide: Deployment Tools

## Overview

Deployment Tools are used to install and distribute the FoxFuel K-Factor Optimizer to staff computers. These tools provide automated installation, shortcuts, and documentation for end users.

## 🎯 **Quick Start**

### **For IT Staff (Installing on Multiple Computers)**

1. **Obtain deployment package:**
   - Download from network share or build using build tools
   - File: `FoxFuel_KFactor_Optimizer_Deployment_YYYYMMDD_HHMMSS.zip`

2. **Extract package:**
   - Right-click ZIP file → "Extract All..."
   - Choose destination folder

3. **Run installer:**
   - Navigate to extracted folder
   - **Right-click** `INSTALL.bat`
   - Select "Run as administrator"
   - Follow on-screen prompts

4. **Verify installation:**
   - Check for desktop shortcut
   - Verify folder structure created
   - Test application

### **For End Users (After Installation)**

1. **Double-click desktop shortcut** or `RUN_GUI.bat`
2. **Place CSV files** in `data/inputs/` folder
3. **Click "Run K-Factor Optimizer"**
4. **Review results** in output files

## 📋 **Installation Process**

### **Step-by-Step Installation:**

#### **Step 1: Extract Package**
```
Right-click FoxFuel_KFactor_Optimizer_Deployment.zip
→ Extract All...
→ Choose destination (e.g., C:\Programs\)
→ Click Extract
```

#### **Step 2: Run Installer**
```
Navigate to extracted folder
Right-click INSTALL.bat
→ Run as administrator
→ Press Enter when prompted
→ Installation completes automatically
```

#### **Step 3: Verify Installation**
```
✓ Desktop shortcut created
✓ Installation directory created (e.g., C:\FoxFuel_KFactor_Optimizer\)
✓ Folder structure in place
✓ Executable file present
```

#### **Step 4: Initial Setup**
```
✓ Place CSV files in: data/inputs/
✓ CSV files: 03_*.csv, 04_*.csv, 06_*.csv
✓ Ready to run application
```

### **Installation Directory Structure:**
```
C:\FoxFuel_KFactor_Optimizer\
├── FoxFuel_KFactor_Optimizer.exe
├── RUN_GUI.bat
├── README.md
├── FoxFuel_KFactor_User_Guide.md
├── INSTALLATION_GUIDE.md
└── data/
    ├── inputs/          (Place CSV files here)
    └── outputs/          (Results appear here)
```

## 🔧 **Deployment Tools Files**

### **INSTALL.bat**
**Purpose:** Automated installation script

**Features:**
- Creates installation directory
- Copies all necessary files
- Sets up folder structure
- Creates desktop shortcut
- Configures file permissions

**Usage:**
```
Right-click INSTALL.bat
→ Run as administrator
→ Follow prompts
```

**Requirements:**
- Administrator privileges
- Disk space (500 MB minimum)
- Windows 10 or later

### **RUN_GUI.bat**
**Purpose:** Simple launcher for GUI application

**Features:**
- Double-click to run
- No command line knowledge required
- Quick access to application

**Usage:**
```
Double-click RUN_GUI.bat
→ GUI application opens
→ Click "Run K-Factor Optimizer"
```

## 📊 **Installation Options**

### **Option 1: Automated Installation (Recommended)**

**Process:**
1. Extract deployment package
2. Run `INSTALL.bat` as administrator
3. System creates all necessary files and folders
4. Desktop shortcut created automatically
5. Ready to use

**Best for:**
- Standard deployments
- Non-technical staff
- Consistent installation across computers

### **Option 2: Manual Installation**

**Process:**
1. Extract deployment package
2. Copy `FoxFuel_KFactor_Optimizer.exe` to desired location
3. Create `data/inputs/` and `data/outputs/` folders
4. Run executable

**Best for:**
- Custom locations
- Advanced users
- Portable installations

## 🎨 **Desktop Shortcut**

### **Creating Shortcut Automatically:**
- Run `INSTALL.bat` → Shortcut created automatically

### **Manually Creating Shortcut:**
```
1. Right-click desktop
2. New → Shortcut
3. Browse to: C:\FoxFuel_KFactor_Optimizer\FoxFuel_KFactor_Optimizer.exe
4. Name: "FoxFuel K-Factor Optimizer"
5. Click Finish
```

### **Shortcut Properties:**
- **Icon:** Custom application icon (if provided)
- **Run as:** Normal user
- **Start in:** Application directory

## 📦 **Post-Installation Setup**

### **1. Place Input Files**
```
Navigate to: C:\FoxFuel_KFactor_Optimizer\data\inputs\
Place CSV files:
  - 03_CustomerFuel.csv
  - 04_DeliveryTickets.csv
  - 06_DegreeDayValues.csv
```

### **2. Test Application**
```
✓ Double-click desktop shortcut
✓ Verify GUI opens
✓ Click "Auto-Detect Files"
✓ Verify files are detected
✓ Ready to use!
```

### **3. Configure (Optional)**
```
✓ Adjust governance rules (src/config.py)
✓ Customize output format
✓ Configure logging
✓ Set up scheduled runs
```

## 🐛 **Troubleshooting**

### **"Administrator privileges required"**
- **Problem:** INSTALL.bat needs admin rights
- **Solution:** Right-click → Run as administrator

### **"Installation directory not created"**
- **Problem:** Permissions issue
- **Solution:** Run as administrator, check folder permissions

### **"Desktop shortcut not created"**
- **Problem:** Administrative restriction
- **Solution:** Manually create shortcut after installation

### **"Data folder missing"**
- **Problem:** Installation incomplete
- **Solution:** 
  - Re-run INSTALL.bat
  - Or manually create `data/inputs/` and `data/outputs/` folders

### **"Executable won't run"**
- **Problem:** Antivirus or Windows Defender blocking
- **Solution:**
  - Add exception in antivirus settings
  - Check Windows Defender exclusions
  - Run as administrator

### **"CSV files not detected"**
- **Problem:** Files not in correct location
- **Solution:**
  - Place files in `data/inputs/` folder
  - Check file naming: `03_*.csv`, `04_*.csv`, `06_*.csv`
  - Verify files exist

## 💡 **Best Practices**

### **Installation:**
1. **Test on One Computer:** Verify installation before mass deployment
2. **Document Steps:** Keep notes on installation process
3. **Backup System:** Create system restore point before installation
4. **Training:** Provide staff training on using the tool
5. **Support:** Establish support contact for issues

### **Maintenance:**
1. **Regular Updates:** Reinstall when new versions available
2. **Clean Uninstall:** Remove old versions before installing new
3. **Data Backup:** Keep previous results for reference
4. **Documentation:** Keep user guides accessible
5. **Monitoring:** Track usage and issues

## 📈 **Updating the Application**

### **When Updates Available:**
1. **Download new deployment package**
2. **Uninstall old version** (optional)
3. **Run installation process** again
4. **Desktop shortcut updates** automatically
5. **Test new version**

### **Version Control:**
- Keep track of installed versions
- Note any custom configurations
- Document any issues encountered
- Maintain change log

## 🔗 **Related Tools**

- **Build Tools:** `tools/build_tools/` - Create deployment packages
- **Main Application:** `tools/main_app/` - Run the optimizer
- **Analysis Tools:** `tools/analysis_tools/` - Customer investigation
- **Documentation:** `tools/documentation/` - User guides

## 📞 **Support**

For installation issues:
1. Check Windows version (10+ required)
2. Verify administrator privileges
3. Check disk space (500 MB minimum)
4. Review error messages in installation output
5. Contact IT support

---

**Last Updated:** October 2025  
**Version:** 1.0
