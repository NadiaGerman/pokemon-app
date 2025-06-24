import json
import os

DB_FILE = "pokemon.json"

def _load_db():
    if os.path.exists(DB_FILE):
        with open(DB_FILE, "r") as f:
            return json.load(f)
    return []

def _save_db(data):
    with open(DB_FILE, "w") as f:
        json.dump(data, f, indent=2)

def insert_pokemon(pokemon: dict):
    db = _load_db()
    if any(p["name"].lower() == pokemon["name"].lower() for p in db):
        print(f"{pokemon['name']} already exists.")
        return
    db.append(pokemon)
    _save_db(db)
    print(f"{pokemon['name']} added.")
