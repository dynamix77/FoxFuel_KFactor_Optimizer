"""
Data loading and validation module for the FoxFuel K-Factor Optimizer.
Handles loading and validating the three CSV input files.
"""

import pandas as pd
from pathlib import Path
from datetime import datetime
from typing import Tuple, Dict, List
import glob

from .config import *
from .logger import get_logger

logger = get_logger()

class DataLoader:
    """Handles loading and validation of input CSV files."""
    
    def __init__(self, input_dir: str = INPUT_DIR):
        self.input_dir = Path(input_dir)
        self.customer_fuel = None
        self.delivery_tickets = None
        self.degree_days = None
        
    def find_latest_files(self) -> Dict[str, Path]:
        """
        Find the latest CSV files matching the required patterns.
        
        Returns:
            Dictionary mapping file type to Path object
        """
        files = {}
        
        # Find latest CustomerFuel file
        customer_files = glob.glob(str(self.input_dir / CUSTOMER_FUEL_PATTERN))
        if customer_files:
            files['customer_fuel'] = Path(max(customer_files, key=lambda x: Path(x).stat().st_mtime))
            logger.info(f"Found CustomerFuel file: {files['customer_fuel'].name}")
        
        # Find latest DeliveryTickets file
        delivery_files = glob.glob(str(self.input_dir / DELIVERY_TICKETS_PATTERN))
        if delivery_files:
            files['delivery_tickets'] = Path(max(delivery_files, key=lambda x: Path(x).stat().st_mtime))
            logger.info(f"Found DeliveryTickets file: {files['delivery_tickets'].name}")
        
        # Find latest DegreeDayValues file
        degree_files = glob.glob(str(self.input_dir / DEGREE_DAY_PATTERN))
        if degree_files:
            files['degree_days'] = Path(max(degree_files, key=lambda x: Path(x).stat().st_mtime))
            logger.info(f"Found DegreeDayValues file: {files['degree_days'].name}")
        
        return files
    
    def load_customer_fuel(self, file_path: Path) -> pd.DataFrame:
        """
        Load and validate CustomerFuel CSV file.
        
        Args:
            file_path: Path to the CustomerFuel CSV file
            
        Returns:
            Validated DataFrame
        """
        logger.info(f"Loading CustomerFuel from {file_path.name}")
        
        # Load CSV, skip first column (Column A)
        df = pd.read_csv(file_path, encoding=CSV_ENCODING, usecols=lambda x: x != 'Unnamed: 0')
        
        # Validate required columns
        missing_cols = set(CUSTOMER_FUEL_COLUMNS) - set(df.columns)
        if missing_cols:
            raise ValueError(f"Missing required columns in CustomerFuel: {missing_cols}")
        
        # Data type conversions
        df['Customer Number'] = df['Customer Number'].astype(str)
        df['Usable Size'] = pd.to_numeric(df['Usable Size'], errors='coerce')
        df['K Factor'] = pd.to_numeric(df['K Factor'], errors='coerce')
        df['Automatic Delivery'] = df['Automatic Delivery'].map({'TRUE': True, 'FALSE': False, True: True, False: False})
        
        # Convert seasonal K factors to numeric
        # Convert seasonal K-factor columns to numeric (Winter/Summer only)
        for col in ['K Factor - Winter', 'K Factor - Summer']:
            if col in df.columns:
                df[col] = pd.to_numeric(df[col], errors='coerce')
        
        # Validation rules
        invalid_size = df['Usable Size'] <= MIN_USABLE_SIZE
        if invalid_size.any():
            logger.warning(f"Found {invalid_size.sum()} customers with invalid usable size")
        
        invalid_k = df['K Factor'] < MIN_K_FACTOR
        if invalid_k.any():
            logger.warning(f"Found {invalid_k.sum()} customers with invalid K factor")
        
        # Filter valid records
        df = df[(df['Usable Size'] > MIN_USABLE_SIZE) & (df['K Factor'] >= MIN_K_FACTOR)]
        
        logger.info(f"Loaded {len(df)} valid customer fuel records")
        return df
    
    def load_delivery_tickets(self, file_path: Path) -> pd.DataFrame:
        """
        Load and validate DeliveryTickets CSV file.
        
        Args:
            file_path: Path to the DeliveryTickets CSV file
            
        Returns:
            Validated DataFrame
        """
        logger.info(f"Loading DeliveryTickets from {file_path.name}")
        
        # Load CSV, skip first column (Column A)
        df = pd.read_csv(file_path, encoding=CSV_ENCODING, usecols=lambda x: x != 'Unnamed: 0')
        
        # Validate required columns
        missing_cols = set(DELIVERY_TICKETS_COLUMNS) - set(df.columns)
        if missing_cols:
            raise ValueError(f"Missing required columns in DeliveryTickets: {missing_cols}")
        
        # Data type conversions
        df['Customer Number'] = df['Customer Number'].astype(str)
        # Handle Ignite date format: "12/12/23 3:28 PM" or "1/24/24 2:00 PM"
        df['Transaction Date'] = pd.to_datetime(df['Transaction Date'], errors='coerce')
        df['Quantity'] = pd.to_numeric(df['Quantity'], errors='coerce')
        # Handle Ignite % Full format: "0%" -> convert to numeric
        df['% Full'] = df['% Full'].str.replace('%', '').astype(float)
        
        # Filter for valid deliveries only
        df = df[df['Transaction Type'] == VALID_TRANSACTION_TYPE]
        
        # Validation rules
        invalid_quantity = df['Quantity'] <= MIN_QUANTITY
        if invalid_quantity.any():
            logger.warning(f"Found {invalid_quantity.sum()} invalid delivery quantities")
        
        invalid_percent = (df['% Full'] < MIN_PERCENT_FULL) | (df['% Full'] > MAX_PERCENT_FULL)
        if invalid_percent.any():
            logger.warning(f"Found {invalid_percent.sum()} invalid percent full values")
        
        invalid_date = df['Transaction Date'].isna()
        if invalid_date.any():
            logger.warning(f"Found {invalid_date.sum()} invalid transaction dates")
        
        # Filter valid records
        df = df[
            (df['Quantity'] > MIN_QUANTITY) &
            (df['% Full'] >= MIN_PERCENT_FULL) &
            (df['% Full'] <= MAX_PERCENT_FULL) &
            (df['Transaction Date'].notna())
        ]
        
        logger.info(f"Loaded {len(df)} valid delivery records")
        return df
    
    def load_degree_days(self, file_path: Path) -> pd.DataFrame:
        """
        Load and validate DegreeDayValues CSV file.
        
        Args:
            file_path: Path to the DegreeDayValues CSV file
            
        Returns:
            Validated DataFrame
        """
        logger.info(f"Loading DegreeDayValues from {file_path.name}")
        
        # Load CSV, skip first column (Column A)
        df = pd.read_csv(file_path, encoding=CSV_ENCODING, usecols=lambda x: x != 'Unnamed: 0')
        
        # Validate required columns
        missing_cols = set(DEGREE_DAY_COLUMNS) - set(df.columns)
        if missing_cols:
            raise ValueError(f"Missing required columns in DegreeDayValues: {missing_cols}")
        
        # Data type conversions
        # Handle Ignite date format: "1/1/22" 
        df['DDay Date'] = pd.to_datetime(df['DDay Date'], errors='coerce')
        df['Heat Only DDays'] = pd.to_numeric(df['Heat Only DDays'], errors='coerce')
        
        # Validation rules
        invalid_date = df['DDay Date'].isna()
        if invalid_date.any():
            logger.warning(f"Found {invalid_date.sum()} invalid degree day dates")
        
        invalid_ddays = df['Heat Only DDays'] < MIN_DEGREE_DAYS
        if invalid_ddays.any():
            logger.warning(f"Found {invalid_ddays.sum()} invalid degree day values")
        
        # Filter valid records
        df = df[
            (df['DDay Date'].notna()) &
            (df['Heat Only DDays'] >= MIN_DEGREE_DAYS)
        ]
        
        # Sort by date
        df = df.sort_values('DDay Date')
        
        logger.info(f"Loaded {len(df)} valid degree day records")
        return df
    
    def load_all_data(self) -> Tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
        """
        Load all three CSV files automatically.
        
        Returns:
            Tuple of (customer_fuel, delivery_tickets, degree_days) DataFrames
        """
        files = self.find_latest_files()
        
        if 'customer_fuel' not in files:
            raise FileNotFoundError(f"No CustomerFuel file found matching pattern {CUSTOMER_FUEL_PATTERN}")
        if 'delivery_tickets' not in files:
            raise FileNotFoundError(f"No DeliveryTickets file found matching pattern {DELIVERY_TICKETS_PATTERN}")
        if 'degree_days' not in files:
            raise FileNotFoundError(f"No DegreeDayValues file found matching pattern {DEGREE_DAY_PATTERN}")
        
        self.customer_fuel = self.load_customer_fuel(files['customer_fuel'])
        self.delivery_tickets = self.load_delivery_tickets(files['delivery_tickets'])
        self.degree_days = self.load_degree_days(files['degree_days'])
        
        logger.info("All data files loaded successfully")
        return self.customer_fuel, self.delivery_tickets, self.degree_days
