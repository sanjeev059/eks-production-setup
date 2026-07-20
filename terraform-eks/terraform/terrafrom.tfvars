region = "ap-south-1"
cidr_block = "10.0.0.0/16"

public_subnets = {
  public-a = { 
    cidr = "10.0.1.0/24"
    az   = "ap-south-1a"
  }

  public-b = {
    cidr = "10.0.2.0/24"
    az   = "ap-south-1b"
  }

  public-c = {
    cidr = "10.0.3.0/24"
    az   = "ap-south-1c"
  }
}

private_subnets = {
  private-a = {
    cidr = "10.0.101.0/24"
    az   = "ap-south-1a"
  }

  private-b = {
    cidr = "10.0.102.0/24"
    az   = "ap-south-1b"
  }

  private-c = {
    cidr = "10.0.103.0/24"
    az   = "ap-south-1c"
  }
}