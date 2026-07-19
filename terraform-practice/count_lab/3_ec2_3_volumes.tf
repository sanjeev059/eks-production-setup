🚀 Problem 10 (One of the Most Asked)

Create:

3 EC2 instances
3 EBS volumes

Rules:

EC2-1 gets EBS-1
EC2-2 gets EBS-2
EC2-3 gets EBS-3

In Terraform this means you'll create:

aws_instance
aws_ebs_volume
aws_volume_attachment

The important part is using the same count.index to connect each volume to its matching instance.

This is one of the most common interview questions because it tests whether you understand how to relate multiple resources created with count.

resource "aws_instance" "example_instance"{
    count = 3
    ami = var.ami
    instance_type = var.instance_type
    subnet_id = aws_subnet.public_subnet.id
    vpc_security_group_ids = [aws_security_group.web_sg.id]

}

resource "aws_ebs_volume" "example" {
  count = 3
  availability_zone = "us-east-1a"
  size              = 20

  tags = {
    Name = "example-${count.index}"
  }
}

resource "aws_volume_attachment" "ebs_att" {
  count = 3
  device_name = "/dev/sdh"
  volume_id   = aws_ebs_volume.example[count.index].id
  instance_id = aws_instance.example_instance[count.index].id
  }