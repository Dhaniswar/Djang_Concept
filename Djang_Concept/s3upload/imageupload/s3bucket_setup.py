import boto3
import requests
import os

# OBJECT_NAME_TO_UPLOAD = 'file_to_upload.jpg'

s3_client = boto3.client(
    's3',
    aws_access_key_id = os.environ["AWS_ACCESS_KEY"],
    aws_secret_access_key =os.environ["AWS_SECRET_KEY"]
)


class AWSSignedURL:
    @staticmethod
    def get(key):
        params = {'Bucket': os.environ["AWS_STORAGE_BUCKET_NAME"], 'Key': key}
        return s3_client.generate_presigned_url('get_object',
                                                Params= params,
                                                ExpiresIn = 50 )