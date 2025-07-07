// File: db/main.tf
resource "aws_dynamodb_table" "pokemon_table" {
  name           = "pokemon-app-table"
  billing_mode   = "PAY_PER_REQUEST"
  hash_key       = "id"

  attribute {
    name = "id"
    type = "N"
  }

  tags = {
    Environment = "dev"
    Name        = "pokemon-app-table"
  }
}
