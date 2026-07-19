Your company has 3 public-facing servers.

Each server needs:

One EC2 instance
One Elastic IP

Each Elastic IP must be associated with its own EC2 instance.

variable "servers" {

  default = {

    web = {
      ami           = "ami-web123"
      instance_type = "t2.micro"
    }

    app = {
      ami           = "ami-app123"
      instance_type = "t3.micro"
    }

    bastion = {
      ami           = "ami-bastion123"
      instance_type = "t3.small"
    }

  }

}   

resource "aws_instance" "example" {
    for_each = servers
    ami = each.value.ami
    instance_type = each.value.instance_type

    tags = "{
        Name = each.key
    }
}

resource "aws_eip" "lb" {
  for_each = var.servers
  instance = aws_instance.example[each.key].id
  domain   = "vpc"
}
resource "aws_eip_association" "eip_assoc" {
  for_each = var.servers
  instance_id   = aws_instance.example[each.key].id
  allocation_id = aws_eip.lb[each.key].id
}