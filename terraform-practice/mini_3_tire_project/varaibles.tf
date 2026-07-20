variable "vpc_cidr" {
  type = string
}

variable "aws_region" {
  type = string
}

variable "public_subnets" {
  default = {
    public-1 = {
      cidr = "10.0.1.0/24"
      az   = "us-east-1a"
    }

    public-2 = {
      cidr = "10.0.2.0/24"
      az   = "us-east-1b"
    }
  }
}

variable "private_subnets" {
  default = {
    private-1 = {
      cidr = "10.0.11.0/24"
      az   = "us-east-1a"
    }

    private-2 = {
      cidr = "10.0.12.0/24"
      az   = "us-east-1b"
    }
  }
}


variable "instance_type" {
  type = string
}