1. Create EC2 instances

Each EC2 should use:

ami
instance_type

from the variable.

2. Create EBS volumes

Each EBS volume should use:

web → 20 GB

app → 50 GB

db → 100 GB
3. Attach the EBS volumes

Expected relationship:

web EC2  <------> web EBS

app EC2  <------> app EBS

db EC2   <------> db EBS

No cross attachments.

variable "servers" {

  default = {

    web = {
      ami           = "ami-web123"
      instance_type = "t2.micro"
      ebs_size      = 20
    }

    app = {
      ami           = "ami-app123"
      instance_type = "t3.micro"
      ebs_size      = 50
    }

    db = {
      ami           = "ami-db123"
      instance_type = "t3.small"
      ebs_size      = 100
    }

  }

}

resource "aws_instance" "example"{
    for_each = var.servers
    ami = each.value.ami
    instance_type = each.value.instance_type
}

resource "aws_ebs_volume" "example" {
  for_each = var.servers
  availability_zone = "us-west-2a"
  size              = each.value.ebs_size

  tags = {
    Name = "example"
  }
}

resource "aws_volume_attachment" "ebs_att" {
  device_name = "/dev/sdh"
  volume_id = aws_ebs_volume.example[each.key].id
  instance_id = aws_instance.example[each.key].id
}