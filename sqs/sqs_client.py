import json
from datetime import datetime
from aws_services_common.aws_services import AWSConnection

aws_services = AWSConnection()
sqs_client = aws_services.get_resource('sqs')

def send_message(queue_name: str, message_body: dict):
    queue = sqs_client.get_queue_by_name(QueueName=queue_name)
    response = queue.send_message(MessageBody=message_body)
    return response

def generate_message_body(s3_path):
    message_body = {
        's3_path': s3_path,
        'sent_at': datetime.now().isoformat()
    }

    return json.dumps(message_body, ensure_ascii=False)