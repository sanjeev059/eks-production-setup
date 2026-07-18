                 15 Million Users
                        │
                    Route53
                        │
                AWS WAF + Shield
                        │
                 CloudFront CDN
                        │
          Application Load Balancer
                        │
      AWS Load Balancer Controller
                        │
                 Amazon EKS
        ┌───────────────────────────────┐
        │                               │
        │ Authentication Service        │
        │ User Service                  │
        │ Video Metadata Service        │
        │ Billing Service               │
        │ Notification Service          │
        │ Recommendation Service        │
        │ Search Service                │
        └───────────────────────────────┘
               │        │         │
               │        │         │
            Redis    Aurora      Vault
               │
               │
             Kafka
               │
        Video Processing
               │
          Amazon S3
               │
          CloudFront