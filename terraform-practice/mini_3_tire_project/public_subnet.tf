resource "aws_subnet" "main" {

  for_each = var.public_subnets
  vpc_id   = aws_vpc.main_vpc.id

  cidr_block        = each.value.cidr
  availability_zone = each.value.az

  tags = {
    Name = each.key
  }
}