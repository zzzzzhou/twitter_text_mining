import boto3
import os
s3 = boto3.client('s3', aws_access_key_id='AKIAQKRHIHI6MNEUI4OZ', aws_secret_access_key='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')
s3.upload_file(
    Filename="new_cosmetics_brand.csv",
    Bucket="cosmetics-tweets",
    Key="new_cosmetics_brand.csv")
