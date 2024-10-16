import pytest
from app.operations import Addition, Subtraction, Multiplication, Division
from app.calculation import Calculation  # Adjust the import path as necessary

# Fixtures for operation instances
@pytest.fixture
def addition_operation():
    return Addition()

@pytest.fixture
def subtraction_operation():
    return Subtraction()

@pytest.fixture
def multiplication_operation():
    return Multiplication()

@pytest.fixture
def division_operation():
    return Division()

# Parameterized test for the __repr__ method
@pytest.mark.parametrize("operation, operand1, operand2, expected_repr", [
    (Addition(), 1, 2, "Calculation(1, addition, 2)"),
    (Subtraction(), 5, 3, "Calculation(5, subtraction, 3)"),
    (Multiplication(), 3, 4, "Calculation(3, multiplication, 4)"),
    (Division(), 8, 2, "Calculation(8, division, 2)"),
])
def test_calculation_repr(operation, operand1, operand2, expected_repr):
    calc = Calculation(operation, operand1, operand2)
    assert repr(calc) == expected_repr

# Parameterized test for the __str__ method
@pytest.mark.parametrize("operation, operand1, operand2, expected_str", [
    (Addition(), 1, 2, "1 addition 2 = 3"),
    (Subtraction(), 5, 3, "5 subtraction 3 = 2"),
    (Multiplication(), 3, 4, "3 multiplication 4 = 12"),
    (Division(), 8, 2, "8 division 2 = 4.0"),  # Adjust according to your implementation
])
def test_calculation_str(operation, operand1, operand2, expected_str):
    calc = Calculation(operation, operand1, operand2)
    assert str(calc) == expected_str

# Test for division by zero
def test_division_by_zero(division_operation):
    calc_div_zero = Calculation(division_operation, 5, 0)
    with pytest.raises(ValueError, match="Division by zero is not allowed."):
        str(calc_div_zero)  # Trigger the __str__ method to perform the calculation
