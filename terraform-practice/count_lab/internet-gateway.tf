resource "aws_internet_gateway" "my_gw" {
  vpc_id = aws_vpc.practice_vpc.id
  tags = {
    Name = "my_gw"
  }
}