"""
Main Calculator Program Module

This module implements an interactive calculator that uses object-oriented programming principles,
including the observer pattern and factory pattern. It provides a Read-Eval-Print Loop (REPL)
for users to perform calculations in real-time.

Features:
- Supports basic arithmetic operations: addition, subtraction, multiplication, and division.
- Allows users to view and clear the calculation history.
- Utilizes logging to track operations and any errors that occur.
- Implements observer pattern to monitor changes in calculation history.
"""

import logging
from app.log_config import setup_logging
from app.operation_factory import OperationFactory
from app.observer import HistoryObserver, CalculatorWithObserver
from app.singleton_calc import SingletonCalculator

def calculator():
    """
    Interactive REPL (Read-Eval-Print Loop) for performing calculator operations.
    Provides a command-line interface for users to interact with the calculator.
    """
    # Set up logging configuration
    setup_logging()

    # Create an instance of the singleton calculator.
    calc = SingletonCalculator()

    # Create an observer to monitor calculation history.
    observer = HistoryObserver()

    # Create an instance of the calculator with observer support.
    calc_with_observer = CalculatorWithObserver()
    calc_with_observer.add_observer(observer)

    # Display a welcome message and instructions.
    print("Welcome to the OOP Calculator! Type 'help' for available commands.")

    # Start the REPL loop.
    while True:
        # Prompt the user for input.
        user_input = input("Enter an operation and two numbers, or a command: ")

        # Handle the 'help' command.
        if user_input.lower() == "help":
            print("\nAvailable commands:")
            print("  add <num1> <num2>       : Add two numbers.")
            print("  subtract <num1> <num2>  : Subtract the second number from the first.")
            print("  multiply <num1> <num2>  : Multiply two numbers.")
            print("  divide <num1> <num2>    : Divide the first number by the second.")
            print("  list                    : Show the calculation history.")
            print("  clear                   : Clear the calculation history.")
            print("  exit                    : Exit the calculator.\n")
            continue

        # Handle the 'exit' command.
        if user_input.lower() == "exit":
            print("Exiting calculator...")
            break

        # Handle the 'list' command to display calculation history.
        if user_input.lower() == "list":
            history = calc.get_history()
            if not history:
                print("No calculations in history.")
            else:
                for calc_item in history:
                    print(calc_item)  # Calls __str__ method of Calculation.
            continue

        # Handle the 'clear' command to clear the history.
        if user_input.lower() == "clear":
            # Clear the history using the singleton instance's method
            calc.get_history().clear()  # Clear the history list.
            logging.info("History cleared.")  # Log the action.
            print("History cleared.")
            continue

        # Attempt to parse and execute the user's command.
        try:
            # Split the user input into components.
            operation_str, num1_str, num2_str = user_input.split()  # May raise ValueError.

            # Convert the operand strings to float.
            num1, num2 = float(num1_str), float(num2_str)  # May raise ValueError.

            # Use the factory to create the appropriate operation object.
            operation = OperationFactory.create_operation(operation_str)

            if operation:
                # Perform the operation using the calculator.
                result = calc_with_observer.perform_operation(operation, num1, num2)
                # Display the result to the user.
                print(f"Result: {result}")
            else:
                # Handle unknown operation names.
                print(f"Unknown operation '{operation_str}'. Type 'help' for available commands.")

        except ValueError as e:
            # Handle errors such as incorrect input format or invalid numbers.
            logging.error("Invalid input or error: %s", e)  # Log the error.
            print(
                "Invalid input. Please enter a valid operation and two numbers. "
                "Type 'help' for instructions."
            )

if __name__ == "__main__":
    # This block ensures that the calculator runs only when the script is executed directly.
    calculator()  # Call the main calculator function to start the REPL.
