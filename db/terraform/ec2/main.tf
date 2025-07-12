provider "aws" {
  region = var.aws_region
}

resource "aws_security_group" "pokemon_app_sg" {
  name        = var.security_group_name
  description = "Security group for Pokemon App"

  ingress {
    description = "SSH"
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    description = "App Port"
    from_port   = var.app_port
    to_port     = var.app_port
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    description = "Allow all outbound traffic"
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

resource "aws_iam_role" "pokemon_app_role" {
  name = "pokemon-app-role"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Effect = "Allow"
      Principal = {
        Service = "ec2.amazonaws.com"
      }
      Action = "sts:AssumeRole"
    }]
  })
}

resource "aws_iam_role_policy_attachment" "attach_dynamodb" {
  role       = aws_iam_role.pokemon_app_role.name
  policy_arn = "arn:aws:iam::aws:policy/AmazonDynamoDBFullAccess"
}

resource "aws_iam_instance_profile" "pokemon_app_role_profile" {
  name = "pokemon-app-role-profile"
  role = aws_iam_role.pokemon_app_role.name
}

resource "aws_instance" "pokemon_app_instance" {
  ami                         = var.ami_id
  instance_type               = var.instance_type
  key_name                   = var.key_pair_name
  vpc_security_group_ids      = [aws_security_group.pokemon_app_sg.id]
  associate_public_ip_address = true

  iam_instance_profile = aws_iam_instance_profile.pokemon_app_role_profile.name

  tags = {
    Name = "PokemonAppInstance"
  }
}
