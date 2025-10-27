"""
PyInstaller build script for creating standalone FoxFuel K-Factor Optimizer executable.
This creates a single .exe file that can run on any Windows computer without Python installed.
"""

import os
import sys
import subprocess
from pathlib import Path

def build_executable():
    """Build standalone executable using PyInstaller."""
    
    print("FoxFuel K-Factor Optimizer - Executable Builder")
    print("=" * 50)
    
    # Check if PyInstaller is installed
    try:
        import PyInstaller
        print(f"PyInstaller version: {PyInstaller.__version__}")
    except ImportError:
        print("PyInstaller not found. Installing...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "pyinstaller"])
        print("PyInstaller installed successfully.")
    
    # Build the executable
    print("\nBuilding executable...")
    print("This may take 2-5 minutes...")
    
    cmd = [
        "pyinstaller",
        "--onefile",                    # Single executable file
        "--windowed",                   # No console window (optional)
        "--name=FoxFuel_KFactor",       # Executable name
        "--add-data=data;data",         # Include data directory
        "--hidden-import=openpyxl",     # Ensure openpyxl is included
        "--hidden-import=loguru",       # Ensure loguru is included
        "run_local.py"                 # Main script
    ]
    
    try:
        subprocess.run(cmd, check=True)
        
        # Check if executable was created
        exe_path = Path("dist/FoxFuel_KFactor.exe")
        if exe_path.exists():
            print(f"\n✓ SUCCESS! Executable created: {exe_path}")
            print(f"File size: {exe_path.stat().st_size / (1024*1024):.1f} MB")
            
            print("\nTo deploy:")
            print(f"1. Copy {exe_path} to any Windows computer")
            print("2. Create a 'data' folder next to the .exe")
            print("3. Put your CSV files in data/inputs/")
            print("4. Double-click FoxFuel_KFactor.exe to run")
            
            return True
        else:
            print("✗ ERROR: Executable not found after build")
            return False
            
    except subprocess.CalledProcessError as e:
        print(f"✗ ERROR: Build failed with code {e.returncode}")
        return False
    except Exception as e:
        print(f"✗ ERROR: {str(e)}")
        return False

def create_console_version():
    """Create console version (shows output window)."""
    
    print("\nCreating console version (shows progress)...")
    
    cmd = [
        "pyinstaller",
        "--onefile",                    # Single executable file
        "--console",                     # Show console window
        "--name=FoxFuel_KFactor_Console", # Executable name
        "--add-data=data;data",         # Include data directory
        "--hidden-import=openpyxl",     # Ensure openpyxl is included
        "--hidden-import=loguru",       # Ensure loguru is included
        "run_local.py"                  # Main script
    ]
    
    try:
        subprocess.run(cmd, check=True)
        
        exe_path = Path("dist/FoxFuel_KFactor_Console.exe")
        if exe_path.exists():
            print(f"✓ Console version created: {exe_path}")
            return True
        else:
            print("✗ Console version not found")
            return False
            
    except Exception as e:
        print(f"✗ Console version failed: {str(e)}")
        return False

if __name__ == "__main__":
    print("Choose build option:")
    print("1. Windowed version (no console)")
    print("2. Console version (shows progress)")
    print("3. Both versions")
    
    choice = input("\nEnter choice (1-3): ").strip()
    
    if choice == "1":
        build_executable()
    elif choice == "2":
        create_console_version()
    elif choice == "3":
        build_executable()
        create_console_version()
    else:
        print("Invalid choice. Building windowed version...")
        build_executable()
    
    input("\nPress Enter to exit...")
