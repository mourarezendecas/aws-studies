import os
from io import BytesIO
from aws_services_common.aws_services import AWSConnection

BUCKET_NAME = os.getenv('BUCKET_NAME')
aws_services = AWSConnection() 
s3_client = aws_services.get_client('s3')

def save_file(content, file_name, mimetype):
    extra_args = {
        'ContentType': mimetype
    }

    file_object = BytesIO(content)

    s3_client.upload_fileobj(
        file_object,
        BUCKET_NAME,
        file_name,
        ExtraArgs=extra_args
    )

    print(f"Upload de bytes concluído com sucesso para 's3://{BUCKET_NAME}/{file_name}'")

    return f's3://{BUCKET_NAME}/{file_name}'