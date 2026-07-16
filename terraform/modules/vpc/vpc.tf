resource "aws_vpc" "main"{
    var.vpc_cidr
    enable_dns_support = true
    enable_dns_hostnames = true

    tags{
        var.common_tags-vpc
    }
}