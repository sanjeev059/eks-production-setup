resource "aws_nat_gateway" "main" {
  allocation_id = aws_eip.nat.id

  subnet_id = aws_subnet.public["public-a"].id

  tags = merge(
    local.common_tags,
    {
      Name = "eks-nat"
    }
  )

  depends_on = [
    aws_internet_gateway.gw
  ]
}