resource "aws_route_table" "my_routes" {
  vpc_id = aws_vpc.practice_vpc.id
  
  tags = {
    Name = "my_routes"
  }
}