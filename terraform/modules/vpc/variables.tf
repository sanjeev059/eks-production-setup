variable "project_name" {
  description = "Project name used for naming AWS resources"
  type        = string
  default     = "video-streaming"
}

variable "environment" {
  description = "Deployment environment (dev, qa, stage, prod)"
  type        = string
  default     = "dev"

  validation {
    condition = contains(
      ["dev", "qa", "stage", "prod"],
      var.environment
    )
    error_message = "Environment must be dev, qa, stage or prod."
  }
}

variable "vpc_cidr"{
    description = "CIDR block for the VPC"
    type    = string
    default = "10.0.0.0/16"
}

variable "availability_zones"{
    description =  "List of Availability Zones for the VPC deployment"
    type        = list(string)
    default = [
        "ap-south-1a",
        "ap-south-1b"
    ]
}


variable "public_subnets" {
  description = "Public subnet CIDRs"

  type = map(string)

  default = {
    public_az1 = "10.0.1.0/24"
    public_az2 = "10.0.2.0/24"
  }
}

variable "private_subnets" {
  description = "private subnet CIDRs"

  type = map(string)

  default = {
    private_az1 = "10.0.11.0/24"
    private_az2 = "10.0.12.0/24"
  }
}

variable "database_subnets" {
  description = "database subnet CIDRs"

  type = map(string)

  default = {
    database_az1 = "10.0.21.0/24"
    database_az2 = "10.0.22.0/24"
  }
}

variable "common_tags" {
  description = "Common tags applied to all AWS resources"

  type = map(string)

  default = {
    Project     = "video-streaming"
    Environment = "dev"
    ManagedBy   = "Terraform"
  }
}