# logging_config.py
import logging

# ==============================================================================
# SETUP LOGGING CONFIGURATION
# ==============================================================================

# Configure the logging settings for the application.
# Logging is crucial for tracking events and diagnosing issues in applications.
class LoggerConfig:
    @staticmethod
    def setup_logging():
        logging.basicConfig(
            filename='calculator.log', # Specifies the file to write log messages to.
            level=logging.DEBUG, # Sets the logging level to DEBUG; captures all levels (DEBUG, INFO, WARNING, ERROR, CRITICAL).
            format='%(asctime)s - %(levelname)s - %(message)s' # Defines the format of the log messages.
            # Format placeholders:
            # %(asctime)s - Timestamp of the log entry.
            # %(levelname)s - Severity level of the log message.
            # %(message)s - The actual log message.
        )
