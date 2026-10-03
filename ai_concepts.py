"""
ai_concepts.py
---------------
This file is the "AI/ML/DL concept demo" part of the project (FR-13 and
FR-14). Nothing here is a trained model - it's plain Python used to
show what these ideas look like in code.

1. recommend_activity() -> a rule-based decision system. The program
   doesn't "learn" anything, it just follows a fixed chain of
   if/elif/else rules based on the current hour. This is the same
   basic idea behind simple expert systems and the earliest chatbots.

2. perceptron_demo() -> the simplest possible artificial neuron.
   - inputs  : numbers the user types in
   - weights : fixed numbers that decide how important each input is
   - bias    : a constant that shifts the result up or down
   - activation function : a step function that turns the final sum
     into a clean 0 or 1 output

   weighted_sum = (x1 * w1) + (x2 * w2) + bias
   output       = 1 if weighted_sum > 0 else 0

   This is forward propagation for a single neuron - no training,
   no library, just the maths that sits underneath a real neural
   network.
"""

from datetime_utils import get_current_hour


def recommend_activity():
    """Rule-based recommendation using the current hour (FR-13)."""
    hour = get_current_hour()

    if 5 <= hour < 11:
        return "Assistant: It's morning - maybe grab some breakfast and plan your day."
    elif 11 <= hour < 16:
        return "Assistant: It's midday - a good time for lunch or a quick walk."
    elif 16 <= hour < 20:
        return "Assistant: It's evening - maybe wrap up tasks and relax a bit."
    else:
        return "Assistant: It's late - probably a good time to rest."


def perceptron_demo():
    """
    Walks the user through a tiny single-neuron calculation.
    Returns the explanation as a string so main.py can print it.
    """
    print("Assistant: Let's try a mini 'perceptron' - the simplest building")
    print("Assistant: block of a neural network. I'll take two numbers from you,")
    print("Assistant: multiply each by a fixed weight, add a bias, then decide 0 or 1.")

    try:
        x1 = float(input("Enter input 1 (a number): "))
        x2 = float(input("Enter input 2 (a number): "))
    except ValueError:
        return "Assistant: Those need to be numbers - let's try the perceptron demo again later."

    # Fixed, hand-picked weights and bias - nothing here is "trained"
    weight1 = 0.6
    weight2 = 0.4
    bias = -0.5

    weighted_sum = (x1 * weight1) + (x2 * weight2) + bias
    output = 1 if weighted_sum > 0 else 0

    return (
        f"Assistant: weighted sum = ({x1} * {weight1}) + ({x2} * {weight2}) + ({bias}) "
        f"= {weighted_sum:.2f}\n"
        f"Assistant: Since {weighted_sum:.2f} {'>' if output == 1 else '<='} 0, the neuron outputs {output}."
    )