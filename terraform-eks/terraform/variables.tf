variable "cidr_block"{
    type = string
}

variable "region"{
    type = string
}

variable "private_subnets" {
  description = "Private subnets"

  type = map(object({
    cidr = string
    az   = string
  }))
}
variable "public_subnets" {
  description = "Public subnets"

  type = map(object({
    cidr = string
    az   = string
  }))
}