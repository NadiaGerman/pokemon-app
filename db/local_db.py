## File: db/local_db.py
# --- a/file:///Users/user/Desktop/projects/pokemon-app/db/local_db.py
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
