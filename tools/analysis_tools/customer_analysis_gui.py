"""
Customer K-Factor Analysis Tool - GUI Version
Interactive tool to trace through the calculation logic for any customer.
"""

import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
import threading
import sys
from pathlib import Path

# Add src to path
sys.path.append('src')

from src.data_loader import DataLoader
from src.interval_builder import IntervalBuilder
from src.kfactor_calculator import KFactorCalculator
from src.governance import GovernanceEngine
from src.config import *

class CustomerAnalysisGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("FoxFuel K-Factor Analysis Tool")
        self.root.geometry("1200x800")
        
        # Initialize components
        self.setup_ui()
        self.load_data()
        
    def setup_ui(self):
        """Create the user interface."""
        
        # Top frame for input
        input_frame = ttk.Frame(self.root, padding="10")
        input_frame.pack(fill=tk.X)
        
        ttk.Label(input_frame, text="Customer Number:", font=('Arial', 12)).pack(side=tk.LEFT, padx=5)
        
        self.customer_var = tk.StringVar()
        entry = ttk.Entry(input_frame, textvariable=self.customer_var, font=('Arial', 12), width=20)
        entry.pack(side=tk.LEFT, padx=5)
        entry.bind('<Return>', lambda e: self.analyze_customer())
        
        ttk.Button(input_frame, text="Analyze", command=self.analyze_customer).pack(side=tk.LEFT, padx=5)
        
        # Main notebook for different views
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Summary tab
        self.summary_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.summary_tab, text="Summary")
        
        # Intervals tab
        self.intervals_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.intervals_tab, text="Delivery Intervals")
        
        # K-Factor Calculation tab
        self.kfactor_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.kfactor_tab, text="K-Factor Calculation")
        
        # Governance tab
        self.governance_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.governance_tab, text="Governance Rules")
        
        # Detailed Output tab
        self.output_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.output_tab, text="Detailed Output")
        
        self.create_summary_tab()
        self.create_output_tab()
        
    def create_summary_tab(self):
        """Create the summary tab."""
        
        # Summary frame
        summary_frame = ttk.LabelFrame(self.summary_tab, text="Customer Summary", padding="10")
        summary_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        self.summary_text = scrolledtext.ScrolledText(summary_frame, height=30, wrap=tk.WORD, font=('Courier', 10))
        self.summary_text.pack(fill=tk.BOTH, expand=True)
        
    def create_output_tab(self):
        """Create the detailed output tab."""
        
        # Output frame
        output_frame = ttk.LabelFrame(self.output_tab, text="Detailed Analysis Output", padding="10")
        output_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        self.output_text = scrolledtext.ScrolledText(output_frame, height=30, wrap=tk.WORD, font=('Courier', 9))
        self.output_text.pack(fill=tk.BOTH, expand=True)
        
    def load_data(self):
        """Load all data files."""
        try:
            self.data_loader = DataLoader(INPUT_DIR)
            self.customer_fuel, self.delivery_tickets, self.degree_days = self.data_loader.load_all_data()
            print("Data loaded successfully")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load data: {e}")
            self.root.destroy()
            
    def analyze_customer(self):
        """Analyze the specified customer."""
        customer_number = self.customer_var.get().strip()
        
        if not customer_number:
            messagebox.showwarning("Warning", "Please enter a customer number")
            return
        
        # Run analysis in separate thread
        thread = threading.Thread(target=self._analyze_thread, args=(customer_number,))
        thread.daemon = True
        thread.start()
        
    def _analyze_thread(self, customer_number):
        """Run analysis in background thread."""
        
        try:
            # Find customer
            customer_data = self.customer_fuel[self.customer_fuel['Customer Number'] == customer_number]
            
            if customer_data.empty:
                self.root.after(0, lambda: messagebox.showerror("Error", f"Customer {customer_number} not found!"))
                return
                
            # Get customer info
            current_winter_k = customer_data['K Factor - Winter'].iloc[0]
            current_summer_k = customer_data['K Factor - Summer'].iloc[0]
            usable_size = customer_data['Usable Size'].iloc[0]
            
            # Build intervals
            interval_builder = IntervalBuilder()
            intervals = interval_builder.build_intervals(self.customer_fuel, self.delivery_tickets, self.degree_days)
            customer_intervals = intervals[intervals['Customer Number'] == customer_number]
            
            # Filter valid intervals
            valid_intervals = interval_builder.filter_valid_intervals(intervals)
            customer_valid_intervals = valid_intervals[valid_intervals['Customer Number'] == customer_number]
            
            # Calculate interval K-factors
            kfactor_calculator = KFactorCalculator()
            interval_k_factors = kfactor_calculator.calculate_interval_k_factors(valid_intervals)
            customer_interval_k = interval_k_factors[interval_k_factors['Customer Number'] == customer_number]
            
            # Calculate weighted K-factor
            customer_k_factors = kfactor_calculator.calculate_weighted_k_by_customer(interval_k_factors)
            customer_weighted_k = customer_k_factors[customer_k_factors['Customer Number'] == customer_number]
            
            if customer_weighted_k.empty:
                weighted_k = None
                interval_count = 0
                total_gallons = 0
                total_days = 0
            else:
                weighted_k = customer_weighted_k['Weighted K Factor'].iloc[0]
                interval_count = customer_weighted_k['Interval Count'].iloc[0]
                total_gallons = customer_weighted_k['Total Gallons'].iloc[0]
                total_days = customer_weighted_k['Total Degree Days'].iloc[0]
            
            # Calculate variance
            variance_data = kfactor_calculator.calculate_variance(self.customer_fuel, customer_k_factors)
            customer_variance = variance_data[variance_data['Customer Number'] == customer_number]
            
            if customer_variance.empty:
                final_data = {
                    'customer_number': customer_number,
                    'current_winter_k': current_winter_k,
                    'current_summer_k': current_summer_k,
                    'usable_size': usable_size,
                    'total_intervals': len(customer_intervals),
                    'valid_intervals': len(customer_valid_intervals),
                    'weighted_k': weighted_k,
                    'intervals': customer_intervals,
                    'interval_k_factors': customer_interval_k,
                    'final_status': 'INSUFFICIENT_DATA',
                    'proposed_k': None,
                    'final_variance': None,
                }
            else:
                # Apply governance
                governance_engine = GovernanceEngine()
                governed_data = governance_engine.apply_governance(variance_data)
                customer_governed = governed_data[governed_data['Customer Number'] == customer_number]
                
                if customer_governed.empty:
                    proposed_k = None
                    final_variance = None
                    final_status = 'INSUFFICIENT_DATA'
                else:
                    proposed_k = customer_governed['Proposed K Factor'].iloc[0]
                    final_variance = customer_governed['Final Variance Percent'].iloc[0]
                    final_status = customer_governed['Final Status'].iloc[0]
                
                final_data = {
                    'customer_number': customer_number,
                    'current_winter_k': current_winter_k,
                    'current_summer_k': current_summer_k,
                    'usable_size': usable_size,
                    'total_intervals': len(customer_intervals),
                    'valid_intervals': len(customer_valid_intervals),
                    'weighted_k': weighted_k,
                    'interval_count': interval_count,
                    'total_gallons': total_gallons,
                    'total_days': total_days,
                    'intervals': customer_intervals,
                    'interval_k_factors': customer_interval_k,
                    'final_status': final_status,
                    'proposed_k': proposed_k,
                    'final_variance': final_variance,
                }
            
            # Update UI in main thread
            self.root.after(0, self._update_display, final_data)
            
        except Exception as e:
            self.root.after(0, lambda: messagebox.showerror("Error", f"Analysis failed: {e}"))
    
    def _update_display(self, data):
        """Update the display with analysis results."""
        
        # Clear previous content
        self.summary_text.delete(1.0, tk.END)
        self.output_text.delete(1.0, tk.END)
        
        # Build summary
        summary = []
        summary.append(f"FoxFuel K-Factor Analysis for Customer: {data['customer_number']}")
        summary.append("=" * 70)
        summary.append("")
        
        summary.append("CUSTOMER INFORMATION")
        summary.append("-" * 70)
        summary.append(f"Current Winter K-Factor: {data['current_winter_k']:.4f}")
        summary.append(f"Current Summer K-Factor: {data['current_summer_k']:.4f}")
        summary.append(f"Usable Tank Size: {data['usable_size']:.0f} gallons")
        summary.append("")
        
        summary.append("DELIVERY INTERVALS")
        summary.append("-" * 70)
        summary.append(f"Total Intervals Found: {data['total_intervals']}")
        summary.append(f"Valid Intervals: {data['valid_intervals']}")
        summary.append(f"Minimum Days Required: {MIN_INTERVAL_DAYS}")
        summary.append("")
        
        if data['valid_intervals'] == 0:
            summary.append("❌ No valid intervals found - insufficient data for analysis")
        else:
            summary.append("Valid Interval Details:")
            for idx, interval in data['intervals'].head(data['valid_intervals']).iterrows():
                summary.append(f"  {interval['Start Date'].strftime('%Y-%m-%d')} to {interval['End Date'].strftime('%Y-%m-%d')}")
                summary.append(f"    Days: {interval['Interval Days']}")
                summary.append(f"    Gallons Used: {interval['Total Gallons']:.1f}")
                summary.append(f"    Degree Days: {interval['Degree Days Used']:.1f}")
                summary.append(f"    Is Full Fill: {interval.get('Is Full Fill', 'N/A')}")
                summary.append("")
        
        summary.append("K-FACTOR CALCULATION")
        summary.append("-" * 70)
        
        if data['weighted_k'] is None:
            summary.append("❌ Could not calculate K-factor (insufficient data)")
        else:
            summary.append(f"Weighted K-Factor: {data['weighted_k']:.4f}")
            variance = ((data['weighted_k'] - data['current_winter_k']) / data['current_winter_k']) * 100
            summary.append(f"Variance from Current: {variance:+.1f}%")
            summary.append("")
            summary.append(f"Interval K-Factors:")
            for idx, k_factor in data['interval_k_factors'].iterrows():
                summary.append(f"  Interval {idx + 1}: {k_factor['Interval K Factor']:.4f}")
            summary.append("")
        
        summary.append("GOVERNANCE RULES APPLIED")
        summary.append("-" * 70)
        summary.append(f"Maximum Increase: {MAX_INCREASE*100:.0f}% per week")
        summary.append(f"Maximum Decrease: {MAX_DECREASE*100:.0f}% per week")
        summary.append(f"Variance Cap: ±{CAP_PCT*100:.0f}%")
        summary.append(f"Confidence Threshold: {CONFIDENCE_THRESHOLD*100:.0f}%")
        summary.append("")
        
        summary.append("FINAL RESULT")
        summary.append("-" * 70)
        summary.append(f"Status: {data['final_status']}")
        
        if data['proposed_k'] is not None:
            summary.append(f"Proposed K-Factor: {data['proposed_k']:.4f}")
            summary.append(f"Final Variance: {data['final_variance']:.1f}%")
            
            if data['final_status'] == 'CAPPED_INCREASE':
                summary.append("Reason: Capped at maximum increase limit (15%)")
            elif data['final_status'] == 'CAPPED_DECREASE':
                summary.append("Reason: Capped at maximum decrease limit (30%)")
            elif data['final_status'] == 'CAPPED_LOWER_BOUND':
                summary.append("Reason: Capped at variance boundary (-25%)")
            elif data['final_status'] == 'CAPPED_UPPER_BOUND':
                summary.append("Reason: Capped at variance boundary (+25%)")
            elif data['final_status'] == 'LOW_CONFIDENCE':
                summary.append("Reason: Low confidence (requires manual review)")
            elif data['final_status'] == 'INSUFFICIENT_DATA':
                summary.append("Reason: Insufficient data (requires manual review)")
        else:
            summary.append("No proposed K-factor (insufficient data)")
        
        # Update display
        self.summary_text.insert(1.0, '\n'.join(summary))
        
        # Also update detailed output
        detailed_output = []
        detailed_output.append("DETAILED CALCULATION TRACE")
        detailed_output.append("=" * 70)
        detailed_output.append("")
        detailed_output.append(f"Customer: {data['customer_number']}")
        detailed_output.append(f"Current Winter K: {data['current_winter_k']:.6f}")
        detailed_output.append(f"Current Summer K: {data['current_summer_k']:.6f}")
        detailed_output.append("")
        
        detailed_output.append(f"Total Intervals: {data['total_intervals']}")
        detailed_output.append(f"Valid Intervals: {data['valid_intervals']}")
        detailed_output.append("")
        
        for idx, interval in data['intervals'].iterrows():
            detailed_output.append(f"Interval {idx + 1}:")
            detailed_output.append(f"  Start: {interval['Start Date'].strftime('%Y-%m-%d')}")
            detailed_output.append(f"  End: {interval['End Date'].strftime('%Y-%m-%d')}")
            detailed_output.append(f"  Days: {interval['Interval Days']}")
            detailed_output.append(f"  Gallons: {interval['Total Gallons']:.2f}")
            detailed_output.append(f"  Degree Days: {interval['Degree Days Used']:.2f}")
            detailed_output.append(f"  Valid: {interval['Interval Days'] >= MIN_INTERVAL_DAYS}")
            detailed_output.append("")
        
        if data['weighted_k'] is not None:
            detailed_output.append(f"Weighted K: {data['weighted_k']:.6f}")
            detailed_output.append(f"Variance: {((data['weighted_k'] - data['current_winter_k']) / data['current_winter_k']) * 100:+.2f}%")
        
        if data['proposed_k'] is not None:
            detailed_output.append(f"Proposed K: {data['proposed_k']:.6f}")
            detailed_output.append(f"Final Variance: {data['final_variance']:.2f}%")
            detailed_output.append(f"Status: {data['final_status']}")
        
        self.output_text.insert(1.0, '\n'.join(detailed_output))

def main():
    """Main function to run the GUI."""
    root = tk.Tk()
    app = CustomerAnalysisGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
