'''
Operation Classes that performs arithmetic operations
- uses the command pattern to encapsulate each operation as an object
- the template method pattern defines a framework subclass have to follow
'''
from abc import ABC, abstractmethod  # For creating abstract base classes (ABCs).
import logging

class TemplateOperation(ABC):
    """
    Abstract base class representing a mathematical operation using the Template Method pattern.
    - Inherits from ABC to make it an abstract base class.
    - The Template Method Pattern defines the steps of an algorithm.
    """
    def calculate(self, a: float, b: float) -> float:
        """
        Template method that defines the structure for performing an operation.
        Steps:
        1. Validate inputs.
        2. Execute the operation.
        3. Log the result.
        """
        self.validate_inputs(a, b)  # Step 1: Validate the inputs.
        result = self.execute(a, b)  # Step 2: Perform the specific operation.
        self.log_result(a, b, result)  # Step 3: Log the operation and the result.
        return result  # Return the result of the operation.

    def validate_inputs(self, a: float, b: float):
        """
        Common validation method to ensure inputs are numbers.
        Raises a ValueError if inputs are not numeric types.
        """
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            # Log an error message.
            logging.error("Invalid input: %s, %s (Inputs must be numbers)", a, b)
            # Raise an exception.
            raise ValueError("Both inputs must be numbers.")

    @abstractmethod
    def execute(self, a: float, b: float) -> float:
        """
        Abstract method to perform the specific operation.
        Must be implemented by subclasses.
        """

    def log_result(self, a: float, b: float, result: float):
        """
        Logs the result of the calculation.
        """
        # Log an informational message.
        logging.info("Operation performed: %s and %s -> Result: %s", a, b, result)

# Concrete operation classes implementing specific arithmetic operations.
# Each class represents a specific operation and extends the TemplateOperation base class.

class Addition(TemplateOperation):
    """
    Class to represent the addition operation.
    Inherits from TemplateOperation.
    """
    def execute(self, a: float, b: float) -> float:
        """
        Returns the sum of two numbers.
        """
        return a + b  # Perform addition.

class Subtraction(TemplateOperation):
    """
    Class to represent the subtraction operation.
    Inherits from TemplateOperation.
    """
    def execute(self, a: float, b: float) -> float:
        """
        Returns the difference between two numbers.
        """
        return a - b  # Perform subtraction.

class Multiplication(TemplateOperation):
    """
    Class to represent the multiplication operation.
    Inherits from TemplateOperation.
    """
    def execute(self, a: float, b: float) -> float:
        """
        Returns the product of two numbers.
        """
        return a * b  # Perform multiplication.

class Division(TemplateOperation):
    """
    Class to represent the division operation.
    Inherits from TemplateOperation.
    """
    def execute(self, a: float, b: float) -> float:
        """
        Returns the quotient of two numbers.
        Raises a ValueError if attempting to divide by zero.
        """
        if b == 0:
            logging.error("Attempted to divide by zero.")  # Log an error message.
            raise ValueError("Division by zero is not allowed.")  # Raise an exception.
        return a / b  # Perform division.

# Why use the Template Method Pattern here?
# - It defines the algorithm's skeleton in a method (`calculate`),
# deferring some steps (`execute`) to subclasses.
# - Promotes code reuse and enforces a consistent structure across different operations.
