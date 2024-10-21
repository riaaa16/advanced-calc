'''
Factory pattern for creating operations
- usased factory pattern to creates instances of operation classes
- based on a given operation name at runtime
- encapsulates object creation --> open/closed principle
'''
import logging
from typing import List  # Provides support for type hints.

from app.operations import TemplateOperation, Addition, Subtraction, Division, Multiplication

class OperationFactory:
    """
    Factory class to create instances of operations based on the operation type.
    Implements the Factory Pattern.
    """
    @staticmethod
    def create_operation(operation: str) -> TemplateOperation:
        """
        Returns an instance of the appropriate Operation subclass based on the operation string.
        Parameters:
        - operation (str): The operation name (e.g., 'add', 'subtract').
        """
        # Dictionary mapping operation names to their corresponding class instances.
        operations_map = {
            "add": Addition(),
            "subtract": Subtraction(),
            "multiply": Multiplication(),
            "divide": Division(),
        }
        # Log the operation creation request at DEBUG level.
        logging.debug("Creating operation for: %s", operation)
        # Retrieve the operation instance from the map.
        return operations_map.get(operation.lower())  # Returns None if the key is not found.

# Why use the Factory Pattern?
# - It provides a way to create objects without specifying the exact class.
# - Enhances flexibility and scalability
# - new operations can be added without modifying existing code.
