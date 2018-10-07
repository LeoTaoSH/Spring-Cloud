# Packer usage
packer validate example.json
packer build \
    -var 'aws_access_key=YOUR ACCESS KEY' \
    -var 'aws_secret_key=YOUR SECRET KEY' \
    example.json
packer build -only=amazon-ebs example.json
