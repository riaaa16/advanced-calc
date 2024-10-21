"""
Test Module for SingletonCalculator

This module contains tests for the SingletonCalculator class, focusing on
its ability to perform operations while maintaining a history of calculations.
It ensures that the history is correctly updated after each operation.
"""

import pytest
from app.operations import Addition, Subtraction
from app.singleton_calc import SingletonCalculator


# Parameterized test for performing operations
@pytest.mark.parametrize("operation, a, b", [
    (Addition(), 1, 2),
    (Addition(), 5.5, 4.5),
    (Subtraction(), 0, 0),
])
def test_history(operation, a, b):
    """Test that history is correctly updated after operations."""
    # Create a new instance of SingletonCalculator
    calculator = SingletonCalculator()
    calculator.get_history().clear()  # Clear the history before the test

    calculator.perform_operation(operation, a, b)
    history = calculator.get_history()

    assert len(history) == 1  # Ensure history has one entry
    assert history[0].operand1 == a
    assert history[0].operand2 == b
    assert history[0].operation.__class__.__name__.lower() == operation.__class__.__name__.lower()
