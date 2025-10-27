#!/usr/bin/env python3
"""
FoxFuel K-Factor Optimizer - Main Runner Script
Entry point for running the K-Factor optimization pipeline.
"""

import sys
import os
from pathlib import Path
from datetime import datetime

# Add src directory to Python path
sys.path.insert(0, str(Path(__file__).parent / "src"))

from src.pipeline import KFactorPipeline
from src.logger import setup_logger

def main():
    """Main entry point for the K-Factor Optimizer."""
    
    print("FoxFuel K-Factor Optimizer")
    print("=" * 40)
    print(f"Started at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print()
    
    # Setup logging
    logger = setup_logger("INFO")
    
    try:
        # Initialize pipeline
        pipeline = KFactorPipeline()
        
        # Run the pipeline
        results = pipeline.run_pipeline()
        
        if results['status'] == 'success':
            print("\n" + "=" * 40)
            print("SUCCESS! K-Factor optimization completed.")
            print("=" * 40)
            
            # Print summary
            print(pipeline.get_pipeline_summary())
            
            # Print file locations
            print("\nOutput Files:")
            print(f"• Apply_K_ThisWeek.csv: {results['files']['apply_k_this_week']}")
            print(f"• K_Review_Queue.xlsx: {results['files']['k_review_queue']}")
            
            # Print statistics
            stats = results['statistics']
            print(f"\nQuick Stats:")
            print(f"• Total customers processed: {stats['total_customers']}")
            print(f"• Valid intervals found: {stats['valid_intervals']}")
            print(f"• Customers ready for auto-apply: {stats['auto_apply_customers']}")
            
            print("\nNext Steps:")
            print("1. Review K_Review_Queue.xlsx for flagged customers")
            print("2. Import Apply_K_ThisWeek.csv into Ignite")
            print("3. Monitor delivery performance for the next week")
            
            return 0
            
        else:
            print("\n" + "=" * 40)
            print("ERROR! Pipeline failed.")
            print("=" * 40)
            print(f"Error: {results['error']}")
            print("\nPlease check:")
            print("• Input CSV files are in data/inputs/ folder")
            print("• Files match expected naming patterns (03_*, 04_*, 06_*)")
            print("• Files have correct column headers")
            print("• Files contain valid data")
            
            return 1
            
    except KeyboardInterrupt:
        print("\n\nPipeline interrupted by user.")
        return 1
        
    except Exception as e:
        print(f"\n\nUnexpected error: {str(e)}")
        logger.exception("Unexpected error in main")
        return 1

if __name__ == "__main__":
    exit_code = main()
    input("\nPress Enter to exit...")
    sys.exit(exit_code)
