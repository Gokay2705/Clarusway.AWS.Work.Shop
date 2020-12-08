provider "aws" {
    region  = "us-east-1"
}

resource "aws_instance" "tf-example-ec2" {
  ami           = "ami-04d29b6f966df1537"
  instance_type = "t2.micro"
  # count = 3
  key_name = "aws_key"
  tags = {
    "Name" = "TF-ec2"
  }
}

resource "aws_s3_bucket" "tf-s3" {
  bucket = "tf-s3-2193"
  acl = "private"
}

output "tf-pi-output" {
  value = aws_instance.tf-example-ec2.public_ip
}

output "tf-s3-meta" {
  value = aws_s3_bucket.tf-s3
}