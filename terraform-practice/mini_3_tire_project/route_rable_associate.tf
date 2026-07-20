resource "aws_route_table_association" "public" {
  for_each       = aws_subnet.main
  subnet_id      = each.value.id
  route_table_id = aws_route_table.example.id
}