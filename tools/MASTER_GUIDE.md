# FoxFuel K-Factor Optimizer - Complete User Guide

## 📚 **Guide Overview**

This comprehensive guide covers all tools and features of the FoxFuel K-Factor Optimizer system. Navigate to specific sections based on your role and needs.

## 🎯 **Quick Navigation**

| I Need To... | Go To Section | Guide Location |
|--------------|---------------|----------------|
| **Run K-Factor Optimization** | [Main Application Guide](#main-application) | `tools/main_app/USER_GUIDE.md` |
| **Investigate a Customer** | [Customer Analysis Guide](#customer-analysis) | `tools/analysis_tools/USER_GUIDE.md` |
| **Build Executables** | [Build Tools Guide](#build-tools) | `tools/build_tools/USER_GUIDE.md` |
| **Install on Computers** | [Deployment Guide](#deployment) | `tools/deployment/USER_GUIDE.md` |

## 📖 **Detailed Guides**

### 1. Main Application Guide

**Location:** `tools/main_app/USER_GUIDE.md`

**What it covers:**
- Running the K-Factor optimizer
- GUI application features
- Batch file execution
- Command-line options
- Configuration settings
- Output file interpretation
- Troubleshooting common issues

**Best for:**
- Staff running weekly K-factor updates
- Users who need to process CSV files
- People using the tool for regular operations

**Quick Link:** [Read Main Application Guide](tools/main_app/USER_GUIDE.md)

---

### 2. Customer Analysis Guide

**Location:** `tools/analysis_tools/USER_GUIDE.md`

**What it covers:**
- Using the customer analysis tool
- Investigating specific customers
- Understanding calculation logic
- Interpreting analysis results
- Debugging issues
- Validating calculations

**Best for:**
- Supervisors investigating issues
- IT staff troubleshooting
- QA teams validating results
- Training new users

**Quick Link:** [Read Customer Analysis Guide](tools/analysis_tools/USER_GUIDE.md)

---

### 3. Build Tools Guide

**Location:** `tools/build_tools/USER_GUIDE.md`

**What it covers:**
- Building standalone executables
- Creating deployment packages
- Understanding build process
- Distribution strategies
- Version management

**Best for:**
- Developers building executables
- IT staff creating deployment packages
- Administrators packaging software

**Quick Link:** [Read Build Tools Guide](tools/build_tools/USER_GUIDE.md)

---

### 4. Deployment Guide

**Location:** `tools/deployment/USER_GUIDE.md`

**What it covers:**
- Installing on staff computers
- Automated installation process
- Manual installation steps
- Desktop shortcuts
- Post-installation setup
- Troubleshooting installation

**Best for:**
- IT staff deploying to computers
- End users following installation
- Administrators managing distribution

**Quick Link:** [Read Deployment Guide](tools/deployment/USER_GUIDE.md)

---

## 🚀 **Quick Start by Role**

### **For End Users (Staff Members)**

1. **Get Started:**
   - Read [Main Application Guide](tools/main_app/USER_GUIDE.md)
   - Place CSV files in `data/inputs/` folder
   - Run the GUI application

2. **Weekly Process:**
   - Export CSVs from Ignite
   - Place in `data/inputs/` folder
   - Run K-Factor Optimizer
   - Review results
   - Import approved changes

3. **Need Help:**
   - Check troubleshooting section
   - Use customer analysis tool for issues
   - Contact IT support

### **For IT Staff**

1. **Installation:**
   - Read [Deployment Guide](tools/deployment/USER_GUIDE.md)
   - Run automated installer
   - Configure for staff

2. **Maintenance:**
   - Update executables as needed
   - Troubleshoot issues
   - Train staff

3. **Support:**
   - Use customer analysis tool
   - Check log files
   - Consult documentation

### **For Supervisors**

1. **Review Process:**
   - Check K_Review_Queue.xlsx weekly
   - Review flagged customers
   - Approve or modify recommendations

2. **Investigation:**
   - Use [Customer Analysis Tool](tools/analysis_tools/USER_GUIDE.md)
   - Enter customer numbers to investigate
   - Review calculation logic

3. **Quality Control:**
   - Spot-check results
   - Validate governance rules
   - Track customer issues

### **For Developers**

1. **Building:**
   - Read [Build Tools Guide](tools/build_tools/USER_GUIDE.md)
   - Create executables
   - Package for distribution

2. **Customization:**
   - Modify governance rules in `src/config.py`
   - Update calculation logic as needed
   - Test thoroughly before deployment

3. **Documentation:**
   - Keep guides updated
   - Document changes
   - Maintain version control

## 📋 **Common Tasks**

### **Task 1: Run Weekly K-Factor Optimization**

**Steps:**
1. Export CSVs from Ignite
2. Place files in `data/inputs/` folder
3. Run GUI application or batch file
4. Review output files
5. Import approved changes to Ignite

**See:** [Main Application Guide](tools/main_app/USER_GUIDE.md)

### **Task 2: Investigate Customer K-Factor**

**Steps:**
1. Open customer analysis tool
2. Enter customer number
3. Click "Analyze"
4. Review calculation details
5. Verify governance rules applied

**See:** [Customer Analysis Guide](tools/analysis_tools/USER_GUIDE.md)

### **Task 3: Install on New Computer**

**Steps:**
1. Obtain deployment package
2. Extract ZIP file
3. Run `INSTALL.bat` as administrator
4. Place CSV files
5. Test application

**See:** [Deployment Guide](tools/deployment/USER_GUIDE.md)

### **Task 4: Build New Executable**

**Steps:**
1. Update code if needed
2. Run `build_gui_exe.py`
3. Wait for build completion
4. Test executable
5. Package for distribution

**See:** [Build Tools Guide](tools/build_tools/USER_GUIDE.md)

## 🐛 **Troubleshooting by Issue**

### **"Can't find CSV files"**
- **Check:** File location in `data/inputs/`
- **Check:** File naming (03_*.csv, 04_*.csv, 06_*.csv)
- **See:** [Main Application Guide - Troubleshooting](tools/main_app/USER_GUIDE.md#troubleshooting)

### **"Customer results seem wrong"**
- **Use:** Customer Analysis Tool
- **See:** [Customer Analysis Guide](tools/analysis_tools/USER_GUIDE.md)
- **Check:** Input data quality

### **"Installation failed"**
- **Check:** Administrator privileges
- **Check:** Disk space (500 MB minimum)
- **See:** [Deployment Guide - Troubleshooting](tools/deployment/USER_GUIDE.md#troubleshooting)

### **"Build failed"**
- **Check:** Python version (3.8+)
- **Check:** All dependencies installed
- **See:** [Build Tools Guide - Troubleshooting](tools/build_tools/USER_GUIDE.md#troubleshooting)

## 📞 **Getting Help**

### **By Issue Type:**
- **Application Issues:** See [Main Application Guide - Troubleshooting](tools/main_app/USER_GUIDE.md#troubleshooting)
- **Analysis Questions:** See [Customer Analysis Guide](tools/analysis_tools/USER_GUIDE.md)
- **Installation Problems:** See [Deployment Guide - Troubleshooting](tools/deployment/USER_GUIDE.md#troubleshooting)
- **Build Issues:** See [Build Tools Guide - Troubleshooting](tools/build_tools/USER_GUIDE.md#troubleshooting)

### **Contact Points:**
- **IT Support:** For technical issues
- **Supervisor:** For business rule questions
- **Developer:** For bug reports
- **Documentation:** Refer to this guide

## 🔗 **Additional Resources**

- **GitHub Repository:** [FoxFuel_KFactor_Optimizer](https://github.com/dynamix77/FoxFuel_KFactor_Optimizer)
- **Main README:** `README.md` - Project overview
- **GitHub Setup:** `tools/documentation/GitHub_Setup_Guide.md`
- **User Guide:** `FoxFuel_KFactor_User_Guide.md` - Original comprehensive guide

## 📈 **Best Practices Summary**

1. **Run Weekly:** Update K-factors on a regular schedule
2. **Review Queue:** Always check K_Review_Queue.xlsx
3. **Validate:** Spot-check results for accuracy
4. **Document:** Keep notes on manual overrides
5. **Backup:** Keep previous week's results
6. **Test First:** Test on sample data before production
7. **Train Staff:** Ensure everyone understands the tool
8. **Support:** Provide clear escalation path

---

**Last Updated:** October 2025  
**Version:** 1.0  
**System:** FoxFuel K-Factor Optimizer
