# ui/menu.py

from db import search_by_name, search_by_id  # <--- Now always correct backend!
from battle.draw import draw_random_pokemon

def main_menu():
    while True:
        print("\n=== Pokémon App Menu ===")
        print("1.  Fetch and Save a Random Pokémon")
        print("2.  Search Pokémon by Name")
        print("3.  Search Pokémon by ID")
        print("4.  Exit")

        choice = input("Enter your choice (1-4): ").strip()

        if choice == "1":
            draw_random_pokemon()
        elif choice == "2":
            name = input("Enter Pokémon name: ").strip()
            result = search_by_name(name)
            if result and isinstance(result, dict):
                result.pop("_id", None)
                print(result)
            else:
                print("Not found.")
        elif choice == "3":
            pid = input("Enter Pokémon ID: ").strip()
            if pid.isdigit():
                result = search_by_id(int(pid))
                if result and isinstance(result, dict):
                    result.pop("_id", None)
                    print(result)
                else:
                    print("Not found.")
            else:
                print("ID must be a number.")
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")
