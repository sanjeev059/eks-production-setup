resource "aws_s3_bucket" "bucket" {
    count = 5
    bucket = "company-dev-${count.index+1}"

    tags = {
        Name = "company-dev-${count.index+1}"
    }
}