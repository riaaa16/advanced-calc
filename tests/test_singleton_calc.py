import pytest
from app.operations import Addition, Subtraction
from app.singleton_calc import SingletonCalculator

@pytest.fixture(scope='function')
def singleton_calculator():
    """Fixture to provide a fresh instance of SingletonCalculator."""
    # Resetting the singleton instance by deleting it (if necessary)
    SingletonCalculator._instance = None
    return SingletonCalculator()  # This will always return a fresh instance

# Parameterized test for performing operations
@pytest.mark.parametrize("operation, a, b", [
    (Addition(), 1, 2),
    (Addition(), 5.5, 4.5),
    (Subtraction(), 0, 0),
])
def test_history(singleton_calculator, operation, a, b):
    """Test that history is correctly updated after operations."""
    singleton_calculator.perform_operation(operation, a, b)
    history = singleton_calculator.get_history()
    
    assert len(history) == 1  # Ensure history has one entry
    assert history[0].operand1 == a
    assert history[0].operand2 == b
    assert history[0].operation.__class__.__name__.lower() == operation.__class__.__name__.lower()
