output "instance_public_ip" {
  description = "Public IP address of the EC2 instance"
  value       = aws_instance.pokemon_app_instance.public_ip
}

output "security_group_id" {
  description = "ID of the security group"
  value       = aws_security_group.pokemon_app_sg.id
}
