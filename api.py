import requests

def fetch_pokemon_data(name: str) -> dict:
    url = f"https://pokeapi.co/api/v2/pokemon/{name.lower()}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return {
            "id": data["id"],
            "name": data["name"],
            "height": data["height"],
            "weight": data["weight"],
            "types": [t["type"]["name"] for t in data["types"]]
        }
    except requests.RequestException as e:
        print(f" Error fetching data for {name}: {e}")
        return None
