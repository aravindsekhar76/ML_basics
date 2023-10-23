# RPS.py

import random

def player(prev_play, opponent_history=[]):
    # Check if it's the first move
    if not prev_play:
        return random.choice(["R", "P", "S"])

    # Define strategies against different bots
    if "Q" in opponent_history:
        # Strategy against Quincy
        return "P"
    elif "D" in opponent_history:
        # Strategy against Mr. Defensive
        return "S"
    elif "C" in opponent_history:
        # Strategy against Copycat
        return prev_play
    else:
        # Default strategy (random)
        return random.choice(["R", "P", "S"])
