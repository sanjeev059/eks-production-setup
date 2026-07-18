resource "aws_route" "default_route" {
    route_table_id = aws_route_table.my_routes.id
    destination_cidr_block = "0.0.0.0/0"
    gateway_id = aws_internet_gateway.my_gw.id
}