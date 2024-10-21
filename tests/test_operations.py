"""
Test Module for Arithmetic Operations

This module contains tests for basic arithmetic operations including addition,
subtraction, multiplication, and division. It ensures that each operation
functions correctly and that logging is handled properly, especially for 
invalid inputs and errors.
"""

import logging
import pytest

from app.log_config import setup_logging  # Import your logging configuration
from app.operations import Addition, Subtraction, Multiplication, Division

# Set up logging configuration
setup_logging()

# Parameterized tests for Addition
@pytest.mark.parametrize("a, b, expected", [
    (1, 2, 3),                # Normal case
    (0, 0, 0),                # Edge case with zeros
    (-1, 1, 0),               # Negative and positive
    (1e6, 1e6, 2e6),          # Large numbers
])
def test_addition(a, b, expected):
    """Test the Addition operation with various inputs."""
    addition = Addition()
    assert addition.calculate(a, b) == expected

# Parameterized tests for Subtraction
@pytest.mark.parametrize("a, b, expected", [
    (3, 2, 1),                # Normal case
    (0, 0, 0),                # Edge case with zeros
    (1, 2, -1),               # Negative result
    (-1, -1, 0),              # Subtracting negatives
])
def test_subtraction(a, b, expected):
    """Test the Subtraction operation with various inputs."""
    subtraction = Subtraction()
    assert subtraction.calculate(a, b) == expected

# Parameterized tests for Multiplication
@pytest.mark.parametrize("a, b, expected", [
    (2, 3, 6),                # Normal case
    (0, 5, 0),                # Zero multiplicand
    (1, 0, 0),                # Zero multiplier
    (-2, 3, -6),              # Negative number
])
def test_multiplication(a, b, expected):
    """Test the Multiplication operation with various inputs."""
    multiplication = Multiplication()
    assert multiplication.calculate(a, b) == expected

# Parameterized tests for Division
@pytest.mark.parametrize("a, b, expected", [
    (6, 2, 3),                # Normal case
    (0, 1, 0),                # Edge case: zero numerator
    (-6, 2, -3),              # Negative result
    (1e6, 1e5, 10),           # Large numbers
])
def test_division(a, b, expected):
    """Test the Division operation with various inputs."""
    division = Division()
    assert division.calculate(a, b) == expected

def test_division_by_zero():
    """Test Division operation raises error on division by zero."""
    division = Division()
    with pytest.raises(ValueError, match="Division by zero is not allowed."):
        division.calculate(1, 0)

# Parameterized tests for invalid inputs
@pytest.mark.parametrize("a, b", [
    (None, 1),                # None as input
    ("string", 1),            # String as input
    (1, "string"),            # String as input
    ([], 1),                  # List as input
    (1, {}),                  # Dictionary as input
])
def test_invalid_inputs(a, b):
    """Test operations raise error on invalid inputs."""
    addition = Addition()
    with pytest.raises(ValueError, match="Both inputs must be numbers."):
        addition.calculate(a, b)

    with pytest.raises(ValueError, match="Both inputs must be numbers."):
        Subtraction().calculate(a, b)

    with pytest.raises(ValueError, match="Both inputs must be numbers."):
        Multiplication().calculate(a, b)

    with pytest.raises(ValueError, match="Both inputs must be numbers."):
        Division().calculate(a, b)

# Test to check logging for successful operations
def test_logging(caplog):
    """Test logging for successful Addition operation."""
    addition = Addition()
    with caplog.at_level(logging.INFO):
        addition.calculate(2, 3)  # Removed the unused variable
    assert "Operation performed: 2 and 3 -> Result: 5" in caplog.text

# Test to check logging for invalid inputs
def test_logging_invalid_input(caplog):
    """Test logging for invalid input in Addition operation."""
    addition = Addition()
    with caplog.at_level(logging.ERROR):
        with pytest.raises(ValueError):
            addition.calculate("string", 1)
    assert "Invalid input: string, 1 (Inputs must be numbers)" in caplog.text
