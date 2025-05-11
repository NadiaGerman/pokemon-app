from utils import get_random_pokemon_name
from api import fetch_pokemon_data
from db import save_to_json  #  new import

def main():
    pokemon_name = get_random_pokemon_name()
    print(f" Randomly selected Pokémon: {pokemon_name}")

    data = fetch_pokemon_data(pokemon_name)
    if data:
        print(f" Pokémon ID: {data['id']}")
        print(f" Name: {data['name']}")
        print(f" Height: {data['height']}")
        print(f" Weight: {data['weight']}")
        print(f" Types: {[t['type']['name'] for t in data['types']]}")
        
        save_to_json(data)  # save to pokemon.json
    else:
        print("Failed to fetch Pokémon data.")

if __name__ == "__main__":
    main()
