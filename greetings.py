"""
greetings.py
------------
Handles the very first thing the assistant does: introducing itself and
capturing the user's name so it can be reused later in the session
(this covers FR-01 and FR-02 from the project brief).
"""


def get_user_name():
    """Ask the user for their name and return it (stripped of extra spaces)."""
    print("=" * 45)
    print(" MINI ALEXA - VIRTUAL ASSISTANT")
    print("=" * 45)
    name = input("Assistant: Hi! I'm Mini Alexa. What's your name?\nYou: ")
    name = name.strip()
    if name == "":
        name = "Friend"  # fallback so the rest of the session doesn't look empty
    return name


def build_greeting(name):
    """Build the short welcome line shown right after the name is captured."""
    return f"Assistant: Nice to meet you, {name}! Type 'help' to see what I can do."