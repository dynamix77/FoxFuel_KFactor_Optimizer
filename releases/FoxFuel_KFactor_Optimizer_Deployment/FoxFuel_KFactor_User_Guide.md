# FoxFuel K-Factor Optimizer - User Guide

## Overview

The FoxFuel K-Factor Optimizer is a data processing tool that analyzes your heating oil delivery patterns and automatically calculates optimized K-factors for your customers. The system processes three CSV exports from Ignite and generates two output files:

- **Apply_K_ThisWeek.csv** - Customers ready for automatic K-factor updates
- **K_Review_Queue.xlsx** - Customers requiring manual review

## Quick Start

### Option 1: Standalone GUI Executable (Recommended for Staff)
1. **Download** `FoxFuel_KFactor_Optimizer.exe` (320 MB)
2. **Create** a `data/inputs/` folder next to the executable
3. **Place your CSV files** in the `data/inputs/` folder
4. **Double-click** `FoxFuel_KFactor_Optimizer.exe`
5. **Click "Auto-Detect Files"** to find your CSV files
6. **Click "Run K-Factor Optimizer"** to start the process
7. **Review results** using the buttons in the GUI

> ✅ **No Python installation required!** Perfect for staff computers.

### Option 2: Double-Click Batch File (Simple)
1. Place your Ignite CSV exports in the `data/inputs/` folder
2. Double-click `RUN_KFACTOR.bat`
3. Wait for completion message
4. Check `data/outputs/` folder for results

### Option 3: GUI Application (Developer)
1. **Install Python** (3.8 or higher)
2. **Install dependencies**: `pip install -r requirements.txt`
3. **Run**: `python gui_runner.py`
4. **Use the graphical interface** to run optimization

---

## Detailed Instructions

### Prerequisites

**For Option 1 (Standalone GUI Executable):**
- No prerequisites - works on any Windows computer
- Just download and run!

**For Option 2 (Batch File):**
- Python 3.8+ installed on your computer
- Required packages installed (run `pip install -r requirements.txt` once)

**For Option 3 (GUI Application):**
- Same as Option 2, or use the executable version

### Input Data Requirements

The system requires three CSV files exported from Ignite:

1. **Customer Fuel Data** (`03_*.csv`)
   - Must contain columns: Customer Number, Usable Size, K Factor, Zone - Fuel, Automatic Delivery, K Factor - Winter, K Factor - Summer, K Factor - Spring, K Factor - Fall

2. **Delivery Tickets** (`04_*.csv`)
   - Must contain columns: Customer Number, Transaction Date, Transaction Type, Quantity, % Full, PIDCustomerFuel1

3. **Degree Day Values** (`06_*.csv`)
   - Must contain columns: DDay Area, DDay Date, Heat Only DDays

### File Setup

1. **Create the input folder:**
   ```
   FoxFuel_KFactor_Optimizer/
   └── data/
       └── inputs/
           ├── 03_CustomerFuel.csv
           ├── 04_DeliveryTickets.csv
           └── 06_DegreeDayValues.csv
   ```

2. **Export your data from Ignite:**
   - Use the standard Ignite export format
   - Ensure files are named with the `03_`, `04_`, `06_` prefixes
   - Place all three files in the `data/inputs/` folder

3. **The system will automatically:**
   - Find the latest files matching the naming patterns
   - Process all valid delivery records
   - Calculate optimized K-factors
   - Apply governance rules for safety

---

## Understanding the Results

### Apply_K_ThisWeek.csv

This file contains customers whose K-factors can be automatically updated in Ignite:

**Columns:**
- `Customer Number` - Customer identifier
- `K Factor - Winter` - New optimized winter K-factor

**When to use:**
- Import directly into Ignite for customers with high confidence scores
- Only customers meeting strict governance criteria appear here

### K_Review_Queue.xlsx

This Excel file contains customers requiring manual review before applying changes:

**Sheets:**
1. **Review Queue** - Main data with all analysis details
2. **Auto-Apply** - Summary of customers ready for automatic updates

**Key Columns:**
- `Customer Number` - Customer identifier
- `Current Winter K Factor` - Current K-factor in Ignite
- `Calculated K` - System-calculated optimal K-factor
- `Proposed K` - Final recommended K-factor (after governance)
- `Variance %` - Percentage change from current to proposed
- `Status` - Why the customer needs review
- `Confidence` - Statistical confidence in the calculation
- `Intervals` - Number of delivery intervals analyzed
- `Total Gallons` - Total fuel delivered in analysis period
- `Total Degree Days` - Heating degree days in analysis period

**Status Meanings:**
- `HIGH_VARIANCE` - Proposed change exceeds safe limits
- `LOW_CONFIDENCE` - Insufficient data for reliable calculation
- `INSUFFICIENT_DATA` - Too few delivery intervals to analyze
- `APPROVED` - Ready for automatic application
- `CAPPED_LOWER_BOUND` - Governed to minimum safe decrease
- `CAPPED_UPPER_BOUND` - Governed to maximum safe increase

---

## Governance Rules

