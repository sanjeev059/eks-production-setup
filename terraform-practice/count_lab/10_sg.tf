resource "aws_security_group" "practice_sg" {
  count       = 10

  name        = "practice-security-group-${count.index + 1}"
  description = "Practice security group ${count.index + 1}"
  vpc_id      = aws_vpc.practice_vpc.id

  ingress {
    description = "HTTP"
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = {
    Name = "practice-security-group-${count.index + 1}"
  }
}
