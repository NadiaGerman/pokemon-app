from db import load_from_json
from db import search_pokemon_by_name

def display_saved_pokemon():
    data = load_from_json()
    if not data:
        print(" No Pokémon saved yet.")
        return

    print(f"\n Total saved Pokémon: {len(data)}\n")
    for idx, p in enumerate(data, 1):
        print(f"{idx}. {p['name'].capitalize()} - ID: {p['id']} - Type(s): {', '.join([t['type']['name'] for t in p['types']])}")


def display_pokemon_by_name(name: str):
    pokemon = search_pokemon_by_name(name)
    if pokemon:
        print(f"\n Found: {pokemon['name'].capitalize()} (ID: {pokemon['id']})")
        print(" Stats:")
        for stat in pokemon['stats']:
            print(f"  {stat['stat']['name']}: {stat['base_stat']}")
    else:
        print(" Pokémon not found.")
