# utils.py

import random

def get_random_element(lst):
    """Return a random element from a list."""
    if not lst:
        return None
    return random.choice(lst)
