module "tf-vpc" {
  source = "../../modules/main-vpc"
  environment = "PROD"
  }

output "test" {
  value = module.tf-vpc.vpc_cidr
}