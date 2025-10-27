"""
Configuration parameters for the FoxFuel K-Factor Optimizer.
Contains all governance rules and business parameters.
"""

# Governance Parameters (aligned with Ignite and heating oil industry)
MAX_INCREASE = 0.15  # 15% maximum increase cap (conservative for heating oil)
MAX_DECREASE = 0.30  # 30% maximum decrease cap (conservative for heating oil)
CAP_PCT = 0.25  # ±25% overall variance boundary (realistic for heating oil)
VAR_THRESHOLD_PCT = 0.10  # 10% review trigger threshold
MIN_INTERVALS = 3  # Minimum valid intervals per customer
CONFIDENCE_THRESHOLD = 0.80  # 80% confidence minimum for auto-apply (realistic threshold)
MIN_INTERVAL_DAYS = 21  # Minimum interval day count
FULL_THRESHOLD = 0.90  # 90% of usable size for "full fill"
SUMMER_MULTIPLIER = 1.2  # Seasonal adjustment factor (summer heating reduction)

# File Configuration
INPUT_DIR = "data/inputs"
OUTPUT_DIR = "data/outputs"
CSV_ENCODING = "utf-8"
# DATE_FORMAT removed - using pandas auto-detection for Ignite formats

# CSV File Patterns
CUSTOMER_FUEL_PATTERN = "03_*.csv"
DELIVERY_TICKETS_PATTERN = "04_*.csv"
DEGREE_DAY_PATTERN = "06_*.csv"

# Required Columns (ignoring Column A) - Winter/Summer only
CUSTOMER_FUEL_COLUMNS = [
    "Customer Number", "Usable Size", "K Factor", "Zone - Fuel", 
    "Automatic Delivery", "K Factor - Winter", "K Factor - Summer"
]

DELIVERY_TICKETS_COLUMNS = [
    "Customer Number", "Transaction Date", "Transaction Type", 
    "Quantity", "% Full", "PIDCustomerFuel1"
]

DEGREE_DAY_COLUMNS = [
    "DDay Area", "DDay Date", "Heat Only DDays"
]

# Validation Rules
MIN_USABLE_SIZE = 0
MIN_K_FACTOR = 0
MIN_QUANTITY = -1000  # Allow negative quantities (returns/adjustments)
MIN_PERCENT_FULL = 0
MAX_PERCENT_FULL = 100
MIN_DEGREE_DAYS = 0

# Transaction Type Filter
VALID_TRANSACTION_TYPE = "Delivery"
