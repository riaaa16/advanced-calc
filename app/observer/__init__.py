'''
Observer pattern for tracking history
- HistoryObserrver and CalculatorWithObserver classes
- observers are notified of changes in calculation history
- logs whenever a new calculation is performed
'''
import logging
from typing import List  # Provides support for type hints.

from app.operations import TemplateOperation
from app.calculation import Calculation

class HistoryObserver:
    """
    Observer that gets notified whenever a new calculation is added to history.
    Implements the Observer Pattern.
    """
    def update(self, calculation):
        """
        Called when a new calculation is added to the history.
        Parameters:
        - calculation (Calculation): The calculation object that was added.
        """
        # Log the notification at INFO level.
        logging.info("Observer: New calculation added -> %s", calculation)

class CalculatorWithObserver:
    """
    Calculator class with observer support for tracking calculation history.
    Maintains a list of observers and notifies them of changes.
    """
    def __init__(self):
        self._history: List[Calculation] = []  # List to store calculation history.
        self._observers: List[HistoryObserver] = []  # List of observers.

    def add_observer(self, observer: HistoryObserver):
        """
        Adds an observer to be notified when history is updated.
        Parameters:
        - observer (HistoryObserver): The observer to add.
        """
        self._observers.append(observer)  # Add the observer to the list.
        logging.debug("Observer added: %s", observer)  # Log the addition.

    def notify_observers(self, calculation):
        """
        Notifies all observers when a new calculation is added.
        Parameters:
        - calculation (Calculation): The calculation object that was added.
        """
        for observer in self._observers:
            observer.update(calculation)  # Call the update method on the observer.
            logging.debug("Notified observer about: %s", calculation)  # Log the notification.

    def perform_operation(self, operation: TemplateOperation, a: float, b: float):
        """
        Performs the operation, stores it in history, and notifies observers.
        Parameters:
        - operation (TemplateOperation): The operation to perform.
        - a (float): The first operand.
        - b (float): The second operand.
        Returns:
        - The result of the operation.
        """
        calculation = Calculation(operation, a, b)  # Create a new Calculation object.
        self._history.append(calculation)  # Add the calculation to the history.
        self.notify_observers(calculation)  # Notify observers of the new calculation.
        logging.debug("Performed operation: %s", calculation)  # Log the operation.
        return operation.calculate(a, b)  # Execute the calculation and return the result.

# Why use the Observer Pattern?
# - Decouples the calculator from the observers, allowing for dynamic addition/removal of observers.
# - Promotes a one-to-many dependency between objects
# - when one object changes state, all dependents are notified.
