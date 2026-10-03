# Mini Alexa — Virtual AI Assistant

A console-based, rule-based virtual assistant built for Project 1 of the
Nexbridge Technologies AI Internship Program. It runs entirely offline
using only the Python standard library — no external datasets, APIs,
or ML frameworks.

## What it does

Mini Alexa greets you, remembers your name for the session, and then
responds to a set of text commands using simple keyword matching —
no trained model, just `if`/`elif` logic (a rule-based system).

## How to run it

You need Python 3 installed. From inside this folder, run:

```
python main.py
```

(On some systems it may be `python3 main.py` instead.)

## Commands

| Command      | What it does                                             |
|--------------|-----------------------------------------------------------|
| `time`       | Shows the current time                                     |
| `date`       | Shows today's date                                          |
| `calculate`  | Does math — e.g. `calculate 12 + 8` (supports `+ - * /`)    |
| `joke`       | Tells a random joke                                         |
| `quote`      | Shares a random motivational quote                          |
| `fact`       | Shares a random fact                                        |
| `game`       | Starts a number guessing game (1–20, 5 tries)               |
| `recommend`  | Suggests an activity based on the current time of day       |
| `perceptron` | A small demo of how a single artificial neuron works        |
| `help`       | Shows this list of commands                                 |
| `exit` / `quit` / `bye` | Ends the session                                |

Anything it doesn't recognize gets a friendly fallback message instead
of crashing.

## Project structure

```
virtual-ai-assistant/
├── main.py            # entry point — runs the main input/response loop
├── greetings.py       # greeting + name capture
├── datetime_utils.py  # date/time helpers
├── calculator.py      # arithmetic parsing and calculation
├── content.py         # quote / joke / fact lists + random selection
├── game.py            # number guessing game
├── ai_concepts.py      # rule-based recommendation + perceptron demo
├── help_menu.py        # prints the command list
└── README.md
```

Each file has a single responsibility, so it's easy to test and explain
one feature at a time.

## The AI/ML/DL concepts in here

Nothing in this project is a trained model. The point was to show what
these ideas look like in plain code:

- **Rule-based system / pattern matching** — the whole assistant is a
  chain of keyword checks (`"time" in command`, etc.) deciding which
  function to call.
- **Rule-based decision-making** — `recommend_activity()` in
  `ai_concepts.py` picks a suggestion purely from `if/elif/else`
  branches on the current hour, the same basic shape as a simple
  classifier choosing between categories.
- **Perceptron (artificial neuron)** — `perceptron_demo()` multiplies
  two user-given inputs by fixed weights, adds a bias, and runs the
  result through a step activation function to produce a 0 or 1. This
  is forward propagation for a single neuron, done with plain
  arithmetic and no library.

## Testing done

Manually tested every command, including edge cases:
- Dividing by zero and typing letters into the calculator (handled,
  no crash)
- Empty input
- Completely unrecognized input (`"tell me about cricket"` style)
- Quitting the guessing game early
- Exiting with `exit`, `quit`, and `bye`

## Notes

This was built for the Mini Alexa / AI Internship Program Project 1
brief — a single-intern, 1–2 week beginner project focused on Python
fundamentals (variables, functions, loops, conditionals, `random`,
`datetime`) plus a first, code-level introduction to AI/ML/DL
vocabulary.
