module "tf-vpc" {
  source = "../../modules/main-vpc"
  environment = "DEV"
  }

output "test" {
  value = module.tf-vpc.vpc_cidr
}