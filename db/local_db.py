# ///Users/user/Desktop/projects/pokemon-app/db/local_db.py
import json
import os

DB_FILE = "pokemon_full_gen1.json"

def _load_db():
    if os.path.exists(DB_FILE):
        with open(DB_FILE, "r") as f:
            return json.load(f)
    return []

def search_by_name(name: str):
    db = _load_db()
    return next((p for p in db if p["name"].lower() == name.lower()), None)

def search_by_id(pid: int):
    db = _load_db()
    return next((p for p in db if p["id"] == pid), None)

def insert_pokemon(pokemon: dict):
    db = _load_db()
    if any(p["name"].lower() == pokemon["name"].lower() or p["id"] == pokemon["id"] for p in db):
        print(f"{pokemon['name']} already exists.")
        return
    db.append(pokemon)
    with open(DB_FILE, "w") as f:
        json.dump(db, f, indent=2)
    print(f"{pokemon['name']} added.")
