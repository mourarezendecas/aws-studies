import boto3
import os
import json
from datetime import datetime

AWS_REGION = os.getenv('AWS_REGION')
AWS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
AWS_SECRET = os.getenv('AWS_SECRET_ACCESS_KEY')

client = boto3.resource(
    'sqs', 
    region_name = AWS_REGION,
    aws_access_key_id = AWS_KEY_ID,
    aws_secret_access_key = AWS_SECRET
)

def send_message(queue_name: str, message_body: dict):
    queue = client.get_queue_by_name(QueueName=queue_name)
    response = queue.send_message(MessageBody=message_body)
    return response

def generate_message_body(s3_path):
    message_body = {
        's3_path': s3_path,
        'sent_at': datetime.now().isoformat()
    }

    return json.dumps(message_body, ensure_ascii=False)