# 🎬 Global Video Streaming Platform on AWS using Terraform & Amazon EKS

![AWS](https://img.shields.io/badge/AWS-232F3E?style=flat&logo=amazonaws&logoColor=white)
![Terraform](https://img.shields.io/badge/Terraform-7B42BC?style=flat&logo=terraform&logoColor=white)
![Kubernetes](https://img.shields.io/badge/Kubernetes-326CE5?style=flat&logo=kubernetes&logoColor=white)
![Jenkins](https://img.shields.io/badge/Jenkins-D24939?style=flat&logo=jenkins&logoColor=white)

---

# 📌 Overview

This repository demonstrates the design and implementation of a **production-inspired global video streaming platform** built on **Amazon Web Services (AWS)** using **Terraform**, **Amazon EKS**, and Kubernetes.

The objective is to design a cloud platform capable of supporting **15 million concurrent users globally** while following modern Platform Engineering and Infrastructure as Code (IaC) best practices.

The project is being built incrementally, with each infrastructure component designed, implemented, documented, and validated.

---

# 🎯 Business Problem

A media company expects its video streaming platform to grow to **15 million concurrent users worldwide** within the next six months.

The platform must provide:

- Global low latency
- High availability
- Zero downtime deployments
- Automatic scaling
- Secure infrastructure
- Disaster recovery
- Infrastructure as Code

---

# ✅ Functional Requirements

- User Authentication
- User Management
- Video Upload
- Video Streaming
- Search
- Recommendation Engine
- Billing
- Notifications

---

# ✅ Non Functional Requirements

- 15 Million Concurrent Users
- 99.99% Availability
- Multi Availability Zone Deployment
- Global Content Delivery
- Fault Tolerant
- Low Latency
- Secure Secret Management
- Infrastructure as Code
- Automatic Scaling

---

# 🏗️ High Level Architecture

```
                    Global Users
                          │
                     Amazon Route53
                          │
                   AWS WAF + Shield
                          │
                    Amazon CloudFront
                          │
               Application Load Balancer
                          │
          AWS Load Balancer Controller
                          │
                  Amazon EKS Cluster
        ┌─────────────────────────────────────┐
        │ Authentication Service              │
        │ User Service                        │
        │ Video Metadata Service              │
        │ Billing Service                     │
        │ Notification Service                │
        │ Search Service                      │
        │ Recommendation Service              │
        └─────────────────────────────────────┘
                │          │          │
             Redis      Aurora      Vault
                │
        Video Processing Workers
                │
             Amazon S3
                │
          Amazon CloudFront
```

---

# ☁️ AWS Services

| Service | Purpose |
|----------|---------|
| Amazon VPC | Isolated Network |
| Public Subnets | ALB, NAT Gateway |
| Private Subnets | Amazon EKS Worker Nodes |
| Internet Gateway | Internet Access |
| NAT Gateway | Outbound Internet Access |
| Route Tables | Traffic Routing |
| Security Groups | Network Security |
| IAM | Identity & Access Management |
| Amazon EKS | Kubernetes Platform |
| Amazon ECR | Docker Image Repository |
| Amazon S3 | Video Storage |
| Amazon CloudFront | Global Content Delivery |
| Amazon Route53 | DNS |
| AWS WAF | Web Application Firewall |
| Amazon Aurora PostgreSQL | Metadata Database |
| Amazon ElastiCache Redis | Application Cache |
| CloudWatch | Monitoring |
| HashiCorp Vault | Secrets Management |

---

# 📁 Repository Structure

```
eks-production-setup/

├── architecture/
├── terraform/
│   ├── backend/
│   ├── environments/
│   └── modules/
├── kubernetes/
├── docs/
└── README.md
```

---

# 🚀 Infrastructure Components

- Terraform Backend
- Amazon VPC
- Public & Private Subnets
- Internet Gateway
- NAT Gateway
- Route Tables
- Security Groups
- IAM
- Amazon EKS
- Managed Node Groups
- Amazon ECR
- Amazon S3
- CloudFront
- Route53
- AWS WAF
- Aurora PostgreSQL
- Redis

---

# ☸️ Kubernetes Components

- Deployments
- Services
- Ingress
- ConfigMaps
- Vault Integration
- Horizontal Pod Autoscaler
- AWS Load Balancer Controller

---

# 🔄 CI/CD Pipeline

```
Developer

↓

GitHub

↓

Jenkins

↓

Docker Build

↓

Amazon ECR

↓

Terraform

↓

Amazon EKS

↓

Rolling Deployment
```

---

# 📊 Monitoring & Logging

- Prometheus
- Grafana
- Fluent Bit
- Amazon CloudWatch
- AlertManager

---

# 🔐 Security

- Worker Nodes in Private Subnets
- Security Groups
- IAM Least Privilege
- IAM Roles for Service Accounts (IRSA)
- TLS Encryption
- HashiCorp Vault
- Kubernetes RBAC

---

# 📈 Scalability Strategy

The platform is designed to support **15 million concurrent users** using:

- Amazon CloudFront edge caching
- Horizontal Pod Autoscaler
- Cluster Autoscaler
- Stateless Microservices
- Amazon S3 Object Storage
- Aurora Read Replicas
- Redis Caching
- Multi Availability Zone Deployment

---

# 📚 Documentation

Additional documentation is available in the `architecture` directory.

- Architecture Overview
- Request Flow
- Deployment Flow
- Failure Scenarios
- Design Decisions

---

# 🛣️ Project Roadmap

- [x] Project Structure
- [x] Architecture Design
- [ ] Terraform Backend
- [ ] VPC & Networking
- [ ] Security Groups
- [ ] IAM
- [ ] Amazon EKS
- [ ] Managed Node Groups
- [ ] Amazon ECR
- [ ] Amazon S3
- [ ] CloudFront
- [ ] Route53
- [ ] AWS WAF
- [ ] Aurora PostgreSQL
- [ ] Redis
- [ ] Vault Integration
- [ ] Jenkins CI/CD
- [ ] Monitoring Stack
- [ ] Production Deployment

---

# 🎯 Learning Objectives

This project demonstrates practical implementation of:

- Terraform
- Amazon Web Services
- Amazon EKS
- Kubernetes
- Infrastructure as Code
- Platform Engineering
- Cloud Architecture
- High Availability
- Disaster Recovery
- System Design

---

# 👨‍💻 Author

**Sanjeev Desai**

Senior DevOps Engineer

This repository is maintained as part of continuous learning, production architecture practice, and cloud platform engineering.
