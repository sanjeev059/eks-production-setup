resource "aws_route_table" "example" {
  vpc_id = aws_vpc.main_vpc.id

  tags = {
    Name = "example"
  }
}