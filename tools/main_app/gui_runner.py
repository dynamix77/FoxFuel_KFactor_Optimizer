"""
FoxFuel K-Factor Optimizer - GUI Interface
A user-friendly graphical interface for running the K-Factor optimization pipeline.
"""

import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import threading
import subprocess
import os
import sys
from pathlib import Path
import webbrowser

# Add src to path for imports
sys.path.append(str(Path(__file__).parent / "src"))

from src.pipeline import KFactorPipeline
from src.logger import get_logger

logger = get_logger()

class FoxFuelGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("FoxFuel K-Factor Optimizer")
        self.root.geometry("600x500")
        self.root.resizable(True, True)
        
        # Set window icon (if available)
        try:
            self.root.iconbitmap("icon.ico")
        except:
            pass
        
        # Configure style
        style = ttk.Style()
        style.theme_use('clam')
        
        self.setup_ui()
        self.setup_variables()
        
    def setup_ui(self):
        """Create the user interface."""
        
        # Main frame
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Configure grid weights
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)
        
        # Title
        title_label = ttk.Label(main_frame, text="FoxFuel K-Factor Optimizer", 
                               font=('Arial', 16, 'bold'))
        title_label.grid(row=0, column=0, columnspan=3, pady=(0, 20))
        
        # Input files section
        input_frame = ttk.LabelFrame(main_frame, text="Input Files", padding="10")
        input_frame.grid(row=1, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=(0, 10))
        input_frame.columnconfigure(1, weight=1)
        
        # Customer Fuel file
        ttk.Label(input_frame, text="Customer Fuel:").grid(row=0, column=0, sticky=tk.W, padx=(0, 10))
        self.customer_fuel_var = tk.StringVar()
        customer_fuel_entry = ttk.Entry(input_frame, textvariable=self.customer_fuel_var, state='readonly')
        customer_fuel_entry.grid(row=0, column=1, sticky=(tk.W, tk.E), padx=(0, 10))
        
        # Delivery Tickets file
        ttk.Label(input_frame, text="Delivery Tickets:").grid(row=1, column=0, sticky=tk.W, padx=(0, 10))
        self.delivery_tickets_var = tk.StringVar()
        delivery_tickets_entry = ttk.Entry(input_frame, textvariable=self.delivery_tickets_var, state='readonly')
        delivery_tickets_entry.grid(row=1, column=1, sticky=(tk.W, tk.E), padx=(0, 10))
        
        # Degree Day Values file
        ttk.Label(input_frame, text="Degree Day Values:").grid(row=2, column=0, sticky=tk.W, padx=(0, 10))
        self.degree_days_var = tk.StringVar()
        degree_days_entry = ttk.Entry(input_frame, textvariable=self.degree_days_var, state='readonly')
        degree_days_entry.grid(row=2, column=1, sticky=(tk.W, tk.E), padx=(0, 10))
        
        # Auto-detect button
        ttk.Button(input_frame, text="Auto-Detect Files", 
                  command=self.auto_detect_files).grid(row=3, column=0, columnspan=2, pady=(10, 0))
        
        # Control buttons
        button_frame = ttk.Frame(main_frame)
        button_frame.grid(row=2, column=0, columnspan=3, pady=(0, 20))
        
        self.run_button = ttk.Button(button_frame, text="Run K-Factor Optimizer", 
                                    command=self.run_optimization, style='Accent.TButton')
        self.run_button.pack(side=tk.LEFT, padx=(0, 10))
        
        self.open_inputs_button = ttk.Button(button_frame, text="Open Inputs Folder", 
                                            command=self.open_inputs_folder)
        self.open_inputs_button.pack(side=tk.LEFT, padx=(0, 10))
        
        self.open_outputs_button = ttk.Button(button_frame, text="Open Outputs Folder", 
                                             command=self.open_outputs_folder)
        self.open_outputs_button.pack(side=tk.LEFT)
        
        # Progress section
        progress_frame = ttk.LabelFrame(main_frame, text="Progress", padding="10")
        progress_frame.grid(row=3, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=(0, 10))
        progress_frame.columnconfigure(0, weight=1)
        
        self.progress_var = tk.StringVar(value="Ready to run optimization...")
        ttk.Label(progress_frame, textvariable=self.progress_var).grid(row=0, column=0, sticky=tk.W)
        
        self.progress_bar = ttk.Progressbar(progress_frame, mode='indeterminate')
        self.progress_bar.grid(row=1, column=0, sticky=(tk.W, tk.E), pady=(5, 0))
        
        # Log section
        log_frame = ttk.LabelFrame(main_frame, text="Log Output", padding="10")
        log_frame.grid(row=4, column=0, columnspan=3, sticky=(tk.W, tk.E, tk.N, tk.S), pady=(0, 10))
        log_frame.columnconfigure(0, weight=1)
        log_frame.rowconfigure(0, weight=1)
        main_frame.rowconfigure(4, weight=1)
        
        # Log text widget with scrollbar
        log_text_frame = ttk.Frame(log_frame)
        log_text_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        log_text_frame.columnconfigure(0, weight=1)
        log_text_frame.rowconfigure(0, weight=1)
        
        self.log_text = tk.Text(log_text_frame, height=10, wrap=tk.WORD, state='disabled')
        self.log_text.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        log_scrollbar = ttk.Scrollbar(log_text_frame, orient=tk.VERTICAL, command=self.log_text.yview)
        log_scrollbar.grid(row=0, column=1, sticky=(tk.N, tk.S))
        self.log_text.configure(yscrollcommand=log_scrollbar.set)
        
        # Results section
        results_frame = ttk.LabelFrame(main_frame, text="Results", padding="10")
        results_frame.grid(row=5, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=(0, 10))
        
        self.results_var = tk.StringVar(value="No results yet")
        ttk.Label(results_frame, textvariable=self.results_var).grid(row=0, column=0, sticky=tk.W)
        
        # Result buttons
        result_button_frame = ttk.Frame(results_frame)
        result_button_frame.grid(row=1, column=0, sticky=tk.W, pady=(5, 0))
        
        self.open_csv_button = ttk.Button(result_button_frame, text="Open Apply_K_ThisWeek.csv", 
                                         command=self.open_csv_file, state='disabled')
        self.open_csv_button.pack(side=tk.LEFT, padx=(0, 10))
        
        self.open_excel_button = ttk.Button(result_button_frame, text="Open K_Review_Queue.xlsx", 
                                          command=self.open_excel_file, state='disabled')
        self.open_excel_button.pack(side=tk.LEFT)
        
        # Status bar
        self.status_var = tk.StringVar(value="Ready")
        status_bar = ttk.Label(main_frame, textvariable=self.status_var, relief=tk.SUNKEN)
        status_bar.grid(row=6, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=(10, 0))
        
    def setup_variables(self):
        """Initialize variables."""
        self.is_running = False
        self.csv_file_path = None
        self.excel_file_path = None
        
    def auto_detect_files(self):
        """Auto-detect CSV files in the inputs folder."""
        inputs_dir = Path("data/inputs")
        
        if not inputs_dir.exists():
            messagebox.showerror("Error", "data/inputs folder not found!\n\nPlease create the folder and add your CSV files.")
            return
        
        # Find files matching patterns
        customer_fuel_files = list(inputs_dir.glob("03_*.csv"))
        delivery_tickets_files = list(inputs_dir.glob("04_*.csv"))
        degree_days_files = list(inputs_dir.glob("06_*.csv"))
        
        # Set the latest files
        if customer_fuel_files:
            latest_customer_fuel = max(customer_fuel_files, key=lambda x: x.stat().st_mtime)
            self.customer_fuel_var.set(str(latest_customer_fuel))
        else:
            self.customer_fuel_var.set("Not found")
            
        if delivery_tickets_files:
            latest_delivery_tickets = max(delivery_tickets_files, key=lambda x: x.stat().st_mtime)
            self.delivery_tickets_var.set(str(latest_delivery_tickets))
        else:
            self.delivery_tickets_var.set("Not found")
            
        if degree_days_files:
            latest_degree_days = max(degree_days_files, key=lambda x: x.stat().st_mtime)
            self.degree_days_var.set(str(latest_degree_days))
        else:
            self.degree_days_var.set("Not found")
        
        # Check if all files found
        all_found = (customer_fuel_files and delivery_tickets_files and degree_days_files)
        
        if all_found:
            self.status_var.set("All input files detected")
            self.log_message("✓ All required CSV files detected successfully")
        else:
            missing = []
            if not customer_fuel_files:
                missing.append("Customer Fuel (03_*.csv)")
            if not delivery_tickets_files:
                missing.append("Delivery Tickets (04_*.csv)")
            if not degree_days_files:
                missing.append("Degree Day Values (06_*.csv)")
            
            self.status_var.set(f"Missing files: {', '.join(missing)}")
            self.log_message(f"⚠ Missing files: {', '.join(missing)}")
    
    def log_message(self, message):
        """Add a message to the log display."""
        self.log_text.configure(state='normal')
        self.log_text.insert(tk.END, f"{message}\n")
        self.log_text.see(tk.END)
        self.log_text.configure(state='disabled')
        self.root.update_idletasks()
    
    def run_optimization(self):
        """Run the K-Factor optimization in a separate thread."""
        if self.is_running:
            return
        
        # Check if files are detected
        if (self.customer_fuel_var.get() == "Not found" or 
            self.delivery_tickets_var.get() == "Not found" or 
            self.degree_days_var.get() == "Not found"):
            messagebox.showerror("Error", "Please auto-detect files first or ensure CSV files are in data/inputs/ folder.")
            return
        
        # Start optimization in separate thread
        self.is_running = True
        self.run_button.configure(state='disabled')
        self.progress_bar.start()
        self.progress_var.set("Running K-Factor optimization...")
        self.status_var.set("Processing...")
        
        # Clear log
        self.log_text.configure(state='normal')
        self.log_text.delete(1.0, tk.END)
        self.log_text.configure(state='disabled')
        
        # Start thread
        thread = threading.Thread(target=self._run_optimization_thread)
        thread.daemon = True
        thread.start()
    
    def _run_optimization_thread(self):
        """Run optimization in background thread."""
        try:
            self.log_message("Starting FoxFuel K-Factor Optimization...")
            self.log_message("=" * 50)
            
            # Create and run the pipeline
            pipeline = KFactorPipeline()
            result = pipeline.run_pipeline()
            
            if result['status'] == 'success':
                self.log_message("=" * 50)
                self.log_message("✓ Optimization completed successfully!")
                
                # Set result paths
                self.csv_file_path = Path(result['files']['apply_k_this_week'])
                self.excel_file_path = Path(result['files']['k_review_queue'])
                
                # Log summary statistics
                stats = result['statistics']
                self.log_message(f"Total customers processed: {stats['total_customers']}")
                self.log_message(f"Valid intervals found: {stats['valid_intervals']}")
                self.log_message(f"Customers ready for auto-apply: {stats['auto_apply_customers']}")
                
                # Update UI
                self.root.after(0, self._optimization_success)
            else:
                self.log_message("=" * 50)
                self.log_message(f"✗ Optimization failed: {result['error']}")
                self.root.after(0, self._optimization_failed)
                
        except Exception as e:
            self.log_message(f"✗ Error: {str(e)}")
            self.root.after(0, self._optimization_error, str(e))
    
    def _optimization_success(self):
        """Handle successful optimization."""
        self.is_running = False
        self.run_button.configure(state='normal')
        self.progress_bar.stop()
        self.progress_var.set("Optimization completed successfully!")
        self.status_var.set("Completed successfully")
        
        # Enable result buttons
        self.open_csv_button.configure(state='normal')
        self.open_excel_button.configure(state='normal')
        
        # Update results display
        if self.csv_file_path and self.csv_file_path.exists():
            self.results_var.set(f"Results generated: {self.csv_file_path.name} and {self.excel_file_path.name}")
        else:
            self.results_var.set("Results generated successfully")
        
        # Show success message
        messagebox.showinfo("Success", 
                           "K-Factor optimization completed successfully!\n\n"
                           "Click the buttons below to open the result files.")
    
    def _optimization_failed(self):
        """Handle failed optimization."""
        self.is_running = False
        self.run_button.configure(state='normal')
        self.progress_bar.stop()
        self.progress_var.set("Optimization failed")
        self.status_var.set("Failed")
        
        messagebox.showerror("Error", "K-Factor optimization failed. Check the log output for details.")
    
    def _optimization_error(self, error_msg):
        """Handle optimization error."""
        self.is_running = False
        self.run_button.configure(state='normal')
        self.progress_bar.stop()
        self.progress_var.set("Error occurred")
        self.status_var.set("Error")
        
        messagebox.showerror("Error", f"An error occurred during optimization:\n\n{error_msg}")
    
    def open_inputs_folder(self):
        """Open the inputs folder in file explorer."""
        inputs_dir = Path("data/inputs")
        if inputs_dir.exists():
            os.startfile(str(inputs_dir))
        else:
            messagebox.showwarning("Warning", "data/inputs folder does not exist.")
    
    def open_outputs_folder(self):
        """Open the outputs folder in file explorer."""
        outputs_dir = Path("data/outputs")
        if outputs_dir.exists():
            os.startfile(str(outputs_dir))
        else:
            messagebox.showwarning("Warning", "data/outputs folder does not exist.")
    
    def open_csv_file(self):
        """Open the CSV result file."""
        if self.csv_file_path and self.csv_file_path.exists():
            os.startfile(str(self.csv_file_path))
        else:
            messagebox.showwarning("Warning", "CSV file not found.")
    
    def open_excel_file(self):
        """Open the Excel result file."""
        if self.excel_file_path and self.excel_file_path.exists():
            os.startfile(str(self.excel_file_path))
        else:
            messagebox.showwarning("Warning", "Excel file not found.")

def main():
    """Main function to run the GUI."""
    root = tk.Tk()
    app = FoxFuelGUI(root)
    
    # Auto-detect files on startup
    app.auto_detect_files()
    
    # Center window on screen
    root.update_idletasks()
    x = (root.winfo_screenwidth() // 2) - (root.winfo_width() // 2)
    y = (root.winfo_screenheight() // 2) - (root.winfo_height() // 2)
    root.geometry(f"+{x}+{y}")
    
    root.mainloop()

if __name__ == "__main__":
    main()