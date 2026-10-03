"""
content.py
----------
Stores the fixed lists of quotes, jokes and facts the assistant can share,
and the functions that pick one at random.

AI/ML concept note:
Picking a random item from a fixed list is NOT a recommendation engine,
but it mimics one at a very basic level - a real system would score
many candidates and pick the "best" one, we just pick randomly from a
small curated list. That's the whole idea behind FR-06, FR-07, FR-08.
"""

import random

QUOTES = [
    "Believe you can and you're halfway there.",
    "Success is not final, failure is not fatal - it's the courage to continue that counts.",
    "The future belongs to those who prepare for it today.",
    "Small steps every day add up to big results.",
    "Discipline is choosing between what you want now and what you want most."
]

JOKES = [
    "Why did the developer go broke? Because they used up all their cache.",
    "Why do programmers prefer dark mode? Because light attracts bugs.",
    "I told my computer I needed a break, and it said no problem, it froze.",
    "Why was the function sad after the party? It didn't get called.",
    "There are 10 types of people in the world - those who understand binary and those who don't."
]

FACTS = [
    "Honey never spoils if it's stored properly.",
    "Octopuses have three hearts.",
    "Bananas are technically berries, but strawberries aren't.",
    "A single bolt of lightning contains enough energy to toast about 100,000 slices of bread.",
    "The first computer 'bug' was an actual moth found stuck in a relay in 1947."
]


def get_random_quote():
    """Return one random motivational quote (FR-06)."""
    return random.choice(QUOTES)


def get_random_joke():
    """Return one random joke (FR-07)."""
    return random.choice(JOKES)


def get_random_fact():
    """Return one random fact (FR-08)."""
    return random.choice(FACTS)