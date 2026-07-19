Problem 11 - EC2 + Elastic IP
Requirement
Create:
4 EC2 instances
4 Elastic IPs
Rules:
EC2-1 → EIP-1
EC2-2 → EIP-2
EC2-3 → EIP-3
EC2-4 → EIP-4
Resources you'll need:
aws_instance
aws_eip

resource "aws_instance" "example"{
    count = 4
    ami = var.ami
    instance_type = var.instance_type


}

resource "aws_eip" "lb" {
  count = 4
  instance = aws_instance.example[count.index].id
  
}
