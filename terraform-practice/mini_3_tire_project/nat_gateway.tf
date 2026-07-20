resource "aws_nat_gateway" "main" {

  for_each = aws_subnet.main

  allocation_id = aws_eip.nat[each.key].id

  subnet_id = each.value.id

  tags = {
    Name = "${each.key}-nat"
  }

  depends_on = [
    aws_internet_gateway.gw
  ]
}