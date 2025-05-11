import json
import os

DB_FILE = "pokemon.json"

def save_to_json(pokemon_data: dict):
    if not pokemon_data:
        print(" No data to save.")
        return

    data = []
    if os.path.exists(DB_FILE):
        with open(DB_FILE, "r") as file:
            try:
                data = json.load(file)
            except json.JSONDecodeError:
                pass

    data.append(pokemon_data)

    with open(DB_FILE, "w") as file:
        json.dump(data, file, indent=2)
    
    print(f" Saved {pokemon_data['name']} to {DB_FILE}")
