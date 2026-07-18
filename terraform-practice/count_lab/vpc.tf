resource "aws_vpc" "practice_vpc"{
    cidr_block = var.aws_vpc_cidr_block
    enable_dns_support = true
    enable_dns_hostnames = true

    tags = {
        Name = "practice_vpc"
    }
}