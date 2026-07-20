############################################
# Application Load Balancer
############################################

resource "aws_lb" "main" {

  name               = "main-alb"
  internal           = false
  load_balancer_type = "application"

  security_groups = [
    aws_security_group.alb.id
  ]

  subnets = [
    for subnet in aws_subnet.main : subnet.id
  ]

  tags = {
    Name = "main-alb"
  }
}

############################################
# Target Group
############################################

resource "aws_lb_target_group" "app" {

  name     = "app-target-group"
  port     = 80
  protocol = "HTTP"

  vpc_id = aws_vpc.main_vpc.id

  health_check {

    path = "/"

    protocol = "HTTP"

    healthy_threshold = 2

    unhealthy_threshold = 2

    timeout = 5

    interval = 30

    matcher = "200"
  }

  tags = {
    Name = "app-target-group"
  }
}

############################################
# Listener
############################################

resource "aws_lb_listener" "http" {

  load_balancer_arn = aws_lb.main.arn

  port = 80

  protocol = "HTTP"

  default_action {

    type = "forward"

    target_group_arn = aws_lb_target_group.app.arn
  }
}

############################################
# Attach EC2 to Target Group
############################################

resource "aws_lb_target_group_attachment" "app" {

  for_each = aws_instance.app

  target_group_arn = aws_lb_target_group.app.arn

  target_id = each.value.id

  port = 80
}