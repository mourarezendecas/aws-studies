import sys
import os
from file_downloader.file_downloader import FileDownloader
from s3.s3_client import save_file
from sqs_client import send_message, generate_message_body

QUEUE_NAME = os.getenv('QUEUE_NAME')

if __name__ == "__main__":
    print("Iniciando processo de download de arquivo...")
    url_download = sys.argv[1]

    file_downloader = FileDownloader(url=url_download)

    response_file = file_downloader.download_image()
    content_file = response_file.content
    filename_download = file_downloader.get_filename(response_file)
    mimetype = file_downloader.get_mimetype(filename_download)

    print("Iniciando processo armazenamento do arquivo...")

    s3_path = save_file(content_file, filename_download, mimetype)

    print("Iniciando processo de envio de mensagem...")

    print(f"Enviando a mensagem com a url do s3: {s3_path} para o SQS...")
    message = generate_message_body(s3_path)

    response = send_message(
        queue_name=QUEUE_NAME,
        message_body=message
    )