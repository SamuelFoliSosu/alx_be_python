"""
1. Robust Division Calculator with Command Line Arguments
mandatory
Objective: Implement a division calculator that robustly handles errors like division by zero and non-numeric inputs using command line arguments.

Task Description:
Create two Python scripts: robust_division_calculator.py, which contains the division logic including error handling, and main.py, which interfaces with the user through the command line.

robust_division_calculator.py:
Define a function safe_divide(numerator, denominator) that performs division, handling potential errors:

Division by Zero: Use a try-except block to catch ZeroDivisionError.
Non-numeric Input: Attempt to convert arguments to floats. Use a try-except block to catch ValueError for non-numeric inputs.
Return appropriate messages for errors or the result for successful division.
main.py for Command Line Interaction:
This script will import safe_divide from robust_division_calculator.py and use it to divide numbers provided as command line arguments.

import sys
from robust_division_calculator import safe_divide

def main():
    if len(sys.argv) != 3:
        print("Usage: python main.py <numerator> <denominator>")
        sys.exit(1)

    numerator = sys.argv[1]
    denominator = sys.argv[2]

    result = safe_divide(numerator, denominator)
    print(result)

if __name__ == "__main__":
    main()
Expected Behavior:
The script is executed from the command line with two additional arguments representing the numerator and denominator. Here are sample commands and the expected outputs:

Normal Division:
  python main.py 10 5
Expected Output: The result of the division is 2.0

Division by Zero:
  python main.py 10 0
Expected Output: Error: Cannot divide by zero.

Invalid Input (Non-numeric):
  python main.py ten 5
Expected Output: Error: Please enter numeric values only.

Implementation Notes for you:
Focus on error handling within safe_divide in robust_division_calculator.py. Ensure you cover the scenarios detailed above.
Test your function using main.py by passing different types of inputs via command line arguments. This method allows you to quickly assess how well your error handling works in various situations.
This task helps you practice writing error-resistant code, a crucial skill in software development.

"""

# robust_division_calculator.py by Gemni

def safe_divide(numerator, denominator):
    """
    Performs division of two numbers, robustly handling potential errors
    like ZeroDivisionError and ValueError for non-numeric inputs.

    Args:
        numerator (str or numeric): The numerator, expected to be convertible to a float.
        denominator (str or numeric): The denominator, expected to be convertible to a float.

    Returns:
        str: A message indicating the result of the division or the type of error encountered.
    """
    try:
        # Attempt to convert both numerator and denominator to floats.
        # This will raise a ValueError if conversion fails (non-numeric input).
        num = float(numerator)
        den = float(denominator)

        # Check for division by zero before performing the division itself.
        # Although Python's division operator will raise ZeroDivisionError,
        # explicitly checking allows for a more controlled error message.
        if den == 0:
            return "Error: Cannot divide by zero."

        # Perform the division if both inputs are valid numbers and denominator is not zero.
        result = num / den
        return f"The result of the division is {result}"

    except ValueError:
        # This block catches errors if numerator or denominator cannot be converted to a float.
        return "Error: Please enter numeric values only."
    except Exception as e:
        # This is a general catch-all for any other unexpected errors.
        # In this specific problem, ZeroDivisionError is handled by the 'if den == 0' check.
        # If we didn't have that check, ZeroDivisionError would be caught here too.
        # However, for robustness, it's good practice to have a general exception.
        return f"An unexpected error occurred: {e}"

