provider "aws" {
  access_key = ""
  secret_key = ""
  region     = "us-east-1"
}

resource "aws_instance" "appserver" {
  ami           = "ami-2757f631"
  instance_type = "t2.micro"
}
