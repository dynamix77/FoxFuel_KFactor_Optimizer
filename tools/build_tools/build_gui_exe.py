"""
Build script to create a standalone .exe file for the FoxFuel K-Factor Optimizer GUI.
This creates a single executable file that includes all dependencies.
"""

import subprocess
import sys
import os
from pathlib import Path

def build_gui_exe():
    """Build the GUI executable using PyInstaller."""
    
    print("Building FoxFuel K-Factor Optimizer GUI Executable...")
    print("=" * 60)
    
    # Check if PyInstaller is installed
    try:
        import PyInstaller
        print(f"PyInstaller version: {PyInstaller.__version__}")
    except ImportError:
        print("Installing PyInstaller...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "pyinstaller"])
        print("PyInstaller installed successfully")
    
    # PyInstaller command with options
    cmd = [
        "pyinstaller",
        "--onefile",                    # Create a single executable file
        "--windowed",                  # No console window (GUI only)
        "--name=FoxFuel_KFactor_Optimizer",  # Name of the executable
        "--icon=icon.ico",             # Icon file (if it exists)
        "--add-data=src;src",          # Include src directory
        "--add-data=data;data",        # Include data directory
        "--add-data=README.md;.",      # Include README
        "--add-data=FoxFuel_KFactor_User_Guide.md;.",  # Include user guide
        "--hidden-import=pandas",      # Ensure pandas is included
        "--hidden-import=numpy",       # Ensure numpy is included
        "--hidden-import=openpyxl",    # Ensure openpyxl is included
        "--hidden-import=loguru",      # Ensure loguru is included
        "--hidden-import=tkinter",     # Ensure tkinter is included
        "--hidden-import=tkinter.ttk", # Ensure ttk is included
        "--hidden-import=tkinter.messagebox",  # Ensure messagebox is included
        "--hidden-import=tkinter.filedialog",  # Ensure filedialog is included
        "--clean",                     # Clean cache before building
        "gui_runner.py"               # Main script
    ]
    
    # Remove icon option if icon file doesn't exist
    if not Path("icon.ico").exists():
        cmd.remove("--icon=icon.ico")
        print("No icon.ico found, building without custom icon")
    
    print("Running PyInstaller...")
    print(f"Command: {' '.join(cmd)}")
    print()
    
    try:
        # Run PyInstaller
        result = subprocess.run(cmd, check=True, capture_output=True, text=True)
        
        print("Build completed successfully!")
        print()
        
        # Check if executable was created
        exe_path = Path("dist/FoxFuel_KFactor_Optimizer.exe")
        if exe_path.exists():
            size_mb = exe_path.stat().st_size / (1024 * 1024)
            print(f"Executable created: {exe_path}")
            print(f"File size: {size_mb:.1f} MB")
            print()
            print("The executable is ready to use!")
            print("You can distribute this single .exe file to staff members.")
            print("They can run it without installing Python or any dependencies.")
            
            return str(exe_path)
        else:
            print("Executable not found in expected location")
            return None
            
    except subprocess.CalledProcessError as e:
        print(f"Build failed with error:")
        print(f"Return code: {e.returncode}")
        print(f"Error output: {e.stderr}")
        return None
    except Exception as e:
        print(f"Unexpected error: {e}")
        return None

def test_exe():
    """Test the created executable."""
    exe_path = Path("dist/FoxFuel_KFactor_Optimizer.exe")
    
    if not exe_path.exists():
        print("Executable not found for testing")
        return False
    
    print("Testing the executable...")
    print("=" * 30)
    
    try:
        # Test if the executable can start (just check if it exists and is executable)
        print(f"Executable exists: {exe_path}")
        print(f"File size: {exe_path.stat().st_size / (1024 * 1024):.1f} MB")
        print()
        print("To test the GUI:")
        print("1. Double-click the executable")
        print("2. Verify the GUI opens")
        print("3. Check that it can detect CSV files")
        print("4. Test running the optimization")
        
        return True
        
    except Exception as e:
        print(f"Test failed: {e}")
        return False

if __name__ == "__main__":
    print("FoxFuel K-Factor Optimizer - GUI Executable Builder")
    print("=" * 60)
    
    # Build the executable
    exe_path = build_gui_exe()
    
    if exe_path:
        print()
        print("=" * 60)
        test_exe()
        
        print()
        print("=" * 60)
        print("BUILD COMPLETE!")
        print("=" * 60)
        print(f"Executable location: {exe_path}")
        print()
        print("Next steps:")
        print("1. Test the executable on your system")
        print("2. Copy it to staff computers")
        print("3. Ensure CSV files are in data/inputs/ folder")
        print("4. Staff can run it with a double-click!")
    else:
        print()
        print("=" * 60)
        print("BUILD FAILED!")
        print("=" * 60)
        print("Please check the error messages above and try again.")
