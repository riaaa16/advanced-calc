"""Testing app.operation_factory."""
import logging

import pytest

from app.log_config import setup_logging
from app.operation_factory import OperationFactory
from app.operations import Addition, Subtraction, Multiplication, Division

# Set up logging configuration for testing
setup_logging()

@pytest.fixture
def factory():
    """Fixture for the operation factory."""
    return OperationFactory


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
def test_create_operations(factory, operation_name, expected_class):
    """Test creating operations using the factory."""
    operation = factory.create_operation(operation_name)

    if expected_class is None:
        assert operation is None, f"Expected None for operation '{operation_name}'"
    else:
        assert isinstance(operation, expected_class), (
            f"Expected an instance of {expected_class.__name__} for operation '{operation_name}'"
        )
