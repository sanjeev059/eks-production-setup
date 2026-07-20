resource "aws_instance" "app" {

  for_each = aws_subnet.private

  ami           = data.aws_ami.amazon_linux.id
  instance_type = var.instance_type

  subnet_id = each.value.id

  vpc_security_group_ids = [
    aws_security_group.app.id
  ]

  associate_public_ip_address = false

  user_data = file("${path.module}/userdata.sh")

  tags = {
    Name = each.key
  }
}