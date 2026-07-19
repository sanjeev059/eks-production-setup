Requirement

Create 3 EC2 instances with different instance types.

Variable:

variable "servers" {
  default = {
    web = "t2.micro"
    app = "t3.micro"
    db  = "t3.small"
  }
}

Also assume:

variable "ami" {
  default = "ami-123456"
}
Requirements
Use for_each
Use the map directly (no toset())
EC2 name should be:
web
app
db

resource "aws_instance" "example" {

  for_each = var.servers

  ami           = var.ami
  instance_type = each.value

  tags = {
    Name = each.key
  }
}