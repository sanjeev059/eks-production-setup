# 🔧 EKS Production Setup

![AWS](https://img.shields.io/badge/AWS-232F3E?style=flat&logo=amazonaws&logoColor=white)
![Terraform](https://img.shields.io/badge/Terraform-7B42BC?style=flat&logo=terraform&logoColor=white)
![Kubernetes](https://img.shields.io/badge/Kubernetes-326CE5?style=flat&logo=kubernetes&logoColor=white)
![Jenkins](https://img.shields.io/badge/Jenkins-D24939?style=flat&logo=jenkins&logoColor=white)

A production-grade AWS EKS cluster setup using Terraform — multi-AZ, autoscaling, CloudWatch monitoring, and Jenkins CI/CD pipeline. Built from real-world experience deploying MyJio, JioCinema, and JioTalkies at Reliance Jio.

---

## 🏗️ Architecture

```
                          ┌─────────────────────────────────┐
                          │         AWS Cloud (ap-south-1)  │
                          │                                  │
                          │   ┌─────────┐  ┌─────────┐      │
          Internet ───────┼──▶│   ALB   │  │Route 53 │      │
                          │   └────┬────┘  └─────────┘      │
                          │        │                         │
                          │   ┌────▼────────────────────┐   │
                          │   │        VPC               │   │
                          │   │  ┌──────────────────┐   │   │
                          │   │  │  EKS Cluster     │   │   │
                          │   │  │  ┌────┐ ┌────┐   │   │   │
                          │   │  │  │ AZ1│ │ AZ2│   │   │   │
                          │   │  │  └────┘ └────┘   │   │   │
                          │   │  └──────────────────┘   │   │
                          │   │  ┌──────┐  ┌─────────┐  │   │
                          │   │  │  RDS │  │CloudWatch│  │   │
                          │   │  └──────┘  └─────────┘  │   │
                          │   └─────────────────────────┘   │
                          └─────────────────────────────────┘
```

---

## ✨ Features

- **Multi-AZ EKS cluster** — worker nodes spread across 2 availability zones
- **Terraform IaC** — 100% infrastructure as code, no manual clicks
- **Auto Scaling** — HPA + Cluster Autoscaler for dynamic workload handling
- **Jenkins CI/CD** — automated build, test, and deploy pipeline
- **CloudWatch monitoring** — metrics, logs, and alarms for production observability
- **IAM least privilege** — scoped roles for nodes, pods, and CI/CD
- **Private subnets** — worker nodes not exposed to internet directly
- **ALB Ingress** — AWS Load Balancer Controller for traffic routing

---

## 📁 Project Structure

```
eks-production-setup/
├── terraform/
│   ├── main.tf          # Provider config, backend
│   ├── vpc.tf           # VPC, subnets, NAT gateway
│   ├── eks.tf           # EKS cluster + node groups
│   ├── monitoring.tf    # CloudWatch dashboards + alarms
│   ├── variables.tf     # Input variables
│   └── outputs.tf       # Output values
├── kubernetes/
│   ├── deployment.yaml  # Sample app deployment
│   ├── service.yaml     # ClusterIP + ALB service
│   └── hpa.yaml         # Horizontal pod autoscaler
├── jenkins/
│   └── Jenkinsfile      # Full CI/CD pipeline
├── docs/
│   └── architecture.md  # Detailed architecture decisions
└── .github/
    └── workflows/
        └── ci.yml       # GitHub Actions lint + validate
```

---

## 🚀 Quick Start

### Prerequisites
- AWS CLI configured (`aws configure`)
- Terraform >= 1.5
- kubectl installed
- AWS account with sufficient permissions

### Deploy

```bash
# Clone the repo
git clone https://github.com/sanjeev059/eks-production-setup
cd eks-production-setup/terraform

# Initialise Terraform
terraform init

# Review what will be created
terraform plan

# Deploy (takes ~15 minutes)
terraform apply
```

### Connect to cluster

```bash
# Update kubeconfig
aws eks update-kubeconfig --name eks-production --region ap-south-1

# Verify nodes are ready
kubectl get nodes

# Deploy sample app
kubectl apply -f ../kubernetes/
```

---

## ⚙️ Configuration

Edit `terraform/variables.tf` to customise:

```hcl
variable "cluster_name"    { default = "eks-production" }
variable "region"          { default = "ap-south-1" }
variable "node_count_min"  { default = 2 }
variable "node_count_max"  { default = 10 }
variable "instance_type"   { default = "t3.medium" }
```

---

## 📊 Monitoring

CloudWatch dashboards included for:
- Node CPU and memory utilisation
- Pod restart counts
- ALB request count and latency
- Custom application metrics

---

## 🔒 Security

- Worker nodes in private subnets only
- NAT Gateway for outbound internet access
- IAM roles with least privilege per service
- Secrets managed via AWS Secrets Manager
- Pod Security Standards enforced

---

## 💡 Lessons from Jio Production

This setup is inspired by real patterns used to run MyJio and JioCinema on AWS EKS:
- Always use multi-AZ — single AZ failures happen
- HPA alone is not enough — Cluster Autoscaler handles node-level scaling
- CloudWatch log groups need retention policies — costs blow up without them
- IAM roles for service accounts (IRSA) — never use node-level IAM for pod permissions

---

## 📄 License

MIT

---

*Part of my AI/MLOps portfolio — [github.com/sanjeev059](https://github.com/sanjeev059)*
