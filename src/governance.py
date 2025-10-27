"""
Governance module for the FoxFuel K-Factor Optimizer.
Applies caps, thresholds, and confidence filtering to K-factor changes.
"""

import pandas as pd
import numpy as np
from typing import Tuple

from .config import *
from .logger import get_logger

logger = get_logger()

class GovernanceEngine:
    """Applies governance rules to K-factor changes."""
    
    def __init__(self):
        self.governed_k_factors = None
        
    def apply_governance(self, variance_data: pd.DataFrame) -> pd.DataFrame:
        """
        Apply governance rules to K-factor changes.
        
        Args:
            variance_data: DataFrame with variance calculations
            
        Returns:
            DataFrame with governed K-factors
        """
        if variance_data is None or len(variance_data) == 0:
            logger.warning("No variance data provided for governance")
            return pd.DataFrame()
        
        logger.info(f"Applying governance rules to {len(variance_data)} customers...")
        
        governed = variance_data.copy()
        
        # Calculate proposed new K-factor
        governed['Proposed K Factor'] = governed['Weighted K Factor']
        
        # Apply maximum increase cap
        max_increase_limit = governed['K Factor - Winter'] * (1 + MAX_INCREASE)
        increase_cap_applied = governed['Proposed K Factor'] > max_increase_limit
        governed.loc[increase_cap_applied, 'Proposed K Factor'] = max_increase_limit
        
        if increase_cap_applied.any():
            logger.info(f"Applied maximum increase cap to {increase_cap_applied.sum()} customers")
        
        # Apply maximum decrease cap
        max_decrease_limit = governed['K Factor - Winter'] * (1 - MAX_DECREASE)
        decrease_cap_applied = governed['Proposed K Factor'] < max_decrease_limit
        governed.loc[decrease_cap_applied, 'Proposed K Factor'] = max_decrease_limit
        
        if decrease_cap_applied.any():
            logger.info(f"Applied maximum decrease cap to {decrease_cap_applied.sum()} customers")
        
        # Apply overall variance boundary
        variance_boundary_upper = governed['K Factor - Winter'] * (1 + CAP_PCT)
        variance_boundary_lower = governed['K Factor - Winter'] * (1 - CAP_PCT)
        
        upper_bound_applied = governed['Proposed K Factor'] > variance_boundary_upper
        lower_bound_applied = governed['Proposed K Factor'] < variance_boundary_lower
        
        governed.loc[upper_bound_applied, 'Proposed K Factor'] = variance_boundary_upper[upper_bound_applied]
        governed.loc[lower_bound_applied, 'Proposed K Factor'] = variance_boundary_lower[lower_bound_applied]
        
        if upper_bound_applied.any() or lower_bound_applied.any():
            logger.info(f"Applied variance boundary to {upper_bound_applied.sum() + lower_bound_applied.sum()} customers")
        
        # Calculate final variance after governance
        governed['Final Variance Percent'] = ((governed['Proposed K Factor'] - governed['K Factor - Winter']) / governed['K Factor - Winter']) * 100
        
        # Update status based on final governance
        governed['Final Status'] = governed['Status'].copy()
        
        # Mark customers that hit governance limits
        governed.loc[increase_cap_applied, 'Final Status'] = 'CAPPED_INCREASE'
        governed.loc[decrease_cap_applied, 'Final Status'] = 'CAPPED_DECREASE'
        governed.loc[upper_bound_applied, 'Final Status'] = 'CAPPED_UPPER_BOUND'
        governed.loc[lower_bound_applied, 'Final Status'] = 'CAPPED_LOWER_BOUND'
        
        # Round to 4 decimal places
        governed['Proposed K Factor'] = governed['Proposed K Factor'].round(4)
        governed['Final Variance Percent'] = governed['Final Variance Percent'].round(2)
        
        self.governed_k_factors = governed
        
        logger.info("Governance rules applied successfully")
        logger.info(f"Final status breakdown: {governed['Final Status'].value_counts().to_dict()}")
        
        return governed
    
    def filter_for_auto_apply(self, governed_data: pd.DataFrame) -> pd.DataFrame:
        """
        Filter customers eligible for automatic K-factor application.
        
        Args:
            governed_data: DataFrame with governed K-factors
            
        Returns:
            DataFrame with customers eligible for auto-apply
        """
        if governed_data is None or len(governed_data) == 0:
            return pd.DataFrame()
        
        logger.info("Filtering customers for auto-apply...")
        
        # Customers eligible for auto-apply must meet confidence threshold
        auto_apply = governed_data[
            (governed_data['Confidence'] >= CONFIDENCE_THRESHOLD) &
            (governed_data['Interval Count'] >= MIN_INTERVALS) &
            (governed_data['Final Status'].isin(['APPROVED', 'CAPPED_INCREASE', 'CAPPED_DECREASE', 
                                                'CAPPED_UPPER_BOUND', 'CAPPED_LOWER_BOUND']))
        ].copy()
        
        logger.info(f"{len(auto_apply)} customers eligible for auto-apply")
        logger.info(f"{len(governed_data) - len(auto_apply)} customers require manual review")
        
        return auto_apply
    
    def get_review_queue(self, governed_data: pd.DataFrame) -> pd.DataFrame:
        """
        Get customers that require manual review.
        
        Args:
            governed_data: DataFrame with governed K-factors
            
        Returns:
            DataFrame with customers requiring review
        """
        if governed_data is None or len(governed_data) == 0:
            return pd.DataFrame()
        
        # Customers requiring review
        review_queue = governed_data[
            (governed_data['Confidence'] < CONFIDENCE_THRESHOLD) |
            (governed_data['Interval Count'] < MIN_INTERVALS) |
            (governed_data['Final Status'].isin(['HIGH_VARIANCE', 'LOW_CONFIDENCE', 'INSUFFICIENT_DATA']))
        ].copy()
        
        # Sort by priority (high variance, low confidence, insufficient data)
        priority_order = {
            'HIGH_VARIANCE': 1,
            'LOW_CONFIDENCE': 2,
            'INSUFFICIENT_DATA': 3,
            'CAPPED_INCREASE': 4,
            'CAPPED_DECREASE': 4,
            'CAPPED_UPPER_BOUND': 4,
            'CAPPED_LOWER_BOUND': 4,
            'APPROVED': 5
        }
        
        review_queue['Priority'] = review_queue['Final Status'].map(priority_order)
        review_queue = review_queue.sort_values(['Priority', 'Final Variance Percent'], ascending=[True, False])
        
        return review_queue
    
    def get_governance_summary(self, governed_data: pd.DataFrame) -> dict:
        """
        Get summary of governance application.
        
        Args:
            governed_data: DataFrame with governed K-factors
            
        Returns:
            Dictionary with governance summary
        """
        if governed_data is None or len(governed_data) == 0:
            return {}
        
        summary = {
            'total_customers': len(governed_data),
            'auto_apply_eligible': len(self.filter_for_auto_apply(governed_data)),
            'manual_review_required': len(self.get_review_queue(governed_data)),
            'capped_customers': len(governed_data[governed_data['Final Status'].str.contains('CAPPED', na=False)]),
            'avg_final_variance': governed_data['Final Variance Percent'].mean(),
            'max_increase_applied': len(governed_data[governed_data['Final Status'] == 'CAPPED_INCREASE']),
            'max_decrease_applied': len(governed_data[governed_data['Final Status'] == 'CAPPED_DECREASE']),
            'status_breakdown': governed_data['Final Status'].value_counts().to_dict()
        }
        
        return summary
