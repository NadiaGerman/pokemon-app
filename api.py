# api.py
import requests
from typing import Optional

POKEAPI_BASE_URL = "https://pokeapi.co/api/v2/pokemon/"

def get_pokemon_data(name: str) -> Optional[dict]:
    """
    Fetches Pokémon data from the PokéAPI.
    
    Args:
        name (str): Name of the Pokémon (e.g., "pikachu")
        
    Returns:
        dict or None: Parsed JSON response if successful, otherwise None.
    """
    try:
        url = f"{POKEAPI_BASE_URL}{name.lower()}"
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Error fetching data for '{name}': {e}")
        return None
