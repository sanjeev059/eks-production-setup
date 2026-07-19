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

    db = {
      ami           = "ami-db123"
      instance_type = "t3.small"
    }

  }

}

resource "aws_instance" "exmaple"{
    for_each = var.servers

    ami = each.value.ami
    instance_type = each.value.instance_type

    subnet_id = aws_subnet.public_subnet.id
    security_group = [
        aws_vpc.practice_vpc.id
    ]

}