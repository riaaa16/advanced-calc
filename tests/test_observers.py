"""
Test Module for Calculator with Observer

This module contains tests for the CalculatorWithObserver class, specifically 
focusing on the observer pattern implementation. It ensures that observers are 
notified of new calculations and that appropriate logging occurs.
"""

import logging
from app.log_config import setup_logging  # Adjust the import according to your structure
from app.observer import CalculatorWithObserver, HistoryObserver
from app.operations import Addition  # Assuming Addition is the operation you want to test

# Setup logging before tests
setup_logging()

def test_update_logging(caplog):
    """Test that the observer logs a message when notified of a new calculation."""
    # Create instances of the calculator and observer
    calculator = CalculatorWithObserver()
    observer = HistoryObserver()
    calculator.add_observer(observer)

    # Perform a calculation to ensure the observer is notified
    calculation = calculator.perform_operation(Addition(), 2, 3)

    # Capture log messages when the update method is called
    with caplog.at_level(logging.INFO):
        observer.update(calculation)  # Directly call update with the calculation

    # Verify that the log message was created
    assert len(caplog.records) == 1
    assert "Observer: New calculation added" in caplog.text
    assert caplog.records[0].levelname == "INFO"
