# Documentation

This folder contains comprehensive documentation for the FoxFuel K-Factor Optimizer.

## Files:

### `FoxFuel_KFactor_User_Guide.md`
- **Purpose:** Complete user manual for the K-Factor Optimizer
- **Contents:**
  - Overview and purpose
  - Installation instructions
  - Usage guide for all tools
  - Understanding results
  - Troubleshooting guide
  - Governance rules explanation
  - Seasonal adjustments

### `GitHub_Setup_Guide.md`
- **Purpose:** Instructions for setting up GitHub repository
- **Contents:**
  - Creating repository
  - Uploading files
  - Setting up releases
  - Managing documentation

## Documentation Overview:

### User Guide Sections:
1. **Introduction** - What the system does
2. **Prerequisites** - System requirements
3. **Installation** - How to install and set up
4. **Usage** - How to run the optimizer
5. **Understanding Results** - Interpreting output files
6. **Governance Rules** - Safety limits and thresholds
7. **Troubleshooting** - Common issues and solutions
8. **Advanced Usage** - Customization options

### Key Topics Covered:

#### **Governance Rules:**
- Maximum increase: 15% per week
- Maximum decrease: 30% per week
- Variance cap: ±25% from current Winter K-factor
- Confidence threshold: 80% for auto-apply

#### **Seasonal Adjustments:**
- Winter K-factor: Primary heating season
- Summer K-factor: Reduced consumption period
- Summer multiplier: 1.2x adjustment
- Degree day calculation: Heating degree days

#### **Output Files:**
- `Apply_K_ThisWeek.csv`: Customers ready for import
- `K_Review_Queue.xlsx`: Customers requiring manual review
- Detailed analysis and governance application

#### **Troubleshooting:**
- Permission errors with Excel files
- Missing CSV files
- Invalid data handling
- File format issues

## Target Audience:

- **End Users:** Staff running the optimizer
- **IT Support:** Installation and maintenance
- **Management:** Understanding governance rules
- **Developers:** System customization

## Maintenance:

- **Update when:** Governance rules change
- **Update when:** New features added
- **Update when:** Troubleshooting issues arise
- **Version:** Keep synchronized with application version
