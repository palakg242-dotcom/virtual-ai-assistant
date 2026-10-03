"""
game.py
-------
A simple number guessing game. Covers FR-09 from the project brief:
the assistant picks a random number in a fixed range, the user has a
limited number of attempts, and gets 'higher'/'lower' hints after
each guess.
"""

import random

MIN_NUMBER = 1
MAX_NUMBER = 20
MAX_ATTEMPTS = 5


def play_guessing_game():
    """Run one full round of the number guessing game."""
    secret_number = random.randint(MIN_NUMBER, MAX_NUMBER)
    attempts_left = MAX_ATTEMPTS

    print(f"Assistant: I'm thinking of a number between {MIN_NUMBER} and {MAX_NUMBER}.")
    print(f"Assistant: You have {attempts_left} tries. Type 'quit' to stop early.")

    while attempts_left > 0:
        guess = input(f"You ({attempts_left} left): ").strip().lower()

        if guess == "quit":
            print(f"Assistant: Okay, stopping the game. The number was {secret_number}.")
            return

        if not guess.lstrip("-").isdigit():
            print("Assistant: That's not a number - please guess again.")
            continue

        guess = int(guess)
        attempts_left -= 1

        if guess == secret_number:
            print(f"Assistant: That's it! The number was {secret_number}. You got it!")
            return
        elif guess < secret_number:
            print("Assistant: Higher!")
        else:
            print("Assistant: Lower!")

    print(f"Assistant: Out of tries! The number was {secret_number}. Better luck next time.")