The system applies several safety rules to prevent dangerous K-factor changes:

### Maximum Change Limits (Heating Oil Industry Standards)
- **Maximum Increase:** 15% per week (conservative for heating oil)
- **Maximum Decrease:** 30% per week (conservative for heating oil)
- **Overall Variance Cap:** ±25% from current Winter K-factor

### Data Quality Requirements
- **Minimum Intervals:** 21 days between deliveries
- **Confidence Threshold:** 80% for automatic application (realistic for heating oil)
- **Full Fill Detection:** 90% of tank capacity

### Seasonal Adjustments (Winter/Summer Focus)
- **Summer Multiplier:** 1.2x (accounts for reduced heating needs in summer)
- **Primary Season:** Winter K-factor (main heating season)
- **Secondary Season:** Summer K-factor (reduced consumption period)
- **Degree Day Calculation:** Uses heating degree days for consumption analysis

---

## Troubleshooting

### Common Issues

**"No valid intervals found"**
- Check that delivery tickets contain actual delivery records (not just estimates)
- Verify that % Full values are populated or that quantities are reasonable
- Ensure transaction dates are in correct format

**"Missing required columns"**
- Verify CSV files are exported from Ignite with correct column names
- Check that files are named with proper prefixes (03_, 04_, 06_)
- Ensure all required columns are present and spelled correctly

**"Pipeline failed with error"**
- Check the log output for specific error details
- Verify input files contain valid data (not empty or corrupted)
- Ensure Python dependencies are installed (for batch file option)

**"Permission denied" when writing Excel files**
- Close any open Excel files (K_Review_Queue.xlsx)
- The system will automatically create a timestamped backup file if the original is locked
- Check the outputs folder for files with timestamps (e.g., K_Review_Queue_20251026_183650.xlsx)

**"0 customers eligible for auto-apply"**
- This is normal - most customers require manual review for safety
- Check K_Review_Queue.xlsx for detailed analysis
- Review customers with HIGH_CONFIDENCE status for potential auto-apply

### Data Quality Tips

1. **Delivery Records:** Ensure delivery tickets contain actual deliveries, not estimates or service calls
2. **Date Formats:** Ignite exports should use standard date formats (MM/DD/YY or MM/DD/YYYY)
3. **Customer Matching:** Verify Customer Numbers match between all three files
4. **Tank Sizes:** Ensure Usable Size values are accurate for proper full-fill detection

---

## Advanced Usage

### Customizing Governance Parameters

Edit `src/config.py` to adjust safety limits:

```python
# Maximum change limits
MAX_INCREASE = 0.10  # 10% maximum increase per week
MAX_DECREASE = 0.50  # 50% maximum decrease per week
CAP_PCT = 0.20       # 20% overall variance cap

# Data quality thresholds
CONFIDENCE_THRESHOLD = 0.85  # 85% confidence for auto-apply
MIN_INTERVAL_DAYS = 21       # Minimum 21 days between deliveries
FULL_THRESHOLD = 0.90        # 90% of tank for "full fill"
```

### Building Standalone Executable

1. Install PyInstaller: `pip install pyinstaller`
2. Run: `python build_exe.py`
3. This creates `FoxFuel_KFactor.exe` (~30MB)
4. Distribute the .exe file to staff computers

### GUI Customization

The GUI version (`gui_runner.py`) can be customized:
- Modify progress messages
- Add additional status indicators
- Change window appearance
- Add file selection dialogs

---

## Best Practices

### Weekly Workflow

1. **Monday:** Export latest data from Ignite
2. **Tuesday:** Run K-Factor Optimizer
3. **Wednesday:** Review K_Review_Queue.xlsx
4. **Thursday:** Import approved changes to Ignite
5. **Friday:** Monitor delivery performance

### Data Management

- **Keep backups** of original Ignite exports
- **Archive results** from previous weeks for comparison
- **Document decisions** made during manual review
- **Track performance** of applied K-factor changes

### Safety Guidelines

- **Never skip manual review** for HIGH_VARIANCE customers
- **Verify tank sizes** before applying large changes
- **Monitor deliveries** closely after K-factor updates
- **Adjust governance rules** based on business experience

---

## Support and Maintenance

### Log Files

The system creates detailed logs showing:
- Data loading progress
- Interval building results
- K-factor calculations
- Governance rule applications
- Output file generation

### Performance Monitoring

Track these metrics weekly:
- Number of customers processed
- Percentage requiring manual review
- Average variance in proposed changes
- Delivery performance after K-factor updates

### System Updates

To update the system:
1. Replace Python files with new versions
2. Rebuild executable if using standalone version
3. Test with sample data before production use
4. Update governance parameters as needed

---

## Contact Information

For technical support or questions about the K-Factor Optimizer:
- Check the log files for detailed error information
- Verify input data format matches requirements
- Review governance parameters for your business needs
- Test with sample data before processing production files

---

*This guide covers all aspects of using the FoxFuel K-Factor Optimizer. For additional customization or advanced features, refer to the source code documentation in the `src/` folder.*
