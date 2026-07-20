resource "aws_subnet" "private" {

  for_each = var.private_subnets
  vpc_id   = aws_vpc.main_vpc.id

  cidr_block        = each.value.cidr
  availability_zone = each.value.az

  tags = {
    Name = each.key
  }
}