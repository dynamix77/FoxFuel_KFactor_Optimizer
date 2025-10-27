"""
FoxFuel K-Factor Optimizer - Deployment Package Creator
Creates a complete deployment package for installing on other computers.
"""

import os
import shutil
import zipfile
from pathlib import Path
from datetime import datetime

def create_deployment_package():
    """Create a complete deployment package."""
    
    print("FoxFuel K-Factor Optimizer - Deployment Package Creator")
    print("=" * 60)
    
    # Define package contents
    package_name = "FoxFuel_KFactor_Optimizer_Deployment"
    package_dir = Path(package_name)
    
    # Files to include in the package
    files_to_copy = [
        "FoxFuel_KFactor_Optimizer.exe",
        "INSTALL.bat",
        "RUN_GUI.bat",
        "FoxFuel_KFactor_User_Guide.md",
        "README.md",
        "INSTALLATION_GUIDE.md"
    ]
    
    print(f"Creating deployment package: {package_name}")
    print()
    
    # Create package directory
    if package_dir.exists():
        print(f"Removing existing package directory...")
        shutil.rmtree(package_dir)
    
    package_dir.mkdir()
    print(f"Created package directory: {package_dir}")
    
    # Copy files to package
    copied_files = []
    missing_files = []
    
    for file_name in files_to_copy:
        source_path = Path(file_name)
        dest_path = package_dir / file_name
        
        if source_path.exists():
            shutil.copy2(source_path, dest_path)
            copied_files.append(file_name)
            print(f"Copied: {file_name}")
        else:
            missing_files.append(file_name)
            print(f"Missing: {file_name}")
    
    # Create data folder structure template
    data_dir = package_dir / "data"
    inputs_dir = data_dir / "inputs"
    outputs_dir = data_dir / "outputs"
    
    data_dir.mkdir()
    inputs_dir.mkdir()
    outputs_dir.mkdir()
    
    # Create placeholder files
    placeholder_files = [
        ("data/inputs/README.txt", "Place your Ignite CSV exports here:\n- 03_CustomerFuel.csv\n- 04_DeliveryTickets.csv\n- 06_DegreeDayValues.csv"),
        ("data/outputs/README.txt", "K-Factor optimization results will appear here:\n- Apply_K_ThisWeek.csv\n- K_Review_Queue.xlsx")
    ]
    
    for file_path, content in placeholder_files:
        full_path = package_dir / file_path
        with open(full_path, 'w') as f:
            f.write(content)
        print(f"Created: {file_path}")
    
    # Create package info file
    package_info = f"""FoxFuel K-Factor Optimizer - Deployment Package
Generated: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}

Package Contents:
- FoxFuel_KFactor_Optimizer.exe ({get_file_size('FoxFuel_KFactor_Optimizer.exe')} MB)
- INSTALL.bat (Automated installer)
- RUN_GUI.bat (Simple launcher)
- FoxFuel_KFactor_User_Guide.md (User manual)
- README.md (Quick reference)
- INSTALLATION_GUIDE.md (Installation instructions)
- data/ folder structure

Installation Instructions:
1. Extract this package to a folder on the target computer
2. Run INSTALL.bat as administrator
3. Place CSV files in data/inputs/ folder
4. Run FoxFuel_KFactor_Optimizer.exe

System Requirements:
- Windows 10 or later
- 500 MB free disk space
- No Python installation required

For support, refer to INSTALLATION_GUIDE.md
"""
    
    info_file = package_dir / "PACKAGE_INFO.txt"
    with open(info_file, 'w') as f:
        f.write(package_info)
    print(f"Created: PACKAGE_INFO.txt")
    
    # Create ZIP archive
    zip_name = f"{package_name}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.zip"
    print(f"\nCreating ZIP archive: {zip_name}")
    
    with zipfile.ZipFile(zip_name, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(package_dir):
            for file in files:
                file_path = Path(root) / file
                arc_path = file_path.relative_to(package_dir.parent)
                zipf.write(file_path, arc_path)
    
    zip_size = Path(zip_name).stat().st_size / (1024 * 1024)
    print(f"Created ZIP archive: {zip_name} ({zip_size:.1f} MB)")
    
    # Summary
    print("\n" + "=" * 60)
    print("DEPLOYMENT PACKAGE CREATED SUCCESSFULLY!")
    print("=" * 60)
    print(f"Package directory: {package_dir}")
    print(f"ZIP archive: {zip_name}")
    print(f"ZIP size: {zip_size:.1f} MB")
    print()
    print("Files included:")
    for file in copied_files:
        print(f"  Copied: {file}")
    
    if missing_files:
        print("\nFiles missing (not included):")
        for file in missing_files:
            print(f"  Missing: {file}")
    
    print("\nNext steps:")
    print("1. Test the package on a clean system")
    print("2. Distribute the ZIP file to staff computers")
    print("3. Staff can extract and run INSTALL.bat")
    print("4. Provide CSV files for data/inputs/ folder")
    
    return zip_name, package_dir

def get_file_size(file_path):
    """Get file size in MB."""
    try:
        size_bytes = Path(file_path).stat().st_size
        return round(size_bytes / (1024 * 1024), 1)
    except FileNotFoundError:
        return "Unknown"

if __name__ == "__main__":
    try:
        zip_file, package_dir = create_deployment_package()
        print(f"\nDeployment package ready: {zip_file}")
    except Exception as e:
        print(f"\nError creating deployment package: {e}")
        print("Please check that all required files exist and try again.")
