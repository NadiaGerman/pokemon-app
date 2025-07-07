# db/dynamodb.py
import boto3
import os
from boto3.dynamodb.conditions import Attr
from dotenv import load_dotenv

load_dotenv()

AWS_REGION = os.getenv("AWS_REGION", "us-west-2")
DYNAMO_TABLE = os.getenv("DYNAMO_TABLE", "pokemon")

try:
    dynamodb = boto3.resource("dynamodb", region_name=AWS_REGION)
    table = dynamodb.Table(DYNAMO_TABLE)
except Exception as e:
    print(f"[ERROR] DynamoDB connection failed: {e}")
    raise

def insert_pokemon(pokemon):
    """
    Insert a Pokémon dict into DynamoDB.
    pokemon = {
        "id": int,
        "name": str,
        "types": [str, ...],
        "base_experience": int
    }
    """
    table.put_item(Item={
        "id": int(pokemon["id"]),
        "name": pokemon["name"],
        "types": pokemon.get("types", []),
        "base_experience": int(pokemon.get("base_experience", 0))
    })

def search_by_id(pokemon_id):
    """Fetch Pokémon by ID (int)."""
    resp = table.get_item(Key={"id": int(pokemon_id)})
    return resp.get("Item")

def search_by_name(name):
    """Fetch Pokémon by name (str)."""
    resp = table.scan(
        FilterExpression=Attr("name").eq(name)
    )
    items = resp.get("Items", [])
    return items[0] if items else None

def get_all_pokemon(limit=20):
    """Get up to `limit` Pokémon."""
    resp = table.scan(Limit=limit)
    return resp.get("Items", [])

def delete_pokemon(pokemon_id):
    """Delete a Pokémon by ID."""
    table.delete_item(Key={"id": int(pokemon_id)})
