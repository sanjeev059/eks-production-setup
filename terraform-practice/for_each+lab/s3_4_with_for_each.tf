🟢 Problem 2 (Slightly Harder)
Requirement

Create 4 S3 buckets.

Variable:

variable "buckets" {
  default = [
    "logs",
    "backup",
    "images",
    "documents"
  ]
}

Requirements:

Use for_each
Each bucket name should come from the variable.
Add a tag: Environment = Dev


resource "aws_s3_bucket" "example"{
    for_each = toset(var.buckets)
    bucket = each.key

    tags = {
        Environment = "Dev"
    }
}
