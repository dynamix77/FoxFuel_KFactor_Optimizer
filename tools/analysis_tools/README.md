# Analysis Tools

This folder contains tools for analyzing individual customer K-factor calculations.

## Files:

### `customer_analysis_gui.py`
- **Purpose:** GUI tool to trace K-factor calculation logic for any customer
- **Usage:** `python customer_analysis_gui.py`
- **Features:**
  - Enter any customer number
  - Shows complete calculation trace
  - Displays delivery intervals
  - Shows governance rules applied
  - Explains final result reasoning

### `RUN_ANALYSIS.bat`
- **Purpose:** Quick launcher for the analysis tool
- **Usage:** Double-click to run

## What the Analysis Shows:

1. **Customer Information**
   - Current Winter/Summer K-factors
   - Tank size and configuration

2. **Delivery Intervals**
   - All intervals found for the customer
   - Start/end dates, days, gallons used, degree days
   - Which intervals passed validation

3. **K-Factor Calculation**
   - Individual interval K-factors
   - Weighted K-factor calculation
   - Variance from current K-factor

4. **Governance Rules**
   - Maximum increase/decrease limits
   - Variance boundaries
   - Confidence thresholds

5. **Final Result**
   - Proposed K-factor
   - Final variance percentage
   - Status and reasoning

## Example Usage:

1. Run `python customer_analysis_gui.py`
2. Enter customer number (e.g., `1000000`, `1000004`)
3. Click "Analyze"
4. Review results in the tabs

## Use Cases:

- **Troubleshooting:** Why did a customer get a specific result?
- **Validation:** Verify the calculation logic is working correctly
- **Training:** Understand how K-factors are calculated
- **Auditing:** Review governance rules application
