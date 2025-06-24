from random import randint
from api.fetcher import fetch_pokemon
from db.persist import insert_pokemon

def draw_random_pokemon():
    pid = randint(1, 151)
    pokemon = fetch_pokemon(pid)
    if pokemon:
        insert_pokemon(pokemon)
