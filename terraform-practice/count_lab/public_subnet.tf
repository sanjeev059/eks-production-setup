resource "aws_subnet" "public_subnet" {
  vpc_id     = aws_vpc.practice_vpc.id
  cidr_block = var.public_subnet
  availability_zone = var.public_subnet_az
  map_public_ip_on_launch = true

  tags = {
    Name = "public_subnet"
  }
}