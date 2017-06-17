provider "aws" {
  access_key = "AKIAJEHLQTTZUAMEZVUQ"
  secret_key = "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"
  region     = "us-east-1"
}

resource "aws_instance" "appserver" {
  ami           = "ami-2757f631"
  instance_type = "t2.micro"
}
