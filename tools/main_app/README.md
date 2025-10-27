# Main Application Tools

This folder contains the core K-Factor Optimizer applications.

## Files:

### `gui_runner.py`
- **Purpose:** Main GUI application for running K-Factor optimization
- **Usage:** `python gui_runner.py`
- **Features:** 
  - Auto-detects CSV files
  - Progress feedback
  - Results display
  - File management buttons

### `run_local.py`
- **Purpose:** Command-line version of the K-Factor optimizer
- **Usage:** `python run_local.py`
- **Features:**
  - Console output
  - Detailed logging
  - Summary statistics

### `RUN_KFACTOR.bat`
- **Purpose:** Simple batch file launcher
- **Usage:** Double-click to run
- **Features:**
  - One-click execution
  - No Python knowledge required

## Quick Start:

1. **GUI Version (Recommended):** Double-click `RUN_KFACTOR.bat` or run `python gui_runner.py`
2. **Command Line:** Run `python run_local.py`
3. **Place CSV files** in `data/inputs/` folder
4. **Review results** in `data/outputs/` folder

## Requirements:
- Python 3.8+
- Required packages: `pip install -r requirements.txt`
- CSV files in `data/inputs/` folder
