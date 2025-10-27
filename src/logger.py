"""
Logging configuration for the FoxFuel K-Factor Optimizer.
Uses loguru for clean, readable output.
"""

from loguru import logger
import sys
from pathlib import Path

def setup_logger(log_level="INFO", log_file=None):
    """
    Configure logging for the K-Factor Optimizer.
    
    Args:
        log_level: Logging level (DEBUG, INFO, WARNING, ERROR)
        log_file: Optional log file path
    """
    # Remove default handler
    logger.remove()
    
    # Console output with colors
    logger.add(
        sys.stdout,
        level=log_level,
        format="<green>{time:HH:mm:ss}</green> | <level>{level: <8}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>",
        colorize=True
    )
    
    # Optional file logging
    if log_file:
        log_path = Path(log_file)
        log_path.parent.mkdir(parents=True, exist_ok=True)
        logger.add(
            log_file,
            level="DEBUG",
            format="{time:YYYY-MM-DD HH:mm:ss} | {level: <8} | {name}:{function}:{line} - {message}",
            rotation="1 week",
            retention="4 weeks"
        )
    
    return logger

def get_logger():
    """Get the configured logger instance."""
    return logger
