"""
Main pipeline module for the FoxFuel K-Factor Optimizer.
Orchestrates the 8-step transformation workflow.
"""

import pandas as pd
from pathlib import Path
from datetime import datetime
from typing import Tuple, Dict

from .data_loader import DataLoader
from .interval_builder import IntervalBuilder
from .kfactor_calculator import KFactorCalculator
from .governance import GovernanceEngine
from .outputs_writer import OutputsWriter
from .logger import get_logger
from .config import *

logger = get_logger()

class KFactorPipeline:
    """Main pipeline orchestrating the K-Factor optimization process."""
    
    def __init__(self, input_dir: str = INPUT_DIR, output_dir: str = OUTPUT_DIR):
        self.input_dir = input_dir
        self.output_dir = output_dir
        
        # Initialize components
        self.data_loader = DataLoader(input_dir)
        self.interval_builder = IntervalBuilder()
        self.kfactor_calculator = KFactorCalculator()
        self.governance_engine = GovernanceEngine()
        self.outputs_writer = OutputsWriter(output_dir)
        
        # Pipeline state
        self.customer_fuel = None
        self.delivery_tickets = None
        self.degree_days = None
        self.intervals = None
        self.interval_k_factors = None
        self.customer_k_factors = None
        self.variance_data = None
        self.governed_data = None
        self.auto_apply_data = None
        
    def run_pipeline(self) -> Dict[str, any]:
        """
        Execute the complete 8-step K-Factor optimization pipeline.
        
        Returns:
            Dictionary with pipeline results and statistics
        """
        logger.info("Starting FoxFuel K-Factor Optimization Pipeline")
        logger.info("=" * 60)
        
        try:
            # Step 1: Clean Delivery Tickets
            logger.info("Step 1: Loading and validating input data...")
            self.customer_fuel, self.delivery_tickets, self.degree_days = self.data_loader.load_all_data()
            
            # Step 2: Build Intervals
            logger.info("Step 2: Building delivery intervals...")
            self.intervals = self.interval_builder.build_intervals(
                self.customer_fuel, self.delivery_tickets, self.degree_days
            )
            
            # Step 3: Filter Valid Intervals
            logger.info("Step 3: Filtering valid intervals...")
            self.intervals = self.interval_builder.filter_valid_intervals(self.intervals)
            
            if len(self.intervals) == 0:
                logger.error("No valid intervals found. Pipeline cannot continue.")
                return self._create_error_result("No valid intervals found")
            
            # Step 4: Calculate Interval K-Factors
            logger.info("Step 4: Calculating interval K-factors...")
            self.interval_k_factors = self.kfactor_calculator.calculate_interval_k_factors(self.intervals)
            
            # Step 5: Weighted K by Customer
            logger.info("Step 5: Calculating weighted K-factors by customer...")
            self.customer_k_factors = self.kfactor_calculator.calculate_weighted_k_by_customer(
                self.interval_k_factors
            )
            
            # Step 6: Apply Governance
            logger.info("Step 6: Applying governance rules...")
            self.variance_data = self.kfactor_calculator.calculate_variance(
                self.customer_fuel, self.customer_k_factors
            )
            self.governed_data = self.governance_engine.apply_governance(self.variance_data)
            
            # Step 7: Apply K This Week
            logger.info("Step 7: Generating Apply_K_ThisWeek.csv...")
            self.auto_apply_data = self.governance_engine.filter_for_auto_apply(self.governed_data)
            apply_file = self.outputs_writer.write_apply_k_this_week(self.auto_apply_data)
            
            # Step 8: K Review Queue
            logger.info("Step 8: Generating K_Review_Queue.xlsx...")
            review_file = self.outputs_writer.write_k_review_queue(self.governed_data)
            
            # Generate results summary
            results = self._create_success_result(apply_file, review_file)
            
            logger.info("=" * 60)
            logger.info("Pipeline completed successfully!")
            logger.info(f"Apply_K_ThisWeek.csv: {apply_file}")
            logger.info(f"K_Review_Queue.xlsx: {review_file}")
            
            return results
            
        except Exception as e:
            logger.error(f"Pipeline failed with error: {str(e)}")
            return self._create_error_result(str(e))
    
    def _create_success_result(self, apply_file: Path, review_file: Path) -> Dict[str, any]:
        """Create success result dictionary."""
        
        # Get summary statistics
        calc_stats = self.kfactor_calculator.get_summary_statistics(self.variance_data)
        gov_stats = self.governance_engine.get_governance_summary(self.governed_data)
        
        return {
            'status': 'success',
            'timestamp': datetime.now().isoformat(),
            'files': {
                'apply_k_this_week': str(apply_file),
                'k_review_queue': str(review_file)
            },
            'statistics': {
                'calculation_stats': calc_stats,
                'governance_stats': gov_stats,
                'total_customers': len(self.customer_fuel) if self.customer_fuel is not None else 0,
                'valid_intervals': len(self.intervals) if self.intervals is not None else 0,
                'auto_apply_customers': len(self.auto_apply_data) if self.auto_apply_data is not None else 0
            }
        }
    
    def _create_error_result(self, error_message: str) -> Dict[str, any]:
        """Create error result dictionary."""
        return {
            'status': 'error',
            'timestamp': datetime.now().isoformat(),
            'error': error_message,
            'files': None,
            'statistics': None
        }
    
    def get_pipeline_summary(self) -> str:
        """
        Get a human-readable summary of the pipeline execution.
        
        Returns:
            Formatted summary string
        """
        if self.governed_data is None:
            return "Pipeline not yet executed."
        
        stats = self.governance_engine.get_governance_summary(self.governed_data)
        
        summary = f"""
FoxFuel K-Factor Optimization Summary
=====================================
Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

Total Customers Processed: {stats.get('total_customers', 0)}
Auto-Apply Eligible: {stats.get('auto_apply_eligible', 0)}
Manual Review Required: {stats.get('manual_review_required', 0)}

Status Breakdown:
- High Variance: {stats.get('status_breakdown', {}).get('HIGH_VARIANCE', 0)}
- Low Confidence: {stats.get('status_breakdown', {}).get('LOW_CONFIDENCE', 0)}
- Insufficient Data: {stats.get('status_breakdown', {}).get('INSUFFICIENT_DATA', 0)}
- Approved: {stats.get('status_breakdown', {}).get('APPROVED', 0)}

Governance Applied:
- Max Increase Cap: {stats.get('max_increase_applied', 0)}
- Max Decrease Cap: {stats.get('max_decrease_applied', 0)}
- Total Capped: {stats.get('capped_customers', 0)}

Average Final Variance: {stats.get('avg_final_variance', 0):.2f}%
"""
        return summary
