variable "aws_region" {
  description = "AWS Region to deploy resources"
  type        = string
  default     = "us-west-2"
}

variable "instance_type" {
  description = "EC2 instance type"
  type        = string
  default     = "t2.micro"
}

variable "key_pair_name" {
  description = "Name of the EC2 key pair"
  type        = string
}

variable "ami_id" {
  description = "AMI ID for the EC2 instance"
  type        = string
}

variable "security_group_name" {
  description = "Name of the security group"
  type        = string
  default     = "pokemon-app-sg"
}

variable "app_port" {
  description = "Port number for application"
  type        = number
  default     = 8080
}
