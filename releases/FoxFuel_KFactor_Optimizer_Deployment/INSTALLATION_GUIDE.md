# FoxFuel K-Factor Optimizer - Installation Guide

## 📦 **Deployment Package Contents**

When you receive the FoxFuel K-Factor Optimizer deployment package, it should contain:

```
FoxFuel_KFactor_Optimizer_Deployment/
├── FoxFuel_KFactor_Optimizer.exe    ← Main application (320 MB)
├── INSTALL.bat                       ← Automated installer
├── FoxFuel_KFactor_User_Guide.md    ← User manual
├── README.md                         ← Quick reference
└── RUN_GUI.bat                      ← Simple launcher
```

## 🚀 **Installation Methods**

### **Method 1: Automated Installation (Recommended)**

1. **Extract** the deployment package to a folder on the target computer
2. **Right-click** `INSTALL.bat` and select "Run as administrator"
3. **Follow** the on-screen prompts
4. **Wait** for installation to complete
5. **Place CSV files** in the created `data/inputs/` folder
6. **Run** the application using the desktop shortcut

### **Method 2: Manual Installation**

1. **Create** a folder called `FoxFuel_KFactor_Optimizer`
2. **Copy** `FoxFuel_KFactor_Optimizer.exe` into this folder
3. **Create** the following folder structure:
   ```
   FoxFuel_KFactor_Optimizer/
   ├── FoxFuel_KFactor_Optimizer.exe
   └── data/
       ├── inputs/     ← Place CSV files here
       └── outputs/    ← Results will appear here
   ```
4. **Place CSV files** in `data/inputs/` folder
5. **Double-click** `FoxFuel_KFactor_Optimizer.exe` to run

## 💻 **System Requirements**

### **Minimum Requirements:**
- **Operating System:** Windows 10 or later
- **RAM:** 4 GB minimum, 8 GB recommended
- **Storage:** 500 MB free space
- **Permissions:** Ability to create folders and files

### **What's NOT Required:**
- ❌ Python installation
- ❌ Additional software dependencies
- ❌ Internet connection (after installation)
- ❌ Administrator privileges (for normal use)

## 📋 **Pre-Installation Checklist**

Before installing on a staff computer:

- [ ] **Verify** Windows version (10 or later)
- [ ] **Check** available disk space (500+ MB)
- [ ] **Ensure** user has folder creation permissions
- [ ] **Prepare** CSV files from Ignite exports
- [ ] **Plan** installation location (recommend C:\FoxFuel_KFactor_Optimizer\)

## 🔧 **Installation Steps (Detailed)**

### **Step 1: Prepare the Computer**
1. **Close** any running applications
2. **Create** a dedicated folder for the application
3. **Ensure** you have write permissions to the chosen location

### **Step 2: Run the Installer**
1. **Right-click** `INSTALL.bat`
2. **Select** "Run as administrator"
3. **Click** "Yes" when prompted by Windows
4. **Wait** for the installation to complete

### **Step 3: Verify Installation**
The installer will create:
- ✅ Application folder with executable
- ✅ Data folder structure (`data/inputs/` and `data/outputs/`)
- ✅ Desktop shortcut
- ✅ Start menu shortcut

### **Step 4: Add CSV Files**
1. **Export** the following files from Ignite:
   - `03_CustomerFuel.csv`
   - `04_DeliveryTickets.csv`
   - `06_DegreeDayValues.csv`
2. **Place** these files in `data/inputs/` folder
3. **Verify** file names match exactly (case-sensitive)

### **Step 5: Test the Application**
1. **Double-click** the desktop shortcut
2. **Verify** the GUI opens correctly
3. **Click** "Auto-Detect Files"
4. **Confirm** all three CSV files are detected
5. **Click** "Run K-Factor Optimizer"
6. **Check** that results are generated

## 🛠️ **Troubleshooting Installation**

### **Common Issues:**

#### **"Access Denied" Error**
- **Solution:** Run installer as administrator
- **Alternative:** Choose a different installation location

#### **"Folder Already Exists" Warning**
- **Solution:** This is normal - installer will use existing folder
- **Action:** No action needed, continue with installation

#### **Executable Not Found**
- **Solution:** Ensure `FoxFuel_KFactor_Optimizer.exe` is in the same folder as `INSTALL.bat`
- **Check:** File size should be approximately 320 MB

#### **Shortcut Creation Failed**
- **Solution:** This is not critical - you can still run the application directly
- **Alternative:** Manually create shortcuts if needed

### **Installation Verification:**

After installation, verify these items exist:
- [ ] `FoxFuel_KFactor_Optimizer.exe` in the application folder
- [ ] `data/inputs/` folder (empty, ready for CSV files)
- [ ] `data/outputs/` folder (empty, ready for results)
- [ ] Desktop shortcut (optional)
- [ ] Start menu shortcut (optional)

## 📞 **Support Information**

### **If Installation Fails:**
1. **Check** system requirements
2. **Verify** file permissions
3. **Try** manual installation method
4. **Contact** IT support with error details

### **If Application Won't Run:**
1. **Check** that CSV files are in `data/inputs/`
2. **Verify** CSV file names match exactly
3. **Ensure** CSV files are not corrupted
4. **Try** running as administrator

### **For Additional Help:**
- **Refer** to `FoxFuel_KFactor_User_Guide.md`
- **Check** the application log output
- **Contact** the system administrator

## 🔄 **Updating the Application**

To update to a newer version:
1. **Backup** any custom configurations
2. **Run** the new installer
3. **Replace** the old executable
4. **Test** the updated application

## 📁 **File Locations After Installation**

```
C:\FoxFuel_KFactor_Optimizer\          ← Main application folder
├── FoxFuel_KFactor_Optimizer.exe     ← Executable file
├── data\
│   ├── inputs\                        ← CSV files go here
│   │   ├── 03_CustomerFuel.csv
│   │   ├── 04_DeliveryTickets.csv
│   │   └── 06_DegreeDayValues.csv
│   └── outputs\                       ← Results appear here
│       ├── Apply_K_ThisWeek.csv
│       └── K_Review_Queue.xlsx
└── logs\                              ← Log files (if any)
```

---

**Installation Complete!** The FoxFuel K-Factor Optimizer is now ready for use on this computer.
