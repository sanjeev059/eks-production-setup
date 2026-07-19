resource "aws_ebs_volume" "example" {
  count = 10
  availability_zone = "us-east-1a"
  size              = 20
  type              = "gp3"

  tags = {
    Name = "EBS-${count.index + 1}
  }
}