"""Testing app.operation_factory."""

import pytest
from app.log_config import setup_logging
from app.operation_factory import OperationFactory
from app.operations import Addition, Subtraction, Multiplication, Division

# Set up logging configuration for testing
setup_logging()

@pytest.mark.parametrize("operation_name, expected_class", [
    ("add", Addition),
    ("subtract", Subtraction),
    ("multiply", Multiplication),
    ("divide", Division),
    ("invalid", None),  # Testing invalid operation
    ("ADD", Addition),   # Testing case insensitivity
    ("Subtract", Subtraction),
    ("MULTIPLY", Multiplication),
    ("DiViDe", Division),
])
def test_create_operations(operation_name, expected_class):
    """Test creating operations using the factory."""
    operation = OperationFactory.create_operation(operation_name)

    if expected_class is None:
        assert operation is None, f"Expected None for operation '{operation_name}'"
    else:
        assert isinstance(operation, expected_class), (
            f"Expected an instance of {expected_class.__name__} for operation '{operation_name}'"
        )
