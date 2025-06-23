resource "aws_dynamodb_table" "pokemon_table" {
  name           = var.table_name
  billing_mode   = "PAY_PER_REQUEST"
  hash_key       = "id"

  attribute {
    name = "id"
    type = "N"
  }

  tags = {
    Environment = var.environment
    Name        = var.table_name
  }
}
