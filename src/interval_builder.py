"""
Interval building module for the FoxFuel K-Factor Optimizer.
Creates delivery intervals between full fills and joins with degree days.
"""

import pandas as pd
from typing import Tuple
from datetime import datetime, timedelta

from .config import *
from .logger import get_logger

logger = get_logger()

class IntervalBuilder:
    """Builds delivery intervals between full fills and calculates degree days used."""
    
    def __init__(self):
        self.intervals = None
        
    def build_intervals(self, customer_fuel: pd.DataFrame, delivery_tickets: pd.DataFrame, 
                       degree_days: pd.DataFrame) -> pd.DataFrame:
        """
        Build delivery intervals between consecutive full fills.
        
        Args:
            customer_fuel: Customer fuel information DataFrame
            delivery_tickets: Delivery tickets DataFrame
            degree_days: Degree days DataFrame
            
        Returns:
            DataFrame with delivery intervals
        """
        logger.info("Building delivery intervals...")
        
        # Merge delivery tickets with customer fuel to get usable size
        merged = delivery_tickets.merge(
            customer_fuel[['Customer Number', 'Usable Size']], 
            on='Customer Number', 
            how='inner'
        )
        
        # Calculate full fill threshold
        merged['Full Fill Threshold'] = merged['Usable Size'] * FULL_THRESHOLD
        
        # Identify full fills - use quantity vs usable size since Ignite % Full is unreliable
        merged['Is Full Fill'] = merged['Quantity'] >= merged['Full Fill Threshold']
        
        # Sort by customer and date
        merged = merged.sort_values(['Customer Number', 'Transaction Date'])
        
        intervals = []
        
        # Process each customer
        for customer in merged['Customer Number'].unique():
            customer_data = merged[merged['Customer Number'] == customer].copy()
            customer_intervals = self._build_customer_intervals(customer_data, degree_days)
            intervals.extend(customer_intervals)
        
        self.intervals = pd.DataFrame(intervals)
        
        if len(self.intervals) > 0:
            logger.info(f"Built {len(self.intervals)} delivery intervals")
        else:
            logger.warning("No valid intervals found")
            
        return self.intervals
    
    def _build_customer_intervals(self, customer_data: pd.DataFrame, 
                                degree_days: pd.DataFrame) -> list:
        """
        Build intervals for a single customer.
        
        Args:
            customer_data: Delivery data for one customer
            degree_days: Degree days DataFrame
            
        Returns:
            List of interval dictionaries
        """
        intervals = []
        full_fills = customer_data[customer_data['Is Full Fill']].copy()
        
        if len(full_fills) < 2:
            return intervals
        
        # Create intervals between consecutive full fills
        for i in range(len(full_fills) - 1):
            start_delivery = full_fills.iloc[i]
            end_delivery = full_fills.iloc[i + 1]
            
            # Calculate degree days between deliveries
            start_date = start_delivery['Transaction Date']
            end_date = end_delivery['Transaction Date']
            
            # Get degree days for this interval
            interval_ddays = degree_days[
                (degree_days['DDay Date'] > start_date) & 
                (degree_days['DDay Date'] <= end_date)
            ]
            
            if len(interval_ddays) == 0:
                continue
            
            # Calculate total gallons delivered in this interval
            interval_deliveries = customer_data[
                (customer_data['Transaction Date'] > start_date) & 
                (customer_data['Transaction Date'] <= end_date)
            ]
            
            total_gallons = interval_deliveries['Quantity'].sum()
            
            # Calculate degree days used in this interval (difference between start and end)
            if len(interval_ddays) >= 2:
                # Use difference between first and last degree day values
                degree_days_used = interval_ddays['Heat Only DDays'].iloc[-1] - interval_ddays['Heat Only DDays'].iloc[0]
            else:
                # Fallback: use the single value if only one day
                degree_days_used = interval_ddays['Heat Only DDays'].iloc[0]
            
            # Only include intervals with sufficient data
            if degree_days_used > 0 and total_gallons > 0:
                interval = {
                    'Customer Number': start_delivery['Customer Number'],
                    'Start Date': start_date,
                    'End Date': end_date,
                    'Start Delivery Gallons': start_delivery['Quantity'],
                    'End Delivery Gallons': end_delivery['Quantity'],
                    'Total Gallons': total_gallons,
                    'Degree Days Used': degree_days_used,
                    'Interval Days': (end_date - start_date).days,
                    'Usable Size': start_delivery['Usable Size']
                }
                intervals.append(interval)
        
        return intervals
    
    def filter_valid_intervals(self, intervals: pd.DataFrame) -> pd.DataFrame:
        """
        Apply minimum day and gallon size rules to filter valid intervals.
        
        Args:
            intervals: Raw intervals DataFrame
            
        Returns:
            Filtered intervals DataFrame
        """
        if intervals is None or len(intervals) == 0:
            return pd.DataFrame()
        
        logger.info(f"Filtering {len(intervals)} intervals...")
        
        # Apply minimum interval days rule
        valid_intervals = intervals[intervals['Interval Days'] >= MIN_INTERVAL_DAYS].copy()
        
        logger.info(f"After minimum days filter: {len(valid_intervals)} intervals")
        
        # Additional filtering could be added here (e.g., minimum gallons)
        
        self.intervals = valid_intervals
        return valid_intervals
    
    def get_customer_summary(self) -> pd.DataFrame:
        """
        Get summary statistics by customer.
        
        Returns:
            DataFrame with customer-level statistics
        """
        if self.intervals is None or len(self.intervals) == 0:
            return pd.DataFrame()
        
        summary = self.intervals.groupby('Customer Number').agg({
            'Total Gallons': 'sum',
            'Degree Days Used': 'sum',
            'Interval Days': 'sum',
            'Interval Days': 'count',  # Number of intervals
            'Usable Size': 'first'
        }).rename(columns={'Interval Days': 'Interval Count'})
        
        return summary
