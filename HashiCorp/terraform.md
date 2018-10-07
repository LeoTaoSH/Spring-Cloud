# terraform get started
- Build infrastructure
```
aws.tf file configuration
provider "aws" {
  access_key = "ACCESS_KEY_HERE"
  secret_key = "SECRET_KEY_HERE"
  region     = "us-east-1"
}

resource "aws_instance" "example" {
  ami           = "ami-2757f631"
  instance_type = "t2.micro"
}
```
1), Initialization 
terraform init
2), Apply Changes
terraform apply
3), Inspect
terraform show
4), Destory
terraform destroy



