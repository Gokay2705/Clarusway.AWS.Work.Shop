
variable "ec2-name" {
  default     = "TF-ec2"
  description = "name for new ec2"
}

variable "ec2-type" {
  default     = "t2.micro"
  description = "type for new ec2"
}

variable "ec2-ami" {
  default     = "ami-04d29b6f966df1537"
  description = "ami for new ec2"
}

variable "s3-bucket-name" {
  default     = "tf-s3-2193"
  description = "name for new s3 bucket"
}