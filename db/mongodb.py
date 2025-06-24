import os
import json
from dotenv import load_dotenv
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017/")
DB_NAME = os.getenv("MONGO_DB_NAME", "pokemon_db")
COLLECTION_NAME = os.getenv("MONGO_COLLECTION", "pokemon")

client = MongoClient(MONGO_URI)
try:
    client.admin.command("ping")
except ConnectionFailure:
    print(" MongoDB connection failed.")
    raise

db = client[DB_NAME]
collection = db[COLLECTION_NAME]


def insert_pokemon(pokemon: dict):
    if collection.find_one({"id": pokemon["id"]}):
        print(f"{pokemon['name']} already exists in MongoDB.")
        return
    collection.insert_one(pokemon)
    print(f"{pokemon['name']} added to MongoDB.")


def search_by_name(name: str):
    name = name.lower()
    result = collection.find_one({"name": name})
    print(result if result else "Not found.")


def search_by_id(pid: int):
    result = collection.find_one({"id": pid})
    print(result if result else "Not found.")


def preload_from_json(json_file="pokemon.json"):
    if collection.count_documents({}) > 0:
        print("MongoDB already populated.")
        return

    try:
        with open(json_file, "r") as f:
            data = json.load(f)
            collection.insert_many(data)
            print(f"Preloaded {len(data)} Pokémon from {json_file} into MongoDB.")
    except Exception as e:
        print(f"Failed to preload data: {e}")
