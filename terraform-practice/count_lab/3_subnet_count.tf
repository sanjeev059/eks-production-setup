Requirement

You have 3 public subnets.

variable "public_subnets" {
  default = [
    "subnet-111",
    "subnet-222",
    "subnet-333"
  ]
}

resource "aws_instance" "example_instance" {
    count = 3
    ami = var.ami
    instance_type = var.instance_type
    subnet_id = var.public_subnets[count.index]
    vpc_security_group_ids = [aws_security_group.web_sg.id] 

    tags = {
        Name = "example_instance-${count.index + 1}"
    }

}
Create 3 EC2 instances.