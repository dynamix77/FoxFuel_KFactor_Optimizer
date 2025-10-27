# User Guide: Main K-Factor Optimizer Application

## Overview

The Main K-Factor Optimizer is the core application for optimizing customer K-factors. It provides three deployment options ranging from simple batch file execution to a graphical user interface.

## 🎯 **Quick Start**

### **Option 1: GUI Application (Recommended)**

1. **Navigate to:** `tools/main_app/` folder
2. **Run:** `python gui_runner.py`
3. **Click "Auto-Detect Files"** to find your CSV files
4. **Click "Run K-Factor Optimizer"** to start
5. **Review results** using the buttons in the GUI

### **Option 2: Batch File (Simplest)**

1. **Navigate to:** `tools/main_app/` folder
2. **Double-click:** `RUN_KFACTOR.bat`
3. Wait for completion message
4. Check `data/outputs/` folder for results

### **Option 3: Command Line**

1. **Navigate to:** `tools/main_app/` folder
2. **Run:** `python run_local.py`
3. View console output for progress
4. Results appear in `data/outputs/` folder

## 📋 **Prerequisites**

### **Required Files:**
Place these CSV files in `data/inputs/` folder:
- `03_CustomerFuel.csv` - Customer fuel information
- `04_DeliveryTickets.csv` - Delivery transaction history
- `06_DegreeDayValues.csv` - Degree day reference data

### **System Requirements:**
- **Python 3.8+** (for Option 2 & 3)
- **Windows 10+** (for all options)
- **Required packages:** `pip install -r requirements.txt` (one-time setup)

## 🎨 **GUI Application Features**

### **Main Window:**
- **Auto-Detect Files Button:** Finds your CSV files automatically
- **Run K-Factor Optimizer Button:** Starts the optimization process
- **Open Apply_K_ThisWeek.csv Button:** Opens the auto-apply file
- **Open K_Review_Queue.xlsx Button:** Opens the review queue file
- **Open Output Folder Button:** Opens the output directory

### **Progress Indicators:**
- Loading bar shows processing progress
- Status messages display current step
- Success/error messages at completion

### **Results Display:**
- Summary statistics
- Number of customers processed
- Number flagged for review
- Processing time

## ⚙️ **Configuration**

### **Governance Rules** (in `src/config.py`):
- `MAX_INCREASE`: 15% maximum increase cap
- `MAX_DECREASE`: 30% maximum decrease cap
- `CAP_PCT`: ±25% overall variance boundary
- `CONFIDENCE_THRESHOLD`: 80% minimum for auto-apply
- `MIN_INTERVALS`: 3 minimum intervals required
- `MIN_INTERVAL_DAYS`: 21 minimum days between deliveries

### **Customization:**
Edit `src/config.py` to adjust governance rules based on your business needs.

## 📊 **Output Files**

### **Apply_K_ThisWeek.csv**
**Purpose:** Customers ready for automatic K-factor import into Ignite

**Contents:**
- Customer Number
- K Factor - Winter (proposed)
- Confidence score
- Status

**Usage:**
1. Review file for accuracy
2. Import into Ignite using data import function
3. Customer K-factors updated automatically

### **K_Review_Queue.xlsx**
**Purpose:** Customers requiring manual review

**Contains Two Sheets:**

#### **Review Sheet:**
- Current Winter K-factor
- Calculated K-factor
- Proposed K-factor
- Variance percentage
- Status and reason
- Confidence level
- Interval count
- Total gallons and degree days

#### **Auto-Apply Sheet:**
- Customers with approved changes
- Can be reviewed before applying

**Usage:**
1. Review each customer's data
2. Check governance rules applied
3. Approve or modify recommended K-factors
4. Manually update in Ignite if needed

## 🔍 **Understanding Results**

### **Status Categories:**

#### **APPROVED**
- Customer meets all governance criteria
- High confidence score (>80%)
- Ready for automatic application
- File: `Apply_K_ThisWeek.csv`

#### **CAPPED_INCREASE**
- Proposed increase exceeded maximum (15%)
- Capped at maximum increase limit
- Review recommended

#### **CAPPED_DECREASE**
- Proposed decrease exceeded maximum (30%)
- Capped at maximum decrease limit
- Review recommended

#### **CAPPED_VARIANCE**
- Proposed K-factor exceeded ±25% variance boundary
- Capped at variance boundary
- Review required

#### **LOW_CONFIDENCE**
- Insufficient data quality
- Confidence score below 80%
- Manual review required

#### **INSUFFICIENT_DATA**
- Less than 3 valid delivery intervals
- Cannot calculate reliable K-factor
- Manual review required

## 🐛 **Troubleshooting**

### **"No CSV files found"**
- **Problem:** CSV files not detected
- **Solution:** 
  - Ensure files are in `data/inputs/` folder
  - Check file naming: `03_*.csv`, `04_*.csv`, `06_*.csv`
  - Verify files exist

### **"Missing required columns"**
- **Problem:** CSV headers don't match expected format
- **Solution:**
  - Verify CSV files are from Ignite exports
  - Check for typos in column names
  - Ensure files weren't modified

### **"Permission denied" error when saving Excel**
- **Problem:** Output file is locked
- **Solution:**
  - Close any open Excel files
  - System will create timestamped backup
  - Try running again

### **"No valid intervals found"**
- **Problem:** Insufficient delivery data
- **Solution:**
  - Verify delivery tickets exist for customers
  - Check date ranges in DeliveryTickets.csv
  - Ensure degree day data covers delivery periods

## 📈 **Best Practices**

1. **Regular Runs:** Update K-factors weekly for best results
2. **Data Quality:** Ensure Ignite CSV exports are complete and current
3. **Review Queue:** Always review K_Review_Queue.xlsx before applying
4. **Backup:** Keep previous week's results for reference
5. **Validation:** Spot-check some customers to verify calculations

## 💡 **Tips**

- Run on Fridays to apply changes for the following week
- Review high-variance customers carefully
- Use the customer analysis tool for detailed investigation
- Keep a log of manual overrides for reference
- Track customer run-out incidents to refine governance rules

## 🔗 **Related Tools**

- **Customer Analysis Tool:** `tools/analysis_tools/` - Detailed customer investigation
- **Build Tools:** `tools/build_tools/` - Create standalone executables
- **Deployment Tools:** `tools/deployment/` - Installation and setup

## 📞 **Support**

For technical issues:
1. Check console output for error messages
2. Review K_Review_Queue.xlsx for data quality issues
3. Verify input CSV files match expected format
4. Check the log files in the console output

---

**Last Updated:** October 2025  
**Version:** 1.0
