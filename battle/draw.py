# battle/draw.py

from random import randint
from api.fetcher import fetch_pokemon

def draw_random_pokemon():
    from db import insert_pokemon  # Import inside function, not at top
    pid = randint(1, 151)
    pokemon = fetch_pokemon(pid)
    if pokemon:
        insert_pokemon(pokemon)
        print(f"Fetched Pokémon: {pokemon['name']} (ID: {pokemon['id']})")
    else:
        print("Failed to fetch Pokémon. Please try again later.")