resource "aws_route" "private" {

  for_each = aws_route_table.private

  route_table_id = each.value.id

  destination_cidr_block = "0.0.0.0/0"

  nat_gateway_id = aws_nat_gateway.main[
    replace(each.key, "private", "public")
  ].id
}