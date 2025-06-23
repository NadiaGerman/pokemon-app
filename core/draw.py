import random
from api.fetcher import fetch_pokemon
from db.local_db import insert_pokemon

def draw_random_pokemon():
    pid = random.randint(1, 151)
    pokemon = fetch_pokemon(pid)
    if pokemon:
        insert_pokemon(pokemon)
