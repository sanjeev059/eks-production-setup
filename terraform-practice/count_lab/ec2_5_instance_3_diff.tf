Create 5 EC2 instances.

Rules:

First 3 instances:
Instance type = t2.micro
Last 2 instances:
Instance type = t3.micro

All should use:
var.ami
Same subnet
Same Security Group

resource "aws_instance" "diff_instance" {
    count = 5
    ami  = var.ami
    instance_type = count.index < 3 ? "t2.micro" : "t3.micro"

    subnet_id = aws_subnet.public_subnet.id
    vpc_security_group_ids = [
        aws_security_group.web_sg.id
    ]

    tags = {
        Name = "Server-${count.index + 1}"
    }
}

