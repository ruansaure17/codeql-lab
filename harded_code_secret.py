import boto3

AWS_ACCESS_KEY = "AKIA123456789SECRET"
AWS_SECRET_KEY = "SUPER_SECRET_KEY_EXAMPLE"

s3 = boto3.client(
    "s3",
    aws_access_key_id=AWS_ACCESS_KEY,
    aws_secret_access_key=AWS_SECRET_KEY
)

print("Conectado")