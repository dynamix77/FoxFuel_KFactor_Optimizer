"""
Build script to create a standalone .exe file for the Customer Analysis Tool.
"""

import subprocess
import sys
from pathlib import Path

def build_analysis_exe():
    """Build the analysis tool executable using PyInstaller."""
    
    print("Building FoxFuel Customer Analysis Tool Executable...")
    print("=" * 60)
    
    # PyInstaller command
    cmd = [
        "pyinstaller",
        "--onefile",
        "--windowed",
        "--name=Customer_Analysis_Tool",
        "--add-data=src;src",
        "--add-data=data;data",
        "--hidden-import=pandas",
        "--hidden-import=numpy",
        "--hidden-import=openpyxl",
        "--hidden-import=loguru",
        "--hidden-import=tkinter",
        "--hidden-import=tkinter.ttk",
        "--hidden-import=tkinter.scrolledtext",
        "--hidden-import=tkinter.messagebox",
        "--clean",
        "customer_analysis_gui.py"
    ]
    
    print("Running PyInstaller...")
    print()
    
    try:
        result = subprocess.run(cmd, check=True)
        
        print()
        print("=" * 60)
        print("BUILD COMPLETE!")
        print("=" * 60)
        
        exe_path = Path("dist/Customer_Analysis_Tool.exe")
        if exe_path.exists():
            size_mb = exe_path.stat().st_size / (1024 * 1024)
            print(f"Executable created: {exe_path}")
            print(f"File size: {size_mb:.1f} MB")
            print()
            print("The Customer Analysis Tool is ready to use!")
            
        return str(exe_path) if exe_path.exists() else None
            
    except subprocess.CalledProcessError as e:
        print(f"Build failed with error: {e}")
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None

if __name__ == "__main__":
    try:
        exe_path = build_analysis_exe()
        if exe_path:
            print(f"\nSuccess! Executable ready: {exe_path}")
        else:
            print("\nBuild failed. Please check errors above.")
    except Exception as e:
        print(f"Error: {e}")
