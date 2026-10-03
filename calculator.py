"""
calculator.py
-------------
Basic arithmetic calculator. Covers FR-05 from the project brief:
add, subtract, multiply, divide - with graceful handling of
divide-by-zero and bad/non-numeric input so the program never crashes.

Expected input format:  calculate <num1> <operator> <num2>
Example:                calculate 12 + 8
"""


def calculate(command):
    """
    Parse a command like 'calculate 12 + 8' and return the result as a
    friendly string. Never raises - any bad input returns a message
    instead of crashing the program (this satisfies the Reliability
    requirement in the non-functional requirements table).
    """
    parts = command.split()

    # We expect exactly 4 pieces: "calculate", num1, operator, num2
    if len(parts) != 4:
        return "Please use the format: calculate <num1> <operator> <num2>  (e.g. calculate 12 + 8)"

    _, raw_num1, operator, raw_num2 = parts

    try:
        num1 = float(raw_num1)
        num2 = float(raw_num2)
    except ValueError:
        return "I need two numbers to calculate with - try something like: calculate 12 + 8"

    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        if num2 == 0:
            return "I can't divide by zero - try a different number."
        result = num1 / num2
    else:
        return "I only understand +, -, * and / as operators."

    # Show whole numbers without a trailing .0 to look cleaner
    if result == int(result):
        result = int(result)

    return f"The result is {result}"