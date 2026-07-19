Create 5 EC2 instances.

The AMIs should come from a list variable:

variable "amis" {
  default = [
    "ami-111",
    "ami-222",
    "ami-333",
    "ami-444",
    "ami-555"
  ]
}

Each instance should use a different AMI:

resource "aws_instance" "ami_diff_instance" {
    count = 5
    ami  = var.amis[count.index]
    instance_type = var.instance_type
    subnet_id = aws_subnet.public_subnet.id
    vpc_security_group_ids = [aws_security_group.web_sg.id]

    tags = {
        Name = "ami_diff_instance-${count.index + 1}"
    }
}