resource "aws_instance" "count_ec2"{
    count = 3
    ami = var.ami
    instance_type = var.instance_type
    subnet_id = aws_subnet.public_subnet.id
    vpc_security_group_ids = [aws_security_group.web_sg.id]

    tags = {
        Name = "web-${count.index + 1}"
    }
}