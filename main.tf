provider "aws" {
  region = "us-west-2"
}

module "dynamodb" {
  source      = "./modules/dynamodb"
  table_name  = "pokemon-app-table"
  environment = "dev"
}
