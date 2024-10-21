"""
Unit Tests for Calculator Operations

This module tests the functionality of the Calculator class and its operations 
using the pytest framework. It includes tests for the __repr__ and __str__ 
methods, verifies arithmetic operations, and checks error handling for 
division by zero.
"""

import pytest
from app.operations import Addition, Subtraction, Multiplication, Division
from app.calculation import Calculation

# Parameterized test for the __repr__ method
@pytest.mark.parametrize("operation, operand1, operand2, expected_repr", [
    (Addition(), 1, 2, "Calculation(1, addition, 2)"),
    (Subtraction(), 5, 3, "Calculation(5, subtraction, 3)"),
    (Multiplication(), 3, 4, "Calculation(3, multiplication, 4)"),
    (Division(), 8, 2, "Calculation(8, division, 2)"),
])
def test_calculation_repr(operation, operand1, operand2, expected_repr):
    """Test the __repr__ method of Calculation."""
    calc = Calculation(operation, operand1, operand2)
    assert repr(calc) == expected_repr

# Parameterized test for the __str__ method
@pytest.mark.parametrize("operation, operand1, operand2, expected_str", [
    (Addition(), 1, 2, "1 addition 2 = 3"),
    (Subtraction(), 5, 3, "5 subtraction 3 = 2"),
    (Multiplication(), 3, 4, "3 multiplication 4 = 12"),
    (Division(), 8, 2, "8 division 2 = 4.0"),
])
def test_calculation_str(operation, operand1, operand2, expected_str):
    """Test the __str__ method of Calculation."""
    calc = Calculation(operation, operand1, operand2)
    assert str(calc) == expected_str

# Test for division by zero
def test_zero_division():
    """Test division by zero raises ValueError."""
    division_operation = Division()  # Create an instance of the Division operation
    calc_div_zero = Calculation(division_operation, 5, 0)
    with pytest.raises(ValueError, match="Division by zero is not allowed."):
        str(calc_div_zero)  # Trigger the __str__ method to perform the calculation
