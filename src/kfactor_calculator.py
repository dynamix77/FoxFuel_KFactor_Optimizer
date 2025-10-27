"""
K-Factor calculation module for the FoxFuel K-Factor Optimizer.
Calculates interval-based K-factors and weighted averages per customer.
"""

import pandas as pd
import numpy as np
from typing import Tuple

from .config import *
from .logger import get_logger

logger = get_logger()

class KFactorCalculator:
    """Calculates K-factors from delivery intervals."""
    
    def __init__(self):
        self.interval_k_factors = None
        self.customer_k_factors = None
        
    def calculate_interval_k_factors(self, intervals: pd.DataFrame) -> pd.DataFrame:
        """
        Calculate K-factor for each delivery interval.
        
        Args:
            intervals: DataFrame with delivery intervals
            
        Returns:
            DataFrame with interval K-factors
        """
        if intervals is None or len(intervals) == 0:
            logger.warning("No intervals provided for K-factor calculation")
            return pd.DataFrame()
        
        logger.info(f"Calculating K-factors for {len(intervals)} intervals...")
        
        # Calculate interval K-factor: K = Gallons / Degree Days Used
        intervals = intervals.copy()
        intervals['Interval K Factor'] = intervals['Total Gallons'] / intervals['Degree Days Used']
        
        # Handle any invalid calculations
        invalid_k = intervals['Interval K Factor'].isna() | (intervals['Interval K Factor'] <= 0)
        if invalid_k.any():
            logger.warning(f"Found {invalid_k.sum()} invalid interval K-factors")
            intervals = intervals[~invalid_k]
        
        self.interval_k_factors = intervals
        
        logger.info(f"Calculated K-factors for {len(intervals)} valid intervals")
        return intervals
    
    def calculate_weighted_k_by_customer(self, interval_k_factors: pd.DataFrame) -> pd.DataFrame:
        """
        Calculate weighted K-factor for each customer based on gallons delivered.
        
        Args:
            interval_k_factors: DataFrame with interval K-factors
            
        Returns:
            DataFrame with customer-level weighted K-factors
        """
        if interval_k_factors is None or len(interval_k_factors) == 0:
            logger.warning("No interval K-factors provided for customer calculation")
            return pd.DataFrame()
        
        logger.info("Calculating weighted K-factors by customer...")
        
        # Group by customer and calculate weighted average
        customer_stats = interval_k_factors.groupby('Customer Number').agg({
            'Total Gallons': ['sum', 'count'],
            'Interval K Factor': lambda x: np.average(x, weights=interval_k_factors.loc[x.index, 'Total Gallons']),
            'Degree Days Used': 'sum',
            'Usable Size': 'first'
        }).round(4)
        
        # Flatten column names
        customer_stats.columns = ['Total Gallons', 'Interval Count', 'Weighted K Factor', 'Total Degree Days', 'Usable Size']
        
        # Reset index to make Customer Number a column
        customer_stats = customer_stats.reset_index()
        
        self.customer_k_factors = customer_stats
        
        logger.info(f"Calculated weighted K-factors for {len(customer_stats)} customers")
        return customer_stats
    
    def calculate_variance(self, customer_fuel: pd.DataFrame, customer_k_factors: pd.DataFrame) -> pd.DataFrame:
        """
        Calculate variance between weighted K and winter K for each customer.
        
        Args:
            customer_fuel: Customer fuel DataFrame with Winter K values
            customer_k_factors: Customer K-factors DataFrame
            
        Returns:
            DataFrame with variance calculations
        """
        logger.info("Calculating K-factor variance...")
        
        # Merge customer fuel with calculated K-factors
        merged = customer_k_factors.merge(
            customer_fuel[['Customer Number', 'K Factor - Winter', 'K Factor']], 
            on='Customer Number', 
            how='inner'
        )
        
        # Calculate variance percentage (using Winter K-factor as baseline)
        merged['Variance Percent'] = ((merged['Weighted K Factor'] - merged['K Factor - Winter']) / merged['K Factor - Winter']) * 100
        
        # Calculate confidence score based on interval count and total gallons
        # More intervals and more gallons = higher confidence
        max_intervals = merged['Interval Count'].max()
        max_gallons = merged['Total Gallons'].max()
        
        if max_intervals > 0 and max_gallons > 0:
            merged['Confidence'] = (
                (merged['Interval Count'] / max_intervals) * 0.5 +
                (merged['Total Gallons'] / max_gallons) * 0.5
            ).round(3)
        else:
            merged['Confidence'] = 0.0
        
        # Determine status based on variance and confidence
        merged['Status'] = 'APPROVED'
        merged.loc[abs(merged['Variance Percent']) > VAR_THRESHOLD_PCT * 100, 'Status'] = 'HIGH_VARIANCE'
        merged.loc[merged['Confidence'] < CONFIDENCE_THRESHOLD, 'Status'] = 'LOW_CONFIDENCE'
        merged.loc[merged['Interval Count'] < MIN_INTERVALS, 'Status'] = 'INSUFFICIENT_DATA'
        
        logger.info(f"Calculated variance for {len(merged)} customers")
        logger.info(f"Status breakdown: {merged['Status'].value_counts().to_dict()}")
        
        return merged
    
    def get_summary_statistics(self, variance_data: pd.DataFrame) -> dict:
        """
        Get summary statistics for the K-factor calculations.
        
        Args:
            variance_data: DataFrame with variance calculations
            
        Returns:
            Dictionary with summary statistics
        """
        if variance_data is None or len(variance_data) == 0:
            return {}
        
        stats = {
            'total_customers': len(variance_data),
            'approved_customers': len(variance_data[variance_data['Status'] == 'APPROVED']),
            'high_variance_customers': len(variance_data[variance_data['Status'] == 'HIGH_VARIANCE']),
            'low_confidence_customers': len(variance_data[variance_data['Status'] == 'LOW_CONFIDENCE']),
            'insufficient_data_customers': len(variance_data[variance_data['Status'] == 'INSUFFICIENT_DATA']),
            'avg_variance': variance_data['Variance Percent'].mean(),
            'avg_confidence': variance_data['Confidence'].mean(),
            'total_intervals': variance_data['Interval Count'].sum(),
            'total_gallons': variance_data['Total Gallons'].sum()
        }
        
        return stats
