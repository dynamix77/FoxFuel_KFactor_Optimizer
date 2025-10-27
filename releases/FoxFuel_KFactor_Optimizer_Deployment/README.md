# FoxFuel K-Factor Optimizer

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Windows](https://img.shields.io/badge/Platform-Windows-lightgrey.svg)](https://windows.com)

A Python-based system for optimizing heating oil delivery K-factors using Ignite CSV exports. This tool replicates and enhances the original Excel Power Query + VBA system with modern Python processing, providing three deployment options for maximum flexibility.

## 🚀 Features

- **One-Click Operation** - Three deployment options from simple batch file to standalone executable
- **Automatic File Detection** - Finds latest CSV files automatically
- **Governance Rules** - Built-in safety limits to prevent dangerous K-factor changes
- **Multiple Output Formats** - CSV for Ignite import, Excel for manual review
- **Comprehensive Logging** - Detailed processing logs for troubleshooting
- **GUI Interface** - User-friendly interface with progress feedback

## Quick Start

### Option 1: Standalone GUI Executable (Recommended for Staff)
1. **Download** `FoxFuel_KFactor_Optimizer.exe` (320 MB)
2. **Create** `data/inputs/` folder next to the executable
3. **Place CSV files** in `data/inputs/` folder:
   - `03_CustomerFuel.csv`
   - `04_DeliveryTickets.csv` 
   - `06_DegreeDayValues.csv`
4. **Double-click** `FoxFuel_KFactor_Optimizer.exe`
5. **Click "Run K-Factor Optimizer"** in the GUI
6. **Review results** in the generated files

> ✅ **No Python installation required!** Perfect for staff computers.

### Option 2: Batch File (Simple)
1. Double-click `RUN_KFACTOR.bat`
2. Wait for completion
3. Check `data/outputs/` for results

### Option 3: GUI Application (Developer)
1. Run `python gui_runner.py`
2. Use the graphical interface
3. Review results in the GUI
4. Click buttons to open output files

## Input Files Required

Place these CSV files in `data/inputs/`:

- **03_CustomerFuel.csv** - Customer fuel information
- **04_DeliveryTickets.csv** - Delivery transaction history  
- **06_DegreeDayValues.csv** - Degree day reference data

The system automatically finds the newest files matching these patterns.

## Output Files Generated

- **Apply_K_ThisWeek.csv** - Import this into Ignite
- **K_Review_Queue.xlsx** - Review flagged customers manually

## Installation

### For Python Users
```bash
pip install -r requirements.txt
```

### For Non-Python Users
Use the standalone executable created by `build_exe.py` - no Python installation needed.

## Testing

Test data is included in `data/inputs/` with 5 sample customers demonstrating:
- Normal customers (auto-apply eligible)
- High variance customer (needs review)
- Low confidence customer (insufficient data)

Run the tool with test data to verify everything works.

## Configuration

Governance parameters are in `src/config.py`:

- `MAX_INCREASE = 10%` - Maximum K-factor increase
- `MAX_DECREASE = 50%` - Maximum K-factor decrease  
- `CONFIDENCE_THRESHOLD = 0.85` - Minimum confidence for auto-apply
- `MIN_INTERVALS = 3` - Minimum intervals per customer

## Troubleshooting

### Common Issues

**"No CSV files found"**
- Ensure files are named `03_*.csv`, `04_*.csv`, `06_*.csv`
- Check files are in `data/inputs/` folder

**"Missing required columns"**
- Verify CSV files have correct headers
- Check for blank Column A (will be ignored)

**"No valid intervals found"**
- Ensure delivery tickets have valid dates and quantities
- Check degree day data covers delivery periods

### Getting Help

1. Check the console output for specific error messages
2. Review `K_Review_Queue.xlsx` for data quality issues
3. Verify input CSV files match expected format

## File Structure

```
FoxFuel_KFactor_Optimizer/
├── src/                          # Core Python modules
│   ├── config.py                 # Configuration parameters
│   ├── data_loader.py           # CSV loading and validation
│   ├── interval_builder.py      # Delivery interval creation
│   ├── kfactor_calculator.py    # K-factor calculations
│   ├── governance.py            # Governance rules application
│   ├── outputs_writer.py        # Output file generation
│   └── pipeline.py              # Main orchestration
├── data/
│   ├── inputs/                  # Place CSV files here
│   └── outputs/                # Results appear here
├── run_local.py                 # Main Python script
├── RUN_KFACTOR.bat             # One-click batch file
├── build_exe.py                # Executable builder
├── gui_runner.py               # GUI interface
└── requirements.txt            # Python dependencies
```

## Business Logic

The system follows the 8-step Ignite K-Factor workflow:

1. **Clean Delivery Tickets** - Validate and filter delivery data
2. **Build Intervals** - Create intervals between full fills
3. **Filter Valid Intervals** - Apply minimum day/gallon rules
4. **Calculate Interval K** - K = Gallons / Degree Days Used
5. **Weighted K by Customer** - Gallons-weighted average per customer
6. **Apply Governance** - Cap increases/decreases, filter unreliable values
7. **Apply K This Week** - Generate Ignite import file
8. **K Review Queue** - Generate Excel review report

## Support

This tool is designed for Fox Fuel, Inc. internal use. For technical issues, check the console output and Excel review file for detailed error information.
