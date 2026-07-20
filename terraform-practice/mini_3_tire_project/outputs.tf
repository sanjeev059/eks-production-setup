output "vpc_id" {
  description = "VPC ID"
  value       = aws_vpc.main_vpc.id
}

output "public_subnets" {
  description = "Public Subnet IDs"
  value       = values(aws_subnet.main)[*].id
}

output "private_subnets" {
  description = "Private Subnet IDs"
  value       = values(aws_subnet.private)[*].id
}

output "alb_dns_name" {
  description = "Application Load Balancer DNS"
  value       = aws_lb.main.dns_name
}

output "alb_url" {
  description = "Application URL"
  value       = "http://${aws_lb.main.dns_name}"
}

output "target_group_arn" {
  description = "Target Group ARN"
  value       = aws_lb_target_group.app.arn
}

output "ec2_private_ips" {
  description = "Private IPs of EC2 instances"
  value = {
    for k, v in aws_instance.app :
    k => v.private_ip
  }
}

output "security_group_ids" {
  description = "Security Groups"
  value = {
    alb = aws_security_group.alb.id
    app = aws_security_group.app.id
  }
}