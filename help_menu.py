"""
help_menu.py
------------
Prints the list of supported commands. Covers FR-10 from the project
brief.
"""


def print_help():
    print("-" * 45)
    print("Assistant: Here's everything I can do -")
    print("  time        -> tell you the current time")
    print("  date        -> tell you today's date")
    print("  calculate   -> do math, e.g. 'calculate 12 + 8'")
    print("  joke        -> tell you a joke")
    print("  quote       -> share a motivational quote")
    print("  fact        -> share a random fact")
    print("  game        -> play a number guessing game")
    print("  recommend   -> suggest an activity based on the time of day")
    print("  perceptron  -> a tiny demo of how a single neuron works")
    print("  help        -> show this menu again")
    print("  exit        -> end our conversation")
    print("-" * 45)