# FoxFuel K-Factor Optimizer - Complete User Guide

> **Complete guide for all tools in the FoxFuel K-Factor Optimizer system**

## Table of Contents

1. [Introduction](#introduction)
2. [Getting Started](#getting-started)
3. [Main K-Factor Optimizer](#main-k-factor-optimizer)
4. [Customer Analysis Tool](#customer-analysis-tool)
5. [Build Tools](#build-tools)
6. [Deployment Tools](#deployment-tools)
7. [Understanding the System](#understanding-the-system)
8. [Troubleshooting](#troubleshooting)
9. [Best Practices](#best-practices)
10. [Quick Reference](#quick-reference)

---

## Introduction

### What is the K-Factor Optimizer?

The FoxFuel K-Factor Optimizer is a data processing tool that analyzes heating oil delivery patterns and automatically calculates optimized K-factors for customers. It processes three CSV exports from Ignite and generates two output files.

### System Overview

- **Input:** Three CSV files from Ignite (CustomerFuel, DeliveryTickets, DegreeDayValues)
- **Process:** Analyzes delivery intervals, calculates K-factors, applies governance rules
- **Output:** Two files - one for automatic application, one for manual review

### Key Features

- ✅ **One-Click Operation** - Multiple deployment options
- ✅ **Automatic File Detection** - Finds latest CSV files
- ✅ **Governance Rules** - Safety limits prevent dangerous changes
- ✅ **Multiple Output Formats** - CSV for import, Excel for review
- ✅ **Comprehensive Logging** - Detailed processing logs
- ✅ **GUI Interface** - User-friendly with progress feedback

---

## Getting Started

### System Requirements

**Minimum Requirements:**
- Windows 10 or later (64-bit recommended)
- 4 GB RAM
- 500 MB disk space

**For Python Development:**
- Python 3.8 or higher
- Required packages: `pip install -r requirements.txt`

### Required Input Files

Place these CSV files in `data/inputs/` folder:
- `03_CustomerFuel.csv` - Customer fuel information
- `04_DeliveryTickets.csv` - Delivery transaction history
- `06_DegreeDayValues.csv` - Degree day reference data

### Installation Options

**Option 1: Standalone Executable (Recommended)**
- No Python installation required
- Download and run immediately
- Best for staff computers

**Option 2: Python with GUI**
- Run `python gui_runner.py`
- Full GUI functionality
- Best for developers

**Option 3: Batch File**
- Double-click `RUN_KFACTOR.bat`
- Simple command-line execution

---

## Main K-Factor Optimizer

### Overview

The Main K-Factor Optimizer is the core application that processes your Ignite CSV exports and generates optimized K-factors for all customers.

### Quick Start

1. **Place CSV files** in `data/inputs/` folder
2. **Navigate to:** `tools/main_app/` folder
3. **Run:** `python gui_runner.py`
4. **Click "Auto-Detect Files"** to find your CSV files
5. **Click "Run K-Factor Optimizer"** to start
6. **Review results** using the buttons in the GUI

### GUI Application Features

**Main Window Buttons:**
- **Auto-Detect Files:** Automatically finds your CSV files
- **Run K-Factor Optimizer:** Starts the optimization process
- **Open Apply_K_ThisWeek.csv:** Opens the auto-apply file
- **Open K_Review_Queue.xlsx:** Opens the review queue file
- **Open Output Folder:** Opens the output directory

**Progress Indicators:**
- Loading bar shows processing progress
- Status messages display current step
- Success/error messages at completion
- Summary statistics after completion

### Output Files

#### Apply_K_ThisWeek.csv
**Purpose:** Customers ready for automatic K-factor import

**Contents:**
- Customer Number
- K Factor - Winter (proposed)
- Confidence score
- Status

**Usage:**
1. Review file for accuracy
2. Import into Ignite using data import function
3. Customer K-factors updated automatically

#### K_Review_Queue.xlsx
**Purpose:** Customers requiring manual review

**Contains Two Sheets:**

**Review Sheet:**
- Current Winter K-factor
- Calculated K-factor
- Proposed K-factor
- Variance percentage
- Status and reason
- Confidence level
- Interval count
- Total gallons and degree days

**Auto-Apply Sheet:**
- Customers with approved changes
- Can be reviewed before applying

**Usage:**
1. Review each customer's data
2. Check governance rules applied
3. Approve or modify recommended K-factors
4. Manually update in Ignite if needed

### Configuration

**Governance Rules** (in `src/config.py`):
- `MAX_INCREASE`: 15% maximum increase cap
- `MAX_DECREASE`: 30% maximum decrease cap
- `CAP_PCT`: ±25% overall variance boundary
- `CONFIDENCE_THRESHOLD`: 80% minimum for auto-apply
- `MIN_INTERVALS`: 3 minimum intervals required
- `MIN_INTERVAL_DAYS`: 21 minimum days between deliveries

### Understanding Results

#### Status Categories:

**APPROVED**
- Customer meets all governance criteria
- High confidence score (>80%)
- Ready for automatic application
- File: `Apply_K_ThisWeek.csv`

**CAPPED_INCREASE**
- Proposed increase exceeded maximum (15%)
- Capped at maximum increase limit
- Review recommended

**CAPPED_DECREASE**
- Proposed decrease exceeded maximum (30%)
- Capped at maximum decrease limit
- Review recommended

**CAPPED_VARIANCE**
- Proposed K-factor exceeded ±25% variance boundary
- Capped at variance boundary
- Review required

**LOW_CONFIDENCE**
- Insufficient data quality
- Confidence score below 80%
- Manual review required

**INSUFFICIENT_DATA**
- Less than 3 valid delivery intervals
- Cannot calculate reliable K-factor
- Manual review required

---

## Customer Analysis Tool

### Overview

The Customer Analysis Tool is a specialized GUI for investigating individual customer K-factor calculations. It provides a detailed, step-by-step trace of the calculation logic.

### Quick Start

1. **Navigate to:** `tools/analysis_tools/` folder
2. **Run:** `python customer_analysis_gui.py`
3. **Enter customer number** in the input field
4. **Click "Analyze"**
5. **Review results** in the Summary and Detailed Output tabs

### When to Use This Tool

**Use Cases:**
- ✅ **Troubleshooting:** Why did a customer get a specific result?
- ✅ **Validation:** Verify the calculation logic is working correctly
- ✅ **Training:** Understand how K-factors are calculated
- ✅ **Auditing:** Review governance rules application
- ✅ **Customer Questions:** Explain to customers why their K-factor changed
- ✅ **Data Quality:** Identify issues with specific customer data

**Who Should Use It:**
- **Supervisors:** Investigating customer complaints or issues
- **IT Staff:** Troubleshooting calculation problems
- **Management:** Understanding system behavior
- **QA Teams:** Validating system accuracy

### Interface Overview

```
┌────────────────────────────────────────────┐
│  FoxFuel K-Factor Customer Analysis        │
├────────────────────────────────────────────┤
│  Customer Number: [_________] [Analyze]   │
├────────────────────────────────────────────┤
│  [Summary Tab]  [Detailed Output Tab]     │
│                                            │
│  ┌────────────────────────────────────┐   │
│  │ Analysis Results Display           │   │
│  │                                    │   │
│  └────────────────────────────────────┘   │
├────────────────────────────────────────────┤
│  Status: Ready...                         │
└────────────────────────────────────────────┘
```

### Analysis Output

#### Summary Tab
Provides a condensed overview:
- Customer Information (K-factors, tank size)
- Delivery Intervals (count, statistics)
- K-Factor Calculation (interval factors, weighted)
- Governance Rules Applied (limits, boundaries)
- Final Result (proposed K, variance, status, reasoning)

#### Detailed Output Tab
Comprehensive trace of calculation steps:
- Data loading and validation
- Complete interval details
- Interval filtering results
- K-factor calculation formulas
- Governance rule application
- Final proposed values

### Example Analysis

```
CUSTOMER INFORMATION
Current Winter K-Factor: 6.5700
Current Summer K-Factor: 4.8900
Usable Tank Size: 247 gallons

DELIVERY INTERVALS
Total Intervals Found: 2
Valid Intervals: 2

Interval 1: 2022-09-12 to 2022-12-20
  Days: 99
  Gallons Used: 228.1
  Degree Days: 1556.0

Interval 2: 2022-12-20 to 2023-10-18
  Days: 301
  Gallons Used: 422.8
  Degree Days: 2959.0

K-FACTOR CALCULATION
Interval K-Factors: 0.1466, 0.1429
Weighted K-Factor: 0.1442
Variance from Current: -97.8%

GOVERNANCE RULES APPLIED
Maximum Increase: 15% per week
Maximum Decrease: 30% per week
Variance Cap: ±25%

FINAL RESULT
Status: CAPPED_LOWER_BOUND
Proposed K-Factor: 4.9275
Final Variance: -25.0%
Reason: Capped at variance boundary (-25%)
```

---

## Build Tools

### Overview

Build Tools create standalone executables and deployment packages that don't require Python installation.

### Quick Start

**Build Main GUI Executable:**
1. **Navigate to:** `tools/build_tools/` folder
2. **Run:** `python build_gui_exe.py`
3. **Wait for completion** (2-5 minutes)
4. **Find executable** in `dist/` folder

**Build Customer Analysis Tool:**
1. **Navigate to:** `tools/build_tools/` folder
2. **Run:** `python build_analysis_exe.py`
3. **Wait for completion**
4. **Find executable** in `dist/` folder

**Create Deployment Package:**
1. **Navigate to:** `tools/build_tools/` folder
2. **Run:** `python create_deployment_package.py`
3. **Wait for completion**
4. **Find package** in main directory

### Prerequisites

**Required Software:**
- Python 3.8+ installed
- PyInstaller: `pip install pyinstaller`
- All dependencies: `pip install -r requirements.txt`

**Disk Space:**
- At least 2 GB free space (for build process)
- Executable files are ~300-320 MB each

### Build Outputs

**Main GUI Executable (`build_gui_exe.py`):**
- Output: `dist/FoxFuel_KFactor_Optimizer.exe` (~320 MB)
- Self-contained, no Python required
- Includes all dependencies

**Customer Analysis Tool (`build_analysis_exe.py`):**
- Output: `dist/FoxFuel_KFactor_Analysis_Tool.exe` (~300 MB)
- Self-contained analysis GUI
- Customer investigation tool

**Deployment Package (`create_deployment_package.py`):**
- Output: `FoxFuel_KFactor_Optimizer_Deployment_YYYYMMDD_HHMMSS.zip`
- Contains executable, documentation, installer
- Ready for staff deployment

### Deployment Package Contents

```
FoxFuel_KFactor_Optimizer_Deployment/
├── FoxFuel_KFactor_Optimizer.exe
├── INSTALL.bat
├── RUN_GUI.bat
├── FoxFuel_KFactor_User_Guide.md
├── INSTALLATION_GUIDE.md
├── README.md
├── data/
│   ├── inputs/
│   └── outputs/
```

---

## Deployment Tools

### Overview

Deployment Tools install and distribute the FoxFuel K-Factor Optimizer to staff computers. They provide automated installation, shortcuts, and documentation.

### Quick Start

**For IT Staff (Installing on Multiple Computers):**

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

### Installation Process

**Step 1: Extract Package**
```
Right-click FoxFuel_KFactor_Optimizer_Deployment.zip
→ Extract All...
→ Choose destination
→ Click Extract
```

**Step 2: Run Installer**
```
Navigate to extracted folder
Right-click INSTALL.bat
→ Run as administrator
→ Press Enter when prompted
```

**Step 3: Verify Installation**
```
✓ Desktop shortcut created
✓ Installation directory created
✓ Folder structure in place
✓ Executable file present
```

**Step 4: Initial Setup**
```
✓ Place CSV files in: data/inputs/
✓ CSV files: 03_*.csv, 04_*.csv, 06_*.csv
✓ Ready to run application
```

### Desktop Shortcut

**Creating Shortcut Automatically:**
- Run `INSTALL.bat` → Shortcut created automatically

**Manually Creating Shortcut:**
```
1. Right-click desktop
2. New → Shortcut
3. Browse to executable
4. Name: "FoxFuel K-Factor Optimizer"
5. Click Finish
```

---

## Understanding the System

### How K-Factors Work

**K-Factor Formula:**
```
K = Gallons Used / Degree Days
```

- **Higher K** = More fuel per degree day (higher consumption)
- **Lower K** = Less fuel per degree day (lower consumption)

### Calculation Process

1. **Clean Delivery Tickets** - Validate and filter delivery data
2. **Build Intervals** - Create intervals between full fills
3. **Filter Valid Intervals** - Apply minimum day/gallon rules
4. **Calculate Interval K** - K = Gallons / Degree Days
5. **Weighted K by Customer** - Gallons-weighted average
6. **Apply Governance** - Cap increases/decreases
7. **Generate Output Files** - CSV for import, Excel for review

### Governance Rules Explained

**Maximum Increase: 15%**
- Prevents sudden dramatic increases
- Protects customer satisfaction
- Conservative for heating oil

**Maximum Decrease: 30%**
- Allows larger decreases than increases
- Account for efficiency improvements
- Still conservative overall

**Variance Cap: ±25%**
- Overall boundary on changes
- Prevents extreme values
- Balances flexibility with safety

**Confidence Threshold: 80%**
- Minimum data quality requirement
- Ensures reliable calculations
- Flags uncertain results

### Seasonal Adjustments

- **Winter K-factor:** Primary heating season
- **Summer K-factor:** Reduced consumption period
- **Summer multiplier:** 1.2x adjustment factor
- **Degree day calculation:** Uses heating degree days

---

## Troubleshooting

### Common Issues

#### "No CSV files found"
**Problem:** CSV files not detected

**Solution:**
- Ensure files are in `data/inputs/` folder
- Check file naming: `03_*.csv`, `04_*.csv`, `06_*.csv`
- Verify files exist

#### "Missing required columns"
**Problem:** CSV headers don't match expected format

**Solution:**
- Verify CSV files are from Ignite exports
- Check for typos in column names
- Ensure files weren't modified

#### "Permission denied" when saving Excel
**Problem:** Output file is locked

**Solution:**
- Close any open Excel files
- System will create timestamped backup
- Try running again

#### "No valid intervals found"
**Problem:** Insufficient delivery data

**Solution:**
- Verify delivery tickets exist for customers
- Check date ranges in DeliveryTickets.csv
- Ensure degree day data covers delivery periods

#### "PyInstaller not found"
**Problem:** PyInstaller not installed

**Solution:** `pip install pyinstaller`

#### "Installation failed"
**Problem:** Installation issues

**Solution:**
- Check administrator privileges
- Verify disk space (500 MB minimum)
- Review error messages

### Getting Help

**For Technical Issues:**
1. Check console output for error messages
2. Review K_Review_Queue.xlsx for data quality issues
3. Verify input CSV files match expected format
4. Consult specific tool guides

**Contact Points:**
- **IT Support:** For technical problems
- **Supervisor:** For business rule questions
- **Developer:** For bug reports

---

## Best Practices

### Running the Optimizer

1. **Regular Runs:** Update K-factors weekly for best results
2. **Data Quality:** Ensure Ignite CSV exports are complete and current
3. **Review Queue:** Always review K_Review_Queue.xlsx before applying
4. **Backup:** Keep previous week's results for reference
5. **Validation:** Spot-check some customers to verify calculations

### Weekly Process

1. **Export:** Get latest CSVs from Ignite on Friday
2. **Process:** Run K-Factor Optimizer
3. **Review:** Check K_Review_Queue.xlsx
4. **Approve:** Review and modify as needed
5. **Import:** Import Apply_K_ThisWeek.csv into Ignite
6. **Monitor:** Track results and customer feedback

### Data Management

1. **Archives:** Keep historical CSV files
2. **Results:** Back up output files
3. **Logs:** Save console output for troubleshooting
4. **Documentation:** Note any manual overrides
5. **Updates:** Track which version is deployed

### Quality Control

1. **Spot Checks:** Randomly verify some customers
2. **Trend Analysis:** Watch for pattern changes
3. **Customer Feedback:** Monitor run-out incidents
4. **Data Validation:** Check for anomalies
5. **Audit Trail:** Keep records of changes

---

## Quick Reference

### File Locations

| Need | File Location |
|------|---------------|
| **Main Optimizer** | `tools/main_app/gui_runner.py` |
| **Analysis Tool** | `tools/analysis_tools/customer_analysis_gui.py` |
| **Build Executable** | `tools/build_tools/build_gui_exe.py` |
| **Deployment Installer** | `tools/deployment/INSTALL.bat` |
| **User Guide** | `FoxFuel_KFactor_User_Guide.md` (this file) |

### Common Commands

**Run Main Optimizer:**
```bash
cd tools/main_app
python gui_runner.py
```

**Run Analysis Tool:**
```bash
cd tools/analysis_tools
python customer_analysis_gui.py
```

**Build Executable:**
```bash
cd tools/build_tools
python build_gui_exe.py
```

**Batch File Launcher:**
```
Double-click RUN_KFACTOR.bat
```

### Input/Output Files

**Input Files (in `data/inputs/`):**
- `03_CustomerFuel.csv` - Customer information
- `04_DeliveryTickets.csv` - Delivery history
- `06_DegreeDayValues.csv` - Degree day data

**Output Files (in `data/outputs/`):**
- `Apply_K_ThisWeek.csv` - Auto-apply customers
- `K_Review_Queue.xlsx` - Review queue

### Status Codes

| Status | Meaning | Action Required |
|--------|---------|-----------------|
| APPROVED | Ready to apply | Automatic |
| CAPPED_INCREASE | Limited by max increase | Review |
| CAPPED_DECREASE | Limited by max decrease | Review |
| CAPPED_VARIANCE | Limited by variance cap | Review |
| LOW_CONFIDENCE | Insufficient data quality | Manual review |
| INSUFFICIENT_DATA | Not enough intervals | Manual review |

### Configuration Values

| Parameter | Value | Purpose |
|-----------|-------|---------|
| MAX_INCREASE | 15% | Maximum weekly increase |
| MAX_DECREASE | 30% | Maximum weekly decrease |
| CAP_PCT | ±25% | Overall variance boundary |
| CONFIDENCE_THRESHOLD | 80% | Minimum confidence |
| MIN_INTERVALS | 3 | Minimum intervals required |
| MIN_INTERVAL_DAYS | 21 | Minimum days between deliveries |

---

## Resources

### Documentation

- **This Guide:** Complete user manual
- **GitHub Repository:** [FoxFuel_KFactor_Optimizer](https://github.com/dynamix77/FoxFuel_KFactor_Optimizer)
- **README:** `README.md` - Project overview
- **Tools READMEs:** Individual tool guides in `tools/` subfolders

### Support

**For Issues:**
1. Check this troubleshooting section
2. Review specific tool documentation
3. Consult K_Review_Queue.xlsx for data issues
4. Contact appropriate support

### Version

**Current Version:** 1.0  
**Last Updated:** October 2025  
**System:** FoxFuel K-Factor Optimizer

---

*End of User Guide*
