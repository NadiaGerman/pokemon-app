import requests

BASE_URL = "https://pokeapi.co/api/v2/pokemon/"

def fetch_pokemon(pokemon_id):
    try:
        response = requests.get(f"{BASE_URL}{pokemon_id}", verify=False, timeout=5)
        response.raise_for_status()
        data = response.json()
        return {
            "id": data["id"],
            "name": data["name"],
            "height": data["height"],
            "weight": data["weight"],
            "types": [t["type"]["name"] for t in data["types"]]
        }
    except Exception as e:
        print(f"Error fetching Pokémon: {e}")
        return None
