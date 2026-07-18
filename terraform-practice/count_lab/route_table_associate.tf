resource "aws_route_table_association" "attach_route"{
    subnet_id      = aws_subnet.public_subnet.id
    route_table_id = aws_route_table.my_routes.id
}