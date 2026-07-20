resource "aws_route_table" "private" {

  for_each = aws_subnet.private

  vpc_id = aws_vpc.main_vpc.id

  tags = {
    Name = "${each.key}-rt"
  }
}