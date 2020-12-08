provider "aws" {
  region = "us-east-1"
}


locals {
  my-instance-name = "EC2-2193"
  my-instance-type = "t2.micro"
}
resource "aws_instance" "tf-example-ec2" {
  ami           = local.my-instance-type
  instance_type = var.ec2-type
  # count = 3
  key_name = "aws_key"
  tags = {
    "Name" = local.my-instance-name
  }
}

resource "aws_s3_bucket" "tf-s3" {
  bucket = var.s3-bucket-name
  acl    = "private"
}


output "tf-pi-output" {
  value = aws_instance.tf-example-ec2.public_ip
}

output "tf-example-private-ip" {
  value = aws_instance.tf-example-ec2.private_ip
}

output "tf-s3-meta" {
  value = aws_s3_bucket.tf-s3
}