terraform {
  backend "s3" {
    bucket         = "sanjeev-eks-tfstate-926909118267-tac-interview"
    key            = "video-streaming-platform/dev/terraform.tfstate"
    region         = "ap-south-1"
    encrypt        = true
    dynamodb_table = "terraform-locks"
  }
}