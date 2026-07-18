#!/bin/bash

yum update -y

amazon-linux-extras install nginx1 -y

yum install -y nginx

systemctl enable nginx

systemctl start nginx