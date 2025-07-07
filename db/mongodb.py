## db/mongodb.py
# --- a/file:///Users/user/Desktop/projects/pokemon-app/db/mongodb.py
import os
import json
from dotenv import load_dotenv
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017/")
DB_NAME = os.getenv("MONGO_DB_NAME", "pokemon_db")
COLLECTION_NAME = os.getenv("MONGO_COLLECTION", "pokemon")

if not MONGO_URI:
    raise ValueError("MONGO_URI environment variable is not set.")
if not DB_NAME:
    raise ValueError("MONGO_DB_NAME environment variable is not set.")
if not COLLECTION_NAME:
    raise ValueError("MONGO_COLLECTION environment variable is not set.")

client = MongoClient(MONGO_URI)
try:
    client.admin.command("ping")
except ConnectionFailure as e:
    print(f"MongoDB connection failed: {e}")
    raise

db = client[DB_NAME]
collection = db[COLLECTION_NAME]

def search_by_name(name: str):
    try:
        return collection.find_one({"name": name.lower()})
    except Exception as e:
        print(f"Error searching by name: {e}")
        return None

def search_by_id(pid: int):
    try:
        return collection.find_one({"id": pid})
    except Exception as e:
        print(f"Error searching by ID: {e}")
        return None
