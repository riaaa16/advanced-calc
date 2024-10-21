"""
Logging Configuration
- Sets up logging configuration.
"""

import logging


def setup_logging():
    """
    Set up the logging configuration.

    This function configures the logging settings for the application, 
    including the log file name, logging level, and message format.
    
    Logs are written to 'calculator.log' and the logging level is set 
    to DEBUG to capture all levels of log messages.
    """
    logging.basicConfig(
        filename='calculator.log',  # Specifies the file to write log messages to.
        level=logging.DEBUG,  # Sets the logging level to DEBUG; captures all levels.
        format='%(asctime)s - %(levelname)s - %(message)s'  # Formats log messages.
        # Format placeholders:
        # %(asctime)s - Timestamp of the log entry.
        # %(levelname)s - Severity level of the log message.
        # %(message)s - The actual log message.
    )
