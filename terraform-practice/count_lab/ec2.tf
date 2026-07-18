resource "aws_instance" "web_server" {

  ami                    = var.ami
  instance_type          = var.instance_type

  subnet_id              = aws_subnet.public_subnet.id

  vpc_security_group_ids = [aws_security_group.web_sg.id]

  user_data = file("${path.module}/userdata.sh")

  tags = {
    Name = "web_server"
  }
}