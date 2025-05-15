from ui import display_pokemon, search_pokemon_by_name, search_pokemon_by_id
from utils import get_random_pokemon
from db import save_to_json, check_file_exists

def main_menu():
    while True:
        print("\n=== Pokémon App Menu ===")
        print("1.  Fetch and Save a Random Pokémon")
        print("2.  Search Pokémon by Name")
        print("3.  Search Pokémon by ID")
        print("4.  Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            pokemon = get_random_pokemon()
            if pokemon:
                display_pokemon(pokemon)
                save_to_json(pokemon)
            else:
                print(" Failed to fetch Pokémon.")
        elif choice == '2':
            name = input("Enter Pokémon name to search: ").lower()
            search_pokemon_by_name(name)
        elif choice == '3':
            try:
                pid = int(input("Enter Pokémon ID to search: "))
                search_pokemon_by_id(pid)
            except ValueError:
                print(" Please enter a valid number.")
        elif choice == '4':
            print(" Goodbye!")
            break
        else:
            print(" Invalid choice. Please enter a number from 1 to 4.")

if __name__ == "__main__":
    main_menu()
