You have this variable:

variable "users" {
  default = [
    "john",
    "alice",
    "bob"
  ]
}

Create 3 IAM users.

resource "aws_iam_user" "example" {
    for_each = toset(var.users)
    name = each.key
}