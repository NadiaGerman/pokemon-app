import boto3

TABLE_NAME = "pokemon"

dynamodb = boto3.client('dynamodb', region_name='us-west-2')

try:
    response = dynamodb.create_table(
        TableName=TABLE_NAME,
        KeySchema=[
            {"AttributeName": "id", "KeyType": "HASH"},
        ],
        AttributeDefinitions=[
            {"AttributeName": "id", "AttributeType": "S"},
        ],
        ProvisionedThroughput={"ReadCapacityUnits": 5, "WriteCapacityUnits": 5}
    )
    print("Table creation initiated:", response.get("TableDescription", {}).get("TableStatus", "Unknown"))
except dynamodb.exceptions.ResourceInUseException:
    print(f"Table '{TABLE_NAME}' already exists.")
