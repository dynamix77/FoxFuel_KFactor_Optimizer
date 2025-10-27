# User Guide: Customer Analysis Tool

## Overview

The Customer Analysis Tool is a specialized GUI application for investigating individual customer K-factor calculations. It provides detailed, step-by-step trace of the calculation logic for any customer.

## 🎯 **Quick Start**

1. **Navigate to:** `tools/analysis_tools/` folder
2. **Run:** `python customer_analysis_gui.py`
3. **Enter customer number** in the input field
4. **Click "Analyze"**
5. **Review results** in the Summary and Detailed Output tabs

## 📋 **When to Use This Tool**

### **Use Cases:**
- ✅ **Troubleshooting:** Why did a customer get a specific result?
- ✅ **Validation:** Verify the calculation logic is working correctly
- ✅ **Training:** Understand how K-factors are calculated
- ✅ **Auditing:** Review governance rules application
- ✅ **Customer Questions:** Explain to customers why their K-factor changed
- ✅ **Data Quality:** Identify issues with specific customer data

### **Who Should Use It:**
- **Supervisors:** Investigating customer complaints or issues
- **IT Staff:** Troubleshooting calculation problems
- **Management:** Understanding system behavior
- **QA Teams:** Validating system accuracy

## 🖥️ **Interface Overview**

### **Main Window:**
```
┌────────────────────────────────────────────┐
│  FoxFuel K-Factor Customer Analysis         │
├────────────────────────────────────────────┤
│  Customer Number: [_________] [Analyze]   │
├────────────────────────────────────────────┤
│  [Summary Tab]  [Detailed Output Tab]     │
│                                            │
│  ┌────────────────────────────────────┐   │
│  │ Analysis Results Display           │   │
│  │                                    │   │
│  │                                    │   │
│  └────────────────────────────────────┘   │
├────────────────────────────────────────────┤
│  Status: Ready. Enter customer number...   │
└────────────────────────────────────────────┘
```

## 📊 **Analysis Output**

### **Summary Tab:**
Provides a condensed overview of the analysis:

#### **CUSTOMER INFORMATION**
- Current Winter K-factor
- Current Summer K-factor
- Usable tank size (gallons)

#### **DELIVERY INTERVALS**
- Total intervals found
- Valid intervals (passing filters)
- Key interval statistics

#### **K-FACTOR CALCULATION**
- Individual interval K-factors
- Weighted K-factor calculation
- Variance from current K-factor

#### **GOVERNANCE RULES APPLIED**
- Maximum increase/decrease limits
- Variance boundaries
- Confidence thresholds

#### **FINAL RESULT**
- Proposed K-factor
- Final variance percentage
- Status (APPROVED, CAPPED, etc.)
- Reasoning

### **Detailed Output Tab:**
Comprehensive trace of all calculation steps:

#### **Data Loading:**
- Files found and loaded
- Record counts
- Data validation results

#### **Interval Building:**
- Complete interval details for each delivery period
- Start and end dates
- Days in interval
- Gallons used
- Degree days used
- Full fill detection

#### **Interval Filtering:**
- Which intervals passed validation
- Which intervals were filtered out
- Reasons for filtering

#### **K-Factor Calculation:**
- K-factor formula for each interval: `K = Gallons / Degree Days`
- Individual interval K-factors
- Weighted calculation details

#### **Governance Application:**
- Which rules were triggered
- How limits were applied
- Final proposed value
- Reasoning for the result

## 🔍 **Interpreting Results**

### **Scenario 1: Customer Gets APPROVED Status**

**What it means:**
- Customer has sufficient data quality
- Proposed K-factor is within governance limits
- High confidence in the calculation
- Ready for automatic application

**Action:**
- Include in Apply_K_ThisWeek.csv
- Automatic import into Ignite

### **Scenario 2: Customer Gets CAPPED Status**

**What it means:**
- Proposed change exceeded a governance limit
- System applied safety cap
- Actual variance is higher than proposed
- May require manual review

**Action:**
- Review in K_Review_Queue.xlsx
- Consider if cap is appropriate
- May need manual adjustment

### **Scenario 3: Customer Gets LOW_CONFIDENCE Status**

**What it means:**
- Insufficient data quality
- Fewer than 3 valid intervals
- Calculated K-factor may be unreliable
- Requires human judgment

**Action:**
- Review delivery history
- Check for data quality issues
- Manual override may be needed

## 📈 **Example Analysis Output**

### **Sample Customer: 1000000**

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

### **Analysis Explanation:**
1. **High Variance:** The calculated K-factor is much lower than current
2. **Governance Applied:** System capped at -25% maximum variance
3. **Conservative Approach:** Prevents drastic changes
4. **Action Required:** Review if this customer's consumption pattern is legitimate

## 🐛 **Troubleshooting**

### **"Customer not found"**
- **Problem:** Customer number doesn't exist in data
- **Solution:**
  - Verify customer number is correct
  - Check CustomerFuel.csv contains the customer
  - Ensure CSV files are loaded

### **"No delivery intervals found"**
- **Problem:** Customer has no delivery history
- **Solution:**
  - Verify customer has deliveries in DeliveryTickets.csv
  - Check date ranges
  - Customer may be new

### **"No valid intervals"**
- **Problem:** Intervals don't meet minimum requirements
- **Solution:**
  - Check minimum days requirement (21 days)
  - Verify degree day data covers period
  - Customer may need more delivery history

### **Analysis shows incorrect results**
- **Problem:** Calculation seems wrong
- **Solution:**
  - Check Detailed Output tab for specifics
  - Verify data quality in source CSVs
  - Review governance rules
  - Contact IT support

## 💡 **Best Practices**

1. **Start with Summary:** Get overview first
2. **Dive into Details:** Use Detailed Output for specifics
3. **Check Intervals:** Verify delivery history is correct
4. **Validate Governance:** Ensure rules were applied correctly
5. **Document Findings:** Keep notes for future reference

## 🔗 **Related Tools**

- **Main Optimizer:** `tools/main_app/` - Run full optimization
- **Build Tools:** `tools/build_tools/` - Create executable
- **Documentation:** `tools/documentation/` - User guides

## 📞 **Support**

For issues with analysis tool:
1. Check console output for errors
2. Verify customer number is correct
3. Ensure all CSV files are in `data/inputs/`
4. Check source data quality in CustomerFuel.csv

---

**Last Updated:** October 2025  
**Version:** 1.0
