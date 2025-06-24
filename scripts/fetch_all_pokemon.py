import requests
import json
from time import sleep

BASE_URL = "https://pokeapi.co/api/v2/pokemon/"
MAX_ID = 1010  # Approximate max as of Gen 9

def fetch_pokemon(pid):
    try:
        response = requests.get(f"{BASE_URL}{pid}", timeout=10)
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
        print(f"❌ Failed for ID {pid}: {e}")
        return None

all_pokemon = []

for pid in range(1, MAX_ID + 1):
    print(f"Fetching Pokémon ID {pid}...")
    poke = fetch_pokemon(pid)
    if poke:
        all_pokemon.append(poke)
    sleep(0.5)  # Respect API rate limits

# Save to JSON
with open("pokemon_full.json", "w") as f:
    json.dump(all_pokemon, f, indent=2)

print(f"\n✅ Saved {len(all_pokemon)} Pokémon to pokemon_full.json")
