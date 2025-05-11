def display_pokemon(pokemon):
    print("\n Pokémon Details")
    print(f"Name: {pokemon['name'].capitalize()}")
    print(f"ID: {pokemon['id']}")
    print(f"Height: {pokemon['height']}")
    print(f"Weight: {pokemon['weight']}")
    types = ', '.join([t['type']['name'] for t in pokemon['types']])
    print(f"Types: {types}")


def search_pokemon(name: str):
    import json
    import os

    db_file = "pokemon.json"
    name = name.lower()

    if not os.path.exists(db_file):
        print(" Database file not found.")
        return

    with open(db_file, "r") as file:
        try:
            data = json.load(file)
        except json.JSONDecodeError:
            print(" Failed to read JSON data.")
            return

    matches = [p for p in data if p["name"] == name]

    if matches:
        print(f"\n Found {len(matches)} match(es):")
        for p in matches:
            display_pokemon(p)
    else:
        print(" No matching Pokémon found.")
