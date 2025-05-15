import requests
import random
from constants import BASE_URL
from api import fetch_pokemon_data
from db import load_from_json

def get_random_pokemon():
    try:
        response = requests.get(BASE_URL)
        response.raise_for_status()
        data = response.json()
        results = data.get("results", [])
        if not results:
            return None
        pokemon = random.choice(results)
        return fetch_pokemon_data(pokemon['name'])
    except requests.RequestException as e:
        print(f" Error getting Pokémon list: {e}")
        return None
