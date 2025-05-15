from db import load_from_json

def display_pokemon(pokemon: dict):
    print("\n Pokémon Details")
    print(f"Name: {pokemon['name'].title()}")
    print(f"ID: {pokemon['id']}")
    print(f"Height: {pokemon['height']}")
    print(f"Weight: {pokemon['weight']}")
    print(f"Types: {', '.join(pokemon['types'])}")

def search_pokemon_by_name(name: str):
    data = load_from_json()
    for p in data:
        if p["name"].lower() == name.lower():
            display_pokemon(p)
            return
    print(" No matching Pokémon found.")

def search_pokemon_by_id(pid: int):
    data = load_from_json()
    for p in data:
        if p["id"] == pid:
            display_pokemon(p)
            return
    print(" No matching Pokémon found.")
