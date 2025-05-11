from api import fetch_pokemon_list
from utils import get_random_pokemon

def main():
    pokemon_list = fetch_pokemon_list()
    print(f"✅ Total Pokémon fetched: {len(pokemon_list)}")

    name, url = get_random_pokemon(pokemon_list)
    print(f"🎲 Randomly selected Pokémon: {name}")
    print(f"🔗 API URL: {url}")

if __name__ == "__main__":
    main()
