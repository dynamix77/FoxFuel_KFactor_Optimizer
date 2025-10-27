# GitHub Repository Setup Guide

## Step 1: Create GitHub Repository

1. **Go to GitHub.com** and sign in to your account
2. **Click the "+" icon** in the top right corner
3. **Select "New repository"**
4. **Fill in repository details:**
   - **Repository name:** `FoxFuel-KFactor-Optimizer`
   - **Description:** `Python-based K-Factor optimization system for heating oil delivery using Ignite CSV exports`
   - **Visibility:** Choose Private (recommended for business use) or Public
   - **Initialize with:** Check "Add a README file" (we'll replace it)
   - **Add .gitignore:** Select "Python"
   - **Choose a license:** Select "MIT License"

5. **Click "Create repository"**

## Step 2: Clone Repository Locally

1. **Copy the repository URL** from GitHub (it will look like: `https://github.com/yourusername/FoxFuel-KFactor-Optimizer.git`)

2. **Open Command Prompt or PowerShell** in your desired location

3. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/FoxFuel-KFactor-Optimizer.git
   cd FoxFuel-KFactor-Optimizer
   ```

## Step 3: Add Project Files

1. **Copy all project files** from your current `FoxFuel_KFactor_Optimizer` folder to the cloned repository folder

2. **Remove the default files** that GitHub created:
   - Delete the default `README.md` (we have our own)
   - Delete the default `.gitignore` (we have our own)

3. **Verify file structure** should look like:
   ```
   FoxFuel-KFactor-Optimizer/
   ├── .gitignore
   ├── LICENSE
   ├── README.md
   ├── FoxFuel_KFactor_User_Guide.md
   ├── requirements.txt
   ├── run_local.py
   ├── RUN_KFACTOR.bat
   ├── build_exe.py
   ├── gui_runner.py
   ├── src/
   │   ├── __init__.py
   │   ├── config.py
   │   ├── data_loader.py
   │   ├── governance.py
   │   ├── interval_builder.py
   │   ├── kfactor_calculator.py
   │   ├── logger.py
   │   ├── outputs_writer.py
   │   └── pipeline.py
   ├── data/
   │   ├── inputs/
   │   │   ├── 03_CustomerFuel.csv
   │   │   ├── 04_DeliveryTickets.csv
   │   │   └── 06_DegreeDayValues.csv
   │   └── outputs/
   │       └── .gitkeep
   └── tests/
   ```

## Step 4: Commit and Push Files

1. **Add all files to git:**
   ```bash
   git add .
   ```

2. **Commit the files:**
   ```bash
   git commit -m "Initial commit: FoxFuel K-Factor Optimizer

   - Complete Python pipeline for K-factor optimization
   - Three deployment options (batch, executable, GUI)
   - Automatic CSV file detection
   - Governance rules and safety limits
   - Comprehensive user guide and documentation
   - Test data included for demonstration"
   ```

3. **Push to GitHub:**
   ```bash
   git push origin main
   ```

## Step 5: Create Releases (Optional but Recommended)

1. **Go to your repository on GitHub**
2. **Click "Releases"** on the right side
3. **Click "Create a new release"**
4. **Fill in release details:**
   - **Tag version:** `v1.0.0`
   - **Release title:** `FoxFuel K-Factor Optimizer v1.0.0`
   - **Description:** 
     ```
     ## Initial Release
     
     Complete K-Factor optimization system with three deployment options:
     
     ### Features
     - One-click batch file execution
     - Standalone executable generation
     - GUI interface with progress feedback
     - Automatic CSV file detection
     - Built-in governance rules
     - Comprehensive logging
     
     ### Files Included
     - Complete Python source code
     - User guide and documentation
     - Test data for demonstration
     - Build scripts for executables
     
     ### Quick Start
     1. Place CSV files in `data/inputs/`
     2. Double-click `RUN_KFACTOR.bat`
     3. Check `data/outputs/` for results
     ```
   - **Attach binaries:** Upload the `.exe` files from your `dist/` folder
   - **Set as latest release:** Check this box

5. **Click "Publish release"**

## Step 6: Repository Settings (Recommended)

1. **Go to repository Settings**
2. **Configure the following:**

   **General:**
   - Add topics: `python`, `k-factor`, `optimization`, `heating-oil`, `ignite`, `data-analysis`
   - Set up branch protection rules for `main` branch

   **Security:**
   - Enable Dependabot alerts
   - Enable secret scanning

   **Pages (if public):**
   - Enable GitHub Pages to host documentation

## Step 7: Team Access (If Private Repository)

1. **Go to Settings > Manage access**
2. **Click "Invite a collaborator"**
3. **Add team members** by GitHub username or email
4. **Set appropriate permissions** (Read, Write, or Admin)

## Step 8: Documentation

Your repository now includes:

- **README.md** - Quick start guide and overview
- **FoxFuel_KFactor_User_Guide.md** - Comprehensive user manual
- **LICENSE** - MIT license for open source compliance
- **requirements.txt** - Python dependencies
- **Test data** - Sample CSV files for demonstration

## Step 9: Ongoing Maintenance

### Regular Updates
```bash
# Make changes to files
git add .
git commit -m "Description of changes"
git push origin main
```

### Creating New Releases
1. Update version numbers in code
2. Create new release tag
3. Upload updated executables
4. Update documentation

### Backup Strategy
- Repository serves as primary backup
- Regular pushes ensure code safety
- Releases provide stable version history

## Repository URL Structure

Your repository will be accessible at:
- **Web:** `https://github.com/yourusername/FoxFuel-KFactor-Optimizer`
- **Clone:** `https://github.com/yourusername/FoxFuel-KFactor-Optimizer.git`
- **Download:** `https://github.com/yourusername/FoxFuel-KFactor-Optimizer/archive/main.zip`

## Next Steps

1. **Share repository URL** with your team
2. **Train staff** on using the tool with the user guide
3. **Set up regular backups** of your Ignite CSV exports
4. **Monitor usage** and gather feedback for future improvements
5. **Consider automation** - schedule weekly CSV exports and K-factor runs

---

**Note:** This guide assumes you have Git installed on your computer. If not, download Git from [git-scm.com](https://git-scm.com/) first.
