import random
from typing import Tuple

def get_random_pokemon(pokemon_list: list[dict[str, str]]) -> Tuple[str, str]:
    """Select a random Pokémon from the list and return its name and URL."""
    selected = random.choice(pokemon_list)
    return selected["name"], selected["url"]
