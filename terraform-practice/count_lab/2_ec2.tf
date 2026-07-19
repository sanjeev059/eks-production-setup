resource "aws_instance" "dev"{
    count = 2
    ami = var.ami
    instance_type = var.instance_type
    subnet_id = aws_subnet.public_subnet.id
    vpc_security_group_ids = [var.aws_security_group.web_sg.id]

    tags = {
        Name = "dev-${count.index + 1}"
    }
}