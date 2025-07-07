// File: db/outputs.tf
output "table_name" {
  value = aws_dynamodb_table.pokemon_table.name
}
