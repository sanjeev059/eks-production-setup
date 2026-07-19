Problem 12 – EC2 + ENI (Elastic Network Interface)
Requirement

Create:

3 Network Interfaces
3 EC2 Instances
Rules
EC2-1 should use NetworkInterface-1.
EC2-2 should use NetworkInterface-2.
EC2-3 should use NetworkInterface-3.
Resources
aws_network_interface
aws_instance

resource "aws_instance" "EC2"{
    count = 3
    ami = var.ami
    instance_type = var.instance_type

    tags = {
        Name = "EC2-${count.index + 1}"
    }
}
resource "aws_network_interface" "EC2_interface" {
  count = 3
  subnet_id       = aws_subnet.public_a.id
  security_groups = [aws_security_group.web.id]

  attachment {
    instance     = aws_instance.EC2[count.index].id
    device_index         = 0
  }

  tags = {
    Name = "EC2_interface-${count.index + 1}"
  }
}