# battle/draw.py
# battle/draw.py

from random import randint
from api.fetcher import fetch_pokemon

def draw_random_pokemon():
    from db import insert_pokemon 
    pid = randint(1, 151)
    pokemon = fetch_pokemon(pid)
    if pokemon:
        insert_pokemon(pokemon)
        print(f"Fetched Pokémon: {pokemon['name']} (ID: {pokemon['id']})")
        # Draw the pokemon after fetching
        draw_pokemon(pokemon)
    else:
        print("Failed to fetch Pokémon. Please try again later.")

def draw_pokemon(pokemon_data):
    """Draw a specific Pokemon based on its data"""
    if not pokemon_data:
        print("No Pokemon data to draw")
        return
    
    name = pokemon_data.get('name', 'Unknown')
    pokemon_id = pokemon_data.get('id', '???')
    types = pokemon_data.get('types', ['Unknown'])
    
    # Format types as comma-separated string
    types_str = ', '.join(types) if isinstance(types, list) else types
    
    print(f"\n====== Pokemon #{pokemon_id}: {name.upper()} ======")
    print(f"Type(s): {types_str}")
    
    # Draw simple ASCII art based on first type
    first_type = types[0].lower() if isinstance(types, list) and types else "normal"
    
    if "fire" in first_type:
        print("""
        🔥🔥🔥
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣠⣤⣤⣤⣤⣤⣀⡀⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⢀⣤⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣤⡀⠀⠀⠀
        ⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⡀⠀
        ⠀⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄
        ⢰⣿⣿⣿⣿⡿⠟⠛⠛⠛⠛⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇
        ⣿⣿⣿⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
        🔥🔥🔥
        """)
    elif "water" in first_type:
        print("""
        💧💧💧
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⣤⣤⣤⣤⣤⣀⡀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣤⡀⠀⠀
        ⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠀⠀
        ⠀⠀⠀⠀⠀⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡆⠀
        ⠀⠀⠀⠀⢰⣿⣿⣿⣿⣿⣿⡿⠛⠛⠛⠛⠛⠻⢿⣿⣿⣿⣿⣿⡇⠀
        ⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⣿⣿⣿⠀
        💧💧💧
        """)
    elif "grass" in first_type:
        print("""
        🌱🌱🌱
        ⠀⠀⠀⠀⠀⠀⠀⢀⣠⣤⣶⣶⣶⣶⣶⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⢀⣤⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣤⡀⠀⠀⠀⠀
        ⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⠀⠀⠀
        ⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀⠀
        ⠀⣿⣿⣿⡿⠟⠋⠉⠉⠛⠻⢿⣿⣿⣿⣿⡿⠟⠛⠉⠉⠙⠻⣿⣷⠀
        ⢰⣿⣿⣿⣷⡄⠀⠀⠀⠀⠀⠀⠙⠻⠟⠋⠀⠀⠀⠀⠀⠀⣰⣿⣿⣇
        🌱🌱🌱
        """)
    elif "electric" in first_type:
        print("""
        ⚡⚡⚡
        ⢀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠈⠉⠛⠓⠶⠶⠶⠶⠶⠿⠿⠿
        ⠀⠀⠀⠀⠀⠀⢀⣀⣀⣀⡀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⢶⡿⠋⠉⠉⠉⠙⢿⡆⠀⠀⠀
        ⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⢷⠀⠀⠀
        ⠀⠀⠀⠀⠀⠙⠿⣿⣿⣿⠿⠋⠁⠀⠀⠀
        ⠀⠀⠀⠀⣠⣶⡿⠿⠿⠿⣶⣄⠀⠀⠀⠀
        ⠀⠀⠀⠰⠿⠃⠀⠀⠀⠀⠈⠿⠷⠀⠀⠀
        ⚡⚡⚡
        """)
    else:
        print("""
        ⭐⭐⭐
        ⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⣤⣤⣤⣤⣤⣄⡀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⢠⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⡀⠀⠀⠀
        ⠀⠀⠀⠀⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣆⠀⠀
        ⠀⠀⠀⣸⣿⣿⣿⡿⠿⠿⠿⠿⠿⠿⠿⢿⣿⣿⣿⣿⣿⣧⠀
        ⠀⠀⢠⣿⣿⣿⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⣿⣿⣿⣿⡄
        ⠀⠀⢸⣿⣿⣿⣧⣤⣤⣤⣤⣤⣤⣤⣤⣤⣼⣿⣿⣿⣿⣿⡇
        ⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇
        ⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇
        ⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇
        ⭐⭐⭐
        """)
    
    # Print additional Pokemon data if available
    stats = pokemon_data.get('stats', {})
    if stats:
        print("\n=== Stats ===")
        for stat_name, value in stats.items():
            print(f"{stat_name.replace('_', ' ').title()}: {value}")
    
    abilities = pokemon_data.get('abilities', [])
    if abilities:
        print("\n=== Abilities ===")
        for ability in abilities:
            print(f"- {ability}")
    
    # Print a divider at the end
    print("\n" + "=" * 40 + "\n")