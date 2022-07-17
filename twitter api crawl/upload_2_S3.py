import boto3
import os
s3 = boto3.client('s3', aws_access_key_id='', aws_secret_access_key='')
s3.upload_file(
    Filename="new_cosmetics_brand.csv",
    Bucket="cosmetics-tweets",
    Key="new_cosmetics_brand.csv")
