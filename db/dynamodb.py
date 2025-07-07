import boto3
import os
from dotenv import load_dotenv

load_dotenv()

TABLE_NAME = os.getenv("DYNAMODB_TABLE", "pokemon-app-table")
REGION = os.getenv("AWS_" \
"REGION", "us-west-2")

dynamodb = boto3.resource("dynamodb", region_name=REGION)
table = dynamodb.Table(TABLE_NAME)


def insert_pokemon(pokemon: dict):
    try:
        table.put_item(Item=pokemon)
        print(f"✅ Inserted Pokémon: {pokemon['name']}")
    except Exception as e:
        print(f"❌ Error inserting Pokémon: {e}")


def search_by_name(name: str):
    try:
        response = table.scan(
            FilterExpression="contains (#name, :name)",
            ExpressionAttributeNames={"#name": "name"},
            ExpressionAttributeValues={":name": name}
        )
        items = response.get("Items", [])
        print(items[0] if items else "Not found.")
    except Exception as e:
        print(f"❌ Error searching by name: {e}")


def search_by_id(pid: int):
    try:
        response = table.get_item(Key={"id": pid})
        item = response.get("Item", None)
        print(item if item else "Not found.")
    except Exception as e:
        print(f"❌ Error searching by ID: {e}")
