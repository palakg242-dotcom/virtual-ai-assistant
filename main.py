"""
main.py
-------
Entry point for the Mini Alexa virtual assistant.

This file ties every feature module together into one request ->
classify -> respond loop, as described in the project's System
Workflow section. It does not contain any feature logic itself -
each feature lives in its own module so the code stays organised
and easy to test one piece at a time.

Run with:   python main.py
Exit with:  typing 'exit', 'quit' or 'bye'
"""

from greetings import get_user_name, build_greeting
from datetime_utils import get_current_time, get_current_date
from calculator import calculate
from content import get_random_quote, get_random_joke, get_random_fact
from game import play_guessing_game
from ai_concepts import recommend_activity, perceptron_demo
from help_menu import print_help


def route_command(command, name):
    """
    Looks at the normalized command text and decides which feature to
    run. Keyword matching is intentionally simple (string 'in' checks)
    - this is the "pattern matching" / "keyword detection" AI concept
    the project brief talks about, not a trained classifier.

    Returns True if the session should keep running, False if it's
    time to exit.
    """
    if command in ("exit", "quit", "bye"):
        print(f"Assistant: Goodbye, {name}! Have a great day.")
        return False

    elif "calculate" in command:
        print("Assistant:", calculate(command))

    elif "time" in command:
        print("Assistant:", get_current_time())

    elif "date" in command:
        print("Assistant:", get_current_date())

    elif "joke" in command:
        print("Assistant:", get_random_joke())

    elif "quote" in command:
        print("Assistant:", get_random_quote())

    elif "fact" in command:
        print("Assistant:", get_random_fact())

    elif "game" in command:
        play_guessing_game()

    elif "recommend" in command:
        print(recommend_activity())

    elif "perceptron" in command:
        print(perceptron_demo())

    elif "help" in command:
        print_help()

    else:
        # FR-12: unrecognized input never crashes the program
        print("Assistant: I'm not sure I understood that - type 'help' to see what I can do.")

    return True


def main():
    name = get_user_name()
    print(build_greeting(name))
    print("Assistant: (type 'help' anytime to see the full command list)\n")

    running = True
    while running:
        raw_command = input("You: ")
        command = raw_command.strip().lower()

        if command == "":
            print("Assistant: I didn't catch that - type 'help' if you're not sure what to say.")
            continue

        running = route_command(command, name)


if __name__ == "__main__":
    main()