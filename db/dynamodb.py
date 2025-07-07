# db/dynamodb.py

import os
import boto3
from dotenv import load_dotenv

load_dotenv()

TABLE_NAME = os.getenv("DYNAMODB_TABLE", "pokemon-app-table")
REGION = os.getenv("AWS_REGION", "us-west-2")  # <-- Fix: Should be AWS_REGION not AWS_ \ "REGION"

dynamodb = boto3.resource("dynamodb", region_name=REGION)
table = dynamodb.Table(TABLE_NAME) # type: ignore

def insert_pokemon(pokemon: dict) -> None:
    """Insert a Pokémon record into DynamoDB."""
    try:
        table.put_item(Item=pokemon)
        print(f"✅ Inserted Pokémon: {pokemon['name']}")
    except Exception as e:
        print(f"❌ Error inserting Pokémon: {e}")

def search_by_name(name: str) -> dict | None:
    """Search for a Pokémon by name (case-insensitive)."""
    try:
        response = table.scan(
            FilterExpression="contains (#name, :name)",
            ExpressionAttributeNames={"#name": "name"},
            ExpressionAttributeValues={":name": name.lower()}
        )
        items = response.get("Items", [])
        return items[0] if items else None
    except Exception as e:
        print(f"❌ Error searching by name: {e}")
        return None

def search_by_id(pid: int) -> dict | None:
    """Search for a Pokémon by ID."""
    try:
        response = table.get_item(Key={"id": pid})
        return response.get("Item", None)
    except Exception as e:
        print(f"❌ Error searching by ID: {e}")
        return None
