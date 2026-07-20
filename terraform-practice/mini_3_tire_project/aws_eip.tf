resource "aws_eip" "nat" {

  for_each = var.public_subnets

  domain = "vpc"

  tags = {
    Name = "${each.key}-eip"
  }
}