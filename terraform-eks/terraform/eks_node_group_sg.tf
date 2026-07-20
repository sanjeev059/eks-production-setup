resource "aws_security_group" "eks_nodes" {
  name        = "eks-node-sg"
  description = "Security group for EKS Worker Nodes"
  vpc_id      = aws_vpc.main.id

  tags = merge(
    local.common_tags,
    {
      Name = "eks-node-sg"
    }
  )
}