import json
import os

DB_FILE = "pokemon.json"

def save_to_json(pokemon_data: dict) -> None:
    if not pokemon_data:
        print(" No data to save.")
        return

    existing_data = []
    if os.path.exists(DB_FILE):
        with open(DB_FILE, "r") as file:
            try:
                existing_data = json.load(file)
            except json.JSONDecodeError:
                print(" JSON file was empty or corrupted. Starting fresh.")

    # Avoid saving duplicates by checking name
    if any(p["name"] == pokemon_data["name"] for p in existing_data):
        print(f" Pokémon '{pokemon_data['name']}' already exists in {DB_FILE}")
        return

    existing_data.append(pokemon_data)

    with open(DB_FILE, "w") as file:
        json.dump(existing_data, file, indent=2)

    print(f" Saved {pokemon_data['name']} to {DB_FILE}")

def load_from_json() -> list[dict]:
    if not os.path.exists(DB_FILE):
        print(" No database file found.")
        return []

    with open(DB_FILE, "r") as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            print(" Failed to read JSON. The file might be corrupted.")
            return []
def search_pokemon_by_name(name: str):
    data = load_from_json()
    for pokemon in data:
        if pokemon['name'].lower() == name.lower():
            return pokemon
    return None
