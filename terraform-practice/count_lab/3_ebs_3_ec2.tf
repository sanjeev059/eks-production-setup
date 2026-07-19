⭐ Next Challenge (Production-Level)

This one is asked in senior DevOps interviews because it combines lists with resource relationships.

Requirement

Create:

3 EC2 instances
3 EBS volumes

Variable:

variable "ebs_config" {
  default = [
    {
      size = 20
      type = "gp3"
    },
    {
      size = 50
      type = "gp2"
    },
    {
      size = 100
      type = "io1"
    }
  ]
}

resource "aws_instance" "exmaple" {
    count = 3
    ami = var.ami
    instance_type = var.instances_type

}

resource "aws_ebs_volume" "ebs_vols" {
  count = 3
  availability_zone = "us-west-2a"
  size              =  var.ebs_config[count.index].size
  type              =  var.ebs_config[count.index].type

  tags = {
    Name = "example-${count.index + 1}"
  }
}