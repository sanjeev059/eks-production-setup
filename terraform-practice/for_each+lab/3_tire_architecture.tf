                    Internet
                        │
                  Application LB
                        │
                 Target Group
                        │
          ┌─────────────┴─────────────┐
          │                           │
        Web-1                      Web-2
          │                           │
          └─────────────┬─────────────┘
                        │
                     App Server
                        │
                     RDS Database


Requirements
Web Tier

Create 2 EC2 instances

web1 = {
    ami = "ami-web"
    instance_type = "t2.micro"
}

web2 = {
    ami = "ami-web"
    instance_type = "t2.micro"
}
App Tier

Create 1 EC2

app = {
    ami = "ami-app"
    instance_type = "t3.micro"
}
Database

Create 1 RDS instance

Load Balancer

Create 1 ALB

Target Group

Create 1 Target Group

Register only the Web Servers

The Target Group should contain:

web1

web2